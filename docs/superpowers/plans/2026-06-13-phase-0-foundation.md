# Phase 0 — Foundation (SSOT + alignment guard) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a structural single source of truth (`curriculum.yaml`) plus a generator and a CI alignment guard that make the four Algebra-1 materials structurally impossible to silently desync, fix the `5.5.6` verification defect with a defense-in-depth point-on-line lint, and correct two stale notation descriptions — with the 765/543/0 answer-key baseline preserved.

**Architecture:** Three Python modules in `_verification/` (build tooling, not shipped): `generate.py` (loads the YAML SSOT, generates marker-bounded data tables, checks `.md`/outline/JSON structure), `check_alignment.py` (umbrella CI guard: alignment + notation + point-on-line + code-grammar), and a refactored `check_notation.py` (importable). All paths repo-relative. TDD with pytest; CircleCI runs the gates.

**Tech Stack:** Python 3.11, sympy 1.14, PyYAML 6, pytest. Windows dev shell is PowerShell; CI is CircleCI on `cimg/python:3.11`.

**Spec:** `docs/superpowers/specs/2026-06-13-phase-0-foundation-design.md`. **Branch:** `phase-0-foundation` (off `main`).

---

## File structure

| File | Responsibility |
|------|----------------|
| `curriculum.yaml` (root) | Structural SSOT: units/lessons, canonical titles, short titles, descriptions, prerequisites, optional flag. Build-only (does not ship). |
| `_verification/generate.py` | `load_ssot()`, `generate()` (write marker regions), `run_checks()` (alignment), CLI (`--check`). |
| `_verification/check_alignment.py` | `code_grammar_lint()`, `point_on_line_lint()`, `main()` orchestrating all four checks. |
| `_verification/check_notation.py` | Refactored: repo-relative path + importable `check()`. |
| `_verification/tests/` | pytest suites + fixtures (one module per component). |
| `requirements.txt` (root) | `sympy`, `PyYAML`, `pytest`. |
| `.gitignore` (root) | `__pycache__/`, `*.pyc`, `.pytest_cache/`. |
| `.circleci/config.yml` | `gates` job: install deps, run verifier + generate --check + alignment + pytest. |

**Conventions:** never `git add -A` / `git add .` (the two untracked HTML files must stay untracked). Stage only the exact files named in each commit step. Run all commands from repo root `C:\Users\18084\algebra`.

---

## Task 1: Scaffolding (deps, ignore, test package)

**Files:**
- Create: `requirements.txt`, `.gitignore`, `_verification/tests/__init__.py`, `_verification/tests/conftest.py`

- [ ] **Step 1: Create `requirements.txt`**

```
sympy>=1.14
PyYAML>=6.0
pytest>=8.0
```

- [ ] **Step 2: Create `.gitignore`** (must NOT list the HTML files)

```
__pycache__/
*.pyc
.pytest_cache/
```

- [ ] **Step 3: Create `_verification/tests/__init__.py`** (empty file).

- [ ] **Step 4: Create `_verification/tests/conftest.py`** (shared repo-root fixture)

```python
import os, sys
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VERIF = os.path.join(REPO_ROOT, "_verification")
sys.path.insert(0, VERIF)  # so tests can `import generate, check_alignment, check_notation`

@pytest.fixture
def repo_root():
    return REPO_ROOT
```

- [ ] **Step 5: Verify pytest collects nothing yet (no error)**

Run: `python -m pytest _verification/tests -q`
Expected: `no tests ran` (exit 5 is acceptable for "no tests collected"; no import errors).

- [ ] **Step 6: Commit**

```bash
git add requirements.txt .gitignore _verification/tests/__init__.py _verification/tests/conftest.py
git commit -m "Phase 0: scaffolding (deps, gitignore, pytest package)"
```

---

## Task 2: Refactor `check_notation.py` (repo-relative + importable)

**Files:**
- Modify: `_verification/check_notation.py`
- Test: `_verification/tests/test_notation.py`

- [ ] **Step 1: Write the failing test**

```python
# _verification/tests/test_notation.py
import os, tempfile, textwrap
import check_notation

def test_clean_tree_has_no_issues():
    issues = check_notation.check()
    assert issues == [], f"unexpected notation leaks: {issues}"

def test_flags_stray_inline_latex(tmp_path):
    d = tmp_path / "algebra-1-tutor" / "references"
    d.mkdir(parents=True)
    (d / "bad.md").write_text("This has inline \\(x+1\\) latex.\n", encoding="utf-8")
    issues = check_notation.check(root=str(tmp_path / "algebra-1-tutor"))
    assert any("bad.md" in str(i) for i in issues)

def test_skill_md_is_excluded(tmp_path):
    d = tmp_path / "algebra-1-tutor"
    d.mkdir(parents=True)
    (d / "SKILL.md").write_text("Documents the \\( ... \\) forbidden form.\n", encoding="utf-8")
    issues = check_notation.check(root=str(d))
    assert issues == []
```

- [ ] **Step 2: Run it to verify it fails**

Run: `python -m pytest _verification/tests/test_notation.py -v`
Expected: FAIL — `check_notation.check` does not exist (it is currently a script).

- [ ] **Step 3: Refactor `check_notation.py`** to be importable and repo-relative. Replace the whole file with:

```python
"""Check that no inline LaTeX leaked outside $$...$$ display blocks in the shipped skill.

For each markdown file under algebra-1-tutor/ (excluding SKILL.md, which intentionally
documents the \\( \\) forms as 'do not use'), strip $$...$$ blocks and fenced code blocks,
then flag any remaining inline-LaTeX delimiters or backslash macros.

Importable: call check(root=None) -> list[str] of issue messages (empty == clean).
"""
import glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ROOT = os.path.join(os.path.dirname(HERE), "algebra-1-tutor")

DELIMS = ["\\(", "\\)", "\\[", "\\]"]
MACRO = re.compile(r"\\[a-zA-Z]+")


def check(root=None):
    """Return a list of issue strings (empty list == clean)."""
    root = root or DEFAULT_ROOT
    issues = []
    files = sorted(glob.glob(os.path.join(root, "**", "*.md"), recursive=True))
    for fp in files:
        if os.path.basename(fp) == "SKILL.md":
            continue
        s = open(fp, encoding="utf-8").read()
        stripped = re.sub(r"\$\$.*?\$\$", " ", s, flags=re.DOTALL)
        stripped = re.sub(r"```.*?```", " ", stripped, flags=re.DOTALL)
        found = [d for d in DELIMS if d in stripped]
        macros = sorted(set(MACRO.findall(stripped)))
        rel = os.path.relpath(fp, root)
        if found:
            issues.append(f"{rel}: inline delimiters present: {found}")
        if macros:
            issues.append(f"{rel}: leftover inline macros: {macros}")
    return issues


def main():
    issues = check()
    if not issues:
        print("Clean: no inline LaTeX leaks outside $$ blocks in any shipped reference/unit file.")
        return 0
    for i in issues:
        print(i)
    print(f"\n{len(issues)} issue(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest _verification/tests/test_notation.py -v`
