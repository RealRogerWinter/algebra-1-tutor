# Phase 1 — Content Elevation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Apply the confirmed red-team findings to the Algebra 1 course (majors first), promote Statistics to a core unit and rescope absolute-value 8.3, and weave in the SOTA-pedagogy moves — all behind the green Phase 0 alignment + sympy gate.

**Architecture:** Six theme-batched PRs off `main`, merged in order. Per-unit content is drafted by an ultracode workflow (one subagent per distinct unit file, parallel-safe), every new answer sympy-verified before it is written and recorded in the unit JSON. SSOT/structural edits (`curriculum.yaml`, `generate.py`, regeneration) are done in the main loop, not by parallel agents. Each PR is gate-green + copyedited + reviewed before merge.

**Tech Stack:** Python 3.11, sympy, PyYAML, pytest; markdown unit files; `gh` for PRs. Verification: `_verification/verify_answers.py`, `check_alignment.py`, `generate.py`, `pytest _verification/tests`.

**Spec:** `docs/superpowers/specs/2026-06-14-phase-1-content-elevation-design.md`.

---

## Conventions (every task obeys)

- **Verify-before-write (content TDD):** compute every numeric/algebraic answer with sympy *first*; write the identical answer into both the `.md` answer key **and** `unit-NN.json`/`appendix.json`. `.md` ↔ JSON answer parity is mandatory (the gate checks JSON-vs-sympy and, for line equations, `.md`-vs-JSON; non-line `.md` parity is enforced by review).
- **Append-only IDs:** new items get new trailing IDs within their lesson; never renumber/reuse. Demoted material keeps its ID.
- **Notation invariant:** shipped `.md` inline math is plain Unicode (x², √2, ½, ±, ≤, →); display only in `$$…$$`; never `\(...\)`/`$...$`. `docs/**` is build-only and exempt.
- **Line-equation `solve` entries** carry `on_line` (+ `slope` for one-point) per `AUTHOR_GUIDE.md`.
- **Algebra-1 ceiling held:** no logs, complex/imaginary numbers, rational/radical functions, asymptotes, polynomial division, degree>2 strand, conics beyond the parabola, matrices, series, trig, composition/inverses.
- **The gate is the safety net.** A wrong JSON answer cannot reach `main` (`verify_answers.py`); misalignment cannot (`check_alignment.py`); notation cannot regress (`check_notation.py`).

## The per-content-PR recipe (referenced by Tasks 2–7)

1. `git checkout main` → `git checkout -b phase-1/<branch>`.
2. Read each target unit `.md`, its `research-output/01` slice, and its JSON.
3. **Workflow** (`Draft` → `Verify`): one drafting subagent per distinct unit file applies its findings and sympy-verifies its answers; a verify subagent independently re-checks answers + `.md`↔JSON parity + notation + scope ceiling + append-only IDs. Structural edits stay in the main loop.
4. Run the gate (below); fix until green.
5. `/copyedit` the new shipped prose (instructional-tutor target); apply.
6. Review component (requesting-code-review skill / review agent); address.
7. Commit → `git push -u origin <branch>` → `gh pr create` → merge when green → delete branch.

**The gate (must all pass before PR):**
```
python _verification/verify_answers.py        # Failures: 0  (totals grow)
python _verification/check_alignment.py        # green
python _verification/generate.py --check       # green  (run generate.py first on structural PRs)
python -m pytest _verification/tests -q         # green
```

---

## Task 0: Land the planning docs on `main`

**Files:** none changed (merge only).

- [ ] **Step 1:** Confirm spec + this plan are committed on `phase-1/planning`.
- [ ] **Step 2:** Merge to main:
```bash
git checkout main && git merge --ff-only phase-1/planning
```
- [ ] **Step 3:** Verify gate still green on main (docs-only change, must be):
```bash
python _verification/verify_answers.py && python _verification/check_alignment.py && python _verification/generate.py --check && python -m pytest _verification/tests -q
```
- [ ] **Step 4:** Confirm the GitHub remote for PRs:
```bash
git remote -v        # expect RealRogerWinter/algebra-1-tutor (PR #1 merged from it)
```
If no remote, fall back to local review branches (merge locally, no `gh pr`).

---

## Task 1: PR1 — Number-line & distance (U1 + 8.3) · `phase-1/u1-u8-number-line-distance`

**Files:**
- Modify: `algebra-1-tutor/references/units/unit-01-foundations.md` (1.2 irrational/real; 1.4 |a|)
- Modify: `algebra-1-tutor/references/units/unit-08-inequalities.md` (8.3 rescope + Reach note)
- Modify: `_verification/unit-01.json`, `_verification/unit-08.json` (append verified items)
- Modify: `curriculum.yaml` (lesson 8.3 retitle) + regenerate `curriculum-map.md`, `docs/CURRICULUM.md`
- Create: `.gitattributes` (eol=lf on the two generated files)

