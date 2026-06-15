"""Drift guard for the student-facing textbook source (build tooling, not shipped).

The student textbook (`textbook-src/`) is a warm rewrite of the tutor lesson source
(`algebra-1-tutor/references/units/`). The PROSE differs by design; the SSOT-verified math must
NOT. The build does not cross-check the .md math against the JSON (verify_answers.py only checks the
JSON against itself; only line-intercept problems get a .md cross-check), so for the student copy
this script is the backstop. It fails if the student copy and the tutor source disagree on:

  * the set of build-emitted reference codes (definitions, transfer-checks, figures, AND the
    worked-example / practice codes the textbook build assigns by position),
  * the lesson set and order,
  * any answer-key values,

or if tutor-only meta or render-breaking notation leaks into the student copy.

Usage:
  python _verification/check_textbook_src.py        # every unit that exists in textbook-src/
  python _verification/check_textbook_src.py 1       # only unit 1 (scoped; for per-author review)
  python _verification/check_textbook_src.py A       # the statistics appendix
"""
import glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
TUTOR = os.path.join(REPO_ROOT, "algebra-1-tutor", "references", "units")
STUDENT = os.path.join(REPO_ROOT, "textbook-src")

ANCHOR_RE = re.compile(r"\{#([^}\s]+)\}")
LESSON_RE = re.compile(r"^##\s+Lesson\s+([0-9A]+\.\d+):", re.M)
ANSKEY_RE = re.compile(r"\*\*Answer key[^\n]*?\*\*")
# Inline tutor-meta that can sit inside an answer-key payload or a definition: an internal .md
# reference or a section mark. Stripped from BOTH sides before the value comparison (authors must
# also remove it from prose per §7).
_INLINE_META_RE = re.compile(r"(?:misconceptions|metaphors|pedagogy|visuals|curriculum-map|SKILL)\.md|§", re.I)

# Tutor-facing meta that must never reach a student book (case-insensitive). The person-words
# "a/the student" and "the tutor" are intentionally NOT listed: they legitimately appear in word
# problems ("each student is paired with one chair"), so flagging them false-positived on verbatim
# answer keys. Genuine tutor stage-direction leaks are caught by the adversarial review pass.
LEAK_RES = [re.compile(p, re.I) for p in [
    r"orientation for the tutor", r"\bSocratic", r"hint ladder", r"Progress Card", r"\binterleav",
    r"misconceptions\.md", r"metaphors\.md", r"pedagogy\.md", r"visuals\.md",
    r"curriculum-map\.md", r"SKILL\.md", r"AUTHOR_GUIDE",
    r"Teaching arc", r"Watch for:", r"Visuals to offer", r"\bTell:", r"\bRepair:",
    r"Hinge question", r"§",
]]


def _ssot_unit_ids():
    sys.path.insert(0, HERE)
    import generate
    return [u.id for u in generate.load_ssot().units]


def _tutor_path(uid):
    if uid == "A":
        return os.path.join(TUTOR, "appendix-statistics.md")
    hits = glob.glob(os.path.join(TUTOR, f"unit-{int(uid):02d}-*.md"))
    return hits[0] if hits else None


def _student_path(uid):
    if uid == "A":
        p = os.path.join(STUDENT, "appendix-statistics.md")
        return p if os.path.exists(p) else None
    hits = glob.glob(os.path.join(STUDENT, f"unit-{int(uid):02d}-*.md"))
    return hits[0] if hits else None


def _all_codes(text):
    """The full set of reference codes that will SHIP: the {#...} anchors already in the text, plus
    the worked-example/practice codes the textbook build injects by position. Reuses the build's own
    counter so this matches exactly what the generated site links to."""
    sys.path.insert(0, HERE)
    import build_textbook as tb
    return set(ANCHOR_RE.findall(tb._id_worked_practice(text)))


def _is_editorial_paren(inner):
    """True if a (...) holds editorial commentary rather than a math value: it carries tutor-meta,
    a decorative glyph, or any 3+ letter word (prose). Purely symbolic groups like (x+2), (3, 5),
    (2/3), or (b ≠ 0) have no 3-letter word and stay locked for the value comparison."""
    return bool(_INLINE_META_RE.search(inner) or re.search(r"[✓✗]", inner) or re.search(r"[A-Za-z]{3,}", inner))