Expected: PASS (3 tests). Also run `python _verification/check_notation.py` → "Clean: ...".

- [ ] **Step 5: Commit**

```bash
git add _verification/check_notation.py _verification/tests/test_notation.py
git commit -m "Phase 0: make check_notation.py importable + repo-relative"
```

---

## Task 3: Code-grammar lint

**Files:**
- Create: `_verification/check_alignment.py` (start it here; later tasks add to it)
- Test: `_verification/tests/test_code_grammar.py`

- [ ] **Step 1: Write the failing test**

```python
# _verification/tests/test_code_grammar.py
import check_alignment as ca

def test_all_real_ids_pass():
    bad = ca.code_grammar_lint()
    assert bad == [], f"ids violating grammar: {bad}"

def test_accepts_known_shapes():
    for good in ["5.5.6", "12.1.w1", "A.2.3", "refA.4", "refB.10", "8.2.5b"]:
        assert ca.ID_RE.match(good), good

def test_rejects_malformed():
    for bad in ["5.5.", "13.1.1", "x.y.z", "5..6", "ref.4", "5.5.w"]:
        assert not ca.ID_RE.match(bad), bad
```

> Note: `13.1.1` must fail (no Unit 13). `5.5.w` must fail (tag without index). `refC.1` would fail (only A/B).

- [ ] **Step 2: Run it to verify it fails**

Run: `python -m pytest _verification/tests/test_code_grammar.py -v`
Expected: FAIL — `check_alignment` module / `ID_RE` not defined.

- [ ] **Step 3: Create `_verification/check_alignment.py`** with the grammar + lint:

```python
"""Umbrella CI alignment guard for the algebra-1-tutor skill (build tooling, not shipped).

Composes four checks; exits non-zero if any fails:
  1. alignment        (generate.run_checks: SSOT <-> tables/.md/outline/JSON ids + staleness)
  2. notation invariant (check_notation.check)
  3. point-on-line lint (geometric witness + .md answer-key cross-check)
  4. code-grammar lint  (every JSON id matches the backward-compatible grammar)
"""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)

# Backward-compatible id grammar (RESEARCH_REDTEAM_HANDOFF.md s5), restricted to the
# forms present in the answer-key JSON this phase:
#   standard : (1-12 | A) . lesson . [w]index [part]    e.g. 5.5.6, 12.1.w1, A.2.3, 8.2.5b
#   refresher: ref[AB] . index                          e.g. refA.4, refB.10
ID_RE = re.compile(r"^(?:(?:[1-9]|1[0-2]|A)\.\d+\.(?:w)?\d+[a-z]?|ref[AB]\.\d+)$")


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


def main():
    sys.path.insert(0, HERE)
    failures = []
    bad = code_grammar_lint()
    if bad:
        failures.append(f"code-grammar: {len(bad)} bad id(s): {bad}")
    # (notation, point-on-line, alignment wired in later tasks)
    if failures:
        print("\n".join(failures))
        return 1
    print("check_alignment: all checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest _verification/tests/test_code_grammar.py -v`
Expected: PASS (3 tests) — confirms all 765 current ids conform.

- [ ] **Step 5: Commit**

```bash
git add _verification/check_alignment.py _verification/tests/test_code_grammar.py
git commit -m "Phase 0: code-grammar lint (JSON id grammar)"
```

---

## Task 4: Point-on-line — geometric witness + fix 5.5.6 + annotate 5.5

**Files:**
- Modify: `_verification/check_alignment.py` (add `point_on_line_geometric`)
- Modify: `_verification/unit-05.json` (fix 5.5.6; add `on_line`/`slope` to the seven 5.5 line-intercept entries)
- Test: `_verification/tests/test_point_on_line.py`

**Background — the seven line-intercept entries in unit-05 lesson 5.5** (template `m*x0+b=y0`, var `b`), with the `.md` given points/slope:

| id | .md problem | annotation |
|----|-------------|-----------|
| 5.5.w1 | through (2,3), slope 4 | `"on_line":[[2,3]],"slope":4` |
| 5.5.w2 | through (1,2) and (3,8) | `"on_line":[[1,2],[3,8]]` |
| 5.5.1 | through (3,1), slope 2 | `"on_line":[[3,1]],"slope":2` |
| 5.5.2 | through (-1,4), slope -3 | `"on_line":[[-1,4]],"slope":-3` |
| 5.5.4 | line through two pts, m=3, via (2,5) | `"on_line":[[2,5],[4,11]]` |
| 5.5.6 | through (0,-2) and (3,7) → **y=3x-2** | `"on_line":[[0,-2],[3,7]]` |
| 5.5.9 | perp to y=2x through (4,0), m=-1/2 | `"on_line":[[4,0]],"slope":"-1/2"` |

- [ ] **Step 1: Write the failing test** (geometric witness: corrected passes, old rejected, missing-annotation rejected)

```python
# _verification/tests/test_point_on_line.py
import check_alignment as ca

OLD_556 = {"id": "5.5.6", "kind": "solve", "eq": "3*1+b=5", "var": "b", "answer": "2",
           "on_line": [[0, -2], [3, 7]]}
NEW_556 = {"id": "5.5.6", "kind": "solve", "eq": "3*3+b=7", "var": "b", "answer": "-2",
           "on_line": [[0, -2], [3, 7]]}
ONE_PT  = {"id": "5.5.1", "kind": "solve", "eq": "2*3+b=1", "var": "b", "answer": "-5",
           "on_line": [[3, 1]], "slope": 2}

def test_corrected_entry_passes_geometric():
    assert ca.point_on_line_geometric(NEW_556) == []

def test_old_entry_rejected_geometric():
    # class regression: self-consistent eq but wrong line -> points are NOT on it
    assert ca.point_on_line_geometric(OLD_556) != []

def test_one_point_slope_entry_passes():
    assert ca.point_on_line_geometric(ONE_PT) == []

def test_two_point_noncollinear_rejected():
    bad = dict(NEW_556, on_line=[[0, -2], [3, 99]])
    assert ca.point_on_line_geometric(bad) != []
```

- [ ] **Step 2: Run it to verify it fails**

Run: `python -m pytest _verification/tests/test_point_on_line.py -v`
Expected: FAIL — `point_on_line_geometric` not defined.

- [ ] **Step 3: Implement `point_on_line_geometric`** in `check_alignment.py` (append):

