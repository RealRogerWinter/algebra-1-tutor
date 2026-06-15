# Architecture

This repository ships two things from one source of truth:

1. an **Agent Skill** — the Algebra 1 tutor for the Claude.ai app, packaged as `algebra-1-tutor.zip`; and
2. a **generated website** (GitHub Pages) — an HTML textbook, a student guide, a tutor guide, and a landing page.

A CircleCI gate makes the two structurally impossible to silently desync: everything is generated from `curriculum.yaml` and the lesson sources, and every generated file is rebuilt and byte-compared on each push.

## Data flow

```
SOURCES (hand-written)               GENERATORS (_verification/)         OUTPUTS
──────────────────────               ──────────────────────────         ───────
curriculum.yaml ───────────┐
  units, lessons, prereqs  ├─► generate.py ───────────► curriculum-map.md, docs/CURRICULUM.md tables
                           │
algebra-1-tutor/           ├─► build_skill.py ─────────► algebra-1-tutor.zip   (the skill)
  references/units/*.md    │
  + SKILL.md, banks        │
                           │
textbook-src/*.md ─────────┼─► build_textbook.py ──────► docs/textbook/
  (student prose)          │   build_student_guide.py ─► docs/student-guide/
                           │   build_tutor_guide.py ───► docs/tutor-guide/
_verification/             │   build_landing.py ───────► docs/index.html
  unit-*.json (answers)    │   (build_all.py runs all four together)
  complementary/*.json     │
  figures.py ──────────────┴─► algebra-1-tutor/figures/*.svg ─► embedded in the textbook & skill
```

Each generator has a `--check` mode that rebuilds in memory and byte-compares against the committed output, so a stale generated file fails CI.

## Source layers

- **`curriculum.yaml`** — the structural source of truth: units, lessons, ids, titles, prerequisites. Everything else derives its skeleton from here.
- **Tutor prose** (`algebra-1-tutor/references/units/*.md`) — what the *skill* reads, written as guidance for the AI tutor. Alongside it: the cross-cutting banks (`misconceptions`, `metaphors`, `visuals`, `pedagogy`, `curriculum-map`, `sources`) and `SKILL.md`, the operating manual.
- **Student prose** (`textbook-src/*.md`) — a warm rewrite of each lesson for a human reader; the *textbook* builds from this. The math, answers, and reference codes must match the tutor source; only the prose differs (guarded by `check_textbook_src.py`).
- **Answer data** (`_verification/unit-*.json`, `appendix.json`) — every computational problem as machine-checkable data. `complementary/*.json` holds the tutor guide's separate "T" practice tier.
- **Figures** (`figures.py`) — coordinate specs rendered to accuracy-checked SVGs under `algebra-1-tutor/figures/`, embedded in the textbook and re-emitted by the skill.

## Correctness: defense in depth

The product's core promise is *never teach wrong math*, so correctness is enforced in layers:

- `verify_answers.py` / `verify_complementary.py` re-derive every stored answer with `sympy`.
- `check_alignment.py` composes six lints: SSOT ↔ (.md / JSON / outline) alignment, notation (no inline LaTeX leaks), point-on-line (an independent geometric witness plus a `.md` cross-check for line problems), reference-code grammar, anchor density and uniqueness, and figure accuracy.
- `check_textbook_src.py` is the one backstop that the student copy kept the same math, answers, and codes as the verified tutor source (and leaked no tutor-only meta).
- `figures.py --check` re-verifies each SVG against its spec.
- `smoke_test.py` proves reference codes resolve across all four surfaces.
- The skill itself is also told to re-derive and re-verify live, trusting live verification over any stored value if the two ever disagree.

## The five behavioral pillars (in SKILL.md)

1. **Never teach wrong math.** Verify every nontrivial result by substitution or the code sandbox *before* asserting it's right or wrong; on a disagreement, re-derive and assume the student may be right. This is the highest-priority rule — a confidently mis-graded correct answer is the worst failure for a tutor a beginner can't double-check.
2. **Ask before telling**, via a graduated hint ladder (diagnose → targeted hint → parallel worked example → co-solve → full solution + fresh practice) that still honors an explicit "just tell me."
3. **Diagnose the misconception**, don't just mark the answer wrong; switch representation rather than repeating the same explanation.
4. **Concrete → pictorial → symbolic** introductions with backward-faded worked examples; check understanding by transfer.
5. **Plain, honest tone** — patient and never harsh, but matter-of-fact, no gushing, no emoji or decorative marks.

## Notation and visuals (platform-shaped)

- **Notation.** On Claude.ai only `$$…$$` display LaTeX renders dependably; inline `\(…\)` and single-`$…$` frequently show as raw, unrendered text. So the skill puts all real notation in `$$…$$` blocks and writes inline math as plain Unicode (x², √12, ½, ±, ≤). The reference and unit files are authored the same way so the model isn't tempted to mimic inline LaTeX.
- **Graphs are Artifacts.** There is no image generator on Claude.ai, and raw SVG in a chat message doesn't render. Graphs are emitted as SVG/HTML artifacts with **computed** coordinates (never freehanded), labeled axes, intercepts, and vertex, and a companion point table. The 22 bundled figures under `algebra-1-tutor/figures/` are pre-rendered and accuracy-checked, so the tutor re-emits a known-correct SVG rather than recomputing one. Recipes and the coordinate-mapping rule live in `visuals.md`.

## Statelessness → the Progress Card

Claude conversations don't share memory by default, so a linear course needs a resume mechanism. At a stopping point the tutor emits a short, human-readable **Progress Card** (current lesson, what's mastered, what to watch, last problem, next step, and a "due for review" line for spacing). The student pastes it back next time. The skill itself holds no per-student state.

## Reference codes

Every worked example, practice problem, definition, and figure has a short, stable code (for example `12.5.w2` is worked example 2 in Lesson 12.5; `1.2.f1` is a figure; `1.1.d3` is a definition). The codes serve three roles at once: deep links in the textbook, click-to-copy tutor prompts, and stable handles the skill re-resolves. The grammar and the append-only rule are documented in [CONTRIBUTING.md](../CONTRIBUTING.md) → "Reference codes".

## What ships vs. what doesn't

- **Ships** (packaged into the `.zip`): everything under `algebra-1-tutor/` — `SKILL.md`, the reference banks and unit lessons, and the bundled figure SVGs.
- **Does not ship**: `_verification/` (the build tooling, the sympy checkers, the JSON answer data, the author guide), `textbook-src/`, and `docs/` (the website).
