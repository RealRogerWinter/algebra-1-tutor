# Unit 8: Inequalities

> **Prerequisites:** Unit 2 (solving one- and two-step equations; the balance-scale meaning of `=`) and Unit 5 (the coordinate plane, slope, and graphing y = mx + b). Comfort with negatives (Unit 1 / `misconceptions.md` §3) is leaned on heavily here.
> **By the end, the student can:**
> - Read and write the four inequality symbols <, ≤, >, ≥ and explain that a solution is a **set** of many values, not a single number.
> - Solve a linear inequality like an equation, applying the **sign-flip rule** when multiplying or dividing by a negative — *and explain why it must flip*.
> - **Graph** an inequality on a number line (open vs. filled circle, shade the ray) and self-check by **testing a point**.
> - Solve and graph **compound** inequalities (*and* = between; *or* = union).
> - Graph y = |x| (the V) and solve the symmetric absolute-value cases |x| = k, |x| < k, |x| > k by reading |x| as distance from 0 (off-center algebraic solving is flagged as Algebra-2 reach).
> - **Graph a two-variable linear inequality** (dashed/solid boundary, shade the correct half-plane via a test point) and find the solution region of a **system** of inequalities.

## Teaching this unit (orientation for the tutor)

Inequalities are "equations with a direction." Almost everything from Unit 2 transfers — isolate the variable with balanced moves — with **one** new rule that causes the overwhelming majority of errors: **multiplying or dividing both sides by a negative reverses the inequality sign.** This is the central trap of the unit (`misconceptions.md` §6). Do not teach it as a rule to memorize; teach the **why**, then the **self-check**:

- **The why:** start from something obviously true, 2 < 3. Multiply both sides by -1: you get -2 and -3. Is -2 < -3? No — -2 is the *bigger* number. To keep a true statement, the sign had to flip: -2 > -3. The flip isn't a trick; it's what keeps the statement true.
- **The self-check (works every time):** after solving, **test a point**. Put a number from your answer set into the *original* inequality. If it makes the original true, good; if the original is true at x = 0 but 0 isn't in your answer, a flip went missing. Model this on every negative-coefficient problem (`misconceptions.md` §6).

The second persistent fuzziness is what a **solution set** *means*: an equation usually has one answer; an inequality has infinitely many, which is exactly why we **graph** it (a shaded ray, not a dot). Keep tying the algebra to the number-line picture.