```python
import sympy as sp

def _line_eq_template(prob):
    """True if this solve entry is a line-intercept problem: '<m>*<x0>+b=<y0>', var b."""
    return (prob.get("kind") == "solve" and prob.get("var") == "b"
            and re.match(r"^[^=]*\*[^=]*\+b=[^=]+$", prob.get("eq", "").replace(" ", "")))

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
    return issues
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest _verification/tests/test_point_on_line.py -v`
Expected: PASS (4 tests). The old-5.5.6 rejection proves the lint catches the class.

- [ ] **Step 5: Edit `_verification/unit-05.json`** — fix 5.5.6 and add annotations to all seven entries.

Replace line `{"id": "5.5.6", "kind": "solve", "eq": "3*1+b=5", "var": "b", "answer": "2"}` with:
```json
    {"id": "5.5.6", "kind": "solve", "eq": "3*3+b=7", "var": "b", "answer": "-2", "on_line": [[0,-2],[3,7]]},
```
And add the annotation field to the other six (keep `eq`/`answer` unchanged):
```json
    {"id": "5.5.w1", "kind": "solve", "eq": "4*2+b=3", "var": "b", "answer": "-5", "on_line": [[2,3]], "slope": 4},
    {"id": "5.5.w2", "kind": "solve", "eq": "3*1+b=2", "var": "b", "answer": "-1", "on_line": [[1,2],[3,8]]},
    {"id": "5.5.1", "kind": "solve", "eq": "2*3+b=1", "var": "b", "answer": "-5", "on_line": [[3,1]], "slope": 2},
    {"id": "5.5.2", "kind": "solve", "eq": "-3*(-1)+b=4", "var": "b", "answer": "1", "on_line": [[-1,4]], "slope": -3},
    {"id": "5.5.4", "kind": "solve", "eq": "3*2+b=5", "var": "b", "answer": "-1", "on_line": [[2,5],[4,11]]},
    {"id": "5.5.9", "kind": "solve", "eq": "(-1/2)*4+b=0", "var": "b", "answer": "2", "on_line": [[4,0]], "slope": "-1/2"},
```

- [ ] **Step 6: Verify the answer-key baseline is unchanged and JSON is valid**

Run: `python _verification/verify_answers.py`
Expected: `Total problems: 765  |  auto-checked: 543  |  manual (skipped): 222` / `Failures: 0`.

- [ ] **Step 7: Verify the geometric witness passes on the real annotated entries**

Run:
```bash
python -c "import sys; sys.path.insert(0,'_verification'); import json,check_alignment as ca; d=json.load(open('_verification/unit-05.json',encoding='utf-8')); print([i for p in d['problems'] if ca._line_eq_template(p) for i in ca.point_on_line_geometric(p)])"
```
Expected: `[]` (every annotated 5.5 entry consistent).

- [ ] **Step 8: Commit**

```bash
git add _verification/check_alignment.py _verification/unit-05.json _verification/tests/test_point_on_line.py
git commit -m "Phase 0: fix 5.5.6 defect + geometric point-on-line witness"
```

---

## Task 5: Point-on-line — `.md` answer-key cross-check (witness B)

**Files:**
- Modify: `_verification/check_alignment.py` (add `point_on_line_md`, `point_on_line_lint`)
- Test: `_verification/tests/test_point_on_line.py` (extend)

**Parsing contract (scoped to practice entries):** witness B applies to the **practice** line-intercept entries (clean, single-line numbered `**Answer key:**` segments). Worked-example (`wN`) entries — whose results sit in multi-line `$$…$$` derivation blocks — are validated by the geometric witness + the existing sympy `verify_answers` check instead. For a practice entry: resolve its unit `.md` (scope `5` → `unit-05-*.md`, `A` → `appendix-statistics.md`); find the `**Answer key:**` block in its `## Lesson` section; split into `N.`-numbered segments; select the entry's index; normalize `⇒`/`\Rightarrow`/`$$` to spaces and take the text after the **last** `y =` (bounded by `·`/newline); parse it with implicit multiplication as linear in `x`; compare `(slope, intercept)` to the JSON-derived line. No parseable `y = …` → hard failure naming the id.

- [ ] **Step 1: Write the failing tests** (append to `test_point_on_line.py`)

```python
def test_md_crosscheck_passes_for_real_556():
    prob = {"id": "5.5.6", "kind": "solve", "eq": "3*3+b=7", "var": "b", "answer": "-2",
            "on_line": [[0, -2], [3, 7]]}
    assert ca.point_on_line_md(prob) == []

def test_md_crosscheck_rejects_wrong_line():
    # JSON encodes y=3x+2 but .md answer key #6 says y=3x-2
    prob = {"id": "5.5.6", "kind": "solve", "eq": "3*1+b=5", "var": "b", "answer": "2",
            "on_line": [[0, -2], [3, 7]]}
    assert ca.point_on_line_md(prob) != []

def test_full_lint_green_on_repo():
    # both witnesses, every line-intercept entry across all units
    assert ca.point_on_line_lint() == []

def test_full_lint_flags_missing_annotation(monkeypatch):
    import json, os
    real = json.load(open(os.path.join(ca.HERE, "unit-05.json"), encoding="utf-8"))
    stripped = {"unit": 5, "problems": [
        {k: v for k, v in p.items() if k != "on_line"} if p.get("id") == "5.5.1" else p
        for p in real["problems"]]}
    monkeypatch.setattr(ca, "_load_problems", lambda fp: stripped
                        if fp.endswith("unit-05.json") else json.load(open(fp, encoding="utf-8")))
    assert any("5.5.1" in str(i) for i in ca.point_on_line_lint())
```

- [ ] **Step 2: Run to verify failure**

Run: `python -m pytest _verification/tests/test_point_on_line.py -v`
Expected: FAIL — `point_on_line_md` / `point_on_line_lint` / `_load_problems` not defined.

- [ ] **Step 3: Implement** in `check_alignment.py` (append):

