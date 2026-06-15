# Reference-code → Tutor Launcher Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn every reference-code badge in the student HTML textbook (`docs/textbook/`) into a one-click tutor launcher — hover/focus shows a ready-to-paste prompt, clicking copies it with a toast — and teach `SKILL.md` to respond to such a pasted prompt by resolving the code silently and asking how the student wants to work it.

**Architecture:** All HTML/CSS/JS is emitted by `_verification/build_textbook.py` (the sole writer of `docs/textbook/`, byte-deterministically). A new `launcher` flag confines the enhanced badge markup to the textbook; new CSS is scoped under `body[data-surface="textbook"]`; one shared `position:fixed` tooltip + toast + a delegated vanilla-JS controller live in the textbook-only `_lesson_page` template. The skill change is additive prose in `SKILL.md`, then `build_skill.py` repackages the `.zip`.

**Tech Stack:** Python 3.11 + `markdown==3.7`; vanilla JS (no deps); pytest. CI compares generated `docs/` byte-for-byte across CPython 3.11.9 (local) and 3.11.15 (`cimg/python:3.11`).

**Spec:** `docs/superpowers/specs/2026-06-14-refcode-tutor-launcher-design.md`

**Working dir:** `C:/Users/18084/algebra/.claude/worktrees/refcode-tutor-launcher` (branch `worktree-refcode-tutor-launcher`). Run pytest as `python -m pytest _verification/tests -q` from the repo root.

---

## File structure

- **Modify** `_verification/build_textbook.py` — add `_label_for`/`_prompt_for`/`_refcode_badge`; `launcher` param on `_convert_anchors`/`md_to_body`; `launcher=True` at the 3 textbook `md_to_body` calls; inject `#rc-tip`/`#rc-toast` + `_REFCODE_JS` into `_lesson_page`; add scoped CSS to the `CSS` constant.
- **Modify** `_verification/tests/test_textbook.py` — add unit + page-level tests.
- **Modify** `algebra-1-tutor/SKILL.md` — additive "Arriving from the textbook" subsection.
- **Regenerate** `docs/textbook/*.html` + `docs/textbook/textbook.css` (and any other surface CSS via `build_all.py`) and `algebra-1-tutor.zip`.

---

### Task 1: Prompt-generation pure functions

**Files:** Modify `_verification/build_textbook.py` (after the `FCODE_RE` line, ~line 25); Test `_verification/tests/test_textbook.py`.

- [ ] **Step 1: Write failing tests** — append to `test_textbook.py`:

```python
def test_label_for_kinds():
    assert bt._label_for("12.5.w2") == "worked example 2 in Lesson 12.5"
    assert bt._label_for("12.5.7") == "practice problem 7 in Lesson 12.5"
    assert bt._label_for("8.2.5b") == "practice problem 5, part b in Lesson 8.2"
    assert bt._label_for("1.1.d1") == "a key term in Lesson 1.1"
    assert bt._label_for("1.1.c1") == "a check-for-understanding question in Lesson 1.1"
    assert bt._label_for("12.6.f1") == "the figure in Lesson 12.6"
    assert bt._label_for("A.2.f1") == "the figure in Lesson A.2"
    assert bt._label_for("mis.3") == "reference mis.3"          # bank code -> fallback
    assert bt._label_for("vis.t1") == "reference vis.t1"


def test_prompt_for_shape():
    p = bt._prompt_for("12.5.w2")
    assert p.startswith("Use the Algebra 1 tutor skill to help me with worked example 2 in Lesson 12.5")
    assert "(reference 12.5.w2)" in p
    assert "explain it, work through it together, or answer a specific question." in p
```

- [ ] **Step 2: Run, verify fail** — `python -m pytest _verification/tests/test_textbook.py -q -k "label_for or prompt_for"` → FAIL (`AttributeError: module 'build_textbook' has no attribute '_label_for'`).

- [ ] **Step 3: Implement** — insert after `FCODE_RE = ...`:

