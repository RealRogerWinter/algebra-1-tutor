# Bundle Viz Figures as Tutor Artifacts — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bundle a self-contained `.html` artifact for every viz figure into the skill so the Algebra-1 tutor emits the real figure (interactive widgets live, math rendered) instead of refusing the reference code.

**Architecture:** A new `build_viz_artifacts.py` reads `viz_figures.VIZ_FIGURES`, pulls each `module.samples()[index]["html"]`, and wraps it in a standalone HTML page that inlines `build_textbook.CSS` (reused wholesale, no drift) and loads KaTeX from cdnjs (the artifact-sanctioned CDN). Files land in `algebra-1-tutor/figures/<code>.html`, get packaged by `build_skill.py`, gated by `--check` + pytest + smoke_test, and SKILL.md's resolution recipe is rewritten to emit them and never refuse a resolvable code.

**Tech Stack:** Python 3.11, sympy (existing), `markdown` (existing), KaTeX via cdnjs, vanilla JS in figures, pytest, CircleCI, Windows Edge headless (visual verification only).

**Key invariants discovered (do not violate):**
- `build_textbook.CSS` (line 1106) is a plain `"""…"""` constant containing **literal `{` `}`** CSS braces; viz bodies also contain `{` (e.g. `\textcolor{#2980b9}{…}`) and `$$`. **Assemble pages by string concatenation / `.replace`, NEVER `.format()` or f-strings**, or the braces break.
- Viz codes are cross-collision-checked disjoint from deterministic `figures.py` SVG codes (`viz_figures.check()`), so `<code>.svg` and `<code>.html` never coexist — resolution "`.svg` else `.html`" is unambiguous.
- 40 viz figures on this branch; 32 contain TeX in the body; 6 are interactive (`1.1.f1, 1.5.f1, 2.1.f1, 5.2.f2, 5.4.f3, 12.6.f2`).
- KaTeX version constant: `build_textbook.KATEX == "0.16.11"`. cdnjs base: `https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11`.
- Auto-render config the textbook uses: delimiters `$$`/`$$` (display) and `\(`/`\)` (inline), `throwOnError:false`.
- Tests live in `_verification/tests/`; run with `cd _verification && python -m pytest` (conftest adds `_verification` to path; modules import bare, e.g. `import figures`).

---

## Task 1: Generator core — `build_viz_artifacts.py` builds one self-contained page

**Files:**
- Create: `_verification/build_viz_artifacts.py`
- Test: `_verification/tests/test_viz_artifacts.py`

- [ ] **Step 1: Write the failing test**

```python
# _verification/tests/test_viz_artifacts.py
import build_viz_artifacts as bva
import viz_figures as vf


def test_page_is_self_contained_and_keyed():
    code = "3.2.f1"
    html = bva.render_page(code)
    assert html.lstrip().lower().startswith("<!doctype html>")
    assert f'id="fig-{code}"' in html
    assert "<style>" in html                      # CSS inlined, not linked to a local file
    assert "var(--ink)" in html                   # the textbook CSS variables are present
    assert "cdnjs.cloudflare.com/ajax/libs/KaTeX/" + bva.KATEX in html
    assert "renderMathInElement" in html


def test_math_body_pulls_katex():
    # 3.2.f1 body contains TeX; the page must load KaTeX css + js from cdnjs
    html = bva.render_page("3.2.f1")
    assert "katex.min.css" in html and "katex.min.js" in html and "auto-render.min.js" in html


def test_interactive_js_preserved():
    # 5.2.f2 is an interactive slider widget; its inline <script> must survive verbatim
    html = bva.render_page("5.2.f2")
    assert "<script" in html
    body = bva.figure_body("5.2.f2")
    assert "addEventListener" in body or "oninput" in body
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd _verification && python -m pytest tests/test_viz_artifacts.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'build_viz_artifacts'`

- [ ] **Step 3: Write minimal implementation**