- [ ] **Step 1:** Branch off main; create `.gitattributes`:
```
curriculum-map.md text eol=lf
algebra-1-tutor/references/curriculum-map.md text eol=lf
docs/CURRICULUM.md text eol=lf
```
Then `git add --renormalize .` so `curriculum-map.md` stops showing dirty.
- [ ] **Step 2 (U1.2 — irrational/real):** Add a "New term: irrational number (non-repeating, non-terminating — π, √2); real number = every point on the line" block after the rational-numbers discussion (unit-01 ~line 103). Add 1–2 worked examples (classify √2, π, and a perfect-square root like √9=3 → rational) and ~3 classify practice items (trailing IDs after the current 1.2 set). JSON: `manual` entries (classification).
- [ ] **Step 3 (U1.4 — absolute value):** Add "New term: absolute value |a| = distance from 0 (always ≥ 0)" beside "opposite/additive inverse" (unit-01 ~line 209). Worked examples (|−5|=5, |5|=5, |0|=0); ~4 practice (trailing IDs). JSON: `eval`-checkable where pure-number (e.g. `{"id":"1.4.17","kind":"eval","expr":"Abs(-5)","answer":"5"}`) — confirm sympy `Abs` parses in `verify_answers.py`; else `manual`.
- [ ] **Step 4 (8.3 rescope):** Reframe lesson 8.3 to (a) the V-shape graph of y=|x| + simple transformations (describe; reference `visuals.md`, no figure authored — Phase 3), (b) |x|=k → x=±k, |x|<k → −k<x<k, |x|>k → x<−k or x>k as *distance*. Move the general algebraic `|ax+b|=c`/`|ax+b|<c` + interval-notation material into a clearly-labeled **"Reach beyond Algebra 1"** note at the lesson end (one worked example, flagged off the mastery path); demoted problems keep their existing IDs under that note. New distance/graph problems get trailing IDs. JSON: solve entries like `{"id":"8.3.N","kind":"solve","eq":"Abs(x)=5","var":"x","answer":"5,-5"}` — verify sympy solves `Abs(x)=5`; if the checker can't handle `Abs` in `solve`, record as `manual` with the human answer.
- [ ] **Step 5 (8.3 retitle):** In `curriculum.yaml` set lesson 8.3 title → `"Absolute value: graphs & distance"`; update the `## Lesson 8.3:` header in the `.md` to match exactly; update the cosmetic outline gloss in `curriculum-map.md` if present. Then `python _verification/generate.py` to refresh tables.
- [ ] **Step 6 — gate:** run the four gate commands; Failures must be 0; alignment/generate/pytest green.
- [ ] **Step 7 — copyedit + review:** `/copyedit` the new U1 + 8.3 prose; run the review component (scope ceiling, notation, append-only, .md↔JSON parity); address.
- [ ] **Step 8 — PR:** commit, push, `gh pr create`, merge when green, delete branch.

---

## Task 2: PR2 — Equation theory & functions (U2 + U4) · `phase-1/u2-u4-equations-functions`

**Files:** `unit-02-linear-equations.md`, `unit-04-functions.md`, `_verification/unit-02.json`, `_verification/unit-04.json`. No SSOT change (append-within-lesson).

- [ ] **Step 1:** Branch off main.
- [ ] **Step 2 (U2 three-outcome):** In 2.4 (variables on both sides), add the framing: **conditional** (one solution), **identity** (both sides identical → infinitely many; e.g. 2x+4=2(x+2)), **contradiction** (false statement, e.g. 0=5 → no solution). Worked examples for each; practice mixing the three (trailing IDs). Minor: tighten "term" so the sign travels with it; consolidate the general solving strategy. JSON: `manual` for "identity/no-solution" classification; computational ones checked.
- [ ] **Step 3 (U4 correspondence + domain):** In 4.1 reword the definition to **correspondence/pairing** (each input → exactly one output), reserving "rule" for the 4.2 formula. In 4.2 add **discrete vs continuous domain** (finite/counting inputs → dots; all reals → unbroken line), no interval notation. Worked/practice as needed.
- [ ] **Step 4 — SOTA:** U2 strategy-choice (two valid solving orders side-by-side; which/why/when); U4 light bidirectional translation (table ↔ equation ↔ words).
- [ ] **Step 5:** Workflow draft+verify (2 agents, distinct files) → gate → copyedit → review → PR/merge.

---

## Task 3: PR3 — Linear functions (U5) · `phase-1/u5-linear-functions`

