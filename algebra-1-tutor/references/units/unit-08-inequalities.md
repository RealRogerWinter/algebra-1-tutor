# Unit 8: Inequalities

> **Prerequisites:** Unit 2 (solving one- and two-step equations; the balance-scale meaning of `=`) and Unit 5 (the coordinate plane, slope, and graphing \(y = mx + b\)). Comfort with negatives (Unit 1 / `misconceptions.md` §3) is leaned on heavily here.
> **By the end, the student can:**
> - Read and write the four inequality symbols \(<, \le, >, \ge\) and explain that a solution is a **set** of many values, not a single number.
> - Solve a linear inequality like an equation, applying the **sign-flip rule** when multiplying or dividing by a negative — *and explain why it must flip*.
> - **Graph** an inequality on a number line (open vs. filled circle, shade the ray) and self-check by **testing a point**.
> - Solve and graph **compound** inequalities (*and* = between; *or* = union).
> - Solve **absolute-value** equations and inequalities, reading \(|x|\) as distance from 0.
> - **Graph a two-variable linear inequality** (dashed/solid boundary, shade the correct half-plane via a test point) and find the solution region of a **system** of inequalities.

## Teaching this unit (orientation for the tutor)

Inequalities are "equations with a direction." Almost everything from Unit 2 transfers — isolate the variable with balanced moves — with **one** new rule that causes the overwhelming majority of errors: **multiplying or dividing both sides by a negative reverses the inequality sign.** This is the central trap of the unit (`misconceptions.md` §6). Do not teach it as a rule to memorize; teach the **why**, then the **self-check**:

- **The why:** start from something obviously true, \(2 < 3\). Multiply both sides by \(-1\): you get \(-2\) and \(-3\). Is \(-2 < -3\)? No — \(-2\) is the *bigger* number. To keep a true statement, the sign had to flip: \(-2 > -3\). The flip isn't a trick; it's what keeps the statement true.
- **The self-check (works every time):** after solving, **test a point**. Put a number from your answer set into the *original* inequality. If it makes the original true, good; if the original is true at \(x = 0\) but \(0\) isn't in your answer, a flip went missing. Model this on every negative-coefficient problem (`misconceptions.md` §6).

The second persistent fuzziness is what a **solution set** *means*: an equation usually has one answer; an inequality has infinitely many, which is exactly why we **graph** it (a shaded ray, not a dot). Keep tying the algebra to the number-line picture.

