"""Umbrella CI alignment guard for the algebra-1-tutor skill (build tooling, not shipped).

Composes four checks; exits non-zero if any fails:
  1. alignment        (generate.run_checks: SSOT <-> tables/.md/outline/JSON ids + staleness)
  2. notation invariant (check_notation.check)
  3. point-on-line lint (geometric witness + .md answer-key cross-check)
  4. code-grammar lint  (every JSON id matches the backward-compatible grammar)
"""
import glob, json, os, re, sys
import sympy as sp
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations,
                                        implicit_multiplication_application)

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
UNIT_MD = os.path.join(REPO_ROOT, "algebra-1-tutor", "references", "units")
TRANSFORMS = standard_transformations + (implicit_multiplication_application,)

# Backward-compatible id grammar (RESEARCH_REDTEAM_HANDOFF.md s5), restricted to the
# forms present in the answer-key JSON this phase:
#   standard : (1-12 | A) . lesson . [w|ex]index [part]  e.g. 5.5.6, 12.1.w1, 6.2.ex1, A.2.3, 8.2.5b
#   refresher: ref[AB] . index                           e.g. refA.4, refB.10
# (the 'w' worked-example and 'ex' example tags are the only alpha tag prefixes present this phase)
ID_RE = re.compile(r"^(?:(?:[1-9]|1[0-2]|A)\.\d+\.(?:w|ex)?\d+[a-z]?|ref[AB]\.\d+)\Z")


def _json_files():
    return sorted(glob.glob(os.path.join(HERE, "unit-*.json"))) + \
           sorted(glob.glob(os.path.join(HERE, "appendix*.json")))


def code_grammar_lint():
    """Return list of (file, id) for every id that violates the grammar."""
    bad = []
    for fp in _json_files():
        data = json.load(open(fp, encoding="utf-8"))
        for prob in data["problems"]:
            pid = prob.get("id", "")
            if not ID_RE.match(str(pid)):
                bad.append((os.path.basename(fp), pid))
    return bad


def _line_eq_template(prob):
    """True if this solve entry is a line-intercept problem: '<m>*<x0>+b=<y0>', var b."""
    return (prob.get("kind") == "solve" and prob.get("var") == "b"
            and re.match(r"^[^=]*\*[^=]*\+b=[^=]+$", prob.get("eq", "").replace(" ", "")))

def _eq_line(eq):
    """Parse a line-intercept eq '<m>*<x0>+b=<y0>' -> (m, x0, y0) as sympy, or None.

    This is an INDEPENDENT witness: the eq encodes the slope and the given point directly,
    which the on_line points alone cannot pin down for a two-point entry. Returns None when
    the string does not match the template (e.g. non-line solve entries).
    """
    s = eq.replace(" ", "")
    m = re.match(r"^(.*?)\*(.*?)\+b=(.+)$", s)
    if not m:
        return None
    try:
        return (sp.sympify(m.group(1), rational=True),
                sp.sympify(m.group(2), rational=True),
                sp.sympify(m.group(3), rational=True))
    except Exception:
        return None

def point_on_line_geometric(prob):
    """Geometric witness. Return [] if consistent, else [issue]. Requires on_line."""
    pid = prob.get("id", "<no-id>")
    pts = prob.get("on_line")
    if pts is None:
        return [f"{pid}: line-intercept entry missing required 'on_line' annotation"]
    pts = [(sp.Rational(str(x)), sp.Rational(str(y))) for x, y in pts]
    b = sp.Rational(str(prob["answer"]))
    if "slope" in prob:
        m = sp.Rational(str(prob["slope"]))
    else:
        if len(pts) < 2:
            return [f"{pid}: needs 'slope' (only one point and no slope given)"]
        (x1, y1), (x2, y2) = pts[0], pts[1]
        if x2 == x1:
            return [f"{pid}: vertical through given points — not y=mx+b"]
        m = (y2 - y1) / (x2 - x1)
    issues = []
    for (x, y) in pts:                       # every given point lies on y = m x + b
        if sp.simplify(m * x + b - y) != 0:
            issues.append(f"{pid}: point ({x},{y}) not on line y={m}x+{b}")
    if pts:                                  # derived intercept matches the stored answer
        x0, y0 = pts[0]
        if sp.simplify((y0 - m * x0) - b) != 0:
            issues.append(f"{pid}: derived intercept {y0 - m*x0} != answer {b}")
    # independent witness from the eq itself ('<m_eq>*<x0_eq>+b=<y0_eq>'): for a two-point
    # entry the line is otherwise fully determined by its own points (collinearity is then
    # tautological), so cross-check the eq's encoded slope and point against the derived line.
    eq_parsed = _eq_line(prob.get("eq", ""))
    if eq_parsed is not None:
        m_eq, x0_eq, y0_eq = eq_parsed
        if sp.simplify(m_eq - m) != 0:
            issues.append(f"{pid}: eq slope {m_eq} != line slope {m}")
        if sp.simplify(m * x0_eq + b - y0_eq) != 0:
            issues.append(f"{pid}: eq point ({x0_eq},{y0_eq}) not on line y={m}x+{b}")
    return issues


def _md_path_for(pid):
    scope = pid.split(".")[0]
    if scope == "A":
        return os.path.join(UNIT_MD, "appendix-statistics.md")
    hits = glob.glob(os.path.join(UNIT_MD, f"unit-{int(scope):02d}-*.md"))
    return hits[0] if hits else None

