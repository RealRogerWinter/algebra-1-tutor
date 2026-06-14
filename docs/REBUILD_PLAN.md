# Algebra 1 Course — Overarching End-to-End Rebuild Plan

> **Status:** approved 2026-06-13 (durable copy of the plan-mode roadmap). Companions:
> `REBUILD_BRIEF.md` (requirements R1–R4), `RESEARCH_REDTEAM_HANDOFF.md` (findings + vetted
> sources). Per-phase specs will live in `docs/superpowers/specs/`.

## Context

The Algebra 1 tutor (an Agent Skill for Claude.ai) was red-teamed and benchmarked by a
64-agent research pass (see `RESEARCH_REDTEAM_HANDOFF.md`). Verdict: the course is **sound** —
0 critical findings, 0 answer-key math errors across 543 sympy-checked answers — so this is an
**elevation + new-artifacts + unification** program, not a repair. The goal is a unified,
college-quality course: the skill + reference files, a **rich HTML textbook with a
reference-code system**, an aligned **student guide** and **tutor guide** (the latter gaining
**complementary problem sets**), a **bundled figure library** and **reference pack**, all driven
from a **single source of truth** and held correct by sympy + CI gates. Requirements R1–R4 are
in `REBUILD_BRIEF.md`.

This document is the **program roadmap**. Each phase gets its **own session**: a detailed spec
(`docs/superpowers/specs/`) + implementation plan, then autonomous implementation. The
fine-grained design of each phase is deliberately out of scope here.

## End state (what "done" looks like)

- One `curriculum.yaml` **source of truth** generates every material's structural skeleton; the
  unit `.md` files remain the **prose source of truth**; the **HTML textbook is generated from
  them** — so the tutor and the textbook can never teach different math.
- Every problem, worked example, definition, figure, and misconception is addressable by a
  **human-typable reference code** (`12.5.w2`, `12.1.d3`, `12.6.f1`) the student can quote to the
  tutor; the tutor resolves it, re-verifies, and shows it.
- College-level rigor throughout (definitions, completeness, the SOTA-pedagogy upgrades), **held
  inside Algebra-1 scope** (the one scope-creep item, 8.3 absolute-value *solving*, rescoped).
- Figures are **pre-generated programmatically, reviewed, and bundled** into the skill (rendered
  in-chat as inline-SVG artifacts) and embedded in the textbook.
- The tutor reads **photos of student work** (confirm-before-advising) and obeys the **house
  voice**; all generated copy passed `/copyedit`.
- Four materials (skill+refs, textbook, student guide, tutor guide) are **aligned by
  construction**, enforced by a CI guard.

## Architecture spine

- **`curriculum.yaml` (root)** = structural skeleton (units, lessons, canonical + short titles,
  prerequisites). A Python generator emits the data-bearing regions of the markdown docs and,
  later, every presentation surface (tutor guide, student guide, textbook).
- **Unit `.md` files** = the prose/teaching source of truth (what the skill loads). The textbook
  is a **generated presentation layer** over them — never a fifth hand-maintained copy.
- **Reference-code grammar** (`scope.lesson.[type-tag]index`) is the shared addressing vocabulary
  across the JSON keys, the skill, the textbook deep-links, and the Progress Card. Tutor-guide
  complementary problems use a **separate namespace** (a "T" tier) so codes never collide.
- **Bundling, not fetching** (platform reality): figures (inline SVG) and the reference pack ship
  *inside* the skill `.zip`; the public GitHub repo is the source of truth + textbook host.

## Execution model (cadence: spec-gated, then autonomous)

For each phase, in its own session:
1. **Brainstorm → spec** (`docs/superpowers/specs/YYYY-MM-DD-<phase>-design.md`) **→ implementation
   plan**, presented for approval.
2. On approval, I **implement autonomously** and open **PR(s)** for that phase; review is **async**.
3. Implementation is safe to run unattended because every change passes the gates below before a
   PR is opened.

**Gates on every content/code PR (the safety net for autonomy):**
- `verify_answers.py` — sympy re-checks every computational answer (must be 0 failures).
- `check_alignment.py` — SSOT ↔ materials ↔ JSON alignment, notation invariant, code-grammar
  lint, point-on-line lint (built in Phase 0).
- `/copyedit` — on all newly generated course **prose** (instructional-tutor voice target).
- `/code-review` — on tooling/generator/build code.

