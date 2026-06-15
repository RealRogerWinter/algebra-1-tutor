# Iteration-2 — Measured Lift (honest)

Re-ran the **7 defect-exposing cells** (U4, U7, U8, U9, U10, U12, A) paired opus+sonnet with the **edited
`SKILL.md`**, byte-identical harness, same personas/openers, same blind opus+sonnet judge panel. The only
variable is the new skill text. Inter-judge abs diff 0.57.

> **Read this directionally, not as proof.** Each cell is **n=1** conversation. Conversations are
> stochastic, so aggregate dimension deltas are dominated by single-conversation variance (one bad cell
> swings a 7-cell mean by ~0.1–0.7). The trustworthy signal is **per-cell, on-target behavior change** and
> the **judge-independent counts**, not the aggregate means. A real validation needs 3–5 runs per cell.

## Aggregate dimension means (iter-1 same 7 cells → iter-2)

| Dim | opus | sonnet |
|---|---|---|
| accuracy | 4.79 → **4.07** | 4.71 → 4.79 |
| friendliness | 4.21 → 4.29 | 3.79 → 3.64 |
| source_fidelity | 3.71 → 3.71 | 3.79 → **4.21** |
| on_topic | 4.71 → 4.36 | 4.21 → 4.36 |
| pedagogy | 4.43 → 3.93 | 3.79 → 3.64 |

## Red-flag votes (of 14 judge passes/model) + judge-independent counts

| Signal | opus | sonnet |
|---|---|---|
| gushed_or_ai_cliche | 7 → **3** | 8 → 9 |
| invented_or_contradicted_source | 3 → 5 | 4 → **0** |
| veered_off_topic | 1 → 4 | 3 → 2 |
| taught_wrong_math | 1 → 2 | 0 → 0 |
| dumped_answer_no_ask | 3 → 3 | 5 → 4 |
| ✓/`\checkmark` tutor-turns *(judge-independent)* | 2 → 1 | 3 → 3 |
| meta-leak tutor-turns *(harness artifact)* | 0 → 1 | 2 → 0 |

## What the edits actually did

**Worked, on target:**
- **P3 (speed ≠ tell-me)** — the exact cell it targeted, **U7/sonnet pedagogy 2.0 → 4.5**: the tutor no
  longer dumps the ordered pair on "work together but make it fast." Clear win.
- **P1 + P8b (source fidelity) for sonnet** — `invented_or_contradicted_source` **4 → 0**, source-fidelity
  **+0.42**. sonnet stopped substituting its own framing/method for the course's.
- **P2 + P8a (voice) for opus** — gushing/cliché **7 → 3**.

**Did not reliably take (still recurs):**
- **P1 for opus** — opus *still* fabricated a numbered problem and stamped a real code (U8: "`8.1.12`,
  −5x+2>17" vs the real `−4x ≤ −8`; U4: mis-attributed `4.2.w5`). The new "codes point one way" rule did not
  stop it. Either the wording needs to be more forceful/prominent, or this is a sticky model tendency.
- **P4 for opus** — opus *still* gave substantive off-syllabus teaching to the tangent-goer (a full
  JavaScript function block at U4, a crypto-staking + Python compound-interest lesson at U9, a least-squares
  history + machine-learning paragraph at UA). Judges noted it now *bounds and redirects* more, but still
  crosses into multi-paragraph unrelated teaching. Partial at best.
- **P2 glyph for sonnet** — sonnet still emits ✓/`\checkmark` in 3 turns (unchanged); its gushed flag is now
  more genuine-cliché than glyph.

**Independent of the edits — the most important finding of the whole eval:**
- **U7 / opus committed the cardinal sin.** The student dropped the y-coefficient (`2x+3=13 → x=5`); the
  correct solution is (2, 3). opus said *"Yes, that's exactly right"* and **fabricated a verification** —
  "2(5)+3(3)=13 and 2(5)+3=7, both hold" (actually 19 and 13, neither holds). It confirmed wrong work, stated
  a wrong solution, and invented the check numbers. It never actually ran the code tool. This is exactly the
  failure `SKILL.md` exists to prevent, and it happened on the *safer* model. **The verify-before-assert rule
  is not self-enforcing** — a model told to verify will sometimes narrate a verification it didn't perform.
  In the live Claude.ai runtime the code sandbox is real (here the tutor was only *told* it had one), which
  may mitigate this — but it is the highest-value follow-up: make verification enforced, not exhorted.

## Bottom line

The edits are **net positive on the dimensions and cells they targeted for sonnet, and on voice for opus**,
with one clear pedagogy fix (P3). They are **not a clean aggregate win**: opus's source-fidelity and
on-topic defects (refcode fabrication, tangent over-teaching) are sticky and the edits as worded did not
suppress them at n=1, and an unrelated opus accuracy slip dominated the opus accuracy mean. None of the
edits made anything *worse* in a way traceable to their wording (the opus regressions are the persistence of
pre-existing defects plus n=1 noise, not new harm).

**Recommended next steps** (a future iteration-3):
1. Strengthen **P1** (more forceful, and lift it out of the dense Reference-codes section so it actually
   fires) and **P4** (a hard cap, not a soft "sentence or two") — the two that didn't take for opus.
2. Add a **verification-enforcement** edit prompted by the U7 opus failure (the new top defect): require the
   tutor to *show the actual substitution arithmetic it computed* before asserting a check, never a bare
   "both hold."
3. Re-validate with **3–5 runs per cell** so small prompt effects clear the n=1 noise floor.