```python
# _verification/build_viz_artifacts.py
"""Generate a self-contained .html artifact per viz figure, bundled into the skill (build tooling).

The student textbook embeds ~40 "viz" figures (viz_figures.VIZ_FIGURES) as HTML/SVG + inline JS
via build_textbook; unlike the deterministic figures.py SVGs they were never bundled into the
skill, so the tutor could not emit them. This writes algebra-1-tutor/figures/<code>.html for every
viz code: each sample's html wrapped in a standalone page that inlines build_textbook.CSS (reused
wholesale so it cannot drift) and loads KaTeX from cdnjs (the CDN Claude.ai artifacts may use).
Codes are disjoint from the .svg codes, so <code>.svg and <code>.html never coexist.

  python _verification/build_viz_artifacts.py            # (re)write the .html artifacts
  python _verification/build_viz_artifacts.py --check     # verify committed artifacts are current
"""
import argparse, glob, html as _html, importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
VIZ_DIR = os.path.join(HERE, "viz")
FIG_DIR = os.path.join(REPO_ROOT, "algebra-1-tutor", "figures")

sys.path.insert(0, HERE)
import viz_figures as _vf
import build_textbook as _bt

KATEX = _bt.KATEX
_CDNJS = "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/" + KATEX

# Assembled by .replace (NOT .format): build_textbook.CSS and the viz bodies contain literal { } and $$.
_HEAD = (
    "<!doctype html>\n<html lang=\"en\">\n<head>\n"
    "<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
    "<title>Figure __CODE__</title>\n"
    "<link rel=\"stylesheet\" href=\"" + _CDNJS + "/katex.min.css\">\n"
    "<style>\n__CSS__\n"
    ".fig-standalone{max-width:760px;margin:1.4rem auto;padding:0 1rem}\n"
    "</style>\n"
    "<script>try{if(window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches)"
    "document.documentElement.classList.add('dark');}catch(e){}</script>\n"
    "</head>\n<body data-surface=\"textbook\">\n<main class=\"fig-standalone\">\n"
)
_TAIL = (
    "\n</main>\n"
    "<script defer src=\"" + _CDNJS + "/katex.min.js\"></script>\n"
    "<script defer src=\"" + _CDNJS + "/contrib/auto-render.min.js\"></script>\n"
    "<script>\ndocument.addEventListener('DOMContentLoaded', function () {\n"
    "  if (typeof renderMathInElement === 'function') {\n"
    "    renderMathInElement(document.body, {delimiters: ["
    "{left: '$$', right: '$$', display: true}, {left: '\\\\(', right: '\\\\)', display: false}],"
    " throwOnError: false});\n  }\n});\n</script>\n</body>\n</html>\n"
)

_MOD_CACHE = {}


def _module(name):
    if name not in _MOD_CACHE:
        fp = os.path.join(VIZ_DIR, name + ".py")
        spec = importlib.util.spec_from_file_location("bva_" + name, fp)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        _MOD_CACHE[name] = m
    return _MOD_CACHE[name]


def _entry(code):
    for e in _vf.VIZ_FIGURES:
        if e["code"] == code:
            return e
    raise KeyError("no viz figure with code " + code)


def figure_body(code):
    """The raw sample html for a viz code (the inline SVG/HTML/JS, before wrapping)."""
    e = _entry(code)
    return _module(e["module"]).samples()[int(e["index"])]["html"]


def _caption(code):
    e = _entry(code)
    cap = _module(e["module"]).samples()[int(e["index"])].get("caption", "")
    return (" &mdash; " + _html.escape(cap)) if cap else ""


def render_page(code):
    """Full standalone HTML document for a viz code."""
    fig = ('<figure class="fig viz" id="fig-' + code + '">' + figure_body(code)
           + '<figcaption><b>Figure ' + code + '</b>' + _caption(code) + '</figcaption></figure>')
    head = _HEAD.replace("__CODE__", code).replace("__CSS__", _bt.CSS)
    return head + fig + _TAIL


def codes():
    return [e["code"] for e in _vf.VIZ_FIGURES]
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd _verification && python -m pytest tests/test_viz_artifacts.py -q`
Expected: PASS (3 passed)

- [ ] **Step 5: Commit**

```bash
git add _verification/build_viz_artifacts.py _verification/tests/test_viz_artifacts.py
git commit -m "feat: viz-figure artifact generator core (render_page)"
```

---

## Task 2: `build()` + `--check` (byte-deterministic) + 1:1 registry↔file lint

**Files:**
- Modify: `_verification/build_viz_artifacts.py` (append `build`, `check`, `main`)
- Test: `_verification/tests/test_viz_artifacts.py` (append)

- [ ] **Step 1: Write the failing test**

