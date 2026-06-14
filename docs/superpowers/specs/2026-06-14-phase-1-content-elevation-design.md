# Phase 1 — Content elevation (per unit; Statistics promoted) — design spec

> **Status:** drafted 2026-06-14 for approval. Implements **Phase 1** of `docs/REBUILD_PLAN.md`
> (the approved 8-phase roadmap; companions `REBUILD_BRIEF.md`, `RESEARCH_REDTEAM_HANDOFF.md`).
> Authoritative per-finding to-do list: `research-output/01-findings-confirmed.md` (sliced per unit).
> Project memory: `algebra-1-tutor-skill`, `claude-ai-skill-constraints`. Builds on Phase 0
> (merged to `main`): the `curriculum.yaml` SSOT + the `check_alignment.py` CI gate.

## 1. Context & scope

The course is **sound** (0 critical findings; 0 answer-key math errors across 543 sympy-checked
answers). Phase 1 is **elevation, not repair**: apply the confirmed red-team findings unit by unit
to lift an already-strong course to college-text rigor, **held inside Algebra-1 scope**. Baseline
gate is green today: `verify_answers.py` → **765 / 543 / 0**; `check_alignment.py`, `generate.py
--check`, and `pytest` (28) all green.

**In scope (this phase):**
- The **33 major** findings + the named **minor math-error / prose** fixes + the in-scope
  minor/enhancement items, applied per unit, **majors first** (full list: `research-output/01`).
- Two **structural** changes: **promote Statistics to a core unit** (in place) and **rescope 8.3**
  (absolute value) to the Algebra-1-legitimate piece.
- The **SOTA-pedagogy** moves: strategy-choice, spot-the-error study items, interpret-in-context —
  woven into the relevant lessons.
- **Document** (do not "fix") two intentional departures: rational expressions omitted;
  proportional reasoning (Unit 3) as a labeled below-the-line bridge/review.

**Explicitly NOT in scope (later phases — do not start here):**
- Reference-code *tagging* of `.md` items (`d`/`f`/`c`/… anchors) — **Phase 2**. Phase 1 keeps the
  existing JSON ID forms (`w`/`ex`/practice), which the code-grammar lint already accepts.
- The figure library — **Phase 3**. Phase 1 references `visuals.md` templates the way the shipped
  files already do; it authors **no** figures and adds no `FIG` codes.
- HTML textbook — **Phase 4**. Tutor guide / complementary problem sets — **Phase 5**.
- `SKILL.md` **behavior/voice** changes (multimodal photo protocol, house-voice persona block,
  reference-code resolution) — **Phase 6**. Phase 1 touches `SKILL.md` only for the one factual
  consistency fix (the `:125` template claim, see PR6) and makes **no** persona/behavior edits.
- The Algebra-1 **ceiling** (held throughout): no logarithms; no complex/imaginary numbers (hold the
  real-solutions ceiling on the discriminant); no rational or radical *functions*, asymptotes, or
  partial fractions; no polynomial division or degree>2 as a strand; no conics beyond the quadratic
  parabola; no matrices, series/summation/binomial theorem, trigonometry, or function
  composition/general inverses. **Raise rigor; do not expand topic scope.**

## 2. Goals / non-goals

**Goals**
1. Apply every in-scope confirmed finding, majors first, unit by unit, at college-text rigor.
2. Promote Statistics to a core unit (in place, append-only) and rescope 8.3 — both keeping the
   Phase 0 gate green.
3. Add the three SOTA-pedagogy elements where the problem types live.
4. Every **new** computational answer sympy-verified and recorded in the unit JSON; the
   `verify_answers.py` failure count stays **0** (totals grow as problems are added).
5. All **new shipped prose** passes `/copyedit` (instructional-tutor target) and the notation
   invariant.
6. Reference codes (JSON IDs) stay **append-only** — never renumber.

