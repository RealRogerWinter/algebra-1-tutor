# Unit 2: Solving Linear Equations

> **Prerequisites:** Unit 1 — especially negative numbers (§1.4) and order of operations (§1.3), plus the equals sign as a *balance* (§1.1) and the variable as a *mystery box* (§1.5).
> **By the end, the student can:**
> - Solve one- and two-step linear equations using inverse operations, isolating the variable.
> - Combine like terms and apply the distributive property — including distributing a negative — without losing a sign.
> - Solve equations with the variable on both sides.
> - Add fractions over a common denominator, use reciprocals, and solve equations containing fractions.
> - **Check every answer by substituting it back** into the original equation.

## Teaching this unit (orientation for the tutor)

This unit is the heart of Algebra 1: it turns "what's the mystery number?" into a reliable *procedure*. The whole unit rests on one idea from Unit 1 — **the equals sign means balance** — so keep the balance-scale metaphor (metaphors.md → "Equations") live throughout. Every solving move is "do the same thing to *both* sides so the scale stays level."

Two habits to thread through **every** example, no exceptions:
1. **Verify by substituting back.** After getting x, put it into the *original* equation and show both sides match. This is both your safety net (you are a language model and can slip) and the single most valuable skill the student carries forward. Model it every single time — make it feel automatic, not optional.
2. **Inverse operations, named honestly.** Avoid the word "cancel." Say a term **"goes to zero"** (for +/-) or **"goes to one"** (for ×/÷) — that's literally what happens, and it heads off the misconception that symbols just vanish by magic (misconceptions.md §1).

The arc: 2.1 formalizes "same to both sides" on one-step equations; 2.2 stacks two operations and introduces *order* of undoing (the getting-dressed metaphor); 2.3 cleans up expressions (like terms + distributing) — **this is where the #1 sign trap lives** (distributing a negative, misconceptions.md §3/§7); 2.4 puts variables on both sides; 2.5 handles fractions, preceded by two short "Fraction Refreshers" that repair fraction gaps (misconceptions.md §4) before they sink the lesson.

**Biggest traps, in order of how often they bite:**
- **Distributing a negative:** -(x-4)=-x-4 (wrong) instead of -x+4. Lesson 2.3. Repair with the "flyers"/area-model picture and the substitution check.
- **Combining unlike terms:** 3x+2=5x. Lesson 2.3 (misconceptions.md §7).
- **Sign loss in two-step / both-sides** equations, especially dividing by a negative (2.2 example 8-2x=14).
- **Fraction magnitude** confusion underneath 2.5 (misconceptions.md §4) — patch with the refreshers.

**Pacing:** Most adults move through 2.1 quickly — don't belabor it, but use it to *cement* the substitution-check ritual and the balance language, because everything later inherits them. Slow down at 2.3 (sign traps) and 2.5 (fractions). Interleave: when a two-step problem lands on a negative answer (e.g. 8-2x=14 ⇒ x=-3), treat it as a deliberate callback to Unit 1 negatives (pedagogy.md → interleaving).

---

## Lesson 2.1: Inverse operations & one-step equations

**Goal:** Solve any one-step equation by doing the *inverse* operation to **both** sides to isolate the variable.

**Why it matters:** This is the atom every later equation is built from. Two-step, both-sides, and fraction equations are all just sequences of these single moves.

**New terms:**
- **Isolate the variable:** get x alone on one side, with a number on the other.
- **Inverse (opposite) operation:** the operation that undoes another. Addition ↔ subtraction; multiplication ↔ division.

**Teaching arc (concrete → pictorial → symbolic):**
- *Concrete (balance scale, metaphors.md):* For x+5=12, picture a covered cup plus 5 coins balancing 12 coins. To find the cup's weight, remove 5 coins from *both* pans — still level. The cup alone balances 7 coins.
- *Pictorial:* `[cup] ●●●●● = ●●●●●●●●●●●●` → cross out 5 coins on each side → `[cup] = ●●●●●●●`.
- *Symbolic:* $$x+5=12 \;\xrightarrow{\,-5\text{ both sides}\,}\; x=7.$$ Then **check:** 7+5=12.

Lead Socratically (SKILL.md): "The +5 is sitting next to x. What's the opposite of adding 5? ... and if we do it to the left pan, what must we do to the right to keep it level?"

