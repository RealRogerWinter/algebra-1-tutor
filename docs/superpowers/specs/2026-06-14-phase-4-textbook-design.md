# Phase 4 — HTML textbook — design spec + plan

> **Status:** self-authored 2026-06-14 under the user's blanket autonomy grant (absent user).
> Implements **Phase 4** of `docs/REBUILD_PLAN.md` (4a design + 4b build, combined here for
> velocity). Depends on Phase 1 (content), Phase 2 (reference codes = deep-link targets), Phase 3
> (bundled figures). The textbook is a **generated presentation layer over the unit `.md` prose** —
> never a hand-maintained copy — so the tutor and the textbook can never teach different math
> (handoff §9, REBUILD_PLAN spine).

## 1. Design language (4a, documented)

A clean, single-column reading textbook (max 48rem measure) that reads like a standard text while
exposing the reference-code system:
- **Reference codes are visible, clickable badges** (`#12.5.w2`) that are also `id` deep-link
  targets — every worked example, practice problem, definition, transfer-check, and figure.
- **Figures embed inline** from the Phase-3 bundled SVGs (the exact, sympy-verified art).
- **Math** renders with KaTeX (`$$…$$` display). The textbook is a normal website, so a **pinned
  jsDelivr CDN** is acceptable — the no-fetch constraint applies only to the skill sandbox.
- **Navigation:** an index (table of contents) + one file per unit + prev/next.
- **Theme & print:** light/dark (system + toggle, persisted), print stylesheet, responsive,
  contrast-minded CSS variables (AA-minded; a formal WCAG audit is a noted follow-up).

## 2. Architecture (4b build)

`_verification/build_textbook.py` (build tooling; build dep `markdown==3.7`):
- Reads `curriculum.yaml` (order/titles), each unit `.md`, and `algebra-1-tutor/figures/*.svg`.
- **Pipeline per unit:** protect `$$…$$` → insert deep-link `{#code}` markers after each
  worked-example / practice number (lesson-aware) → convert every `{#code}` to a visible
  `<a class="refcode" id=…>` badge and **embed the bundled SVG** for f-codes → markdown→HTML
  (`extra`, `sane_lists`) → restore `$$…$$` **HTML-escaped** (so `&`/`<` in LaTeX survive to the
  text node KaTeX reads) → wrap in the template.
- Outputs `docs/textbook/{index.html, textbook.css, unit-NN.html, appendix.html}`.
- `--check` verifies the committed site is current (staleness gate, like `generate.py`).

## 3. Plan (one PR: `phase-4/textbook`)

1. Build `build_textbook.py` (renderer + pipeline + `--check`). ✓
2. Generate the site; verify HTML well-formed, one `<h1>`/page, math escaped, deep-link ids for
   d/c/f/w/practice, figures embedded. ✓
3. Tests (`test_textbook.py`): staleness clean, ids present, figure embedded, math escaped.
4. Wire `build_textbook.py --check` into CI (`.circleci/config.yml`).
5. Commit, lean single-subagent review, PR, merge.

## 4. Verification

`build_textbook.py --check` green · existing gate stays green (textbook is additive, under
`docs/`, which is build-only and notation/copyedit-exempt) · `pytest` green · HTML parses · KaTeX
loads from CDN. **Pending human review:** visual/typographic polish and a formal WCAG 2.2 AA audit;
optional follow-ups: Pagefind full-text search and fully self-hosted (offline) KaTeX assets.

## 5. Notes / deferred (flagged for review)

- **Search (Pagefind)** and **offline self-hosted KaTeX** are deferred follow-ups; the current build
  uses the standard pinned CDN and per-page browser find. Structure is search-ready (semantic HTML).
- The textbook lives under `docs/` so it can be served by GitHub Pages (from `/docs`) and is the
  repo's canonical textbook host (handoff §6).