```python
_CODE_RE = re.compile(r"^([0-9]+|[A-Z])\.(\d+)\.(.+)$")  # scope.lesson.item (3-part lesson codes only)


def _label_for(code):
    """Plain-words description of a reference code, for the launcher prompt. Pure function of the
    code string (no SSOT lookup) so the generated prompt is deterministic. Two-part bank codes
    (mis.3, vis.t1, met.<slug>) fall back to the bare code."""
    m = _CODE_RE.match(code)
    if not m:
        return f"reference {code}"
    scope, lesson, item = m.groups()
    clause = f" in Lesson {scope}.{lesson}"
    mw = re.match(r"^(?:w|ex)(\d+)([a-z]?)$", item)
    if mw:
        return f"worked example {mw.group(1)}" + (f", part {mw.group(2)}" if mw.group(2) else "") + clause
    mp = re.match(r"^(\d+)([a-z]?)$", item)
    if mp:
        return f"practice problem {mp.group(1)}" + (f", part {mp.group(2)}" if mp.group(2) else "") + clause
    if re.match(r"^d\d+$", item):
        return "a key term" + clause
    if re.match(r"^c\d+$", item):
        return "a check-for-understanding question" + clause
    if re.match(r"^f\d+[a-z]?$", item):
        return "the figure" + clause
    if re.match(r"^h\d+$", item):
        return "a how-to" + clause
    return f"reference {code}" + clause


def _prompt_for(code):
    """The ready-to-paste tutor-launch prompt for a reference code."""
    return (f"Use the Algebra 1 tutor skill to help me with {_label_for(code)} "
            f"(reference {code}). Pull it up, then ask whether I'd like you to explain it, "
            f"work through it together, or answer a specific question.")
```

- [ ] **Step 4: Run, verify pass** — same command → PASS.

- [ ] **Step 5: Commit**

```bash
git add _verification/build_textbook.py _verification/tests/test_textbook.py
git commit -m "feat(textbook): reference-code launcher prompt generation (_label_for/_prompt_for)"
```

---

### Task 2: Launcher-aware badge markup

**Files:** Modify `_verification/build_textbook.py` (`_convert_anchors` ~line 91, `md_to_body` ~line 243); Test `test_textbook.py`.

- [ ] **Step 1: Write failing tests**

```python
def test_badge_launcher_attrs():
    html = bt.md_to_body("See {#12.5.w2} here.", launcher=True)
    assert 'class="refcode" id="12.5.w2" href="#12.5.w2"' in html
    assert 'data-prompt="Use the Algebra 1 tutor skill to help me with worked example 2' in html
    assert 'aria-label="Copy a tutor prompt for worked example 2 in Lesson 12.5"' in html


def test_badge_plain_by_default():
    html = bt.md_to_body("See {#12.5.w2} here.")          # launcher defaults False
    assert 'class="refcode" id="12.5.w2" href="#12.5.w2">12.5.w2</a>' in html
    assert "data-prompt" not in html and "aria-label" not in html
```

- [ ] **Step 2: Run, verify fail** — `python -m pytest _verification/tests/test_textbook.py -q -k "badge"` → FAIL (`md_to_body() got an unexpected keyword argument 'launcher'`).

- [ ] **Step 3: Implement** — replace `_convert_anchors` (keep the figure-embed loop) and add `_refcode_badge` above it:

```python
def _refcode_badge(code, launcher):
    """The visible, linkable refcode badge. When launcher=True it also carries the tutor-launch
    prompt (data-prompt) + an aria-label so the textbook's refcode script can show and copy it."""
    base = f'<a class="refcode" id="{code}" href="#{code}"'
    if not launcher:
        return base + f">{code}</a>"
    prompt = _html.escape(_prompt_for(code), quote=True)
    aria = _html.escape("Copy a tutor prompt for " + _label_for(code), quote=True)
    return base + f' data-prompt="{prompt}" aria-label="{aria}">{code}</a>'


def _convert_anchors(text, launcher=False):
    """Turn {#code} into a visible, linkable refcode badge; embed the bundled SVG for f-codes.
    launcher=True (the HTML textbook) also attaches the tutor-launcher prompt to each badge."""
    out = []
    for ln in text.split("\n"):
        fcodes = [c for c in ANCHOR_RE.findall(ln)
                  if FCODE_RE.match(c) and os.path.exists(os.path.join(FIG_DIR, c + ".svg"))]
        ln = ANCHOR_RE.sub(lambda m: _refcode_badge(m.group(1), launcher), ln)
        out.append(ln)
        for c in fcodes:
            svg = open(os.path.join(FIG_DIR, c + ".svg"), encoding="utf-8").read().strip()
            out += ["", f'<figure class="fig" id="fig-{c}">{svg}<figcaption><b>Figure {c}</b></figcaption></figure>', ""]
    return "\n".join(out)
```

Change `md_to_body` signature + the `_convert_anchors` call:

```python
def md_to_body(text, launcher=False):
    text, math = _protect_math(text)
    text = _id_worked_practice(text)
    text = _convert_anchors(text, launcher)
    text = _space_subheads(text)
    text = _blockify(text)
    text = _ensure_list_blank_lines(text)
    body = mdlib.markdown(text, extensions=["extra", "sane_lists", "toc", "md_in_html"], output_format="html5")
    body = body.replace(' markdown="1"', '')
    body = body.replace("<hr />", _DIVIDER).replace("<hr>", _DIVIDER)
    body = body.replace(chr(92) + "$", "$")
    return _restore_math(body, math)
```

- [ ] **Step 4: Run, verify pass** — `python -m pytest _verification/tests/test_textbook.py -q -k "badge"` → PASS.

- [ ] **Step 5: Commit**

```bash
git add _verification/build_textbook.py _verification/tests/test_textbook.py
git commit -m "feat(textbook): launcher-aware refcode badge (data-prompt + aria-label, gated by launcher flag)"
```

---

### Task 3: Wire the textbook — flag the build calls, inject tooltip/toast/JS, add scoped CSS

**Files:** Modify `_verification/build_textbook.py` (3 call sites ~735/774/786; `_lesson_page` ~331–396; `CSS` constant end ~711; new `_REFCODE_JS` constant ~before `_lesson_page`); Test `test_textbook.py`.

- [ ] **Step 1: Write failing tests** (operate on the in-memory build, not committed files)

```python
def _built():
    return bt.build_site(bt._ssot())


def test_shared_elements_once_per_textbook_page():
    files = _built()
    page = files["unit-12-5.html"]
    assert page.count('id="rc-tip"') == 1 and page.count('id="rc-toast"') == 1
    assert "data-prompt=" in page                          # lesson badges carry the prompt
    # the unit index also routes through _lesson_page, so it gets the shared elements too
    assert files["index.html"].count('id="rc-toast"') == 1


def test_refcode_controller_present():
    page = _built()["unit-12-5.html"]
    assert "navigator.clipboard" in page and 'closest(".refcode")' in page


def test_launcher_css_scoped():
    css = _built()["textbook.css"]
    assert 'body[data-surface="textbook"] .refcode{cursor:copy}' in css
    assert "#rc-tip" in css and "#rc-toast" in css
```

- [ ] **Step 2: Run, verify fail** — `python -m pytest _verification/tests/test_textbook.py -q -k "shared_elements or controller or css_scoped"` → FAIL.

- [ ] **Step 3a: Flag the three textbook `md_to_body` calls** — `launcher=True`:
  - `_intro_page` (~735): `body = _strip_lead(md_to_body(md, launcher=True), "h1")`
  - overview intro (~774): `intro_html = _strip_lead(md_to_body(intro, launcher=True), "h1")`
  - lesson body (~786): `lbody = _strip_lead(md_to_body(chunk, launcher=True), "h2")`

- [ ] **Step 3b: Add `_REFCODE_JS` constant** immediately before `def _lesson_page(`:

```python
# delegated controller for the reference-code tutor launcher (textbook pages only). Vanilla JS,
# no deps; event-delegated so it covers every .refcode badge; a position:fixed tooltip escapes the
# overflow:hidden on .worked/.answers cards. Defined as a plain string so its braces stay literal.
_REFCODE_JS = r"""
(function () {
  var tip = document.getElementById("rc-tip"), toast = document.getElementById("rc-toast");
  if (!tip || !toast) return;
  var toastT = 0;
  function hideTip() { tip.classList.remove("show"); tip.setAttribute("aria-hidden", "true"); }
  function showTip(a) {
    var p = a.getAttribute("data-prompt"); if (!p) return;
    tip.textContent = "";
    var h = document.createElement("span"); h.className = "rc-tip-h";
    h.textContent = "Tutor prompt (click the code to copy):";
    var q = document.createElement("span"); q.className = "rc-tip-q"; q.textContent = p;
    tip.appendChild(h); tip.appendChild(q);
    tip.setAttribute("aria-hidden", "false"); tip.classList.add("show");
    var r = a.getBoundingClientRect(), t = tip.getBoundingClientRect();
    var top = r.top - t.height - 8; if (top < 8) top = r.bottom + 8;
    var left = Math.max(8, Math.min(r.left + r.width / 2 - t.width / 2, window.innerWidth - t.width - 8));
    tip.style.top = top + "px"; tip.style.left = left + "px";
  }
  function showToast(msg) {
    toast.textContent = msg; toast.classList.add("show"); toast.setAttribute("aria-hidden", "false");
    if (toastT) clearTimeout(toastT);
    toastT = setTimeout(function () {
      toast.classList.remove("show"); toast.setAttribute("aria-hidden", "true");
    }, 2600);
  }
  function fallbackCopy(text, ok) {
    try {
      var ta = document.createElement("textarea"); ta.value = text;
      ta.style.position = "fixed"; ta.style.top = "-1000px"; ta.style.opacity = "0";
      document.body.appendChild(ta); ta.focus(); ta.select();
      var done = document.execCommand("copy"); document.body.removeChild(ta);
      if (done) { ok(); } else { showToast("Select the prompt above and copy it."); }
    } catch (e) { showToast("Select the prompt above and copy it."); }
  }
  function copyText(text, ok) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(ok, function () { fallbackCopy(text, ok); });
    } else { fallbackCopy(text, ok); }
  }
  document.addEventListener("pointerover", function (e) {
    var a = e.target.closest && e.target.closest(".refcode"); if (a) showTip(a);
  });
  document.addEventListener("pointerout", function (e) {
    var a = e.target.closest && e.target.closest(".refcode");
    if (a && !a.contains(e.relatedTarget)) hideTip();
  });
  document.addEventListener("focusin", function (e) {
    var a = e.target.closest && e.target.closest(".refcode"); if (a) showTip(a);
  });
  document.addEventListener("focusout", function (e) {
    if (e.target.closest && e.target.closest(".refcode")) hideTip();
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") hideTip(); });
  window.addEventListener("scroll", hideTip, true);
  window.addEventListener("resize", hideTip);
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest(".refcode"); if (!a) return;
    e.preventDefault();
    copyText(a.getAttribute("data-prompt") || a.textContent, function () {
      showToast("Copied. Paste it into Claude to start.");
    });
  });
})();
"""
```

- [ ] **Step 3c: Inject the shared elements + controller into `_lesson_page`.** In the returned template, after the `</div>` that closes `.shell` and before the first KaTeX `<script defer ...>`, add:

```html
<div id="rc-tip" role="tooltip" aria-hidden="true"></div>
<div id="rc-toast" role="status" aria-live="polite" aria-hidden="true"></div>
```

And immediately before `</body>` (after the existing inline `</script>`), add:

```html
<script>{_REFCODE_JS}</script>
```

