# Fraction Refresher Expansion — Implementation Plan

> **For agentic workers:** This plan is executed by an ultracode Workflow (the
> user opted in). Phases map to workflow phases; creative content (lesson prose,
> problems, SVG) is generated during execution, informed by Phase 1 research.

**Goal:** Expand Lesson 2.5 of the algebra textbook into a comprehensive
intro-level fraction primer (adding what-a-fraction-is, equivalent fractions,
GCD/reducing, multiply/divide) with new deterministic visuals, preserving all
existing content and downstream numbering.

**Architecture:** Dual-source markdown (student `textbook-src/` + tutor
`algebra-1-tutor/references/units/`), sympy-verified JSON answer layer
(`_verification/unit-02.json`), deterministic SVG viz module
(`_verification/viz/fractions.py`) registered in `_verification/viz_figures.py`
and embedded via `<!--viz:fractions#i-->` markers, built to `docs/` by
`_verification/build_textbook.py`, gated by the `_verification/check_*.py`
scripts + `pytest`.

**Tech Stack:** Python 3.11, sympy, python-markdown, KaTeX, CircleCI
(`cimg/python:3.11`), git worktree.

**Spec:** `docs/superpowers/specs/2026-06-15-fraction-refresher-expansion-design.md`

---

## File map

- **Modify** `textbook-src/unit-02-linear-equations.md` — student Lesson 2.5:
  reframed intro + 3 new sections, existing 2 sections re-seated.
- **Modify** `algebra-1-tutor/references/units/unit-02-linear-equations.md` —
  tutor Lesson 2.5: same math/problems/answers, tutor-facing framing.
- **Modify** `_verification/unit-02.json` — new sympy-checkable problems
  (groups `refC`/`refD`/`refE`/`refF` as needed).
- **Modify** `_verification/check_alignment.py` — widen `ref[AB]` → `ref[A-Z]`.
- **Modify** `_verification/tests/test_code_grammar.py` — add a `refC.*`-style
  good case so the widened grammar is tested.
- **Create** `_verification/viz/fractions.py` — deterministic SVG viz module.
- **Modify** `_verification/viz_figures.py` — register new `fractions` figures
  (`VIZ_FIGURES` entries with sympy `facts`).
- **Modify** `algebra-1-tutor/references/curriculum-map.md` — update the 2.5 line.
- **Regenerate** `docs/` via `build_textbook.py` (+ skill bundle if applicable).

---

## Phase 1 — Research & red-team (parallel, read-only)

- [ ] **1a. Pedagogy research** — best practices for teaching fractions to adult
  / returning learners: part-whole vs. measurement (number-line) models;
  introducing GCD and lowest terms; motivating "invert and multiply"; common
  misconceptions (add-across, bigger-denominator-is-bigger, treating fractions
  as two independent whole numbers). Output: a ranked list of teaching moves +
  pitfalls to adopt, with sources.
- [ ] **1b. Red-team existing 2.5** — adversarially read the current Lesson 2.5
  prose + worked examples + answer key (both sources) for math errors,
  ambiguous wording, misconception traps, and notation-guide violations. Output:
  a defect list (severity-tagged) to fix while expanding.
- [ ] **1c. Visual audit** — assess the current `<!--viz:anatomy#1-->` and
  `illus-2-5-pizza-fractions` for fit in the new arc; recommend placement and
  what the new `fractions.py` samples must cover (no overlap, no gaps).
- [ ] **1d. Convention scan** — confirm exact patterns by reading a sibling viz
  module (`bar_models.py` / `area_models.py`), `viz_figures.py` entry shape, the
  JSON schema in use, and `check_textbook_src` parity rules. Output: the precise
  templates to follow.

Acceptance: a consolidated findings brief the drafting phase consumes.

## Phase 2 — Draft prose (both sources) + problems

- [ ] **2a. Write the 3 new student sections + reframed intro** in
  `textbook-src/unit-02-linear-equations.md`, placing existing sections 3 & 5
  unchanged in the new order. Section content per spec arc. Insert
  `<!--viz:fractions#i-->` markers at the right sentences.
