# Phase 2 — Reference-code system — design spec

> **Status:** approved 2026-06-14; implementing. Implements **Phase 2** of `docs/REBUILD_PLAN.md`
> (the approved 8-phase roadmap; companions `REBUILD_BRIEF.md`, `RESEARCH_REDTEAM_HANDOFF.md` —
> the authoritative grammar is **§5**). Project memory: `algebra-1-tutor-skill`,
> `claude-ai-skill-constraints`. Builds on Phase 0 (the `curriculum.yaml` SSOT + the
> `check_alignment.py` CI gate) and Phase 1 (content elevation), both merged to `main`.

## 1. Context & scope

The reference-code grammar is the **shared addressing vocabulary** across the JSON keys, the skill,
the Phase-4 textbook deep-links, and the Progress Card (REBUILD_PLAN "Architecture spine"). The
design is already resolved in handoff §5; this phase **implements it repo-wide, additively**. The
JSON ids already conform — they are never renumbered. Baseline gate is green today:
`verify_answers.py` → **909 / 614 / 0**; `check_alignment.py`, `generate.py --check`, and `pytest`
(29) all green.

This phase delivers the reference-code **capability** (the grammar made real in the files + a linter
+ a resolution recipe the tutor can follow). It is **not** the resolution *persona / behavior* work
(multimodal, house-voice, the full teaching-loop integration) — that is **Phase 6**.

**In scope (this phase):**
- A repo-wide **inline anchor** convention (`{#code}`) marking every referenceable non-numbered item.
- **Tag the 13 unit `.md` files:** every new-term **definition** (`d`) and every **transfer-check**
  (`c`); **how-to** (`h`) where a lesson states an explicit reusable *method*; **figure** (`f`)
  reserved where *Visuals to offer* names a real figure.
- **Tag the 3 global banks:** `misconceptions.md` → `mis.N`, `visuals.md` → `vis.tN`,
  `metaphors.md` → `met.<slug>`.
- **Extend the build linter** (`check_alignment.py`): the unified code-grammar regex + a new
  `md_anchor_lint()` (grammar + collision + density + SSOT-existence) — **TDD, tests first**.
- A shipped **"Reference codes"** section + resolution recipe in `SKILL.md` (runs through
  `/copyedit`); a **Reference-code anchors** convention note in `AUTHOR_GUIDE.md` (build tooling,
  copyedit-exempt).

**Explicitly NOT in scope (later phases — do not start here):**
- **Authoring figures** — Phase 3. This phase only *reserves* the `f` tag and anchors the spot;
  it draws no figure and ships no SVG. Figure sub-addressing (`f1s.N`, panels) is Phase 3.
- **Tutor-guide complementary problems** and their separate **"T" namespace** — Phase 5. The grammar
  is designed so a future `…​.T7` tier cannot collide (letter-then-digit tag space).
- **HTML textbook** generation — Phase 4 (this phase makes its deep-link targets exist).
- **`SKILL.md` behavior/voice** (multimodal photo protocol, house-voice persona block, the full
  reference-code resolution *behavior* woven into the teaching loop) — Phase 6. This phase adds only
  the self-contained "Reference codes" *capability* section.
- **Renumbering any existing id** — forbidden. The grammar is backward-compatible by construction.

## 2. Goals / non-goals

**Goals**
1. Every referenceable item in the shipped files carries a **collision-free, human-typable** code
   under the §5 grammar, addressable by a student (`#12.5.w2`) and by the Phase-4 textbook generator.
2. The build **enforces** the grammar, no collisions, dense document-order indices, and
   SSOT-existence on every `.md` anchor — additive to the existing JSON-id check, TDD.
3. The tutor has a written **resolution recipe** (parse → load → find → re-verify → echo the
   canonical code).
4. The baseline gate stays green: `verify_answers.py` **0 failures** (totals unchanged at 909/614),
   `check_alignment.py` green (now including `md_anchor_lint`), `generate.py --check` green, `pytest`
   green.
5. The new SKILL.md prose passes `/copyedit` (instructional-tutor target) and the notation invariant.

**Non-goals:** authoring figures (Phase 3); the "T" complementary-problem namespace (Phase 5); the
textbook (Phase 4); any SKILL.md behavior/voice/persona work (Phase 6); a cross-commit code **ledger**
(YAGNI — the dense+unique lint is the practical append-only proxy); renumbering any id.

## 3. The grammar (one unified regex, two scanners)

Replace the restricted `ID_RE` in `check_alignment.py` (today: only `(1-12|A).lesson.[w|ex]idx[part]`
+ `ref[AB].idx`) with the full §5 grammar. **One regex; two scanners** consume it — the existing
JSON-id check (`code_grammar_lint`) and the new `.md` anchor check (`md_anchor_lint`).