```python
def test_check_passes_after_build(tmp_path, monkeypatch):
    # building then checking must be clean and deterministic
    bva.build()
    assert bva.check() == []


def test_check_detects_stale(monkeypatch):
    # if a file's content drifts, check() must report it
    import os
    bva.build()
    target = os.path.join(bva.FIG_DIR, "3.2.f1.html")
    original = open(target, encoding="utf-8").read()
    try:
        open(target, "w", encoding="utf-8").write(original + "<!--drift-->")
        issues = bva.check()
        assert any("3.2.f1.html" in i for i in issues)
    finally:
        open(target, "w", encoding="utf-8").write(original)


def test_one_to_one_with_registry():
    bva.build()
    import glob, os
    on_disk = {os.path.splitext(os.path.basename(p))[0]
               for p in glob.glob(os.path.join(bva.FIG_DIR, "*.html"))}
    assert on_disk == set(bva.codes())
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd _verification && python -m pytest tests/test_viz_artifacts.py -k "check or one_to_one" -q`
Expected: FAIL with `AttributeError: module 'build_viz_artifacts' has no attribute 'build'`

- [ ] **Step 3: Write minimal implementation** (append to `build_viz_artifacts.py`)

```python
def build():
    """Write algebra-1-tutor/figures/<code>.html for every viz code. Returns the count."""
    os.makedirs(FIG_DIR, exist_ok=True)
    for code in codes():
        with open(os.path.join(FIG_DIR, code + ".html"), "w", encoding="utf-8", newline="\n") as f:
            f.write(render_page(code))
    return len(codes())


def check():
    """Verify every committed <code>.html matches a fresh render and there are no orphans."""
    issues = []
    want = set(codes())
    for code in sorted(want):
        p = os.path.join(FIG_DIR, code + ".html")
        if not os.path.exists(p):
            issues.append(code + ".html: missing (run build_viz_artifacts.py)")
            continue
        on_disk = open(p, encoding="utf-8").read().replace("\r\n", "\n")
        if on_disk != render_page(code):
            issues.append(code + ".html: content differs from source (run build_viz_artifacts.py)")
    have = {os.path.splitext(os.path.basename(p))[0]
            for p in glob.glob(os.path.join(FIG_DIR, "*.html"))}
    for orphan in sorted(have - want):
        issues.append(orphan + ".html: bundled but has no viz_figures entry")
    return issues


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if a.check:
        iss = check()
        if iss:
            print("FAIL:\n  " + "\n  ".join(iss)); return 1
        print("viz artifacts: " + str(len(codes())) + " figures bundled as .html; current."); return 0
    n = build(); print("built " + str(n) + " viz-figure .html artifacts in algebra-1-tutor/figures/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd _verification && python -m pytest tests/test_viz_artifacts.py -q`
Expected: PASS (6 passed). NOTE: this build step also writes the 40 `.html` files into `algebra-1-tutor/figures/` — leave them; Task 3 commits them.

- [ ] **Step 5: Commit (code only; generated files in Task 3)**

```bash
git add _verification/build_viz_artifacts.py _verification/tests/test_viz_artifacts.py
git commit -m "feat: viz-artifact build + --check + 1:1 registry lint"
```

---

## Task 3: Generate and commit the 40 artifacts

**Files:**
- Create (generated): `algebra-1-tutor/figures/<code>.html` × 40

- [ ] **Step 1: Generate**

Run: `python _verification/build_viz_artifacts.py`
Expected: `built 40 viz-figure .html artifacts in algebra-1-tutor/figures/.`

- [ ] **Step 2: Verify check is clean**

Run: `python _verification/build_viz_artifacts.py --check`
Expected: `viz artifacts: 40 figures bundled as .html; current.`

- [ ] **Step 3: Sanity-spot one file**

Run: `python -c "import sys;sys.path.insert(0,'_verification');import build_viz_artifacts as b;print(b.render_page('3.2.f1')[:120])"`
Expected: starts with `<!doctype html>` and a `<title>Figure 3.2.f1</title>`.

- [ ] **Step 4: Pin `.html` under figures to LF in .gitattributes**

Confirm `.gitattributes` already pins `algebra-1-tutor/figures/*.svg eol=lf`; add an analogous line so the committed `.html` stays LF cross-OS:

```
algebra-1-tutor/figures/*.html eol=lf
```
(If a broader `*.html eol=lf` rule already exists, skip.)

- [ ] **Step 5: Commit**

```bash
git add algebra-1-tutor/figures/*.html .gitattributes
git commit -m "feat: bundle 40 viz-figure .html artifacts into the skill"
```

---

## Task 4: Package `.html` into the skill `.zip` (`build_skill.py`)