- [ ] **2b. Author the new practice problems** (8–12 per new section,
  easy→hard), with answer keys, choosing clean pedagogical numbers. Every
  computational answer **sympy-verified** before it is written.
- [ ] **2c. Mirror to the tutor source** with tutor-facing framing (Goal / Why /
  New terms / Teaching arc / Worked examples / Watch for / Visuals to offer /
  CFU / Practice / Answer key), identical math/problems/answers/order.
- [ ] **2d. Update `_verification/unit-02.json`** — add every new computational
  problem (`eval`/`simplify`/`solve`/`manual`), groups `refC`…`refF`. Run the
  central answer self-check; fix any mismatch.
- [ ] **2e. `/copyedit` pass** — run all new student-facing prose + figure
  captions through the copyedit skill; apply the house voice; re-mirror any
  wording changes to keep parity.

Acceptance: both sources updated, parity-consistent; all new JSON answers pass
the sympy self-check.

## Phase 3 — Visuals

- [ ] **3a. Build `_verification/viz/fractions.py`** — ~6 deterministic SVG
  samples (fraction bar, number line, equivalent split, GCD reduce, common
  denominator, multiply-as-area/reciprocal), house palette, with an import-time
  sympy/arithmetic self-check (`_verify`). Run `python -m` self-check.
- [ ] **3b. Register in `_verification/viz_figures.py`** — add `VIZ_FIGURES`
  entries (`code, module="fractions", index, facts`) with correct sympy facts
  for the asserted numbers; codes are `2.5.fN` appended after existing 2.5
  figures. Run `python _verification/viz_figures.py --check`.
- [ ] **3c. Confirm markers resolve** — `_convert_viz` embeds each sample;
  re-place `anatomy#1` and the pizza illus into the new arc.

Acceptance: module self-check + `viz_figures --check` green; markers bidirectional-synced.

## Phase 4 — Build, gate, verify

- [ ] **4a. Widen grammar** — `ref[AB]`→`ref[A-Z]` in `check_alignment.py`; add
  test case in `test_code_grammar.py`.
- [ ] **4b. Update `curriculum-map.md`** 2.5 line.
- [ ] **4c. Regenerate `docs/`** — `python _verification/build_textbook.py`
  (and the skill bundle if the build emits it).
- [ ] **4d. Run the full gate suite** — every `_verification/check_*.py`,
  `viz_figures.py --check`, `figures`/viz lints, `check_textbook_src` parity,
  and `pytest` (full suite, per the PR #38 `_CODE_RE`-shadow lesson). Fix until
  green.
- [ ] **4e. Byte-determinism in CI image** — `docker run --rm -v <repo>:/work -w
  /work cimg/python:3.11 bash -lc "pip install -q -r requirements.txt && python
  _verification/build_textbook.py --check"` from PowerShell. Expect no diff.
- [ ] **4f. Headless render sweep** of the 2.5 page(s): 0 KaTeX errors, 0
  unrendered sets, 0 horizontal overflow.

Acceptance: all gates + pytest + determinism + render sweep pass.

## Phase 5 — Integrate & PR

- [ ] **5a. Sync main** — `git fetch origin`; merge latest `origin/main` into the
  branch; regenerate `docs/` if the build changed; re-run gates.
- [ ] **5b. Commit** sources, JSON, viz module, registry, lints, regenerated
  `docs/`, curriculum-map — grouped logically.
- [ ] **5c. Open PR** to `main` with a summary (what expanded, new visuals,
  verification evidence). Poll `gh pr view --json mergeable` until ready.

Acceptance: green PR, mergeable, against latest `main`.

---

## Self-review

- **Spec coverage:** every spec section maps to a task — arc (2a–2c), GCD (2a),
  visuals (3), codes/grammar (4a/2d), parity (2c/4d), verification (4), copyedit
  (2e), process/red-team (1). ✓
- **Placeholders:** none — content is generated in-phase by design (this is a
  content task; exact prose/SVG are produced during execution, not pre-written).
- **Consistency:** module name `fractions`, marker `<!--viz:fractions#i-->`,
  codes `2.5.fN`, JSON groups `refC…refF`, grammar `ref[A-Z]` used consistently.