| Form | Regex piece (within `^(?: … )\Z`) | Examples |
|---|---|---|
| lesson item (practice / worked / example / **d/c/h/f**) | `(?:[1-9]\|1[0-2]\|A)\.\d+\.(?:w\|ex\|d\|c\|h\|f)?\d+[a-z]?` | `5.5.6`, `8.2.5b`, `12.1.w1`, `6.2.ex1`, `1.1.d1`, `1.1.c1`, `2.2.h1`, `1.2.f1` |
| fraction refresher | `ref[AB]\.\d+` | `refA.4`, `refB.10` |
| misconception section | `mis\.\d+` | `mis.3` |
| visual template | `vis\.t\d+` | `vis.t1` |
| metaphor slug | `met\.[a-z0-9]+(?:-[a-z0-9]+)*` | `met.balance-scale` |

- **Backward-compatible:** the JSON ids (practice/worked/example/refresher) are a strict subset, so
  `code_grammar_lint()` and the existing tests still pass.
- **Collision-free by construction:** numeric scope (`1`–`12`/`A`) vs. letter-prefixed scope
  (`ref`/`mis`/`vis`/`met`); within a lesson, a **letter-then-digit** tag (`w/ex/d/c/h/f`) vs.
  **digit-only** practice. A future Phase-5 `…​.T<digit>` tutor tier and Phase-3 figure sub-forms
  occupy distinct, non-overlapping shapes.
- **Tag meanings:** `w` worked example · `ex` example · (omitted) practice problem · `d`
  definition/new-term · `c` transfer-check · `h` how-to/procedure · `f` figure (reserved this phase).
- **Figures reserved:** only the simple `fN[part]` form is accepted now; richer figure
  sub-addressing is a Phase-3 grammar extension.

## 4. Anchor syntax & placement (locked: `{#code}`)

`{#code}` is the kramdown / Pandoc / markdown-it-attrs explicit-id form: the Phase-4 generator maps
`{#12.5.w2}` → `id="12.5.w2"`, and the URL fragment `#12.5.w2` equals what a student types. It carries
no backslash, so `check_notation.py` (which strips `$$…$$`, fenced, and inline-code spans, then flags
only `\(`,`\)`,`\[`,`\]`,`\macro`) stays clean.

**Placement rules:**
- **Headings** → trailing: `## 3. Negative numbers {#mis.3}`, `## Template 1 — … {#vis.t1}`.
- **List items / bold-led paragraphs** → leading, right after the marker:
  `- {#1.1.d1} **Variable:** …`, and for a metaphor paragraph
  `{#met.balance-scale} **A. The balance scale.** …`.
- **Never anchor** the `# Unit N:` H1 or the `## Lesson N.M:` headers — `generate.py`'s `H1_RE` /
  `LESSON_RE` parse those lines and an anchor would corrupt the captured title. Lessons are already
  addressable as `N.M`.

**What is anchored (density — systematic d+c, opportunistic h/f):**
- **`d`** — every genuinely-new-term bullet in **New terms** (document order: `d1`, `d2`, …).
- **`c`** — every prompt in **Check for understanding (transfer)** (document order).
- **`h`** — only where a lesson presents an explicit, imperative, reusable **multi-step method**
  (typically "To <do X>: 1) … 2) …"); anchor the method's lead line. Many conceptual/early lessons
  have **none** — that is expected and correct.
- **`f`** — only where **Visuals to offer** names a *real* figure (not "none needed"); anchor the
  lead line and append `[figure reserved — Phase 3]`. Authors do **not** draw the figure.

**What is NOT anchored (addressed by visible number):**
- **Worked examples** (`wK`) and **practice problems** (`K`) are already numbered in document order
  (and JSON-keyed). The resolver/textbook address them by that number. **This is the parsing-safety
  guarantee:** every `{#code}` anchor lands in a *New terms / Check / Teaching-arc / Visuals* block —
  none of which the point-on-line lint (`Worked examples:` / `Answer key:`) or `generate.py` parse —
  so no existing lint can be disturbed.

## 5. Global-bank tagging (all three, this phase)

- **`misconceptions.md`** — `{#mis.1}`…`{#mis.8}` trailing the eight `## N. Title` section headings
  (in document order; the existing "§N" cross-references stay as prose).