**Naming the move honestly:** When we subtract 5 from x+5, the +5 **goes to zero** — x is left alone. For 4x=20, dividing both sides by 4 makes the coefficient **go to one** (4/4=1, and 1x=x). Avoid "cancel" (misconceptions.md §1).

**Worked examples** (each isolates with the inverse, then checks):

*Addition — undo by subtracting:*
$$x+5=12 \;\xrightarrow{\,-5\,}\; x=7 \qquad \text{Check: } 7+5=12$$

*Subtraction — undo by adding:*
$$x-4=10 \;\xrightarrow{\,+4\,}\; x=14 \qquad \text{Check: } 14-4=10$$

*Multiplication — undo by dividing:*
$$4x=20 \;\xrightarrow{\,\div 4\,}\; x=5 \qquad \text{Check: } 4(5)=20$$

*Division — undo by multiplying:*
$$\frac{x}{2}=6 \;\xrightarrow{\,\times 2\,}\; x=12 \qquad \text{Check: } \frac{12}{2}=6$$

*A "looks empty" case (good for the equals-sign idea):*
$$x+7=7 \;\xrightarrow{\,-7\,}\; x=0 \qquad \text{Check: } 0+7=7$$
"There's nothing wrong with x=0 — zero is a perfectly good number." (misconceptions.md §1: = means *same as*, not "compute something.")

**Watch for:**
- Doing the operation to only one side ("I subtracted 5 from the left"). Tell: the scale would tip. Repair: "What did the right pan do? It has to match."
- Using the *same* operation instead of the inverse (subtracting on x-4=10). Repair with the balance: "We already have *too few* on the left — do we remove more, or add?"
- Reading = as "the answer goes here" rather than balance (misconceptions.md §1) — surfaces on x+7=7 and x-8=0. Hinge question: "Fill the blank so this stays true: 8+4=□+5."

**Visuals to offer:** A balance-scale sketch or the ASCII cup-and-coins above is plenty; no artifact needed.

**Check for understanding (transfer):**
1. "Solve x-5=12, and prove it's right without me." (listen for the substitution check)
2. "In 6x=6, what's the inverse operation, and why does the 6 in front *go to one*?"
3. "If I change x+9=14 to 9+x=14, does anything about your method change?" (no — addition order doesn't matter)

**Practice problems:**

*Add (undo by subtracting):*
1. x+5=12  2. x+9=14  3. x+7=7  4. 11+x=20  5. x+3=8

*Subtract (undo by adding):*
6. x-4=10  7. x-6=1  8. x-2=9  9. x-8=0  10. x-5=12

*Multiply (undo by dividing):*
11. 4x=20  12. 3x=21  13. 6x=6  14. 5x=45  15. 7x=28

*Divide (undo by multiplying):*
16. x/2=6  17. x/3=4  18. x/5=2  19. x/4=8  20. x/6=3

*Mixed (pick the right inverse):*
21. x+14=23  22. 9x=54  23. x-7=15  24. x/8=3  25. x+6=19

**Answer key (all verified):**
1) 7  2) 5  3) 0  4) 9  5) 5  6) 14  7) 7  8) 11  9) 8  10) 17  11) 5  12) 7  13) 1  14) 9  15) 4  16) 12  17) 12  18) 10  19) 32  20) 18  21) 9  22) 6  23) 22  24) 24  25) 13

---

## Lesson 2.2: Two-step equations

**Goal:** Solve equations needing two inverse operations, undoing them in the **opposite order** they were built.

**Why it matters:** Most "real" equations are two-step (and the both-sides and fraction equations later collapse *to* two-step). Getting the *order* of undoing right keeps the numbers clean.

**New terms:** none new — this is two one-step moves in sequence.

**Teaching arc (concrete → pictorial → symbolic):**
- *Metaphor (getting dressed, metaphors.md → Equations B):* To build 2x+3 from x you *multiply by 2, then add 3* — socks, then shoes. To undo it, reverse both the order and the action: **shoes off first** (subtract 3), **then socks** (divide by 2). That's why we strip the +/- before the ×/÷.
- *Symbolic, with the check built in (pedagogy.md → backward fading):*
$$2x+3=11 \;\xrightarrow{\,-3\,}\; 2x=8 \;\xrightarrow{\,\div 2\,}\; x=4 \qquad \text{Check: } 2(4)+3=11$$

