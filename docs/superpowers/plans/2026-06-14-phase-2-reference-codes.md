# Phase 2 — Reference-code system — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make every referenceable item in the shipped skill addressable by a collision-free, human-typable reference code (`12.5.w2`, `1.1.d3`, `mis.3`, `met.balance-scale`), enforced by a build linter, with a resolution recipe in `SKILL.md`.

**Architecture:** Additive inline `{#code}` anchors in the unit `.md` files (definitions `d`, transfer-checks `c`, how-tos `h`, reserved figures `f`) and the three global banks (`mis.N`, `vis.tN`, `met.<slug>`). One unified grammar regex in `check_alignment.py` drives two scanners — the existing JSON-id check and a new `md_anchor_lint()` (grammar + collision + dense document-order + SSOT-existence). Worked examples and practice problems stay addressable by their visible number (no anchor), keeping every anchor out of the blocks the point-on-line lint and `generate.py` parse.

**Tech Stack:** Python 3.11, `re`, `sympy`, `PyYAML`, `pytest`. Build tooling in `_verification/`; shipped content in `algebra-1-tutor/`.

**Spec:** `docs/superpowers/specs/2026-06-14-phase-2-reference-codes-design.md`.

---

## File structure

**Modify (PR1):**
- `_verification/check_alignment.py` — unified `ID_RE`; new `_scan_anchors()`, `_group_key_and_index()`, `_lint_anchor_list()`, `md_anchor_lint()`; wire into `main()`.
- `_verification/tests/test_code_grammar.py` — new grammar + anchor-lint tests; existing tests stay.
- `algebra-1-tutor/references/misconceptions.md` — `{#mis.1}`…`{#mis.8}` on the 8 section headings.
- `algebra-1-tutor/references/visuals.md` — `{#vis.t1}`…`{#vis.t4}` on the 4 Template headings.
- `algebra-1-tutor/references/metaphors.md` — 18 `{#met.<slug>}` leading the lettered entries.
- `algebra-1-tutor/SKILL.md` — new "Reference codes" section (copyedited).
- `_verification/AUTHOR_GUIDE.md` — "Reference-code anchors" convention subsection.

**Modify (PR2):**
- `algebra-1-tutor/references/units/unit-01..12*.md` + `appendix-statistics.md` — `d`/`c`/`h`/`f` anchors.

**Untouched:** `curriculum.yaml`, `generate.py`, all `*.json` answer keys, `verify_answers.py`, `check_notation.py`, `pedagogy.md`, `curriculum-map.md`.

---

# PR1 — Foundation: grammar, linter, banks, docs · branch `phase-2/foundation`

## Task 1: Commit the spec + this plan

- [ ] **Step 1: Stage and commit the planning docs**

```bash
git add docs/superpowers/specs/2026-06-14-phase-2-reference-codes-design.md \
        docs/superpowers/plans/2026-06-14-phase-2-reference-codes.md
git commit -m "Phase 2: spec + implementation plan (reference-code system)"
```

## Task 2: Extend `ID_RE` to the full grammar (TDD)

**Files:**
- Modify: `_verification/check_alignment.py:24` (the `ID_RE` definition)
- Test: `_verification/tests/test_code_grammar.py`

- [ ] **Step 1: Write the failing tests** — append to `test_code_grammar.py`:

```python
def test_accepts_new_shapes():
    for good in ["1.1.d1", "1.1.c1", "2.2.h1", "1.2.f1",
                 "mis.3", "vis.t1", "met.balance-scale", "met.two-round-flyers",
                 "5.5.6", "12.1.w1", "A.2.3", "refA.4", "8.2.5b", "6.2.ex1"]:
        assert ca.ID_RE.match(good), good

def test_rejects_malformed_new():
    for bad in ["1.1.d", "mis.", "vis.3", "vis.tx", "met.Bad_Slug", "met.",
                "met.-x", "met.x-", "5.5.", "13.1.1", "x.y.z", "5..6", "ref.4", "5.5.w"]:
        assert not ca.ID_RE.match(bad), bad
```

