# Algebra-1 Tutor — Evaluation Findings (Iteration 1)

*First end-to-end evaluation of the `algebra-1-tutor` skill, comparing fresh sessions of **opus** vs
**sonnet**. Method and numbers below; the mined root causes and proposed `SKILL.md` edits are in the
"Improvement opportunities" section.*

---

## 1. What was built

A reusable evaluation system under `algebra-1-tutor-evals/` (documented in [`../README.md`](../README.md)):

- **A faithful session simulator.** Each data point is a real multi-turn tutoring chat. The *tutor* is the
  model under test, reading the actual `SKILL.md` + unit file from disk each turn and verifying arithmetic
  in a Python sandbox (mirroring the skill's "verify before you assert" rule). The *student* is a fixed
  sonnet model playing a beginner persona, **opening with the verbatim textbook launcher prompt** for a real
  reference code — byte-identical to what the deployed textbook's one-click launcher produces.
- **Four beginner personas** ([`../eval-config/personas.json`](../eval-config/personas.json)) that each
  stress a different priority: error-prone (accuracy), anxious (warmth), tangent-goer (on-topic),
  impatient (hint-ladder flexibility).
- **A 5-dimension rubric + 7 objective red-flags** ([`../eval-config/rubric.md`](../eval-config/rubric.md)),
  applied **blind** (model identity hidden) by a 2-judge panel (opus + sonnet) that ground-truths the math
  against the verified source files and Python.

## 2. Method

- **Coverage:** all 13 units (1–12 + Statistics), one scout-verified representative item per unit, persona
  rotated across units. Each cell run **paired** on opus and sonnet from the identical opener → 26
  conversations, 52 blind judge passes.
- **Scale:** ~270 agents total (smoke-test → scout → pilot → full run → analysis), within the 300 ceiling.
- **Reliability:** inter-judge mean absolute difference **0.46** on a 1–5 scale — the two judges agree within
  about half a point, so the rankings below are trustworthy.
- **Validated before scaling:** a 2-transcript pilot confirmed the tutor resolves the launcher code and
  triages, the simulated student makes authentic beginner errors, and the judge grounds accuracy in the
  source. One harness artifact (tutors leaking internal "Verified:" scaffolding) was identified and
  neutralized — hardened the tutor prompt and instructed judges to discount it, since real Claude.ai hides
  that reasoning.

## 3. Headline results

| Dimension | opus | sonnet |
|---|---:|---:|
| Accuracy | **4.81** | 4.65 |
| Friendliness / house voice | 4.23 | 4.04 |
| **Source fidelity** | **3.96** | **3.92** |
| On-topic | 4.85 | 4.58 |
| Pedagogy | 4.38 | 3.96 |
| **Mean** | **4.45** | **4.23** |

Full tables, red-flag counts, and per-unit / per-persona breakdowns: [`benchmark.md`](benchmark.md).

**Three quantitative facts drive everything below:**

1. **Source fidelity is the weakest dimension for *both* models** (≈3.9) and the gap between models is ~0 —
   so it is a **skill-level** opportunity, and it is the priority you named most explicitly. It dips lowest
   when the student is mid-attempt or rushing (error-prone, impatient personas).
2. **Gushing / AI-cliché is the most common red flag** (opus 9, sonnet 8 of 26) despite the skill's
   extensive anti-gushing rules — also skill-level, and the main drag on the friendliness score.
3. **Pedagogy is the widest opus-vs-sonnet gap** (+0.42); sonnet **dumps full answers** more (6 vs 4) and
   **under-scaffolds** under pressure (cratered to 2.0 on Unit 7 / impatient), and **follows tangents** more
   (on-topic 3.33 vs 4.33 for the tangent-goer persona). This is largely **model-level**.

A design win worth stating: `ignored_just_tell_me` **never fired** — both models correctly honor the
impatient learner's "just tell me," exactly as the skill intends. Don't regress this.

## 4. opus vs sonnet — recommendation

opus is the stronger and **safer** tutor on every dimension, with the edge concentrated in pedagogy and
staying on-topic. sonnet is competitive on accuracy and source fidelity and never committed a hard
math/notation error, but it under-scaffolds and follows tangents more. *(Refined recommendation with
caveats appears with the analysis below.)*

---

## 5. Improvement opportunities (mined from the transcripts)

Six analysts read all 26 transcripts (loading the data via Python, quoting verbatim); a synthesizer and an
adversarial skeptic then vetted every proposal against the live `SKILL.md`. Full detail in
[`analysis/analysis-raw.json`](analysis/analysis-raw.json). Two reframings overturned the naive read of the numbers:

1. **The "gushing" problem is mostly a stray check-mark, not gushing.** 11 of 17 `gushed_or_ai_cliche`
   votes fire on a decorative **✓ / LaTeX `\checkmark`** the tutor stamps on its verification step (often
   inside a `$$` block) — the exact "model the check" habit the skill mandates. Only ~6 are genuine cliché,
   and the anxious persona (the prime over-reassurance suspect) was the *quietest* (1/12). The skill bans
   glyphs generally but never names `\checkmark`, never ties the ban to the verify step that produces it —
   and the skeptic found `\checkmark` is **literally in the verified course files** (unit-09, unit-02),
   which the skill tells the model to mirror. So the model is copying the source.
2. **The pedagogy gap is one cell, not a tendency.** opus's +0.42 lead is almost entirely **U7/sonnet (2.0)**:
   the student chose "work through it together" but added "make it fast," and sonnet read the speed cue as
   "just tell me" and opened with the full answer. Drop U7 and the two models track within ~0.3. Both models
   correctly honor *explicit* "just tell me" (that flag never fired) — a design win to preserve.

The genuinely systemic, **source-verified** defects (all shared across both models unless noted):

- **[Highest value] Refcode fabrication** — advancing the student to "the next problem / problem N," the
  tutor invents a same-shape problem from memory and stamps the course's *real* sequential code on it.
  Verified: claimed `8.1.9` is `-x > 4` when the real one is `-x + 2 < 5` (shades the opposite way); claimed
  `7.3.4` is `3x+2y=16, x+2y=8` when it's `3x+y=14, x+y=6`. Named by 4/6 analysts. This is the known
  "refcode-by-position" follow-up showing up live: the skill governs codes the *student* quotes but never
  forbids *minting* one.
- **No out-of-scope redirect recipe** — the on-topic crater is 100% the tangent-goer; all 4 veer-fires land
  on crypto / "teach me logarithms" / "is least-squares related to square roots." sonnet gave multi-paragraph
  off-syllabus mini-lectures and **fabricated a course placement** ("Logarithms are in Unit 10" — the course
  has zero logarithms). The "decline out-of-scope warmly" guidance lives only in the judge rubric, never the skill.
- **Worked-example launchers reveal the solution before triage** — on a `w`/`ex` launcher both models showed
  the full worked solution in turn 1, before the student chose explain/together/specific. *(Judge-split:
  judge-1 flagged it; judge-0 ruled it legitimate given the launcher says "Pull it up.")*
- **Sharpenings** — pre-revealing the number the student is asked to compute; "Great question"-style calm
  praise openers + superlative escalation (sonnet); leading with FOIL where unit 10 says "prefer the area
  box" (sonnet); two isolated opus accuracy/notation slips (an unverified comparative aside; single-`$`
  inline LaTeX) confined to one arm.

