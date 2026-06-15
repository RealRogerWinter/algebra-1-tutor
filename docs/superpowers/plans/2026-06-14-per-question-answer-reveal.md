# Per-question Answer Reveal Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** In the student textbook, render each practice problem on its own row with an individual native reveal showing only that problem's answer, replacing the single end-of-lesson answer box (with graceful fallback for irregular sets).

**Architecture:** A build-only, lesson-aware transform in `_verification/build_textbook.py`. It runs inside `md_to_body` after reference-code badges are inserted but before `_blockify`. It builds a `{number → answer}` map from the lesson's `**Answer key**` block(s), splits each `**Practice problems:**` block into numbered problems, and — only when every shown problem number has a matching answer — rewrites the set to per-problem rows (each with a native `<details>` reveal) and deletes the consumed answer-key block(s). Irregular sets are left untouched for `_blockify` to render the old way. Problem/answer fragments are rendered to inline HTML up front (`_md_inline`) so no fragile `md_in_html` nesting is introduced.

**Tech Stack:** Python 3.11, `markdown` 3.7 (python-markdown), pytest. No new dependencies, no JavaScript.

---

## File structure

- **Modify** `_verification/build_textbook.py`
  - Add helpers: `_md_inline`, `_parse_answer_key`, `_split_practice_block`, `_render_practice`, `_pair_practice_answers`.
  - Wire `_pair_practice_answers` into `md_to_body` (one line).
  - Append a new CSS block (`.prow/.prob/.pnum/.qcheck/.qa/.practice-sub/.vh` + print + reduced-motion) to the `CSS` string.
- **Modify** `_verification/tests/test_textbook.py` — new tests (unit + integration + determinism + tutor-guide-safety).
- **Regenerate** `docs/textbook/*`, and (CSS shared) `docs/student-guide/textbook.css`, `docs/tutor-guide/textbook.css` — committed output.

All logic lives in one module; helpers are small and independently testable.

---

## Task 1: `_md_inline` — render a markdown fragment to inline HTML

**Files:**
- Modify: `_verification/build_textbook.py` (add helper near `md_to_body`)
- Test: `_verification/tests/test_textbook.py`

- [ ] **Step 1: Write the failing test**

```python
def test_md_inline_strips_paragraph_and_keeps_formatting():
    assert bt._md_inline("x+5=12") == "x+5=12"
    assert bt._md_inline("**prime**") == "<strong>prime</strong>"
    # raw inline HTML (a refcode badge) passes through untouched
    assert bt._md_inline('<a class="refcode">2.1.1</a> x=1') == '<a class="refcode">2.1.1</a> x=1'
    # no md_in_html residue ever leaks
    assert 'markdown="1"' not in bt._md_inline("**a**")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest _verification/tests/test_textbook.py::test_md_inline_strips_paragraph_and_keeps_formatting -v`
Expected: FAIL (`AttributeError: module 'build_textbook' has no attribute '_md_inline'`).

- [ ] **Step 3: Write minimal implementation**

Add near the top-level helpers (e.g. just above `md_to_body`):

```python
def _md_inline(s):
    """Render a short markdown fragment (a practice problem or an answer) to inline HTML.
    Core markdown only (no toc/md_in_html) for deterministic, dependency-light output; strip the
    single wrapping <p>. Inline raw HTML (refcode badges) and math sentinels pass through."""
    h = mdlib.markdown(s.strip(), output_format="html5").strip()
    if h.startswith("<p>") and h.endswith("</p>"):
        h = h[3:-4]
    return h.replace(' markdown="1"', '')
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest _verification/tests/test_textbook.py::test_md_inline_strips_paragraph_and_keeps_formatting -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add _verification/build_textbook.py _verification/tests/test_textbook.py
git commit -m "feat(textbook): _md_inline fragment renderer"
```

---

## Task 2: `_parse_answer_key` — sequential answer-key parser

The key robustness idea: answers are numbered **sequentially**, so after entry `n` we look only for the *specific* marker `n+1`. This ignores stray `\d)`/`\d.` inside answer text (e.g. `… exponent +1)`).