- [ ] **Step 2: Run to verify they fail**

Run: `python -m pytest _verification/tests/test_code_grammar.py -q`
Expected: FAIL (`1.1.d1` etc. not yet accepted by the restricted regex).

- [ ] **Step 3: Replace `ID_RE`** (`check_alignment.py`, the block at line ~19-24):

```python
# Unified backward-compatible id grammar (RESEARCH_REDTEAM_HANDOFF.md §5). One regex, two
# scanners: code_grammar_lint() checks JSON ids (a subset); md_anchor_lint() checks .md {#code}
# anchors. Collision-free by construction (numeric vs letter scope; letter-then-digit tag vs
# digit-only practice).
#   lesson item : (1-12|A).lesson.[w|ex|d|c|h|f]index[part]   e.g. 5.5.6, 12.1.w1, 1.1.d3, 1.2.f1
#   refresher   : ref[AB].index                               e.g. refA.4
#   globals     : mis.N | vis.tN | met.<kebab-slug>           e.g. mis.3, vis.t1, met.balance-scale
ID_RE = re.compile(
    r"^(?:"
    r"(?:[1-9]|1[0-2]|A)\.\d+\.(?:w|ex|d|c|h|f)?\d+[a-z]?"
    r"|ref[AB]\.\d+"
    r"|mis\.\d+"
    r"|vis\.t\d+"
    r"|met\.[a-z0-9]+(?:-[a-z0-9]+)*"
    r")\Z"
)
```

- [ ] **Step 4: Run to verify all grammar tests pass**

Run: `python -m pytest _verification/tests/test_code_grammar.py -q`
Expected: PASS (incl. existing `test_accepts_known_shapes`, `test_rejects_malformed`, `test_all_real_ids_pass`).

- [ ] **Step 5: Commit**

```bash
git add _verification/check_alignment.py _verification/tests/test_code_grammar.py
git commit -m "Phase 2: unified reference-code grammar (ID_RE accepts d/c/h/f + mis/vis/met)"
```

## Task 3: Implement `md_anchor_lint()` (TDD)

**Files:**
- Modify: `_verification/check_alignment.py` (add functions after `code_grammar_lint`; call in `main`)
- Test: `_verification/tests/test_code_grammar.py`

- [ ] **Step 1: Write the failing logic tests** — append to `test_code_grammar.py`:

```python
SSOT = {"1.1", "1.2", "2.2"}  # minimal lesson set for pure-logic tests

def test_anchor_clean():
    anchors = [("1.1.d1", "u.md"), ("1.1.d2", "u.md"), ("1.1.c1", "u.md"),
               ("mis.1", "m.md"), ("vis.t1", "v.md"), ("met.balance-scale", "x.md")]
    assert ca._lint_anchor_list(anchors, SSOT) == []

def test_anchor_grammar_failure():
    issues = ca._lint_anchor_list([("1.1.zz", "u.md")], SSOT)
    assert any("grammar" in i for i in issues)

def test_anchor_collision():
    issues = ca._lint_anchor_list([("1.1.d1", "a.md"), ("1.1.d1", "b.md")], SSOT)
    assert any("duplicate" in i.lower() for i in issues)

def test_anchor_density_gap():
    issues = ca._lint_anchor_list([("1.1.d1", "u.md"), ("1.1.d3", "u.md")], SSOT)
    assert any("dense" in i for i in issues)

def test_anchor_unknown_lesson():
    issues = ca._lint_anchor_list([("9.9.d1", "u.md")], SSOT)
    assert any("unknown lesson" in i for i in issues)

def test_md_anchor_lint_real_tree_clean():
    assert ca.md_anchor_lint() == []          # holds once banks (PR1) / units (PR2) are tagged
```

- [ ] **Step 2: Run to verify they fail**

Run: `python -m pytest _verification/tests/test_code_grammar.py -q`
Expected: FAIL (`_lint_anchor_list` / `md_anchor_lint` not defined).

- [ ] **Step 3: Implement** — add to `check_alignment.py` after `code_grammar_lint()`:

```python
ANCHOR_RE = re.compile(r"\{#([^}\s]+)\}")
_LESSON_SCOPE_RE = re.compile(r"^((?:[1-9]|1[0-2]|A)\.\d+)\.")

def _shipped_md_for_anchors():
    """All shipped .md under algebra-1-tutor/ except SKILL.md (which documents the convention
    by example and must not be linted as if its examples were real anchors)."""
    root = os.path.join(REPO_ROOT, "algebra-1-tutor")
    files = sorted(glob.glob(os.path.join(root, "**", "*.md"), recursive=True))
    return [f for f in files if os.path.basename(f) != "SKILL.md"], root

def _scan_anchors():
    """Return [(code, relpath), ...] for every {#code}, document order. Strips $$ blocks and
    fenced code first (anchors never live inside math/code)."""
    files, root = _shipped_md_for_anchors()
    out = []
    for fp in files:
        s = open(fp, encoding="utf-8").read()
        s = re.sub(r"\$\$.*?\$\$", " ", s, flags=re.DOTALL)
        s = re.sub(r"```.*?```", " ", s, flags=re.DOTALL)
        rel = os.path.relpath(fp, root)
        out += [(m.group(1), rel) for m in ANCHOR_RE.finditer(s)]
    return out

def _group_key_and_index(code):
    """For the density check: (group_key, index_int) for index-grouped codes, else None.
    met.<slug> has no index -> None (uniqueness is covered by the collision check)."""
    m = re.match(r"^((?:[1-9]|1[0-2]|A)\.\d+)\.(w|ex|d|c|h|f)?(\d+)[a-z]?$", code)
    if m:
        return (f"{m.group(1)}.{m.group(2) or ''}", int(m.group(3)))
    m = re.match(r"^mis\.(\d+)$", code)
    if m:
        return ("mis", int(m.group(1)))
    m = re.match(r"^vis\.t(\d+)$", code)
    if m:
        return ("vis.t", int(m.group(1)))
    return None

def _lint_anchor_list(anchors, ssot_ids):
    """Pure linter over [(code, relpath), ...]: grammar + collision + density + SSOT existence."""
    issues, seen, groups = [], {}, {}
    for code, rel in anchors:
        if not ID_RE.match(code):
            issues.append(f"{rel}: anchor {{#{code}}} violates grammar")
            continue
        if code in seen:
            issues.append(f"{rel}: anchor {{#{code}}} duplicates {seen[code]} (collision)")
        else:
            seen[code] = rel
        m = _LESSON_SCOPE_RE.match(code)
        if m and m.group(1) not in ssot_ids:
            issues.append(f"{rel}: anchor {{#{code}}} -> unknown lesson {m.group(1)}")
        gk = _group_key_and_index(code)
        if gk:
            groups.setdefault(gk[0], []).append(gk[1])
    for key, idxs in sorted(groups.items()):
        dist = sorted(set(idxs))
        if dist != list(range(1, len(dist) + 1)):
            issues.append(f"group {key}: indices {sorted(idxs)} not dense 1..N "
                          f"(gap/append-only violation)")
    return issues

def md_anchor_lint():
    """Lint every {#code} anchor across the shipped .md files."""
    sys.path.insert(0, HERE)
    import generate
    ssot_ids = {l.id for u in generate.load_ssot().units for l in u.lessons}
    return _lint_anchor_list(_scan_anchors(), ssot_ids)
```

- [ ] **Step 4: Wire into `main()`** — in `check_alignment.py` `main()`, after the `g = code_grammar_lint()` block, add:

```python
    md = md_anchor_lint()
    if md:
        failures += [f"md-anchor: {i}" for i in md]
```

And update the success print line to mention it:

```python
    print("check_alignment: alignment + notation + point-on-line + code-grammar + md-anchor all green.")
```

- [ ] **Step 5: Run the anchor tests + the umbrella**

Run: `python -m pytest _verification/tests/test_code_grammar.py -q && python _verification/check_alignment.py`
Expected: logic tests PASS; `test_md_anchor_lint_real_tree_clean` PASS (no anchors yet → `[]`); umbrella prints the new green line.