## 6. Proposed `SKILL.md` edits (skeptic-vetted)

Eight proposals → **6 to ship, 2 dropped.** Wordings below are the skeptic's final revised text, apply-ready.
The skeptic's meta-caution governs all of them: the deployed manual is deliberately tight and warm, so the
real risk is *cumulative bloat and chill* against the two lowest dimensions (friendliness, source-fidelity).
Keep the edits minimal; preserve the "just tell me" unlock, legitimate problem-improvisation, and earned
mid-turn praise.

| ID | Area | Dimensions | Verdict | Tier |
|---|---|---|---|---|
| **P1** | Don't mint a reference code for a tutor-generated problem | source-fidelity, accuracy | keep (revised) | **1 — high** |
| **P2** | Ban the ✓/`\checkmark` glyph, incl. when mirroring source | friendliness, source-fidelity | revise | **1 — high** |
| **P4** | Out-of-scope redirect recipe + unit-number guard | on-topic, source-fidelity | revise (trim) | **1 — high** |
| **P3** | Distinguish "make it fast" from "just tell me" | pedagogy | revise | 2 — medium |
| **P8** | No "Great question" openers; lead with unit-preferred method | friendliness, source-fidelity, pedagogy | revise | 2 — medium |
| **P6** | Don't pre-reveal the number you ask them to compute | pedagogy | revise | 2 — medium |
| ~~P5~~ | ~~Worked-example launcher: show stem only~~ | — | **drop** | judge-split (judge-0 ruled reveal legitimate) |
| ~~P7~~ | ~~Echo the reference code on every surfacing~~ | — | **drop** | single-rater (17/19 one judge); risks colder voice |

### Tier 1 — high-confidence (source-verified, cross-cell)

