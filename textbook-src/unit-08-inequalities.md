# Unit 8: Inequalities

> This unit is about the math of "enough," "at most," and "in range." A lot of real life isn't one exact number but a whole range of values that work, and inequalities are how you write that down and reason about it. If your arithmetic with negative numbers feels a little rusty, a quick warm-up there will help, since negatives show up often.

Here's a habit worth keeping for this unit and the rest of the book. Before you start a new lesson, redo two or three problems from a lesson or two back from memory first.

It feels like a detour and it isn't. Pulling a method back from memory is a few minutes well spent, and it's a big part of why a skill is still there next week.

An inequality is an equation with a direction. Almost everything you already do to solve an equation carries straight over: isolate the variable with balanced moves.

There's exactly one new rule, and it's the source of most slips in the whole unit. So the first lesson spends its time on that rule, and on a check that catches it every time.

After that, the unit chains two conditions together, reads absolute value as plain distance, and finally lifts the whole picture into two variables, where the answer becomes a shaded region instead of a line.

---

## Lesson 8.1: One-variable inequalities

Real limits are rarely "exactly equal." You need *at least* $20 for the ticket, *no more than* 8 hours in the workday, a speed *under* the limit. Each of those describes a whole range of acceptable values, not one magic number, and that range is what an inequality is for.

Start with something you can picture: a sign at a ride that says "you must be at least 13." Is a 13-year-old allowed on? Yes. "At least 13" invites 13 itself in. Is a 20-year-old allowed? Yes. Is a 12-year-old? No.

So the rule doesn't pick out one age. It lets in a whole crowd of them, everyone from 13 upward. Write the age as a and that's a ≥ 13.

This is the first real difference from an equation. An equation like a = 13 has one answer. An inequality has many, and that's normal, not a sign something went wrong.

Each of the four signs is just a way of saying which numbers are let in:

- a < 13 means *less than* 13: everyone under 13, but not 13 itself.
- a > 13 means *greater than* 13: everyone over 13, but not 13 itself.
- a ≤ 13 means *less than or equal to* 13: under 13, and 13 too.
- a ≥ 13 means *greater than or equal to* 13: over 13, and 13 too.

The little line under ≤ and ≥ is doing real work: it's the "or equal to," and it's what invites the boundary number itself into the crowd. A sign without the line (< or >) leaves the boundary out. That one distinction shapes the picture you're about to draw, so read the sign slowly and ask, every time: is the boundary invited in, or not?