**Non-goals:** authoring figures (Phase 3); tagging `.md` items with `d`/`f`/`c` codes (Phase 2);
any `SKILL.md` behavior/voice work (Phase 6); the HTML textbook or complementary problems
(Phases 4–5); expanding topic scope past the Algebra-1 ceiling.

## 3. Approach & invariants (hold on every PR)

- **Gate-green before every PR.** Run the full baseline gate; open the PR only when green:
  `verify_answers.py` (0 failures), `check_alignment.py` (green), `generate.py --check` (green),
  `pytest`. New verified problems raise the totals; **0 failures is the invariant**, not 765.
- **Append-only IDs.** New worked examples / problems get **new trailing IDs** within their lesson
  (`8.3.w3`, `5.6.4`, `A.2.7`). Never renumber or reuse an existing ID. Demoted/relocated material
  keeps its existing ID (e.g., moved under a "Reach beyond" note); it is not deleted-and-reused.
- **Verify-before-write (the content analog of TDD).** Per `AUTHOR_GUIDE.md`: every numeric/algebraic
  answer is sympy-checked *before* it is written into the `.md`, then recorded in `unit-NN.json` /
  `appendix.json`. Line-equation `solve` entries (find intercept `b`) **must** carry
  `on_line` (+ `slope` for one-point) or the point-on-line lint fails.
- **Notation invariant.** Shipped `.md`: inline math is plain Unicode (x², √12, ½, ±, ≤, →); real
  notation only in `$$…$$` display blocks; never `\(...\)` or lone `$...$`. `check_notation.py`
  enforces this on `algebra-1-tutor/**.md` (SKILL.md excluded). `docs/**` is build-only and exempt.
- **Copyedit gate (R4).** New shipped **prose** runs through `/copyedit` with an instructional-tutor
  voice target (keeps natural second-person "you"). Math, answer keys, JSON, and planning/build docs
  are exempt.
- **SSOT sync discipline.** Any **structural** change (new lesson, retitle, optional-flip, unit
  retitle) updates `curriculum.yaml` **and** the unit `.md` header(s) **and** the curriculum-map
  lesson-outline, then **regenerates** the tables (`python _verification/generate.py`) so
  `generate.py --check` stays green. Most Phase 1 work is **append-within-lesson** and touches no SSOT.

**Per-PR working style (full autonomy, confirmed):** implement each PR via an **ultracode workflow**
(fan-out drafting per unit/lesson → sympy-verify the new answers → an adversarial pass: scope-ceiling
+ notation + append-only-ID + copyedit), with **TDD** on the one code change (the `generate.py`
`H1_RE` tweak in PR5: failing test first). Then I integrate, run the full gate, run a **review
component** (the `requesting-code-review` skill / a review agent — **not** `/code-review`), address
it, and **PR + merge once the gate is green and review is addressed**. Each branch is cut off the
latest `main`; PRs merge sequentially (no concurrent edits to shared files → no `curriculum.yaml`
conflicts).

## 4. The six PRs (theme-batched; majors first)

Branches off `main`, merged in order. Each cites the handoff §2.2 theme letter and the
`research-output/01` line range that is the authoritative checklist for that unit.

### PR1 — Number-line & distance · `phase-1/u1-u8-number-line-distance`
*Units 1 + 8.3. Findings: handoff §A, §I-8.3; `01` lines 4–30 (U1), 206–235 (U8).*
- **U1.2** — add a light **irrational / real** layer: name irrational numbers (π, √2 as
  non-repeating non-terminating), and **"real = every point on the line"** (closing the existing
  "algebra uses the whole line" claim, currently unnamed at unit-01 line 103). New terms; 1–2 worked
  examples; classify-style practice (`manual` JSON). *Core Algebra 1, not scope-creep.*
- **U1.4** — introduce **absolute value |a| = distance from 0** alongside the existing
  "opposite/additive inverse" (unit-01 line 209). This is the **distance** sense that 8.3 builds on
  (graphing/distance, **not** algebraic solving). New term; worked examples; practice (|a| values are
  `eval`-checkable or `manual`).