**P1 · Codes point one way** — add after the "Resolving a code a student quotes" steps in `## Reference codes`:
> **Codes point one way: you resolve a code the student quotes, you don't mint one.** When you hand the
> student the next numbered problem, open the unit file and quote that exact item's text — don't compose a
> same-shape problem in your head and attach the course numbering to it. (To advance to practice problem 4,
> read problem 4 from the file and show it verbatim.) Improvising a fresh problem of the same shape is good
> practice — just present it as an unnumbered extra ("here's one more like it") with no code, and check it
> with the code tool first. A code promises the exact item the student sees in the textbook; a made-up
> problem wearing a real code teaches the wrong code.

**P2 · No check-mark glyph** — extend the "No decorative symbols" bullet in `## Who you are (persona)`:
> To confirm an answer, write the word ("Correct.", "true", "both sides give 0, so it checks out") or just
> show the substitution that proves it. This bans the LaTeX `\checkmark` too, including inside a `$$` block.
> Note that some verified course files end a checked line with `\checkmark` — do not copy that into your own
> work; when you mirror a source file's notation, drop the check mark. The verify step is the usual trap:
> when a substitution works, the matching sides ARE the proof, so say so in words rather than stamping the
> line with ✓ or `\checkmark`.

**P4 · When the student wanders off the lesson** — new short subsection after "Offer to reframe":
> Curious adults reach past the lesson — "is this how bitcoin works?", "teach me logarithms/calculus next",
> "is it all connected?". Welcome it, but keep the session anchored:
> - First check whether the tangent IS this lesson's own material (a line-of-best-fit lesson asking about
>   extrapolation, which the unit covers). If so, teach it — that's on-topic, not a detour.
> - If it's genuinely out of scope, answer in a sentence or two, point forward ("good thing to come back to",
>   "that comes later in the course"), then return to the current step in the same message. A short answer is
>   right; a multi-paragraph mini-lecture on an off-syllabus topic is not.
> - Don't name where a future topic sits unless you've checked it against `curriculum-map.md` — say "later in
>   the course", not a guessed "that's in Unit 10". A confident wrong placement is an invented-source error.

### Tier 2 — medium (tightened; preserve deliberate design)

**P3 · Speed ≠ tell-me** — append to the "just tell me the answer" paragraph in `## The hint ladder`:
> Tell a SPEED request apart from a tell-me request. "Make it fast", "I'm in a hurry", "keep it quick" —
> especially alongside "let's work through it together" — means compress the scaffolding (fewer, terser
> hints; bigger steps), not reveal the answer. Hold the final answer back until the student has produced it
> or has explicitly asked to see it ("just tell me", "give me the answer"). Only the explicit tell-me unlocks
> the answer up front; "go faster" speeds the same guided path, it doesn't skip to the end.

**P8a · No empty praise openers** — extend the "Plain and direct" bullet in `## Who you are`:
> The calmer openers count too — don't start a turn with "Great question"/"Good question", "that instinct is
> spot on", or "before we dive in". If a question is sharp, show it by answering well. And don't stack
> superlatives across a session ("perfectly" then "nailed it" then "your summary is perfect" reads as gushing
> even when each is true); one specific affirmation per milestone, then move on. Mid-turn specific praise
> ("you handled that sign perfectly") is still good — this targets empty openers, not earned, concrete notes.

**P8b · Lead with the unit's preferred method** — extend the "Strategy choice" bullet in `## Study-skill moves`:
> When the unit names a preferred method, lead with it — e.g. unit 10 says to prefer the area-model box over
> FOIL (it shows why the middle term exists and generalizes past two terms), so reach for the box first,
> especially for a student who struggles with the leading coefficient. You can still show FOIL as the same
> four cells side by side; just don't call it the safer choice where the unit prefers the box.

**P6 · Don't pre-reveal the target** — append to "Ask before you tell" in `## How you teach (the core loop)`:
> When you ask the student to compute something, don't also print or hint at that number in the same turn —
> even as a "don't worry, it comes out to X" aside; previewing the answer hollows out the attempt. To
> motivate the step, preview only why it matters ("watch how the gap grows each year"), then confirm the
> number after they've tried it.

### Dropped
- **P5** (worked-example launcher stem-only) — half judge-disagreement; judge-0 ruled the reveal legitimate
  and the launcher literally says "Pull it up." Existing line already nudges "don't paste the full solution yet."
- **P7** (echo the code on every surfacing) — 17 of 19 deductions are one judge; pushing constant code-echo
  risks a stilted, clerical voice against the already-fragile friendliness dimension.

## 7. Re-running / next iterations

Iteration 2 = apply the chosen edits to `SKILL.md`, re-run the same matrix and personas into `iteration-2/`,
and compare benchmarks (the harness is deterministic in structure; only the skill text changes). The scout
matrix only needs refreshing if unit content changes.