Ask first: "We have a ×2 and a +3 wrapped around x. Which layer is on the *outside* — which do we peel first?"

**Worked examples:**

*Multiply-then-add:*
$$2x+3=11 \;\xrightarrow{\,-3\,}\; 2x=8 \;\xrightarrow{\,\div 2\,}\; x=4 \qquad \text{Check: } 2(4)+3=8+3=11$$

*Division type:*
$$\frac{x}{3}-2=4 \;\xrightarrow{\,+2\,}\; \frac{x}{3}=6 \;\xrightarrow{\,\times 3\,}\; x=18 \qquad \text{Check: } \frac{18}{3}-2=6-2=4$$

*Dividing by a negative (Unit 1 callback):*
$$8-2x=14 \;\xrightarrow{\,-8\,}\; -2x=6 \;\xrightarrow{\,\div(-2)\,}\; x=-3 \qquad \text{Check: } 8-2(-3)=8+6=14$$
Narrate the sign: -2x=6, divide both sides by -2; 6/-2=-3. The check is where a sign slip would get caught — 8-2(-3) uses subtracting a negative (metaphors.md → negatives; misconceptions.md §3).

*A surprising one (answer is 0):*
$$3x+6=6 \;\xrightarrow{\,-6\,}\; 3x=0 \;\xrightarrow{\,\div 3\,}\; x=0 \qquad \text{Check: } 3(0)+6=6$$

**Watch for:**
- **Undoing in the wrong order** — dividing before subtracting on 2x+3=11 (often giving messy fractions). Repair with the getting-dressed order: "Which went on *last*? Take that off *first*."
- **Sign loss with subtraction/negatives:** on 8-2x=14, treating -2x as +2x. Separate the operation sign from the number's sign out loud (misconceptions.md §3). The substitution check catches it.
- **"Variable must be on the left" assumption:** problems 13–14 flip the format (8+2x=14, 10=4x-2). Reassure: balance works both directions; 10=4x-2 is the same as 4x-2=10.

**Visuals to offer:** none needed; the → step notation is the visual.

**Check for understanding (transfer):**
1. "Solve 3x+4=19 — and tell me *why* you subtracted before dividing." (pedagogy.md near-twin)
2. "What would change if it were 2x-5=13 instead of 2x+5=13?"
3. "In 10=4x-2, the variable's on the right. Does that break anything?"

**Practice problems:**

*Multiply-then-add:*
1. 2x+1=9  2. 3x+4=19  3. 5x+2=27  4. 4x+7=23

*Multiply-then-subtract:*
5. 3x-5=10  6. 6x-4=20  7. 2x-9=1  8. 7x-3=25

*Division type:*
9. x/2+3=8  10. x/4-1=2  11. x/3+5=9  12. x/5-2=0

*Flipped format (don't assume x is on the left):*
13. 8+2x=14  14. 10=4x-2  15. 3x+6=6

**Answer key (all verified):**
1) 4  2) 5  3) 5  4) 4  5) 5  6) 4  7) 5  8) 4  9) 10  10) 12  11) 12  12) 10  13) 3  14) 3  15) 0

*(Notes: 13–14 break the "variable on the left" habit on purpose; 15 lands on 0, which surprises people — zero is a fine answer.)*

---

## Lesson 2.3: Combining like terms & the distributive property

**Goal:** Simplify an expression by combining like terms and distributing — **including distributing a negative without flipping a sign by accident.**

**Why it matters:** Before you can solve a messier equation you have to *tidy* it. This lesson also seeds the area model that returns for multiplying binomials and factoring (Units 10–11). And distributing a negative is the single most common sign error in all of Algebra 1 — worth real care here.

**New terms:**
- **Term:** a single piece of an expression separated by + or - (e.g. in 3x+2, the terms are 3x and 2).
- **Coefficient:** the number multiplying the variable (the 3 in 3x).
- **Like terms:** terms with the **same variable part** — 3x and 2x are like; 3x and 2 are **not** (one is "boxes," the other is "loose units").
- **Distributive property:** a(b+c)=ab+ac — the outside factor multiplies *everything* inside.