- **`visuals.md`** — `{#vis.t1}`…`{#vis.t4}` trailing the four `## Template N — …` headings.
- **`metaphors.md`** — leading `{#met.<slug>}` on each lettered entry's bold lead line. Eighteen
  slugs, kebab-case, derived from each entry's name:

  | Concept | Entry | Slug |
  |---|---|---|
  | Equations | A. The balance scale | `met.balance-scale` |
  | Equations | B. Undoing a getting-dressed sequence | `met.getting-dressed` |
  | Negatives | A. Money and debt | `met.money-debt` |
  | Negatives | B. Facing and walking the number line | `met.number-line-walk` |
  | Variables | A. The mystery box / labeled cup | `met.mystery-box` |
  | Variables | B. The reserved seat | `met.reserved-seat` |
  | Functions | A. The vending machine | `met.vending-machine` |
  | Functions | B. The recipe | `met.recipe` |
  | Slope | A. Stairs / a wheelchair ramp | `met.stairs-ramp` |
  | Slope | B. Speed as a rate | `met.speed-rate` |
  | Distributive | A. Handing out flyers | `met.flyers` |
  | Distributive | B. Area of a garden plot | `met.garden-area` |
  | FOIL | A. The area box (2×2) | `met.area-box` |
  | FOIL | B. Two rounds of handing out flyers | `met.two-round-flyers` |
  | Factoring | A. Reverse-distributing / un-baking | `met.reverse-distribute` |
  | Factoring | B. Pulling the common item out of every bag | `met.gcf-bags` |
  | Quadratics-two-solutions | A. Squaring loses the sign | `met.squaring-loses-sign` |
  | Quadratics-two-solutions | B. The parabola crossing the axis twice | `met.parabola-two-roots` |

  `generate.py` does not parse the global banks, so heading/paragraph anchors there are unconstrained
  by the SSOT checks; `check_notation.py` does run on them (and `{#…}` passes).

## 6. The linter extension — `md_anchor_lint()` (TDD, tests first)

A new function in `check_alignment.py`, scanning `{#…}` anchors across all shipped `.md`
(`algebra-1-tutor/**`), wired into `main()` beside the existing four checks. Fails on:

1. **Grammar** — an anchor that does not match the unified `ID_RE`.
2. **Collision** — any code appearing more than once anywhere (global uniqueness).
3. **Density / document order** — within each `(lesson, tag)` group the index set is exactly
   `{1..N}` (no gaps, no dups); likewise `mis.*` is `{1..N}` and `vis.t*` is `{1..N}`. This is the
   practical **append-only proxy**: an accidental renumber produces either a duplicate or a gap, both
   caught here. (Strict cross-commit append-only remains a review check; a code ledger is a non-goal.)
4. **SSOT existence** — every lesson-scoped anchor's `scope.lesson` is a known lesson in
   `curriculum.yaml` (reuse `generate.load_ssot()` ids; `ref*`/`mis*`/`vis*`/`met*` are bank-scoped
   and exempt from the lesson-existence check).

**Tests** (`_verification/tests/test_code_grammar.py`, extended; the umbrella stays green):
- `ID_RE` accepts the new shapes (`1.1.d1`, `1.1.c1`, `2.2.h1`, `1.2.f1`, `mis.3`, `vis.t1`,
  `met.balance-scale`) and still accepts the old (`5.5.6`, `12.1.w1`, `A.2.3`, `refA.4`, `8.2.5b`).
- `ID_RE` rejects malformed (`1.1.d`, `mis.`, `vis.3`, `vis.tx`, `met.Bad_Slug`, `met.`, plus the
  existing `5.5.`, `13.1.1`, `x.y.z`, `5..6`, `ref.4`, `5.5.w`).
- `md_anchor_lint()` on the real tree returns `[]` (after tagging).
- Synthetic-fixture unit tests for the three failure modes (bad grammar, collision, index gap) and
  the SSOT-existence failure, driven against small in-memory/tmp markdown samples.
- A **regression test** asserting `point_on_line_lint()` still returns `[]` with anchors present
  (guards the parsing-safety guarantee from §4).

## 7. SKILL.md + AUTHOR_GUIDE

- **`SKILL.md` — new "Reference codes" section** (shipped prose; runs through `/copyedit`,
  instructional-tutor target). Contents: the grammar in brief (scope.lesson.[tag]index; the tag
  letters; the `mis`/`vis`/`met` banks); and the **resolution recipe** — when a student quotes a code
  (`#12.5.w2`, case-insensitive; spoken fallback "worked example 2 of lesson 12.5"): parse it →
  load the matching unit `.md` or bank → find the item (by its `{#code}` anchor for `d/c/h/f`/bank
  items, or by its number for `wK`/practice) → **re-verify any computation** against the bundled JSON
  and live before showing → **echo the canonical code back** so the student learns it. Placed near
  "Navigating the course"; it is a *capability* description only (no teaching-loop/persona rewiring —
  that is Phase 6).
- **`AUTHOR_GUIDE.md` — "Reference-code anchors" subsection** (build tooling; copyedit/notation
  exempt): the `{#code}` convention and placement rules; the tag letters; the document-order
  assignment + append-only discipline; and the "numbered items (`wK`, practice) need no anchor" rule —
  so future unit authoring stays consistent and the linter stays green.

## 8. PR plan (2 PRs; branches off latest `main`, merged in order)