```python
UNIT_MD = os.path.join(REPO_ROOT, "algebra-1-tutor", "references", "units")
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations,
                                        implicit_multiplication_application)
TRANSFORMS = standard_transformations + (implicit_multiplication_application,)

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
    end = re.search(r"^\*\*[A-Z]", rest, re.M)   # next bold label
    return rest[: end.start() if end else len(rest)]

def _segment_for_index(block, idx):
    """Within a numbered block, return the segment for item number `idx`."""
    # segments start with 'N.' at a line start or after ' · '
    parts = re.split(r"(?:^|\s)(\d+)\.\s", block)
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
    """`.md` answer-key cross-check (practice line-intercept entries). [] if matches, else [issue].

    Scoped to practice problems: their numbered '**Answer key:**' segments are single-line and
    clean. Worked-example (wN) results live in multi-line $$...$$ blocks and are validated by the
    geometric witness instead, so this is not called for them.
    """
    pid = str(prob["id"])
    if "on_line" not in prob:                 # geometric witness owns the missing-annotation error
        return []
    scope, lesson_n, tail = pid.split(".")
    lesson_id = f"{scope}.{lesson_n}"
    idx = int(re.match(r"\d+", tail).group())
    path = _md_path_for(pid)
    if not path:
        return [f"{pid}: no unit .md found"]
    block = _lesson_section(open(path, encoding="utf-8").read(), lesson_id, "Answer key:")
    md = _last_line_eq(_segment_for_index(block, idx) if block else None)
    if md is None:
        return [f"{pid}: no parseable 'y = ...' in .md Answer key item {idx}"]
    m_md, b_md = md
    b_json = sp.Rational(str(prob["answer"]))
    if "slope" in prob:
        m_json = sp.Rational(str(prob["slope"]))
    else:
        (x1, y1), (x2, y2) = [(sp.Rational(str(a)), sp.Rational(str(c)))
                              for a, c in prob["on_line"][:2]]
        m_json = (y2 - y1) / (x2 - x1)
    if sp.simplify(m_md - m_json) != 0 or sp.simplify(b_md - b_json) != 0:
        return [f"{pid}: .md line y={m_md}x+{b_md} != JSON line y={m_json}x+{b_json}"]
    return []

def _load_problems(fp):
    return json.load(open(fp, encoding="utf-8"))

def point_on_line_lint():
    """Geometric witness on every line-intercept entry; .md cross-check on practice ones."""
    issues = []
    for fp in _json_files():
        for prob in _load_problems(fp)["problems"]:
            if _line_eq_template(prob):
                issues += point_on_line_geometric(prob)
                if not str(prob["id"]).rsplit(".", 1)[-1].startswith("w"):
                    issues += point_on_line_md(prob)
    return issues
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest _verification/tests/test_point_on_line.py -v`
Expected: PASS (8 tests).

- [ ] **Step 5: Commit**

```bash
git add _verification/check_alignment.py _verification/tests/test_point_on_line.py
git commit -m "Phase 0: .md answer-key cross-check (point-on-line witness B)"
```

---

## Task 6: `curriculum.yaml` + SSOT loader

**Files:**
- Create: `curriculum.yaml`
- Modify: `_verification/generate.py` (create with `load_ssot`)
- Test: `_verification/tests/test_generate.py`

- [ ] **Step 1: Create `curriculum.yaml`** (root) with the complete SSOT (titles verbatim from the `.md` headers; descriptions/prereqs unified from the two tables, `x^2`→`x²`):

```yaml
course: "Algebra 1"
units:
  - id: 1
    slug: foundations
    title: "Foundations & the Language of Algebra"
    short_title: "Foundations"
    description: "Variables, the equals sign as a balance, the number system & number line, order of operations, negative numbers, expressions vs. equations"
    prerequisites: "Arithmetic only"
    optional: false
    lessons:
      - { id: "1.1", title: "Variables and the meaning of equations" }
      - { id: "1.2", title: "The number system & the number line" }
      - { id: "1.3", title: "Order of operations" }
      - { id: "1.4", title: "Negative numbers" }
      - { id: "1.5", title: "Expressions vs. equations; evaluating expressions" }
  - id: 2
    slug: linear-equations
    title: "Solving Linear Equations"
    short_title: "Linear Equations"
    description: "One- and two-step equations, like terms, distributive property, variables on both sides, fractions in equations"
    prerequisites: "Unit 1 (esp. negatives, order of operations)"
    optional: false
    lessons:
      - { id: "2.1", title: "Inverse operations & one-step equations" }
      - { id: "2.2", title: "Two-step equations" }
      - { id: "2.3", title: "Combining like terms & the distributive property" }
      - { id: "2.4", title: "Variables on both sides" }
      - { id: "2.5", title: "Equations with fractions (with two Fraction Refreshers)" }
  - id: 3
    slug: proportional-reasoning
    title: "Proportional Reasoning (the bridge to linearity)"
    short_title: "Proportional Reasoning"
    description: "Ratios, rates, unit rate, proportions, percents"
    prerequisites: "Unit 2 (solving), fraction comfort"
    optional: false
    lessons:
      - { id: "3.1", title: "Ratios and rates" }
      - { id: "3.2", title: "Proportions & cross-multiplication" }
      - { id: "3.3", title: "Percents" }
  - id: 4
    slug: functions
    title: "Introducing Functions"
    short_title: "Functions"
    description: "What a function is, f(x) notation, domain & range, table/graph/equation/words"
    prerequisites: "Unit 2; helped by Unit 3 (rates)"
    optional: false
    lessons:
      - { id: "4.1", title: "What is a function" }
      - { id: "4.2", title: "Function notation f(x), domain & range" }
      - { id: "4.3", title: "Multiple representations; linear vs. nonlinear" }
  - id: 5
    slug: linear-functions-graphs
    title: "Linear Functions & Their Graphs"
    short_title: "Linear Functions"
    description: "Coordinate plane, graphing, slope, slope-intercept, writing equations of lines"
    prerequisites: "Units 3 & 4 (rate, functions)"
    optional: false
    lessons:
      - { id: "5.1", title: "The coordinate plane" }
      - { id: "5.2", title: "Graphing linear equations from a table" }
      - { id: "5.3", title: "Slope" }
      - { id: "5.4", title: "Slope-intercept form y = mx + b" }
      - { id: "5.5", title: "Writing equations of lines" }
  - id: 6
    slug: modeling-translation
    title: "Modeling & Translation"
    short_title: "Modeling"
    description: "Turning words into equations; number/age/distance/mixture problems; intro scatter plots"
    prerequisites: "Units 2 & 5"
    optional: false
    lessons:
      - { id: "6.1", title: "Translating words into expressions and equations" }
      - { id: "6.2", title: "Classic word problems (number, age, distance, mixture)" }
      - { id: "6.3", title: "Scatter plots & line of best fit (a first taste of data)" }
  - id: 7
    slug: systems
    title: "Systems of Equations"
    short_title: "Systems"
    description: "Two equations, two unknowns: graphing, substitution, elimination, special cases"
    prerequisites: "Units 5 & 6"
    optional: false
    lessons:
      - { id: "7.1", title: "Solving by graphing" }
      - { id: "7.2", title: "Substitution" }
      - { id: "7.3", title: "Elimination" }
      - { id: "7.4", title: "Special cases & applications" }
  - id: 8
    slug: inequalities
    title: "Inequalities"
    short_title: "Inequalities"
    description: "One-variable, the sign-flip, compound, absolute value, two-variable graphing"
    prerequisites: "Units 2 & 5"
    optional: false
    lessons:
      - { id: "8.1", title: "One-variable inequalities" }
      - { id: "8.2", title: "Compound inequalities" }
      - { id: "8.3", title: "Absolute-value equations & inequalities" }
      - { id: "8.4", title: "Graphing linear inequalities (two variables) & systems" }
  - id: 9
    slug: sequences-exponentials
    title: "Sequences & Exponential Functions"
    short_title: "Sequences & Exponentials"
    description: "Arithmetic/geometric sequences as functions, exponential growth & decay, linear vs. exponential"
    prerequisites: "Unit 4 (functions); some Unit 5"
    optional: false
    lessons:
      - { id: "9.1", title: "Arithmetic & geometric sequences as functions" }
      - { id: "9.2", title: "Exponential growth & decay; linear vs. exponential" }
  - id: 10
    slug: exponents-polynomials
    title: "Exponents & Polynomials"
    short_title: "Exponents & Polynomials"
    description: "Exponent rules, scientific notation, polynomial operations, FOIL/area model"
    prerequisites: "Unit 1 (exponents), Unit 2 (distributive)"
    optional: false
    lessons:
      - { id: "10.1", title: "Exponent rules (including zero & negative exponents)" }
      - { id: "10.2", title: "Scientific notation" }
      - { id: "10.3", title: "Polynomials — terms, degree, standard form; add & subtract" }
      - { id: "10.4", title: "Multiplying polynomials" }
  - id: 11
    slug: factoring
    title: "Factoring"
    short_title: "Factoring"
    description: "GCF, factoring trinomials, special patterns"
    prerequisites: "Unit 10 (multiplying polynomials)"
    optional: false
    lessons:
      - { id: "11.1", title: "Greatest common factor (GCF)" }
      - { id: "11.2", title: "Factoring trinomials x²+bx+c" }
      - { id: "11.3", title: "Special patterns" }
  - id: 12
    slug: quadratics
    title: "Quadratic Functions & Equations (the capstone)"
    short_title: "Quadratics"
    description: "Square roots & radicals, x²=9, factoring, completing the square, quadratic formula, parabolas"
    prerequisites: "Units 10 & 11; Unit 5 (graphing)"
    optional: false
    lessons:
      - { id: "12.1", title: "Square roots & simplifying radicals" }
      - { id: "12.2", title: "The simplest quadratics (x²=9 → two solutions)" }
      - { id: "12.3", title: "Solving by factoring (zero-product property)" }
      - { id: "12.4", title: "Completing the square" }
      - { id: "12.5", title: "The quadratic formula & the discriminant" }
      - { id: "12.6", title: "Graphing parabolas" }
  - id: "A"
    slug: statistics
    title: "Data & Statistics"
    short_title: "Statistics"
    description: "One/two-variable statistics, line of best fit, correlation vs. causation, two-way tables"
    prerequisites: "Unit 5 (graphing lines)"
    optional: true
    lessons:
      - { id: "A.1", title: "One-variable statistics — center & spread" }
      - { id: "A.2", title: "Two-variable data — line of best fit, correlation vs. causation" }
      - { id: "A.3", title: "Two-way tables" }
```

