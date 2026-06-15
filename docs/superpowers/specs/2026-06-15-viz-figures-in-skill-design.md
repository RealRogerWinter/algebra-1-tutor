# Spec: Bundle viz figures as tutor artifacts

**Date:** 2026-06-15
**Branch:** `textbook/viz-figures-in-skill`
**Status:** Approved (design), proceeding autonomously to plan + implementation.

## Problem

The student HTML textbook embeds two kinds of numbered `f` figures:

1. **Deterministic figures** (`_verification/figures.py`) — pure SVG, **bundled** into the
   skill at `algebra-1-tutor/figures/<code>.svg` (23 files).
2. **Viz figures** (`_verification/viz_figures.py` → `VIZ_FIGURES`) — HTML/CSS/SVG +
   dependency-free inline JS, rendered only in the website build via `<!--viz:module#index-->`
   markers. **40 figures, none bundled into the skill.**

Every `f` badge in the textbook is a one-click tutor launcher (PR #23): clicking it pastes a
deterministic "show me figure `<code>`" prompt into the Claude.ai tutor. For a viz code (e.g.
`3.2.f1`), SKILL.md's figure-resolution recipe reads `figures/<code>.svg`, finds nothing, and —
because the fallback language says the figure "may not have been added… I won't invent one" —
the tutor **refuses outright**. So ~40 real, student-visible figures are unreachable from the
tutor, and clicking their launcher badges produces a flat denial.

Confirmed inventory on this branch: 40 viz figures; 32 contain KaTeX/TeX in the body
(`\frac`, `\sqrt`, `$$…$$`); 6 are live interactive widgets (`interactive_equation`,
`interactive_graph`); bodies use rich HTML (`div`, `table`, `style`, `script`, inline SVG).

## Goal

Full parity with the deterministic SVGs: the tutor emits the **real** figure for every viz
code, as a self-contained artifact — interactive widgets stay live, math renders, light/dark
both look right — and never refuses a code that resolves to a bundled file.

## Approach

Uniform **self-contained `.html` artifact per viz code**, bundled alongside the SVGs in
`algebra-1-tutor/figures/<code>.html`. Viz codes are already cross-collision-checked disjoint
from deterministic SVG codes (`viz_figures.check()`), so each code maps to exactly one file and
resolution ("`.svg` else `.html`") is unambiguous.

### 1. Generator — `_verification/build_viz_artifacts.py`

- Import `viz_figures.VIZ_FIGURES`; for each entry import the module and pull
  `module.samples()[index]["html"]`.
- Wrap in a minimal **self-contained** HTML document:
  - Inlines the **viz CSS subset** the bodies depend on — the `.fig`/`.viz` rules and the
    light/dark color overrides keyed on the literal palette hexes — extracted from
    `build_textbook.CSS` via a single shared constant so it cannot drift. Default to light;
    honor `prefers-color-scheme: dark`.
  - Loads **KaTeX from cdnjs** (the artifact-sanctioned CDN), pinned to the same version the
    textbook uses, with auto-render over the body. Degradation: if a sandbox blocks cdnjs,
    auto-render leaves raw `$$…$$` text and the diagram still renders.
  - Interactive JS is already inline, dependency-free, IIFE-scoped, double-init-guarded — copied
    verbatim.
- Write `algebra-1-tutor/figures/<code>.html` for all 40 codes.
- `build()` / `--check` modes mirroring `build_textbook.py`: `--check` is a byte-deterministic
  compare, verified inside the `cimg/python:3.11` image (string-built HTML is patch-stable).
- An import-time/`--check` consistency assert: every `VIZ_FIGURES` code produces exactly one
  file and every `figures/*.html` corresponds to a registry code (1:1).

### 2. SKILL.md resolution rewrite

Lines ~131 ("Prefer a bundled figure…") and ~240 (figure-code resolution). New recipe:

- Resolve an `f` code by reading `figures/<code>.svg` → emit as an SVG/image Artifact;
  **else** `figures/<code>.html` → emit as an **HTML Artifact** (interactive widgets stay
  live; math is pre-rendered by KaTeX). The geometry/math is pre-verified — don't recompute.
- **Remove** the "may not have been added / I won't invent" dead-end. A code that resolves to a
  bundled file is never denied. Only website-only `T` codes (tutor-guide problems) legitimately
  lack files; keep that single carve-out.

### 3. Packaging — `build_skill.py`

- Add `.html` to `_TEXT_EXT` so the 40 files package into `.skill`/`.zip`.
- Repackage; `--check` (test_skill_zip_current) catches a stale zip.
- Confirm the resulting `.zip` stays within Claude.ai skill size limits (40 small HTML files,
  largest body ~10 KB; expected well under limit — verify).

### 4. Gates (this repo runs a 12+ gate CI)

- **Figure↔file lint:** extend `viz_figures.py --check` (or `check_alignment.figure_lint`) to
  assert 1:1 between `VIZ_FIGURES` and `figures/*.html`, each current (delegates to
  `build_viz_artifacts --check`).
- **smoke_test.py:** every figure code (svg **or** html) resolves to a bundled file.
- **pytest:** new tests for the generator (determinism, self-containment, 1:1, KaTeX cdnjs
  present for math bodies, interactive JS preserved) + the SKILL.md no-refusal contract.
- **.circleci/config.yml:** add a `build_viz_artifacts --check` step.

### 5. Implementation via ultracode Workflow

The generator + CSS subset + gates are authored in the **main loop** (structural, TDD). Then a
**Workflow** fans out one agent per figure to render the bundled artifact headless (Windows Edge
`--screenshot`, **light and dark**, plus an interactive smoke for the 6 JS widgets), read its own
screenshot, and critique fidelity vs. the textbook — feeding CSS-subset fixes back to the main
loop until each figure matches. This is the visual-verification muscle the deterministic
`--check` cannot provide.

## Non-goals

- Re-styling or re-authoring the figures themselves (math is already sympy-verified upstream).
- Bundling raster/illustration images (`docs/assets/*.jpg`) — those are website-only by design.
- Changing the textbook build or the viz registry's numbering.

## Verification / success criteria

- All 40 `figures/<code>.html` exist, self-contained, byte-deterministic in the CI image.
- `build_skill.py --check` green with the 40 files in the `.zip`.
- Full existing gate suite stays green (verify_answers 909/614/0, verify_complementary 269/0,
  notation/alignment/anchor/figure lints, all `--check` builds, smoke_test, pytest).
- Manual: a sampled set of artifacts open standalone and visually match the textbook in light
  and dark; the 6 interactive widgets respond to input; KaTeX renders.
- SKILL.md no longer contains refusal language for resolvable `f` codes.