**Files:**
- Modify: `_verification/build_textbook.py`
- Test: `_verification/tests/test_textbook.py`

- [ ] **Step 1: Write the failing test**

```python
def test_parse_answer_key_basic_and_robust():
    assert bt._parse_answer_key("1) 7  2) 5  3) 0") == {1: "7", 2: "5", 3: "0"}
    # prose / bold / parenthetical-with-stray-paren answers
    m = bt._parse_answer_key("11) 2×10¹² (from 20×10¹¹ — slide left, exponent +1)  12) 5.6×10⁶")
    assert m[11] == "2×10¹² (from 20×10¹¹ — slide left, exponent +1)"
    assert m[12] == "5.6×10⁶"
    # multi-line block, prose answer
    m2 = bt._parse_answer_key("1) 4  2) 5\n13) x=4  14) identity — all real numbers")
    assert m2[2] == "5" and m2[13] == "x=4" and m2[14] == "identity — all real numbers"
    # '.' delimiter and a leading italic note are both handled
    assert bt._parse_answer_key("*(note)* 13. -4 14. 4") == {13: "-4", 14: "4"}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest _verification/tests/test_textbook.py::test_parse_answer_key_basic_and_robust -v`
Expected: FAIL (no attribute `_parse_answer_key`).

- [ ] **Step 3: Write minimal implementation**

```python
def _parse_answer_key(block_text):
    """Parse an answer-key block body into {int: answer_markdown}. Sequential expectation makes it
    robust to stray '\\d)'/'\\d.' inside answers. Accepts ')' or '.' delimiters; strips a leading
    italic '*(note)*'/'*note*' off the label remainder."""
    s = " ".join(ln.strip() for ln in block_text.splitlines()).strip()
    s = re.sub(r'^\*\([^)]*\)\*\s*', '', s)   # drop a leading *(parenthetical note)*
    s = re.sub(r'^\*[^*]+\*\s+(?=\d)', '', s) # or a leading *note* sitting before the first number
    first = re.search(r'(?<![\w.])(\d+)[).]\s', s)
    if not first:
        return {}
    out, n, cur = {}, int(first.group(1)), first.end()
    while True:
        nxt = re.compile(r'(?<![\w.])%d[).]\s' % (n + 1)).search(s, cur)
        if nxt:
            out[n] = s[cur:nxt.start()].strip().rstrip(",;").strip()
            n, cur = n + 1, nxt.end()
        else:
            out[n] = s[cur:].strip().rstrip(",;").strip()
            return out
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest _verification/tests/test_textbook.py::test_parse_answer_key_basic_and_robust -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add _verification/build_textbook.py _verification/tests/test_textbook.py
git commit -m "feat(textbook): robust sequential answer-key parser"
```

---

## Task 3: `_split_practice_block` — subheads + sequential problems

Splits a practice block body (already carrying refcode badges from `_convert_anchors`) into an ordered list of items: `("sub", text)` for italic group sub-heads and `("prob", number, html_or_md_text)` for problems. Uses the same sequential-number idea across packed lines and continuation lines.

**Files:**
- Modify: `_verification/build_textbook.py`
- Test: `_verification/tests/test_textbook.py`

- [ ] **Step 1: Write the failing test**

```python
def test_split_practice_block_packed_and_subheads():
    body = ("*Add (undo by subtracting):*\n"
            "1. x+5=12  2. x+9=14  3. x+7=7\n"
            "*Subtract (undo by adding):*\n"
            "6. x-4=10  7. x-6=1")
    items = bt._split_practice_block(body)
    assert items[0] == ("sub", "Add (undo by subtracting):")
    assert items[1] == ("prob", 1, "x+5=12")
    assert items[3] == ("prob", 3, "x+7=7")
    assert items[4] == ("sub", "Subtract (undo by adding):")
    assert items[5] == ("prob", 6, "x-4=10")

def test_split_practice_block_carries_badge_and_multiline():
    body = ('1. <a class="refcode" id="2.1.1">2.1.1</a> Two trains leave at\nthe same time. How far?\n2. Short one')
    items = bt._split_practice_block(body)
    assert items[0][0] == "prob" and items[0][1] == 1
    assert '<a class="refcode" id="2.1.1">2.1.1</a>' in items[0][2]
    assert "Two trains leave at the same time. How far?" in items[0][2]
    assert items[1] == ("prob", 2, "Short one")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest _verification/tests/test_textbook.py -k split_practice_block -v`