- [ ] **Step 6: Commit**

```bash
git add _verification/check_alignment.py _verification/tests/test_code_grammar.py
git commit -m "Phase 2: md_anchor_lint (grammar + collision + density + SSOT) wired into check_alignment"
```

## Task 4: Tag `misconceptions.md` (`mis.1`–`mis.8`)

**Files:** Modify `algebra-1-tutor/references/misconceptions.md`

- [ ] **Step 1: Append `{#mis.N}` to each of the 8 `## N. Title` headings**, in document order:
  - `## 1. The equals sign: …` → `## 1. The equals sign: … {#mis.1}`
  - `## 2. Variables: … {#mis.2}` · `## 3. Negative numbers … {#mis.3}` · `## 4. Fractions: … {#mis.4}`
  - `## 5. Order of operations … {#mis.5}` · `## 6. Inequalities: … {#mis.6}`
  - `## 7. Algebraic structure … {#mis.7}` · `## 8. Slope: … {#mis.8}`
  - Do **not** anchor the intro or "How to use this in the flow" sections.

- [ ] **Step 2: Verify anchors + notation**

Run: `python _verification/check_notation.py && python -c "import sys; sys.path.insert(0,'_verification'); import check_alignment as ca; print([a for a in ca._scan_anchors() if a[0].startswith('mis')])"`
Expected: notation clean; prints `mis.1`…`mis.8` in order.

## Task 5: Tag `visuals.md` (`vis.t1`–`vis.t4`)

**Files:** Modify `algebra-1-tutor/references/visuals.md`

- [ ] **Step 1: Append `{#vis.tN}` to the four Template headings:**
  - `## Template 1 — Number line with a marked point (SVG artifact) {#vis.t1}`
  - `## Template 2 — Coordinate plane + a line y = mx + b (SVG artifact) {#vis.t2}`
  - `## Template 3 — Parabola y = ax² + bx + c (SVG artifact) {#vis.t3}`
  - `## Template 4 — Inequality region (2-D shading) {#vis.t4}`
  - Do **not** anchor the ASCII/balance-scale/area-model subsections (no `vis` code this phase).

- [ ] **Step 2: Verify** — `python _verification/check_notation.py` → clean.

## Task 6: Tag `metaphors.md` (18 `met.<slug>`)

**Files:** Modify `algebra-1-tutor/references/metaphors.md`

- [ ] **Step 1: Prepend `{#met.<slug>}` to each lettered entry's bold lead**, e.g.:
  `**A. The balance scale.** An equation…` → `{#met.balance-scale} **A. The balance scale.** An equation…`
  Use the slug table from spec §5 (balance-scale, getting-dressed, money-debt, number-line-walk, mystery-box, reserved-seat, vending-machine, recipe, stairs-ramp, speed-rate, flyers, garden-area, area-box, two-round-flyers, reverse-distribute, gcf-bags, squaring-loses-sign, parabola-two-roots).

- [ ] **Step 2: Verify all 18 slugs scanned + notation clean**

Run: `python _verification/check_notation.py && python -c "import sys; sys.path.insert(0,'_verification'); import check_alignment as ca; m=[a[0] for a in ca._scan_anchors() if a[0].startswith('met')]; print(len(m), m)"`
Expected: notation clean; `18` slugs printed.

- [ ] **Step 3: Run the full umbrella (banks now tagged) + commit Tasks 4–6**

```bash
python _verification/check_alignment.py
git add algebra-1-tutor/references/misconceptions.md algebra-1-tutor/references/visuals.md algebra-1-tutor/references/metaphors.md
git commit -m "Phase 2: tag global banks (mis.1-8, vis.t1-4, 18 met slugs)"
```
Expected: `check_alignment` green incl. md-anchor.

## Task 7: `SKILL.md` "Reference codes" section (+ `/copyedit`)

**Files:** Modify `algebra-1-tutor/SKILL.md` (insert a new `## Reference codes` section after "Navigating the course")