**Teaching arc (concrete → pictorial → symbolic):**
- *Combining like terms (mystery-box picture, metaphors.md → Variables):* 3x is three identical boxes, 2x is two more of the same box — together 5x. But 3x+2 is three boxes plus two loose coins: you can't merge boxes with loose coins, so it **stays** 3x+2 (misconceptions.md §7). Ask: "Can you add boxes to loose units and get one kind of thing?"
- *Distribution (flyers + area model, metaphors.md → Distributive; visuals.md → area-model):* The outside number must hand a flyer to *everyone* inside — nobody skipped. Picture 2(x+4) as a rectangle 2 tall and (x+4) wide:
$$\begin{array}{c|c|c}
 & x & 4 \\ \hline
2 & 2x & 8
\end{array}\qquad\Rightarrow\qquad 2(x+4)=2x+8$$
- *Distributing a negative — the big one:* A leading minus is a -1 shaking hands with **everyone** inside. -(x-4): the -1 meets x (giving -x) **and** meets -4 (giving +4, because -1 × -4 = +4). So -(x-4)=-x+4, **not** -x-4 (misconceptions.md §3). Verify by substituting x=1: original -(1-4)=-(-3)=3; rewrite -1+4=3.

**Worked examples:**

*Combine like terms:*
$$3x+2x=5x$$

*Combine, leaving unlike terms alone:*
$$7x-4x+2 = 3x+2 \quad(\text{the }+2\text{ has no like partner})$$

*Distribute (positive):*
$$2(x+4)=2x+8$$

*Distribute a negative — the #1 sign trap:*
$$-(x-4) = -x+4 \qquad \text{Check at }x=1:\; -(1-4)=3 \;\text{ and }\; -1+4=3$$

*Distribute a negative, then combine (the trap in full):*
$$3-2(x-5) \;=\; 3 + (-2)(x) + (-2)(-5) \;=\; 3 - 2x + 10 \;=\; -2x+13$$
Check at x=1: original 3-2(1-5)=3-2(-4)=3+8=11; rewrite -2(1)+13=11. (Common wrong answer: 3-2x-10=-2x-7 from giving -2 × -5 a minus sign.)

**Watch for:**
- **Combining unlike terms:** 3x+2=5x (misconceptions.md §7). Tell: a variable term fused with a constant. Repair: boxes-vs-loose-coins.
- **Sign dropped distributing a negative:** -(x-4)=-x-4, or 3-2(x-5)=3-2x-10. Tell: the second product kept the wrong sign. Repair: "What is -2 times -5? The minus has to greet *every* term." Then substitution-check (try x=1).
- **Partial distribution:** 2(x+4)=2x+4 (forgot the 4). Repair: the flyers picture — "did everyone inside get one?"

**Visuals to offer:** The LaTeX `array` area-model box above (visuals.md → area-model) for any distribution — especially helpful when a negative is involved; show the -1 entering each cell.

**Check for understanding (transfer):**
1. "Simplify 5x+2-x. Which terms are 'like,' and which loner stays put?"
2. "Expand -(2x+5) and convince me the signs are right by testing x=1."
3. "A student writes 4-2(x+3)=4-2x+6. Where exactly did it go wrong?" (the -2×3 should be -6)

**Practice problems** (mix of combine and distribute; several lead with a negative):

*Combine like terms:*
1. 4x+3x  2. 9x-2x  3. 5x+2-x  4. 6+3x-4+x  5. 2x+5x-3x

*Distribute:*
6. 3(x+2)  7. 5(x-3)  8. 4(2x+1)

*Distribute a leading negative:*
9. -(x-7)  10. -(2x+5)

*Distribute, then combine:*
11. 2x+3(x+4)  12. 10-3(x-2)  13. 4-2(x+3)  14. 6(x-1)-2x

**Answer key (all verified):**
1) 7x  2) 7x  3) 4x+2  4) 4x+2  5) 4x  6) 3x+6  7) 5x-15  8) 8x+4  9) -x+7  10) -2x-5  11) 5x+12  12) -3x+16  13) -2x-2  14) 4x-6

---

## Lesson 2.4: Variables on both sides