**Files:**
- Modify: `_verification/build_skill.py:19` (`_TEXT_EXT`)
- Modify: `_verification/tests/test_skill_package.py` (figure count)

- [ ] **Step 1: Update the failing test first**

In `_verification/tests/test_skill_package.py`, change the figure-count assertion to count svg + html:

```python
    figs = [n for n in names if "/figures/" in n]
    assert sum(1 for n in figs if n.endswith(".svg")) == 23      # deterministic SVGs
    assert sum(1 for n in figs if n.endswith(".html")) == 40     # viz-figure artifacts
```

- [ ] **Step 2: Run to verify it fails**

Run: `cd _verification && python -m pytest tests/test_skill_package.py -q`
Expected: FAIL — zip lacks the 40 `.html` (and/or `test_skill_zip_current` flags them stale).

- [ ] **Step 3: Implement — add `.html` to `_TEXT_EXT`**

`_verification/build_skill.py:19`:
```python
_TEXT_EXT = (".md", ".svg", ".txt", ".html")
```
(`_files()` already globs every file under the skill dir, so the `.html` artifacts are picked up automatically; adding the extension only ensures LF-normalization → deterministic zip.)

- [ ] **Step 4: Rebuild the zip and verify**

Run: `python _verification/build_skill.py && cd _verification && python -m pytest tests/test_skill_package.py -q`
Expected: rebuild prints `built … (N files).` with N = previous + 40; pytest PASS.

- [ ] **Step 5: Commit**

```bash
git add _verification/build_skill.py _verification/tests/test_skill_package.py algebra-1-tutor.zip
git commit -m "feat: package viz-figure .html artifacts into the skill zip"
```

---

## Task 5: CI gate — `figure_lint` also enforces viz artifact freshness

**Files:**
- Modify: `_verification/check_alignment.py` (`figure_lint`)
- Test: `_verification/tests/test_figures.py` (extend `test_figure_lint_clean` already covers; add a viz assertion)

- [ ] **Step 1: Write the failing test** (append to `test_figures.py`)

```python
def test_figure_lint_covers_viz_artifacts():
    import check_alignment as ca, build_viz_artifacts as bva, os
    bva.build()
    assert ca.figure_lint() == []
    # the lint must FAIL if a viz artifact goes stale
    p = os.path.join(bva.FIG_DIR, "3.2.f1.html")
    orig = open(p, encoding="utf-8").read()
    try:
        open(p, "w", encoding="utf-8").write(orig + "<!--x-->")
        assert any("3.2.f1.html" in i for i in ca.figure_lint())
    finally:
        open(p, "w", encoding="utf-8").write(orig)
```

- [ ] **Step 2: Run to verify it fails**

Run: `cd _verification && python -m pytest tests/test_figures.py::test_figure_lint_covers_viz_artifacts -q`
Expected: FAIL — `figure_lint` doesn't yet check viz artifacts.

- [ ] **Step 3: Implement — fold viz check into `figure_lint`**

In `_verification/check_alignment.py`, inside `figure_lint()`, before `return issues` add:

```python
    import build_viz_artifacts as _bva
    issues += _bva.check()
```

- [ ] **Step 4: Run to verify it passes**

Run: `cd _verification && python -m pytest tests/test_figures.py -q`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add _verification/check_alignment.py _verification/tests/test_figures.py
git commit -m "feat: figure_lint enforces viz-artifact freshness"
```

---

## Task 6: smoke_test resolves every viz code to a bundled artifact

**Files:**
- Modify: `_verification/smoke_test.py`

- [ ] **Step 1: Write the failing assertion into smoke_test**

In `check()`, after the existing figure block (after line ~50), add a viz-resolution block:

```python
    # 2b. every viz figure resolves to a bundled .html artifact AND is embedded in its lesson page
    bva = _imp("build_viz_artifacts")
    for e in __import__("viz_figures").VIZ_FIGURES:
        code = e["code"]
        if not os.path.exists(os.path.join(REPO_ROOT, "algebra-1-tutor", "figures", code + ".html")):
            issues.append(f"viz figure {code} has no bundled .html artifact")
        lesson = code.rsplit(".f", 1)[0]            # "3.2.f1" -> "3.2", "5.0.f1" -> "5.0"
        p = os.path.join(tb.OUT_DIR, tb._lesson_fname(lesson))
        if os.path.exists(p) and f'id="fig-{code}"' not in open(p, encoding="utf-8").read():
            issues.append(f"viz figure {code} not embedded in {os.path.basename(p)}")