- [ ] **Step 2: Write the failing test**

```python
# _verification/tests/test_generate.py
import generate

def test_load_ssot_shape():
    ssot = generate.load_ssot()
    assert len(ssot.units) == 13                       # 12 units + appendix A
    total = sum(len(u.lessons) for u in ssot.units)
    assert total == 50                                  # 47 core + 3 appendix
    u5 = next(u for u in ssot.units if u.id == "5")
    assert u5.title == "Linear Functions & Their Graphs"
    assert [l.id for l in u5.lessons][0] == "5.1"
    appA = next(u for u in ssot.units if u.id == "A")
    assert appA.optional is True

def test_unit_ids_normalized_to_str():
    ssot = generate.load_ssot()
    assert {u.id for u in ssot.units} == {str(n) for n in range(1, 13)} | {"A"}
```

- [ ] **Step 3: Run to verify failure**

Run: `python -m pytest _verification/tests/test_generate.py -v`
Expected: FAIL — `generate` module not defined.

- [ ] **Step 4: Create `_verification/generate.py`** with the loader:

```python
"""SSOT generator + checker for the algebra-1-tutor curriculum (build tooling, not shipped).

Generates the marker-bounded data tables in curriculum-map.md and docs/CURRICULUM.md from
curriculum.yaml, and CHECKS the unit .md titles / lesson ids / counts / outline / JSON ids
against the SSOT. `--check` writes nothing and exits non-zero on any drift or staleness.
"""
import argparse, glob, json, os, re, sys
from dataclasses import dataclass, field
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
SSOT_PATH = os.path.join(REPO_ROOT, "curriculum.yaml")
MAP_MD = os.path.join(REPO_ROOT, "algebra-1-tutor", "references", "curriculum-map.md")
CURRIC_MD = os.path.join(REPO_ROOT, "docs", "CURRICULUM.md")
UNIT_MD = os.path.join(REPO_ROOT, "algebra-1-tutor", "references", "units")

@dataclass
class Lesson:
    id: str
    title: str

@dataclass
class Unit:
    id: str
    slug: str
    title: str
    short_title: str
    description: str
    prerequisites: str
    optional: bool
    lessons: list = field(default_factory=list)

@dataclass
class Ssot:
    course: str
    units: list

def load_ssot(path=SSOT_PATH):
    raw = yaml.safe_load(open(path, encoding="utf-8"))
    units = []
    for u in raw["units"]:
        lessons = [Lesson(str(l["id"]), l["title"]) for l in u["lessons"]]
        units.append(Unit(str(u["id"]), u["slug"], u["title"], u["short_title"],
                          u["description"], u["prerequisites"], bool(u["optional"]), lessons))
    return Ssot(raw["course"], units)
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python -m pytest _verification/tests/test_generate.py -v`
Expected: PASS (2 tests).

- [ ] **Step 6: Commit**

```bash
git add curriculum.yaml _verification/generate.py _verification/tests/test_generate.py
git commit -m "Phase 0: curriculum.yaml SSOT + loader"
```

---

## Task 7: Table generation + marker insertion (idempotent)

**Files:**
- Modify: `_verification/generate.py` (add `render_*`, `generate`, marker rewriting)
- Modify: `algebra-1-tutor/references/curriculum-map.md` (insert markers around the units table)
- Modify: `docs/CURRICULUM.md` (insert markers around the Units table)
- Test: `_verification/tests/test_generate.py` (extend)

**Row templates (exact):**
- curriculum-map units-at-a-glance: `| {id} | **{title}**{opt_map} | {description} | {prerequisites} |`, where `opt_map` = ` *(optional, off the main path)*` if optional else ``.
- docs/CURRICULUM Units: `| {id} | {title}{opt_cur} | {description} |`, where `opt_cur` = ` (optional)` if optional else ``.
- Header rows are preserved as static text above the generated row block (see Step 3). The generator replaces only the table **body rows** between the markers.