**Goal:** Solve equations with the variable on **both** sides by gathering variable terms on one side and constants on the other — same move to both sides.

**Why it matters:** Real comparisons ("when does plan A cost the same as plan B?") put unknowns on both sides. It's also a direct rehearsal of every habit so far.

**New terms:** none new — it's "do the same to both sides" applied to a variable term.

**Teaching arc (concrete → pictorial → symbolic):**
- *Balance picture:* 5x+2=3x+10 — both pans have boxes *and* coins. To corner x, remove the same thing from both pans. Take 3x off each side (the 3x on the right **goes to zero**), leaving 2x+2=10. Then it's a familiar two-step.
$$5x+2=3x+10 \;\xrightarrow{\,-3x\,}\; 2x+2=10 \;\xrightarrow{\,-2\,}\; 2x=8 \;\xrightarrow{\,\div 2\,}\; x=4$$
$$\text{Check: } 5(4)+2=22 \;\text{ and }\; 3(4)+10=22$$

Ask first: "We've got boxes on both pans. What could we subtract from *both* sides to get all the boxes onto one?" (Tip: move the *smaller* variable term to avoid negatives — but either choice works.)


**Worked examples:**

*Standard:*
$$5x+2=3x+10 \xrightarrow{-3x} 2x+2=10 \xrightarrow{-2} 2x=8 \xrightarrow{\div 2} x=4 \quad\text{Check: }22=22$$

*Constants and variables both to move:*
$$7x-3=2x+12 \xrightarrow{-2x} 5x-3=12 \xrightarrow{+3} 5x=15 \xrightarrow{\div 5} x=3 \quad\text{Check: }18=18$$

*Negative answer (move the larger variable term, land below zero — Unit 1 callback):*
$$4x+1=6x+9 \xrightarrow{-4x} 1=2x+9 \xrightarrow{-9} -8=2x \xrightarrow{\div 2} x=-4$$
$$\text{Check: } 4(-4)+1=-15 \;\text{ and }\; 6(-4)+9=-15$$

*Distribute first, then gather:*
$$2(x-1)=x+5 \xrightarrow{\text{distribute}} 2x-2=x+5 \xrightarrow{-x} x-2=5 \xrightarrow{+2} x=7$$
$$\text{Check: } 2(7-1)=12 \;\text{ and }\; 7+5=12$$

**Watch for:**
- **Sign loss when subtracting a variable term:** subtracting 3x from 5x but forgetting it also hits the right side. Repair: "Both pans, every time."
- **Distributing-a-negative carry-over** from 2.3 (e.g. in problem 10, 2(x-1)=4x+6). Same trap; same fix.
- **Forgetting to distribute before gathering** (problems 9–12). Tip: tidy each side *first*, then move terms across.
- A **negative answer feels "wrong"** to some students — reassure (Unit 1): negatives are real solutions; the substitution check confirms them.

**Visuals to offer:** none needed; a two-pan balance sketch can help a stuck student *see* boxes coming off both sides.

**Check for understanding (transfer):**
1. "Solve 6x+1=4x+9. Which side did you move the variable to, and why that one?"
2. "In 3x+8=7x+20, if you move 3x right you'll hit a negative. Walk me through it and check."
3. "Why must we distribute 2(x-1) *before* gathering the x's?"

**Practice problems:**

*Gather variables (positive answers):*
1. 6x+1=4x+9  2. 8x-5=3x+10  3. 5x+3=2x+18  4. 7x-2=5x+8  5. 9x+4=6x+19  6. 4x-7=x+5

*Negative answers (Unit 1 callback):*
7. 3x+8=7x+20  8. 2x-9=5x+3

*Distribute first, then gather:*
9. 3(x+2)=x+10  10. 2(x-1)=4x+6  11. 5x-4=3(x+2)  12. 4(x-3)=2x+2

**Answer key (all verified — and worth substitution-checking each with the student):**
1) 4  2) 3  3) 5  4) 5  5) 5  6) 4  7) -3  8) -4  9) 2  10) -4  11) 5  12) 7

*Substitution spot-checks:* #7: 3(-3)+8=-1, 7(-3)+20=-1. #10: 2(-4-1)=-10, 4(-4)+6=-10. #11: 5(5)-4=21, 3(5+2)=21.

---