- [ ] **Step 1: Draft the section** (prose; will be copyedited). Cover, plainly:
  - **What a code is:** `scope.lesson.tag+index` — scope is a unit (`1`–`12`, `A`) or a bank (`mis`, `vis`, `met`); the tag letter says what kind of item (`w` worked example, `d` definition, `c` check, `h` how-to, `f` figure; no letter = a practice problem). Examples in a fenced block: `12.5.w2`, `1.1.d3`, `8.2.5b`, `mis.3`, `vis.t1`, `met.balance-scale`.
  - **Resolving one a student quotes** (`#12.5.w2`, case-insensitive; spoken "worked example 2 of lesson 12.5" works too): read the matching unit file or bank → find the item (by its `{#…}` anchor for definitions/checks/how-tos/figures/bank entries, or by its number for worked examples and practice) → re-verify any computation against the bundled JSON answer key and live before showing it → show it and echo the canonical code back so the student learns the shorthand.
  - One sentence: figures (`f…`) are placeholders until Phase 3; if asked for one, say it's not drawn yet and describe/compute it per `visuals.md`.
  - Keep examples in fenced code blocks (so they render literally and are not mistaken for live anchors).

- [ ] **Step 2: Run `/copyedit` on the new section** (instructional-tutor voice target); apply edits.

- [ ] **Step 3: Verify the umbrella still green** (SKILL.md is excluded from notation + md-anchor by design):

Run: `python _verification/check_alignment.py`
Expected: green.

- [ ] **Step 4: Commit**

```bash
git add algebra-1-tutor/SKILL.md
git commit -m "Phase 2: SKILL.md Reference codes section + resolution recipe (copyedited)"
```

## Task 8: `AUTHOR_GUIDE.md` convention note

**Files:** Modify `_verification/AUTHOR_GUIDE.md`

- [ ] **Step 1: Add a "Reference-code anchors" subsection** under Conventions: the `{#code}` syntax; placement (trailing on headings, leading on list items/bold-led paragraphs; never on H1/`## Lesson` headers); tag letters; document-order assignment + append-only (never renumber); and that worked examples (`wK`) and practice (`K`) need no anchor (addressed by their visible number).

- [ ] **Step 2: Commit**

```bash
git add _verification/AUTHOR_GUIDE.md
git commit -m "Phase 2: AUTHOR_GUIDE reference-code anchor convention"
```

## Task 9: Full gate, review, PR1

- [ ] **Step 1: Run the full baseline gate**

```bash
python _verification/verify_answers.py && python _verification/check_alignment.py && \
python _verification/generate.py --check && python -m pytest _verification/tests -q
```
Expected: 909/614/0 · green · green · all pass.

- [ ] **Step 2: Clean tree check** — `git status` + `git ls-files --others --exclude-standard`; remove any stray scratch files; the two root HTML files stay untracked.

- [ ] **Step 3: `/code-review`** the linter change; address findings.

- [ ] **Step 4: Push + open PR1**

```bash
git push -u origin phase-2/foundation
gh pr create --title "Phase 2 PR1: reference-code grammar, linter, banks, docs" \
  --body "Implements Phase 2 foundation per docs/superpowers/specs/2026-06-14-phase-2-reference-codes-design.md: unified ID_RE + md_anchor_lint (TDD); tags the 3 global banks (mis/vis/met); SKILL.md Reference codes section; AUTHOR_GUIDE convention. Gate green (909/614/0, pytest green)."
```

- [ ] **Step 5: Merge + sync main**

```bash
gh pr merge --merge --delete-branch
git checkout main && git pull --ff-only
```

---

# PR2 — Unit-file tagging · branch `phase-2/unit-tagging`

## Task 10: Tag the 13 unit files (`d`/`c`/`h`/`f`), parallelized

**Files:** Modify each `algebra-1-tutor/references/units/unit-01..12*.md` + `appendix-statistics.md`

- [ ] **Step 1: Branch off the freshly-merged main**

```bash
git checkout main && git pull --ff-only && git checkout -b phase-2/unit-tagging
```