- **8.3 rescope** — keep the Algebra-1-legitimate core: the **V-shape graph of y=|x|** (+ simple
  transformations) and **absolute value as distance from zero** — the symmetric, no-algebra cases:
  |x|=k → x=±k; |x|<k → −k<x<k; |x|>k → x<−k or x>k (pairs with U1.4). **Demote** the general
  algebraic `|ax+b|=c` / `|ax+b|<c` + interval-notation solving to a clearly-labeled, off-the-mastery-path
  **"Reach beyond Algebra 1"** note at the end of 8.3 (one short worked example, flagged as beyond
  the course). This note doubles as the documented scope boundary.
- **8.3 retitle (recommended):** `Absolute-value equations & inequalities` →
  `Absolute value: graphs & distance` — a 2-line SSOT sync (`curriculum.yaml` lesson 8.3 + the `.md`
  `## Lesson 8.3:` header; outline is id-checked only). 8.3 **stays 8.3** (append-only); existing
  8.3 problems that are pure algebraic-solving move under the "Reach" note keeping their IDs; new
  distance/graph problems get trailing IDs.
- **Carries** the `.gitattributes` pin (`eol=lf` on the two generated files —
  `curriculum-map.md` + `docs/CURRICULUM.md`, which `generate.py` already writes LF-only) that ends
  the Windows CRLF carry-over on regenerated files (handoff "cosmetic carry-over").
- **Gate:** U1 additions are append-within-lesson (no SSOT change); 8.3 retitle is the one SSOT sync
  → regenerate tables. New problems sympy-verified into `unit-08.json` (and any U1 `eval` items into
  `unit-01.json`).

### PR2 — Equation theory & functions · `phase-1/u2-u4-equations-functions`
*Units 2 + 4. Findings: handoff §B, §C; `01` lines 31–61 (U2), 94–122 (U4).*
- **U2** — add the **three-outcome framing**: a linear equation is **conditional** (one solution),
  an **identity** (infinitely many — both sides identical), or a **contradiction** (no solution —
  a false statement like 0 = 5). Follows directly from variables-on-both-sides (2.4). Minor (same
  PR): consolidate the explicit general solving strategy; tighten the "term" definition so the
  **sign travels with the term**.
- **U4.1** — define a function as a **correspondence / pairing** (each input paired with exactly one
  output), reserving the word **"rule"** for the **4.2** formula. The unit's own examples are
  pair-sets/tables, so "correspondence" matches them; "rule/formula" is the special case.
- **U4.2** — name **discrete vs continuous domain** (no interval notation): a finite/counting-number
  input set vs. "all real numbers" — why the graph is dots vs. an unbroken line.
- **SOTA:** strategy-choice in U2 (two valid solving orders side-by-side — which/why/when each wins);
  bidirectional translation light-touch in U4 (table ↔ equation ↔ words).
- **Gate:** content-only, append-within-lesson; no SSOT change. New `manual`/computational entries
  into `unit-02.json` / `unit-04.json` as applicable.

### PR3 — Linear functions · `phase-1/u5-linear-functions`
*Unit 5. Findings: handoff §D, §I-slope; `01` lines 123–154.*
- Add **x-intercept, graphing-by-intercepts, and standard form Ax+By=C** — standard Algebra-1
  content currently missing. **Recommended:** a new trailing lesson **5.6** "x-intercepts, graphing
  by intercepts & standard form" (append-only: 5.1–5.5 unchanged; SSOT + `.md` + outline sync +
  regenerate). If it reads better folded into 5.2 (graphing) + 5.5 (writing equations), fold instead
  as append-within-lesson — decided at implementation; either way append-only.
- **Interpret slope & intercept in context** (story meaning) in each linear worked example; state the
  **constant-rate-of-change** defining property explicitly.