## Lesson 2.5: Equations with fractions (with two Fraction Refreshers)

**Goal:** Solve equations containing fractions — by multiplying by a **reciprocal** (single fraction coefficient) or by **clearing fractions** (multiply the whole equation by a common denominator).

**Why it matters:** Fractions appear everywhere downstream (slope, proportions, rates). Adults often stalled here years ago, so the two short refreshers below repair the foundation *before* the lesson proper. Fraction-magnitude understanding is the #1 long-run predictor of algebra success (misconceptions.md §4) — invest here.

> **Teach the refreshers first if there's any hesitation** — surface them with the placement-style question (2/3)x=6. If the student is already fluent with fractions, skip straight to the lesson proper (pedagogy.md → don't make a confident student crawl).

### Fraction Refresher A — Common Denominators

**The idea:** You can only add **same-sized pieces**. Thirds and quarters aren't the same size, so first rename both as a common size, *then* add the numerators (the count of pieces). Tie it to **magnitude**: 1/6 < 1/4 — splitting a pizza among 6 gives *smaller* slices than among 4 (misconceptions.md §4). And never add across (1/2 + 1/3 ≠ 2/5).

**Finding a common denominator:**
- *Bulletproof:* multiply the denominators (4 and 6 → 24) — always works, may need reducing.
- *Cleaner:* use the **LCM** (least common multiple) of the denominators (4 and 6 → 12).

**Worked:**
$$\frac34+\frac16:\quad \text{LCM}(4,6)=12,\quad \frac34=\frac{9}{12},\ \frac16=\frac{2}{12} \;\Rightarrow\; \frac{9}{12}+\frac{2}{12}=\frac{11}{12}$$

**Practice (add/subtract; reduce your answer):**
1. 1/4+2/4  2. 1/3+1/6  3. 1/2+1/4  4. 2/3+1/4  5. 3/4-1/2  6. 5/6-1/3  7. 1/2+1/5  8. 3/8+1/4  9. 2/3-1/6  10. 1/2+1/3+1/6

**Key (verified):** 1) 3/4  2) 1/2  3) 3/4  4) 11/12  5) 1/4  6) 1/2  7) 7/10  8) 5/8  9) 1/2  10) 1

### Fraction Refresher B — Reciprocals

**The idea:** The **reciprocal** of a fraction is the fraction flipped, and a number times its reciprocal **goes to one**: 2/3 × 3/2 = 1. A whole number is "over 1," so its reciprocal flips too: 5=5/1 → 1/5. **To undo multiplication by a fraction, multiply by its reciprocal** — that's the inverse operation for a fraction coefficient. So (2/3)x=6 is solved by multiplying both sides by 3/2.

**Worked:**
$$\frac23 x = 6 \;\xrightarrow{\,\times \frac32\,}\; x = 6\cdot\frac32 = 9 \qquad \text{Check: } \frac23(9)=6$$

**Practice — name the reciprocal:**
1. 5/8  2. 1/9  3. 6  4. 11/4

**Practice — solve using a reciprocal:**
5. (1/2)x=7  6. (2/5)x=4  7. (3/4)x=6  8. (2/3)x=10  9. (5/6)x=5  10. (3/2)x=9

**Key (verified):** 1) 8/5  2) 9  3) 1/6  4) 4/11  5) 14  6) 10  7) 8  8) 15  9) 6  10) 6

---

### The lesson proper: solving equations with fractions

**Two strategies:**

**(1) Single fraction coefficient → multiply by the reciprocal** (Refresher B):
$$\frac23 x=6 \;\xrightarrow{\,\times \frac32\,}\; x=9 \qquad \text{Check: } \frac23(9)=6$$

**(2) Fractions scattered in the equation → clear them** by multiplying *every term on both sides* by a common denominator. This turns a fraction equation into a clean whole-number one (Refresher A supplies the common denominator).
$$\frac{x}{2}+\frac{x}{3}=5 \;\xrightarrow{\,\times 6\text{ (the LCM)}\,}\; 6\cdot\frac{x}{2}+6\cdot\frac{x}{3}=6\cdot 5 \;\Rightarrow\; 3x+2x=30 \;\Rightarrow\; 5x=30 \;\Rightarrow\; x=6$$
$$\text{Check: } \frac{6}{2}+\frac{6}{3}=3+2=5$$
Stress: multiply **every** term, including the right side — the balance must stay level (a flyers-style "everyone gets multiplied").