- [ ] **Step 1: Insert markers in `curriculum-map.md`.** Around the existing "units at a glance" table (the `| # | Unit | ... |` header, the `|---|` divider, and the 13 body rows), wrap the **body rows only** so the header stays human-owned:

```markdown
| # | Unit | What it's about | Assumes (prerequisites) |
|---|------|-----------------|--------------------------|
<!-- BEGIN GENERATED: units-at-a-glance -->
| 1 | **Foundations & the Language of Algebra** | ... | Arithmetic only |
... (existing 13 rows; will be regenerated in Step 4) ...
<!-- END GENERATED: units-at-a-glance -->
```

- [ ] **Step 2: Insert markers in `docs/CURRICULUM.md`** around that table's 13 body rows the same way (markers between the `|---|` divider and the next blank line).

- [ ] **Step 3: Write the failing tests** (append to `test_generate.py`)

```python
import subprocess, sys, os, shutil

def test_render_units_table_normalizes(tmp_path):
    ssot = generate.load_ssot()
    body = generate.render_map_table(ssot)
    assert "x²" in body and "x^2" not in body
    assert "**Proportional Reasoning (the bridge to linearity)**" in body
    assert "*(optional, off the main path)*" in body          # appendix row

def test_marker_rewrite_is_idempotent(tmp_path):
    f = tmp_path / "doc.md"
    f.write_text("pre\n<!-- BEGIN GENERATED: x -->\nOLD\n<!-- END GENERATED: x -->\npost\n",
                 encoding="utf-8")
    generate.write_region(str(f), "x", "NEW\nLINES")
    once = f.read_text(encoding="utf-8")
    generate.write_region(str(f), "x", "NEW\nLINES")
    assert f.read_text(encoding="utf-8") == once
    assert "NEW\nLINES" in once and "OLD" not in once

def test_missing_marker_raises(tmp_path):
    f = tmp_path / "doc.md"
    f.write_text("no markers here\n", encoding="utf-8")
    try:
        generate.write_region(str(f), "x", "NEW")
        assert False, "expected error"
    except ValueError as e:
        assert "marker" in str(e).lower()

def test_generate_then_check_is_clean():
    generate.generate()                                        # write regions
    r = subprocess.run([sys.executable, os.path.join(generate.HERE, "generate.py"), "--check"])
    assert r.returncode == 0
```

- [ ] **Step 2b: Run to verify failure**

Run: `python -m pytest _verification/tests/test_generate.py -v`
Expected: FAIL — `render_map_table` / `write_region` / `generate` not defined.

- [ ] **Step 3: Implement generation** in `generate.py` (append):

```python
def _opt(u, kind):
    if not u.optional:
        return ""
    return " *(optional, off the main path)*" if kind == "map" else " (optional)"

def render_map_table(ssot):
    rows = [f"| {u.id} | **{u.title}**{_opt(u,'map')} | {u.description} | {u.prerequisites} |"
            for u in ssot.units]
    return "\n".join(rows)

def render_curric_table(ssot):
    rows = [f"| {u.id} | {u.title}{_opt(u,'cur')} | {u.description} |"
            for u in ssot.units]
    return "\n".join(rows)

def write_region(path, region_id, body):
    text = open(path, encoding="utf-8").read()
    begin = f"<!-- BEGIN GENERATED: {region_id} -->"
    end = f"<!-- END GENERATED: {region_id} -->"
    pat = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.DOTALL)
    if not pat.search(text):
        raise ValueError(f"missing marker pair for region '{region_id}' in {path}")
    new = pat.sub(begin + "\n" + body + "\n" + end, text)
    if new != text:
        open(path, "w", encoding="utf-8", newline="\n").write(new)

def generate():
    ssot = load_ssot()
    write_region(MAP_MD, "units-at-a-glance", render_map_table(ssot))
    write_region(CURRIC_MD, "units-table", render_curric_table(ssot))
```

- [ ] **Step 4: Regenerate the tables and inspect the diff**

Run: `python _verification/generate.py` then `git --no-pager diff --stat algebra-1-tutor/references/curriculum-map.md docs/CURRICULUM.md`
Expected: small diffs limited to the normalizations (U3/U12 titles gain "(the …)", `x^2`→`x²`, CURRICULUM case/optional suffix). Eyeball `git --no-pager diff` to confirm no structural damage.

- [ ] **Step 5: Run tests to verify they pass**

Run: `python -m pytest _verification/tests/test_generate.py -v`
Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add _verification/generate.py algebra-1-tutor/references/curriculum-map.md docs/CURRICULUM.md _verification/tests/test_generate.py
git commit -m "Phase 0: generate units tables from SSOT (marker-bounded, idempotent)"
```

---

## Task 8: Structure checks (`run_checks`) — .md / outline / counts / JSON ids / staleness

**Files:**
- Modify: `_verification/generate.py` (add `run_checks`, `--check` CLI)
- Test: `_verification/tests/test_generate.py` (extend)

**Check contract (each returns issue strings):**
1. Unit `.md` H1 == `# Unit <n>: <title>` / `# Appendix A: <title>`, title exact == SSOT.
2. `.md` `## Lesson <id>: <title>` set (id+title) == SSOT set (exact).
3. Per-unit lesson counts: `.md` == SSOT.
4. curriculum-map outline: lesson-id set == SSOT id set; per-unit counts match (IDs/counts only — outline prose titles are curated, not title-checked).
5. Every JSON answer-key id's `(unit, lesson)` exists in the SSOT.
6. Staleness: regenerating the two regions would not change the files.

- [ ] **Step 1: Write the failing tests** (append)

```python
def test_run_checks_clean_on_repo():
    assert generate.run_checks() == []

def test_check_detects_md_title_drift(monkeypatch):
    ssot = generate.load_ssot()
    next(u for u in ssot.units if u.id == "5").title = "WRONG TITLE"
    monkeypatch.setattr(generate, "load_ssot", lambda *a, **k: ssot)
    assert any("WRONG TITLE" in i or "Unit 5" in i for i in generate.run_checks())

def test_check_detects_stale_region(tmp_path, monkeypatch):
    # corrupt a generated region, then --check must fail
    import shutil
    bak = MAP_MD = generate.MAP_MD
    original = open(generate.MAP_MD, encoding="utf-8").read()
    try:
        corrupt = original.replace("<!-- END GENERATED: units-at-a-glance -->",
                                   "| 99 | **BOGUS** | x | y |\n<!-- END GENERATED: units-at-a-glance -->")
        open(generate.MAP_MD, "w", encoding="utf-8", newline="\n").write(corrupt)
        assert any("stale" in i.lower() or "units-at-a-glance" in i for i in generate.run_checks())
    finally:
        open(generate.MAP_MD, "w", encoding="utf-8", newline="\n").write(original)
```