```

- [ ] **Step 2: Run to verify current state**

Run: `python _verification/build_viz_artifacts.py && python _verification/smoke_test.py`
Expected: `[OK]` line. (If a `<unit>.0` overview lesson has no own page, `_lesson_fname` maps it to the unit page — the `os.path.exists(p)` guard prevents false failures; confirm no new issues are printed.)

- [ ] **Step 3: Commit**

```bash
git add _verification/smoke_test.py
git commit -m "feat: smoke_test resolves every viz figure to a bundled artifact"
```

---

## Task 7: SKILL.md — emit viz artifacts, never refuse a resolvable code

**Files:**
- Modify: `algebra-1-tutor/SKILL.md` (lines ~131 and ~240)
- Repackage: `algebra-1-tutor.zip`

- [ ] **Step 1: Rewrite the "Prefer a bundled figure" guidance (~line 131)**

Replace the existing bullet with (keep surrounding bullets intact):

```markdown
- **Prefer a bundled figure when one exists.** Most figures have a pre-generated, math-verified file bundled in `figures/`, keyed by reference code. Two kinds: a `.svg` (deterministic graph — emit its contents as an Artifact) or a `.html` (an interactive/explanatory figure — emit its contents as an **HTML Artifact**; the widget stays live and the math renders via KaTeX). Look up the code's file in `figures/`; the math is already checked, so don't recompute or redraw it. Compute a fresh graph (below) only when no bundled figure fits.
```

- [ ] **Step 2: Rewrite the figure-code resolution recipe (~line 240)**

Replace the existing sentence(s) with:

```markdown
If a student gives a figure code (`f…`), resolve it from `figures/`: read `figures/<code>.svg` and emit it as an Artifact, or — if there is no `.svg` — read `figures/<code>.html` and emit it as an **HTML Artifact** (these are the interactive/explanatory figures; they stay live and the math is pre-rendered). Every numbered figure in the course has one of these files, so a real `f` code always resolves — never tell a student a figure "doesn't exist" or refuse to show it. Only on the rare chance that neither file is present, describe the picture from `visuals.md` instead of inventing one.
```

- [ ] **Step 3: Verify no refusal language remains**

Run: `grep -n "doesn't exist\|hasn't been added\|won't invent\|invent one\|may be a figure" algebra-1-tutor/SKILL.md`
Expected: no match implying refusal of a resolvable code (the only `invent` reference is the "rather than inventing one" fallback, which is acceptable).

- [ ] **Step 4: Repackage and verify**

Run: `python _verification/build_skill.py && python _verification/build_skill.py --check`
Expected: rebuild then `skill package: algebra-1-tutor.zip current (… files).`

- [ ] **Step 5: Commit**

```bash
git add algebra-1-tutor/SKILL.md algebra-1-tutor.zip
git commit -m "feat: SKILL.md emits viz-figure artifacts and never refuses a resolvable code"
```

---

## Task 8: CircleCI runs the viz-artifact `--check`

**Files:**
- Modify: `.circleci/config.yml` (after the `viz_figures.py --check` step, ~line 28)

- [ ] **Step 1: Add the step**

After the existing "Viz figures coded + sympy-vetted…" run block, insert:

```yaml
      - run:
          name: Viz figure artifacts bundled + current
          command: python _verification/build_viz_artifacts.py --check
```

- [ ] **Step 2: Lint the YAML locally**

Run: `python -c "import yaml;yaml.safe_load(open('.circleci/config.yml'))"`
Expected: no exception.

- [ ] **Step 3: Commit**

```bash
git add .circleci/config.yml
git commit -m "ci: gate viz-figure artifact freshness"
```

---

## Task 9: Visual verification of all 40 artifacts (ultracode Workflow)

**Files:** none committed unless a fidelity fix is needed (then `build_viz_artifacts.py` `_HEAD`/`_TAIL` or the inlined CSS hook).

This is the verification muscle `--check` cannot provide: confirm each artifact *looks* right standalone, in light and dark, and that the 6 interactive widgets respond.

- [ ] **Step 1: Build artifacts** — `python _verification/build_viz_artifacts.py`

- [ ] **Step 2: Run a Workflow** — one agent per figure (pipeline). Each agent:
  1. Writes a dark-variant copy: same file with `<html lang="en" class="dark">` (don't rely on `prefers-color-scheme` in headless).
  2. Screenshots both via Windows Edge headless — the reliable recipe (see memory `algebra-textbook-image-pipeline`):
     `Start-Process -FilePath msedge -ArgumentList @('--headless','--disable-gpu','--no-sandbox','--user-data-dir=<tmp>','--window-size=820,900','--virtual-time-budget=9000','--screenshot=<out.png>','<file-url>') -Wait`
     (no `?query` on a `file://` URL — it breaks loading; use a separate dark file.)
  3. Reads its own PNGs and checks: figure visible & centered, text legible on the paper/dark background, no raw `$$`/`\frac` leaking (KaTeX rendered), no clipping. For the 6 interactive codes, also confirm the control (slider/buttons) is present in the screenshot.
  4. Returns a structured verdict `{code, light_ok, dark_ok, katex_ok, interactive_ok, notes}`.