Expected: FAIL (no attribute `_split_practice_block`).

- [ ] **Step 3: Write minimal implementation**

```python
_PSUB_RE = re.compile(r'^\*[^*].*?\*$')   # a whole-line *italic sub-head* (single asterisks)


def _split_practice_block(body):
    """-> ordered list of ('sub', text) and ('prob', int, text). Problems may be packed several per
    line and/or span continuation lines; sub-heads sit on their own italic lines. Sequential problem
    numbering (find n, then look only for n+1) avoids splitting on stray 'N.' inside problem text."""
    # group consecutive non-sub lines into content segments, preserving sub-head order
    segments, buf = [], []
    for raw in body.splitlines():
        st = raw.strip()
        if not st:
            continue
        if _PSUB_RE.match(st) and not st.startswith("**"):
            if buf:
                segments.append(("content", " ".join(buf))); buf = []
            segments.append(("sub", st.strip("*").strip()))
        else:
            buf.append(st)
    if buf:
        segments.append(("content", " ".join(buf)))

    items = []
    for kind, text in segments:
        if kind == "sub":
            items.append(("sub", text)); continue
        first = re.search(r'(?<![\w.])(\d+)\.\s', text)
        if not first:
            continue
        n, cur = int(first.group(1)), first.end()
        while True:
            nxt = re.compile(r'(?<![\w.])%d\.\s' % (n + 1)).search(text, cur)
            if nxt:
                items.append(("prob", n, text[cur:nxt.start()].strip()))
                n, cur = n + 1, nxt.end()
            else:
                items.append(("prob", n, text[cur:].strip()))
                break
    return items
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest _verification/tests/test_textbook.py -k split_practice_block -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add _verification/build_textbook.py _verification/tests/test_textbook.py
git commit -m "feat(textbook): practice-block splitter (subheads + packed/multiline problems)"
```

---

## Task 4: `_pair_practice_answers` + `_render_practice`, wired into `md_to_body`

