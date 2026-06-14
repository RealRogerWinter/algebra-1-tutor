# Phase 0 — Foundation: source of truth + alignment guard (design spec)

> **Status:** drafted 2026-06-13 for approval. Implements **Phase 0** of `docs/REBUILD_PLAN.md`
> (the approved 8-phase roadmap; companions `REBUILD_BRIEF.md`, `RESEARCH_REDTEAM_HANDOFF.md` —
> all on branch `docs/rebuild-planning`). Project memory: `algebra-1-tutor-skill`,
> `claude-ai-skill-constraints`. Branch: `phase-0-foundation` off `main`.

## 1. Context & scope

The Algebra 1 tutor skill was red-teamed and benchmarked and found **sound** (0 critical findings,
0 answer-key math errors across 543 sympy-checked answers). This program is **elevation +
new-artifacts + unification**, not repair. Phase 0 builds the **lean data/tooling foundation** that
unblocks every later phase: a single structural source of truth and a CI alignment guard.

**In scope (this phase):** a structural SSOT (`curriculum.yaml`), a generator + checker
(`generate.py`), a CI guard (`check_alignment.py`), the fix for the `5.5.6` verification defect plus
a point-on-line lint, and correction of two stale notation lines. Plus the minimum to make the gates
real CI: a deps file, a CircleCI config, a path fix to the existing notation checker, and build
hygiene.

**Explicitly NOT in scope (later phases, do not start here):** any HTML/textbook work (Phase 4);
any content edits or red-team findings (Phase 1); the reference-code *tagging* of `.md` items
(`d`/`f`/`c`/… — Phase 2); the figure library (Phase 3); promoting Statistics to a core unit
(Phase 1); generating `.md` front-matter or the lesson-level outline (kept as curated prose this
phase). Phase 0 makes **no content edits** to teaching prose.

## 2. Goals / non-goals

**Goals**

1. One structural SSOT (`curriculum.yaml`) describing the **current** structure: 12 units +
   Appendix A, 47 core + 3 optional = 50 lessons.
2. A generator that emits the data-bearing table regions of `curriculum-map.md` and
   `docs/CURRICULUM.md` (idempotent, marker-bounded, `--check` mode) and **checks** the unit `.md`
   titles / lesson IDs / lesson counts against the SSOT.
3. A CI guard composing four checks: alignment, notation invariant, point-on-line lint, code-grammar
   lint.
4. Fix `_verification/unit-05.json` `5.5.6` and add a point-on-line lint that **provably** catches
   its class of error.
5. Correct the two stale notation descriptions (`SKILL.md`, `AUTHOR_GUIDE.md`).
6. Preserve the **765 / 543 / 0** answer-key baseline.

**Non-goals:** changing teaching content; regenerating curated prose; touching the two untracked
Phase 5/7 HTML files; implementing the full reference-code grammar over `.md` (Phase 2).

## 3. `curriculum.yaml` (repo root — build-only, does not ship)

Plain-YAML structural skeleton. Canonical unit/lesson **titles are sourced verbatim from the unit
`.md` headers** (the prose source of truth); `description` and `prerequisites` are unified from the
two existing tables (normalizing the `x^2`→`x²` and capitalization drift). Requires PyYAML
(build-only dep).

```yaml
course: "Algebra 1"
notation:
  # canonical inline style is plain Unicode (see SKILL.md / ARCHITECTURE.md)
  superscript_caret_forbidden: true   # informational; the generator emits Unicode (x², not x^2)
units:
  - id: 1
    slug: foundations
    title: "Foundations & the Language of Algebra"   # == unit-01 .md H1 after "Unit 1: "
    short_title: "Foundations"                        # learner-facing; consumed by later phases
    description: "variables, the equals sign as a balance, the number system & number line, order of operations, negative numbers, expressions vs. equations"
    prerequisites: "Arithmetic only"                  # display text for curriculum-map 'Assumes'
    optional: false
    lessons:
      - { id: "1.1", title: "Variables and the meaning of equations (the equals sign as a balance)" }
      - { id: "1.2", title: "The number system & the number line" }
      # ... one entry per '## Lesson N.M:' header, title == the .md header text verbatim
  # ... units 2–12 ...
  - id: "A"
    slug: statistics
    title: "Data & Statistics"
    short_title: "Statistics"
    description: "one/two-variable statistics, line of best fit, correlation vs. causation, two-way tables"
    prerequisites: "Unit 5 (graphing lines)"
    optional: true
    lessons:
      - { id: "A.1", title: "One-variable statistics — center & spread" }
      - { id: "A.2", title: "Two-variable data, line of best fit, correlation vs. causation" }
      - { id: "A.3", title: "Two-way tables" }
```