(The `{_REFCODE_JS}` interpolates the plain-string constant into the f-string; its braces are literal because they live in the value, not the f-string literal. The existing brace-escaped inline script is left untouched.)

- [ ] **Step 3d: Add scoped CSS** at the end of the `CSS` constant, just before the closing `"""`:

```css

/* ---- reference-code tutor launcher (textbook surface only) ---- */
body[data-surface="textbook"] .refcode{cursor:copy}
body[data-surface="textbook"] #rc-tip{position:fixed; z-index:80; max-width:min(92vw,30rem); margin:0;
  padding:.6rem .8rem; background:var(--card); color:var(--ink); border:1px solid var(--rule);
  border-radius:var(--radius-sm); box-shadow:var(--shadow);
  font:var(--step--1)/1.5 "Source Serif 4",var(--serif-math),Georgia,serif;
  opacity:0; visibility:hidden; pointer-events:none}
body[data-surface="textbook"] #rc-tip.show{opacity:1; visibility:visible}
body[data-surface="textbook"] #rc-tip .rc-tip-h{display:block; font-weight:600; font-size:.82em;
  letter-spacing:.01em; color:var(--ink-soft); margin-bottom:.25rem}
body[data-surface="textbook"] #rc-tip .rc-tip-q{display:block; color:var(--ink)}
body[data-surface="textbook"] #rc-toast{position:fixed; left:50%; bottom:1.4rem; transform:translateX(-50%);
  z-index:90; background:var(--ink); color:var(--paper); border-radius:999px; padding:.55rem 1.1rem;
  font:var(--step--1)/1.3 "Source Serif 4",Georgia,serif; box-shadow:var(--shadow);
  opacity:0; visibility:hidden; pointer-events:none; max-width:92vw}
body[data-surface="textbook"] #rc-toast.show{opacity:1; visibility:visible}
@media (prefers-reduced-motion:no-preference){
  body[data-surface="textbook"] #rc-tip{transition:opacity .12s ease}
  body[data-surface="textbook"] #rc-toast{transition:opacity .18s ease, transform .18s ease}
  body[data-surface="textbook"] #rc-toast.show{transform:translateX(-50%) translateY(-2px)}
}
```

- [ ] **Step 4: Run, verify pass** — `python -m pytest _verification/tests/test_textbook.py -q -k "shared_elements or controller or css_scoped"` → PASS. (`test_check_clean` will now fail until Task 4 regenerates `docs/` — expected.)

- [ ] **Step 5: Commit**

```bash
git add _verification/build_textbook.py _verification/tests/test_textbook.py
git commit -m "feat(textbook): hover tooltip + click-to-copy controller, shared elements, scoped CSS"
```

---

### Task 4: Regenerate the textbook and re-green the full build gate

**Files:** Regenerate `docs/textbook/*` (+ any surface CSS).

- [ ] **Step 1:** `python _verification/build_all.py` (rebuilds textbook + guides + landing from source).
- [ ] **Step 2:** `python _verification/build_textbook.py --check` and `python _verification/build_all.py --check` → both print "current."
- [ ] **Step 3:** `python -m pytest _verification/tests -q` → all pass (incl. `test_check_clean`, `smoke_test`).
- [ ] **Step 4: Sanity-grep the output** — `git grep -c 'data-prompt' -- docs/textbook | head` shows many; `git grep -c 'data-prompt' -- docs/student-guide docs/tutor-guide docs/index.html` shows **none** (guides unaffected). Confirm `#rc-tip`/`#rc-toast` appear in each surface's CSS but the elements only in `docs/textbook/*.html`.
- [ ] **Step 5: Commit**

```bash
git add docs/
git commit -m "build(textbook): regenerate docs/ with the refcode tutor launcher"
```

---

### Task 5: Teach the skill, repackage the .zip

**Files:** Modify `algebra-1-tutor/SKILL.md` (in the "Reference codes" section, before its closing `---`); regenerate `algebra-1-tutor.zip`.