**Worked examples:**

*Reciprocal method:*
$$\frac23 x=6 \xrightarrow{\times \frac32} x=9 \qquad \text{Check: } \frac23(9)=6$$

*Clear-the-fractions method:*
$$\frac{x}{2}+\frac{x}{3}=5 \xrightarrow{\times 6} 3x+2x=30 \Rightarrow 5x=30 \Rightarrow x=6 \qquad \text{Check: } 3+2=5$$

*Reciprocal with a bigger numerator:*
$$\frac34 x=9 \xrightarrow{\times \frac43} x=12 \qquad \text{Check: } \frac34(12)=9$$

**Watch for:**
- **Multiplying only some terms** when clearing fractions (forgetting the constant or the right side). Repair: "Every term gets the ×6 — the scale only stays level if *both whole pans* are multiplied."
- **Flipping the wrong thing / not flipping:** dividing by 2/3 instead of multiplying by 3/2. Both are valid, but the reciprocal is cleaner; show they agree.
- **Adding-across error** resurfacing (x/2 + x/3 → x/5, misconceptions.md §4). Repair via Refresher A: different-sized pieces.
- **Fraction magnitude** confusion ((3/2)x feels "less than x"). Tie back to the number line (misconceptions.md §4).

**Visuals to offer:** none needed; an ASCII number line can anchor a magnitude question (3/2 sits past 1) if the student doubts it.

**Check for understanding (transfer):**
1. "Solve (2/5)x=8 two ways — by reciprocal, and by multiplying through by 5 — and confirm they agree."
2. "In x/2 + x/4 = 6, what number clears *both* fractions, and why that one?"
3. "Why does multiplying by 3/2 make (2/3)x *go to one* times x?"

**Practice problems:**

*Reciprocal method (single fraction coefficient):*
1. (1/2)x=5  2. (2/3)x=8  3. (3/5)x=9  4. (5/2)x=10

*Clear the fractions (common denominator):*
5. x/2+x/4=6  6. x/3+x/6=3  7. x/2-x/5=3  9. x/4+x/2=9

*Mixed (fraction coefficient with a constant):*
8. (2/3)x+1=7  10. (3/4)x-2=4

**Answer key (all verified):**
1) 10  2) 12  3) 15  4) 4  5) 8  6) 6  7) 10  8) 9  9) 12  10) 8

*Substitution spot-checks:* #5: 8/2+8/4=4+2=6. #7: 10/2-10/5=5-2=3. #8: (2/3)(9)+1=6+1=7.

---

## Wrap-up & interleaving

**Consolidate:** The student should leave able to solve any linear equation by a single reliable habit — *do the same inverse move to both sides until x is alone, then substitute back to check.* The procedure is identical whether the equation is one-step, two-step, both-sides, or fractional; only the number of moves changes.

**Mix back in (interleaving, pedagogy.md):**
- Keep slipping in **negative answers** (callback to Unit 1.4) — e.g. revisit 8-2x=14 and the both-sides negatives — so signs stay sharp.
- Re-run the **distributing-a-negative** trap (2.3) inside both-sides and fraction problems; it's the error most likely to relapse.
- Warm up each session with a 60-second one-step or two-step solve before new material.
- When you reach later units, **narrate solving in function language** where natural ("setting f(x)=0 is just solving an equation you already know how to solve").

**Progress Card should note:**
- Which lessons are mastered (e.g. "2.1–2.3 solid").
- Whether the **substitution-check habit** is automatic yet.
- Any lingering **sign trap** (distributing a negative; dividing by a negative) or **fraction** shakiness — and whether the refreshers were needed.
- Tone/detail preference.

Example:
```
ALGEBRA PROGRESS CARD
Unit/Lesson: 2.4 — Variables on both sides
Mastered: 2.1–2.3; substitution-check is now automatic
Watch for: distributing a leading negative still occasionally drops a sign
Last problem: 2(x-1) = x + 5  →  x = 7
Next up: finish 2.4, then 2.5 (fractions) — may want Refresher A/B first
Tone preference: medium detail
```