**The arc.** **8.1** builds one-variable solving + number-line graphing + the flip. **8.2** chains two conditions (*and*/*or*). **8.3** centers on *distance from 0* — graph the V of y = |x|, then solve the symmetric |x| = k / |x| < k / |x| > k cases, where "within" becomes an *and* and "outside" an *or* (a direct payoff of 8.2); off-center algebraic solving is flagged as Algebra-2 reach. **8.4** lifts everything into two variables: a line splits the plane, you shade a half, and a **system** is the overlap. Thread **function language** where natural: a boundary like y = 2x+1 *is* the function f(x) = 2x+1; the inequality y > 2x+1 asks "where is the output *above* the line?"

**Pacing.** Spend real time on the flip in 8.1 until the *test-a-point* habit is automatic — it pays off in 8.2 and 8.3. Don't drill number-line drawing to exhaustion; its job is meaning. In 8.4, precision matters less than three correct decisions: dashed-vs-solid, which side, and stating the test point out loud.

---

## Lesson 8.1: One-variable inequalities

**Goal:** Solve a linear inequality in one variable (including the negative-coefficient flip) and graph its solution set on a number line.
**Why it matters:** Real constraints are rarely "exactly equal" — *at least* $20, *no more than* 8 hours, *under* the speed limit. Inequalities are how we solve "how much is enough / too much," and the solution is a whole range of acceptable values.
**New terms:**
- {#8.1.d1} **Inequality:** a statement that **compares** two quantities using < (less than), > (greater than), ≤ (less than *or equal to*), or ≥ (greater than or equal to) — saying one is less than, greater than, or at most/at least the other (an *order* relation).
- {#8.1.d2} **Solution set:** *all* the values that make the inequality true — usually infinitely many, drawn as a shaded ray.
- {#8.1.d3} **Strict** (<, >) vs. **inclusive** (≤, ≥): whether the boundary value itself counts.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** "‘You must be **at least** 13’ — is 13 allowed? Is 20? Is 12? That's age ≥ 13: a whole crowd of allowed numbers, not one." Contrast with an equation (one answer). Anchor ≤/≥ to "*or equal to* = the boundary is invited in."
- **Pictorial:** The solution lives on a **number line**. **Open circle** ○ at the boundary for strict (<, >) — "the boundary itself is *not* included"; **filled circle** ● for inclusive (≤, ≥) — "included." Then **shade the ray** toward all the values that work. Use the ASCII number lines in `visuals.md` (the x>2 and x ≤ -1 sketches) for in-chat, or **Template 1** for a polished SVG artifact. Always say in words what the picture shows.
- **Symbolic:** Solve *exactly like an equation* (Unit 2 balanced moves) with **one** added rule: **if you multiply or divide both sides by a negative, flip the inequality sign.** Adding/subtracting, or multiplying/dividing by a *positive*, never flips it.

Teach the flip's **why** (the 2<3 → -2 ? -3 argument above, `misconceptions.md` §6), then close every problem with **test a point**.

**Worked examples:**

*Example 1 — no flip.* Solve x + 3 < 7.
Subtract 3 from both sides: x < 4.
Graph: **open circle** at 4 (strict), shade **left** (toward smaller values).
Test a point: try x = 0. Original: 0 + 3 = 3 < 7, and 0 < 4 — agree. Solution: **x < 4**.

*Example 2 — two steps, no flip.* Solve 2x - 1 ≥ 5.
Add 1: 2x ≥ 6. Divide by **+2** (positive → no flip): x ≥ 3.
Graph: **filled circle** at 3 (inclusive), shade **right**.
Test x = 4: 2(4) - 1 = 7 ≥ 5, and 4 ≥ 3. Solution: **x ≥ 3**.

*Example 3 — the flip.* Solve -2x < 6.
Divide both sides by **-2** → **flip** the sign: x > -3.
Graph: **open circle** at -3, shade **right**.
Test x = 0: original -2(0) = 0 < 6; is 0 > -3? — agree. (Had we forgotten to flip and written x < -3, then 0 would be *excluded* even though it makes the original true — the test catches it.) Solution: **x > -3**.

*Example 4 — the -x trap.* Solve 5 - x > 2.
Subtract 5: -x > -3. Now divide by -1 → **flip**: x < 3.
Test x = 0: 5 - 0 = 5 > 2; is 0 < 3?. Solution: **x < 3**.
*(Alternative that avoids a negative coefficient: add x to both sides → 5 > 2 + x → 3 > x, i.e. x < 3. Same answer; show this as the flip-free route.)*

**Watch for:**
- **The missing flip** (`misconceptions.md` §6) — the unit's headline error. Tell: -2x < 6 ⇒ x < -3. Repair with the 2<3 argument *and* the test-a-point check, not a louder restatement.
- **Mishandling -x** in 5 - x > 2 (writing x > 3). Same root; the test-a-point check exposes it.
- **Open vs. filled circle** confusion — ≤/≥ get a **filled** dot ("equal is included"), </> an **open** one.
- **Treating it like an equation with one answer** — push "name three numbers that work" to surface the *set*.

**Visuals to offer:** {#8.1.f1} ASCII number line in chat for quick feedback (the x>2/x≤-1 sketches in `visuals.md`), or **Template 1** (SVG artifact) for a polished line — open vs. filled endpoint, shaded ray, boundary labeled. Always pair with a sentence.

**Check for understanding (transfer):**
1. {#8.1.c1} "Solve -3x ≥ 12, then test x = -5 in the *original*. Walk me through how the test confirms (or would catch a mistake in) your answer."
2. {#8.1.c2} "Two students solve -x < 4. One writes x < -4, the other x > -4. Using x = 0, decide who's right and explain how you know."
3. {#8.1.c3} "In words, describe the number-line graph of x ≤ 2: which circle, filled or open, and which direction do you shade?"

**Practice problems** (solve; then describe the number-line graph in words — which circle and which way you shade):

*Set A — no flip*
1. x - 2 < 3
2. x + 5 ≤ 2
3. 3x > 12
4. x/2 ≥ 4
5. 2x + 1 ≤ 9
6. 4x - 3 > 9

*Set B — requires a flip (multiply/divide by a negative)*
7. -x < 4
8. -3x ≤ 9
9. -x + 2 < 5
10. 10 - 2x ≥ 4
11. 3 - x ≤ 7
12. -4x ≤ -8

*Set C — read the graph (manual)*
13. A number line shows an **open** circle at 1 shaded to the **right**. Write the inequality.
14. A number line shows a **filled** circle at -2 shaded to the **left**. Write the inequality.

**Answer key (all verified):**
1. x < 5 — open circle at 5, shade left.
2. x ≤ -3 — filled circle at -3, shade left.
3. x > 4 — open circle at 4, shade right.
4. x ≥ 8 — filled circle at 8, shade right.
5. x ≤ 4 — filled circle at 4, shade left.
6. x > 3 — open circle at 3, shade right.
7. x > -4 — **flip** (÷ by -1); open circle at -4, shade right. *(Test x=0: -0<4, 0>-4.)*
8. x ≥ -3 — **flip** (÷ by -3); filled circle at -3, shade right.
9. x > -3 — subtract 2 → -x < 3 → **flip** → x > -3; open circle at -3, shade right.
10. x ≤ 3 — subtract 10 → -2x ≥ -6 → **flip** (÷ by -2) → x ≤ 3; filled circle at 3, shade left.
11. x ≥ -4 — subtract 3 → -x ≤ 4 → **flip** → x ≥ -4; filled circle at -4, shade right.
12. x ≥ 2 — divide by -4 → **flip** → x ≥ 2; filled circle at 2, shade right. *(Test x=2: -8 ≤ -8.)*
13. x > 1 (open + right = strict greater-than).
14. x ≤ -2 (filled + left = inclusive less-than-or-equal).

---

## Lesson 8.2: Compound inequalities

**Goal:** Solve and graph compound inequalities joined by **and** (intersection — *between*) or **or** (union — two separate rays).
**Why it matters:** Real constraints often come in pairs — "between 60 and 80," "older than 12 **or** with a guardian." *And* narrows; *or* widens.
**New terms:**
- {#8.2.d1} **Compound inequality:** two inequalities combined into one statement.
- {#8.2.d2} **And (intersection):** *both* parts must hold. 2 < x ≤ 5 is shorthand for x > 2 **and** x ≤ 5 — the values **between** 2 and 5 (with 5 included). On the line, the **overlap** of the two shaded regions — a single segment.
- {#8.2.d3} **Double inequality** (a.k.a. **three-part inequality**): the chained form a < x < b. It is only well-formed when **both symbols point the same way**, and it *always* means an **and** (a < x **and** x < b). Never write something like 3 < x > 1 — a chained form with the symbols pointing opposite ways is meaningless.
- {#8.2.d4} **Or (union):** *at least one* part holds. x < -1 **or** x > 3 — **everything** in either ray; the two pieces don't touch.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** *And* = "you must clear **both** bars" (narrows to the overlap). *Or* = "clear **either** bar" (widens to the union). "Temperature between 60 and 80" is an *and*; "under 32 or over 100" is an *or*.
- **Pictorial:** Shade each condition on the same number line. *And* keeps only where the shadings **overlap** (a between-segment, two endpoints). *Or* keeps **everything** shaded by either (two rays heading opposite ways). Endpoints follow 8.1's open/filled rule per symbol.
- **Symbolic:** A three-part *and* like -1 < x + 2 < 4 is solved by doing the **same move to all three parts** at once. An *or* is solved as **two separate** inequalities, then unioned.

**Worked examples:**

*Example 1 — "and" (three-part).* Solve -1 < x + 2 < 4.
Subtract 2 from **all three** parts: -1 - 2 < x < 4 - 2, i.e. -3 < x < 2.
Graph: open circles at -3 and 2, shade the segment **between**.
Test x = 0 (inside): -1 < 0+2=2 < 4. Solution: **-3 < x < 2**.

*Example 2 — "and" with a division.* Solve 3 ≤ 2x - 1 ≤ 9.
Add 1 to all parts: 4 ≤ 2x ≤ 10. Divide all by +2 (positive → no flip): 2 ≤ x ≤ 5.
Graph: filled circles at 2 and 5, shade between. Solution: **2 ≤ x ≤ 5**.

*Example 3 — "or".* Solve x < -1 **or** x > 3.
Already solved — two rays. Graph: open circle at -1 shading **left**, open circle at 3 shading **right**; nothing in the middle. Solution: **x < -1 or x > 3**.

*Example 4 — "or" needing work.* Solve 2x ≤ -4 **or** x - 3 > 2.
Left: x ≤ -2. Right: x > 5. Graph: filled circle at -2 shading left, open circle at 5 shading right. Solution: **x ≤ -2 or x > 5**.

*Example 5 — three-part, divide by a negative (flip BOTH signs).* Solve -6 < -2x ≤ 4.
Divide **all three** parts by **-2** → **flip both** signs: -6/-2 > x ≥ 4/-2, i.e. 3 > x ≥ -2.
Rewrite left-to-right in **increasing** order (smaller number on the left): reading 3 > x ≥ -2 backwards gives **-2 ≤ x < 3**. (The strict end stays strict and the inclusive end stays inclusive — only their positions move, so the 3 keeps its open/strict mark and -2 keeps its filled/inclusive one.)
Graph: filled circle at -2, open circle at 3, shade the segment **between**.
Test a point — x = 0 (inside): -6 < -2(0) = 0 ≤ 4 ✓. Check the endpoints too: x = -2 is **in** (-2(-2) = 4, and -6 < 4 ≤ 4 ✓, so -2 is included), while x = 3 is **out** (-2(3) = -6, and -6 < -6 is false, so 3 is excluded). Solution: **-2 ≤ x < 3**.

**Watch for:**
- **Confusing *and* with *or*.** *And* = overlap (between, narrower); *or* = union (two rays, wider). If a student shades the whole line for an *and*, they've unioned by mistake.
- **In a three-part *and*, only changing the middle.** Whatever you do, do it to **all three** parts (`misconceptions.md` §1 — balance applies across the whole statement).
- **The flip still applies** to compound inequalities — dividing the three-part statement by a negative flips **both** signs (turning a < x < b into b > x > a). Same self-check: test a point.
- **Writing an empty *and* as if it had answers** — e.g. x > 5 **and** x < 1 has *no* solution (no overlap). Worth one example if it arises.

**Visuals to offer:** ASCII number lines (one segment for *and*, two rays for *or*), or two endpoints on **Template 1**. Show *and* and *or* on stacked lines so the contrast is visible. Pair with words.

**Check for understanding (transfer):**
1. {#8.2.c1} "Rewrite 2 < x ≤ 5 as two separate inequalities joined by a word. Which word, and why is the graph a single segment instead of two rays?"
2. {#8.2.c2} "Why does x > 5 **and** x < 1 have no solution, while x > 5 **or** x < 1 has lots? Describe both graphs."
3. {#8.2.c3} "You solve a three-part inequality and divide all parts by -2. What happens to the two inequality signs, and how would testing a point confirm it?"

**Practice problems** (solve and describe the graph: segment-between for *and*, two rays for *or*):

*Set A — "and"*
1. -2 < x - 1 < 3
2. 0 ≤ x + 1 ≤ 4
3. 3 ≤ 2x - 1 ≤ 9
4. -4 < 2x < 6

*Set B — "or"*
5. x < -1 or x > 5
6. x + 1 < 0 or x - 3 > 2
7. 2x ≤ -4 or x > 3
8. x - 3 ≥ 2 or x < -2

*Set C — three-part, divide by a negative (flip BOTH signs, then rewrite in increasing order)*
9. -9 ≤ -3x < 6

**Answer key (all verified):**
1. -1 < x < 4 — add 1 to all parts; open circles at -1 and 4, shade between.
2. -1 ≤ x ≤ 3 — subtract 1 from all parts; filled circles at -1 and 3, shade between.
3. 2 ≤ x ≤ 5 — add 1, divide by 2; filled circles at 2 and 5, shade between.
4. -2 < x < 3 — divide all by 2; open circles at -2 and 3, shade between.
5. x < -1 or x > 5 — two rays (open at -1 left, open at 5 right).
6. x < -1 or x > 5 — left: x<-1; right: x>5; two rays.
7. x ≤ -2 or x > 3 — filled at -2 left, open at 3 right.
8. x ≥ 5 or x < -2 — filled at 5 right, open at -2 left.
9. -2 < x ≤ 3 — divide all three parts by -3 and **flip both** signs (3 ≥ x > -2), then rewrite increasing; open circle at -2, filled circle at 3, shade between. *(Test x = 0: -9 ≤ 0 < 6 ✓; endpoint x = 3 is in since -3(3) = -9 ≥ -9; endpoint x = -2 is out since -3(-2) = 6 < 6 is false.)*

---

## Lesson 8.3: Absolute value: graphs & distance

**Goal:** Read |x| as **distance from 0**, graph **y = |x|** (the V) and its simple shifts, and solve the **symmetric** cases |x| = k, |x| < k, |x| > k straight from that distance picture.
**Why it matters:** Absolute value measures *how far*, ignoring direction — tolerance ("within 0.5 of target"), distance, magnitude. Centering on 0 keeps the algebra light and makes "within → *and* / outside → *or*" visible (the payoff of 8.2). *(Shifting the center off 0 — |x − 3| = 5, |2x − 1| = 7 — needs a two-case algebraic method that belongs to Algebra 2; it's flagged in the Reach note at the end.)*
**New terms:**
- {#8.3.d1} **Absolute value |x|:** the distance of x from 0 on the number line; always ≥ 0. |5| = 5 and |-5| = 5 — both are 5 units from 0 (callback to Unit 1.4).
- {#8.3.d2} **The graph y = |x|:** a **V** with its vertex at the origin — the right arm rises at slope +1, the left arm at slope -1 — and it never dips below the x-axis, because an output that *is* a distance can't be negative.
- {#8.3.d3} **Simple shifts of the V:** y = |x| + 2 lifts the whole V up 2; y = |x| − 3 drops it 3; y = |x − 1| slides it right 1 (the vertex moves to where the inside equals 0). These are *graph* moves read off the picture — not algebra to solve.

**Teaching arc (concrete → pictorial → symbolic):**
- **Distance from 0 (concrete).** |x| asks "how far is x from 0?" |3| = 3 and |-3| = 3 — different inputs, same distance.
- **The V-graph (pictorial).** Plot y = |x| at x = -3…3: (-3,3), (-2,2), (-1,1), (0,0), (1,1), (2,2), (3,3) — a V resting on the origin. Then name the simple shifts above. (Sketch it as a line/curve per `visuals.md`; describe it in words in chat.)
- **Symmetric solving, read off the distance.** With the center at 0:
  - **|x| = k → x = k or x = -k** ("k from 0, both ways"). Needs k ≥ 0; at k = 0 the one answer is x = 0; if k < 0 there's **no solution**.
  - **|x| < k → -k < x < k** ("within k of 0" — an **and**, one segment). Needs k > 0; if k ≤ 0, no solution.
  - **|x| > k → x < -k or x > k** ("more than k from 0" — an **or**, two rays). Holds for any k ≥ 0; if k < 0 it's **all real numbers**.
- **Isolate the |·| first (one positive step).** If the absolute value is scaled, divide to get |x| by itself, then read it: 2|x| ≤ 8 → |x| ≤ 4 → -4 ≤ x ≤ 4. (Keep isolation to a *positive* divide here; the sign-flip-during-isolation case is Algebra 2.)

**Worked examples** (the mastery set — symmetric, centered at 0; quote a code like 8.3.w7 to revisit one):

*w5 — inclusive "within".* Solve |x| ≤ 2. Within 2 of 0, inclusive → -2 ≤ x ≤ 2. Filled circles at -2 and 2, shade between. Solution: **-2 ≤ x ≤ 2**.

*w6 — the graph y = |x|.* Plot (-2,2), (-1,1), (0,0), (1,1), (2,2): a **V** with vertex (0,0), arms at slope ±1, resting on the x-axis. y = |x| − 2 is the same V dropped 2 (vertex (0,-2)); y = |x − 1| is it slid right 1 (vertex (1,0)). No solving here — just read the picture.

*w7 — "outside" (or).* Solve |x| > 2. More than 2 from 0 → **x < -2 or x > 2**. Open circles at -2 and 2, shade outward (two rays).

*w8 — isolate first.* Solve 2|x| ≤ 8. Divide by 2 (positive → no flip): |x| ≤ 4. Within 4 of 0 → **-4 ≤ x ≤ 4**. Filled circles at -4 and 4, shade between.

*w9 — no solution / all reals.* Distance is never negative, so read these straight off the picture: |x| = -3 has **no solution**; |x| < -2 has **no solution**; |x| > -1 is true for **every** real x (**all real numbers**).

**Watch for:**
- **Giving only one answer to |x| = k.** Distance goes *both* ways → two answers, x = ±k (unless k = 0, one answer; k < 0, none).
- **Swapping *and*/*or*:** "within / less-than" → **and** (one segment between -k and k); "outside / greater-than" → **or** (two rays). Re-derive from the distance picture if unsure.
- **Forgetting to isolate first.** In 2|x| ≤ 8 you must divide by 2 *before* reading the distance — |x| ≤ 8 is a different (wrong) statement.
- **|x| = negative, or |x| < negative:** distance can't be negative. |x| = -4 → **no solution**; |x| < -3 → **no solution**; |x| > -3 → **all reals**. Reason from the picture, never a blind shortcut.
- **Graph vs. solve.** y = |x| (and its shifts) is a *picture* to read; |x| = k is an *equation* to solve. Don't try to "solve" the graph.

**Visuals to offer:** {#8.3.f1} Two pictures carry this lesson — the **V-graph** of y = |x| (vertex at the origin, slope ±1, sits on the axis), and a **number line** for solving (mark 0, step k each way; dot the two solutions, or shade the between-segment for *and* / two rays for *or*). Use `visuals.md` for a clean sketch; always state the distance interpretation in words.

**Check for understanding (transfer):**
1. {#8.3.c1} "Sketch y = |x| in words: where's the vertex, what are the arm slopes, and why does it never go below the x-axis? Then describe y = |x| + 1."
2. {#8.3.c2} "Why does |x| < 4 become an *and* (a single segment) while |x| > 4 becomes an *or* (two rays)? Use the distance picture."
3. {#8.3.c3} "What is the solution of |x| = -3? Of |x| > -3? Explain each from ‘distance is never negative.’"

**Practice problems (core — the mastery path):** symmetric, centered at 0. *(Problems 2, 3, 5, 6, 7 shift the center off 0 — they've moved to the Reach set below.)*

*Equations (give both solutions; check):*
1. |x| = 4
4. |2x| = 8
9. |x| = 7

*Inequalities (solve; describe the graph):*
8. |2x| < 6
10. |x| > 5
11. 2|x| ≤ 10
12. |x| < -2
13. |x| > -1

**Answer key (all verified):**
1. x = 4 or x = -4. (|4| = 4, |-4| = 4.)
4. x = 4 or x = -4. (|2·4| = 8, |2·(-4)| = 8.)
9. x = 7 or x = -7. (|7| = 7, |-7| = 7.)
8. -3 < x < 3 — |2x| < 6 ⇒ -6 < 2x < 6; open circles at -3 and 3, shade between (*and*).
10. x < -5 or x > 5 — "more than 5 from 0"; open circles at -5 and 5, shade outward (*or*).
11. -5 ≤ x ≤ 5 — isolate: divide by 2 → |x| ≤ 5; filled circles at -5 and 5, shade between.
12. **no solution** — a distance can't be less than -2.
13. **all real numbers** — every distance is more than -1.

---

### Reach beyond Algebra 1 (optional — off the mastery path)

When the center moves off 0 — |x − 3| = 5, |2x − 1| = 7 — you can't just read x = ±k. You split into **two cases** (the inside equals +k *or* −k), solve each, and name the answer set with **interval notation**. That general algebraic method is the standard **Algebra 2 / intermediate-algebra** treatment. It's here so you can see where the idea goes, but it is **not** part of the Algebra-1 mastery target — master the distance-from-0 core above first.

*The general method, one worked example.*

*w1 — |x − 3| = 5.* Two cases: x − 3 = 5 → x = 8, or x − 3 = -5 → x = -2. Solutions: **x = 8 or x = -2**. Check: |8 − 3| = 5, |-2 − 3| = 5. *(Pictured: "distance 5 from 3.")*

*A few more, same idea.*
*w2 — |x − 3| < 5.* Within 5 of 3 → -5 < x − 3 < 5 → -2 < x < 8 (interval (-2, 8)).
*w3 — |x − 3| > 5.* More than 5 from 3 → x − 3 < -5 or x − 3 > 5 → x < -2 or x > 8.
*w4 — |x + 2| = 3.* |x + 2| = |x − (-2)|, distance 3 from -2 → x = 1 or x = -5.

*Reach practice (optional):*
2. |x + 2| = 3
3. |x - 1| = 4
5. |2x - 1| = 7
6. |x + 1| < 3
7. |x - 2| ≥ 4

**Reach answer key:**
2. x = 1 or x = -5. (|1+2| = 3, |-5+2| = 3.)
3. x = 5 or x = -3. (|5-1| = 4, |-3-1| = 4.)
5. x = 4 or x = -3. (2x-1 = 7 → x = 4; 2x-1 = -7 → x = -3.)
6. -4 < x < 2 — "within 3 of -1"; interval (-4, 2).
7. x ≤ -2 or x ≥ 6 — "at least 4 from 2"; two rays.

---

## Lesson 8.4: Graphing linear inequalities (two variables) & systems

**Goal:** Graph a two-variable linear inequality (boundary line + shaded half-plane) and find the solution region of a system of inequalities (the overlap).
**Why it matters:** It generalizes "the line is the solution" (Unit 5) to "a whole region is the solution," and it's the picture behind constraints and optimization (which combination of two quantities is *allowed*).
**New terms:**
- {#8.4.d1} **Linear inequality in two variables:** e.g. y > 2x + 1 — satisfied not by a line but by a **half-plane** (every point on one side of the boundary).
- {#8.4.d2} **Boundary line:** the line you get by replacing the inequality with = (here y = 2x + 1, the function f(x) = 2x+1). **Dashed** if strict (<, >) — the line itself is *not* included; **solid** if inclusive (≤, ≥).
- {#8.4.d3} **Half-plane / test point:** one of the two sides the boundary cuts the plane into. To choose the correct side, **test a point** not on the line — the **origin (0,0)** is easiest — and shade the side that makes the inequality true.
- {#8.4.d4} **System of inequalities:** two or more inequalities at once; the solution is the **overlap** of their shaded regions.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete / symbolic:** y > 2x + 1 asks "where is the output **above** the line y = 2x+1?" The boundary splits "above" from "below."
- **Pictorial (the procedure):**
  1. Graph the **boundary** (Unit 5 — compute two points; **dashed** for </>, **solid** for ≤/≥).
  2. **Test a point** off the line (use (0,0) unless the line passes through it). If it makes the inequality **true**, shade **its** side; if **false**, shade the **other** side.
  3. **Say the test out loud** in words ("(0,0): 0 > 1? false → shade the *other* side").
- Use `visuals.md` **Template 4** — a **computed SVG artifact**: boundary line + semi-transparent fill, with the test point and its true/false result stated. **Compute the boundary points** (`visuals.md` rule 1), never eyeball.
- **Systems:** graph each inequality's region, then keep only the **overlap** — the points satisfying *all* of them at once.

**Worked examples:**

*Example 1 — strict, dashed.* Graph y > 2x + 1.
Boundary y = 2x + 1 (points (0,1) and (1,3)), **dashed** (strict).
Test (0,0): 0 > 2(0)+1 = 1? **False** → shade the side **not** containing the origin (above the line). Region: everything above the dashed line.

*Example 2 — inclusive, solid.* Graph y ≤ -x + 3.
Boundary y = -x + 3 (points (0,3) and (3,0)), **solid** (inclusive).
Test (0,0): 0 ≤ -0 + 3 = 3? **True** → shade the side **containing** the origin (below the line). Region: the line and everything below it.

*Example 3 — fractional slope, dashed.* Graph y < (1/2)x - 2.
Boundary y = (1/2)x - 2 (points (0,-2) and (2,-1)), **dashed**.
Test (0,0): 0 < (1/2)(0) - 2 = -2? **False** → shade the **other** side (below the line). Region: below the dashed line.

*Example 4 — a system.* Graph the system y ≥ x - 1 **and** y ≤ -x + 3.
Boundary 1: y = x - 1, **solid**; test (0,0): 0 ≥ -1? **True** → shade the side with the origin (above/left).
Boundary 2: y = -x + 3, **solid**; test (0,0): 0 ≤ 3? **True** → shade the side with the origin (below/left).
**Solution = the overlap** of the two shaded regions (a wedge containing the origin, bounded by both solid lines, e.g. the point (0,0) satisfies both). Check a point in the overlap, e.g. (1,0): 0 ≥ 1-1=0 and 0 ≤ -1+3=2.

**Watch for:**
- **Dashed vs. solid:** strict (<, >) → **dashed** (boundary excluded); inclusive (≤, ≥) → **solid**. Mirrors the open/filled circle from 8.1.
- **Shading the wrong half.** The only reliable cure is to **test a point and state the result** — don't guess from the inequality direction (a > does *not* always mean "shade up" once the line tilts). If the boundary passes through the origin, pick a different test point (e.g. (1,0)).
- **For a system, shading each region but forgetting the answer is the *overlap*** — not the union. Confirm by testing a point that should be inside *all* of them.
- **Sign slips computing boundary points** (`misconceptions.md` §3) — compute, don't eyeball (`visuals.md`).

**Visuals to offer:** {#8.4.f1} `visuals.md` **Template 4** as an **SVG artifact** — computed boundary line (dashed/solid), semi-transparent fill on the correct side, the test point and its true/false stated in the caption. For a system, layer the regions and highlight the overlap. Never paste raw SVG into chat — emit an artifact, and pair with a sentence naming the test point.

**Check for understanding (transfer):**
1. {#8.4.c1} "For y < x + 4: is the boundary dashed or solid, and how do you decide which side to shade? Do the origin test out loud."
2. {#8.4.c2} "Your boundary line passes through (0,0). Why can't you use the origin as your test point, and what would you use instead?"
3. {#8.4.c3} "A system is y > x and y < 4. Describe the solution region — which two boundaries, dashed or solid, and roughly where the overlap sits."

**Practice problems** (for each: name the boundary line, dashed or solid, the test point with its true/false result, and which side to shade):

*Set A — single inequalities*
1. y > x + 2
2. y ≤ 2x - 1
3. y < -x + 4
4. y ≥ 3x  *(boundary through origin — choose a different test point)*
5. x + y < 5

*Set B — a system*
6. y > x **and** y < -x + 4  *(describe the overlap region)*

*Set C — boundary arithmetic (eval)*
7. For the boundary y = 2x - 3, compute y at x = 2 (a point to plot).

**Answer key (all verified):**
1. Boundary y = x + 2 (e.g. (0,2),(1,3)), **dashed**. Test (0,0): 0 > 2? **false** → shade the side **without** the origin (above the line).
2. Boundary y = 2x - 1 ((0,-1),(1,1)), **solid**. Test (0,0): 0 ≤ -1? **false** → shade the **other** side (below the line).
3. Boundary y = -x + 4 ((0,4),(4,0)), **dashed**. Test (0,0): 0 < 4? **true** → shade the side **with** the origin (below/left).
4. Boundary y = 3x ((0,0),(1,3)), **solid**. Origin is *on* the line — test (1,0): 0 ≥ 3(1)=3? **false** → shade the side **not** containing (1,0): the side holding points like (0,1) and (-1,0) — above/left of the steep line. *(For a steep line, locate the region by a true in-region point, not "left/right" — the Watch-for warning in action.)*
5. Boundary x + y = 5 ((0,5),(5,0)), **dashed**. Test (0,0): 0 + 0 = 0 < 5? **true** → shade the side **with** the origin (below/left).
6. Boundary 1 y = x, **dashed**, shade above (test (0,1): 1 > 0). Boundary 2 y = -x + 4, **dashed**, shade below (test (0,0): 0 < 4). **Solution = the overlap**, a wedge between the two dashed lines (e.g. (1,2): 2 > 1 and 2 < 3).
7. y = 2(2) - 3 = 1 → plot (2, 1).

---

## Wrap-up & interleaving

**Consolidate:** An inequality's solution is a **set** (a shaded ray, segment, region) — not a single value. Solve like an equation, with the one new rule: **multiply/divide by a negative ⇒ flip the sign** — justified by the 2<3 → -2 > -3 argument, and **confirmed by testing a point in the original** (`misconceptions.md` §6). Graph with open/filled circles (strict/inclusive) and a shaded ray. **And** = overlap (between); **or** = union (two rays). **Absolute value** = distance from 0 → two cases for "=", "within" is an *and*, "outside" is an *or*. In **two variables**, the boundary is dashed (strict) or solid (inclusive), and a **test point** picks the half-plane; a **system** is the overlap of regions.

**Mix back in (spaced review, per `pedagogy.md`):**
- **Unit 2** — every inequality solve *is* a Unit 2 equation solve plus the flip rule; warm up with a plain two-step equation, then make it an inequality.
- **Unit 5** — graphing a 2-D inequality is Unit 5 line-graphing plus a shade; have the student graph the boundary *as a line* first. Reinforce "the boundary *is* a function, f(x) = mx + b."
- **Negatives (`misconceptions.md` §3)** — the flip, the -x trap, and boundary-point arithmetic all lean on sign fluency; slip in a sign-heavy warm-up.
- Interleave **and/or** classification and **within/outside** absolute-value reading, since both hinge on the same intersection-vs-union idea.

**Progress Card should note:** whether the student **flips reliably** on negative coefficients and **tests a point** without prompting (the §6 self-check); whether they pick **open vs. filled** circles and **dashed vs. solid** boundaries correctly; whether they distinguish **and (overlap)** from **or (union)**; whether they read **absolute value as distance** and map "within→and / outside→or"; and whether, for 2-D systems, they take the **overlap** (not the union) and **state the test point**. Flag lingering sign slips (`misconceptions.md` §3) for targeted warm-ups.