**Files:** `unit-05-linear-functions-graphs.md`, `_verification/unit-05.json`, `algebra-1-tutor/references/misconceptions.md` (slope entry), `curriculum.yaml` (+ lesson 5.6) + regenerate.

- [ ] **Step 1:** Branch off main.
- [ ] **Step 2 (new lesson 5.6, recommended):** Add `## Lesson 5.6: x-intercepts, graphing by intercepts & standard form` covering x-intercept (set y=0), graphing a line by both intercepts, and standard form Ax+By=C (convert to/from slope-intercept). Worked examples + ~10 practice. **SSOT sync:** add 5.6 to `curriculum.yaml` U5 lessons; add 5.6 to the `curriculum-map.md` lesson outline; `python _verification/generate.py`. (Fallback: fold into 5.2 + 5.5 append-within-lesson if it reads better — then no SSOT change.)
- [ ] **Step 3 (interpret-in-context):** In 5.3/5.4 worked examples, state slope & intercept story meaning; state the **constant-rate-of-change** defining property explicitly.
- [ ] **Step 4 (5.3 typo):** Read the 5.3 example with the (150, _) point; correct (150,50) → **(150,10)** (confirm via sympy against the stated rate); re-verify.
- [ ] **Step 5 (misconceptions slope entry):** Add a Slope entry to `misconceptions.md`: steepness vs **direction** (sign); magnitude is |slope|; *tell* + *repair*.
- [ ] **Step 6 (SOTA):** strategy-choice "slope two ways" (rise/run vs formula); one spot-the-error item from the new slope misconception.
- [ ] **Step 7:** Line-equation JSON entries carry `on_line`/`slope`. Gate (run `generate.py` first for the 5.6 sync) → copyedit → review → PR/merge.

---

## Task 4: PR4 — Back-half rigor (U9 + U10 + U11 + U12) · `phase-1/u9-u12-back-half-rigor`

**Files:** `unit-09-sequences-exponentials.md`, `unit-10-exponents-polynomials.md`, `unit-11-factoring.md`, `unit-12-quadratics.md`, and their four JSONs. No SSOT change.

- [ ] **Step 1:** Branch off main.
- [ ] **Step 2 (U9):** 9.2 — define the exponential as **well-defined** (a≠0, b>0, b≠1, one-sentence reasons each); fix "tied at x=2" → **tied at x=1 and x=2, dips below between** (verify the two curves numerically). 9.1 — name the **discrete domain** (counting numbers); geometric sequence = exponential restricted to those inputs; add **recursive and explicit** formulas for arithmetic & geometric (CCSS F-BF.A.2). Worked/practice with sympy-checked terms.
- [ ] **Step 3 (U10):** 10.2 — add a sci-notation worked example where the coefficient product exceeds 10 and renormalizes (e.g. (6×10⁴)(5×10³)=30×10⁷ → 3×10⁸). Practice incl. one renormalizing case. JSON: `eval`/`manual`.
- [ ] **Step 4 (U11):** Introduce **prime/irreducible trinomials** (not everything factors) + a stopping rule (no integer pair multiplies to ac and adds to b); scope to **factoring over the integers**; reframe the a²+b² note as "not factorable over the integers" (no complex numbers). `factor_check` entries for the factorable ones; `manual` "prime" for the irreducible ones.
- [ ] **Step 5 (U12):** Promote the **square-root property** to a named conditional rule ("if x²=k with k≥0 then x=±√k; if k<0 no real solution"). Keep discriminant real-only. Worked/practice.
- [ ] **Step 6 (SOTA):** factoring strategy-choice (U11/U12); interpret-in-context for growth/decay (U9).
- [ ] **Step 7:** Workflow draft+verify (4 agents, distinct files) → gate → copyedit → review → PR/merge.

---

## Task 5: PR5 — Statistics → Unit A (structural + content) · `phase-1/unit-a-statistics-promotion`

**Files:** `curriculum.yaml`, `_verification/generate.py` (H1_RE + test), `_verification/tests/` (new test), `algebra-1-tutor/references/units/appendix-statistics.md`, `_verification/appendix.json`, regenerated `curriculum-map.md` + `docs/CURRICULUM.md`.

