# Phase 3 — Figure library — design spec + plan

> **Status:** self-authored 2026-06-14 under the user's blanket autonomy grant (absent user).
> Implements **Phase 3** of `docs/REBUILD_PLAN.md`. Builds on Phase 2 (the reference-code grammar
> already **reserves the `f` tag**; this phase assigns real f-codes to generated figures).
> Companions: `RESEARCH_REDTEAM_HANDOFF.md` §6 (figures resolved), `REBUILD_BRIEF.md` R2,
> `claude-ai-skill-constraints` (bundle-not-fetch; inline-SVG-artifact path).

## 1. Context & scope

Figures must be **programmatic, not generative-AI** (accuracy requirement): computed SVG from
coordinate data, each backed by a reproducible spec, sympy-accuracy-checked, then **bundled into the
skill** (the tutor reads the local SVG and re-emits it as an Artifact — no runtime fetch, math exact).
This supersedes the current "compute coordinates and eyeball an artifact at runtime" instruction.

**In scope:**
- A figure **spec registry** + a deterministic **SVG renderer** + a **sympy accuracy checker**
  (`_verification/figures.py`), TDD.
- A curated, accurate figure set covering the curriculum's **coordinate-graph needs** (where
  "LLM-eyeballed coordinates → wrong picture" is the real risk): lines, parabolas, the V-graph,
  a 2-D inequality region, scatter+fit, and polished number lines. Source: the lessons whose
  "Visuals to offer" names a real artifact figure (5.x lines, 4.3, 7.4, 12.6/12.2, 8.2/8.3/8.4,
  6.3/A.2, 1.2).
- Generated SVGs stored in **`algebra-1-tutor/figures/<code>.svg`** (bundled in the skill).
- **f-code assignment**: anchor each figure in its lesson (`{#N.M.fK}`), completing Phase 2's
  deferred `f` tagging.
- A **`figure_lint`** in `check_alignment.py`: every `fN` anchor has a bundled SVG and vice-versa
  (bidirectional), plus a staleness check (regenerating matches the committed SVG) and the sympy
  accuracy gate.
- Update `SKILL.md` (figure-emission instruction) and `visuals.md` (point to bundled figures).

**Not in scope:** figures for cases already served by ASCII/LaTeX in chat (balance scales, area-model
`array` boxes, simple tables, "none needed" lessons) — those stay as-is. PNG export (SVG is
canonical). The HTML-textbook embedding of figures is Phase 4 (it consumes these SVGs by f-code).

## 2. Figure types (accuracy-critical)

| type | params | sympy accuracy check |
|---|---|---|
| `number_line` | min,max,ticks,points[],segments[] | marked points lie at stated coords; in range |
| `line` | m,b,xwindow | endpoints satisfy y=mx+b; intercept correct |
| `parabola` | a,b,c,xwindow | vertex=(-b/2a, c-b²/4a); roots solve ax²+bx+c=0; samples on curve |
| `vgraph` | k (y=|x|+ shift), window | sampled points satisfy y=\|x\|(+shift) |
| `inequality_region` | m,b,op,xwindow | test point's truth matches the shaded side |
| `scatter` | points[], fit{m,b} | fit endpoints on the line; points in window |

The rendered coordinates and the accuracy-checked features come from the **same computation**, so a
passing accuracy check guarantees the SVG's math is correct. Rendering style mirrors the existing
`visuals.md` templates (axes, labels, key points, ~220px viewBox).

## 3. Architecture

- **`_verification/figures.py`** (build tooling, not shipped): `FIGURES` registry (list of specs,
  each with `code`, `lesson`, `type`, params, `caption`); `render(spec)->svg`; `accuracy_issues(spec)`;
  `generate()` writes `algebra-1-tutor/figures/<code>.svg`; `check()` = accuracy + staleness;
  `main(--check)`.
- **`algebra-1-tutor/figures/<code>.svg`** (shipped): one reviewed SVG per figure, filename = f-code
  (e.g. `5.4.f1.svg`).
- **`check_alignment.py`** gains `figure_lint()`: bidirectional f-anchor ↔ SVG-file, wired into
  `main()`.
- **f-anchors** added in the unit `.md` on the lesson's "Visuals to offer" line (leading the named
  figure), e.g. `**Visuals to offer:** {#5.4.f1} ...`.

## 4. Plan (TDD; one PR: `phase-3/figures`)

1. **TDD `accuracy_issues`** — failing tests first (a correct line/parabola passes; a wrong vertex or
   off-line endpoint is caught), then implement the checker + the coordinate/feature computation.
2. **Implement `render`** per type (compact SVG; valid XML smoke test).
3. **Author the `FIGURES` registry** — the curated set, each spec's math drawn from the lesson's
   worked example.
4. **`generate()` + `check()`** — write SVGs; `--check` verifies staleness + accuracy. TDD the
   staleness check.
5. **Add f-anchors** in the units (`{#N.M.fK}` on the Visuals line). The Phase-2 `md_anchor_lint`
   already validates these (dense, unique, grammar, SSOT).
6. **`figure_lint`** in `check_alignment.py` (bidirectional anchor↔file) + tests; wire into `main()`.
7. **Docs:** `SKILL.md` — replace "compute & eyeball" with "read the bundled `figures/<code>.svg`
   and emit it as an Artifact; the math is pre-verified"; `visuals.md` — note the bundled figures are
   canonical (templates remain for any ad-hoc graph). `/copyedit` the SKILL.md prose change.
8. **Gate + lean review (single subagent) + PR + merge.**

## 5. Verification

`figures.py --check` (accuracy + staleness) green · `check_alignment.py` green (incl. `md_anchor_lint`
for the new f-anchors + `figure_lint`) · `generate.py --check` green · `verify_answers.py` 909/614/0 ·
`pytest` green · `check_notation.py` clean. SVGs are valid XML and render. **Human visual review of
figure legibility is flagged as pending** (programmatic accuracy is guaranteed; aesthetic sign-off is
the one thing an absent user must do later).

## 6. Risks

- **Illegible/overlapping labels** (no human eye) → keep figures simple, one concept each, generous
  spacing; flag for human visual review.
- **Figure math wrong** → sympy accuracy gate on every figure (the core safeguard).
- **f-code churn vs Phase 2** → Phase 2 deferred `f` precisely so codes attach to real figures here;
  append-only, dense per lesson.
- **Stale committed SVG** → `--check` regenerates and diffs (like `generate.py`).
