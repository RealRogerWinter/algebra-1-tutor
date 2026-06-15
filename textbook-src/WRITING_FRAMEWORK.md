# Pedagogic Writing Framework — Algebra 1 Student Textbook

This is the operative house-style sheet. Thirteen authors, one each on a unit, follow it so the finished book reads as one book. It governs voice, lesson shape, metaphors, misconception prose, notation, what to cut, the self-applied copyedit pass, and the rules that keep the verified math from drifting. Read it once in full before you write a line; keep it open while you write.

One test sits behind everything here: **could a nervous adult, alone at a kitchen table with no one to ask, read this passage and come away understanding the idea AND feeling calmer than before?** If not, it isn't done.

Two warnings before anything else, because they are the two ways this book can quietly break:

- **The math, the anchors, and the structural labels are load-bearing for an automated build.** Changing them, or reformatting around them, can silently delete deep links or ship wrong math with a green build. §3, §6, and §9 give the exact rules. Follow them literally.
- **This framework is written in bullets and tables for authors. The textbook is written in connected prose for a reader.** Do not mistake the form of this document for the target voice. Student copy is paragraphs; reserve bullets for genuinely parallel items (a short list of steps, a set of terms).

---

## 0. Scope, precedence, and who writes what

**Precedence.** For the student-textbook pass, this framework is the governing document. There is an older guide, `_verification/AUTHOR_GUIDE.md`, that tells authors to write the unit files *for the AI tutor* and to keep tutor meta and cross-references. That guide describes the original purpose of these files; for the textbook rewrite it is superseded by this framework wherever they conflict. Keep using `AUTHOR_GUIDE.md` only for the mechanics it documents that this framework also relies on: the reference-code grammar, the `unit-NN.json` schema, and the sympy answer-verification step.

**One file, two readers — confirm before you strip meta.** The textbook is generated from the same `algebra-1-tutor/references/units/*.md` files the tutor skill reads. So removing the tutor-facing meta (§7) changes what the tutor sees, and may affect the skill's tests. Before you begin, confirm with the orchestrator which of these is true for this pass:

1. the textbook builds from a **separate student copy** of the unit files (you edit the copy; the tutor keeps its meta), or
2. the tutor is being **retired from these files**, so editing them in place is intended.

Do not strip meta in place until that is settled. Everything else in this framework you can apply regardless.

**RESOLVED for this pass (orchestrator decision): option 1 — a SEPARATE student copy.** You create a brand-new file under `textbook-src/`; the tutor's `algebra-1-tutor/references/units/*.md` files are left untouched and keep their meta. Concretely: **READ** the tutor unit file as your input, and **WRITE** the rewritten student version to `C:/Users/18084/algebra-textbook-copy/textbook-src/<the identical filename>`. Strip the tutor meta (§7) freely in your student copy; never edit the tutor original. A deterministic guard, `_verification/check_textbook_src.py`, then verifies your student copy kept every SSOT-verified item (codes, lessons, answer keys) and leaked no tutor meta — run `python _verification/check_textbook_src.py <UNIT>` on your unit and fix until it passes. This replaces §9's `git diff`/global-build steps for this pass (your file is new, so there is no diff baseline, and the orchestrator runs the global build centrally).

**The 13 assignments.** Twelve numbered units plus one appendix:

- Units 1–12, one author each.
- The thirteenth is the statistics appendix, **Unit A** (lessons A.1, A.2, A.3; anchors like `{#A.1.d1}`). Use the `A` scope everywhere, not `13`. Unit A is an optional, lighter strand: prefer one brisk beat to the full three-beat treatment, matching its source, which says to keep it light.

---

## 1. Who we write for, and what success feels like

You are writing to one specific person. Picture them clearly.

A motivated adult, fluent in basic arithmetic — the four operations, simple fractions, simple decimals — who is meeting almost everything in algebra for the **first time**. Many carry math anxiety or a long history of feeling "bad at math." This book is their **primary, self-contained textbook**: they read it **alone**, with no tutor in the room. They are a capable adult, never a child.

**Success has two halves, and both are required.**

1. **They understand the idea.** Not "can mimic the steps" — understand. The test is that they can do a *variation*, not re-read the example. A reader who can only repeat the worked example doesn't understand yet; one who can handle a small change does.
2. **They feel calm, capable, and willing to keep going.** A reader who got the right answer but feels shaky and dreads the next page has not succeeded. Emotional state is a first-class outcome here, not a nicety.

What "calm, capable, willing to continue" reads like on the page:

- A strange answer (3.5, −5, "no solution," √7) arrives already reassured: the reader trusts it's real and correct, not a sign they slipped.
- A hard spot is named plainly and in passing, so the reader feels met, not caught or behind.
- The reader is never stranded: if one explanation doesn't land, a second angle is right there on the page, and there's honest permission to step away and come back.
- The reader always knows where they are and what each part of the page is for.
- The reader leaves a section owning the actual algebra, not just a story about a balance scale.

**Default to more scaffolding, not less.** Your reader is meeting this for the first time and is often anxious. The dominant risk for this audience is too *little* support. There is a real effect where extra scaffolding slows down an already-fluent reader, and §3 tells you to ration ceremony — but that caution applies to refreshers and to a move the reader has *demonstrably just used correctly*, not to anything new to them. The concrete test: go brisk only if the reader solved this exact move-type correctly within the last page or two; otherwise scaffold it. You are fluent in algebra and will systematically underestimate what feels new to a beginner. To this reader, x/2 = 6 (undo by multiplying) does not automatically feel like "the same move" as x + 5 = 12. When in doubt, teach it.

**Calibrate to the reader's energy across the lesson, not just to each concept.** A reader has a finite budget of focus and morale over a sitting. Spend the heavy, slow treatment on the genuinely hard idea of the lesson; let the easier surrounding material move lightly so there's budget left when it's needed. After a hard stretch, give something the reader can win at before the practice mixes things up (§3, "after a hard stretch"). "Brisk" is a tool for protecting that budget — but to an anxious reader, brisk can read as "the book assumes I already get this," which is its own quiet way of feeling behind. So pace for relief, not for speed.

---

## 2. The house voice

The voice is warm, patient, plain-spoken, and direct. You are a knowledgeable person sitting beside the reader, explaining plainly. Calm and understated, never cheerful-hype, never down to them. Honest over nice. **Lead with the idea, not with how important it is.**

This voice is a deliberate choice, grounded in how people learn. Writing to the reader as "you," in plain conversational language, improves understanding and transfer; it matches one-on-one tutoring, the format with the largest effect in this project's evidence base. Cutting decorative, hyped, and extraneous words helps learning rather than hurting it. Plain is not only kinder; it teaches better. (State this as direction, not as decimals — the project's verified research covers worked examples, interleaving, concreteness-fading, and tutoring; it does not contain personalization or coherence effect sizes, so do not cite numbers we can't back.)

### The one deliberate override

The generic copyedit standard bans second-person "you" and contractions. **For this learner-facing textbook, that ban is overridden.** Second-person "you," "we," and contractions (it's, don't, you'll, we're) are the intentional house voice. Run the full copyedit *discipline* — strip every AI tell — but with an **instructional-tutor target**, not the generic-prose target. Every other copyedit rule binds in full.

A note on "let's": prefer bare imperatives. The approved Lesson 1.1 sample says "Start with the equals sign," not "Let's start with." An occasional "let's" is allowed, but it drifts toward the cheerful register §2 warns against, so reach for the imperative first.

### DO / SAY

- **Write to "you," with contractions.** "You can subtract 3 from both sides." This is the house register.
- **Lead with the idea itself.** Open on the concept, not on a claim that it matters. If something genuinely matters, anchor it to a concrete payoff ("this is the move every later equation is built from"), never to abstract significance.
- **Be specific and concrete.** "Subtract 3 from both sides," not "manipulate the equation." Real numbers, the real undo-step, the actual reason.
- **Keep sentences short — one idea each.** Aim for roughly 15–20 words on average. One new idea per paragraph. Active voice: you do the thing.
- **Name the move before you make it.** "We undo the +5 first, because it's the outermost layer." Use plain connectives — first, next, because, so, notice — that expose the logic.
- **State a result and let it stand.** Let worked examples carry the weight. A plain "Correct" is the ceiling for praise.
- **Normalize difficulty in one understated line,** attached to a real difficulty, then move on (see §5).
- **Reframe nervous feelings as ordinary alertness** where a section is genuinely hard ("a bit of nervous energy here is normal, and it can sharpen your focus") — never "don't be nervous," never "relax."