Lesson-aware orchestrator: build the merged answer map (dropping conflicting duplicate numbers), find practice/answers blocks (reusing `_blockify`'s label/stop rules), convert pairable sets, drop consumed answer keys, leave the rest for `_blockify`.

**Files:**
- Modify: `_verification/build_textbook.py`
- Test: `_verification/tests/test_textbook.py`

- [ ] **Step 1: Write the failing test**

```python
LESSON_OK = (
    "## Lesson 9.9: Demo\n\n"
    "**Practice problems:**\n\n"
    "*Group one:*\n"
    "1. x+5=12  2. x+9=14  3. x+7=7\n\n"
    "**Answer key:**\n"
    "1) 7  2) 5  3) 0\n\n"
    "---\n")

def test_pair_converts_and_drops_key():
    html = bt.md_to_body(LESSON_OK)
    assert html.count('class="prow"') == 3            # one row per problem
    assert html.count('class="qcheck"') == 3          # one reveal per problem
    assert 'class="practice-sub"' in html             # sub-head preserved
    assert '>7<' in html and 'Reveal answer' in html  # answer paired in
    assert 'class="answers"' not in html              # single box removed
    assert 'to problem 1' in html                     # accessible per-problem name

def test_pair_falls_back_when_answer_missing():
    bad = LESSON_OK.replace("1) 7  2) 5  3) 0", "1) 7  2) 5")   # no answer for #3
    html = bt.md_to_body(bad)
    assert 'class="qcheck"' not in html               # no per-problem reveal
    assert 'class="answers"' in html                  # keeps the single box
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest _verification/tests/test_textbook.py -k pair_ -v`
Expected: FAIL (currently emits `class="answers"`, no `prow`).

- [ ] **Step 3: Write minimal implementation**

Add the helpers (after `_split_practice_block`):

```python
def _render_practice(items):
    """Render converted practice items (with paired answers) to raw HTML. Inner problem/answer
    markdown is rendered up front via _md_inline (no md_in_html nesting)."""
    out = ['<section class="practice">',
           f'<span class="eyebrow">{_ICONS.get("practice", "")}Practice</span>']
    for it in items:
        if it[0] == "sub":
            out.append(f'<p class="practice-sub">{_md_inline(it[1])}</p>')
        else:
            _, num, ptext, ans = it
            out.append(
                f'<div class="prow">'
                f'<span class="prob"><span class="pnum">{num}.</span> {_md_inline(ptext)}</span>'
                f'<details class="qcheck"><summary>'
                f'<span class="qc-label">Reveal answer</span>'
                f'<span class="vh"> to problem {num}</span></summary>'
                f'<span class="qa">{_md_inline(ans)}</span></details></div>')
    out.append("</section>")
    return "\n".join(out)


def _scan_labeled_blocks(lines):
    """Yield (kind, start, end, inner_text) for every labelled block, using _blockify's rules."""
    i, n, infence = 0, len(lines), False
    while i < n:
        ln = lines[i]
        if ln.lstrip().startswith("```"):
            infence = not infence; i += 1; continue
        if infence:
            i += 1; continue
        lab = _match_label(ln)
        if not lab:
            i += 1; continue
        kind, _eyebrow, remainder = lab
        body, j, f2 = ([remainder] if remainder.strip() else []), i + 1, False
        while j < n:
            l2 = lines[j]
            if l2.lstrip().startswith("```"):
                f2 = not f2; body.append(l2); j += 1; continue
            if not f2 and (_match_label(l2) or _STOP_RE.match(l2)):
                break
            body.append(l2); j += 1
        yield kind, i, j, "\n".join(body).strip("\n")
        i = j


def _pair_practice_answers(text):
    """Convert each pairable Practice+Answer-key set in a lesson chunk to per-problem reveals;
    delete the consumed answer keys. Irregular sets are left for _blockify."""
    lines = text.split("\n")
    blocks = list(_scan_labeled_blocks(lines))
    # merged answer map; drop numbers that conflict across keys
    amap, conflict = {}, set()
    for kind, _s, _e, inner in blocks:
        if kind == "answers":
            for k, v in _parse_answer_key(inner).items():
                if k in amap and amap[k] != v:
                    conflict.add(k)
                amap.setdefault(k, v)
    for k in conflict:
        amap.pop(k, None)

    edits, consumed = [], set()   # edits: (start, end, replacement_lines or None)
    for kind, s, e, inner in blocks:
        if kind != "practice":
            continue
        items = _split_practice_block(inner)
        nums = [it[1] for it in items if it[0] == "prob"]
        if len(nums) >= 2 and all(k in amap for k in nums):
            paired = [it if it[0] == "sub" else ("prob", it[1], it[2], amap[it[1]]) for it in items]
            edits.append((s, e, ["", _render_practice(paired), ""]))
            consumed.update(nums)
    for kind, s, e, inner in blocks:
        if kind == "answers":
            ks = set(_parse_answer_key(inner).keys())
            if ks and ks <= consumed:
                edits.append((s, e, None))     # drop fully-consumed key

    if not edits:
        return text
    edits.sort(key=lambda t: t[0])
    out, prev = [], 0
    for s, e, repl in edits:
        out.extend(lines[prev:s])
        if repl:
            out.extend(repl)
        prev = e
    out.extend(lines[prev:])
    return "\n".join(out)
```

Wire it into `md_to_body` immediately after `_convert_anchors`:

```python
def md_to_body(text, launcher=False):
    text, math = _protect_math(text)
    text = _id_worked_practice(text)
    text = _convert_anchors(text, launcher)
    text = _pair_practice_answers(text)      # NEW
    text = _space_subheads(text)
    text = _blockify(text)
    ...
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest _verification/tests/test_textbook.py -k pair_ -v`
Expected: PASS.

- [ ] **Step 5: Run the whole suite (guard against regressions)**

Run: `python -m pytest _verification/tests -q`
Expected: all pass. If a pre-existing test asserts the old single-box behavior on a *convertible* lesson, update that test to the new markup (note it in the commit).

- [ ] **Step 6: Commit**

```bash
git add _verification/build_textbook.py _verification/tests/test_textbook.py
git commit -m "feat(textbook): pair practice problems with per-question answer reveals + fallback"
```

---

## Task 5: CSS for the per-question reveal

Append to the `CSS` string (after the `/* ---- answer key reveal ---- */` section, near line 761). **Do not modify `.answers`.** Reuse existing custom properties; mirror the existing `.practice li` card look; green (`--leaf`) reveal pill.

**Files:**
- Modify: `_verification/build_textbook.py` (the `CSS` string)
- Test: `_verification/tests/test_textbook.py`

- [ ] **Step 1: Write the failing test**

```python
def test_qcheck_css_present_and_answers_untouched():
    css = bt.CSS
    assert ".prow{" in css and ".qcheck" in css and ".practice-sub" in css and ".vh{" in css
    # the shared .answers component (used by the tutor guide) keeps its reveal styling
    assert ".answers > summary{cursor:pointer" in css

def test_tutor_guide_answers_unchanged():
    import build_tutor_guide as tg
    files = tg.build_site(tg._ssot())
    unit = next(v for k, v in files.items() if k.startswith("unit-"))
    assert 'details class="answers"' in unit        # worked-solution boxes intact
    assert 'class="qcheck"' not in unit              # new component never leaks here
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest _verification/tests/test_textbook.py -k "qcheck_css or tutor_guide_answers" -v`
Expected: FAIL on the first assert (no `.prow{` in CSS yet).

- [ ] **Step 3: Write minimal implementation**

Insert this block into the `CSS` string (immediately after the existing `.answers .ak-body{…}` rule):

```css
/* ---- per-question answer reveal (textbook practice) ---- */
.vh{position:absolute!important; width:1px; height:1px; padding:0; margin:-1px; overflow:hidden;
  clip:rect(0 0 0 0); white-space:nowrap; border:0}
.practice-sub{font-weight:600; font-size:var(--step--1); color:var(--ink-soft); margin:1.3rem 0 .5rem}
.prow{display:flex; gap:.6rem .9rem; align-items:baseline; flex-wrap:wrap; background:var(--card);
  border:1px solid var(--rule); border-radius:var(--radius); padding:.7rem .9rem; margin:.6rem 0}
.prow .prob{flex:1 1 60%; min-width:0; overflow-wrap:break-word}
.prow .pnum{color:var(--ink-soft); margin-right:.3rem}
.prow .katex{white-space:normal} .prow .katex-display{overflow-x:auto; margin:.3rem 0}
.qcheck{margin-left:auto; flex:0 0 auto}
.qcheck > summary{cursor:pointer; list-style:none; display:inline-flex; align-items:center; gap:.4rem}
.qcheck > summary::-webkit-details-marker{display:none}
.qcheck .qc-label{font-size:var(--step--1); font-weight:600; color:var(--leaf);
  border:1px solid var(--leaf); border-radius:999px; padding:.28rem .7rem; background:var(--tint-leaf, transparent)}
.qcheck[open] .qc-label{color:var(--ink-soft); border-color:var(--rule)}
.qcheck .qa{display:inline-flex; align-items:center; gap:.4rem; margin-left:.55rem;
  font-weight:600; color:var(--leaf)}
.qcheck .qa::before{content:"\2713"; font-weight:700}
.qcheck:not([open]) .qa{display:none}
@media (prefers-reduced-motion:no-preference){ .prow{transition:border-color .15s ease} }
@media print{ .qcheck .qa{display:inline-flex} .qcheck > summary{display:none} }
```

(If `--tint-leaf` is not defined in the palette, the `transparent` fallback applies — verify in Step 4.)

- [ ] **Step 4: Run test + visually confirm a built page**

Run: `python -m pytest _verification/tests/test_textbook.py -k "qcheck_css or tutor_guide_answers" -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add _verification/build_textbook.py _verification/tests/test_textbook.py
git commit -m "style(textbook): per-question reveal CSS (.prow/.qcheck), .answers untouched"
```

---

## Task 6: Determinism, regenerate sites, coverage report

**Files:**
- Test: `_verification/tests/test_textbook.py`
- Regenerate: `docs/**`

- [ ] **Step 1: Determinism test**

```python
def test_pair_build_is_deterministic():
    out1 = bt.md_to_body(LESSON_OK)
    out2 = bt.md_to_body(LESSON_OK)
    assert out1 == out2
    assert 'markdown="1"' not in out1
```

Run: `python -m pytest _verification/tests/test_textbook.py::test_pair_build_is_deterministic -v`
Expected: PASS.

- [ ] **Step 2: Coverage probe (temporary script, not committed)**

Count convert vs fall-back across every lesson so we can see real coverage:

```bash
python - <<'PY'
import sys; sys.path.insert(0, "_verification")
import build_textbook as bt, generate
conv = fb = 0
for u in generate.load_ssot().units:
    intro, lessons = bt._split_unit(open(bt._md_path(u.id), encoding="utf-8").read())
    for lid, _t, chunk in lessons:
        if "**Practice problems" not in chunk:
            continue
        html = bt.md_to_body(chunk, launcher=True)
        if 'class="qcheck"' in html: conv += 1
        if 'class="answers"' in html: fb += 1
        tag = "CONVERT" if 'class="qcheck"' in html else "fallback"
        print(f"{lid:>6}  {tag}")
print(f"\nlessons converting: {conv}   lessons still using single box: {fb}")
PY
```

Expected: a per-lesson list plus totals. Record the totals in the final commit message. (No assertion — this is an observability probe.)

- [ ] **Step 3: Regenerate every site and verify nothing is stale**

```bash
python _verification/build_all.py
python _verification/build_textbook.py --check
python _verification/build_student_guide.py --check
python _verification/build_tutor_guide.py --check
```

Expected: builds succeed; every `--check` prints "current." (no stale/missing).

- [ ] **Step 4: Full suite**

Run: `python -m pytest _verification/tests -q`
Expected: all pass (≥ baseline 71 + new tests).

- [ ] **Step 5: Commit regenerated output**

```bash
git add docs _verification
git commit -m "build(textbook): regenerate sites with per-question answer reveals"
```

---

## Self-review checklist (done before handoff)

- **Spec coverage:** Option-A inline reveal (Task 4/5), per-question (Task 4), single box removed when converted (Task 4 test), graceful fallback (Task 4 test), native `<details>`/no-JS (Task 5), accessible per-problem name (Task 4 test), `.answers`/tutor-guide untouched (Task 5 test), determinism (Task 6), source/refcodes unchanged (transform runs after `_convert_anchors`, source not edited), coverage report (Task 6). All mapped.
- **Edge cases (spec table):** packed/subheads (Task 3), prose/bold/superscript/`(x,y)` (Task 2 + `_md_inline`), multi-line & multiple keys merged (Task 2/4), `N.` delimiter (Task 2), non-contiguous/missing → fallback (Task 4), tables/word-problems → fallback or convert per pairing (Task 4).
- **Type/name consistency:** helpers `_md_inline`, `_parse_answer_key`, `_split_practice_block`, `_scan_labeled_blocks`, `_pair_practice_answers`, `_render_practice`; classes `.prow/.prob/.pnum/.qcheck/.qc-label/.qa/.practice-sub/.vh` — used identically across tasks and tests.
- **Placeholders:** none.