- [ ] **Step 2: Run the per-unit tagging workflow** (ultracode). One subagent per unit; each:
  - Reads ONLY its unit file. Adds, **in document order**:
    - `{#N.M.d1}`, `{#N.M.d2}`, … leading every bullet in each lesson's **New terms** block.
    - `{#N.M.c1}`, `{#N.M.c2}`, … leading every prompt in each **Check for understanding (transfer)** block.
    - `{#N.M.h1}`, … only where a lesson states an explicit, imperative, reusable **multi-step method** ("To <do X>: 1)… 2)…"); anchor that method's lead line. Most lessons have none.
    - `{#N.M.f1}`, … only where **Visuals to offer** names a *real* figure (not "none needed"); anchor the lead line and append `[figure reserved — Phase 3]`. Draw nothing.
  - Never anchors: the `# Unit`/`## Lesson` headers, worked examples, practice problems, answer keys, "Watch for", "Teaching arc" prose (unless it is the explicit method for an `h`).
  - Self-verifies with inline `python -c` (no scratch files): every anchor matches the grammar and each `(lesson, tag)` is dense 1..N in document order; notation stays clean.
  - Returns: unit id, per-lesson counts `{d, c, h, f}`.

- [ ] **Step 3: Main-loop gate after the fan-out**

```bash
python _verification/check_notation.py && python _verification/check_alignment.py && \
python _verification/generate.py --check && python -m pytest _verification/tests -q && \
python _verification/verify_answers.py
```
Expected: clean · green (md-anchor now covers all units) · green · pass · 909/614/0.

- [ ] **Step 4: Clean tree** — `git ls-files --others --exclude-standard`; remove any mangled `C:Users…` scratch files a subagent may have dropped.

## Task 11: Adversarial review, PR2

- [ ] **Step 1: Adversarial review pass** (one review subagent per unit, or a workflow): re-derive the expected `{d,c,h,f}` codes for each unit from the source, and confirm against the anchors actually present — checking grammar, collisions, dense document order, `h`/`f` judgment (no over-tagging), notation, and that no worked-example/practice/header was anchored. Fix any finding in the main loop.

- [ ] **Step 2: Commit + PR2**

```bash
git add algebra-1-tutor/references/units/*.md
git commit -m "Phase 2: tag all 13 unit files with d/c/h/f reference-code anchors"
git push -u origin phase-2/unit-tagging
gh pr create --title "Phase 2 PR2: unit-file reference-code tagging" \
  --body "Tags all 13 unit .md files with d/c/h/f anchors under the Phase-2 grammar. md_anchor_lint green across the corpus. Gate green (909/614/0)."
```

- [ ] **Step 3: Merge + sync main**

```bash
gh pr merge --merge --delete-branch
git checkout main && git pull --ff-only
```

## Task 12: Update project memory

- [ ] **Step 1:** Update memory `algebra-1-tutor-skill`: Phase 2 complete (PRs merged), baseline 909/614/0, the `{#code}` grammar + `md_anchor_lint` shipped, next = Phase 3 (figure library). Note the anchor-placement/parsing-safety learning and that worked-ex/practice are addressed by number.

---

## Self-review

**Spec coverage:** grammar (§3 → Task 2); `md_anchor_lint` collision/density/SSOT (§6 → Task 3); banks (§5 → Tasks 4–6); SKILL.md recipe + copyedit (§7 → Task 7); AUTHOR_GUIDE (§7 → Task 8); unit tagging d/c/h/f (§4 → Task 10); PR plan (§8 → PR1/PR2); verification (§10 → Tasks 9, 11); memory (§10 phase-end → Task 12). No gaps.

**Placeholders:** none — linter code is complete; tagging specs enumerate exact anchors; prose tasks specify content + the copyedit gate.

**Type consistency:** `_lint_anchor_list(anchors, ssot_ids)`, `_scan_anchors()`, `_group_key_and_index()`, `md_anchor_lint()`, `ANCHOR_RE`, `_LESSON_SCOPE_RE` are named identically across Task 3 and its tests; `ID_RE` group shapes in Task 2 match `_group_key_and_index` in Task 3.
