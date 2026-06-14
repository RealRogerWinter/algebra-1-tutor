# Phase 5 — Tutor guide + complementary problem sets (R1) — design spec + plan

> **Status:** self-authored 2026-06-14 under the user's blanket autonomy grant (absent user).
> Implements **Phase 5** of `docs/REBUILD_PLAN.md` + requirement **R1** (`REBUILD_BRIEF.md`).
> Depends on Phase 1 (content) and Phase 2 (codes; the **T** tier was reserved by design).

## 1. Scope

The tutor needs *fresh* problems to hand a student who has already worked the textbook practice
(hint-ladder rung 5; transfer checks). So author **complementary problem sets**: new, original,
**parallel-form** problems (same skill, different numbers/contexts), in a **separate namespace** so
codes never collide with textbook codes, **sympy-verified**, with **full worked solutions**, plus a
per-unit **mixed-review** set for interleaving (the biggest learning lever, handoff §4).

**T-tier grammar (separate namespace):**
- per-lesson: `scope.lesson.T<n>` — e.g. `5.4.T1`, `12.3.T7`
- unit mixed-review: `scope.R.T<n>` — e.g. `5.R.T1`

**Shape (R1 defaults):** ~4 per lesson (increasing difficulty + a light stretch) + ~5 mixed-review
per unit; tutor-facing → **full worked solutions**, not just answers.

## 2. Architecture

- **Datastore:** `_verification/complementary/<unit>.json` (one per unit + `appendix.json`). Each
  problem: an auto-checkable core (`kind` + `eq`/`expr`/`var`/`answer`, same kinds as the textbook
  keys) **plus** `prompt` (statement) and `solution` (worked solution). Notation: Unicode inline,
  `$$…$$` display.
- **`_verification/verify_complementary.py`** (gate): reuses `verify_answers.CHECKERS` to re-derive
  every answer with sympy; validates the T-grammar (`TID_RE`), global uniqueness, SSOT lesson/unit
  existence, and the presence of `prompt`/`solution`. Vacuously green on an empty set.
- **`_verification/build_tutor_guide.py`** (generator): `docs/tutor-guide/` HTML — per-lesson sets +
  per-unit mixed-review; each problem shows its reference code, prompt, and a collapsible worked
  solution; **CSS/KaTeX shared with the textbook**. `--check` staleness gate.

## 3. Plan (one PR: `phase-5/tutor-guide`)

1. `verify_complementary.py` (grammar + sympy + well-formedness). ✓
2. Author the T-tier datastore via a **per-unit ultracode workflow** — one agent per unit authors
   ~4/lesson + ~5 mixed-review, **sympy-verifies every answer inline**, writes its
   `complementary/<unit>.json` (bulk content to disk, not the orchestrator's context).
3. `build_tutor_guide.py` generates `docs/tutor-guide/`. ✓
4. Wire `verify_complementary.py` + `build_tutor_guide.py --check` into CI.
5. Main-loop re-verify (sympy) + lean single-subagent review (spot-check problem quality / parallel-
   form / solutions) + fix + PR.

## 4. Verification

`verify_complementary.py` 0 failures · `build_tutor_guide.py --check` green · the existing gate stays
green (additive; `docs/**` build-only) · `pytest`. Every complementary answer is sympy-checked, same
rigor as the textbook keys. **Pending human review:** pedagogical quality/voice of the new problem
prose (a `/copyedit` pass on the prompts/solutions is a noted follow-up — the authoring used the house
notation rules; a full copyedit of ~270 prompts is deferred).