- [ ] **Step 2: Run to verify failure**

Run: `python -m pytest _verification/tests/test_generate.py -k run_checks or check_detects -v`
Expected: FAIL — `run_checks` not defined.

- [ ] **Step 3: Implement** in `generate.py` (append):

```python
H1_RE = re.compile(r"^#\s+(?:Unit\s+(\d+)|Appendix\s+([A-Z])):\s+(.*?)\s*$", re.M)
LESSON_RE = re.compile(r"^##\s+Lesson\s+([0-9A]+\.\d+):\s+(.*?)\s*$", re.M)

def _unit_md_path(uid):
    if uid == "A":
        return os.path.join(UNIT_MD, "appendix-statistics.md")
    hits = glob.glob(os.path.join(UNIT_MD, f"unit-{int(uid):02d}-*.md"))
    return hits[0] if hits else None

def _outline_lesson_ids(text):
    m = re.search(r"^##\s+Lesson-level outline\s*$", text, re.M)
    if not m:
        return set()
    rest = text[m.end():]
    end = re.search(r"^##\s", rest, re.M)
    region = rest[: end.start() if end else len(rest)]
    return set(re.findall(r"^-\s+([0-9A]+\.\d+)\b", region, re.M))

def _region_body(path, region_id):
    text = open(path, encoding="utf-8").read()
    m = re.search(re.escape(f"<!-- BEGIN GENERATED: {region_id} -->") + r"\n(.*?)\n"
                  + re.escape(f"<!-- END GENERATED: {region_id} -->"), text, re.DOTALL)
    return m.group(1) if m else None

def run_checks():
    ssot = load_ssot()
    issues = []
    ssot_lessons = {(u.id, l.id, l.title) for u in ssot.units for l in u.lessons}
    ssot_ids = {l.id for u in ssot.units for l in u.lessons}
    # 1-3: unit .md H1 + lesson headers + counts
    for u in ssot.units:
        path = _unit_md_path(u.id)
        if not path:
            issues.append(f"unit {u.id}: no .md file found"); continue
        text = open(path, encoding="utf-8").read()
        h1 = H1_RE.search(text)
        title = h1.group(3) if h1 else None
        if title != u.title:
            issues.append(f"unit {u.id}: .md H1 title {title!r} != SSOT {u.title!r}")
        md_lessons = LESSON_RE.findall(text)
        if len(md_lessons) != len(u.lessons):
            issues.append(f"unit {u.id}: .md lesson count {len(md_lessons)} != SSOT {len(u.lessons)}")
        for lid, ltitle in md_lessons:
            if (u.id, lid, ltitle) not in ssot_lessons:
                issues.append(f"unit {u.id}: .md lesson {lid} {ltitle!r} not in SSOT")
    # 4: outline ids
    map_text = open(MAP_MD, encoding="utf-8").read()
    outline_ids = _outline_lesson_ids(map_text)
    if outline_ids != ssot_ids:
        issues.append(f"curriculum-map outline ids mismatch: "
                      f"missing={sorted(ssot_ids - outline_ids)} extra={sorted(outline_ids - ssot_ids)}")
    # 5: JSON ids belong to a known lesson
    for fp in (sorted(glob.glob(os.path.join(HERE, "unit-*.json")))
               + sorted(glob.glob(os.path.join(HERE, "appendix*.json")))):
        for prob in json.load(open(fp, encoding="utf-8"))["problems"]:
            pid = str(prob.get("id", ""))
            if pid.startswith("ref"):
                continue                                   # refresher items live under a lesson 2.5
            mm = re.match(r"^([0-9A]+\.\d+)\.", pid)
            if mm and mm.group(1) not in ssot_ids:
                issues.append(f"{os.path.basename(fp)}: id {pid} -> unknown lesson {mm.group(1)}")
    # 6: staleness
    if _region_body(MAP_MD, "units-at-a-glance") != render_map_table(ssot):
        issues.append("curriculum-map.md units-at-a-glance region is stale (run generate.py)")
    if _region_body(CURRIC_MD, "units-table") != render_curric_table(ssot):
        issues.append("docs/CURRICULUM.md units-table region is stale (run generate.py)")
    return issues

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="verify only; write nothing")
    args = ap.parse_args(argv)
    if args.check:
        issues = run_checks()
        if issues:
            print("\n".join(issues)); return 1
        print("alignment: SSOT <-> tables/.md/outline/JSON all consistent."); return 0
    generate()
    print("generated: curriculum-map.md + docs/CURRICULUM.md regions.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run tests + the CLI**

Run: `python -m pytest _verification/tests/test_generate.py -v` (Expected: PASS) then
`python _verification/generate.py --check` (Expected: "alignment: … consistent." exit 0).

- [ ] **Step 5: Commit**

```bash
git add _verification/generate.py _verification/tests/test_generate.py
git commit -m "Phase 0: SSOT alignment checks (.md/outline/counts/ids/staleness)"
```

---

## Task 9: Wire `check_alignment.py` umbrella (all four checks)

**Files:**
- Modify: `_verification/check_alignment.py` (`main` runs all four)
- Test: `_verification/tests/test_check_alignment.py`

- [ ] **Step 1: Write the failing test**

```python
# _verification/tests/test_check_alignment.py
import subprocess, sys, os
import check_alignment as ca

def test_main_green_on_repo():
    assert ca.main() == 0

def test_cli_exit_zero():
    r = subprocess.run([sys.executable,
                        os.path.join(ca.HERE, "check_alignment.py")])
    assert r.returncode == 0
