# Per-question answer reveal — design

- **Date:** 2026-06-14
- **Status:** Approved (brainstorming) → ready for implementation plan
- **Branch / worktree:** `per-question-answers`
- **Surface:** the student-facing HTML textbook (`docs/textbook/`), built by `_verification/build_textbook.py`

## Problem

In the student textbook, every lesson's practice problems are followed by a single
collapsible **Answer key** box (`<details class="answers">`, "Try each one yourself first,
then open to check"). A student who wants to check problem 3 has to open the whole key and
see all 25 answers at once — which spoils the rest and makes one-at-a-time self-checking hard.

We want each problem to carry **its own** revealable answer, right next to the question, so a
student can check their work one problem at a time.

## Surface topology (what changes, what does not)

There are three generated sites. Practice-with-answers content lives in only one:

| Site | Built by | Has practice + answer key? | Change? |
|------|----------|----------------------------|---------|
| `docs/textbook/` | `build_textbook.py` (`md_to_body(..., launcher=True)`) | **Yes** — `**Practice problems:**` + `**Answer key:**` from `textbook-src/unit-*.md` | **Yes — this is the target** |
| `docs/student-guide/` | `build_student_guide.py` | No — a roadmap / how-to-use page | No |
| `docs/tutor-guide/` | `build_tutor_guide.py` | Per-problem worked solutions already, via its own `_problem_html` path (also `<details class="answers">`) | No |

The CSS string (`build_textbook.CSS`) is shared and written to every site's `textbook.css`.
The tutor guide reuses `.answers` for its per-problem "Worked solution" boxes, so **we must not
restyle or repurpose `.answers`** — the new per-question reveal gets its own class.

## Goals

1. In the textbook, render each practice problem on its own row with an individual, native
   reveal control that shows only that problem's answer.
2. Remove the single end-of-lesson answer box for any set converted to per-question reveals.
3. Never mangle content: any set we cannot confidently pair keeps today's single box.
4. No JavaScript, no new dependencies, keyboard-accessible, print-friendly, byte-deterministic.

## Non-goals

- No change to `textbook-src/*.md` (the SSOT). The math verifier (`verify_answers.py`,
  `check_textbook_src.py`) and reference codes stay valid.
- No change to reference-code assignment behavior (`_id_worked_practice`), the tutor launcher,
  the tutor guide, or the student-guide roadmap.
- No "reveal all" control (decided: purely per-question).
- No restyle of the existing `.answers` component (still used as the fallback and by the tutor guide).

## Approach

**Build-only transform with confident-pairing + graceful fallback.** All logic lives in
`build_textbook.py`. The transform is lesson-aware (and `md_to_body` already receives one lesson
chunk at a time):

1. **Build an answer map.** Scan the chunk for every `**Answer key…:**` block. Parse entries
   delimited by `N)` (primary) or `N.` (fallback delimiter, e.g. unit-01's `13. -4 14. 4 …`),
   spanning continuation lines, into `{int → answer_markdown}`. Strip any trailing italic note on
   the label line (e.g. `**Answer key:** *(percents reported with their % sign…)*`).
2. **Split each practice set into problems.** Within a `**Practice problems…:**` block, split on
   leading problem numbers `N.` (problems are frequently packed several per line and grouped under
   italic sub-heads like `*Add (undo by subtracting):*`). Each problem captures its number, its
   markdown text (which may span lines, e.g. word problems), and any `{#code}`/refcode badge that
   `_id_worked_practice`/`_convert_anchors` already attached to the first problem of a line.
3. **Pair and decide.** A practice set converts **only if every problem number it shows has a
   matching answer in the map** (and ≥ 2 problems parsed). Otherwise the set falls back unchanged.
4. **Emit.** For a converting set, render a `<section class="practice">` whose problems are rows,
   each with a native `<details class="qcheck">` reveal holding that problem's answer; italic
   sub-heads are preserved as captions between rows. Mark the answer-key block(s) whose numbers
   were fully consumed as **dropped** (not rendered). Non-converting sets and their answer keys
   fall through to today's `_blockify` rendering (`.practice` + the single `.answers` box).

### Markup (per converted set)

```html
<section class="practice">
  <span class="eyebrow">…Practice</span>
  <p class="practice-sub">Add (undo by subtracting):</p>           <!-- preserved group sub-head -->
  <div class="prow">
    <span class="prob"><span class="pnum">1.</span> x + 5 = 12</span>
    <details class="qcheck">
      <summary><span class="qc-label">Reveal answer</span></summary>
      <span class="qa">7</span>
    </details>
  </div>
  …
</section>
```

- The reveal is a native `<details>/<summary>` — no JS, keyboard-focusable, and expands in print
  via the existing `@media print { details > * { display: revert } }` rule.
- `<summary>` carries an accessible name that includes the problem number (e.g. a visually-hidden
  "answer to problem 1"), so screen-reader users know which answer a control reveals.
- Inner problem/answer markdown is rendered with the same `markdown="1"` + residue-strip convention
  the existing blocks use (see Determinism), so bold, `(x, y)`, superscripts, and `$…$`/`$$…$$`
  math survive exactly as in the current box.

### CSS (new, scoped)

A new `.qcheck` / `.prow` / `.practice-sub` block in `build_textbook.CSS`. Closed state: a green
"Reveal answer" pill aligned to the right of the row (the textbook's `--leaf` accent). Open state:
the answer shown inline (green, checkmarked), pill collapses to a small "Hide". Reuses existing
custom properties (`--leaf`, `--card`, `--rule`, `--radius`, etc.) and respects
`prefers-reduced-motion`. **`.answers` is left untouched.**

## Edge cases (observed in `textbook-src/`)

| Case | Example | Handling |
|------|---------|----------|
| Packed several-per-line | `1. x+5=12  2. x+9=14 …` | Split on leading `N.`; one row each |
| Group sub-heads | `*Add (undo by subtracting):*` | Preserved as `.practice-sub` caption |
| Prose answers | `14) identity — all real numbers` | Carried as answer markdown |
| Bold in answers | `16) **prime (irreducible…)**` | Carried as answer markdown |
| Superscripts / sci-notation | `1) x⁷`, `5) 7.2×10⁵` | Carried verbatim |
| Ordered-pair answers | `(2, 3)` (unit-07) | Carried verbatim |
| Multi-line answer key | unit-02 L2.4 (`1)…12)` then `13)…21)`) | Continuation lines concatenated into one map |
| `N.` answer delimiter | unit-01 `**Answer key:** 13. -4 14. 4 …` | Supported as fallback delimiter |
| Multiple keys per lesson | unit-01 (lines 403 & 423), unit-12 (436 & 453) | All keys merged into one lesson map |
| Label trailing note | `**Answer key:** *(…)*` | Note stripped from the parsed key |
| Word-problem sets | unit-06, unit-07 | Convert iff every shown number maps; else fall back |
| Non-contiguous numbering | unit-08 "core" set (2,3,5,6,7 moved to Reach) | Convert iff every **shown** number maps |
| Table / non-`N.` problems | appendix statistics | Falls back (no clean split) |

### Fallback triggers (keep today's single box)

- A practice block with fewer than 2 parseable numbered problems.
- Any shown problem number missing from the lesson answer map.
- No `**Answer key…:**` block found for the practice set's numbers.

The build will **log a per-lesson convert/fall-back summary** so we can see coverage and confirm
nothing regressed.

## Determinism

Per the known CI constraint (`md_in_html` emits a stray `markdown="1"` on some CPython patch
levels), the build already does `body.replace(' markdown="1"', '')`. The new markup uses the same
`markdown="1"` inner-rendering convention and relies on that same strip, so output stays
byte-identical across Python patch levels. New emitted HTML must be deterministic (no dict/set
ordering leaks; ordered iteration only).

## Interaction with reference codes

`_id_worked_practice` continues to run unchanged and attaches a `{#code}` badge to the first
numbered problem of each practice line. The split carries that badge onto the first problem's row.
Per-problem deep-link coverage is therefore **unchanged** from today (first-of-line only); widening
it is explicitly out of scope.

## Testing

TDD, extending `_verification/tests/test_textbook.py` (and helpers it already uses). Cases:

1. **Clean convert** — a packed numbered set with a `N)` key → N `.prow` rows, N `.qcheck`
   reveals, each answer matched to its number; **no** `.answers` box emitted for that set.
2. **Multi-per-line split** — `1. … 2. … 3. …` on one source line → 3 separate rows.
3. **Group sub-heads preserved** — `*Add…:*` becomes a `.practice-sub` caption, not a problem.
4. **Prose / bold / superscript / `(x,y)` answers** — survive into `.qa` verbatim.
5. **Multi-line & multiple keys merged** — unit-02-style split key pairs correctly.
6. **`N.` fallback delimiter** — unit-01-style `13. -4 …` key parses.
7. **Fallback: missing answer** — a set with an unmatched number keeps the single `.answers` box
   and emits no `.qcheck`.
8. **Fallback: non-numbered/table set** — unchanged rendering.
9. **Accessibility** — every `<summary>` has an accessible name containing its problem number.
10. **Tutor guide untouched** — `_problem_html` still emits `<details class="answers">`
    "Worked solution"; `.answers` CSS unchanged (assert on the rendered tutor-guide output).
11. **Determinism** — no residual ` markdown="1"`; rebuilding twice is byte-identical.

Then: regenerate all sites (`build_all.py` / each `build_*.py`), run every `--check`, and run the
full `pytest` suite. Report the convert/fall-back counts per unit.

## Files touched

- `_verification/build_textbook.py` — the pairing transform + new CSS (only file with logic).
- `_verification/tests/test_textbook.py` — new tests.
- `docs/textbook/*.html`, `docs/textbook/textbook.css` — regenerated output (committed, per repo
  convention). Other sites' `textbook.css` also regenerate because CSS is shared (additive only).

## Risks

- **Parser breadth.** Mitigated by strict pairing + fallback + the per-lesson coverage log and
  case-by-case tests; worst case a set keeps today's behavior.
- **Determinism drift.** Mitigated by reusing the existing residue-strip and ordered iteration.
- **Accidental `.answers` regression** affecting the tutor guide. Mitigated by a dedicated new
  class and an explicit tutor-guide assertion.
