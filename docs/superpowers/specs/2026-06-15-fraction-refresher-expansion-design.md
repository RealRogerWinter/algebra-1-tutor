# Design: Comprehensive Fraction Refresher (Lesson 2.5)

**Date:** 2026-06-15
**Branch / worktree:** `worktree-textbook+fraction-refresher-expand`
**Source of truth:** student `textbook-src/unit-02-linear-equations.md` (mirrored to tutor `algebra-1-tutor/references/units/unit-02-linear-equations.md`)

## Goal

Expand Lesson 2.5 ("Fraction refresher") from its current two skills (common
denominators for +/-, and reciprocals) into a comprehensive, intro-level
fraction primer that starts from "what a fraction is," adds the explicitly
missing **GCD / reducing** material, and grounds reciprocals in
multiplication/division. The existing content is preserved (math, problems,
answers) and re-seated into a fuller arc. New deterministic visuals support the
new material.

## Decisions (locked with the user)

- **Depth:** comprehensive primer (not a minimal GCD insert).
- **Structure:** expand *within* Lesson 2.5. No renumbering of Lesson 2.6+.
- **Visuals:** new deterministic SVG viz module `_verification/viz/fractions.py`
  (~6 samples), wired as numbered viz figures. Not Gemini raster, not figures.py.
- **Comparing fractions:** folded into the Equivalent/GCD section (no standalone
  section).
- **Practice load:** standard 8–12 sympy-verified problems per new section.

## Non-goals

- No change to Lesson 2.6 content or to any other lesson.
- No renumbering of lessons; no change to existing `refA.*` / `refB.*` answer
  data beyond what position-shift requires.
- No new Gemini raster illustrations (the existing pizza illustration stays; it
  may be re-placed in the arc but not regenerated).

## Lesson arc (final — five sections)

Concrete → pictorial → symbolic throughout. Existing content is marked *(keep)*.

1. **What a fraction means** *(new)*
   - Numerator = how many pieces; denominator = how big each piece is / how many
     make one whole. Unit fractions. A fraction's place on the number line.
   - "Bigger bottom number → smaller piece" (the pizza insight, pulled forward
     from the current Refresher A intro).
   - Light touch on improper fractions and mixed numbers, so an answer like 11/2
     reads as legitimate (ties to the existing 2.6 "a fraction is a fine answer"
     note).
2. **Equivalent fractions & reducing (GCD)** *(new — the requested gap)*
   - Multiplying or dividing top and bottom by the same number renames a fraction
     without changing its value (building up vs. reducing).
   - **GCD** to reduce to lowest terms: list-common-factors method *and* the
     quick divide-by-shared-factors method.
   - Comparison woven in: rename to a common denominator or judge against
     benchmarks (1/2, 1); place on a number line.
3. **Adding & subtracting: common denominators** *(keep — current Refresher A)*
   - Content preserved verbatim; now flows naturally out of §2 (equivalent
     fractions already established). Visuals refreshed.
4. **Multiplying & dividing** *(new)*
   - Multiply straight across, then reduce. Dividing = "flip and multiply,"
     which *motivates* the reciprocal before §5 uses it to solve.
5. **Reciprocals & solving (2/3)x = 6** *(keep — current Refresher B)*
   - Content preserved; now grounded by §4.