```

- [ ] **Step 2: Run to verify it fails**

Run: `python -m pytest _verification/tests/test_check_alignment.py -v`
Expected: FAIL — `main` currently only runs code-grammar (and may pass trivially); after Step 3 it must run all four. (If it passes now, Step 3 still required for coverage.)

- [ ] **Step 3: Replace `main()` in `check_alignment.py`** to run all four:

```python
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
```

- [ ] **Step 4: Run the full guard + the whole suite**

Run: `python _verification/check_alignment.py` (Expected: "… all green." exit 0) then
`python -m pytest _verification/tests -v` (Expected: all PASS).

- [ ] **Step 5: Commit**

```bash
git add _verification/check_alignment.py _verification/tests/test_check_alignment.py
git commit -m "Phase 0: check_alignment umbrella runs all four checks"
```

---

## Task 10: Doc corrections (notation reality)

**Files:**
- Modify: `algebra-1-tutor/SKILL.md` (the stale line ~115)
- Modify: `_verification/AUTHOR_GUIDE.md` (line 13, the `\(f(x)=…\)` example near 17, + JSON schema doc)

- [ ] **Step 1: Fix `SKILL.md` line 115.** Replace the paragraph beginning `**The reference and lesson files you read are written with` with:

```markdown
**The reference and lesson files you read use this same convention** — plain-Unicode inline, real notation in `$$ ... $$` blocks. They were converted away from inline `\( ... \)`, so you can mirror their notation directly; reserve `$$ ... $$` for standalone notation. Currency is just a dollar sign in prose, e.g. "it costs $5" (no escaping needed in plain text), but keep a bare `$` away from any `$$` block so it isn't misread.
```

- [ ] **Step 2: Verify SKILL.md still has its forbidden-output examples** (lines ~101/106/113 unchanged) so the notation scan still legitimately excludes it. Run:
`python _verification/check_notation.py` → "Clean: …".

- [ ] **Step 3: Fix `AUTHOR_GUIDE.md` line 13.** Replace:
```
- All math in **LaTeX**: `$$...$$` for display, `\(...\)` for inline. **Never** lone `$...$`. Escape literal currency as `\$`.
```
with:
```
- Display math in **`$$...$$`** blocks. **Inline math is plain Unicode** (x², √12, ½, ±, ≤, →) — **never** `\(...\)` or lone `$...$` (they show as raw text on Claude.ai). Escape literal currency as `\$`.
```

- [ ] **Step 4: Fix the inline-LaTeX example near line 17.** Change `\(f(x)=2x+1\)` to plain `f(x)=2x+1` in that sentence.

- [ ] **Step 5: Document the new JSON fields** — in the "JSON schema for `unit-NN.json`" section (after the `solve` rule, ~line 74), add:
```
- Line-equation `solve` problems (find the intercept `b`, template `m*x0+b=y0`) MUST also carry
  `on_line`: the given point(s) as `[[x,y],...]`, plus `slope` for one-point (point+slope)
  problems. The point-on-line lint rebuilds the line and cross-checks it against the .md answer key.
```

- [ ] **Step 6: Commit**

```bash
git add algebra-1-tutor/SKILL.md _verification/AUTHOR_GUIDE.md
git commit -m "Phase 0: correct stale inline-LaTeX notation docs (SKILL.md, AUTHOR_GUIDE.md)"
```

---

## Task 11: CircleCI config + full-gate verification

**Files:**
- Create: `.circleci/config.yml`

- [ ] **Step 1: Create `.circleci/config.yml`**

```yaml
version: 2.1
jobs:
  gates:
    docker:
      - image: cimg/python:3.11
    steps:
      - checkout
      - run:
          name: Install deps
          command: pip install -r requirements.txt
      - run:
          name: Answer-key verifier (sympy)
          command: python _verification/verify_answers.py
      - run:
          name: SSOT generation up to date
          command: python _verification/generate.py --check
      - run:
          name: Alignment guard (alignment + notation + point-on-line + code-grammar)
          command: python _verification/check_alignment.py
      - run:
          name: Unit tests
          command: python -m pytest _verification/tests -v
workflows:
  phase-0-gates:
    jobs:
      - gates
```

- [ ] **Step 2: Run the full gate locally (mirror CI)**

Run, expecting each to exit 0:
```
python _verification/verify_answers.py
python _verification/generate.py --check
python _verification/check_alignment.py
python -m pytest _verification/tests -v
```
Expected: verifier 765/543/0; generate --check consistent; alignment all green; all tests pass.

- [ ] **Step 3: Confirm the two HTML files are still untracked and unmodified**

Run: `git status --short`
Expected: only `?? algebra-1-lesson-plan.html` and `?? algebra-1-student-guide.html`.

- [ ] **Step 4: Commit**

```bash
git add .circleci/config.yml
git commit -m "Phase 0: CircleCI gates (verify + alignment + tests)"
```

---

## Task 12: Code review + PR

- [ ] **Step 1: Run `/code-review` on the tooling diff** (generators/lints). Address findings (new commits).
- [ ] **Step 2: Re-run the full gate** (Task 11 Step 2) — all green.
- [ ] **Step 3: Push and open the PR**

```bash
git push -u origin phase-0-foundation
gh pr create --base main --title "Phase 0: foundation — SSOT + alignment guard" \
  --body "Implements Phase 0 of the rebuild (spec: docs/superpowers/specs/2026-06-13-phase-0-foundation-design.md). Adds curriculum.yaml SSOT, generate.py (marker-bounded tables + .md/outline/id checks), check_alignment.py (alignment + notation + point-on-line + code-grammar), fixes the 5.5.6 verification defect with a defense-in-depth point-on-line lint, corrects two stale notation docs, and wires CircleCI gates. Baseline preserved (765/543/0)."
```

---

## Acceptance criteria (verify before calling done)

1. `python _verification/verify_answers.py` → **765 / 543 / 0**.
2. `python _verification/check_alignment.py` → all green.
3. `python _verification/generate.py --check` → consistent; running `generate.py` twice → clean `git diff`.
4. Point-on-line regression test rejects the pre-fix 5.5.6 and accepts the fix (`test_old_entry_rejected_geometric`, `test_md_crosscheck_rejects_wrong_line`).
5. `python -m pytest _verification/tests -v` → all pass; CircleCI `gates` green.
6. `git diff main...phase-0-foundation` touches no teaching prose beyond the two notation lines + marker insertions + table normalizations; the two HTML files remain untracked.

---

## Self-review notes (author)

- **Spec coverage:** SSOT (T6) · generate tables (T7) · `.md`/id/count checks (T8) · check_alignment umbrella (T9) · notation invariant reuse (T2) · point-on-line both witnesses (T4+T5) · code-grammar (T3) · 5.5.6 fix (T4) · doc corrections (T10) · requirements/gitignore (T1) · CircleCI (T11) · PR (T12). All §13 deliverables mapped.
- **Spec reconciliation:** the spec's "outline lesson titles checked by normalized containment" is **superseded** here by strict outline IDs+counts + strict `.md`-header titles (no fuzzy outline-title match), because `.md` titles and outline glosses each carry words the other lacks (8.4 vs 5.3) → fuzzy matching would false-positive. Update spec §4.2/§5 wording to match before merge.
- **Type consistency:** `point_on_line_geometric` / `point_on_line_md` / `point_on_line_lint`, `_line_eq_template`, `_load_problems`, `ID_RE`, `render_map_table` / `render_curric_table` / `write_region` / `run_checks` — names consistent across tasks and tests.
- **Known risks:** the `.md` parser (`_segment_for_index`, `_last_line_eq`) is the most delicate piece — its tests (T5) pin the contract; if a future line problem's answer key isn't a parseable `y = …`, the lint fails loudly by design.