Here's the picture. The answer to an inequality lives on a number line, as a shaded stretch of it. You mark the boundary with a circle, and the circle tells you whether the boundary counts. An **open circle** (a hollow ○) sits at the boundary when the sign is strict, < or >, meaning the boundary itself is *not* included. A **filled circle** (a solid ●) sits there when the sign is inclusive, ≤ or ≥, meaning it *is* included. Then you shade the ray, the whole run of numbers that work, in the direction of the values that make the statement true. For x ≤ 2, that's a filled circle at 2 and shading running left, off toward the smaller numbers, because every number 2 and below belongs {#8.1.f1}.

Now the symbols. You solve an inequality almost exactly like an equation. Use the same balanced moves from Unit 2, whatever you do to one side you do to the other, to get the variable alone. Adding or subtracting from both sides never changes the direction. Multiplying or dividing both sides by a *positive* number never changes it either. There is one move, and only one, that does.

That one move: if you multiply or divide both sides by a *negative* number, the inequality sign flips. Less-than becomes greater-than, and the other way around. This is the rule that trips people, so don't take it on faith. Look at why it has to be true. Start with something nobody would argue with:
$$2 < 3$$
Plainly true. Now multiply both sides by −1, which turns the 2 into −2 and the 3 into −3. Is −2 < −3? No. Owing $2 leaves you better off than owing $3, so −2 is the *bigger* number here. The statement 2 < 3 was true, and to keep it true after multiplying by the negative, the sign has to turn around:
$$2 < 3 \;\xrightarrow{\;\times(-1)\;}\; -2 > -3$$
So the flip isn't a trick to memorize. It's the only way the statement stays honest when a negative reverses which side is bigger.

And here's the habit that makes this whole lesson safe: after you solve, **test a point**. Take any number from your answer set, put it back into the *original* inequality, and check that it makes a true statement. If it does, you can trust your answer.

And if you ever forget the flip, the test catches it. A number that clearly should work won't, and that mismatch is your signal to look again.

Read each worked example slowly, a line at a time, and ask why each line follows from the one before it. That's what turns a worked example into something you can actually reuse.

**Worked examples:**

{#8.1.w1}
*Example 1, no flip.* Solve x + 3 < 7.
The +3 is added onto x, so undo it: subtract 3 from both sides, which sends the +3 to zero and leaves x alone. That gives x < 4. The sign didn't move, because subtracting doesn't flip it.
Graph: an open circle at 4, since < leaves the boundary out, and shade left toward the smaller values.
Now test a point. Try x = 0, which is in "x < 4." Back in the original: 0 + 3 = 3, and 3 < 7 is true. (And 0 < 4 fits the answer too.) So the answer holds: **x < 4**.

{#8.1.w2}
*Example 2, two steps, no flip.* Solve 2x − 1 ≥ 5.
Undo the −1 first by adding 1 to both sides: 2x ≥ 6. Now x is multiplied by 2, so divide both sides by 2 to free it. You're dividing by a *positive* 2, so the sign stays put: x ≥ 3.
Graph: a filled circle at 3, since ≥ includes the boundary, and shade right.
Test x = 4: in the original, 2(4) − 1 = 8 − 1 = 7, and 7 ≥ 5 is true; and 4 ≥ 3 fits. Solution: **x ≥ 3**.

If a test ever *doesn't* come out true, you haven't failed. Your check just did its job and caught something before it counted. That's exactly what it's for. Go back to your first step and re-run the arithmetic slowly. A mismatch is almost always one small slip, often a dropped sign or a flip you missed, not the whole method coming apart.

Now the move worth slowing down for. With a *positive* coefficient, an inequality behaves just like an equation. The moment a *negative* coefficient appears, the flip enters.

{#8.1.w3}
*Example 3, the flip.* Solve −2x < 6.
Here x is multiplied by −2, so divide both sides by −2 to free it. Dividing by a negative flips the sign, so < becomes >: x > −3.
Graph: an open circle at −3, and shade right.
Test x = 0, which is in "x > −3": the original is −2(0) = 0, and 0 < 6 is true; and 0 > −3 fits. Solution: **x > −3**.

This is where testing a point earns its keep. Had you forgotten to flip and written x < −3, then 0 would be shut out of your answer, even though 0 plainly makes the original true. The test would have caught the missing flip on the spot.

A bare −x, as in the next example, hides the same trap. Reading −x as "negative x" can tempt you to leave the sign alone, but −x is −1 times x, and undoing that −1 means dividing by a negative, so the flip still applies.

{#8.1.w4}
*Example 4, the −x trap.* Solve 5 − x > 2.
Subtract 5 from both sides: −x > −3. Now x is multiplied by −1, so divide both sides by −1, and that flips the sign: x < 3.
Test x = 0: in the original, 5 − 0 = 5, and 5 > 2 is true; and 0 < 3 fits. Solution: **x < 3**.
There's a tidy way to dodge the negative coefficient entirely: add x to both sides first, giving 5 > 2 + x, then subtract 2 to get 3 > x, which reads as x < 3, the same answer with no flip to remember. Two honest routes, same checked result.

When a problem hands you a −x, you can flip carefully, or you can move the variable to the other side so its coefficient is positive. The choice is yours, and picking the one that feels cleaner to you is a real strategy, not a shortcut.

Here's a clean one to get the method moving before the practice mixes things up. Solve 3x > 12: x is multiplied by 3, so divide both sides by the positive 3, no flip, and x > 4. Open circle at 4, shade right. Test x = 5: 3(5) = 15 > 12, true. Nothing tricky here, just the undo move, once, with a positive coefficient.

One way people get stuck early is treating an inequality like it has a single answer. It doesn't. A quick way to feel the difference: after you solve, name three different numbers from your answer set and check that each one works in the original. Three numbers, all true. That's the *set* the shaded ray stands for.

**New terms:**
- {#8.1.d1} **Inequality:** a statement that **compares** two quantities using < (less than), > (greater than), ≤ (less than *or equal to*), or ≥ (greater than or equal to), saying one is less than, greater than, or at most/at least the other (an *order* relation).
- {#8.1.d2} **Solution set:** *all* the values that make the inequality true, usually infinitely many, drawn as a shaded ray.
- {#8.1.d3} **Strict** (<, >) vs. **inclusive** (≤, ≥): whether the boundary value itself counts.

**Check for understanding (transfer):**
1. {#8.1.c1} Solve −3x ≥ 12, then put x = −5 into the *original* inequality and walk through how the test confirms your answer (or would have caught a slip). (Dividing by −3 flips the sign: x ≤ −4. Test x = −5, which is in "x ≤ −4": the original is −3(−5) = 15, and 15 ≥ 12 is true, so the answer holds. If you'd forgotten the flip and written x ≥ −4, then −5 would be excluded even though it makes the original true. The test would flag it.)
2. {#8.1.c2} Two people solve −x < 4. One writes x < −4, the other x > −4. Use x = 0 to decide who's right and say how you know. (Put x = 0 in the original: −0 = 0, and 0 < 4 is true, so 0 must be in the answer. It fits x > −4 but not x < −4, so x > −4 is correct. The −1 was divided out, which flips the sign.)
3. {#8.1.c3} In words, describe the number-line graph of x ≤ 2: which circle, and which way do you shade? (A filled circle at 2, because ≤ includes the boundary, then shade left toward the smaller numbers.)

A mixed set is harder than a page of one kind of problem, and that difficulty is what makes the skill last. Every problem below has its answer at the end of the lesson, and if one stalls you, flip back to the worked example it's based on. Watch especially for Set B, where a negative coefficient means a flip is coming, and close every problem by testing a point.

**Practice problems** (solve; then describe the number-line graph in words: which circle and which way you shade):

*Set A, no flip*
1. x - 2 < 3
2. x + 5 ≤ 2
3. 3x > 12
4. x/2 ≥ 4
5. 2x + 1 ≤ 9
6. 4x - 3 > 9

*Set B, requires a flip (multiply/divide by a negative)*
7. -x < 4
8. -3x ≤ 9
9. -x + 2 < 5
10. 10 - 2x ≥ 4
11. 3 - x ≤ 7
12. -4x ≤ -8

*Set C, read the graph (manual)*
13. A number line shows an **open** circle at 1 shaded to the **right**. Write the inequality.
14. A number line shows a **filled** circle at -2 shaded to the **left**. Write the inequality.

**Answer key:**
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

Real limits often come in pairs. A thermostat might need to keep a room *between* 60 and 80 degrees, two conditions at once. A ride might admit anyone *older than 12 or with a guardian*, where either condition will do.

Those two little words, *and* and *or*, are what this lesson is about, and they pull in opposite directions. *And* narrows things down to where both conditions hold, while *or* opens things up to where either one does.

Picture two bars you might have to clear. *And* is "you must clear **both** bars": the only numbers that survive are the ones that pass every condition, so you end up with the narrow strip where the conditions overlap. "Temperature between 60 and 80" is an *and*, since a reading has to be above 60 *and* below 80, so only the middle band counts.

*Or* is "clear **either** bar," so a number gets in if it passes even one condition, and you end up with everything either condition allows. "Water under 32 degrees or over 100" is an *or*: freezing *or* boiling, with the whole comfortable middle left out.

On a number line, you shade each condition and then read off the combination. For an *and*, you keep only the part where the two shadings **overlap**, typically a single segment between two endpoints {#8.2.f1}. For an *or*, you keep **everything** that either shading covered, often two separate rays heading opposite ways with a gap between them. The endpoints follow the same open/filled rule from Lesson 8.1: each boundary is open or filled according to its own sign.

In symbols, an *and* often gets written as one chained statement. "x > 2 and x ≤ 5," the numbers between 2 and 5 with 5 included, can be squeezed into 2 < x ≤ 5, read as a single sentence: x is bigger than 2 *and* at most 5.

A chained form like that always means *and*, and it's only well-formed when both signs point the same way. Something like 3 < x > 1 points two ways at once and doesn't say anything coherent, so don't write it. An *or*, by contrast, usually stays as two separate statements joined by the word "or," because its two pieces don't touch.

The solving follows the picture. For a chained *and*, you do the same move to **all three** parts at once, left, middle, and right together, because the whole statement has to stay balanced, not just the middle. For an *or*, you solve the two inequalities **separately** and then put their answers together.

**New terms:**
- {#8.2.d1} **Compound inequality:** two inequalities combined into one statement.
- {#8.2.d2} **And (intersection):** *both* parts must hold. 2 < x ≤ 5 is shorthand for x > 2 **and** x ≤ 5: the values **between** 2 and 5 (with 5 included). On the line, the **overlap** of the two shaded regions, a single segment.
- {#8.2.d3} **Double inequality** (a.k.a. **three-part inequality**): the chained form a < x < b. It is only well-formed when **both symbols point the same way**, and it *always* means an **and** (a < x **and** x < b). Never write something like 3 < x > 1. A chained form with the symbols pointing opposite ways is meaningless.
- {#8.2.d4} **Or (union):** *at least one* part holds. x < -1 **or** x > 3: **everything** in either ray; the two pieces don't touch.

**Worked examples:**

{#8.2.w1}
*Example 1, "and" (three-part).* Solve -1 < x + 2 < 4.
The middle has a +2 you want to clear, so subtract 2. To keep the whole chain balanced, subtract it from all three parts at once: -1 − 2 < x < 4 − 2, which is -3 < x < 2.
Graph: open circles at -3 and 2 (both signs strict), shade the segment between them.
Test a point from inside, x = 0: in the original, 0 + 2 = 2, and -1 < 2 < 4 is true. Solution: **-3 < x < 2**.

{#8.2.w2}
*Example 2, "and" with a division.* Solve 3 ≤ 2x - 1 ≤ 9.
Add 1 to all three parts: 4 ≤ 2x ≤ 10. Now divide all three by 2; it's a positive 2, so no sign flips: 2 ≤ x ≤ 5.
Graph: filled circles at 2 and 5 (both inclusive), shade between. Solution: **2 ≤ x ≤ 5**.

{#8.2.w3}
*Example 3, "or".* Solve x < -1 **or** x > 3.
This one is already solved. It's two separate conditions, so there's nothing to isolate. Graph: an open circle at -1 shading left, and an open circle at 3 shading right, with nothing in the middle. Solution: **x < -1 or x > 3**.

{#8.2.w4}
*Example 4, "or" needing work.* Solve 2x ≤ -4 **or** x - 3 > 2.
Solve each piece on its own. Left: divide 2x ≤ -4 by the positive 2 to get x ≤ -2. Right: add 3 to x − 3 > 2 to get x > 5. Then put them together. Graph: a filled circle at -2 shading left, and an open circle at 5 shading right. Solution: **x ≤ -2 or x > 5**.

The flip rule hasn't gone anywhere. It still applies to a chained inequality, and there it touches *both* signs at once.

{#8.2.w5}
*Example 5, three-part, divide by a negative (flip BOTH signs).* Solve -6 < -2x ≤ 4.
The middle is -2x, so divide all three parts by -2. Dividing by a negative flips each sign: the < and the ≤ both turn around, giving -6/-2 > x ≥ 4/-2, that is 3 > x ≥ -2.
That's correct, but it's awkward to read with the bigger number on the left. Rewrite it left-to-right in increasing order: reading 3 > x ≥ -2 backwards gives **-2 ≤ x < 3**. Notice only the *positions* moved. The strict end stayed strict and the inclusive end stayed inclusive, so the 3 keeps its open mark and the -2 keeps its filled one.
Graph: a filled circle at -2, an open circle at 3, shade the segment between.
Now test, and check the endpoints too, since a flip is exactly where an endpoint can slip. Inside, x = 0: -6 < -2(0) = 0 ≤ 4, true. Endpoint x = -2: -2(-2) = 4, and -6 < 4 ≤ 4 is true, so -2 is in. Endpoint x = 3: -2(3) = -6, and -6 < -6 is false, so 3 is out. That matches the filled -2 and open 3. Solution: **-2 ≤ x < 3**.

Two mix-ups are worth naming now that you've seen the clean cases. The first is shading the whole line for an *and*: if you ever end up shading everything for an *and*, you've combined the pieces like an *or* by mistake, when an *and* keeps only the overlap.

The second shows up when the two conditions don't actually overlap. "x > 5 and x < 1" asks for numbers that are both above 5 and below 1, and there aren't any, so the answer is *no solution*, an empty graph rather than the whole line. (Swap the word to *or* and the same two pieces cover a great deal: everything below 1 together with everything above 5.)

**Check for understanding (transfer):**
1. {#8.2.c1} Rewrite 2 < x ≤ 5 as two separate inequalities joined by a word. Which word, and why is the graph a single segment instead of two rays? (It's x > 2 *and* x ≤ 5. The word is *and*, so only the numbers satisfying both survive, the overlap, which is the single segment from 2 to 5, open at 2 and filled at 5.)
2. {#8.2.c2} Why does x > 5 **and** x < 1 have no solution, while x > 5 **or** x < 1 has lots? Describe both graphs. (No number is above 5 and below 1 at once, so the *and* has no solution and its graph is empty. The *or* needs only one condition, so it covers everything below 1 together with everything above 5: two rays heading opposite ways.)
3. {#8.2.c3} You solve a three-part inequality and divide all parts by -2. What happens to the two inequality signs, and how would testing a point confirm it? (Dividing by a negative flips both signs at once. To confirm, pick a number from your final segment, put it in the original, and check it makes a true statement; testing the endpoints shows which is included and which isn't.)

These problems mix *and* with *or* on purpose, since having to tell them apart each time is what gets the difference to stick. The answers and the matching worked examples are at the end of the lesson if you get stuck. Notice as you go that *and* problems should collapse to one segment and *or* problems should open into two rays. If your picture comes out the other way, that's a cue to re-read the joining word.

**Practice problems** (solve and describe the graph: segment-between for *and*, two rays for *or*):

*Set A, "and"*
1. -2 < x - 1 < 3
2. 0 ≤ x + 1 ≤ 4
3. 3 ≤ 2x - 1 ≤ 9
4. -4 < 2x < 6

*Set B, "or"*
5. x < -1 or x > 5
6. x + 1 < 0 or x - 3 > 2
7. 2x ≤ -4 or x > 3
8. x - 3 ≥ 2 or x < -2

*Set C, three-part, divide by a negative (flip BOTH signs, then rewrite in increasing order)*
9. -9 ≤ -3x < 6

**Answer key:**
1. -1 < x < 4 — add 1 to all parts; open circles at -1 and 4, shade between.
2. -1 ≤ x ≤ 3 — subtract 1 from all parts; filled circles at -1 and 3, shade between.
3. 2 ≤ x ≤ 5 — add 1, divide by 2; filled circles at 2 and 5, shade between.
4. -2 < x < 3 — divide all by 2; open circles at -2 and 3, shade between.
5. x < -1 or x > 5 — two rays (open at -1 left, open at 5 right).
6. x < -1 or x > 5 — left: x<-1; right: x>5; two rays.
7. x ≤ -2 or x > 3 — filled at -2 left, open at 3 right.
8. x ≥ 5 or x < -2 — filled at 5 right, open at -2 left.
9. -2 < x ≤ 3 — divide all three parts by -3 and **flip both** signs (3 ≥ x > -2), then rewrite increasing; open circle at -2, filled circle at 3, shade between. *(Test x = 0: -9 ≤ 0 < 6; endpoint x = 3 is in since -3(3) = -9 ≥ -9; endpoint x = -2 is out since -3(-2) = 6 < 6 is false.)*

---

## Lesson 8.3: Absolute value: graphs & distance

Sometimes what you care about is *how far*, not which direction. A part machined to "within 0.5 millimeters of target" can be a little over or a little under. What matters is the size of the gap, not its sign. That idea, distance with the direction thrown away, is exactly what absolute value measures.

Picture the number line. The **absolute value** of a number, written |x|, is simply how far x sits from 0, and distance is never negative. So |5| = 5, because 5 is five steps from 0. And |−5| = 5 too, because −5 is also five steps from 0, just on the other side. Different inputs, same distance. (This builds on the number line from Unit 1; here it becomes a tool.)

Once you read |x| as distance, its graph almost draws itself. Plot y = |x| at a few inputs: at x = −3 you get 3, at −2 you get 2, at −1 you get 1, at 0 you get 0, then 1, 2, 3 going right. Those points are (-3,3), (-2,2), (-1,1), (0,0), (1,1), (2,2), (3,3), and joined up they make a **V** sitting on the origin {#8.3.f1}.

The right arm climbs at slope +1, the left arm climbs at slope −1, and the whole thing rests on the x-axis, never dipping below it, because an output that *is* a distance can't be negative. Shifts just slide that V around without changing its shape: y = |x| + 2 lifts it up 2, y = |x| − 3 drops it down 3, and y = |x − 1| slides it right 1, so its vertex moves to where the inside equals 0. Those are pictures to read off, not equations to solve.

Now the solving, read straight from the distance picture. There are three shapes, and each one is a plain-language question about distance from 0:

- |x| = k asks "which numbers are exactly k from 0?" Two of them, one each way: **x = k or x = -k**. (This needs k ≥ 0. At k = 0 the two answers collapse to the single x = 0; if k is negative there's no solution, since no distance is negative.)
- |x| < k asks "which numbers are within k of 0?" Everything in the band around 0: **-k < x < k**. That's an *and*, a single segment, and it's a direct payoff of Lesson 8.2. (This needs k > 0.)
- |x| > k asks "which numbers are more than k from 0?" Everything out past k on either side: **x < -k or x > k**. That's an *or*, two rays. (This holds for any k ≥ 0.)

One setup step comes before you read any of those off: get the absolute value by itself first. If it's scaled, as in 2|x| ≤ 8, divide to isolate it (here divide by 2 to get |x| ≤ 4), and *then* read the distance. Keep that isolating step a division by a *positive* number for now.

**New terms:**
- {#8.3.d1} **Absolute value |x|:** the distance of x from 0 on the number line; always ≥ 0. |5| = 5 and |-5| = 5, both are 5 units from 0 (callback to Unit 1.4).
- {#8.3.d2} **The graph y = |x|:** a **V** with its vertex at the origin (the right arm rises at slope +1, the left arm at slope -1), and it never dips below the x-axis, because an output that *is* a distance can't be negative.
- {#8.3.d3} **Simple shifts of the V:** y = |x| + 2 lifts the whole V up 2; y = |x| − 3 drops it 3; y = |x − 1| slides it right 1 (the vertex moves to where the inside equals 0). These are *graph* moves read off the picture, not algebra to solve.

**Worked examples:**

{#8.3.w1}
*Example: inclusive "within".* Solve |x| ≤ 2. This asks for the numbers within 2 of 0, and the ≤ includes the boundary, so -2 ≤ x ≤ 2. Filled circles at -2 and 2, shade the segment between. Solution: **-2 ≤ x ≤ 2**.

{#8.3.w2}
*Example: the graph y = |x|.* Plot (-2,2), (-1,1), (0,0), (1,1), (2,2): a **V** with vertex (0,0), arms at slope ±1, resting on the x-axis. Then y = |x| − 2 is the same V dropped 2, with vertex (0,-2), and y = |x − 1| is it slid right 1, with vertex (1,0). Nothing to solve here, you're just reading the picture.

{#8.3.w3}
*Example: "outside" (or).* Solve |x| > 2. This asks for the numbers more than 2 from 0, which is **x < -2 or x > 2**. Open circles at -2 and 2, shade outward in two rays.

{#8.3.w4}
*Example: isolate first.* Solve 2|x| ≤ 8. Divide both sides by 2 first; it's a positive 2, so nothing flips: |x| ≤ 4. That's the numbers within 4 of 0, so **-4 ≤ x ≤ 4**. Filled circles at -4 and 4, shade between.

{#8.3.w5}
*Example: no solution / all reals.* Distance is never negative, so you can read these straight off the picture without any algebra. |x| = -3 has **no solution**, because nothing sits a negative distance from 0. |x| < -2 has **no solution** for the same reason: no distance is below -2. And |x| > -1 is true for **every** real x, since every distance is more than -1.

That last example points at the trap to watch here. It's tempting to give |x| = k a single answer and stop, but distance runs both ways, so expect two: x = k and x = −k (the lone exception is k = 0).

And a quick self-check on the *and*/*or* split: "within" or "less than" gives one segment between -k and k, while "outside" or "greater than" gives two rays. If you're ever unsure which, don't reach for a memorized rule. Go back to the distance question and re-derive it.

**Check for understanding (transfer):**
1. {#8.3.c1} Sketch y = |x| in words: where's the vertex, what are the arm slopes, and why does it never go below the x-axis? Then describe y = |x| + 1. (Vertex at the origin (0,0); right arm slope +1, left arm slope −1; it stays at or above the axis because an output that is a distance can't be negative. y = |x| + 1 is the same V lifted up 1, vertex at (0,1).)
2. {#8.3.c2} Why does |x| < 4 become an *and* (a single segment) while |x| > 4 becomes an *or* (two rays)? Use the distance picture. ("Within 4 of 0" means closer than 4 on both sides at once: an *and*, the band -4 < x < 4. "More than 4 from 0" means out past 4 on either side: an *or*, the two rays x < -4 or x > 4.)
3. {#8.3.c3} What is the solution of |x| = -3? Of |x| > -3? Explain each from "distance is never negative." (|x| = -3 has no solution: nothing sits a negative distance from 0. |x| > -3 is all real numbers: every distance is greater than -3, so every x qualifies.)

For practice, stay on the core path: everything here is centered at 0, so you can read each one off the distance picture. Give both solutions for the equations, describe the graph for the inequalities, and check your answers by substituting.

**Practice problems (core, the mastery path):** symmetric, centered at 0. *(Problems 2, 3, 5, 6, 7 shift the center off 0, so they've moved to the Reach set below.)*

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

**Answer key:**
1. x = 4 or x = -4. (|4| = 4, |-4| = 4.)
4. x = 4 or x = -4. (|2·4| = 8, |2·(-4)| = 8.)
9. x = 7 or x = -7. (|7| = 7, |-7| = 7.)
8. -3 < x < 3 — |2x| < 6 ⇒ -6 < 2x < 6; open circles at -3 and 3, shade between (*and*).
10. x < -5 or x > 5 — "more than 5 from 0"; open circles at -5 and 5, shade outward (*or*).
11. -5 ≤ x ≤ 5 — isolate: divide by 2 → |x| ≤ 5; filled circles at -5 and 5, shade between.
12. **no solution** — a distance can't be less than -2.
13. **all real numbers** — every distance is more than -1.

---

### Reach beyond Algebra 1 (optional, off the mastery path)

This part is here so you can see where the idea goes next. It isn't part of the Algebra 1 target, so get the distance-from-0 core above solid first and treat the rest as a preview.

When the center moves off 0, as in |x − 3| = 5 or |2x − 1| = 7, you can't just read x = ±k anymore. The move is to split into **two cases** (the inside equals +k, or the inside equals −k), solve each, and name the answer set. Here's that method on one example.

{#8.3.w6}
*w1: |x − 3| = 5.* Two cases: x − 3 = 5 → x = 8, or x − 3 = -5 → x = -2. Solutions: **x = 8 or x = -2**. Check: |8 − 3| = 5, |-2 − 3| = 5. *(Pictured: "distance 5 from 3.")*

*A few more, same idea.*
{#8.3.w7}
*w2: |x − 3| < 5.* Within 5 of 3 → -5 < x − 3 < 5 → -2 < x < 8 (interval (-2, 8)).
{#8.3.w8}
*w3: |x − 3| > 5.* More than 5 from 3 → x − 3 < -5 or x − 3 > 5 → x < -2 or x > 8.
{#8.3.w9}
*w4: |x + 2| = 3.* |x + 2| = |x − (-2)|, distance 3 from -2 → x = 1 or x = -5.

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

In Unit 5, the answer to a two-variable equation like y = 2x + 1 was a line, every point on it. Loosen the = to an inequality and the answer grows: instead of the line, you get a whole *region*, a flat sheet of points filling one side of that line. This is the picture behind questions like "which combinations of two things are allowed," where a budget or a limit carves the plane into the allowed part and the rest.

Think about y > 2x + 1. It's asking, for each point, "is the output bigger than what the line gives?" Put another way, "which points sit *above* the line y = 2x + 1?" The line itself is the dividing fence: above it the inequality is true, below it false. So the answer isn't the fence, it's the whole field on one side of it. That field is called a **half-plane**, and the line is its **boundary** {#8.4.f1}.

Once the boundary is drawn, two decisions turn it into a finished graph:

1. **Dashed or solid?** This is the same open-versus-filled choice from Lesson 8.1 in a new costume. If the inequality is strict (< or >), the boundary itself isn't included, so you draw it **dashed**. If it's inclusive (≤ or ≥), the boundary counts, so you draw it **solid**.
2. **Which side to shade?** Here there's a reliable method that never makes you guess: **test a point** that isn't on the line, drop it into the inequality, and see if it makes a true statement. If it does, shade the side that point is on; if it doesn't, shade the other side.

The easiest test point is almost always the origin, (0,0), because the arithmetic is trivial, unless the line runs through the origin, in which case you pick any other off-line point. And say the test out loud as you do it, because hearing it keeps you honest: "at (0,0), is 0 > 1? No, so shade the other side."

So you graph the boundary, mark it dashed or solid, and let a tested point pick the side. Compute the two boundary points rather than eyeballing them; a small sign slip there throws off the whole line.

For a **system**, meaning two or more inequalities that must all hold at once, you graph each region the same way, then keep only where they **overlap**. The overlap is the set of points that satisfy every inequality together, and you confirm it by testing a point that should be inside all of them.

**New terms:**
- {#8.4.d1} **Linear inequality in two variables:** e.g. y > 2x + 1, satisfied not by a line but by a **half-plane** (every point on one side of the boundary).
- {#8.4.d2} **Boundary line:** the line you get by replacing the inequality with = (here y = 2x + 1, the function f(x) = 2x+1). **Dashed** if strict (<, >), meaning the line itself is *not* included; **solid** if inclusive (≤, ≥).
- {#8.4.d3} **Half-plane / test point:** one of the two sides the boundary cuts the plane into. To choose the correct side, **test a point** not on the line (the **origin (0,0)** is easiest) and shade the side that makes the inequality true.
- {#8.4.d4} **System of inequalities:** two or more inequalities at once; the solution is the **overlap** of their shaded regions.

**Worked examples:**

{#8.4.w1}
*Example 1, strict, dashed.* Graph y > 2x + 1.
Boundary: y = 2x + 1, through (0,1) and (1,3). It's strict (>), so draw it **dashed**: the line itself isn't part of the answer.
Test (0,0): is 0 > 2(0) + 1 = 1? That's 0 > 1, which is **false**, so shade the side *not* containing the origin. Region: everything above the dashed line.

{#8.4.w2}
*Example 2, inclusive, solid.* Graph y ≤ -x + 3.
Boundary: y = -x + 3, through (0,3) and (3,0). It's inclusive (≤), so draw it **solid**: the line is included.
Test (0,0): is 0 ≤ -0 + 3 = 3? That's 0 ≤ 3, which is **true**, so shade the side containing the origin. Region: the line and everything below it.

{#8.4.w3}
*Example 3, fractional slope, dashed.* Graph y < (1/2)x - 2.
Boundary: y = (1/2)x - 2, through (0,-2) and (2,-1). Strict (<), so **dashed**.
Test (0,0): is 0 < (1/2)(0) - 2 = -2? That's 0 < -2, which is **false**, so shade the other side. Region: below the dashed line.

{#8.4.w4}
*Example 4, a system.* Graph the system y ≥ x - 1 **and** y ≤ -x + 3.
Take them one at a time. Boundary 1: y = x - 1, **solid** (inclusive); test (0,0): is 0 ≥ -1? **True**, so shade the side with the origin. Boundary 2: y = -x + 3, **solid**; test (0,0): is 0 ≤ 3? **True**, so shade the side with the origin again.
The solution is the **overlap** of the two shaded regions, a wedge that contains the origin, fenced by both solid lines. Confirm it with a point inside the overlap, say (1,0): 0 ≥ 1 − 1 = 0 is true, and 0 ≤ -1 + 3 = 2 is true, so (1,0) belongs to both.

A couple of things to keep straight, now that you've worked the clean cases. Don't try to guess the side from the direction of the sign: once the line tilts, a > does not always mean "shade up," so let the tested point decide every time.

And if the boundary runs through the origin, the origin sits *on* the fence and can't tell you a side, so pick a different test point, like (1,0). For a system, the answer is the overlap, never the union: shading each region is only the setup, and the solution is just the part they share.

**Check for understanding (transfer):**
1. {#8.4.c1} For y < x + 4: is the boundary dashed or solid, and how do you decide which side to shade? Do the origin test out loud. (Strict <, so dashed. Test (0,0): is 0 < 0 + 4 = 4? Yes, true, so shade the side with the origin, below the line.)
2. {#8.4.c2} Your boundary line passes through (0,0). Why can't you use the origin as your test point, and what would you use instead? (Because (0,0) is on the boundary, it can't tell you which side is the solution. It's on the fence, not on either side. Pick any point not on the line, such as (1,0), and test that.)
3. {#8.4.c3} A system is y > x and y < 4. Describe the solution region: which two boundaries, dashed or solid, and roughly where the overlap sits. (Both boundaries are dashed: the line y = x and the horizontal line y = 4. The overlap is the region above y = x and below y = 4, a wedge opening to the left, where points satisfy both at once.)

For each problem, name the boundary line, say dashed or solid, run the test point out loud, and then state which side to shade. The answers are at the end of the lesson, with a worked example to match each problem.

**Practice problems** (for each: name the boundary line, dashed or solid, the test point with its true/false result, and which side to shade):

*Set A, single inequalities*
1. y > x + 2
2. y ≤ 2x - 1
3. y < -x + 4
4. y ≥ 3x  *(boundary through origin, so choose a different test point)*
5. x + y < 5

*Set B, a system*
6. y > x **and** y < -x + 4  *(describe the overlap region)*

*Set C, boundary arithmetic (eval)*
7. For the boundary y = 2x - 3, compute y at x = 2 (a point to plot).

**Answer key:**
1. Boundary y = x + 2 (e.g. (0,2),(1,3)), **dashed**. Test (0,0): 0 > 2? **false** → shade the side **without** the origin (above the line).
2. Boundary y = 2x - 1 ((0,-1),(1,1)), **solid**. Test (0,0): 0 ≤ -1? **false** → shade the **other** side (below the line).
3. Boundary y = -x + 4 ((0,4),(4,0)), **dashed**. Test (0,0): 0 < 4? **true** → shade the side **with** the origin (below/left).
4. Boundary y = 3x ((0,0),(1,3)), **solid**. Origin is *on* the line — test (1,0): 0 ≥ 3(1)=3? **false** → shade the side **not** containing (1,0): the side holding points like (0,1) and (-1,0) — above/left of the steep line. *(For a steep line, pick the shaded side by testing a point you can see is in or out, not by "left" or "right".)*
5. Boundary x + y = 5 ((0,5),(5,0)), **dashed**. Test (0,0): 0 + 0 = 0 < 5? **true** → shade the side **with** the origin (below/left).
6. Boundary 1 y = x, **dashed**, shade above (test (0,1): 1 > 0). Boundary 2 y = -x + 4, **dashed**, shade below (test (0,0): 0 < 4). **Solution = the overlap**, a wedge between the two dashed lines (e.g. (1,2): 2 > 1 and 2 < 3).
7. y = 2(2) - 3 = 1 → plot (2, 1).

---

You can now solve a one-variable inequality the same way you solve an equation, flipping the sign only when you multiply or divide by a negative, and confirm it by testing a point in the original.

You can graph a solution with the right circle and direction, chain conditions with *and* (the overlap) and *or* (the union), read absolute value as distance from 0 to handle |x| = k, |x| < k, and |x| > k, and graph a two-variable inequality or a system as a shaded region picked out by a test point.

One habit runs through all of it: solve the way you always have, then test a point in the original to confirm the answer.