Reframed lesson intro widens the current "you need just two skills" framing to
the fuller arc, but keeps the existing off-ramp ("if fractions feel solid, skim;
test yourself on (2/3)x = 6").

Each section: short teaching prose → 3–5 worked examples (every result
sympy-verified) → a "Check for understanding" transfer prompt or two → a graded
8–12 practice block → answer key. A closing paragraph hands off to Lesson 2.6.

## Visuals — `_verification/viz/fractions.py`

New self-contained viz module following the established pattern
(`TITLE / KIND="deterministic-svg" / LESSONS / samples() -> [{caption, html}]`,
on the house palette, with an import-time sympy self-check). Registered in
`_verification/viz_figures.py` (`VIZ_FIGURES`, with `facts` where math is
assertable) and embedded via `<!--viz:fractions#index-->` markers in the student
source. Planned samples (~6):

1. **Fraction bar** — "3/4 means 3 of 4 equal pieces" (numerator/denominator roles).
2. **Number line** — the same 3/4 placed between 0 and 1.
3. **Equivalent split** — one bar cut into 4 then 8: 3/4 = 6/8.
4. **GCD reduce** — 6/8: group the eight pieces into pairs (divide both by GCD 2)
   to recover 3/4.
5. **Common denominator** — 3/4 and 1/6 renamed to twelfths on aligned bars
   (feeds §3).
6. **Multiply-as-area / reciprocal flip** — 1/2 × 2/3 as an overlap grid; the
   reciprocal as the same bar flipped.

Final sample count and which collapse may shift slightly during implementation;
the registry + markers are the source of truth and are CI-gated either way.

The existing Lesson 2.5 visuals stay: `<!--viz:anatomy#1-->` (fraction anatomy)
and the `illus-2-5-pizza-fractions` raster. They will be re-placed into the new
arc where they fit best (anatomy near §1; pizza near §1 or §3), not removed.

## Reference codes & numbering

- **Visible badges are `2.5.N`, auto-generated by document position** by
  `build_textbook._id_worked_practice` (confirmed against the built HTML — the
  current page carries `2.5.1`…`2.5.20`). Inserting new practice blocks ahead of
  the existing ones **renumbers** the existing problems by position. This is
  expected and mirrors the PR #38 set-math/numbering shift; it is not a code
  stability violation because these are position codes, not appended anchors.
- **`refA.*` / `refB.*` live only in the JSON verification layer**
  (`_verification/unit-02.json`); they are not the visible badges. New
  verification groups use `refC`, `refD`, `refE`, `refF` in document order.
- **Grammar regex must widen:** `check_alignment.py` and
  `_verification/tests/test_code_grammar.py` currently hard-code `ref[AB]`;
  change to `ref[A-Z]` so the new groups validate.
- Update `algebra-1-tutor/references/curriculum-map.md` line 51 (the 2.5
  summary) to describe the new arc.

## Dual-source parity

Every prose / worked-example / problem / answer change is mirrored into the
tutor file `algebra-1-tutor/references/units/unit-02-linear-equations.md` with
identical math, answers, and structure. `check_textbook_src` enforces parity by
recomputing both sources through the same `_id_worked_practice`. The tutor file
keeps its tutor-facing framing (Goal / Why it matters / New terms / Teaching arc
/ Watch for / Visuals to offer / CFU / Practice / Answer key per AUTHOR_GUIDE);
the student file keeps the warm student voice.

## Verification (all must pass before merge)

1. `python _verification/<each gate>.py` — notation, alignment (incl.
   `md_anchor_lint`), figure/viz lints, `check_textbook_src` parity,
   `check_answers` (sympy) over the new JSON entries.
2. `pytest` (full suite) — catches logic regressions `--check` cannot (per the
   `_CODE_RE`-shadowing lesson from PR #38).
3. `fractions.py` and `viz_figures.py --check` self-checks green.
4. Byte-deterministic build verified in the CI image:
   `docker run --rm -v <repo>:/work -w /work cimg/python:3.11 bash -lc "pip
   install -q -r requirements.txt && python _verification/build_textbook.py
   --check"` (run from PowerShell).
5. Headless render sweep of the 2.5 page(s): 0 KaTeX errors, 0 unrendered sets,
   0 horizontal overflow.

## Process (ultracode workflow, after plan approval)

1. **Research & red-team (parallel):** pedagogy research on teaching fractions to
   adult learners (part-whole vs. measurement models, GCD introduction, "why
   flip," number-line emphasis, common misconceptions) + an adversarial red-team
   of the *existing* 2.5 prose and answers + an audit of the current pizza /
   anatomy visuals for fit. Findings feed the draft.
2. **Draft prose:** write the new sections (both sources), sympy-verify every
   answer, run **all generated student-facing prose and figure captions through
   the `/copyedit` skill** before finalizing.
3. **Visuals:** build + self-check `fractions.py`, register in `viz_figures.py`,
   place `<!--viz:fractions#i-->` markers, re-seat existing visuals.
4. **Verify:** the full gate list above; regenerate `docs/` from merged sources;
   confirm byte-determinism in `cimg/python:3.11`.

## Copyedit scope note

Per the user instruction "subject any text you generate to /copyedit," the
`/copyedit` pass is applied to **shipping narrative prose** — the new lesson
sections (both sources) and figure captions. It is *not* applied to JSON answer
data, Python code, reference codes, or this spec scaffolding, where it would be
noise.

## Risks & mitigations

- **Position renumbering of 2.5.N badges** → update JSON + re-run
  `check_textbook_src`; verify the per-question answer reveal still pairs by
  position (PR #31 parser).
- **`main` moves mid-task** (it has through #42 already) → re-`git fetch`, merge
  latest `main`, regenerate `docs/` before any merge; poll `gh pr view --json
  mergeable`.
- **viz module import-time self-check** must be updated whenever displayed
  numbers change, or the build dies on import (PR #40 lesson).
- **Lesson length** → standard 8–12 practice keeps it comprehensive without
  bloat; the off-ramp lets fluent students skim.