- **5.3 minor math-error:** correct the coordinate typo — the point is **(150, 10)**, not (150, 50)
  (confirmed by independent sympy check in the handoff). Re-verify the affected example.
- **`misconceptions.md` — new Slope entry:** steepness vs **direction** (sign), and that magnitude is
  |slope| (a bigger |slope| is steeper regardless of sign). This new entry seeds the U5
  spot-the-error item.
- **SOTA:** strategy-choice "**slope two ways**" (rise/run from the graph vs. the
  (y₂−y₁)/(x₂−x₁) formula); a **spot-the-error** item drawn from the new slope misconception;
  interpret-in-context throughout.
- **Gate:** the new 5.6 lesson (if taken) is an SSOT sync → regenerate. New line-equation `solve`
  problems carry `on_line` (+ `slope` for one-point) per the point-on-line lint. New problems
  sympy-verified into `unit-05.json`.

### PR4 — Back-half rigor · `phase-1/u9-u12-back-half-rigor`
*Units 9, 10, 11, 12. Findings: handoff §E, §F, §G; `01` lines 236–262, 263–284, 285–310, 311–342.*
- **U9** — make the exponential object **well-defined**: a≠0, b>0, b≠1, each with a one-sentence
  reason. Name the **discrete domain** (counting numbers) and that a **geometric sequence is an
  exponential restricted to those inputs**. Add **recursive *and* explicit** formulas for
  arithmetic/geometric sequences (meets CCSS F-BF.A.2). **9.2 minor math-error:** "tied at x=2" →
  the curves are **tied at x=1 and x=2, and the exponential dips below between** (handoff-confirmed).
- **U10.2** — add a **scientific-notation worked example where the coefficient product exceeds 10**
  and must renormalize (e.g., 30×10⁷ → 3×10⁸). Keep sci-notation as Grade-8 fluency maintenance
  (in-scope).
- **U11** — introduce **prime / irreducible trinomials** (not everything factors) with an explicit
  **stopping rule**, and scope the unit to **factoring over the integers** (reframe the a²+b² note as
  "not factorable over the integers," **not** complex numbers — holds the ceiling).
- **U12** — promote the **square-root property to a named conditional rule**: *if x²=k with k≥0 then
  x=±√k; if k<0 there is no real solution.* Keep the discriminant **real-only** (the optional
  rational-vs-irrational-roots connection may be added as a note, but **no** complex roots).
- **SOTA:** strategy-choice on factoring approaches (U11/U12); interpret-in-context for exponential
  growth/decay (U9).
- **Gate:** content-only, append-within-lesson (recursive/explicit formulas fit 9.1; well-defined
  exponential fits 9.2; no new lessons). New problems sympy-verified into the four unit JSONs.

### PR5 — Statistics → Unit A · `phase-1/unit-a-statistics-promotion`
*Appendix A. Findings: handoff §H; `01` lines 343–374. The structural promotion + content elevation.*
- **Promote in place (append-only):** flip `optional: true → false` in `curriculum.yaml` (the
  generated tables then drop the "(optional, off the main path)" render automatically). Keep scope
  **`A`** and all `A.*` IDs — **no renumber**, **no mid-sequence insert** (Unit A stays **trailing**
  after Unit 12).
- **`generate.py` `H1_RE` tweak (TDD):** `^#\s+(?:Unit\s+(\d+)|Appendix\s+([A-Z])):…` →
  accept a **letter scope after "Unit"** (e.g. `Unit\s+(\d+|[A-Z])`), so the H1 can read
  `# Unit A: Data & Statistics`. Write the failing test first (a `# Unit A:` H1 must align), then
  make the change. `LESSON_RE` and `_unit_md_path("A")` already handle `A`.
- **Retitle the H1:** `# Appendix A: Data & Statistics` → `# Unit A: Data & Statistics` (the SSOT
  `title` stays "Data & Statistics"; only the prefix changes). **Drop** the "OPTIONAL — OFF THE MAIN
  PATH" framing from the prose.