### DON'T / AVOID

- **Don't lead with significance or hype.** No "this crucial, powerful concept," no "the single most important idea," no "the capstone where everything converges."
- **Don't gush or hand out empty praise.** No "You're doing amazing," no "Great question," no "You've got this," no exclamation-point cheerleading. Never call a wrong result good.
- **Don't praise the person's ability.** No "you're so smart," no "you're a math person." Praise the *method*, only when earned ("checking by substituting is exactly the habit that catches errors").
- **Don't say "this is easy"** — it makes a stuck reader feel worse. Don't dismiss the feeling ("don't worry").
- **Don't compare or rank the reader.** No "most people find this easy," no "most people get this wrong," no "faster than your peers." You may call an *error* common (§5); you may not rank the *reader* against other people. Social comparison spikes anxiety even in capable readers.
- **Don't anthropomorphize the math** ("the equation wants to balance"). The person acts: "subtract 3 from both sides and the equation stays balanced."
- **Don't chop connected reasoning into a bullet avalanche,** and don't stack hedges ("this can sometimes occasionally fail" — pick one).
- **Don't patronize.** Don't re-explain what the reader already owns; don't pad with filler reassurance; don't over-confirm.

### The corrective-contrast exception

The copyedit standard bans the "It's not X, it's Y" fake-insight flip. A beginner genuinely needs certain corrective contrasts, and those are encouraged: "= doesn't mean *compute the answer here*; it means the two sides balance." That is a real misconception repair. The banned thing is the *hollow* flip used for fake profundity. When you write a contrast, make sure the X is a real, named misreading the reader actually holds.

---

## 3. The shape of a lesson

Every lesson uses the same small set of moves in the same order, so the reader learns the rhythm and always knows what each block is for. Consistent structure is itself a comfort, and it helps comprehension. Keep all required structural markers and verified items exactly intact while you do this (see §9).

### Mandatory structure to preserve, verbatim and in order

Do not remove, rename, reorder, or renumber any of these — the build depends on them:

- `# Unit N: Title` and `## Lesson N.M: Title` headers. **The title text is locked to the SSOT (`curriculum.yaml`) and is checked by the build (`generate.py`).** Reproduce it byte-for-byte, including any en-dash or punctuation. You may **not** warm up, reword, shorten, or add a subtitle to a unit or lesson title. Warmth goes in the prose under the header, never in the header. Never put an anchor on these header lines.
- The bold section labels the build keys on, reproduced verbatim:
  - `**New terms:**`
  - `**Worked examples:**`
  - `**Practice problems:**`
  - `**Answer key:**`
  - `**Check for understanding (transfer):**` — reproduce the whole label, including "(transfer)". Do not shorten it to "Check:" or warm it to "Check your understanding." (If the team wants a friendlier label, that's a separate one-time change across all 13 sources, not a per-author choice.)
- Every `{#...}` anchor: term anchors (`{#2.1.d1}`), figure anchors (`{#...f...}`), check anchors (`{#...c...}`).
- Every numbered worked example and practice item, with its sub-group labels, in its original count and order.

### How the build assigns deep-link codes (read this before you reformat anything)

The build turns certain items into linkable reference codes. The rule is mechanical and easy to break by accident:

- **Practice problems** are top-level numbered list items (`1. `, `2. `, …) under `**Practice problems:**`. Every one becomes a code by position. **Never add, drop, reorder, or renumber them** — doing so silently shifts every code after it.
- **Worked examples get a code ONLY when written as a top-level numbered list item (`1. `, `2. `, …) directly under `**Worked examples:**`.** Worked examples written as `$$` display blocks with italic labels (the form Units 2, 4, 6, 7, 8, 10, 11 currently use) receive **no** code, by design. Units 1, 3, 5, 9, 12, and A currently number theirs and do get codes.
- **What terminates the block for the counter:** any line that *starts* with `**` (a bold label at the start of a line) or with `## ` ends the worked/practice block. Items after such a line get no code.

These wK and practice codes are injected in memory at build time. They are **not** linted by any checker. You are the only safeguard.

**Counter-safe formatting — follow these literally inside a `**Worked examples:**` or `**Practice problems:**` block:**

1. **Do not start a line with `**bold**`.** It ends the block, so every numbered item after it loses its code. (Confirmed: a bold label on its own line mid-block dropped all later worked-example codes.) Put a purpose-label as an *inline* lead-in on the same line as the number instead — `2. **Make the coefficient 1:** divide both sides by 4…` — which is safe and is exactly how Unit 12.1 already does it.
2. **Do not begin a step or sub-line with `N. `** inside a worked example. The counter treats every `^\d+\. ` line as a new item, so numbering the steps of one example turns one example into several codes. (Confirmed: a 1-example, 4-substep block produced four codes.) Narrate steps with "first," "next," "then," "so," or arrow notation, never as a numbered sub-list.
3. **Keep exactly one top-level `N. ` line per worked example and per practice item.**
4. **Do not change a worked example between numbered-list form and `$$`-block form.** The form determines whether it gets a code. If your source numbers them, keep them numbered; if it uses `$$` blocks, keep that.

### Do not rewrite worked examples or practice into different containers

This collides with two prose instructions below, so be explicit: "present each worked example as reasoning narrated" (later in this section) means add a short *why* on the same line or in the prose **around** the item — it does **not** mean convert a `$$`-block example into a numbered list, or split one example into numbered steps. "Interleave and name it" (practice, below) means *prose* callbacks and a separate non-keyed review block (defined below) — it does **not** mean inserting a bold note that ends the practice block. When in doubt, leave the container exactly as the source has it and put your warmth in the surrounding prose.

### The canonical lesson skeleton (fixed order)

Within each lesson, keep the student-facing sections in this order so 13 lessons line up:

1. `## Lesson N.M: Title` (verbatim).
2. Warm opening prose: one to three short paragraphs, the idea grounded in something concrete (§ "How to OPEN").
3. Teaching prose: the three beats for each new idea (§ "How to TEACH").
4. `**New terms:**` (verbatim definitions + anchors; you may add teaching prose around them, never inside them).
5. `**Worked examples:**` and the items, in their original container form.
6. Misconception notes, placed inline at the fork where each bites — and after at least one clean success (§5).
7. Transfer prose leading into the check.
8. `**Check for understanding (transfer):**` (verbatim label + its `{#...c...}` anchors).
9. `**Practice problems:**` (verbatim, in order).
10. `**Answer key:**` (verbatim).

Some real units carry extra subsections — `### Fraction Refresher A/B` (Unit 2), a short word-problems strand (Unit 12), a quadratics reference, a "two valid solving orders" aside. **Preserve every such heading and its content; warm only the prose inside; never delete or reorder them.** Mark a clearly optional refresher as skippable for a confident reader (§ "Calibrate the ceremony"), but keep it on the page.

### How to OPEN a lesson

Open on the **idea**, grounded in something the reader can picture — never on a label, a bare definition, or a naked equation.

- Convert the source's `Goal:` / `Why it matters:` labels into flowing sentences. Don't print "Goal:". State the idea and its concrete payoff in prose.
- The first sentence or two should put a tangible thing in the reader's hands or mind (a balance scale, a covered cup and coins, money owed, a street map) before any symbol.
- If you flag that the lesson matters, tie it to a concrete payoff or a trap it saves them from, not "this is the most important lesson."

The approved opening for Lesson 1.1 is the calibration target for every opener:

> You already know how to work with numbers. Algebra adds just one new idea: sometimes a number is hidden, and we use a letter to stand for it until we track it down.
>
> Start with the equals sign, because almost everything ahead leans on reading it the right way. It's tempting to read "=" as "now write the answer." It actually means "the same as": picture a balance scale, with both sides level.

Notice it leads with capability and the idea, not with a trap. Do the same.

### How to TEACH a concept: the three-beat order

For each genuinely new or trap-prone idea, write three beats **in this fixed order**, with the transitions narrated in prose. This is concrete, then pictorial, then symbolic, rendered for a lone reader. Never let a symbol arrive cold.

1. **Concrete anchor.** One everyday, physical, picturable thing (covered cup and coins on a balance; money and debt; a vending machine; stairs). Let the reader form the image before any notation.
2. **Picture.** The same idea as a stripped-down, labeled picture, number line, or area box — described in words on the page (and, where a figure exists, with the figure). Plain and labeled, not a decorative cartoon.
3. **Symbols.** Introduce the notation as **shorthand for the thing they just pictured**, and say so. Write the sentence that connects the picture to the symbols ("Here's that same balance in symbols," "Those four cells *are* the four products").

Two disciplines on top of the three beats:

- **Thin the picture as you reach the symbols.** Once the symbols arrive, retire the concrete scaffold rather than repeating the full cartoon under every line. The picture is temporary support, not permanent furniture beside the algebra.
- **Calibrate the ceremony, with the default set toward support.** Give the full three beats to new or trap-laden ideas (the equals sign, negatives, distributing a negative, fractions, slope's sign-versus-steepness, the ± in quadratics — in practice, the ideas in the §4 metaphor table and the §5 catalog; treat those tables as the canonical list of "genuinely new or trap-prone"). For a routine extension of something the reader *just used correctly* on the previous page or two, one brisk beat is enough. The brisk path is the exception you justify, not the default; when unsure, give the fuller treatment.

**Definitions.** Define every genuinely new term the first time it appears, in plain everyday words, tied to the picture, *before* the formal phrasing — and never use a symbol or term the reader hasn't met. Don't re-define what's already established. The level to match: "a letter that stands in for a number we don't know yet (not a label for an object)."

Definitional imprecision was the single largest error category in the source audit, so get the honest definition right the first time. Watch these recurring ones the audit caught — reproduce the source's exact wording, and don't loosen it:

- a **function** assigns each input *exactly one* output (a pairing or correspondence, not a vague "rule");
- a **term** carries its own sign (the leading + or − belongs to it);
- a **solution** is a value that makes the equation a *true statement*;
- **like terms** share the same variable *and* the same power;
- **discrete vs. continuous** domain is a real distinction; don't blur it.

### How to PRESENT worked examples

Worked examples are the spine of the book. Present each as **reasoning narrated**, not a bare column of steps. Studying worked examples beats problem-solving for novices — but only if the reasoning is visible and the reader actually studies it. (Keep the item in its source container form; see the counter-safe rules above.)

Each worked example carries:

1. **The problem.**
2. **The goal and the reason,** in one line ("To get x by itself, we'll undo the +5 first, because it's the outermost layer").
3. **Every step with a short plain-language reason** — *you* supplying the why, on the same line or in the surrounding prose ("subtract 5 from both sides — that sends the +5 to zero"). Author-supplied why-lines belong on every step; that is what makes a worked example work. This is different from asking the *reader* to explain (see the self-explanation rule at the end of "How to FRAME practice"), which must be rationed.
4. **The check, inside the example, every time.** After x = 4, immediately show 2(4) + 5 = 13. The reader never sees an answer asserted without seeing how you know it's right. Teach the check by performing it every time, so it reads as the natural last move.
5. **A purpose phrase for each cluster of steps** when a solution has several stages — but as an *inline* lead-in on the numbered line ("Get the variable terms together," "Make the coefficient 1"), never as its own bold line (a bold line at the start of a line breaks the deep-link counter; see above). Purpose labels help transfer; just place them safely.

Two more rules:

- **Never collapse the arithmetic you're teaching.** Write f(2) = 3(2) − 1 = 6 − 1 = 5, never 3(2) − 1 = 5 in one jump. Skipping the 6 − 1 step undercuts the very habit ("substitute, then compute carefully") at the moment it's being taught.
- **Tell the reader to study, not skim,** at the first worked example of a hard idea: "Read each line and ask why it follows from the one above before you try the next one."

**When the check doesn't match.** This is the most important affective moment in the book, and it must be taught the *first* time you teach checking. The check is sold as the reader's safety net; a tutor-less reader whose check fails is exactly who can decide "I'm bad at this" and close the book. So the first time a lesson shows the substitution check, add a short, calm note in the reader's voice that covers two things: (1) a check that doesn't match is the safety net **working** — it caught something before it counted, which is a good outcome, not a verdict on you; and (2) a concrete, low-anxiety next move — "go back to your first step and re-run just the arithmetic; a mismatched check almost always means one sign or one subtraction slipped, not that the whole method was wrong." Reframe the failed check from judgment to tool. Model phrasing:

> If the two sides don't match, you haven't failed — your check just did its job and caught something. That's exactly what it's for. Go back to your first step and re-run the arithmetic slowly; a mismatch is almost always one sign or one small slip, not the whole method.

**Two valid methods, side by side.** Where two legitimate methods exist (distribute-first vs. divide-first; substitution vs. elimination; reciprocal vs. clearing fractions; slope from two points vs. from the equation), show both, confirm they reach the *same checked answer*, and state the rule for choosing the cleaner one ("divide first when the number divides the right side cleanly; distribute first when dividing would drag in a fraction"). Then tell the reader the choice is theirs — perceived control lowers anxiety, and choosing a strategy on purpose is one of the strongest recommendations in the evidence base.

**Spot-the-error, gated on a prior success.** Recurringly, you may present a plausible worked solution containing one planted, common mistake (drawn from §5) and ask the reader to find and explain the broken line before you show the fix and its substitution check. Two guardrails, both required for this audience:

- **Only after the reader has seen, and ideally done, the correct version of that exact skill.** A beginner who hasn't yet got the right answer can encode the wrong one or just feel newly unsure which of two things was true.
- **Show the correct line beside the broken one, simultaneously** — never wrong-first-then-reveal across a page turn. And if the reader can't spot it, that's fine: the next line shows it. Never leave a broken solution sitting as an unresolved puzzle.

Keep correct examples the default; use error examples deliberately, for misconception repair, not as the norm.

### How to FRAME practice

Stage the handover from reading to doing **on the page**. Don't dump 25 near-identical problems after one example.

- **Pair each worked example with an immediate near-twin to try** (the example then a problem just like it). That example-then-twin pair is the default unit of practice.
- **Fade the scaffolding across the sequence** (backward fading): a fully worked example, then a near-twin with only the **last** step left for the reader, then one with more steps open, then a fresh one solo. Peel from the last step first — backward fading is an evidence-supported gentle default that reliably beats jumping straight to a blank problem; for some procedures the faded-step position matters less than getting the reader to explain each step, so adapt to the skill. Keep a "check by substituting" line at every stage.
- **Build in retrieval, not just re-reading.** At least once per hard idea, tell the reader to cover the worked example and reproduce it from memory before checking. Recalling from memory teaches more than re-reading; it is one of the highest-value moves available to a read-alone reader.
- **End every concept boundary with a do-something transfer task,** never "does that make sense?" (there's no one to answer, and even live it gets a false yes). Use a near-twin to solve, a "why does this step work?" to put in words, or a one-change variation ("what changes if it's 2x − 5 = 13 instead?"). Make the answer reachable so the lone reader can self-check.
- **Give transfer tasks worked solutions, not just answers.** A bare answer can't repair a misreading; visible reasoning can. For each transfer task, provide a short reachable worked solution (the read-alone substitute for a tutor's hint), so a reader who got it wrong can see *where*.
- **Interleave, and say why — and point to the support in the same breath.** Mix old skills into new sets so consecutive problems need different first moves, and name the callback in plain English ("this one lands on a negative — a chance to keep your signed arithmetic sharp"). The mechanism that makes interleaving work is that the reader has to *choose* the method, so make sure consecutive review items genuinely need different first moves, not just different numbers. Tell the reader plainly that mixed, spaced practice feels harder on purpose and is exactly what makes a skill last to next week — **and in the same sentence, point to where the help is**, because for a reader with no tutor, "this is hard on purpose" can otherwise read as "so no help is coming." For example: "Mixed practice feels harder, and that's the point — it's what makes this stick. Every one of these has its answer at the end of the lesson, and if one stalls you, flip back to the worked example it's based on. That's what it's there for."
- **Place at most one self-explanation prompt** at the conceptual hinge of a procedure, and let it fade as fluency grows. Asking the reader "why?" on *every* step adds load and can erase the worked-example benefit; this is the opposite of the author-supplied why-lines in worked examples, which belong on every step.

**Delivering interleaving and spacing in a static book.** The highest-leverage practice technique is also the hardest for a book with no tutor to schedule it, and §9 forbids touching the keyed practice items. Two mechanisms that respect §9:

- You **may add a clearly labeled review block** — `### Mixed review` or `### Warm-up` — containing prose plus a few problems with answers, placed **outside** any `**Practice problems:**` block. These are not SSOT-counted items, so they don't touch the positional codes. Use them to build the cumulative, strategy-discriminating set the evidence calls for, where no two consecutive items share a first move.
- Because there is no tutor to schedule spacing, **give the reader the schedule in plain words**: at each unit opening, a short standing instruction like "before you start, redo two or three problems from a couple of lessons back from memory," and a cumulative review block every few lessons.

### Self-regulation, lightly

A self-study book is the right place for a little planning and self-monitoring, and it suits this adult audience. Model it in the reader's voice, with no jargon: before a multi-step problem, "before you start, name your plan in a sentence — what are you solving for, and what's the first move?"; and frame the check as the reader's own monitoring habit ("how will you know it's right? Put your answer back in"). Keep it to a line or two; don't turn it into a worksheet.

### How to CLOSE a lesson

Close on the last real point — no "By following these steps," no "The bottom line is," no "take your algebra to the next level." If a recap helps, write a brief, warm, second-person note of what the reader can now *do* ("You can now solve any one-step equation by undoing the operation and checking your answer by substituting it back") — concrete capability, not ceremony. Convert any tutor "Wrap-up & interleaving" note into this short recap, or cut it.

### After a hard stretch: a designed-in easy win

A live tutor watching a frustrated learner stops questioning and hands them a quick success to rebuild momentum. A book can't see frustration, so design the easy win in. After the genuinely hard idea of a lesson, offer one clean, confidence-restoring case the reader is very likely to get — a problem that lets the method click before the set turns mixed. Frame it honestly, by what it does, not "here's an easy one" (which condescends): "Here's a clean case to get the method moving before we mix things up." This is the structural stand-in for the tutor noticing a hard moment.

### When both explanations miss: honest permission to pause

Sometimes the concrete angle and the second angle (§4) both fail to land, and there's no human to escalate to. Give the reader an honest out rather than leaving them stuck and ashamed: plain permission to step away and return ("if this one still isn't landing, it's fine to leave it and come back tomorrow — a break genuinely helps, and you haven't lost anything"), and a pointer back to the most concrete version of the idea (the metaphor, the picture) as the thing to re-read first. This is not failure talk; it's what a steady tutor would say.

---

## 4. Metaphor playbook

These are the book's established metaphors. **Reuse these; don't invent new ones.** One image reused across units makes the reader feel a growing skill, not a pile of unrelated tricks, and keeps the textbook, tutor, and guides aligned. Lead with the metaphor that targets the *specific* confusion. For each hard idea, build a **second angle into the page** ("if that picture didn't click, here's another way to see it") so a stuck reader has somewhere to turn. Every metaphor leaks: state it, do the real math on it, walk back to the symbols, and name where it stops being exact when silence would mislead. Never strand the reader in the story.

**Let the reader succeed at the plain case before you name the trap.** The proactive warning belongs at the fork where the reader is about to choose — after one clean worked success, not in the concept's opening breath. At most one named "common slip" per concept introduction, and never in the first sentence of a new idea. And keep the superlatives off: "a slip that's easy to make here" carries the same warning as "the #1 sign trap" or "the most common slip in all of early algebra" without ranking the reader's expected failure. Naming an *error* as common is fine; ranking the *reader* is not (§2).

| Concept | Metaphor | Model phrasing (open here, then walk to symbols) |
|---|---|---|
| **What "=" means; solving** | Balance scale | "Picture an old balance scale with two pans. x + 3 = 5 is that scale resting level: the left pan holds x and 3, the right holds 5, and they weigh the same. The one rule that runs all of algebra: whatever you do to one pan, do to the other, or it tips." Leak to name: "This works for adding, subtracting, and splitting into equal groups, but there's no clean weight-picture for multiplying both sides by a negative — we'll switch pictures there rather than stretch this one until it lies." |
| **Order of undo-steps** | Getting dressed (socks then shoes) | "You put socks on, then shoes; to undo it you take the shoes off first. Building 2x + 3 means times-2 (sock), then +3 (shoe). So to get back to x, undo the last thing first: subtract 3, then divide by 2. Not a rule to memorize — just shoes before socks." |
| **Negatives: meaning, ordering, subtracting a negative** | Money and debt | "Think of a negative as a debt: −5 means you owe $5. Would you rather owe $5 or owe $2? Owing less leaves you better off, so −2 is the bigger number. And subtracting a negative is having a debt forgiven — wipe out a $2 debt and you're $2 richer, which is exactly why 6 − (−2) comes out to 8." |
| **Signed arithmetic (second angle)** | Walking the number line | "Stand on a number line facing right. A minus sign is an about-face. Subtracting a negative is two about-faces, so you end up facing right again — walking forward, which is adding." |
| **Variable** | Mystery box / reserved seat | "A letter isn't short for a thing like 'apples.' It's a closed box with a number hidden inside that we don't know yet. Every x in one problem holds the same hidden number, so 3x is three of that one box. If the box turns out to hold 6, then 3x is 18 — not 36 stuck together." |
| **Evaluating at a value** | The reserved guest sits down | "5x is five chairs reserved for one guest who hasn't arrived. 'Evaluate at x = 6' is the guest finally sitting down: every reserved seat is now a 6, so 5x is five 6s, which is 30." |
| **Function (one output per input)** | Vending machine | "A function is a vending machine: press a code, get exactly one item. Press B4 today and tomorrow, you get the same snack. Two buttons can dispense the same snack, but one button can't give two different things." Leak to name: "A real machine can be sold out; in math, the rule must give an output for every input it accepts." |
| **Function notation f(x)** | A recipe | "f(x) = 3x − 1 just names a recipe: 'triple it, then subtract one.' f(2) means run 2 through that recipe: triple to 6, subtract 1, land on 5. The letter in parentheses tells you which number you dropped in." |
| **Slope (all four cases, steepness)** | Stairs / ramp | "Slope is steepness: how far you rise for each step forward. A gentle ramp is a small slope, a steep staircase a big one, downhill is negative, a flat landing is zero, and a wall going straight up is undefined, because there's no 'forward' to divide by." |
| **Slope as rate of change** | Speed on a distance–time graph | "On a graph of distance against time, the slope *is* the speed — more miles per hour. Slope isn't new; it's the same 'so much for every one' as the unit rate you already know, read off a line." |
| **Distributing** | Hand a flyer to everyone | "The number outside the parentheses hands a flyer to everyone inside, skipping no one. In 3(x + 4), the 3 greets the x (3x) and the 4 (12), giving 3x + 12. The easy slip, 3x + 4, is walking past the second person." |
| **Distributing a negative** | A −1 shaking every hand | "It's tempting to write −x − 4 here. But the minus is a −1 that shakes hands with every term inside: it meets the x (−x) and it meets the −4 (and −1 times −4 is +4). So it's −x + 4." |
| **Distribution / binomials as area** | Garden plot / area box | "Picture a rectangle (x + 2) wide and (x + 3) tall, cut into four cells: x², 3x, 2x, 6. The two middle cells, 3x and 2x, are exactly the pieces people drop. Add all four: x² + 5x + 6." Prefer this box over the FOIL acronym — it shows *why* the middle term exists and keeps working on bigger problems. |
| **Binomials (second angle)** | Two rounds of flyers | "First x greets everyone in the second parentheses (x² and 3x), then 2 greets everyone (2x and 6). It's distributing, done twice." |
| **Factoring** | The area box, run backward | "Factoring is the same area box, backward: you're handed the finished area x² + 5x + 6 and asked to rebuild the edges. The key question: what two numbers multiply to 6 and add to 5? Those are your edges: (x + 2)(x + 3)." |
| **Factoring out a GCF** | Same item in every gift bag | "Every term is quietly carrying the same factor. In 6x + 9, both carry a 3, so set it out front: 3(2x + 3). Multiply back to check nothing was lost." |
| **Two solutions / the ±** | Squaring loses the sign | "Squaring is forgetful: 3² = 9 and (−3)² = 9, so squaring throws away whether you started positive or negative. Undoing a square has to allow for both: x = 3 or x = −3. The ± is just recovering what squaring erased." |
| **How many solutions (second angle)** | Parabola crossing the axis | "A quadratic draws a U. The solutions are where it crosses the x-axis — usually twice, once down and once back up. It touches once if the U just kisses the axis, and never if the whole U floats clear of it." |

**Metaphor deployment rules (apply to every one above):**

- Open with the physical object before any x appears.
- Let one plain rhetorical question carry the insight ("Would you rather owe $5 or owe $2?"). One question, not a stack.
- Finish by working the actual algebra through, with the picture as support you can drop.
- Recast a memorized "rule" as the only sensible outcome of the picture (two about-faces make subtracting-a-negative obviously move you right).
- Frame the famous error as a natural, common slip — "a slip that's easy to make here" — and place it after a clean success, not in the opening line.
- Hand over a self-check the metaphor supplies (multiply the GCF back out; substitute x = 1 to catch a dropped sign).
- These table cells are compressed. When you expand a metaphor into running prose, hold to at most one em-dash per paragraph and at most one rule-of-three per page (§8). Don't treat the dense cells as the prose target.

---

## 5. Pre-empting misconceptions, in calm prose

There's no tutor to diagnose a wrong answer, so the book surfaces the known trap **proactively, right where it bites** — worded like a trail sign at the exact fork, not an alarm back at the trailhead, and placed **after the reader has had one clean success at the plain case** (§4). The pattern is always: **name the mix-up as a sensible misreading, show the short concrete *why* of the right reading (so the reader can re-run it), hand over a self-check.** Show, then state.

**Cap the trap density.** A page that warns of a way to fail attached to every new idea teaches fear along with math. At most one named "common slip" per concept introduction; never in the first sentence of a new idea; and suppress a pre-emption entirely until the trap is actually reachable for the reader.

**Vary the opener — don't template the warmth.** "It's tempting to…" is one option among several, not the house formula. Rotate: "Most people's first instinct here is…", "On a calculator this would be…", "You'd expect this to get smaller — it actually…", "It's easy to read this as…". No single softener should open more than one misconception in a lesson. The self-check: if you could swap the first five words of any two misconception notes without noticing, the warmth has gone templated, which reads as the book *managing* the reader rather than talking to them. Real warmth varies.

**Tone and language rules for every misconception note:**

- Frame the slip as reasonable, with its cause named ("on a calculator, = really does mean compute, so it's natural to…"). The reader must feel met, never caught or foolish.
- Keep it brief and matter-of-fact. State the mix-up in one breath, the why in the next. No "Warning," no "Be careful," no "a lot of people get this WRONG," no emoji, no check or cross marks.
- Never just assert the rule — a rule with no reason is exactly what these mix-ups come from.
- Say a term **"goes to zero"** (+/−) or **"goes to one"** (×/÷), **never "cancel."** Apply this everywhere it's needed — clearing an equation, factoring, multiplying binomials — not just once.
- Separate the **operation sign** from the **number's sign** in words when a negative is in play; separate **distance from zero** (always ≥ 0) from **value** (can be negative) for negatives and slope.
- End on the symbolic move the reader will actually write.

**The catalog of pre-emptions** (lead each with the matching metaphor from §4; place each after a clean success at the plain case):

- **Equals sign as "compute here."** "It's tempting to read = as a button that means *the answer goes next* — that's how a calculator works. Here it means something steadier: the two sides weigh the same. So in 8 + 4 = □ + 5, the right side has to balance 12, which makes the box 7, not 9." Self-check: if you catch yourself writing the running total in the blank, that's the calculator habit — come back to the scale.
- **Letter as object / 5y read as "56."** "A letter isn't a label like 'apples' — it's a number you don't know yet. 5y means five of whatever the box holds, so if it holds 6, 5y is 30, not 56." Self-check: read every letter aloud as "some number."
- **Adding two negatives makes a positive.** "The rule *two negatives make a positive* belongs to multiplying, not adding. Owing $3 and then owing $5 more leaves you owing $8: −3 + (−5) = −8."
- **Subtracting a negative makes it smaller.** "Subtracting a negative looks like it should shrink a number, so 6 − (−2) tempts everyone toward 4. But taking away a $2 debt leaves you $2 richer, so it climbs to 8."
- **Ordering negatives (−5 vs −2).** "With negatives, the bigger digit is the smaller number. Owing $5 is worse off than owing $2, so −5 is less than −2; the 5 only says how far from zero, not which side."
- **−3² vs (−3)².** "Watch where the negative sits. (−3)² squares the whole −3, giving +9. −3² squares only the 3 and leaves the minus out front, giving −9." Read aloud as "the quantity negative three, squared" vs "the negative of three squared."
- **Order of operations as six ranks.** "PEMDAS reads like six steps, but it's really four tiers, and two of them are ties: multiply and divide are equal partners, and so are add and subtract. So 8 − 3 + 2 goes left to right: 8 − 3 is 5, then + 2 is 7." Frame the only question as "which comes first, reading left to right?"
- **Fractions: bigger bottom means bigger; reducing shrinks; adding across.** "Split one pizza among 6 people instead of 4 — whose slice is smaller? That's why 1/6 is less than 1/4, even though 6 is the bigger number." Reducing: "6/8 and 3/4 mark the same spot on the number line; you've just renamed it." Adding across: "You can only add same-sized pieces — rename to sixths first." Self-check: place the answer between the nearest whole numbers and ask whether its size makes sense.
- **A non-whole answer feels wrong.** "When you solve 2x = 7 and land on 3.5, the instinct is to assume you slipped. You didn't — 3.5 is a real point on the line, halfway between 3 and 4. Algebra uses the whole line, gaps included." (√7 is exact the same way 1/3 is exact even though its decimal never stops.)
- **A number's type from how it's written.** "A fraction bar or a decimal point is just how a number is spelled, not what it is. 10/2 has the value 5, so it's an integer. Work out the value first, then classify."
- **Distributing to only the first term.** "It's easy to send the 3 to only the x. But it has to greet everyone inside, so 3(x + 4) is 3x + 12, not 3x + 4." Self-check: a quick head count — did the outside number reach every term?
- **Distributing a negative.** "It's tempting to write −x − 4. But the minus is a −1 meeting every term, and −1 times −4 is +4, so −(x − 4) is −x + 4." Self-check: substitute x = 1 — both readings should agree, and they disagree exactly where a sign went missing.
- **Combining unlike terms (3x + 2 = 5x).** "3x is three boxes; 2 is two loose coins. You can't fold loose coins into boxes, so 3x + 2 just stays 3x + 2. Only matching kinds combine: 3x and 2x make 5x."
- **Missing the middle term in binomials.** "Multiplying the fronts and backs and stopping drops terms. The area box has four cells, and the two middle ones, 3x and 2x, add to the 5x that's easy to lose: x² + 5x + 6."
- **Inequality sign-flip.** "Start with something plainly true: 2 < 3. Multiply both sides by −1 and you get −2 and −3 — but −2 is the *bigger* one, so the sign had to flip. That's the whole rule: multiplying or dividing both sides by a negative reverses < or >." Self-check: put a number from your answer back into the original; if it should fit and doesn't, a flip went missing. (Test x = 0 in −2x < 6: 0 < 6 is true, and 0 fits x > −3.)
- **Slope sign read as steepness.** "Slope packs two facts: the sign says which way the line tilts (minus is downhill), the size says how steep. So a slope of −3 is steeper than 2, because 3 is the bigger size — even though −3 is the smaller number. Strip the signs to compare steepness; bring them back to say uphill or downhill."
- **Two solutions to x² = 9.** "It's easy to write x = 3 and stop. But squaring hides the sign — both 3 and −3 square to 9 — so both are answers. Whenever you undo a square, expect two and write the ± to catch the one you'd otherwise miss."
- **"No real solution" feels like failure.** "Landing on *no real solution* isn't a dead end or a mistake — it's the honest answer, because no real number squares to a negative. You don't owe anyone a rounded decimal unless one is asked for."
- **The variable disappears.** "If the x's all vanish when you gather terms, that's not an error — read what's left. If it's true, like 4 = 4, every number works. If it's false, like 3 = 5, no number works. There's no x left to report, so don't write x = 0."
- **Setting a quadratic's factors equal to a nonzero number.** "The split-into-two-easy-equations trick only works when the product equals zero, because zero is the one value a product reaches only if one part is zero. Move everything to one side to get a 0 first."
- **When the check doesn't match (recovery, not a misconception).** Covered fully in §3 ("When the check doesn't match"). Teach it the first time you teach checking: a failed check is the safety net working, and the next move is to re-run the arithmetic from the first step, not to conclude the method was wrong. Keep it in the calm name-then-why-then-do shape used here.

---

## 6. Notation rules

These are strict. Wrong notation renders as raw broken backslashes for the reader, and some forms fail the build.

- **Real, standalone math goes in a `$$ … $$` display block on its own line** — multi-step solves, fractions, exponents, roots, the quadratic formula, area-model arrays.
- **Inline math (math inside a sentence) is plain-text Unicode:** x², x³, n⁵, x⁻², 2/3 and (2/3)x when multiplied, √12, ½, ±, ≤, ≥, ≠, ·, ×, →, −, π. Sample register: "To solve (2/3)x = 6, multiply both sides by 3/2, which gives x = 9."
- **Never emit `\( \)`, `\[ \]`, or single-dollar `$ … $`** for math, anywhere. This is the most common notation failure and has no exceptions. The notation checker (`check_notation.py`) flags these the moment they appear outside a `$$` block.
- **No backslash macros outside `$$` blocks.** `check_notation.py` flags *any* `\word` (for example `\checkmark`, `\frac`, `\times`) found in prose. Inside a `$$` block, LaTeX macros are fine. So keep all `\…` strictly inside `$$`.
- **Choose the display block by whether it aids reading, not by reflex.** Set-apart `$$` blocks are for genuinely multi-step or visually tangled work, where laying it out helps the reader follow. Keep the simplest one-line steps and quick checks (a single undo, "Check: 7 + 5 = 12") in the flow of the sentence as Unicode where it reads naturally. A page that turns every line of arithmetic into a centered monument re-creates the intimidating-textbook feel the warm prose is dissolving. (This never overrides the broken-backslash rule — it's about *which* math earns a display block, not how to typeset it.)
- **Promote any inline expression too tangled for clean Unicode** (stacked fractions, big radicals, the quadratic formula) into its own `$$ … $$` block rather than forcing ugly inline text.
- **Inside markdown table cells, use plain ASCII** (x^2, -3, 1/2) — Unicode superscripts and fraction glyphs can silently drop out in table renderers.
- **Currency is a bare `$` in prose** ("it costs $5"), kept well away from any `$$` block so it isn't misread.
- **No emoji, no decorative check or cross marks** (the ✓ ✗ family), in prose or inside math. To confirm correctness, write "Correct" or show the substitution that proves it. (Do not reach for `\checkmark` either — it's banned by house style and fails the notation checker if it lands in prose.)
- Use the minus sign − for negatives and subtraction in inline Unicode, not a hyphen, where the distinction is visible.

---

## 7. What to REMOVE, and how to convert teaching-arc IDEAS into student explanation

The source files are written *for an AI tutor*. None of that meta may appear in the student book. Remove it entirely — but mine the teaching *ideas* inside it and rewrite them as real explanation. **This is where the textbook actually teaches.** (Do this only once the dual-consumer question in §0 is settled.)

### Remove entirely (these are invisible to a learner)

- **The `## Teaching this unit (orientation for the tutor)` section** — every word.
- **The `## Wrap-up & interleaving` and `Progress Card should note:` blocks** — instructor rubrics about the student. Optionally replace with a brief, warm recap of what the reader can now do.
- **The label skeleton as labels:** don't print `Goal:`, `Why it matters:`, `Teaching arc (concrete → pictorial → symbolic):`, or the bracketed `Concrete:` / `Pictorial:` / `Symbolic:` stage tags. Dissolve them into narrated prose. (Keep the build-required bold labels from §3 — including `**Check for understanding (transfer):**` verbatim.)
- **`Watch for:` tutor diagnostics,** including every `Tell:` / `Repair:` and "a student may…" line. Optionally keep the student-useful warning as a short, calm "a common mix-up" note in the reader's voice (per §5).
- **`Visuals to offer:` lines.** First move any figure `{#...f...}` anchor onto a natural student sentence so the figure still embeds, *then* drop the tutor line. (See the figure-anchor rule below — it's stricter than it looks.)
- **All tutor stage directions:** "Lead Socratically," "Ask first," "Have the student confirm," "Hinge question," hint-ladder framing.
- **All tooling and production notes:** "verify with the code tool," "emit as an SVG artifact," screen-coordinate maps (`screenX = 110 + x*20`), "Artifact (Template 2)…".
- **Every internal cross-reference:** misconceptions.md, metaphors.md, pedagogy.md, visuals.md, curriculum-map.md, SKILL.md, "§", "Progress Card," "the student," "the tutor," "interleaving" as a named term, and machine anchor IDs surfacing in prose. Replace a genuinely useful pointer with a plain in-text callback ("remember from earlier that…").
- **Meta-commentary explaining the lesson design** to a colleague: "(11 previews exponents on a negative)," "13 vs 14 is the headline contrast," citation asides like "(this is the OpenStax definition)." Teach the point directly or cut it.
- **Stakes-raising framing:** "(the capstone)," "every back-half skill composes here," prerequisite dependency-graph walls. Soften a prerequisite into a brief plain "here's what's worth having fresh" note; open warmly and concretely.

### Watch the math while you strip meta

Tutor cross-references are frequently glued to the same line as, or the line right below, a `$$` worked example (for example, a line reading "Narrate the sign… (metaphors.md → negatives; misconceptions.md §3)" sitting under a `$$` block). When you strip `(misconceptions.md §3)` and the like, edit **only** the meta text; never touch the adjacent `$$` block, number, or anchor. After stripping meta from any lesson, re-run the count and notation checks in §9 to confirm you didn't disturb a numbered item, a `$$` block, or a code.

### Figure anchors: relocate precisely, never invent

When a source `Visuals to offer:` line names a real figure with a `{#N.M.fK}` anchor, move that anchor onto a real student sentence. The build is strict and CI-enforced here (`figure_lint`):

- The anchor must land on a sentence **within that same Lesson N.M**. Moving `{#5.2.f1}` into Lesson 5.3's prose renders the figure in the wrong lesson and breaks the lesson-scope expectation.
- The figure renders **immediately after the line that contains the anchor**, so choose the sentence where the figure should visually appear.
- Never duplicate an f-anchor, never delete it, and **never invent a new one.** Every f-anchor must have a bundled `figures/<code>.svg`, and every bundled SVG must be referenced by exactly one f-anchor — `figure_lint` hard-fails the build on an orphaned SVG or a dangling anchor. If a lesson has no figure anchor, it gets no figure; do not add one.

### How to convert a teaching-arc IDEA into student explanation

Lift the idea, drop the stage direction, write it *to the reader*. Worked conversions:

- **Socratic prompt → narrated reasoning.** Tutor: "Lead Socratically: 'The +5 is sitting next to x. What's the opposite of adding 5?'" → Student: "The +5 is sitting right next to x. To peel it away, do the opposite of adding 5 — subtract 5. And to keep the scale level, subtract 5 from the other side too."
- **`Tell:`/`Repair:` diagnostic → reader-owned, normalized note.** Tutor: "Tell: fills 8 + 4 = □ + 5 with 9. Repair: go back to the balance scale." → Student: "It's natural to compute 8 + 4 and write 12, or 9, in the box; that's the calculator habit. But the box plus 5 has to balance 12, so the box holds 7."
- **`Check for understanding` script → reflective self-check.** Tutor: "Give me a number that is rational but not an integer, and explain how you know." → Student: "Try this: name a number that's rational but not a whole number, and say how you know it's rational. (One answer: 0.5, because it's 1/2 — a ratio of two integers.)"
- **`Visuals to offer` → embedded figure sentence.** Move the `{#...f...}` anchor onto a real sentence in the same lesson: "Here's the line through those points {#5.2.f1}, with the rise and run marked," then delete the tutor visual line.
- **Surveillance error-framing → supportive second person.** Tutor: "A student may force x = ±2 by ignoring the minus." → Student: "It's easy to write x = ±2 here by glancing past the minus. Substitute it back, though — (±2)² = +4, not −4 — and you'll see no real number works."

Preserve verbatim while you do all this: the `**New terms:**` definitions (term + meaning) with their `{#...}` anchors; every `**Worked examples:**` item and its result; every `**Practice problems:**` item and sub-group label; the `**Answer key:**`; the `**Check for understanding (transfer):**` prompts with their `{#...c...}` anchors; and figure `{#...f...}` anchors.

---

## 8. The /copyedit + anti-AI-tell checklist (self-apply before submitting)

Run this on every passage. The core principle: **fix the voice, not the substance — never alter a number, a claim, or the math to make prose flow.** Math, answer keys, and anchors are exempt from voice editing and must not be touched.

**Voice (the deliberate override):**
- [ ] Second-person "you" and contractions are present and natural. (Override active — do **not** strip them.)
- [ ] Every other copyedit rule applied with the instructional-tutor target.
- [ ] "Let's" used sparingly if at all; bare imperatives preferred (matches the approved sample).

**Banned filler words — none present** (land on a plain word; don't swap one banned word for another):
delve, utilize, leverage, harness, streamline, unlock, foster, underscore, elevate, empower, navigate/orchestrate as metaphor, robust, crucial, vital, essential, seamless, holistic, comprehensive as filler, pivotal, game-changing, cutting-edge, transformative; landscape, paradigm, synergy, deep dive, journey, ecosystem unless literal, realm, tapestry.

**Banned openers / transitions / closers — none present:**
Furthermore, Moreover, Indeed, It's worth noting, It's important to note, Let's dive in, Let's unpack/explore/break this down, In today's…, When it comes to…, That said, At the end of the day, The bottom line is, By following these steps…, Ready to take your X to the next level. (Just start on the subject; end on the last real point.)
- [ ] **Banned phrases also bar their paraphrases.** Don't swap "it's worth noting" for "it's worth saying / worth mentioning / one thing to note"; don't swap "delve" for "dig into" or "leverage" for "tap into." Catch the dodge, not just the literal word.

**Banned patterns — none present:**
- [ ] No "It's not X, it's Y" *fake-insight* flip. (A real misconception correction is fine — confirm the X is a genuine misreading the reader holds.)
- [ ] No rule-of-three pile-ups (at most one per page; trim the rest to two or one).
- [ ] No em-dash overuse (a rare one is fine; three in a paragraph isn't — prefer commas, colons, periods).
- [ ] No throat-clearing or announce-the-point openers.
- [ ] No stacked hedges; no bullet avalanche (connected reasoning stays as prose). Remember: this framework's bulleted form is for authors; student copy is prose.
- [ ] No anthropomorphized math.
- [ ] No puffery, significance-inflation, gushing, or empty/ability praise — in student copy *and* in any explanatory aside.
- [ ] No comparison or ranking of the reader, and no "who's good at math" framing. (Calling an *error* common is allowed; ranking the *reader* — "most people find this easy/hard" — is not.)
- [ ] **No templated warmth.** Vary the misconception opener; no single softener opens more than one misconception per lesson. If two notes' first five words are swappable, rewrite one.

**Notation pass:**
- [ ] No `\( \)`, `\[ \]`, or single-`$` math. Inline math is Unicode; standalone math is `$$ … $$`; table cells are ASCII; currency is a bare `$` away from `$$`.
- [ ] No emoji, no ✓/✗ marks.
- [ ] **No `\checkmark` or any `\macro` outside a `$$` block** (banned in prose, and fails `check_notation.py`).
- [ ] **No stray ✓/✗ glyph inside a `$$` block either** — confirm correctness with "Correct" or the substitution, not a glyph.

**Affect pass (specific to this book):**
- [ ] The failure path is covered where relevant: a failed check has a calm recovery note; a hard stretch is followed by an easy win; there's honest permission to pause when both angles miss.
- [ ] No trap is named before the reader has had one clean success at the plain case; no trap in the first sentence of a new idea; trap density is at most one named slip per concept.
- [ ] "This is hard on purpose" never appears without pointing, in the same breath, to where the reachable help is.

**Over-correction guards:**
- [ ] Didn't rewrite substance or alter math; didn't install a generic voice that strips intended "you"; didn't edit quoted/verbatim items; thinned hedges and clichés without zeroing out all personality.

---

## 9. Math-preservation and no-drift rules

The math is already correct and SSOT-verified. **Present it better; never change it.**

**Be honest with yourself about what CI does and does not catch.** The build does *not* compare your `.md` practice problems or answer key against the verified JSON. `verify_answers.py` only re-checks the JSON against itself with sympy; the *only* `.md`-to-JSON cross-check is a narrow point-on-line lint for line-intercept problems (`var = b`, template `m*x0 + b = …`). So if you reword a practice problem from `4x = 20` to `4x = 21`, or flip an answer-key entry, or drop or renumber an item in the `.md`, **nothing will fail** — you will simply have shipped wrong math with a green build. For everything except those few line problems, the `.md` math is protected only by your own eyes. The verbatim-preservation rule below is therefore absolute and unbackstopped.

**Absolute rules — an author may not, under any circumstances:**

1. **Alter any number, variable, equation, expression, worked-example result, practice problem, or answer-key entry.** Not to "simplify," not to "clean up," not to fix a suspected typo. If you believe an item is genuinely wrong, **flag it for a human — do not edit it.**
2. **Renumber, reorder, add, or delete any worked example or practice item.** Count and order must match the source exactly. Remember the counting rule (§3): adding a numbered worked example, or changing one between numbered-list and `$$`-block form, or starting a line with `**` inside a block, silently shifts or deletes deep-link codes.
3. **Remove, rename, or reword the bold structural labels** the build keys on: `**New terms:**`, `**Worked examples:**`, `**Practice problems:**`, `**Answer key:**`, `**Check for understanding (transfer):**`.
4. **Change any unit or lesson title.** Titles are locked to `curriculum.yaml` and checked by `generate.py`; reproduce them byte-for-byte, no warming, no subtitles.
5. **Touch any `{#...}` anchor** — term, figure, or check. Anchors are append-only, globally unique, and must stay densely numbered 1..N within each group (`md_anchor_lint` enforces grammar, uniqueness, and density). When you embed a figure you *move* its existing anchor onto a student sentence in the same lesson — you never change the anchor's text, duplicate it, or invent one.
6. **Alter the New-terms definitions** (the term and its mathematical *meaning*). Preserve the term and the meaning verbatim with their anchors, and add surrounding teaching prose freely. One edit *inside* a definition IS allowed and required: if a definition's parenthetical carries tutor-meta — an internal ref like `metaphors.md`, a stage direction, a `§` — strip just that meta per §7, keeping the mathematical content exact. (Example: `…compute (use the reserved-seat metaphor — …, metaphors.md, Variables B)` becomes `…compute (the reserved seat finally has its guest sit down)`.) Never change the term, a number, or the meaning.
7. **Change the practice sub-group labels.** These are italic, non-numbered lines (for example `*Multiply-then-add:*`). Keep them italic and non-numbered: a bold label would end the practice block for the counter, and a leading `N. ` would be miscounted as a problem.

8. **Modify any script under `_verification/`** (the drift guard, the build, or the checkers). The gate is read-only for authors. If the drift check looks like it is reporting a false positive, say so in your handoff to the orchestrator and leave it; never edit the checker to make your unit pass.

**What you MAY do:** rewrite all explanatory prose around these fixed items; convert tutor labels and meta into student explanation (§7); add concrete anchors, narrated why-lines, transfer prompts, recovery notes, and reassurance; add non-keyed `### Mixed review` / `### Warm-up` blocks (§3); embed figures by relocating their existing anchors; present the *same* verified items more warmly.

**Runnable verification gate — do this before you submit; don't rely on eyeballing.**

1. `git diff` your unit file and confirm no `$$` block, number, answer-key line, title, or `{#...}` anchor changed. Diff the `**Practice problems:**` and `**Answer key:**` blocks against the pre-edit source specifically.
2. Build the textbook and diff the emitted codes for your lesson against the pre-edit build: run `python _verification/build_textbook.py`, and confirm the `wK` and practice codes for your lesson are identical before and after your edit (grep the generated HTML, or compare the in-memory codes).
3. Run the full guard and confirm all green:
   - `python _verification/generate.py --check` (SSOT, titles, lesson counts, outline, JSON ids, staleness)
   - `python _verification/check_alignment.py` (anchor lint, point-on-line, code grammar, figure lint, notation)
   - `python _verification/check_notation.py` (no `\( \)`, `$…$`, or stray `\macro` in prose)
   - `python _verification/verify_answers.py` (JSON answer key re-checked with sympy)
   - `python _verification/build_textbook.py --check` (committed site is current)

If any of these fails, or any code/count/anchor/number changed that you didn't intend, you've drifted — revert and redo.

**Per-unit handoff to the orchestrator.** Return, in a few lines: which files you touched; the scripts you ran and that they passed; the before/after worked-example and practice code counts for your unit (they must match); and explicit confirmation that no math, answer-key entry, title, label, or `$$` block changed.

---

## 10. Gold exemplar: BEFORE → AFTER, plus model sentences

Two exemplars. The first is a lesson whose worked examples are `$$` blocks (so they carry **no** deep-link codes — Units 2, 4, 6, 7, 8, 10, 11). The second is a lesson whose worked examples are a **numbered list** (so each carries a code — Units 1, 3, 5, 9, 12, A); it shows counter-safe narration. Match the form your assigned unit already uses.

### Exemplar A — `$$`-block worked examples (Lesson 2.1)

**BEFORE (real source text, `unit-02-linear-equations.md`, byte-accurate):**

> **Goal:** Solve any one-step equation by doing the *inverse* operation to **both** sides to isolate the variable.
>
> **Why it matters:** This is the atom every later equation is built from. Two-step, both-sides, and fraction equations are all just sequences of these single moves.
>
> **New terms:**
> - {#2.1.d1} **Solution:** a value that makes the equation a *true statement* when you substitute it in. (That's exactly why we check by substituting — we're confirming the statement is true.)
> - {#2.1.d2} **Isolate the variable:** get x alone on one side, with a number on the other.
> - {#2.1.d3} **Inverse (opposite) operation:** the operation that undoes another. Addition ↔ subtraction; multiplication ↔ division.
>
> **Teaching arc (concrete → pictorial → symbolic):**
> - *Concrete (balance scale, metaphors.md):* For x+5=12, picture a covered cup plus 5 coins balancing 12 coins. To find the cup's weight, remove 5 coins from *both* pans — still level.
> - *Pictorial:* `[cup] ●●●●● = ●●●●●●●●●●●●` → cross out 5 coins on each side → `[cup] = ●●●●●●●`.
> - *Symbolic:* $$x+5=12 \;\xrightarrow{\,-5\text{ both sides}\,}\; x=7.$$ Then **check:** 7+5=12.
>
> Lead Socratically (SKILL.md): "The +5 is sitting next to x. What's the opposite of adding 5? ... and if we do it to the left pan, what must we do to the right to keep it level?"
>
> **Naming the move honestly:** When we subtract 5 from x+5, the +5 **goes to zero** — x is left alone. For 4x=20, dividing both sides by 4 makes the coefficient **go to one**. Avoid "cancel" (misconceptions.md §1).

**AFTER (student-facing rewrite):**

> ## Lesson 2.1: Inverse operations & one-step equations
>
> Every equation you'll ever solve is built from one move, repeated. Once you can solve a one-step equation, the longer ones ahead are just a few of these single moves in a row. So this is the piece worth getting solid.
>
> Here's the idea, in something you can picture. Imagine a covered cup on a balance scale, sitting next to 5 coins, and the whole thing balancing 12 coins on the other pan. You want to know how much the cup weighs. If you lift 5 coins off the left pan, the scale tips — unless you also lift 5 coins off the right. Do both, and it stays level: now the cup alone balances 7 coins. The cup weighs 7.
>
> That's the same thing this equation says:
> $$x + 5 = 12$$
> The x is the cup. The +5 is sitting right next to it, and you want x by itself — alone on one side, with a number on the other. (Getting x alone like this has a name: you're **isolating the variable**.) To peel the +5 away, do the opposite of adding 5: subtract 5. That's the **inverse operation**, the move that undoes another (adding and subtracting undo each other; multiplying and dividing undo each other). And to keep the scale level, subtract 5 from the other side too:
> $$x + 5 = 12 \;\xrightarrow{\;-5 \text{ from both sides}\;}\; x = 7$$
> When you subtract 5 from x + 5, the +5 goes to zero, and x is left standing alone. Notice what *didn't* happen: nothing got "cancelled" by magic — the +5 went to zero because you subtracted 5.
>
> One move left, and it's the one to build into a habit now: check it. Put your answer back into the original equation and see if both sides match. Here, x = 7, so the left side is 7 + 5 = 12, which matches the right side. So x = 7 is the **solution** — the value that makes the equation a true statement. (And if a check ever *doesn't* match, that's not failure — your check just caught something. Go back to your first step and re-run the arithmetic slowly; a mismatch is almost always one small slip, not the whole method.)
>
> **New terms:**
> - {#2.1.d1} **Solution:** a value that makes the equation a *true statement* when you substitute it in. (That's exactly why we check by substituting — we're confirming the statement is true.)
> - {#2.1.d2} **Isolate the variable:** get x alone on one side, with a number on the other.
> - {#2.1.d3} **Inverse (opposite) operation:** the operation that undoes another. Addition ↔ subtraction; multiplication ↔ division.

**What changed, and why:** the `Goal:`/`Why it matters:` labels became an opening that leads with the idea and a concrete payoff; the bracketed `Concrete:`/`Pictorial:`/`Symbolic:` tags dissolved into narrated prose with the transition spoken ("That's the same thing this equation says"); the "Lead Socratically" stage direction became the reader's own reasoning; "metaphors.md," "SKILL.md," and "(misconceptions.md §1)" are gone; the check is shown inside the example as the natural last move, **and** the failed-check recovery is taught right there the first time checking appears; "goes to zero" and the anti-"cancel" note are kept in the reader's voice (opened with "Notice," not a throat-clearing "It's worth saying"); the check is written as plain prose, not a `$$` block with a glyph; the verified `$$` math, the New-terms definitions, the `{#2.1.d…}` anchors, and the locked lesson title are byte-for-byte the source.

### Exemplar B — numbered worked examples, counter-safe (Lesson 12.1 shape)

In units that number their worked examples, each numbered line carries a code (`12.1.w1`, `12.1.w2`, …). Keep exactly one `N. ` line per example, put any purpose-label as an inline lead-in on that line, and never number the sub-steps. This is safe:

> **Worked examples:**
>
> 1. √50 = √(25·2) = √25 · √2 = 5√2. We split off the *largest* perfect-square factor (25), so it comes out in one step.
> 2. **Add like radicals:** 2√3 + 4√3 = 6√3. Same radicand, so add the counts — exactly like 2x + 4x = 6x.

Both lines start with `N. `, so both get codes; the bold "Add like radicals:" rides *inside* line 2, after the number, so it doesn't end the block. The following would silently break it — **do not do this:**

> **Add like radicals**
> 2. 2√3 + 4√3 = 6√3.

Here the bold label on its own line ends the worked block, so item 2 (and everything after) loses its code.

### Model sentences (each passes /copyedit with the instructional override)

1. "It's tempting to read = as a button that means *the answer goes here*. It actually means *the same as*: the two sides balance, like a level scale."
2. "Subtracting a negative looks like it should make a number smaller, but taking away a $2 debt leaves you $2 richer — so 6 − (−2) is 8."
3. "When you solve 2x = 7 and land on 3.5, that's not a slip. It's a real point on the line, sitting halfway between 3 and 4."
4. "This is a common place to slow down, and a wrong turn here is useful — it shows you exactly what to aim at."
5. "Draw the rectangle and cut it into four cells: x², 3x, 2x, and 6. The two middle cells are the pieces people drop, and together they're the 5x."
6. "If the two sides of your check don't match, your check just did its job. Re-run the arithmetic from the first step; it's almost always one small slip, not the method."

### One failing passage, and its fix (so you can calibrate the copyedit eye)

A draft that *looks* fine but isn't:

> **Failing:** "It's worth noting that solving equations is a crucial, foundational skill — and honestly, most people find this part really easy! Let's dive in. The equation *wants* to be balanced, so we just move things across — it's not about memorizing, it's about understanding."

Why it fails: "It's worth noting" (banned opener), "crucial/foundational" (significance-inflation), "most people find this easy" (reader comparison **and** "this is easy"), exclamation cheerleading, "Let's dive in" (banned), anthropomorphized equation ("wants to be balanced"), em-dash pile-up, and the hollow "it's not X, it's Y" flip.

> **Fixed:** "Solving an equation comes down to one habit: keep both sides balanced. Whatever you do to one side, do to the other. Start with the picture, and the symbols will follow."

---

*End of framework. Math is fixed; voice is yours to make warm. When the two seem to conflict, the math and the structure win, and you find another way to be kind.*