## The phases

> Phase 0 is designed and approved (the lean SSOT foundation). The rest are described at roadmap
> altitude; each is detailed in its own session.

### Phase 0 — Foundation: source of truth + alignment guard *(approved)*
- **Deliverables:** `curriculum.yaml`; `_verification/generate.py` (generates the
  `curriculum-map.md` + `docs/CURRICULUM.md` data tables; *checks* unit `.md` titles/IDs/counts);
  `_verification/check_alignment.py` (CI guard); fix the `unit-05.json` **5.5.6** defect + add the
  point-on-line lint; correct the stale notation lines in `SKILL.md` and `AUTHOR_GUIDE.md`.
- **Depends:** nothing. **Unblocks:** everything. **Skills:** tooling only.

### Phase 1 — Content elevation (per unit; **Statistics now a core unit**)
- Apply the confirmed red-team findings unit by unit (majors first): irrational/real + absolute
  value as distance (U1), no-solution/identity (U2), function-as-correspondence + discrete/
  continuous domain (U4), x-intercept/standard form + interpret-in-context (U5), exponential/
  sequence precision (U9), prime trinomials + factor-over-integers (U11), square-root property
  (U12), and the **promoted Statistics unit** (linearity-before-fit, two-way-table association,
  the genuinely-Algebra-1 regression/correlation layer). **Rescope 8.3** to the V-shape graph +
  `|x|=k` distance (defer full solving). Add the **SOTA-pedagogy** elements (strategy-choice,
  spot-the-error study items, interpret-in-context). **Document** the two remaining intentional
  departures (rational expressions omitted; proportional reasoning as a labeled bridge).
- **Phase-1 decisions to settle:** Statistics unit's final number/placement (keep IDs
  **append-only** — likely a new trailing unit rather than a mid-sequence insert) and the 8.3
  rescope depth.
- **Depends:** Phase 0. **Parallelizable per unit.** **Skills:** content authoring, skill-creator
  (reference files), `/copyedit`, verify.

### Phase 2 — Reference-code system
- Implement the (already-designed) grammar repo-wide: tag the non-problem items in the unit `.md`
  (`d`/`f`/`c`/…), add the linter to the build, and add a **"Reference codes"** section +
  resolution recipe to `SKILL.md`. Existing JSON IDs already conform — additive only.
- **Depends:** Phase 0. **Enables:** textbook deep-linking, tutor code lookup. **Skills:**
  skill-creator, tooling.

### Phase 3 — Figure library
- Author **figure specs** → render **programmatically** (matplotlib/computed SVG) → **accuracy
  check** (sympy) + **visual review** → store versioned in the repo and **bundle the SVGs into the
  skill**; assign `FIG` codes; replace the runtime-eyeballed-artifact instructions.
- **Depends:** Phase 1 (which figures), Phase 2 (figure codes). **Skills:** tooling, verify,
  visual review. *(Not generative-AI image creation — accuracy requirement.)*

### Phase 4 — HTML textbook *(split; design starts early in parallel)*
- **4a — Design workshop (early parallel track):** with `/frontend-design` + the visual companion,
  workshop and **red-team a new visual design language** that maximizes the HTML format and works
  as **learning guide + textbook + reference** while reading like a standard textbook. Output: an
  approved **design spec + clickable prototype**. **Depends only on Phase 0 + the code-grammar
  spec** (already designed), so it runs alongside Phases 1–3.
- **4b — Build:** generate the textbook from the unit `.md` + SSOT per the 4a design — KaTeX
  pre-render + MathML, one file per unit, WCAG 2.2 AA (reflow/contrast/resize), deep-linking by
  reference code, embedded reviewed SVGs, offline self-hosted assets, search (Pagefind), dark +
  print. **Depends:** 1 (content), 2 (codes), 3 (figures), 4a (design).

### Phase 5 — Tutor guide + complementary problem sets (R1)
- Author **complementary problem sets** (separate "T" namespace, **sympy-verified**, full worked
  solutions; per-lesson + a unit-level **mixed-review** set for interleaving). Regenerate the
  tutor-guide HTML (**look preserved**, data from SSOT) with new problem-set pages.
- **Depends:** Phase 1 (content), Phase 2 (codes). **Skills:** content authoring, verify,
  frontend-design (problem-set pages within the existing design), `/copyedit`.