- **Content elevation (within A.1–A.3):** teach **checking the cloud is roughly linear before
  fitting** a line; **name outliers**; make the **two-way table show association** (tweak the numbers
  so the conditional rates differ); add the genuinely-Algebra-1 **regression/correlation** layer
  (interpret r's sign/strength qualitatively; correlation ≠ causation — **no** inferential stats,
  no formal regression computation beyond line-of-best-fit reasoning). Add a new lesson **A.4 only
  if** a dedicated lesson is warranted; **never** renumber A.1–A.3.
- **Gate:** SSOT sync (optional flip, + A.4 if added) → **regenerate** `curriculum-map.md` +
  `docs/CURRICULUM.md`; if A.4 added, add it to the lesson-outline. Update/add a `pytest` case for
  the letter-scope H1. New problems sympy-verified into `appendix.json` (append-only `A.*`).

### PR6 — Cross-cutting cleanup · `phase-1/cross-cutting-cleanup`
*Residual minors + departures + bank consistency. Findings: handoff §I, §3; `01` lines 155–205
(U6/U7), 375–410 (banks), plus residual per-unit minors not yet placed.*
- **U7.3 minor math-error:** the claim "adding two equations gives a line through the crossing point"
  is **false** for inconsistent/dependent systems — correct it (elimination produces a true/false
  numeric statement in those cases, not a line through an intersection). Optional SOTA here:
  **substitution vs elimination** strategy-choice.
- **U6** — apply any in-scope minors (e.g., scatter-plot/line-of-best-fit framing in 6.3 consistent
  with the promoted Unit A); interpret-in-context.
- **Documented departures (do not "fix"):** add a short **"Scope & intentional departures"** note to
  `docs/CURRICULUM.md` (build doc; copyedit/notation-exempt) — (a) **rational expressions omitted**
  (narrower than traditional OpenStax, by design); (b) **proportional reasoning (Unit 3) is below the
  Algebra-1 line** (Grade 6–7), kept as a labeled **bridge/review** unit. Add a one-sentence
  reflection of (b) to unit-03's "Teaching this unit" orientation.
- **`visuals.md` / `SKILL.md:125` reconciliation:** `SKILL.md` claims balance-scale and algebra-tile
  **templates** exist in `visuals.md` but they don't. **Resolve by adding the two missing templates
  to `visuals.md`** (content elevation that makes the claim true and serves U1/U2 balance-scale and
  U10/U11 algebra-tiles) — **not** by editing `SKILL.md` behavior (Phase 6). If a template is genuinely
  not wanted, the fallback is a minimal factual correction to the `SKILL.md` claim line only.
- **Residual minors:** sweep the remaining in-scope minor/enhancement items per `research-output/01`
  for any unit, applying those that raise rigor and are not owned by a later phase.
- **Gate:** mostly content/build-doc; `docs/**` edits are exempt from notation/copyedit; shipped-`.md`
  edits (unit-03, unit-06, unit-07, visuals.md, misconceptions.md) hold the notation + copyedit gates.

## 5. SOTA-pedagogy placement (handoff §4)

| Move | Where it lands |
|---|---|
| **Strategy-choice** (two valid methods side-by-side; which/why/when) | U2 (solving orders), U5 (slope two ways), U11/U12 (factoring approaches), U7 (subst vs elim, optional in PR6) |
| **Spot-the-error** (pair correct + incorrect, from `misconceptions.md`, *proactive*) | One item per heavy unit, drawn from that unit's misconception section (U1 =/negatives, U2, U5 slope, U11 sign errors, …) |
| **Interpret-in-context** (context ↔ table ↔ equation ↔ graph) | U5 (slope/intercept story), U6 (modeling), U9 (growth/decay) |

Interleaving (the biggest lever) and the complementary mixed-review sets are **Phase 5** (R1); Phase 1
only seeds the spot-the-error/strategy-choice study items the later sets will draw on.

