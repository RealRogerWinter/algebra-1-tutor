# Phase 6 — Skill behavior + repackage — design spec + plan

> **Status:** self-authored 2026-06-14 under the user's blanket autonomy grant (absent user).
> Implements **Phase 6** of `docs/REBUILD_PLAN.md`. Depends on Phases 1–3 (refs, codes, figures).
> Requirements R3 (multimodal), R4 (house voice). The reference-code resolution recipe and the
> figure-emission instruction already shipped in Phases 2–3; this phase adds the remaining behavior.

## 1. Scope (SKILL.md behavior + the bundled reference pack + repackage)

- **R3 — multimodal photo protocol:** a new SKILL.md section, "Reading the student's work from a
  photo" — **read → render in `$$…$$` → confirm "is this what you wrote?" → only then advise** (an
  extension of verify-before-asserting), plus the edge cases (illegible, multi-problem, rotated).
- **R4 — house voice at runtime:** extend the persona with the explicit anti-AI-tell rules (no
  cliché filler, no "it's not X it's Y", no forced rule-of-threes, no throat-clearing, no em-dash
  pile-ups), matching the `/copyedit` standard the course copy is held to.
- **SOTA pedagogy:** a "Study-skill moves to weave in" section — strategy-choice, spot-the-error
  (proactive misconception use), and self-regulated learning — plus a **Progress-Card "Due for
  review"** line so spacing/interleaving survives statelessness (feeds from the tutor-guide
  mixed-review sets).
- **Bundled reference pack:** `references/sources.md` — a vetted, authoritative source per unit
  (mostly OpenStax, with licenses) + the pedagogy evidence; links are **printed for the human**, the
  model never fetches (platform reality). A SKILL.md pointer in "Reference files".
- **Repackage:** rebuild `algebra-1-tutor.skill` + `.zip` (the committed installable) so the bundle
  includes the Phase-3 figures, the reference pack, and the updated SKILL.md.

**Out of scope:** the student guide (Phase 7); any content/answer changes (none here).

## 2. Architecture

- `_verification/build_skill.py` — packages everything under `algebra-1-tutor/` into `.skill` + `.zip`
  (deterministic entries). `--check` compares the committed `.zip` to the source folder **file-for-
  file by content** (not zip-container bytes), so it's stable across OS/zlib and catches a stale zip.
- SKILL.md is excluded from `check_notation`/`md_anchor_lint` by design; `sources.md` is a normal
  shipped reference (notation-clean, plain links).

## 3. Plan (one PR: `phase-6/skill-behavior`)

1. SKILL.md: persona house-voice rules; the photo-protocol section; the study-skill-moves section;
   the Progress-Card "Due for review" line; the `sources.md` pointer. (Authored to the `/copyedit`
   standard — R4.) ✓
2. `references/sources.md` reference pack. ✓
3. `build_skill.py` + test + CI step; rebuild the `.zip`. ✓
4. Full gate + lean review + PR.

## 4. Verification

10-check gate green incl. `build_skill.py --check`; `check_notation` clean on `sources.md`; the
rebuilt `.zip` contains SKILL.md + 13 unit files + 12 figures + the reference pack (32 files); 58
pytest. **Pending human review:** a read-through of the new SKILL.md behavior in a live session
(the photo protocol and study-skill moves are instructions, exercised by the model at runtime).