### Phase 6 — Skill behavior + repackage
- `SKILL.md` updates: **multimodal photo protocol** (R3: detect → render → confirm → advise),
  **reference-code resolution**, **house-voice rules** (R4), the SOTA-pedagogy moves
  (strategy-choice / spot-the-error / light SRL + a Progress-Card "due for review" list),
  figure-as-artifact emission, and the **bundled reference pack**. **Repackage + re-verify** the
  `.zip`.
- **Depends:** Phases 1–3 (refs, codes, figures bundle). **Skills:** skill-creator, packaging,
  verify.

### Phase 7 — Student guide refresh + final integration
- **Redesign** the student guide (`/frontend-design`) generated from the SSOT; bring **all four
  materials to green** on the alignment CI; run **end-to-end smoke tests** (new learner, topic
  jump, wrong-answer diagnosis, photo upload, code lookup, figure render); final packaging.
- **Depends:** most prior phases. **Skills:** frontend-design, tooling, verify.

## Sequencing & dependency graph

```
Phase 0 (foundation)
        │
        ├──────────────► Track A (content):   Phase 1 ─────────────┐
        │                                                          │
        ├──────────────► Track B (systems):   Phase 2 ─► Phase 3 ──┤
        │                                          │               │
        └──────────────► Track C (design):    Phase 4a (textbook design) ─┐
                                                                   │       │
                                          ┌────────────────────────┘       │
                                          ▼                                 ▼
                              Phase 5 (tutor guide+R1)            Phase 4b (textbook build)
                              [needs 1,2]                          [needs 1,2,3,4a]
                                          ▼
                              Phase 6 (skill behavior) [needs 1,2,3]
                                          ▼
                              Phase 7 (student guide + final integration) [needs most]
```

- After Phase 0, three tracks run in parallel: **content** (1), **systems** (2→3), **design**
  (4a). They converge into the build/integration phases (4b, 5, 6, 7).
- Within Phase 1, units parallelize.

## PR strategy

- Branch per phase (and per unit within Phase 1) off `main`; open a PR per logical unit of work;
  the gates above must pass before a PR is opened; review is async, then merge.
- The repo is a real git repo on `main` (the two HTML files are still untracked — folded into
  Phase 0/7 housekeeping). Confirm remote/PR host at Phase 0; if no remote, use local review
  branches.

## Program-level decisions (settled)

1. **Cadence:** spec-gated, then autonomous implementation + async PR review.
2. **Statistics:** promoted to a **core unit** (CCSS-aligned); full elevation in Phase 1;
   append-only numbering preserved.
3. **Licensing:** **free / non-commercial** — author original copy and link/cite; may **excerpt
   OpenStax/Khan (CC BY-NC-SA) into the bundled reference pack with attribution + ShareAlike**;
   the skill remains non-commercial.
4. **Textbook:** **early parallel design track** (4a after Phase 0); build (4b) after its inputs.

*Deferred to each phase's own session:* the Statistics unit's exact number/placement and 8.3
rescope depth (Phase 1); the complementary-set difficulty band (Phase 5); the textbook design
language specifics (Phase 4a).

## Risks & mitigations

- **Material desync** → the SSOT + `check_alignment.py` CI guard make it structurally impossible.
- **Teaching wrong math** → sympy verification on every change + the tutor's live verify rule;
  figures generated programmatically and reviewed (no eyeballing, no diffusion-AI).
- **Scope creep** → the documented Algebra-1 boundary + "not in this course" ceiling; 8.3 rescoped.
- **Platform surprises** (fetch/display/render) → already resolved by research; bundle-not-fetch.
- **Cross-session continuity** → the `docs/` trio (BRIEF, HANDOFF, this PLAN) + project memory;
  per-phase specs in `docs/superpowers/specs/`.

## Verification (how we know the program is succeeding)

- Per PR: `verify_answers.py` (0 failures), `check_alignment.py` (green), `/copyedit` on new prose,
  `/code-review` on tooling.
- Per presentation phase: render checks (textbook builds, figures render in-chat as artifacts,
  WCAG AA spot-checks).
- Final (Phase 7): the end-to-end smoke-test set above, and a clean repackaged, re-uploadable
  skill `.zip`.

## Status & next action

Phase 0 is designed and approved. **Next session begins Phase 0**: its spec + implementation plan,
then autonomous implementation behind the gates.