## 6. Structural-change mechanics (precise — the gate-sensitive parts)

**Statistics promotion (PR5).** Files: `curriculum.yaml` (optional flip; +A.4 if added),
`_verification/generate.py` (`H1_RE` letter-scope tweak + a test), `appendix-statistics.md` (H1
retitle, drop OPTIONAL framing, content), `appendix.json` (append-only), regenerated
`curriculum-map.md` + `docs/CURRICULUM.md` (+ outline if A.4). The file name
`appendix-statistics.md` does **not** need to change (`_unit_md_path("A")` resolves it). The map
table renders Unit A **last** (SSOT order) → trailing, no renumber.

**8.3 rescope (PR1).** Content within `unit-08-inequalities.md` lesson 8.3; optional retitle syncs
`curriculum.yaml` lesson 8.3 + the `.md` header (+ cosmetic outline gloss). Demoted solving keeps its
IDs under the "Reach beyond Algebra 1" note; new V-shape/distance problems get trailing IDs in
`unit-08.json`.

**U5 new lesson 5.6 (PR3, recommended).** Append-only trailing lesson: `curriculum.yaml` U5 +5.6,
`.md` `## Lesson 5.6:` header, curriculum-map outline +5.6, regenerate. 5.1–5.5 untouched.

All other PRs are append-within-lesson and touch **no** SSOT structure.

## 7. Verification & acceptance

**Per PR (all must hold before the PR opens):**
1. `python _verification/verify_answers.py` → **0 failures** (totals ≥ 765, growing).
2. `python _verification/check_alignment.py` → green (alignment + notation + point-on-line +
   code-grammar).
3. `python _verification/generate.py --check` → green; running `generate.py` is idempotent (clean
   second diff).
4. `python -m pytest _verification/tests` → green (incl. the new letter-scope H1 test from PR5).
5. `/copyedit` run on all new shipped prose (instructional-tutor target); changes applied.
6. Review component run and addressed; append-only IDs verified; the Algebra-1 ceiling held.

**Phase-end:** every in-scope confirmed finding applied (majors + named minors + in-scope
minor/enhancement), the two structural changes landed, the three SOTA moves placed, the two
departures documented, gate green on `main`, baseline failures still 0.

## 8. Risks & mitigations

- **Scope creep past the Algebra-1 ceiling** → the §1 ceiling list is restated as a per-PR
  review-pass check; the 8.3 "Reach beyond" note and the U11/U12 real-only framing are the explicit
  boundary markers; the documented departures keep reviewers reading omissions as choices.
- **Breaking the Phase 0 gate via a structural change** → §6 enumerates every SSOT-touching edit;
  the `H1_RE` tweak ships TDD with a test; regenerate-then-`--check` is part of each structural PR.
- **A wrong new answer key** → verify-before-write (sympy) + the JSON record + `verify_answers.py`;
  line-equation entries forced through the point-on-line lint.
- **Notation regressions in new prose** → `check_notation.py` in the gate; Unicode-inline / `$$`-display
  discipline; `docs/**` kept build-only.
- **Voice drift in new prose** → the `/copyedit` gate (R4) with the instructional-tutor target.
- **ID churn** → append-only discipline; demoted material keeps its IDs; the code-grammar lint
  catches malformed new IDs.

## 9. Deliverables

- This spec + the Phase 1 implementation plan (`docs/superpowers/plans/`).
- Six PRs (§4), each gate-green and copyedited, merged to `main` in order.
- Edited shipped `.md` (units 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, appendix; `misconceptions.md`,
  `visuals.md`), their `_verification/*.json` (append-only verified problems), `curriculum.yaml`
  (Stats optional-flip, 8.3 + 5.6 retitles/additions), `_verification/generate.py` (H1_RE tweak +
  test), regenerated `curriculum-map.md` + `docs/CURRICULUM.md`, a `.gitattributes` eol pin, and the
  `docs/CURRICULUM.md` scope-departures note.