def _lesson_section(text, lesson_id, heading):
    """Return the text of `heading` block within the `## Lesson <lesson_id>:` section."""
    m = re.search(r"^##\s+Lesson\s+" + re.escape(lesson_id) + r":.*?$", text, re.M)
    if not m:
        return None
    start = m.end()
    nxt = re.search(r"^##\s+Lesson\s", text[start:], re.M)
    section = text[start: start + (nxt.start() if nxt else len(text))]
    h = re.search(r"\*\*" + re.escape(heading) + r"\*\*", section)
    if not h:
        return None
    rest = section[h.end():]
    end = re.search(r"(?m)^(?:\*\*[A-Z]|---|##\s)", rest)   # next bold label / rule / heading
    return rest[: end.start() if end else len(rest)]

def _segment_for_index(block, idx, line_start=False):
    """Within a numbered block, return the segment for item number `idx`.

    Practice answer keys are one '·'-separated line (split on inline ' N. '); worked-example
    blocks are multi-line with items at line starts (split on '^N. ' so a mid-line number like
    '= 3. Then' in the prose is not mistaken for an item boundary).
    """
    pat = r"(?m)^(\d+)\.\s" if line_start else r"(?:^|\s)(\d+)\.\s"
    parts = re.split(pat, block)
    # parts = [pre, '1', seg1, '2', seg2, ...]
    for i in range(1, len(parts) - 1, 2):
        if parts[i] == str(idx):
            return parts[i + 1]
    return None

def _last_line_eq(segment):
    """Parse the last 'y = <rhs>' in a numbered answer-key segment -> (m, b), or None.

    Handles implicit multiplication ('3x'), '=>'/'⇒' derivation chains (take the FINAL
    'y = ...'), and item separators ('·'). Returns None if no clean linear 'y = rhs' is found.
    """
    if not segment:
        return None
    s = segment
    for tok in ("\\;", "\\,", "\\Rightarrow", "\\rightarrow", "\\to", "$$", "$"):
        s = s.replace(tok, " ")
    s = s.replace("⇒", " ").replace("→", " ")
    hits = list(re.finditer(r"y\s*=\s*", s))
    if not hits:
        return None
    rhs = re.split(r"[·\n]", s[hits[-1].end():])[0].strip().rstrip(". ")
    if not rhs or "=" in rhs:                 # grabbed a non-final eq -> reject
        return None
    x = sp.Symbol("x")
    try:
        e = parse_expr(rhs.replace("^", "**"), local_dict={"x": x}, transformations=TRANSFORMS)
    except Exception:
        return None
    poly = sp.Poly(sp.expand(e), x)
    if poly.degree() > 1:
        return None
    return sp.Rational(poly.coeff_monomial(x)), sp.Rational(poly.coeff_monomial(1))

def point_on_line_md(prob):
    """`.md` cross-check for a line-intercept entry. [] if it matches, else [issue].

    Recovers the canonical line independently from the unit `.md`: the numbered
    '**Answer key:**' list for a practice entry, or the '**Worked examples:**' block for a
    worked-example (wN) entry (multi-line, items at line starts). This is the only witness that
    can catch a self-consistent-but-wrong entry, so it runs on worked examples too.
    """
    pid = str(prob["id"])
    if "on_line" not in prob:                 # geometric witness owns the missing-annotation error
        return []
    scope, lesson_n, tail = pid.split(".")
    lesson_id = f"{scope}.{lesson_n}"
    is_worked = tail.startswith("w")
    idx = int(re.search(r"\d+", tail).group())
    heading = "Worked examples:" if is_worked else "Answer key:"
    path = _md_path_for(pid)
    if not path:
        return [f"{pid}: no unit .md found"]
    block = _lesson_section(open(path, encoding="utf-8").read(), lesson_id, heading)
    seg = _segment_for_index(block, idx, line_start=is_worked) if block else None
    md = _last_line_eq(seg)
    if md is None:
        return [f"{pid}: no parseable 'y = ...' in .md {heading} item {idx}"]
    m_md, b_md = md
    b_json = sp.Rational(str(prob["answer"]))
    pts = prob["on_line"]
    if "slope" in prob:
        m_json = sp.Rational(str(prob["slope"]))
    elif len(pts) >= 2:                       # two points determine the slope
        (x1, y1), (x2, y2) = [(sp.Rational(str(a)), sp.Rational(str(c))) for a, c in pts[:2]]
        m_json = (y2 - y1) / (x2 - x1)
    else:                                     # one point and no slope: report, don't crash
        return [f"{pid}: needs 'slope' for .md cross-check (one point, no slope)"]
    if sp.simplify(m_md - m_json) != 0 or sp.simplify(b_md - b_json) != 0:
        return [f"{pid}: .md line y={m_md}x+{b_md} != JSON line y={m_json}x+{b_json}"]
    return []

def _load_problems(fp):
    return json.load(open(fp, encoding="utf-8"))

def point_on_line_lint():
    """Both witnesses (geometric + .md cross-check) on every line-intercept entry."""
    issues = []
    for fp in _json_files():
        for prob in _load_problems(fp)["problems"]:
            if _line_eq_template(prob):
                issues += point_on_line_geometric(prob)
                issues += point_on_line_md(prob)
    return issues


def main():
    sys.path.insert(0, HERE)
    import generate
    import check_notation
    failures = []
    a = generate.run_checks()
    if a:
        failures += [f"alignment: {i}" for i in a]
    n = check_notation.check()
    if n:
        failures += [f"notation: {i}" for i in n]
    p = point_on_line_lint()
    if p:
        failures += [f"point-on-line: {i}" for i in p]
    g = code_grammar_lint()
    if g:
        failures += [f"code-grammar: bad id {i}" for i in g]
    if failures:
        print("FAIL:\n  " + "\n  ".join(failures))
        return 1
    print("check_alignment: alignment + notation + point-on-line + code-grammar all green.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
