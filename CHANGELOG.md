# Changelog

Notable changes to the project. The course is generated from one source of truth and verified by CI; see [CONTRIBUTING.md](CONTRIBUTING.md).

## [Unreleased]

### Added
- Split licensing: MIT for code, CC BY-NC 4.0 for course content, CC0 for the AI-generated images (`LICENSE`, `LICENSE-CONTENT`, `docs/assets/README.md`).
- Open-source community files: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, and GitHub issue and pull-request templates.

### Changed
- Rewrote `README.md` around the two ways to use the course (read the textbook online; install the tutor skill), corrected the unit and problem counts, and clarified that the skill works on the free plan.
- Refreshed `docs/ARCHITECTURE.md` and `docs/DEVELOPMENT.md` to cover the full generate-and-verify pipeline.

### Removed
- Internal planning and research documents that aren't part of the shipped product, plus two obsolete one-shot scripts. De-personalized absolute paths in the remaining tooling.

## 2026-06-15
- Textbook: per-question answer reveal; fraction-refresher lesson and badges; reveal-glyph fix.
- Brought the student guide, tutor guide, and landing page onto the shared textbook design.
- Image pipeline: 22 deterministic figures plus per-lesson hero and inline illustrations; deployed to GitHub Pages.

## 2026-06-14
- College-quality rebuild, in phases: `curriculum.yaml` as the single source of truth; content elevation across all units; the reference-code system; the computed figure library; the HTML textbook; the tutor guide with 269 complementary problems; and the student guide.
- Student-facing textbook overhaul and reader-reported copy fixes.

## Earlier
- Initial Algebra 1 Tutor Agent Skill, with Claude.ai notation fixes (`$$` blocks plus Unicode inline).
