# Algebra-1 Tutor — Benchmark, Iteration 1

**Design:** 13 units (1–12 + Statistics), one representative reference-code item per unit, each run as a
4-tutor-turn conversation **paired on opus and sonnet** from the identical verbatim textbook launcher
opener. A fixed sonnet "student" played a rotated beginner persona. Every transcript was graded **blind**
(model identity hidden) by a **2-judge panel (opus + sonnet)** against [`../eval-config/rubric.md`](../eval-config/rubric.md).

- 26 conversations · 52 judge passes · **inter-judge mean abs difference 0.46** (judges agree within ~½ point — reliable)
- Scores are 1–5; each cell = mean of the 2 judges. Raw data in [`raw-result.json`](raw-result.json).

## Overall (mean over 13 transcripts/model)

| Dimension | opus | sonnet | Δ (opus−sonnet) |
|---|---:|---:|---:|
| Accuracy | **4.81** | 4.65 | +0.16 |
| Friendliness / house voice | 4.23 | 4.04 | +0.19 |
| **Source fidelity** | **3.96** | **3.92** | +0.04 |
| On-topic | 4.85 | 4.58 | +0.27 |
| Pedagogy | 4.38 | 3.96 | +0.42 |
| **Mean** | **4.45** | **4.23** | +0.22 |

**Both models are strong** (this is a well-built skill), but **source fidelity is the weakest dimension for
both** — and it is the priority you flagged most explicitly. opus edges sonnet on every dimension; the gap is
**widest on pedagogy** (+0.42) and narrowest on source fidelity (+0.04, essentially tied — a *skill* issue, not a
model one).

## Red-flag votes (out of 26 judge passes per model)

| Red flag | opus | sonnet |
|---|---:|---:|
| **gushed_or_ai_cliche** | **9** | **8** |
| dumped_answer_no_ask | 4 | **6** |
| invented_or_contradicted_source | 3 | 4 |
| veered_off_topic | 1 | 3 |
| broke_notation | 2 | 0 |
| taught_wrong_math | 1 | 0 |
| ignored_just_tell_me | 0 | 0 |

The dominant flag for **both** models is **gushing / AI-cliché** — fired on roughly a third of passes despite the
skill's explicit and extensive anti-gushing rules. `ignored_just_tell_me` never fired: both models correctly
**honor** the impatient learner's request to be told (a deliberate design win). The rare hard-accuracy failures
(`taught_wrong_math` 1, `broke_notation` 2) are **opus-only** and isolated; sonnet's accuracy mean is lower
without tripping those flags (more soft slips, fewer hard ones).

## Where the low scores live (notable cells)

| Cell | Persona | What stands out |
|---|---|---|
| **U7 · 7.3 Elimination** | impatient | **sonnet pedagogy 2.0** vs opus 5.0 — the single largest gap; sonnet under-scaffolds under time pressure |
| **U9 · 9.2 Exponentials** | tangent_goer | **sonnet on-topic 2.0, friendliness 2.5** (opus on-topic 3.5) — the tangent-goer pulled sonnet off the lesson |
| **U8 · 8.1 Inequalities** | error_prone | **opus source-fidelity 2.5** vs sonnet 4.5 — opus drifted from the source here |
| **U10 · 10.4 Polynomials** | error_prone | source-fidelity low for both (opus 3.0 / sonnet 2.5); **opus accuracy 4.0** (its lowest) |

## Persona patterns (mean over the units each persona covered)

- **tangent_goer** is the hardest persona for **on-topic** (opus 4.33, **sonnet 3.33**) — confirms the "don't veer
  off into other discussions" concern, with sonnet markedly more susceptible.
- **error_prone** and **impatient** produce the lowest **source-fidelity** (≈3.4–3.8) — when the student is mid-attempt
  or rushing, tutors lean on their own framing instead of the unit's verified material.
- **impatient** is where **sonnet pedagogy** is weakest (3.67 vs opus 5.0).
- **anxious** is handled well by both (source-fidelity and friendliness hold up) — the persona that most stresses
  warmth did not expose a gap.

## Reading these numbers

The quantitative story: **two shared, skill-level opportunities** — source fidelity (lowest dimension) and
gushing/AI-cliché (top red flag) — plus **one model-level story** — opus is the safer tutor overall, especially on
pedagogy and staying on-topic, while sonnet is competitive on accuracy/source-fidelity but under-scaffolds and
follows tangents more.

The *why* behind each number — the verbatim recurring phrases, root causes, and proposed `SKILL.md` edits — is in
[`analysis/`](analysis/) (produced by the analysis sub-agent teams) and summarized in the top-level findings report.

> Caveats (see [`../README.md`](../README.md)): this is a faithful proxy, not the live product — skill is injected
> not router-triggered, the student is simulated, there's no live Artifact/photo rendering, and conversations are
> 4 turns (cross-session Progress-Card behavior is barely exercised). All caveats apply equally to both models, so
> the **comparison** is fair; treat absolute scores as directional.