**The arc.** **8.1** builds one-variable solving + number-line graphing + the flip. **8.2** chains two conditions (*and*/*or*). **8.3** reframes through *distance from 0* — absolute value — where "within" becomes an *and* and "outside" becomes an *or* (a direct payoff of 8.2). **8.4** lifts everything into two variables: a line splits the plane, you shade a half, and a **system** is the overlap. Thread **function language** where natural: a boundary like \(y = 2x+1\) *is* the function \(f(x) = 2x+1\); the inequality \(y > 2x+1\) asks "where is the output *above* the line?"

**Pacing.** Spend real time on the flip in 8.1 until the *test-a-point* habit is automatic — it pays off in 8.2 and 8.3. Don't drill number-line drawing to exhaustion; its job is meaning. In 8.4, precision matters less than three correct decisions: dashed-vs-solid, which side, and stating the test point out loud.

---

## Lesson 8.1: One-variable inequalities

**Goal:** Solve a linear inequality in one variable (including the negative-coefficient flip) and graph its solution set on a number line.
**Why it matters:** Real constraints are rarely "exactly equal" — *at least* \$20, *no more than* 8 hours, *under* the speed limit. Inequalities are how we solve "how much is enough / too much," and the solution is a whole range of acceptable values.
**New terms:**
- **Inequality:** a statement that two quantities are *not* (necessarily) equal, using \(<\) (less than), \(>\) (greater than), \(\le\) (less than *or equal to*), or \(\ge\) (greater than or equal to).
- **Solution set:** *all* the values that make the inequality true — usually infinitely many, drawn as a shaded ray.
- **Strict** (\(<, >\)) vs. **inclusive** (\(\le, \ge\)): whether the boundary value itself counts.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** "‘You must be **at least** 13’ — is 13 allowed? Is 20? Is 12? That's \(\text{age} \ge 13\): a whole crowd of allowed numbers, not one." Contrast with an equation (one answer). Anchor \(\le/\ge\) to "*or equal to* = the boundary is invited in."
- **Pictorial:** The solution lives on a **number line**. **Open circle** \(\circ\) at the boundary for strict (\(<, >\)) — "the boundary itself is *not* included"; **filled circle** \(\bullet\) for inclusive (\(\le, \ge\)) — "included." Then **shade the ray** toward all the values that work. Use the ASCII number lines in `visuals.md` (the \(x>2\) and \(x \le -1\) sketches) for in-chat, or **Template 1** for a polished SVG artifact. Always say in words what the picture shows.
- **Symbolic:** Solve *exactly like an equation* (Unit 2 balanced moves) with **one** added rule: **if you multiply or divide both sides by a negative, flip the inequality sign.** Adding/subtracting, or multiplying/dividing by a *positive*, never flips it.

Teach the flip's **why** (the \(2<3 \to -2 \mathbin{?} -3\) argument above, `misconceptions.md` §6), then close every problem with **test a point**.

**Worked examples:**

*Example 1 — no flip.* Solve \(x + 3 < 7\).
Subtract 3 from both sides: \(x < 4\).
Graph: **open circle** at 4 (strict), shade **left** (toward smaller values).
Test a point: try \(x = 0\). Original: \(0 + 3 = 3 < 7\), and \(0 < 4\) — agree. Solution: \(\boxed{x < 4}\).

*Example 2 — two steps, no flip.* Solve \(2x - 1 \ge 5\).
Add 1: \(2x \ge 6\). Divide by **\(+2\)** (positive → no flip): \(x \ge 3\).
Graph: **filled circle** at 3 (inclusive), shade **right**.
Test \(x = 4\): \(2(4) - 1 = 7 \ge 5\), and \(4 \ge 3\). Solution: \(\boxed{x \ge 3}\).

*Example 3 — the flip.* Solve \(-2x < 6\).
Divide both sides by **\(-2\)** → **flip** the sign: \(x > -3\).
Graph: **open circle** at \(-3\), shade **right**.
Test \(x = 0\): original \(-2(0) = 0 < 6\); is \(0 > -3\)? — agree. (Had we forgotten to flip and written \(x < -3\), then \(0\) would be *excluded* even though it makes the original true — the test catches it.) Solution: \(\boxed{x > -3}\).

*Example 4 — the \(-x\) trap.* Solve \(5 - x > 2\).
Subtract 5: \(-x > -3\). Now divide by \(-1\) → **flip**: \(x < 3\).
Test \(x = 0\): \(5 - 0 = 5 > 2\); is \(0 < 3\)?. Solution: \(\boxed{x < 3}\).
*(Alternative that avoids a negative coefficient: add \(x\) to both sides → \(5 > 2 + x\) → \(3 > x\), i.e. \(x < 3\). Same answer; show this as the flip-free route.)*

**Watch for:**
- **The missing flip** (`misconceptions.md` §6) — the unit's headline error. Tell: \(-2x < 6 \Rightarrow x < -3\). Repair with the \(2<3\) argument *and* the test-a-point check, not a louder restatement.
- **Mishandling \(-x\)** in \(5 - x > 2\) (writing \(x > 3\)). Same root; the test-a-point check exposes it.
- **Open vs. filled circle** confusion — \(\le/\ge\) get a **filled** dot ("equal is included"), \(<\!/\!>\) an **open** one.
- **Treating it like an equation with one answer** — push "name three numbers that work" to surface the *set*.

**Visuals to offer:** ASCII number line in chat for quick feedback (the \(x>2\)/\(x\le-1\) sketches in `visuals.md`), or **Template 1** (SVG artifact) for a polished line — open vs. filled endpoint, shaded ray, boundary labeled. Always pair with a sentence.

**Check for understanding (transfer):**
1. "Solve \(-3x \ge 12\), then test \(x = -5\) in the *original*. Walk me through how the test confirms (or would catch a mistake in) your answer."
2. "Two students solve \(-x < 4\). One writes \(x < -4\), the other \(x > -4\). Using \(x = 0\), decide who's right and explain how you know."
3. "In words, describe the number-line graph of \(x \le 2\): which circle, filled or open, and which direction do you shade?"

**Practice problems** (solve; then describe the number-line graph in words — which circle and which way you shade):

*Set A — no flip*
1. \(x - 2 < 3\)
2. \(x + 5 \le 2\)
3. \(3x > 12\)
4. \(\dfrac{x}{2} \ge 4\)
5. \(2x + 1 \le 9\)
6. \(4x - 3 > 9\)

*Set B — requires a flip (multiply/divide by a negative)*
7. \(-x < 4\)
8. \(-3x \le 9\)
9. \(-x + 2 < 5\)
10. \(10 - 2x \ge 4\)
11. \(3 - x \le 7\)
12. \(-4x \le -8\)

*Set C — read the graph (manual)*
13. A number line shows an **open** circle at \(1\) shaded to the **right**. Write the inequality.
14. A number line shows a **filled** circle at \(-2\) shaded to the **left**. Write the inequality.

**Answer key (all verified):**
1. \(x < 5\) — open circle at 5, shade left.
2. \(x \le -3\) — filled circle at \(-3\), shade left.
3. \(x > 4\) — open circle at 4, shade right.
4. \(x \ge 8\) — filled circle at 8, shade right.
5. \(x \le 4\) — filled circle at 4, shade left.
6. \(x > 3\) — open circle at 3, shade right.
7. \(x > -4\) — **flip** (÷ by \(-1\)); open circle at \(-4\), shade right. *(Test \(x=0\): \(-0<4\), \(0>-4\).)*
8. \(x \ge -3\) — **flip** (÷ by \(-3\)); filled circle at \(-3\), shade right.
9. \(x > -3\) — subtract 2 → \(-x < 3\) → **flip** → \(x > -3\); open circle at \(-3\), shade right.
10. \(x \le 3\) — subtract 10 → \(-2x \ge -6\) → **flip** (÷ by \(-2\)) → \(x \le 3\); filled circle at 3, shade left.
11. \(x \ge -4\) — subtract 3 → \(-x \le 4\) → **flip** → \(x \ge -4\); filled circle at \(-4\), shade right.
12. \(x \ge 2\) — divide by \(-4\) → **flip** → \(x \ge 2\); filled circle at 2, shade right. *(Test \(x=2\): \(-8 \le -8\).)*
13. \(x > 1\) (open + right = strict greater-than).
14. \(x \le -2\) (filled + left = inclusive less-than-or-equal).

---

## Lesson 8.2: Compound inequalities

**Goal:** Solve and graph compound inequalities joined by **and** (intersection — *between*) or **or** (union — two separate rays).
**Why it matters:** Real constraints often come in pairs — "between 60 and 80," "older than 12 **or** with a guardian." *And* narrows; *or* widens.
**New terms:**
- **Compound inequality:** two inequalities combined into one statement.
- **And (intersection):** *both* parts must hold. \(2 < x \le 5\) is shorthand for \(x > 2\) **and** \(x \le 5\) — the values **between** 2 and 5 (with 5 included). On the line, the **overlap** of the two shaded regions — a single segment.
- **Or (union):** *at least one* part holds. \(x < -1\) **or** \(x > 3\) — **everything** in either ray; the two pieces don't touch.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** *And* = "you must clear **both** bars" (narrows to the overlap). *Or* = "clear **either** bar" (widens to the union). "Temperature between 60 and 80" is an *and*; "under 32 or over 100" is an *or*.
- **Pictorial:** Shade each condition on the same number line. *And* keeps only where the shadings **overlap** (a between-segment, two endpoints). *Or* keeps **everything** shaded by either (two rays heading opposite ways). Endpoints follow 8.1's open/filled rule per symbol.
- **Symbolic:** A three-part *and* like \(-1 < x + 2 < 4\) is solved by doing the **same move to all three parts** at once. An *or* is solved as **two separate** inequalities, then unioned.

**Worked examples:**

*Example 1 — "and" (three-part).* Solve \(-1 < x + 2 < 4\).
Subtract 2 from **all three** parts: \(-1 - 2 < x < 4 - 2\), i.e. \(-3 < x < 2\).
Graph: open circles at \(-3\) and \(2\), shade the segment **between**.
Test \(x = 0\) (inside): \(-1 < 0+2=2 < 4\). Solution: \(\boxed{-3 < x < 2}\).

*Example 2 — "and" with a division.* Solve \(3 \le 2x - 1 \le 9\).
Add 1 to all parts: \(4 \le 2x \le 10\). Divide all by \(+2\) (positive → no flip): \(2 \le x \le 5\).
Graph: filled circles at 2 and 5, shade between. Solution: \(\boxed{2 \le x \le 5}\).

*Example 3 — "or".* Solve \(x < -1\) **or** \(x > 3\).
Already solved — two rays. Graph: open circle at \(-1\) shading **left**, open circle at 3 shading **right**; nothing in the middle. Solution: \(\boxed{x < -1 \text{ or } x > 3}\).

*Example 4 — "or" needing work.* Solve \(2x \le -4\) **or** \(x - 3 > 2\).
Left: \(x \le -2\). Right: \(x > 5\). Graph: filled circle at \(-2\) shading left, open circle at 5 shading right. Solution: \(\boxed{x \le -2 \text{ or } x > 5}\).

**Watch for:**
- **Confusing *and* with *or*.** *And* = overlap (between, narrower); *or* = union (two rays, wider). If a student shades the whole line for an *and*, they've unioned by mistake.
- **In a three-part *and*, only changing the middle.** Whatever you do, do it to **all three** parts (`misconceptions.md` §1 — balance applies across the whole statement).
- **The flip still applies** to compound inequalities — dividing the three-part statement by a negative flips **both** signs (turning \(a < x < b\) into \(b > x > a\)). Same self-check: test a point.
- **Writing an empty *and* as if it had answers** — e.g. \(x > 5\) **and** \(x < 1\) has *no* solution (no overlap). Worth one example if it arises.

**Visuals to offer:** ASCII number lines (one segment for *and*, two rays for *or*), or two endpoints on **Template 1**. Show *and* and *or* on stacked lines so the contrast is visible. Pair with words.

**Check for understanding (transfer):**
1. "Rewrite \(2 < x \le 5\) as two separate inequalities joined by a word. Which word, and why is the graph a single segment instead of two rays?"
2. "Why does \(x > 5\) **and** \(x < 1\) have no solution, while \(x > 5\) **or** \(x < 1\) has lots? Describe both graphs."
3. "You solve a three-part inequality and divide all parts by \(-2\). What happens to the two inequality signs, and how would testing a point confirm it?"

**Practice problems** (solve and describe the graph: segment-between for *and*, two rays for *or*):

*Set A — "and"*
1. \(-2 < x - 1 < 3\)
2. \(0 \le x + 1 \le 4\)
3. \(3 \le 2x - 1 \le 9\)
4. \(-4 < 2x < 6\)

*Set B — "or"*
5. \(x < -1\) or \(x > 5\)
6. \(x + 1 < 0\) or \(x - 3 > 2\)
7. \(2x \le -4\) or \(x > 3\)
8. \(x - 3 \ge 2\) or \(x < -2\)

**Answer key (all verified):**
1. \(-1 < x < 4\) — add 1 to all parts; open circles at \(-1\) and 4, shade between.
2. \(-1 \le x \le 3\) — subtract 1 from all parts; filled circles at \(-1\) and 3, shade between.
3. \(2 \le x \le 5\) — add 1, divide by 2; filled circles at 2 and 5, shade between.
4. \(-2 < x < 3\) — divide all by 2; open circles at \(-2\) and 3, shade between.
5. \(x < -1\) or \(x > 5\) — two rays (open at \(-1\) left, open at 5 right).
6. \(x < -1\) or \(x > 5\) — left: \(x<-1\); right: \(x>5\); two rays.
7. \(x \le -2\) or \(x > 3\) — filled at \(-2\) left, open at 3 right.
8. \(x \ge 5\) or \(x < -2\) — filled at 5 right, open at \(-2\) left.

---

## Lesson 8.3: Absolute-value equations & inequalities

**Goal:** Solve \(|expression| = k\), \(|expression| < k\), and \(|expression| > k\) by reading absolute value as **distance from 0**.
**Why it matters:** Absolute value measures *how far*, regardless of direction — error tolerance ("within 0.5 of target"), distance, magnitude. It's also the cleanest place to *see* why "within" is an *and* and "outside" is an *or* (payoff of 8.2).
**New terms:**
- **Absolute value \(|x|\):** the distance of \(x\) from 0 on the number line. Always \(\ge 0\). \(|5| = 5\) and \(|-5| = 5\) — both are 5 units from 0.
- \(|x - a|\): the distance between \(x\) and \(a\). So \(|x - 3| = 5\) reads "\(x\) is **5 units from 3**."

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete / pictorial:** Put it on the number line. \(|x - 3| = 5\): start at 3, step 5 units **each way** → \(x = 8\) or \(x = -2\). *Two* answers, because distance ignores direction. This picture *is* the method.
- **From the picture to inequalities:**
  - \(|x - 3| < 5\): "**within** 5 of 3" → the points **between** \(-2\) and \(8\) → \(-2 < x < 8\). "Within" → an **and** (8.2).
  - \(|x - 3| > 5\): "**more than** 5 from 3" → the points **outside** that band → \(x < -2\) **or** \(x > 8\). "Outside" → an **or** (8.2).
- **Symbolic shortcut (after the picture lands):** \(|A| = k \Rightarrow A = k\) or \(A = -k\). \(|A| < k \Rightarrow -k < A < k\) (and). \(|A| > k \Rightarrow A < -k\) or \(A > k\) (or). (Requires \(k > 0\); see the watch-for.)

**Worked examples:**

*Example 1 — equation.* Solve \(|x - 3| = 5\).
"Distance 5 from 3": \(x - 3 = 5 \Rightarrow x = 8\), or \(x - 3 = -5 \Rightarrow x = -2\). Solutions: \(\boxed{x = 8 \text{ or } x = -2}\).
Check: \(|8 - 3| = |5| = 5\), \(|-2 - 3| = |-5| = 5\).

*Example 2 — "within" (and).* Solve \(|x - 3| < 5\).
Within 5 of 3 → \(-5 < x - 3 < 5\). Add 3 to all parts: \(-2 < x < 8\).
Graph: open circles at \(-2\) and 8, shade between. Solution: \(\boxed{-2 < x < 8}\).

*Example 3 — "outside" (or).* Solve \(|x - 3| > 5\).
More than 5 from 3 → \(x - 3 < -5\) **or** \(x - 3 > 5\) → \(x < -2\) **or** \(x > 8\).
Graph: open circle at \(-2\) shading left, open circle at 8 shading right. Solution: \(\boxed{x < -2 \text{ or } x > 8}\).

*Example 4 — equation, shift inside.* Solve \(|x + 2| = 3\).
\(|x + 2| = |x - (-2)|\): distance 3 from \(-2\) → \(x = 1\) or \(x = -5\).
Check: \(|1 + 2| = 3\), \(|-5 + 2| = |-3| = 3\). Solutions: \(\boxed{x = 1 \text{ or } x = -5}\).

*Example 5 — inclusive "within".* Solve \(|x| \le 2\).
Within 2 of 0 (inclusive) → \(-2 \le x \le 2\). Filled circles at \(-2\) and 2, shade between. Solution: \(\boxed{-2 \le x \le 2}\).

**Watch for:**
- **Giving only one answer to \(|A| = k\).** Distance goes *both* ways — always two cases (unless \(k = 0\), one answer).
- **Dropping the negative case** or mishandling its sign: \(x - 3 = -5\) gives \(x = -2\), not \(x = 8\).
- **Swapping *and*/*or*:** "within / less-than" → **and** (between); "outside / greater-than" → **or** (two rays). Re-derive from the distance picture if unsure.
- **\(|A| = \) negative, or \(|A| < \) negative:** distance can't be negative. \(|x| = -4\) has **no solution**; \(|x| < -3\) has **no solution**; \(|x| > -3\) is **all reals**. Reason from the picture, don't apply the shortcut blindly.

**Visuals to offer:** A number line is ideal — mark the center (\(a\)), step \(k\) each way, dot the two solutions; for inequalities show the between-segment (*and*) or two rays (*or*). ASCII in chat, or **Template 1** artifact. Always state the distance interpretation in words.

**Check for understanding (transfer):**
1. "Read \(|x + 1| = 4\) as a distance sentence (from what number, how far?), then give both solutions."
2. "Why does \(|x - 2| < 4\) become an *and* (a single segment) while \(|x - 2| > 4\) becomes an *or* (two rays)? Use the distance picture."
3. "What is the solution of \(|x| = -3\)? Of \(|x| > -3\)? Explain each from ‘distance is never negative.’"

**Practice problems:**

*Set A — equations (give both solutions; check)*
1. \(|x| = 4\)
2. \(|x + 2| = 3\)
3. \(|x - 1| = 4\)
4. \(|2x| = 8\)
5. \(|2x - 1| = 7\)

*Set B — inequalities (solve; describe the graph)*
6. \(|x + 1| < 3\)
7. \(|x - 2| \ge 4\)
8. \(|2x| < 6\)

**Answer key (all verified):**
1. \(x = 4\) or \(x = -4\). (\(|4|=4\), \(|-4|=4\).)
2. \(x = 1\) or \(x = -5\). (\(|1+2|=3\), \(|-5+2|=3\).)
3. \(x = 5\) or \(x = -3\). (\(|5-1|=4\), \(|-3-1|=4\).)
4. \(x = 4\) or \(x = -4\). (\(|2\cdot4|=8\), \(|2\cdot(-4)|=8\).)
5. \(x = 4\) or \(x = -3\). (\(2x-1=7\Rightarrow x=4\); \(2x-1=-7\Rightarrow x=-3\). \(|7|=7\), \(|-7|=7\).)
6. \(-4 < x < 2\) — "within 3 of \(-1\)"; open circles at \(-4\) and 2, shade between (*and*).
7. \(x \le -2\) or \(x \ge 6\) — "at least 4 from 2"; filled circles at \(-2\) and 6, shade outward (*or*).
8. \(-3 < x < 3\) — \(|2x|<6 \Rightarrow -6 < 2x < 6\); open circles at \(-3\) and 3, shade between (*and*).

---

## Lesson 8.4: Graphing linear inequalities (two variables) & systems

**Goal:** Graph a two-variable linear inequality (boundary line + shaded half-plane) and find the solution region of a system of inequalities (the overlap).
**Why it matters:** It generalizes "the line is the solution" (Unit 5) to "a whole region is the solution," and it's the picture behind constraints and optimization (which combination of two quantities is *allowed*).
**New terms:**
- **Linear inequality in two variables:** e.g. \(y > 2x + 1\) — satisfied not by a line but by a **half-plane** (every point on one side of the boundary).
- **Boundary line:** the line you get by replacing the inequality with \(=\) (here \(y = 2x + 1\), the function \(f(x) = 2x+1\)). **Dashed** if strict (\(<, >\)) — the line itself is *not* included; **solid** if inclusive (\(\le, \ge\)).
- **Half-plane / test point:** one of the two sides the boundary cuts the plane into. To choose the correct side, **test a point** not on the line — the **origin \((0,0)\)** is easiest — and shade the side that makes the inequality true.
- **System of inequalities:** two or more inequalities at once; the solution is the **overlap** of their shaded regions.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete / symbolic:** \(y > 2x + 1\) asks "where is the output **above** the line \(y = 2x+1\)?" The boundary splits "above" from "below."
- **Pictorial (the procedure):**
  1. Graph the **boundary** (Unit 5 — compute two points; **dashed** for \(<\!/\!>\), **solid** for \(\le\!/\!\ge\)).
  2. **Test a point** off the line (use \((0,0)\) unless the line passes through it). If it makes the inequality **true**, shade **its** side; if **false**, shade the **other** side.
  3. **Say the test out loud** in words ("\((0,0)\): \(0 > 1\)? false → shade the *other* side").
- Use `visuals.md` **Template 4** — a **computed SVG artifact**: boundary line + semi-transparent fill, with the test point and its true/false result stated. **Compute the boundary points** (`visuals.md` rule 1), never eyeball.
- **Systems:** graph each inequality's region, then keep only the **overlap** — the points satisfying *all* of them at once.

**Worked examples:**

*Example 1 — strict, dashed.* Graph \(y > 2x + 1\).
Boundary \(y = 2x + 1\) (points \((0,1)\) and \((1,3)\)), **dashed** (strict).
Test \((0,0)\): \(0 > 2(0)+1 = 1\)? **False** → shade the side **not** containing the origin (above the line). Region: everything above the dashed line.

*Example 2 — inclusive, solid.* Graph \(y \le -x + 3\).
Boundary \(y = -x + 3\) (points \((0,3)\) and \((3,0)\)), **solid** (inclusive).
Test \((0,0)\): \(0 \le -0 + 3 = 3\)? **True** → shade the side **containing** the origin (below the line). Region: the line and everything below it.

*Example 3 — fractional slope, dashed.* Graph \(y < \tfrac{1}{2}x - 2\).
Boundary \(y = \tfrac12 x - 2\) (points \((0,-2)\) and \((2,-1)\)), **dashed**.
Test \((0,0)\): \(0 < \tfrac12(0) - 2 = -2\)? **False** → shade the **other** side (below the line). Region: below the dashed line.

*Example 4 — a system.* Graph the system \(y \ge x - 1\) **and** \(y \le -x + 3\).
Boundary 1: \(y = x - 1\), **solid**; test \((0,0)\): \(0 \ge -1\)? **True** → shade the side with the origin (above/left).
Boundary 2: \(y = -x + 3\), **solid**; test \((0,0)\): \(0 \le 3\)? **True** → shade the side with the origin (below/left).
**Solution = the overlap** of the two shaded regions (a wedge containing the origin, bounded by both solid lines, e.g. the point \((0,0)\) satisfies both). Check a point in the overlap, e.g. \((1,0)\): \(0 \ge 1-1=0\) and \(0 \le -1+3=2\).

**Watch for:**
- **Dashed vs. solid:** strict (\(<, >\)) → **dashed** (boundary excluded); inclusive (\(\le, \ge\)) → **solid**. Mirrors the open/filled circle from 8.1.
- **Shading the wrong half.** The only reliable cure is to **test a point and state the result** — don't guess from the inequality direction (a \(>\) does *not* always mean "shade up" once the line tilts). If the boundary passes through the origin, pick a different test point (e.g. \((1,0)\)).
- **For a system, shading each region but forgetting the answer is the *overlap*** — not the union. Confirm by testing a point that should be inside *all* of them.
- **Sign slips computing boundary points** (`misconceptions.md` §3) — compute, don't eyeball (`visuals.md`).

**Visuals to offer:** `visuals.md` **Template 4** as an **SVG artifact** — computed boundary line (dashed/solid), semi-transparent fill on the correct side, the test point and its true/false stated in the caption. For a system, layer the regions and highlight the overlap. Never paste raw SVG into chat — emit an artifact, and pair with a sentence naming the test point.

**Check for understanding (transfer):**
1. "For \(y < x + 4\): is the boundary dashed or solid, and how do you decide which side to shade? Do the origin test out loud."
2. "Your boundary line passes through \((0,0)\). Why can't you use the origin as your test point, and what would you use instead?"
3. "A system is \(y > x\) and \(y < 4\). Describe the solution region — which two boundaries, dashed or solid, and roughly where the overlap sits."

**Practice problems** (for each: name the boundary line, dashed or solid, the test point with its true/false result, and which side to shade):

*Set A — single inequalities*
1. \(y > x + 2\)
2. \(y \le 2x - 1\)
3. \(y < -x + 4\)
4. \(y \ge 3x\)  *(boundary through origin — choose a different test point)*
5. \(x + y < 5\)

*Set B — a system*
6. \(y > x\) **and** \(y < -x + 4\)  *(describe the overlap region)*

*Set C — boundary arithmetic (eval)*
7. For the boundary \(y = 2x - 3\), compute \(y\) at \(x = 2\) (a point to plot).

**Answer key (all verified):**
1. Boundary \(y = x + 2\) (e.g. \((0,2),(1,3)\)), **dashed**. Test \((0,0)\): \(0 > 2\)? **false** → shade the side **without** the origin (above the line).
2. Boundary \(y = 2x - 1\) (\((0,-1),(1,1)\)), **solid**. Test \((0,0)\): \(0 \le -1\)? **false** → shade the **other** side (below the line).
3. Boundary \(y = -x + 4\) (\((0,4),(4,0)\)), **dashed**. Test \((0,0)\): \(0 < 4\)? **true** → shade the side **with** the origin (below/left).
4. Boundary \(y = 3x\) (\((0,0),(1,3)\)), **solid**. Origin is *on* the line — test \((1,0)\): \(0 \ge 3(1)=3\)? **false** → shade the **other** side (below/right of the line).
5. Boundary \(x + y = 5\) (\((0,5),(5,0)\)), **dashed**. Test \((0,0)\): \(0 + 0 = 0 < 5\)? **true** → shade the side **with** the origin (below/left).
6. Boundary 1 \(y = x\), **dashed**, shade above (test \((0,1)\): \(1 > 0\)). Boundary 2 \(y = -x + 4\), **dashed**, shade below (test \((0,0)\): \(0 < 4\)). **Solution = the overlap**, a wedge between the two dashed lines (e.g. \((1,2)\): \(2 > 1\) and \(2 < 3\)).
7. \(y = 2(2) - 3 = 1\) → plot \((2, 1)\).

---

## Wrap-up & interleaving

**Consolidate:** An inequality's solution is a **set** (a shaded ray, segment, region) — not a single value. Solve like an equation, with the one new rule: **multiply/divide by a negative ⇒ flip the sign** — justified by the \(2<3 \to -2 > -3\) argument, and **confirmed by testing a point in the original** (`misconceptions.md` §6). Graph with open/filled circles (strict/inclusive) and a shaded ray. **And** = overlap (between); **or** = union (two rays). **Absolute value** = distance from 0 → two cases for "=", "within" is an *and*, "outside" is an *or*. In **two variables**, the boundary is dashed (strict) or solid (inclusive), and a **test point** picks the half-plane; a **system** is the overlap of regions.

**Mix back in (spaced review, per `pedagogy.md`):**
- **Unit 2** — every inequality solve *is* a Unit 2 equation solve plus the flip rule; warm up with a plain two-step equation, then make it an inequality.
- **Unit 5** — graphing a 2-D inequality is Unit 5 line-graphing plus a shade; have the student graph the boundary *as a line* first. Reinforce "the boundary *is* a function, \(f(x) = mx + b\)."
- **Negatives (`misconceptions.md` §3)** — the flip, the \(-x\) trap, and boundary-point arithmetic all lean on sign fluency; slip in a sign-heavy warm-up.
- Interleave **and/or** classification and **within/outside** absolute-value reading, since both hinge on the same intersection-vs-union idea.

**Progress Card should note:** whether the student **flips reliably** on negative coefficients and **tests a point** without prompting (the §6 self-check); whether they pick **open vs. filled** circles and **dashed vs. solid** boundaries correctly; whether they distinguish **and (overlap)** from **or (union)**; whether they read **absolute value as distance** and map "within→and / outside→or"; and whether, for 2-D systems, they take the **overlap** (not the union) and **state the test point**. Flag lingering sign slips (`misconceptions.md` §3) for targeted warm-ups.