- [ ] **Step 3:** Collect verdicts. For any failure, fix in `build_viz_artifacts.py` (e.g. dark-mode hook, max-height, padding), rebuild, re-verify only the failing codes.
- [ ] **Step 4: Commit** any generator fix + regenerated artifacts:

```bash
git add _verification/build_viz_artifacts.py algebra-1-tutor/figures/*.html algebra-1-tutor.zip
git commit -m "fix: viz-artifact rendering fidelity (light/dark/katex/interactive)"
```

---

## Task 10: Full gate + CI-image determinism + ship

**Files:** memory update; PR.

- [ ] **Step 1: Full local gate**

Run (from repo root):
```bash
python _verification/build_viz_artifacts.py --check
python _verification/viz_figures.py --check
python _verification/figures.py --check
python _verification/build_textbook.py --check
python _verification/build_skill.py --check
python _verification/smoke_test.py
cd _verification && python -m pytest -q && cd ..
```
Expected: every step green; pytest all pass.

- [ ] **Step 2: Determinism in the CI image** (catches any patch-version HTML drift)

Run from **PowerShell** (not Git Bash — MSYS mangles `-w /work`):
```powershell
docker run --rm -v ${PWD}:/work -w /work cimg/python:3.11 bash -lc "pip install -q -r requirements.txt && python _verification/build_viz_artifacts.py --check && python _verification/build_skill.py --check"
```
Expected: both `--check` report current. (In-container `git` may fail on a worktree — that's expected, not a failure.)

- [ ] **Step 3: Push under a clean branch name (no `+`) and open the PR**

```bash
git push origin HEAD:textbook/viz-figures-in-skill
gh pr create --title "Bundle viz figures as tutor artifacts" --body "<summary + human action items>"
```

- [ ] **Step 4: Poll CI** via the circleci MCP `get_latest_pipeline_status` for branch `textbook/viz-figures-in-skill`; confirm green. (`gh pr view --json mergeable` computes async; `UNKNOWN` ≠ conflict.)

- [ ] **Step 5: Update memory** — append to `algebra-1-tutor-skill.md` (and cross-link `algebra-textbook-image-pipeline.md`): the viz figures are now bundled as `.html` artifacts; SKILL.md resolution emits svg-or-html and never refuses a resolvable code; the new generator + gate; the cdnjs-KaTeX decision; **human action item: re-upload `algebra-1-tutor.zip` on Claude.ai** for the new behavior to take effect.

- [ ] **Step 6: PR body must list the two human action items**: (1) re-upload the rebuilt `.zip` on Claude.ai; (2) the cdnjs-KaTeX dependency for math in artifacts (degrades to raw `$$` if a sandbox ever blocks it).

---

## Self-review notes
- **Spec coverage:** generator (T1–T3) ✓; KaTeX cdnjs (T1) ✓; SKILL.md rewrite + no-refusal (T7) ✓; packaging (T4) ✓; gates figure_lint/smoke/pytest/CI (T5,6,8) ✓; Workflow visual verify (T9) ✓; determinism + ship + memory (T10) ✓. Non-goals respected (no figure re-authoring, no raster bundling).
- **Brace hazard:** every page assembly uses `.replace`, never `.format`/f-strings (T1). ✓
- **Naming consistency:** `render_page`, `figure_body`, `build`, `check`, `codes`, `FIG_DIR`, `KATEX` used identically across T1–T6. ✓
- **Count consistency:** 40 viz figures / 23 SVGs asserted in T4 test and smoke_test; if the branch's `VIZ_FIGURES` length differs at execution time, treat the registry length as truth and update the literal `40`/`23` in T4's test to match (single source: `len(viz_figures.VIZ_FIGURES)` and the `*.svg` glob count).