### PR1 — Foundation: grammar, linter, banks, docs · `phase-2/foundation`
The spec + the implementation plan (`docs/superpowers/`), the unified `ID_RE` + `md_anchor_lint()`
**(TDD: tests first)**, the **3 global banks** tagged (so the linter validates real anchors, not just
fixtures), the `SKILL.md` "Reference codes" section (`/copyedit`-ed), and the `AUTHOR_GUIDE.md`
convention note. Gate green; `/code-review` on the linter change; merge.

### PR2 — Unit-file tagging · `phase-2/unit-tagging`
All **13 unit `.md`** files tagged with `d`/`c`/`h`/`f` anchors, **parallelized per-unit** (an
ultracode workflow: one drafting subagent per unit edits ONLY its own file and self-verifies its
anchors with inline `python -c`; the main loop runs the real gate; an adversarial review subagent
re-checks grammar / collision / density / notation / scope per unit). Gate green; merge.

*(Single-PR is an acceptable alternative since the whole phase is additive; the 2-PR split keeps the
linter logic reviewable on its own and isolates the mechanical bulk tagging under an already-proven
linter.)*

## 9. Approach & invariants (hold on every PR)

- **Gate-green before every PR:** `verify_answers.py` (0 failures; totals stay 909/614 — no answers
  change), `check_alignment.py` (green, incl. `md_anchor_lint`), `generate.py --check` (green),
  `pytest` (green).
- **Additive only:** no lesson added/renamed/removed, no `curriculum.yaml` change, no answer-key
  change → `generate.py --check` and `verify_answers.py` are a safety net, not expected to move.
- **Append-only ids:** anchors are stable references; never renumber. New items get the next trailing
  index in their `(lesson, tag)`. Enforced in practice by the dense+unique lint.
- **Notation invariant:** `{#code}` is plain text (no backslash); shipped `.md` stays Unicode-inline /
  `$$…$$`-display; `check_notation.py` runs on `algebra-1-tutor/**` (SKILL.md excluded).
- **Copyedit gate (R4):** only the new `SKILL.md` prose runs through `/copyedit` (anchors aren't
  prose; `AUTHOR_GUIDE.md` is build tooling, exempt).
- **Clean tree:** `git ls-files --others` before each commit; remove any stray scratch files (the
  Phase-1 mangled-`C:Users…` gotcha — subagents use inline `python -c`, never write scratch files).
  The two root HTML files (Phases 5/7) stay untracked.

## 10. Verification & acceptance

**Per PR (all hold before the PR opens):**
1. `python _verification/verify_answers.py` → **909 / 614 / 0**.
2. `python _verification/check_alignment.py` → green (alignment + notation + point-on-line +
   code-grammar + **md-anchor**).
3. `python _verification/generate.py --check` → green.
4. `python -m pytest _verification/tests` → green (incl. the new grammar/anchor tests).
5. `/copyedit` on the new SKILL.md prose (PR1); `/code-review` on the linter change (PR1).
6. Adversarial review addressed; working tree clean.

**Phase-end:** all 13 units + 3 banks tagged under the grammar; `md_anchor_lint` green on `main`;
the SKILL.md resolution recipe shipped; baseline still 909/614/0; project memory updated (Phase 2
complete, next = Phase 3).

## 11. Risks & mitigations

- **Breaking an existing lint via an anchor** → the §4 placement guarantee (anchors only in
  non-parsed blocks; never on H1/lesson headers) + the §6 regression test that point-on-line stays
  green with anchors present.
- **Notation regression** → `{#code}` carries no backslash; `check_notation.py` in the gate.
- **Collision / accidental renumber** → `md_anchor_lint` global-uniqueness + dense-index checks.
- **Inconsistent `h`/`f` judgment across per-unit taggers** → the crisp §4 rules (`h` only for an
  explicit reusable method; `f` only where a real figure is named) + the adversarial review pass.
- **Subagent scratch-file litter (Phase-1 gotcha)** → inline `python -c` only; `git ls-files
  --others` sweep before commit.
- **Voice drift in the SKILL.md section** → the `/copyedit` gate (R4, instructional-tutor target).

## 12. Deliverables

- This spec + the Phase-2 implementation plan (`docs/superpowers/plans/2026-06-14-phase-2-reference-codes.md`).
- **PR1:** `check_alignment.py` (unified `ID_RE` + `md_anchor_lint`), extended
  `tests/test_code_grammar.py`, tagged `misconceptions.md` / `visuals.md` / `metaphors.md`, the
  `SKILL.md` "Reference codes" section, the `AUTHOR_GUIDE.md` convention note.
- **PR2:** all 13 tagged unit `.md` files (`d`/`c`/`h`/`f` anchors).
- Gate green on `main` after each; baseline preserved at 909/614/0; memory updated.