Field notes:
- `id` is `1`–`12` for units, the string `"A"` for the appendix.
- `short_title` is included now (the roadmap lists it as part of the SSOT spine) even though no
  Phase-0 surface consumes it yet; later phases (student guide, Progress Card) will.
- `prerequisites` is a free-text display string used only by the `curriculum-map.md` "Assumes"
  column.
- Lesson `title` is the **exact** text after `## Lesson <id>: ` in the unit `.md`. The
  curriculum-map lesson-outline glosses (e.g. 5.3's "(rate of change, rise/run, …)") are *not*
  stored — they stay as curated prose in the outline, which is **linted**, not regenerated.

## 4. `_verification/generate.py`

One module, two responsibilities: **generate** the data tables, and **check** the `.md` structure.

### 4.1 Generated regions (marker-bounded, idempotent)

Two HTML-comment-fenced regions, rewritten in place between their markers:

```
<!-- BEGIN GENERATED: units-at-a-glance -->
… markdown table …
<!-- END GENERATED: units-at-a-glance -->
```

| File | Region id | Columns |
|------|-----------|---------|
| `algebra-1-tutor/references/curriculum-map.md` | `units-at-a-glance` | `# \| Unit \| What it's about \| Assumes (prerequisites)` |
| `docs/CURRICULUM.md` | `units-table` | `# \| Unit \| Focus` |

- The markers are inserted **once** (a one-time edit in this PR) around the two existing tables;
  thereafter the generator only ever replaces text *between* existing markers and **hard-fails with
  a clear message if a marker pair is missing** (never guesses an insertion point).
- Both tables draw the unit title and `description` from the same SSOT fields, so the prior drift
  between "What it's about" and "Focus" collapses to one canonical phrasing. Output uses Unicode
  (`x²`, `f(x)`), fixing `curriculum-map.md`'s `x^2` vs `x²` inconsistency.
- Idempotent: running twice with an unchanged SSOT produces a byte-identical file.

### 4.2 Checks (read-only; no rewrite)

Against the SSOT, verify:
- each unit `.md` H1 matches `# Unit <n>: <title>` (or `# Appendix A: <title>`), title exact;
- every `## Lesson <id>: <title>` header exists in the SSOT with the **same id and title**, and vice
  versa (no missing/extra lessons);
- per-unit lesson **counts** match;
- the `curriculum-map.md` lesson-level **outline** lists exactly the SSOT lesson ids (strict
  set-equality), with per-unit counts matching. Outline lesson *titles* are **not** fuzzy-matched —
  they are curated prose whose wording legitimately differs from the `.md` headers in both directions
  (8.4's `.md` title carries "(two variables)" the outline omits; 5.3's outline carries a gloss the
  `.md` omits), so any containment test would false-positive. The strict title guarantee lives at the
  `.md`-header level (next bullet); the outline is held honest structurally by its id-set + counts;
- every JSON answer-key `id` belongs to a unit/lesson that exists in the SSOT.

### 4.3 CLI

- `python _verification/generate.py` — writes the generated regions.
- `python _verification/generate.py --check` — writes nothing; exits non-zero if any region is stale
  **or** any §4.2 check fails. This is the alignment gate CI invokes (directly and via
  `check_alignment.py`).

## 5. `_verification/check_alignment.py` (the CI guard)

Single umbrella entry point. Runs all four checks, accumulates failures, prints a report, exits
non-zero if any fail. Paths are repo-relative (derived from `__file__`), like `verify_answers.py`.

1. **Alignment** — calls `generate.py`'s check routine (§4.2 + staleness). SSOT ↔ tables ↔ `.md` ↔
   outline ↔ JSON ids.
2. **Notation invariant** — **reuses** `check_notation.py` (see §8), not a re-implementation: no
   inline `\(`, `\)`, `\[`, `\]` or `\macro` outside `$$…$$`/code fences in any shipped
   `algebra-1-tutor/**.md` (SKILL.md excluded — it quotes the forbidden forms deliberately).
3. **Point-on-line lint** (§6) — defense-in-depth, both witnesses.
4. **Code-grammar lint** (§7) — every JSON `id` matches the grammar.

## 6. Point-on-line lint (defense-in-depth: two independent witnesses)

**Problem class.** A `solve` entry can be *internally self-consistent* (its `answer` solves its
`eq`) yet encode the **wrong line** for the stated problem. An "answer solves eq" check is
tautological and cannot catch this — `5.5.6` is the live example. The lint therefore cross-checks
each line-equation entry against **two independent witnesses** that must both agree.

**Trigger.** Any `solve` entry whose `eq` matches the line-intercept template — `<m>*<x0> + b =
<y0>`, `var: "b"` — is a *line-equation entry*. The lint **requires** the geometric annotation on
every such entry (a missing annotation is a lint failure), so the class can never silently skip the
check.

**Annotation (new optional JSON fields, ignored by `verify_answers.py`):**
```json
{"id":"5.5.6","kind":"solve","eq":"3*3+b=7","var":"b","answer":"-2","on_line":[[0,-2],[3,7]]}
{"id":"5.5.1","kind":"solve","eq":"2*3+b=1","var":"b","answer":"-5","on_line":[[3,1]],"slope":2}
```
- `on_line`: list of `[x,y]` points the resulting line **must** pass through (the problem's given
  points).
- `slope`: required only for one-point (point + slope) problems; for two-point problems the slope is
  derived from the points and `slope`, if present, is cross-checked.

**Witness A — geometric (from the JSON).** Build the line from the annotation: with ≥2 points,
derive `m,b` from the points and assert collinearity; with 1 point, use `slope`. Assert (a) every
`on_line` point satisfies `y = m·x + b`, and (b) the derived intercept `b` equals the entry's
`answer`. (sympy, exact rationals.)

**Witness B — `.md` answer-key cross-check.** Independently recover the canonical line from the unit
`.md`:
1. Resolve the **practice** entry to its unit `.md` and lesson; find its `**Answer key:**` block.
   (Worked-example `w`-tagged entries are validated by witness A only — their results sit in
   multi-line `$$…$$` blocks, not a clean numbered answer key.)
2. Split that section into numbered segments (`1.`, `2.`, …) and select the segment matching the
   entry's index.
3. Extract the **last** `y = <expr>` in the segment; sympy-parse `<expr>` as linear in `x` →
   `m_md, b_md`.
4. Assert `m_md == m_json` and `b_md == b_json`.
- If an annotated entry's segment yields **no parseable `y = …`**, the lint **fails loudly** with a
  message naming the id and the segment text (forcing either an explicit answer-key line or a
  documented fix) — the parser is scoped and anchored, never a free-form prose scan.

**Both must pass.** A disagreement between A, B, and the entry is a failure.

**Why this catches `5.5.6`:** the old entry encodes line `y = 3x + 2`. Witness A fails (neither
`(0,-2)` nor `(3,7)` lies on it; derived `b=-2 ≠ 2`). Witness B fails (`.md` answer key #6 says
`y = 3x - 2`). The corrected entry (`y = 3x - 2`, `b=-2`) passes both. A unit test asserts the lint
**rejects** the old entry (regression guard for the class).

**Coverage this phase:** annotate every line-intercept `solve` entry in unit-05 lesson 5.5
(`5.5.w1`, `5.5.w2`, `5.5.1`, `5.5.2`, `5.5.4`, `5.5.6`, `5.5.9`) and any others found by enumerating
the template across all JSON files; the enumerator's output is recorded so coverage is explicit.

## 7. Code-grammar lint

Every answer-key `id` must match the backward-compatible grammar (`RESEARCH_REDTEAM_HANDOFF.md` §5),
restricted to the forms present in the answer-key JSON this phase:

```
standard  : (?:[1-9]|1[0-2]|A) \. \d+ \. (?:w)?\d+ [a-z]?     # 5.5.6, 12.1.w1, A.2.3, 8.2.5b
refresher : ref[AB] \. \d+                                     # refA.4, refB.10
```

- **Format-only.** It does **not** enforce global uniqueness, so the legitimate multi-part repeats
  (e.g. `12.6.w1` appearing for parts a/b/c) are not flagged. (The broader grammar — `d`/`f`/`c`/…
  tags and global banks like `mis.3` — is Phase 2 `.md` work, out of scope here.)
- Implementation enumerates all ids and asserts every one matches; a non-matching id fails with its
  file and value.

## 8. `check_notation.py` refactor (reuse, don't duplicate)

The notation invariant already exists. Phase 0 makes it CI-grade and importable:
- Replace the hardcoded `ROOT = r"C:\Users\18084\algebra\algebra-1-tutor"` with a repo-relative path
  derived from `__file__` (so it runs on CircleCI/Linux).
- Expose a `check(root=None) -> list[issue]` function; keep `__main__` behavior identical.
- `check_alignment.py` imports and runs it for the notation-invariant check. No second
  implementation.

## 9. Fixes & doc corrections

- **`_verification/unit-05.json` `5.5.6`:** `eq: "3*1+b=5"`/`answer: "2"` → `eq: "3*3+b=7"`/
  `answer: "-2"` + `on_line: [[0,-2],[3,7]]`. (Matches `.md` lesson 5.5 practice 5–6: line through
  (0,−2) & (3,7), slope 3, **y = 3x − 2**.) Verifier still passes → baseline unchanged.
- **`algebra-1-tutor/SKILL.md` ~line 115:** drop the stale claim that the reference/lesson files use
  `\( … \)` inline; state the reality (they use the same plain-Unicode-inline / `$$…$$`-display
  convention), modeled on the correct `docs/ARCHITECTURE.md:33`. The forbidden-*output* examples at
  lines 101/106/113 are correct and stay (so SKILL.md remains excluded from the notation scan).
- **`_verification/AUTHOR_GUIDE.md` line 13 (and the `\(f(x)=…\)` example near line 17):** inline
  math is plain Unicode, never `\(…\)`; correct both. Add the `on_line`/`slope` fields to the JSON
  schema documentation (§ "JSON schema for unit-NN.json").

## 10. New build/CI files

- **`requirements.txt`** (repo root or `_verification/`): `sympy`, `PyYAML`, `pytest` — reproducible
  gate environment.
- **`.gitignore`**: `__pycache__/`, `*.pyc`, `.pytest_cache/` only. **Must not** ignore the two
  untracked HTML files (they are tracked in later phases).
- **`.circleci/config.yml`**: a single `gates` job on a `cimg/python:3.11` image —
  `pip install -r requirements.txt`, then run, in order: `verify_answers.py` (expect 0 failures),
  `generate.py --check`, `check_alignment.py`, and `pytest` over the new tests. Any non-zero exit
  fails the build. Runs on every push/PR.

## 11. Testing (TDD)

Tests live in `_verification/tests/` (pytest). Written test-first per component:
- **generate**: idempotency (generate twice → byte-identical); `--check` detects a deliberately
  stale region; a missing marker pair raises a clear error; `.md`/SSOT title/id/count mismatches are
  detected (titles, missing lesson, extra lesson, wrong count).
- **point-on-line**: corrected `5.5.6` passes both witnesses; **the *old* `5.5.6` is rejected**
  (class regression); a fabricated self-consistent-but-wrong entry is rejected; a line-intercept
  entry missing its annotation is rejected; witness B parse-failure raises a clear, identified error.
- **code-grammar**: all current ids pass; samples (`5.5.6`, `12.1.w1`, `A.2.3`, `refA.4`) pass; a
  malformed id (`5.5.`, `13.1.1`, `x.y.z`) fails; multi-part repeats are not flagged.
- **notation**: a temp file with a stray `\(` is flagged; the real tree is clean; SKILL.md is
  excluded.

## 12. Acceptance criteria

1. `python _verification/verify_answers.py` → **765 / 543 / 0** (unchanged).
2. `python _verification/check_alignment.py` → green (all four checks pass).
3. `python _verification/generate.py --check` → green; running `generate.py` twice is a no-op (clean
   git diff the second time).
4. The point-on-line regression test proves the lint **rejects** the pre-fix `5.5.6` and **accepts**
   the fix.
5. `pytest` green; CircleCI `gates` job green.
6. `git diff` touches **no** teaching prose beyond the two stale notation lines and the marker
   insertions; the two HTML files remain untracked and unmodified.

## 13. Deliverables (files)

**New:** `curriculum.yaml`, `_verification/generate.py`, `_verification/check_alignment.py`,
`_verification/tests/` (+ fixtures), `requirements.txt`, `.gitignore`, `.circleci/config.yml`, this
spec, and the implementation plan.
**Changed:** `_verification/unit-05.json` (5.5.6 + `on_line` annotations across 5.5),
`_verification/check_notation.py` (path fix + importable), `algebra-1-tutor/SKILL.md` (line 115),
`_verification/AUTHOR_GUIDE.md` (lines 13/17 + schema doc), `algebra-1-tutor/references/curriculum-map.md`
(+ markers, regenerated tables), `docs/CURRICULUM.md` (+ markers, regenerated table).

## 14. Sequencing & PR

Implemented on `phase-0-foundation` (off `main`), TDD, via an ultracode workflow: build the SSOT +
`generate.py` and `check_alignment.py` (with the four lints) in parallel where independent, then
adversarially verify (idempotency; the lints catch their target classes; baseline preserved). Gates:
`verify_answers.py` (0 failures) + `check_alignment.py` (green) + `pytest` + CircleCI + `/code-review`
on the tooling. PR via `gh` to `RealRogerWinter/algebra-1-tutor`; async review.

## 15. Risks & mitigations

- **`.md` answer-key parser fragility** → scoped & anchored (section + numbered segment + sympy
  parse), hard-fail with identifying message; covered by tests; paired with the geometric witness so
  a parse gap never silently passes.
- **Marker insertion corrupts a table** → markers added once around verified-current tables; `--check`
  + idempotency tests + `/code-review` catch regressions.
- **Hidden title/count drift across materials** (6.3, 8.3, 8.4 noted in research) → surfaced by §4.2
  checks; resolved by aligning the SSOT to the `.md` (prose source of truth), no content edits.
- **Baseline regression** → acceptance criterion #1 + CI gate.
