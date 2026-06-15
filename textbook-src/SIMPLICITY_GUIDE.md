# Simplicity Watch-List — Algebra 1 Student Textbook (Prose-Rewrite Pass)

**For:** the ~13 unit authors rewriting prose. This is the *simplicity lens* you apply on top of `WRITING_FRAMEWORK.md` (same folder), which is the **governing document** for this pass. Where this list and the framework agree, the framework's hard rules still govern; this list tells you what "too complex for a first-timer" looks like in our actual book and the simplest fix, grounded in how the best open-source Algebra 1 intros do it (OpenStax, Tyler Wallace, CK-12, Illustrative Mathematics, Math is Fun).

**Read the Quick-reference card (last page) first — it's your working surface.** Everything above it is the explanation you consult when a row is unclear. One canonical statement per idea; sections cross-reference rather than repeat.

---

## 0. Before you touch anything: where you edit, and what's locked

- **Read the tutor source, write a separate student copy.** Per `WRITING_FRAMEWORK.md` §0, your input is the tutor unit file `algebra-1-tutor/references/units/unit-NN-*.md`; you **write the rewritten student version** to `textbook-src/<the identical filename>` (these student copies already exist for Units 1–12 and Unit A — you are revising them, not creating from scratch). Never edit the tutor original. The student copy is already reader-facing prose; your job is simplicity, not a persona switch.
- **Run the guard before you submit:** `python _verification/check_textbook_src.py <UNIT>` (verifies your copy kept every SSOT item — codes, lessons, answer keys — and leaked no tutor meta). Then the full §9 gate (`generate.py --check`, `check_alignment.py`, `check_notation.py`, `verify_answers.py`, `build_textbook.py --check`). Fix until green.
- **The math is unbackstopped.** `WRITING_FRAMEWORK.md` §9 is explicit: CI does **not** cross-check your `.md` numbers/answers against the verified JSON (except a narrow line-intercept lint). If you reword `4x = 20` to `4x = 21`, flip an answer key, or drop a numbered item, **the build stays green and you've shipped wrong math.** The verbatim-preservation rule is therefore absolute and protected only by your eyes.
- **Two lines never to cross** (framework §9 Absolute Rules): never alter math, worked-example results, practice items, answer keys, titles, the bold structural labels, New-terms definitions (term + meaning), or `{#…}` anchors; never renumber/reorder worked examples or practice; never start a relocated note with `**` or a new `N.` line (it shifts/deletes deep-link codes); never invent, duplicate, or delete a figure anchor. When simplicity and the math/structure conflict, **the math and structure win — find another way to be kind.**
- **Every rewrite must pass the copyedit + anti-AI-tell checklist in framework §8.** Plain words, sparing em-dashes (a rare one is fine; three in a paragraph isn't), no rule-of-three pile-ups, no hollow "not X, it's Y" flips. Note the two deliberate overrides §8 grants this book: **second-person "you" and contractions are the house voice (keep them),** and a **genuine misconception corrective-contrast is encouraged** ("= doesn't mean *compute*; it means the two sides balance") — only the *hollow* flip is banned. There is no separate `/copyedit` ship-gate file for this pass; §8 is the gate.

**Tag on every rule below:** **[AGENT]** = a prose rewrite you do; **[FLAG]** = something only the orchestrator/SSOT owner can change — flag it in your handoff, do not do it yourself.

---

## 1. The simplicity bar

**Who you write for** (framework §1, restated as the test): one motivated adult, alone at a kitchen table, fluent in arithmetic, meeting almost everything in algebra for the **first time**, often math-anxious. No tutor in the room. This book is their only explanation.

**The one test, applied to every paragraph:**

> **Could a nervous beginner follow this on the *first* read, without re-reading and without already knowing the idea?**

If a sentence needs a second pass, needs a term defined three lines later, or needs the reader to hold an abstraction before seeing a concrete case, it fails. Rewrite it. Two corollaries decide most close calls:

- **Simplest true thing first.** The reader should always attach a new sentence to something they already understand (a picture, a number, a one-line plain definition). Never make them hold an abstraction with nothing under it.
- **Calm is part of "followed it."** A reader who got the right answer but feels behind or braced for failure has not passed the test. Plain, unranked, unhurried prose is a simplicity feature.

**Heuristics, not gates.** The numeric triggers below (≤8-word tag, 3+ dense paragraphs, 5-word swap test, 5+ definitions) are recognition aids. On a borderline call, keep the change minimal and preserve the source structure (framework §3/§9); when unsure whether to bullet or cut, do neither and leave the prose intact. Divergence should fail safe toward the locked structure.

---

## 2. Watch-for → do-instead rules (apply book-wide)

Each rule: the pattern, the do-instead, and at least one **verified** instance from our source (file + line, so you can open it). Scan every lesson for all of these.

### R1. Mixed or stacked metaphors → one image per idea, used to the end **[AGENT]**

- **Watch for:** two or more images for one concept; a slash like "mystery-box / reserved-seat"; a metaphor introduced then dropped; an image drifting to where it no longer fits.
- **Do instead:** pick the **one** image from the framework §4 playbook that targets *this* confusion, state it once, do the real math on it, then walk back to symbols. If the lesson must switch pictures, **mark the handoff in one honest sentence** and name *where the first picture stops being exact* (framework §4: every metaphor leaks; name the leak when silence would mislead).
- **Get the balance-scale leak point right** (framework §4 table, "=" row, is the SSOT): the scale stays valid for **adding, subtracting, and splitting into equal groups (multiplying/dividing both sides by a *positive*)**. It loses its clean picture **only when you multiply or divide both sides by a *negative*.** So `2x = 10` is solved by halving both pans and the scale still works — do **not** tell the reader the scale is "only for adding and subtracting," and do not retire it at `2x = 10`. The honest handoff line is the framework's: "this works for adding, subtracting, and scaling both sides by a positive; there's no clean weight-picture for multiplying both sides by a negative, so we'll switch pictures there rather than stretch this one until it lies."
- **Verified instances:** unit-08 line 144 sets up "Picture two bars you might have to clear" for *and*/*or*, a one-shot framing not reused; unit-08 line 333+ runs "the dividing fence" / "half-plane" / "boundary" together and line 335 adds "open-versus-filled choice ... in a new costume"; unit-12 line 233 brings in "the same balance scale from Unit 2" alongside the area-box work of the unit; unit-05 line 9 opens slope with "an old friend in new clothes." Each is a place to settle on one image per idea.

### R2. Overwhelming intro (vocabulary dump / philosophy essay) → one concrete handhold first **[AGENT]**

- **Watch for:** a New-terms-style run of ~5+ formal definitions before any picture; a lesson opening with several abstract "big idea" paragraphs before the reader touches a number; the hardest member of a set introduced fully-formalized in the first breath.
- **Do instead:** **one concrete handhold first** (a picture, a single worked number, or a 2-line plain definition), then layer detail one beat at a time. This is the framework's three-beat order (§3, §4 below). Cut any unifying-philosophy paragraph to a sentence and move synthesis to the *end* of the first relevant lesson as a payoff.
- **Verified instance:** unit-01 line 108 (Lesson 1.2) opens by naming counting/whole/integer/rational in one dense paragraph *before* the number line is drawn at line 112. The fix is in §3a below.

### R3. Over-hedged rule → simplest common case first, edge cases later — *but never drop a correctness guard* **[AGENT]**

- **Watch for:** a first-encounter rule stated with stacked edge-conditions, nested parentheticals, forward-references, or meta-commentary about the rule's status, before the reader has used the rule once.
- **Do instead:** state the rule in its **simplest common case**, let the reader use it once on a clean worked example, then split edge cases into a short follow-up beat.
- **THE HARD CARVE-OUT (verified, do not get this wrong): simplest-case-first governs PLACEMENT, never PRESENCE.** Never simplify away a condition whose removal makes the rule *false*. Defer where it sits on the page; never defer that it exists. Three guards this protects, all load-bearing in the source:
  - **The k<0 branch of the Square-Root Property** is not an edge case. unit-12 line 115 states it outright: "*x²=k ⇒ x=±√k when k≥0; no real solution when k<0.* The k<0 branch is not a side-exception to patch later. It is half of the rule." Dropping it teaches the false `x² = k ⇒ x = ±√k`. Place it *after* a clean `x² = 9 ⇒ x = ±3`, but keep it (the source already does, at line 124).
  - **The discriminant<0 case** (unit-12 lines 298, 329) — same "no real solution" branch; keep it.
  - **The three absolute-value shapes carry genuinely different guards on k** and must not be merged into one. The source has them correct (unit-08 lines 240–242): `|x| = k` needs **k ≥ 0** (at k=0 one answer x=0; k<0 no solution); `|x| < k` needs **k > 0 strict** (at k≤0 it is empty, *not* x=0); `|x| > k` holds for **any k ≥ 0** (k<0 → all reals). Defer the degenerate k=0/k<0 cases to a follow-up beat (the source does, line 261), but never collapse the three guards into a single one — that teaches a false rule.
- **Verified instance of harmless over-hedging to fix:** unit-01 line 185, "it reads like six ranked steps when it's really four tiers, and two of the tiers are ties" — leads with an abstract count before any example. Fix in §3b (and see the locked-token carve-out in R6).

### R4. Mid-walkthrough error note → clean solution first, mix-up note after **[AGENT]**

- **Watch for:** inside a worked example, an aside longer than a short parenthetical that describes a mistake the reader didn't make, narrates a meta-lesson, or explains a sign aside.
- **Do instead:** the worked example narrates **correct reasoning only** (framework §3 "How to PRESENT worked examples" — every step gets an author-supplied *why*, but for the right move). At a step where a sign/operation could flip, the most you leave is a terse ≤8-word method tag ("dividing by a negative, so the sign flips"). Move any multi-sentence "if you'd forgotten…" passage into a "common mix-up" note in surrounding prose, placed *after* one clean success (§5).
- **Counter-safety (framework §3/§9):** when you relocate a note, keep it in prose; never make it a new numbered line, never start its line with `**`, never split a worked step into sub-`N.` lines — any of these shifts or deletes the worked-example deep-link codes.
- **Which of your examples even carry codes:** numbered-list worked examples (Units 1, 3, 5, 9, 12, A) get codes by position — counter-safety is mandatory. `$$`-block worked examples (Units 2, 4, 6, 7, 8, 10, 11) get no codes by design — but still never split one example into `N.` sub-lines. Check your unit's form before relocating any note.
- **Verified instance:** unit-01 line 57, worked example 1: "(Filling 9 here is the calculator habit. You computed 8 + 4 and forgot the right pan still has a +5 to balance.)" This is a mistake-the-reader-didn't-make aside *inside* a numbered (coded) worked example. Move it to a "common mix-up" note after the example, in prose, using the framework's own approved wording (§5, "Equals sign as compute here," and §7 line 392): *"It's natural to compute 8 + 4 and write 12, or 9, in the box; that's the calculator habit. But the box plus 5 has to balance 12, so the box holds 7."* Do not renumber the worked-example list.

### R5. Wall of text → short lead-in + bullets, a small table, or numbered steps **[AGENT]**

- **DEFAULT IS PROSE.** Convert to a list **only** when the items are a genuine parallel set (steps, cases, types). Connected reasoning that explains *why* stays prose even when long; fix a long passage by tightening sentences, not by bulleting it (framework §2: "this framework's bulleted form is for authors; student copy is prose"). The fix here is for lists masquerading as paragraphs.
- **Watch for:** a single paragraph listing several parallel items (types, signs, steps) in sentence form; a procedure narrated as a run-on.
- **Verified instance:** unit-08 line 335 narrates the two boundary decisions (solid/dashed, which side to shade) inside prose; this genuinely-parallel pair reads more clearly as a short 2-step list with the test-point method as the second step. (Contrast: do **not** bullet the connected reasoning at line 333 that builds the half-plane idea.)

### R6. Jargon before grounding → plain word first; house coinages reworded *in prose only*, never in the locked definition **[AGENT]**

- **Watch for:** an invented term-of-art used before (or instead of) a plain equivalent; the formal/symbolic form of a definition given before the friendly gloss; a first-contact definition packed with three clauses plus a misconception correction.
- **Do instead:** use the **field-standard plain phrase**; give the **plain gloss first, formal notation second**; keep a first-contact definition to one clause and fold "but not X" corrections in *at the moment the misconception surfaces*.
- **CRITICAL LOCKED-TOKEN CARVE-OUT (verified — read before you "drop tiers"):** the words **"four tiers"** and the bracket notation **[M…ultiply/D…ivide]** and **[A…dd/S…ubtract]** appear **verbatim inside the locked New-terms definition `{#1.3.d1}`** (unit-01 line 200), and "four tiers"/"ties" also appears in the lesson recap (line 221) and is the framework's own approved misconception phrasing (§5, "Order of operations as six ranks," line ~323). You may **NOT** edit the definition, the recap label, or the framework's approved note (framework §9 Rule #6). So: simplify the **teaching prose** you write around them toward plain "equal priority, done left to right" (§3b) — but the locked definition keeps "four tiers" and the brackets. When your prose and the locked definition use different words for the same idea, **that is allowed and expected.** Do not touch the definition to "harmonize" it; CI will not catch the violation, but it breaks a hard rule and a reviewer will.
- **Same caution for `{#1.2.d4}`** (the rational-number definition, "a ratio of two integers a/b (b ≠ 0)…", unit-01 line ~? in the 1.2 New-terms): it is locked verbatim. Lead your *prose* with the plain gloss ("a number you can write as one whole number over another"); the formal `a/b` stays in the definition untouched.
- **Verified instance:** unit-01 line 187 teaching prose uses "Picture four shelves … as equal partners." Reword the *prose* to plain "equal priority, left to right" per §3b; leave `{#1.3.d1}` alone.

### R7. Expression and equation are defined apart → frame "=" as a sentence's verb in 1.1, *in plain words* **[AGENT for the prose half; FLAG for the sequencing half]**

- **Verified state:** "Equation" is defined in 1.1 (`{#1.1.d2}`, unit-01 line 50). "Expression" is defined only in 1.5 (`{#1.5.d1}`, unit-01 line 355), where line 334 already draws the phrase-vs-sentence contrast well.
- **[AGENT] do-now in 1.1:** frame "=" as the verb of a sentence and contrast a *phrase* vs a *sentence* in **plain words** so "=" lands on the spot — **without using the term "expression"** (it isn't defined until 1.5; framework §3 forbids using a term the reader hasn't met). Do not re-define "equation" (already done in 1.1).
- **[FLAG] do-not:** moving the formal Expression definition earlier, or otherwise resequencing term scope across lessons, is an SSOT/orchestrator decision (anchors are append-only and density-locked, framework §9 Rule #5). Flag it; never do it.

### R8. First example is the diagnostic trap → supply the clean canonical case in *prose* before the worked block **[AGENT]**

- **Watch for:** the first worked example of a concept being the hard non-standard / "spot the trap" form.
- **Do instead:** you cannot reorder the worked-example list (framework §9). Where the first worked example is already the trap, the **teaching prose before the worked block must supply the clean canonical case** so the reader wins once before meeting the trap. Frame the clean case as the model and the trap case as the deliberate stress-test in your surrounding prose. (Flag to the orchestrator any lesson where no clean case exists anywhere, prose or list.)
- **Verified instance:** unit-01 line 57, worked example 1 is `8 + 4 = □ + 5` — the both-sides-have-operations form chosen to catch the "compute here" misread, and it is the *first* coded example. The fix: the 1.1 teaching prose should solve a clean single-unknown case (`x + 3 = 7`, which the source already works at lines 41–45) as the model *before* the worked block, so worked example 1 reads as the deliberate stress-test, not first contact. Do not reorder.

### R9. Two methods for one task at once → teach the one that scales, alone **[AGENT]**

- **Do instead:** teach the method that scales ("undo with the opposite") as the spine; present the alternative as a quick sanity-check *after*. (Framework §3 "Two valid methods, side by side" still applies where two methods are genuinely co-equal later — this rule is about *first* contact with solving.)
- **Verified instance:** unit-01 lines 41–45 (Lesson 1.1) introduce "ask the question out loud" (inspection) and "undo it" together at first contact. Keep undoing as the spine; demote inspection to the after-the-fact check.

### R10. Repeated boilerplate → say it once, then cut or compress **[AGENT]**

- **Watch for:** the same motivational set-pieces recurring near-verbatim across lessons — the "redo two or three problems from memory" spaced-practice line, the "mixed practice feels harder, and that's the point" interleaving speech, the "a check that disagrees is the check doing its job" reassurance.
- **Do instead:** keep **one** strong instance per unit (ideally in the unit front matter), compress the per-lesson repeats to a short pointer. Apply the **swap test** (framework §8): if two lessons' notes share their first five words, rewrite one. Keep the single instance that also points to where the reachable help is (framework §3 requires the "this is hard on purpose" line to point to the help in the same breath).
- **Verified instance:** the spaced-practice line is in the unit front matter (unit-01 line 7, "redo two or three problems from a lesson or two earlier from memory") *and* the difficulty-is-real-work note recurs (e.g. unit-01 line ~? in the 1.2 close, "that difficulty is doing real work"). Keep the front-matter instance; compress the per-lesson echoes.

### R11. Cross-references and any surviving tutor-meta inside explanations → cut forward-refs, strip meta, ≤1 backward callback **[AGENT]**

- **Watch for:** forward-references ("returns in 12.5," "full treatment in 5.6") embedded in the sentence teaching a new idea; any internal file ref (`misconceptions.md`, `metaphors.md`, `§N`), machine anchor IDs surfaced in prose, or tutor imperatives ("Have them…," "Front-load…") that slipped through the student copy.
- **Do instead:** remove forward-references from the explanatory body — they preview difficulty the reader hasn't met. Keep at most **one** load-reducing *backward* callback as a brief plain aside ("remember the rate from earlier"). Strip every internal file citation and tutor imperative on sight (framework §7). The student copies are mostly clean already; treat any leak as a defect to fix, not the dominant job.
- **Verified instance:** unit-12 line 102 teaching prose says the k<0 branch "comes straight back in Lesson 12.5" and line 115 "returns in 12.5 as the discriminant's sign" — keep the branch (R3), but cut the forward-reference from the teaching sentence.

### R12. Saying one idea three or four times → keep the strongest placement, thin the rest **[AGENT]**

- **Watch for:** the same point taught in the prose **and** New-terms **and** a worked example **and** the answer-key note.
- **Do instead:** keep the single strongest placement (the worked example for a procedure, the prose for a concept) and thin the rest. **Thinning must not delete a correct distinction** (see the §3a/§3b warnings: keep "value not spelling" and at least one "looks-irrational-but-isn't" / "looks-fraction-but-is-an-integer" example).
- **Verified instance:** "value, not spelling" recurs across Lesson 1.2 — prose (line ~?), worked example 3 (`10/2 = 5`) and 6 (`√9 = 3`), the check (`{#1.2.c2}`, `12/3`), and the answer-key note. Keep the worked examples (they carry it best) and the one prose statement; compress the echoes. Do **not** cut the `√9 = 3` and `10/2 = 5` cases — they are the load-bearing correct distinction.

---

## 3. Concept-specific simpler approaches for the hard intros

The three highest-leverage intros, grounded in the open-source consensus. Each follows the §4 four-beat order; that order is stated once in §4 and referenced here.

### 3a. The number line and the number system (Lesson 1.2) **[AGENT]**

The open-source pattern is unanimous and the opposite of the current opening: **picture first, taxonomy second, hardest member last and lightest.** The current source (unit-01) names four number types in a dense paragraph at line 108 *before* drawing the line at line 112, and runs "nested boxes" against the line.

- **Lead with the picture, empty then populated.** Open with one sentence and a bare number line. Show whole numbers first; a second beat adds the negatives to the left of 0. Define the *line* before any "type." Keep the first picture minimal: no fractions, no π, no √2.
- **Then the one big idea, shown not stated: the gaps are full.** Add a single in-between point (3/4 between 0 and 1, or 0.5) and say "the in-between points are numbers too." Show one instance *before* naming "rational." Do **not** demote density to a throwaway aside — it is the load-bearing idea (algebra lives on the *whole* line). Make the follow-up a real sentence: "every gap is packed with numbers, no matter how far you zoom in."
- **Layer the types as a short plain ladder that grows the same picture:** counting → add 0 and negatives = integers → the gap-fillers you can write as a fraction = rational (plain gloss first) → a few famous gap points you *can't* write as a fraction, like π = irrational (one sentence, one example) → all points = real. Each rung adds to the same line.
- **Demote the formal definitions** into the New-terms box *after* the picture and ladder (the locked `{#1.2.d4}`–`{#1.2.d6}` stay verbatim; lead your prose with the friendly version).
- **Give irrationals a one-sentence cameo, not a section.** Keep √2 light here; it returns in Unit 12. **Newly added, watch closely:** *irrational* and *real* (`{#1.2.d5}`, `{#1.2.d6}`) were added recently per the research/red-team handoff — treat them as fragile first-encounter material.
- **Pick one metaphor: the line.** Drop or strongly subordinate "nested boxes" (unit-01 line 108). If containment is wanted, express it *on the line* ("7 is a counting number and a whole number and an integer and rational").
- **Keep the type-from-value distinction intact** (R12): the rewrite must retain at least one "looks-irrational-but-isn't" (`√9 = 3`) and one "looks-fraction-but-is-an-integer" (`10/2 = 5`) example. Don't let "value not spelling" collapse to a slogan with no example.
- **Keep the forward hook as the closing payoff:** end on "2x = 7 → 3.5 is a real point halfway between 3 and 4" (framework §5, "A non-whole answer feels wrong," is the approved phrasing).

### 3b. Order of operations / PEMDAS (Lesson 1.3) **[AGENT]**

- **Motivate before you state the rule.** Open with one expression worked two ways landing on two answers, so the rule arrives as the fix to a problem the reader just felt. The source already has the case (`2 + 3 × 4`); lead with it: "Both used real arithmetic but got different answers. A written expression has to mean exactly one thing, so everyone agrees on one order." *Then* the list.
- **In the teaching prose, drop "tiers"/"shelves" and the abstract count.** Present a plain four-line list and let the grouping carry the idea:
  1. Parentheses and other grouping symbols
  2. Exponents
  3. Multiply and divide — equally important, done left to right
  4. Add and subtract — equally important, done left to right
- **Use the universal phrase** "equal priority / equally important, done left to right" (the wording framework §5 endorses) in your prose.
- **REMEMBER R6's locked-token carve-out:** the definition `{#1.3.d1}`, the recap at line 221, and the framework's §5 note keep "four tiers"/"[M.../D...]"/"ties" verbatim. You only plain-language the *teaching prose* around them.
- **Repair the mnemonic in place; don't tell the reader to abandon it.** Most adults know PEMDAS. Keep it and patch its one flaw by **stacking it vertically** (P / E / MD / AS) so the bottom two pairs visibly read left to right.
- **Anchor "left to right" to reading:** "within the bottom two lines, work in reading order, the way you read a sentence."
- **Introduce the fraction bar as grouping with one plain line** and cut the duplicate fraction-bar mentions (R12).

### 3c. The equals sign, variables, expressions-vs-equations (Lesson 1.1) **[AGENT]**

- **Lead with one plain sentence for "=," then the metaphor.** Define "=" in words first ("the two sides have the *same value*") *before* the balance scale appears. The current source (unit-01 line 19) introduces the plain meaning and the metaphor in the same breath; separate them so the picture supports a meaning the reader already has.
- **Commit to one image for "=" and stay in it.** Use the balance scale as the single supporting picture and walk back to symbols cleanly. Honor the leak point from R1 (valid for +, −, and scaling by a positive).
- **Choose one variable metaphor for 1.1: the mystery box** (it pairs with the scale — a covered weight on a pan; framework §4 "Variable" row). Keep its first-contact definition to one clause; add "every copy of the same letter holds the same number" and "it's a number, not an object" at the moment they bite (when `5x` or `3x` appears), not in the opening definition. **Retire the reserved-seat image from 1.1** — it earns its keep in 1.5 (framework §4 "Evaluating at a value" row).
- **Teach one solving method: "undo with the opposite"** (R9); show inspection as a quick check after.
- **Frame "=" via the phrase/sentence contrast in plain words** (R7) so "=" reads as the verb of a sentence — without using the term "expression."
- **Fix the first-example trap by prose framing** (R8): work the clean `x + 3 = 7` in the teaching prose before the worked block, so the `8 + 4 = □ + 5` worked example reads as the deliberate stress-test.

---

## 4. Required structure for a concept intro (the four-beat order — stated here once)

This is the framework's three-beat arc (§3 "How to TEACH") made explicit for simplicity. Every first-encounter concept follows it; §3a/§3b/§3c above just apply it.

1. **Simplest idea first** — one plain sentence, or one concrete number/picture the reader already understands. For a symbol, state its plain-language meaning here, before any metaphor. No abstraction with nothing under it.
2. **One consistent metaphor** — a single image from the framework §4 playbook, targeting *this* confusion. Open with the physical object before any x; do the real math on it; walk back to symbols; if you must switch pictures, mark the handoff and name the leak.
3. **Then the bullet-point detail** — once the reader has the idea and the picture, layer the parallel pieces (types, cases, steps) as a short list or small table, one new thing per beat, easiest to hardest, hardest last and lightest.
4. **Then the symbols** — formal definition, notation, `$$` blocks come *after* the friendly version. Plain gloss first, formal notation second.

**The abstract takeaway comes after a concrete instance, never before it.** The single most useful rule of a lesson ("value not spelling," "a term carries its sign," "distribute to everyone") is *earned* by a worked example, then stated once as the payoff — not announced at the top.

**Reassurance is load-bearing, keep it.** A strange answer (3.5, −5, "no solution," √7) arrives already reassured, placed as the payoff after the reader sees why it's true (framework §1, §5).

---

## 5. Where "common mistake" notes belong (stated here once; R4 points here)

Full rules live in framework §5. The simplicity-critical points:

- **After a clean success at the plain case** — never in the opening breath of a new idea, never in the first sentence; at most one named slip per concept introduction (framework §4, §5). Let the reader win once before you name the trap.
- **In a "common mix-up" note in the reader's voice, in surrounding prose — not inside a worked example's steps** (R4). Shape: **name the mix-up as a sensible misreading → show the short concrete *why* → hand over a self-check.** Show, then state.
- **At the fork where the reader chooses,** worded like a trail sign at the exact spot, not an alarm back at the trailhead. Suppress a pre-emption until the trap is reachable.
- **Inside a worked step, only a terse ≤8-word method tag is allowed** ("dividing by a negative, so the sign flips"). Everything longer moves out, counter-safely.
- **Vary the opener** (framework §5, §8): rotate "It's tempting to…," "Most people's first instinct here is…," "On a calculator this would be…." No single softener opens more than one mix-up per lesson; apply the swap test.
- **Tone:** frame the slip as reasonable with its cause named; no "Warning," no "Be careful," no ranking the reader; say "goes to zero / goes to one," never "cancel"; end on the symbolic move the reader will write.

---

## 6. Three BEFORE → AFTER exemplars (cleaned to pass framework §8)

These rewrite the **openings** of 1.1/1.2/1.3 the simplest way. They are models of register and sequencing. **Each AFTER replaces only the stated source line range; the surrounding locked content above and below stays byte-for-byte.** All three honor framework §9: no number, worked example, answer, title, bold label, or `{#…}` anchor is altered; the numbered worked-example lists keep their exact count and order; approved phrasings are pulled from framework §4/§5.

### Exemplar 1 — Lesson 1.1 opening (the equals sign)

**Replaces unit-01-foundations.md lines 19–23 only.** Line 17 — the framework's locked calibration-target opener, "You already know how to work with numbers. Algebra adds just one new idea…" (framework §0, lines 163–169) — stays exactly as is, directly above this. The New-terms box and the numbered worked-example list (`1.1.w1…`) below stay untouched.

**BEFORE** (lines 19–23, verbatim):

> Start with the equals sign, because almost everything ahead leans on reading it the right way. It's tempting to read "=" as "now write the answer." It actually means "the same as": picture a balance scale, with both sides level.
>
> Here's that picture in full. Imagine an old balance scale with two pans. On the left pan you put 8 coins and 4 more; on the right pan, some coins and 5 more. For the scale to rest level, the two pans have to weigh the same.
>
> The left pan holds 12, so the right pan also has to come to 12. That means the unknown pile holds 7. You didn't "compute" anything off to the side; you asked what keeps the two sides equal. That's what the equals sign is really about.

*What's too complex:* plain meaning and metaphor arrive in the same breath; "8 coins and 4 more… some coins and 5 more" is the hard both-sides-with-operations case as *first* contact; "compute… off to the side" gestures at the misconception before any clean success.

**AFTER:**

> Start with the equals sign, because almost everything ahead leans on reading it the right way. The equals sign means the same value: whatever is on the left is worth exactly what's on the right.
>
> Here's a picture for it. Imagine an old balance scale with two pans. If the two pans rest level, the weights on them are equal; that's all "=" claims, that the two sides weigh the same.
>
> So read x + 3 = 7 as that scale resting level: the left pan holds x and 3, the right pan holds 7, and they balance. Here is the one rule to remember: whatever you do to one pan, you do to the other, or it tips.

*Why:* plain meaning first (R6, §4 beat 1); one image, stated cleanly and committed to (R1); the clean single-unknown case `x + 3 = 7` as first contact instead of the both-sides trap (R8). The "compute here" mix-up is **not** here — it moves to a "common mix-up" note after worked example 1, using the framework's approved line (§5, §7 line 392): *"It's natural to compute 8 + 4 and write 12, or 9, in the box; that's the calculator habit. But the box plus 5 has to balance 12, so the box holds 7."* "Here is the one rule to remember…" is the framework's own approved balance-scale phrasing (§4 table, "=" row), reworded to a plain sentence rather than a colon-fragment.

### Exemplar 2 — Lesson 1.2 opening (the number system)

**Replaces unit-01-foundations.md lines 106–114 only.** The `**New terms:**` box (`{#1.2.d1}…d7`), the worked examples, and the answer key below stay verbatim. The single figure anchor `{#1.2.f1}` stays in this lesson (see §7 for its placement and the figure-owner fix).

**BEFORE** (lines 106–114, condensed):

> When you solve 2x = 7 later on, the answer is 3.5. […] This lesson lays out the kinds of numbers there are and puts them all on one picture […].
>
> Think of the kinds of numbers as nested boxes, each one bigger than the last. Start with the **counting numbers**: 1, 2, 3 […]. Toss in 0 and you have the **whole numbers**. Add the negatives […] and you have the **integers** […]. Allow ratios next […] and you reach the **rational numbers**.
>
> Each box sits inside the next […].
>
> The picture that holds all of this is the number line. […] between any two ticks there are infinitely many more numbers. The values 3/4, 2.5, and 0.333… all live in the gaps […] {#1.2.f1}.

*What's too complex:* two competing organizing images (nested boxes vs the line); four number types dumped before any picture; "infinitely many" asserted as a bold abstract fact; the picture arrives third.

**AFTER:**

> When you solve 2x = 7 later on, the answer is 3.5. The instinct is to assume you slipped. You didn't; 3.5 is a real, ordinary number. To see why, start with one picture that holds every number you'll meet: the number line.
>
> Draw a straight line and mark 0 in the middle. The counting numbers (1, 2, 3, and so on, the ones you'd use to count apples) step off to the right. Their negatives, the mirror image on the other side of 0, step off to the left. Every number you'll meet lives somewhere on this one line {#1.2.f1}.
>
> The line is not only the evenly spaced ticks. Look between two ticks, say between 0 and 1, and there are more numbers sitting in the gap: 3/4 lands there, and so does 0.5. The in-between points are numbers too, and every gap is packed with them, no matter how far you zoom in.

*Why:* the line is the single image, stated first and committed to (R1, R2); negatives are layered as the second beat, not dumped (3a); the "gaps are full" idea is **shown** with one concrete point first, and density is kept as a real sentence rather than demoted to a throwaway (3a). "You didn't; 3.5 is a real, ordinary number" is a genuine misconception repair (framework §5, "A non-whole answer feels wrong" — approved phrasing), allowed by §8's corrective-contrast exception. The single figure anchor `{#1.2.f1}` is reused on the "every number lives on this line" sentence — **do not invent a second anchor.** The type names (rational, irrational, real) then follow as the short plain ladder (3a), with the locked New-terms definitions verbatim afterward; the 3.5 reassurance returns as the closing payoff.

### Exemplar 3 — Lesson 1.3 opening (order of operations)

**Replaces unit-01-foundations.md lines 183–187 only.** The New-terms definition `{#1.3.d1}` (which keeps "four tiers" and the [M.../D...] brackets **verbatim**), the recap, and the numbered worked examples below stay untouched.

**BEFORE** (lines 183–187, condensed):

> When two people read 2 + 3 × 4, they need to land on the same value […]. Order of operations is just the shared agreement that makes that happen. […]
>
> There's a common memory hook for this order, the word PEMDAS. It's a fine reminder, but it's misleading in one way: it reads like six ranked steps when it's really **four tiers**, and two of the tiers are ties.
>
> Picture four shelves, top to bottom. The top shelf is **grouping** […]. Then one shelf shared by **multiply and divide** as equal partners. Then one shelf shared by **add and subtract**, also equal partners. You work the top shelf first; within a shared shelf you go left to right.

*What's too complex:* the rule is stated cold, no two-answers motivation; "four tiers, and two of the tiers are ties" leads with an abstract count before any example (R3); "shelf"/"tier" is a house coinage layered on the math (R6).

**AFTER:**

> Read 2 + 3 × 4 two different ways and you get two different answers. Add first: 2 + 3 is 5, then 5 × 4 is 20. Multiply first: 3 × 4 is 12, then 2 + 12 is 14. Both used real arithmetic, but they can't both be right, because a written expression has to mean exactly one thing. So everyone agrees on one order to read it in, and that agreement is the order of operations.
>
> Here's the order, top to bottom:
>
> 1. Parentheses and other grouping symbols
> 2. Exponents
> 3. Multiply and divide, equally important, done left to right
> 4. Add and subtract, equally important, done left to right
>
> Within the bottom two lines you work in reading order, left to right, the way you read a sentence. Multiply and divide aren't ranked against each other; they're equal, so you just take them in the order they come. Same for add and subtract. If you already know PEMDAS, you can keep it; just write it stacked, with MD on one line and AS on the next, so each of those pairs is read left to right.

*Why:* motivate-then-state, two-answers case first (3b, R3); a plain four-line list with the pairing visible, no "tier"/"shelf" jargon in the prose (R6); "equally important… left to right" in the universal wording; PEMDAS *repaired in place* by stacking, not replaced (3b). The note that "lines 3 and 4 are the ones that trip people" is **left out** of the opener — naming a trap before the reader has tried it primes anxiety (framework §4/§5; suppress the trap until reachable); the correct reading is simply modeled, and any caution moves to a post-success mix-up note. The locked definition `{#1.3.d1}` (with "four tiers" and the brackets) and the numbered worked examples follow unchanged; trim duplicate fraction-bar mentions per R12.

---

## 7. Image guidance (which concepts want a visual)

**Hard rule (framework §7, `figure_lint`, CI-enforced):** the prose pass may **only relocate an existing `{#…fK}` anchor** onto a natural student sentence **within the same lesson**. You may **never invent, duplicate, or delete** a figure anchor; the figure renders immediately after the line containing its anchor. If a lesson has no anchor, it gets no figure from this pass — **[FLAG]** it to the orchestrator/figure owner, don't create one.

**The figure mechanism (so you don't desync anything):** the `{#…fK}` anchor in the `.md` is what the build keys the figure to; the SVG itself lives under `algebra-1-tutor/figures/<code>.svg` and is emitted into the build. A prose agent working in `textbook-src/` cannot and must not edit the SVG. Relocating an anchor within its lesson is safe; **re-rendering a figure's content is a figure-owner task — [FLAG] it.** The authority is `_verification/` (figure_lint / build); there is no separate "R2 pipeline."

**Figures must demonstrate the lesson's actual point.** If the concept is "points between the ticks," the figure must plot points between the ticks.

### Verified per-lesson figure-anchor inventory (use this; don't re-derive)

Determined by grepping every `textbook-src/*.md`. **Relocate-only** where an anchor exists; **flag-only** everywhere else.

| Lesson | Anchor(s) present | Action |
|---|---|---|
| 1.2 | `{#1.2.f1}` (line 112) | relocate within 1.2; **content fix needed — flag (below)** |
| 4.3 | `{#4.3.f1}`, `{#4.3.f2}` | relocate within 4.3 |
| 5.2 | `{#5.2.f1}` | relocate within 5.2 |
| 5.3 | `{#5.3.f1}` | relocate within 5.3 |
| 5.4 | `{#5.4.f1}` | relocate within 5.4 |
| 5.6 | `{#5.6.f1}` | relocate within 5.6 |
| 8.1 | `{#8.1.f1}` | relocate within 8.1 |
| 8.3 | `{#8.3.f1}` | relocate within 8.3 |
| 8.4 | `{#8.4.f1}` | relocate within 8.4 |
| 12.6 | `{#12.6.f1}` | relocate within 12.6 |
| A.2 | `{#A.2.f1}` | relocate within A.2 |
| **Flag-only (NO anchor)** | — | **all of Units 2, 3, 6, 7, 9, 10, 11**, plus lessons **1.1, 5.1, 5.5, 8.2, 12.1–12.5** |

### Priority actions

- **FIX-EXISTING figure content, high priority — Lesson 1.2, `{#1.2.f1}` [FLAG to figure owner]:** the bundled SVG (`algebra-1-tutor/figures/1.2.f1.svg`) is **confirmed wrong** — it plots a single red dot at `cx=230`, which is exactly the integer tick labeled "3", contradicting the prose that promises 3/4, 2.5, 0.333… *in the gaps.* It must be re-rendered to show in-between points (e.g. 3/4, 2.5, −2.5) visibly between integer ticks. Prose agent: relocate the anchor onto the "every number lives on this line / gaps are packed" sentence (Exemplar 2). The SVG re-render is the figure owner's job.
- **FLAG — Lesson 1.1 balance scale:** there is **no anchor in 1.1** (confirmed). A clean two-pan scale (left `x + 3`, right `7`, level), with a matched second frame removing the same amount from both pans, would let the prose lean on a picture. Adding an anchor is an SSOT/orchestrator decision — flag it, don't create it.
- **FLAG — Lesson 1.2 on-ramp set:** a bare whole-number line 0–5, then the same line extended with negatives, then a zoom showing one fraction between two ticks; optionally a capstone nested-set chart at the *end* as a summary.
- **FLAG — Lesson 1.3:** the four-line list rendered as a small vertical-stack graphic with MD on one line and AS on one line, each marked "left to right."

Concepts elsewhere that most want a visual (relocate if the lesson has an anchor per the table; otherwise flag): negatives as two-color counters with a circled "neutral pair = 0" (1.4); opposites/absolute value as equal distances from 0 (1.4 — **newly added content, watch closely**, and the 8.3 V-graph anchor exists); the coordinate plane with quadrant signs (5.1 — **no anchor, flag**); rise/run right triangles for positive- and negative-slope (5.3 — anchor exists); the function machine input → rule → output (4.x — 4.3 anchors exist); open- vs filled-circle on a number line (8.1 — anchor exists); the half-plane boundary with a marked test point and shaded side (8.4 — anchor exists); the area-model box for distributing and factoring-run-backward (keep FOIL arrows out); a parabola with dashed axis of symmetry, vertex, and two roots (12.6 — anchor exists); straight-vs-bending curves for linear vs exponential growth (9.2 — **no anchor, flag**).

---

## Quick reference card (pin this)

| # | Tag | Watch for | Do instead |
|---|---|---|---|
| R1 | A | Two+ images / dropped or drifting metaphor | One playbook image to the end; mark any handoff. Scale leaks **only** at ×/÷ by a negative — keep it for +, −, and ×/÷ by a positive |
| R2 | A | Definition dump / philosophy essay before a handhold | One concrete handhold first; synthesis at the end |
| R3 | A | Over-hedged rule, "X tiers, Y ties" before an example | Simplest case first → use it → edge cases later. **But defer PLACEMENT, never PRESENCE of a correctness guard** (k<0; discriminant<0; the three abs-value k-guards) |
| R4 | A | Error note inside a worked step | Clean solution; mix-up note after, in prose (counter-safe; know if your unit's examples are coded) |
| R5 | A | Parallel items as a run-on paragraph | **Prose is default**; list only a genuine parallel set; connected reasoning stays prose |
| R6 | A | House coinages, formal-before-gloss, packed definitions | Plain field-standard phrase in **prose**; plain gloss first. **Locked: "four tiers"/[M.../D...] in `{#1.3.d1}`, `{#1.2.d4}` — reword prose only, never the definition** |
| R7 | A + FLAG | Expression defined apart from equation | [A] In 1.1, frame "=" as a sentence's verb in plain words (don't use "expression"); [FLAG] resequencing term scope |
| R8 | A | First worked example is the trap | Supply the clean case in **prose before** the worked block (can't reorder the list) |
| R9 | A | Two methods at once | Teach the scaling one alone ("undo with the opposite"); alternative as a check |
| R10 | A | Repeated motivational boilerplate | Once per unit (front matter); compress repeats (swap test) |
| R11 | A | Forward-refs / leaked tutor-meta in explanations | Cut forward-refs; ≤1 backward callback; strip any internal file ref/imperative |
| R12 | A | Same idea taught 3–4 times | Keep the strongest placement; thin the rest — **without deleting a correct distinction** (`√9=3`, `10/2=5`) |

**Where you edit:** read `algebra-1-tutor/references/units/unit-NN-*.md`; write `textbook-src/<same name>`; run `python _verification/check_textbook_src.py <UNIT>` then the §9 gate. **Never edit the tutor original or any `_verification/` script.**

**Two lines never to cross (framework §9):** never alter math, worked examples, answers, titles, bold labels, New-terms definitions, or `{#…}` anchors; never renumber/reorder worked examples or start a relocated note with `**` or a new `N.` line. **CI will not catch a math edit — your eyes are the only guard.** When simplicity and the math/structure conflict, the math and structure win; find another way to be kind.