- [ ] **Step 1:** Branch off main.
- [ ] **Step 2 — TDD the H1_RE tweak (main loop):** Add a pytest case asserting `# Unit A: Data & Statistics` aligns (and that `# Appendix A:` is no longer required). Run it → FAIL (current `H1_RE` rejects `Unit A`).
```python
# in _verification/tests/test_generate.py (or a new test module)
def test_unit_a_letter_scope_h1_accepted():
    # an H1 "# Unit A: Data & Statistics" must satisfy the H1 regex with title group == "Data & Statistics"
    import generate
    m = generate.H1_RE.search("# Unit A: Data & Statistics\n")
    assert m and m.group(3) == "Data & Statistics"
```
- [ ] **Step 3 — make it pass:** change `H1_RE` in `generate.py` from `Unit\s+(\d+)` to `Unit\s+(\d+|[A-Z])`. Run the test → PASS. Run full `pytest` → green.
- [ ] **Step 4 — promote in SSOT:** in `curriculum.yaml`, set unit `A` `optional: false`. (Title stays "Data & Statistics".)
- [ ] **Step 5 — retitle the .md H1:** `# Appendix A: Data & Statistics` → `# Unit A: Data & Statistics`; remove any "OPTIONAL — OFF THE MAIN PATH" framing in the prose; update the orientation paragraph to read as a core unit.
- [ ] **Step 6 — content elevation (A.1–A.3):** check-linearity-before-fitting; name **outliers**; tweak the two-way-table numbers so conditional rates differ (it now *shows association* — verify the rates differ via sympy); add the Algebra-1 regression/correlation layer (qualitative r sign/strength; correlation ≠ causation; **no** inferential stats). Add lesson **A.4 only if** warranted (then sync SSOT + outline). New problems → `appendix.json` (append-only `A.*`).
- [ ] **Step 7 — regenerate + gate:** `python _verification/generate.py` (drops the "(optional…)" render; adds A.4 row/outline if added); run the full gate; the new pytest case is green.
- [ ] **Step 8:** copyedit (appendix prose) → review → PR/merge.

---

## Task 6: PR6 — Cross-cutting cleanup · `phase-1/cross-cutting-cleanup`

**Files:** `unit-07-systems.md`, `unit-06-modeling-translation.md`, `unit-03-proportional-reasoning.md`, `algebra-1-tutor/references/visuals.md`, `docs/CURRICULUM.md` (scope note), possibly `algebra-1-tutor/SKILL.md` (only if the visuals.md fix is declined), relevant JSONs.

- [ ] **Step 1:** Branch off main.
- [ ] **Step 2 (U7.3):** correct the "adding two equations gives a line through the crossing point" claim — for inconsistent/dependent systems elimination yields a true/false numeric statement, not a line through an intersection. Re-verify any affected example. Optional: substitution-vs-elimination strategy-choice.
- [ ] **Step 3 (U6):** apply in-scope minors (6.3 scatter/line-of-best-fit framing consistent with the now-core Unit A); interpret-in-context.
- [ ] **Step 4 (departures):** add a "Scope & intentional departures" prose section to `docs/CURRICULUM.md` (outside the generated markers): (a) rational expressions omitted by design; (b) Unit 3 proportional reasoning is below the Algebra-1 line, kept as a bridge/review. Add a one-sentence reflection of (b) to unit-03's "Teaching this unit".
- [ ] **Step 5 (visuals/SKILL:125):** add the two missing templates (balance-scale, algebra-tiles) to `visuals.md` so SKILL.md:125's claim is true; do **not** edit SKILL.md behavior. (Fallback: minimal factual correction to the SKILL.md claim line only.)
- [ ] **Step 6 (residual minors):** sweep `research-output/01` per unit for remaining in-scope minor/enhancement items not owned by a later phase; apply.
- [ ] **Step 7:** gate → copyedit (shipped `.md` prose only) → review → PR/merge.

---

## Task 7: Phase close-out

- [ ] **Step 1:** On `main`, run the full gate; confirm 0 failures and green across the board.
- [ ] **Step 2:** Confirm every spec §4 finding is applied (majors + named minors + SOTA + departures), the two structural changes landed, append-only preserved.
- [ ] **Step 3:** Update project memory (`algebra-1-tutor-skill`) with Phase 1 completion + what shipped.
- [ ] **Step 4:** Summarize the phase (PRs, new problem counts, baseline delta) for the user.

---

## Self-review (spec coverage)

- §A U1 irrational/real + |a| → Task 1. · 8.3 rescope → Task 1.
- §B U2 three-outcome → Task 2. · §C U4 correspondence/domain → Task 2.
- §D U5 intercepts/standard-form/interpret + 5.3 typo + slope misconception → Task 3.
- §E U9 exponential/sequence + 9.2 → Task 4. · §F U10 sci-notation + U11 prime trinomials → Task 4. · §G U12 √-property → Task 4.
- §H Statistics promotion + content → Task 5.
- §I U7.3 + visuals/SKILL:125 → Task 6. · departures → Task 6.
- SOTA (strategy-choice/spot-the-error/interpret-in-context) → distributed across Tasks 2–4, 6.
- Gate green + copyedit + append-only + ceiling → Conventions + every task.