- [ ] **Step 1:** Insert, right after the figure-code paragraph that ends the "Resolving a code a student quotes" block and before the section's `---`:

```markdown

**Arriving from the textbook (the copy-paste launcher).** The HTML textbook turns every reference code into a one-click launcher: a student can copy a prompt like "Use the Algebra 1 tutor skill to help me with worked example 2 in Lesson 12.5 (reference 12.5.w2). Pull it up, then ask whether I'd like you to explain it, work through it together, or answer a specific question." When a message like that arrives:

1. **Resolve the code silently first, for your own reference.** Open the file it points to, find the item, and re-verify the math (the steps just above). Ground yourself in the exact item before you respond; don't paste the full solution yet.
2. **Ask how they want to work it:** have you explain it, work through it together, or answer a specific question they already have. If their message already says which, skip the question and go.
3. **Then teach** for the mode they chose, climbing the hint ladder and verifying before you assert, as always.
```

- [ ] **Step 2:** `python _verification/build_skill.py` → "built algebra-1-tutor.skill + .zip (N files)."
- [ ] **Step 3:** `python _verification/build_skill.py --check` → "current." and `python -m pytest _verification/tests/test_skill_package.py -q` → pass.
- [ ] **Step 4: Commit**

```bash
git add algebra-1-tutor/SKILL.md algebra-1-tutor.zip
git commit -m "feat(skill): respond to the textbook launcher prompt (resolve silently, then triage)"
```

---

### Task 6: Full gate + CI-image byte-determinism

- [ ] **Step 1:** Full suite — `python -m pytest _verification/tests -q` → all green.
- [ ] **Step 2:** Every `--check` gate — run each builder's `--check` and `check_alignment.py`, `check_textbook_src.py`, `verify_answers.py`, `verify_complementary.py`, `check_notation.py`, `smoke_test.py`. All pass.
- [ ] **Step 3: Reproduce CI's interpreter** (the byte-determinism trap that bit this repo before):

```bash
docker run --rm -v "C:/Users/18084/algebra/.claude/worktrees/refcode-tutor-launcher":/work -w /work \
  cimg/python:3.11 bash -lc "pip install -q markdown==3.7 pyyaml && python _verification/build_all.py && git status --porcelain"
```

Expected: empty output (no stale/changed files). If anything shows, fix the non-determinism, regenerate, recommit `docs/`.

- [ ] **Step 4:** No commit unless Step 3 changed files.

---

### Task 7: Adversarial review (ultracode workflow)

- [ ] **Step 1:** Run a review workflow: parallel agents each take one dimension — (a) byte-determinism / no `markdown="1"` residue / stable ordering, (b) HTML-escaping & injection safety of `data-prompt`/`aria-label`, (c) accessibility (keyboard, focus, Escape, `aria-live`, no-JS degradation, deep-link `id`s intact), (d) CSS scoping / no bleed to guides+landing, (e) clipboard fallback correctness, (f) test discriminating-power (fault injection), (g) `SKILL.md` house-voice + consistency with the existing recipe. Each returns structured findings; verify each real finding before acting.
- [ ] **Step 2:** Fix confirmed findings, re-run the gate, commit.

---

## Self-review (against the spec)

- **Spec §1 prompt generation →** Task 1. **§2 badge + launcher flag →** Task 2. **§3 tooltip/toast/JS + a11y →** Task 3. **§4 scoped CSS →** Task 3d. **§5 SKILL.md + repackage →** Task 5. **§6 determinism →** Task 4 + Task 6. **Testing →** Tasks 1–3 + 4/6. **Out-of-scope (guides untouched) →** verified in Task 4 Step 4. No gaps.
- **Placeholder scan:** every code/test/command step contains real content; no TBD/TODO.
- **Type/name consistency:** `_label_for`, `_prompt_for`, `_refcode_badge`, `_REFCODE_JS`, `launcher`, `#rc-tip`/`#rc-toast`/`.rc-tip-h`/`.rc-tip-q` used identically across tasks and CSS/JS.
