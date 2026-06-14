# Phase 7 — Student guide refresh + final integration — design spec + plan

> **Status:** self-authored 2026-06-14 under the user's blanket autonomy grant (absent user).
> Implements **Phase 7** (final) of `docs/REBUILD_PLAN.md`. Depends on most prior phases.

## 1. Scope

- **Student guide** regenerated from the SSOT: a learner-facing **roadmap** (a motivating map, not a
  textbook) — how to use the tutor + Progress Card, the reference-code primer, and the unit roadmap
  with links into the generated textbook.
- **Final integration:** confirm the four materials (skill, textbook, tutor guide, student guide)
  are aligned and that reference codes resolve **across** materials.
- **Smoke tests:** the automatable analog of the live end-to-end tests (new-learner / topic-jump /
  wrong-answer / photo / code-lookup / figure-render).
- **Final packaging:** the `.zip` is deterministic (LF-normalized) so it never churns.

## 2. Architecture

- `_verification/build_student_guide.py` → `docs/student-guide/index.html` (+ shared `textbook.css`)
  from `curriculum.yaml`. `--check` staleness gate.
- `_verification/smoke_test.py` — cross-material integration: every unit has a textbook page, a
  tutor-guide page, and a complementary set; every bundled figure is embedded in its textbook page;
  reference-code spot-checks resolve (a definition, a worked example, a figure, a complementary
  problem, a misconception, a bundled SVG); the student guide links the textbook.
- `build_skill.py` now LF-normalizes shipped text into the package, so the committed `.zip` is
  deterministic across OS/zlib (the `--check` compares decompressed content, which is platform-stable).

## 3. Plan (one PR: `phase-7/student-guide-integration`)

1. `build_student_guide.py` + generate `docs/student-guide/`. ✓
2. `smoke_test.py` + `test_integration.py`; wire `build_student_guide --check` + `smoke_test` into CI. ✓
3. `build_skill.py` LF-normalization (deterministic package). ✓
4. Full gate + lean review + PR + merge.
5. **Repo housekeeping:** prune merged phase branches; confirm the working tree is clean (only the two
   legacy root HTML files remain untracked, superseded by the generated `docs/` versions).

## 4. Verification

The full 12-check gate green: `verify_answers` (909/614/0), `verify_complementary` (269/0),
`check_notation`, `check_alignment` (alignment+notation+point-on-line+code-grammar+md-anchor+figure),
`generate/figures/build_textbook/build_tutor_guide/build_skill/build_student_guide --check`, and
`smoke_test`. 60 pytest. **Pending human review (the genuinely manual part):** a live Claude.ai
session running the behavioral smoke tests — new learner, topic jump, wrong-answer diagnosis, photo
upload, code lookup, figure render — and visual/typographic sign-off on the textbook, figures, and
guides.

## 5. End state

`curriculum.yaml` is the single source of truth; from it (and the prose unit files) the skill,
textbook, tutor guide, and student guide are generated/aligned and **held correct by sympy + a 12-gate
CI**. Every problem, worked example, definition, figure, and misconception is addressable by a
human-typable reference code that resolves across all materials. The skill `.zip` bundles the prose,
the figures, and the reference pack, and is re-uploadable.