def _answer_core(payload):
    """Reduce an answer-key payload to just its locked VALUES for comparison. Editorial content an
    author may legitimately reword or drop per §7 is removed from BOTH sides first: italic `*(…)*`
    asides anywhere, plain `(…)` parentheticals that are editorial (prose / meta / glyph), decorative
    ✓/✗ marks, and inline meta refs. Symbolic parentheses (factored forms, coordinates) are kept, so
    a real change to an answer value is still caught."""
    s = re.sub(r"</?em>", "", payload)
    s = re.sub(r"\*\(.*?\)\*", " ", s, flags=re.S)                        # italic asides anywhere (may hold inner parens)
    s = re.sub(r"\(([^()]*)\)", lambda m: " " if _is_editorial_paren(m.group(1)) else m.group(0), s)
    s = re.sub(r"[✓✗]", " ", s)                                           # decorative marks
    s = _INLINE_META_RE.sub(" ", s)                                       # residual refs
    s = re.sub(r"\s+", " ", s).strip()
    return re.sub(r"\s+([.,;:])", r"\1", s)                               # drop a space left before punctuation


def _answer_values(text):
    """lesson_id -> list of answer-key VALUE strings, one per '**Answer key...:**' block in that
    lesson, each reduced by _answer_core. The label and all editorial commentary are excluded, so an
    author may de-leak the label and reword or drop asides; the answer values themselves must match."""
    out = {}
    ls = list(LESSON_RE.finditer(text))
    for i, m in enumerate(ls):
        lid = m.group(1)
        start = m.end()
        end = ls[i + 1].start() if i + 1 < len(ls) else len(text)
        body = text[start:end]
        vals = []
        for am in ANSKEY_RE.finditer(body):
            rest = body[am.end():]
            stop = re.search(r"(?m)^(?:\*\*|##\s|---)", rest)
            payload = rest[:stop.start()] if stop else rest
            vals.append(_answer_core(payload.strip()))
        out[lid] = vals
    return out


def _leak_hits(text):
    hits = []
    for rx in LEAK_RES:
        m = rx.search(text)
        if m:
            s = max(0, m.start() - 25)
            hits.append(f"matched /{rx.pattern}/ near '...{text[s:m.start() + 30].strip()}...'")
    return hits


def _notation_hits(text):
    """Render-breaking notation outside $$ blocks (a focused subset of check_notation.py, applied to
    the new student source). $$ blocks and fenced code are removed first."""
    s = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    s = re.sub(r"\$\$.*?\$\$", " ", s, flags=re.DOTALL)
    hits = []
    for pat, desc in [(r"\\\(", r"\\( inline-LaTeX (use Unicode or a $$ block)"),
                      (r"\\\[", r"\\[ display-LaTeX (use a $$ block)"),
                      (r"\\[a-zA-Z]+", r"\\macro outside a $$ block")]:
        m = re.search(pat, s)
        if m:
            i = max(0, m.start() - 20)
            hits.append(f"{desc} -> '...{s[i:m.start() + 15].strip()}...'")
    return hits


def check(only=None):
    issues = []
    uids = _ssot_unit_ids()
    if only is not None:
        uids = [u for u in uids if str(u) == str(only)]
        if not uids:
            return [f"unknown unit id: {only}"]
    for uid in uids:
        tp, sp = _tutor_path(uid), _student_path(uid)
        if tp is None:
            issues.append(f"unit {uid}: tutor source missing (unexpected)"); continue
        if sp is None:
            issues.append(f"unit {uid}: student source missing in textbook-src/"); continue
        t = open(tp, encoding="utf-8").read()
        s = open(sp, encoding="utf-8").read()
        tc, sc = _all_codes(t), _all_codes(s)
        for c in sorted(tc - sc):
            issues.append(f"unit {uid}: reference code {c} is in the tutor source but missing from the student copy")
        for c in sorted(sc - tc):
            issues.append(f"unit {uid}: reference code {c} is in the student copy but not the tutor source")
        tl, sl = LESSON_RE.findall(t), LESSON_RE.findall(s)
        if tl != sl:
            issues.append(f"unit {uid}: lesson set/order differs (tutor {tl} vs student {sl})")
        tv, sv = _answer_values(t), _answer_values(s)
        for lid in tv:
            if tv[lid] != sv.get(lid):
                issues.append(f"unit {uid}: lesson {lid} answer key differs from the verified source")
        for h in _leak_hits(s):
            issues.append(f"unit {uid}: tutor-meta leakage {h}")
        for h in _notation_hits(s):
            issues.append(f"unit {uid}: notation {h}")
    return issues


def main(argv):
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # issue snippets may contain Unicode (→, −, ²)
    except Exception:
        pass
    only = argv[1] if len(argv) > 1 else None
    iss = check(only)
    if iss:
        print("TEXTBOOK-SRC DRIFT FAIL:\n  " + "\n  ".join(iss))
        return 1
    scope = f"unit {only}" if only is not None else "all present units"
    print(f"textbook-src ({scope}): reference codes, lessons, and answer keys match the verified "
          f"tutor source; no tutor-meta leakage; notation clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
