# Unit 7: Systems of Equations

A single equation like y = 2x + 1 has a whole line of answers. Every point on that line fits it. This unit is about what happens when you have two equations that both have to be true at once. That second demand usually narrows things down to a single answer, the one pair of numbers that works for both.

Keep one picture in mind the whole way through. Each equation draws a line. A pair of equations is asking a simple question: is there one point that sits on both lines at once? When there is, it's the place the two lines cross. Everything in this unit, whether graphing or substitution or elimination, is just a different way to find that crossing point.

One habit never changes here. Once you have an answer, put it back into both equations and make sure both come out true.

It helps to have your work with single equations fresh. Before each new lesson, redo two or three problems from the lesson before from memory, then check them. Practice spaced out like that feels harder in the moment, and that's exactly what makes a skill last to next week. Every set in this unit has its answers at the end of the lesson, so the help is always right there.

---

## Lesson 7.1: Solving by graphing

Start with what a single equation already gives you. Write y = x + 1, and you don't get one answer. You get a whole line of them: (0, 1), (1, 2), (2, 3), and on forever. Write y = −x + 5, and that's a second line, its own endless list of points. Now ask a fair question: is there a single point that lives on *both* lines at the same time?

That question is what a **system** asks. Two relationships, both true at once. The answer, when there is one, is the point where the two lines cross {#7.1.f1}. It's the one (x, y) that satisfies both equations together.

<!--viz:example_graphs#2-->

The way to *see* it is to graph both lines on one plane and look for where they meet. One caution before you draw, though: don't trust your eye to read a crossing point off the picture. Compute the points instead. Pick a few x-values, run each through both equations, and watch for the row where the two outputs match. That row is the crossing.

Take y = x + 1 and y = −x + 5. Here's a short table for each:

$$\begin{array}{c|c|c}
x & y = x+1 & y = -x+5 \\ \hline
0 & 1 & 5 \\
2 & 3 & 3 \\
4 & 5 & 1
\end{array}$$

Look at the row x = 2: both equations give y = 3. So both lines pass through (2, 3), and that shared point is the solution. The graph would show the two lines crossing right there. You didn't need to eyeball it, though, because the table told you exactly.

**New terms:**
- {#7.1.d1} **System of equations:** two (or more) equations considered together, asking for values that satisfy all of them at once.
- {#7.1.d2} **Solution of a system:** an ordered pair (x, y) that makes **every** equation in the system true. A system may have **one** such pair, **none**, or **infinitely many** (see 7.4). So don't assume there's exactly one until you've solved it.

Notice that a solution here is an *ordered pair*, not a single number. This is the one thing to hold onto for the whole unit: you're not done when you know x, you're done when you have both x and y. Finding x = 2 and walking away is finishing half the problem.

**Worked examples:**

Read each of these slowly, line by line, and ask why each step follows from the one before.

{#7.1.w1}
*Example 1, the canonical one.* Solve y = x + 1 and y = −x + 5 by graphing.
From the table above, both lines pass through (2, 3), so that's the only point on both. Now confirm it by putting (2, 3) into **both** equations, not just one, because the answer has to satisfy both at once. First equation: is 3 = 2 + 1? Yes. Second equation: is 3 = −2 + 5? Yes. Both are true, so the solution is (2, 3).

If a check like that ever *doesn't* come out true, you haven't failed. Your check just did its job and caught something before it counted. That's the whole reason we check. Go back to your first step and re-run the arithmetic slowly. A mismatch is almost always one sign or one small slip, not the whole method falling apart.

{#7.1.w2}
*Example 2, a horizontal line.* Solve y = 2x and y = 6.
The equation y = 6 is a flat line sitting at height 6. Every point on it has y = 6, no matter the x. The line y = 2x climbs steadily, and you want to know when it reaches that same height of 6. It does when 2x = 6, that is, when x = 3. So the crossing is (3, 6). Check both: is 6 = 2(3)? Yes, since 2(3) = 6. And is 6 = 6? Yes. Solution: (3, 6).

{#7.1.w3}
*Example 3.* Solve y = x + 2 and y = −x + 4.
Build a small table and look for the matching row. At x = 1, the first equation gives 1 + 2 = 3, and the second gives −1 + 4 = 3. They agree, so the lines cross at (1, 3). Check both: 3 = 1 + 2, and 3 = −1 + 4. Both true. Solution: (1, 3).

{#7.1.w4}
*Example 4, the limitation, on purpose.* Solve y = 2x and y = x + 1 but suppose the answer weren't clean. Here it is clean: they meet at (1, 2), since 2 = 2(1) and 2 = 1 + 1, both true. But picture a different system whose lines crossed at, say, (2.5, −1.3). Could you read those numbers off a graph you drew by hand? You couldn't. The best you'd manage is "somewhere near there." That's the honest limit of graphing, and it's exactly why the next two lessons give you methods that produce the exact answer without any squinting.

That's the trade graphing makes. It shows the meaning of a system clearly, because you can *see* the solution as a crossing point, but it only reliably reads off whole-number crossings. When the intersection looks like it falls between the gridlines, that's not your cue to guess a decimal. It's your cue to reach for substitution or elimination, the methods in the next two lessons.

**Check for understanding (transfer):**

Each of these has a short answer below it, so you can check your thinking.

1. {#7.1.c1} "Without graphing yet, what does it *mean*, in words, that (2, 3) is the solution of a system? What two things must be true?" (It means the point (2, 3) lies on both lines at once. So putting x = 2, y = 3 into the first equation makes it true, *and* putting the same pair into the second equation makes it true. Both, not one.)
2. {#7.1.c2} "Two lines on the same plane never touch. What does that tell you about how many solutions the system has?" (None. If the lines never meet, there's no point that's on both, so no (x, y) satisfies both equations. You'll meet this case head-on in 7.4.)
3. {#7.1.c3} "If a system's solution were (1.5, 4.2), why would graphing by hand let you down, and what would you reach for instead?" (You can't read 1.5 and 4.2 off a hand-drawn grid with any confidence. The point falls between the lines you can draw. You'd switch to an algebraic method, substitution or elimination, to get the exact values.)

**Practice problems** (solve by graphing / finding where the two lines meet; give the ordered pair and check both):

*Set A: one line is horizontal or through the origin*
1. y = x and y = 4
2. y = 2x and y = 6
3. y = -x + 6 and y = x

*Set B: two slanted lines*
4. y = x + 2 and y = -x + 4
5. y = x - 1 and y = -x + 3
6. y = 2x - 1 and y = x + 1

**Answer key:**
1. (4, 4) — 4 = 4, 4 = 4
2. (3, 6) — 6 = 2(3), 6 = 6
3. (3, 3) — 3 = -3 + 6, 3 = 3
4. (1, 3) — 3 = 1 + 2, 3 = -1 + 4
5. (2, 1) — 1 = 2 - 1, 1 = -2 + 3
6. (2, 3) — 3 = 2(2) - 1, 3 = 2 + 1

---

## Lesson 7.2: Substitution

Graphing showed you what a solution *is*. Now you'll find it exactly, with no graph to read. The trick rests on one fact you already trust: in a system, x means the same number in both equations, and so does y. The two equations aren't strangers. They describe the same pair of hidden numbers.

Think of y as a mystery box with one number hidden inside. Suppose the first equation tells you outright what's in the box: y = 2x. That's not a different y from the one in the second equation. It's the *same* box, and you've just been told what it holds. So anywhere the second equation says y, you can pour in 2x instead, because they're equal. That swap is **substitution**.

<!--illus:7-2-substitution-->

The payoff is what makes the swap worth doing. The second equation has two unknowns, x and y, and you can't solve one equation in two unknowns. But the moment you replace y with 2x, that equation has only x in it. One equation, one unknown, the kind you've been solving since Unit 2. The crossing point falls out as soon as a single variable is left standing.

The full move, start to finish: isolate a variable in one equation, substitute that expression into the *other* equation, solve the one-variable equation you're left with, back-substitute to find the partner coordinate, and check both. That last "find the partner" step is the one people skip most, so watch for it.

**New terms:**
- {#7.2.d1} **Substitution:** replacing a variable with an expression equal to it. Because each variable denotes the *same* number in both equations, an expression equal to (say) y in one equation may stand in for y in the other.

**Worked examples:**

{#7.2.w1}
*Example 1.* Solve y = 2x and x + y = 9.
Here y is already alone. The first equation tells you the box holds 2x. So in the second equation, wherever you see y, pour in 2x:
$$x + 2x = 9 \;\Rightarrow\; 3x = 9 \;\Rightarrow\; x = 3.$$
Why this works: x plus 2x is three x's, so 3x = 9, and dividing both sides by 3 gives x = 3. But you're not done. You have x, not the pair. Go back and find y: since y = 2x, y = 2(3) = 6. So the solution is (3, 6). Check both: is 6 = 2(3)? Yes. Is 3 + 6 = 9? Yes. Solution: (3, 6).

{#7.2.w2}
*Example 2, isolate first.* Solve x = y + 1 and 2x + y = 8.
This time x is the one already alone: x = y + 1. Substitute y + 1 in place of x in the second equation:
$$2(y + 1) + y = 8 \;\Rightarrow\; 2y + 2 + y = 8 \;\Rightarrow\; 3y + 2 = 8 \;\Rightarrow\; 3y = 6 \;\Rightarrow\; y = 2.$$
Step by step: the 2 outside the parentheses has to reach *everything* inside, so 2(y + 1) becomes 2y + 2. That's the distributing move from Unit 6, handing a copy to each term. Then 2y + y is 3y, so 3y + 2 = 8; subtract 2 from both sides to get 3y = 6; divide by 3 to get y = 2. Now find the partner: x = y + 1 = 2 + 1 = 3. Solution (3, 2). Check both: is 3 = 2 + 1? Yes. Is 2(3) + 2 = 8? Yes, since 6 + 2 = 8. Solution: (3, 2).

That distributing step is the one to slow down on. It's tempting to write 2(y + 1) as 2y + 1, sending the 2 to only the first thing inside. But the 2 has to greet everyone in the parentheses, so it's 2y + 2. A quick way to catch it: count the terms inside, and make sure the outside number reached every one.

{#7.2.w3}
*Example 3, watch the distribution.* Solve y = x − 2 and x + y = 10.
y is alone, so substitute x − 2 for y in the second equation:
$$x + (x - 2) = 10 \;\Rightarrow\; 2x - 2 = 10 \;\Rightarrow\; 2x = 12 \;\Rightarrow\; x = 6.$$
The x plus another x makes 2x, and the −2 comes along, so 2x − 2 = 10; add 2 to both sides for 2x = 12, then divide by 2 to get x = 6. Partner: y = x − 2 = 6 − 2 = 4. Solution (6, 4). Check both: is 4 = 6 − 2? Yes. Is 6 + 4 = 10? Yes. Solution: (6, 4).

{#7.2.w4}
*Example 4, isolate when nothing is alone yet.* Solve x + y = 7 and 2x + y = 11 by substitution.
Neither variable is alone here, so make one alone first. The first equation is the easy one to rearrange: subtract x from both sides to get y = 7 − x. Now substitute 7 − x for y in the second equation:
$$2x + (7 - x) = 11 \;\Rightarrow\; x + 7 = 11 \;\Rightarrow\; x = 4.$$
Here 2x − x is just x, so x + 7 = 11, and subtracting 7 gives x = 4. Partner: y = 7 − x = 7 − 4 = 3. Solution (4, 3). Check both: is 4 + 3 = 7? Yes. Is 2(4) + 3 = 11? Yes, since 8 + 3 = 11. Solution: (4, 3). (This same system has a matching pair of y-terms, which makes it a natural fit for the elimination method coming in 7.3. You'll solve it that way too.)

Which equation you substitute into matters too. You isolated y from the *first* equation, so you pour the result into the *second* one. If you pour it back into the first, the one you just got it from, everything collapses to something like 0 = 0, which is true but tells you nothing, because you've only said "the first equation equals itself." Always substitute into the other equation.

Here's a clean one to get the method moving before the practice mixes things up. Solve y = 5 and x + y = 8. The first equation hands you y outright, so substitute 5 for y in the second: x + 5 = 8, which gives x = 3. Partner's already known, y = 5. Solution (3, 5). Check both: 5 = 5, and 3 + 5 = 8. When one equation just states a value like that, substitution is almost no work at all.

**Check for understanding (transfer):**

1. {#7.2.c1} "In y = 2x and x + y = 9, why is it safe to write x + 2x = 9? What justifies swapping y for 2x?" (Because the first equation says y *equals* 2x, so they're the same number, and y is the same number in both equations. Swapping equal things for equal things keeps the second equation true.)
2. {#7.2.c2} "You isolated y in equation one. Into *which* equation do you substitute, and why not the other?" (Into equation two, the one you didn't isolate from. Substituting back into equation one just restates it as something like 0 = 0, true but empty, so it finds nothing.)
3. {#7.2.c3} "Make up a system where substitution is clearly the easier method than elimination, and say why." (Any system with a variable already alone, like y = 3x − 2 and x + y = 10, lets you pour 3x − 2 straight in with no rearranging. When a variable is sitting by itself, substitution is the short path.)

**Practice problems** (solve by substitution; give (x, y) and verify both):
1. y = 3x and x + y = 8
2. y = x + 4 and 2x + y = 10
3. x = 2y and x + y = 9
4. y = x - 1 and 3x + y = 11
5. x = y + 3 and x + 2y = 9
6. y = 2x + 1 and x + y = 7
7. y = 4x and 2x + y = 18
8. x = 3y and 2x - y = 10

**Answer key:**
1. (2, 6) — 6 = 3(2), 2 + 6 = 8
2. (2, 6) — 6 = 2 + 4, 2(2) + 6 = 10
3. (6, 3) — 6 = 2(3), 6 + 3 = 9
4. (3, 2) — 2 = 3 - 1, 3(3) + 2 = 11
5. (5, 2) — 5 = 2 + 3, 5 + 2(2) = 9
6. (2, 5) — 5 = 2(2) + 1, 2 + 5 = 7
7. (3, 12) — 12 = 4(3), 2(3) + 12 = 18
8. (6, 2) — 6 = 3(2), 2(6) - 2 = 10

---

## Lesson 7.3: Elimination

Substitution shines when a variable is already alone. But plenty of systems come written like this, 3x + 2y = 16 and x + y = 6, with nothing isolated and no clean way to isolate it without dragging in fractions. For those, there's a method built to handle them head-on, and it's the workhorse you'll lean on most in later math.

The idea starts from the balance scale. Each equation is a level scale: the left side weighs exactly what the right side weighs. So if you have two true equations and you add their left sides together and their right sides together, the result is still balanced and still true. That's the move. You stack two equations and combine them, and if you've lined things up right, one variable disappears in the adding.

<!--illus:7-3-add-equations-->

Picture x + y = 10 and x − y = 4. Stack them and add straight down. On the left, x + x is 2x, and then there's a +y and a −y. Those are a debt and an equal amount of cash sitting together: they go to zero and leave nothing behind. On the right, 10 + 4 is 14. So adding the two equations gives 2x = 14, one equation in one unknown. The y didn't get "cancelled" by some trick. The +y and the −y summed to zero because they were exact opposites.

That's the whole engine: combine the two equations so one variable's terms go to zero, solve what's left, then back-substitute for the partner and check both. The phrase to keep is "go to zero." It's literally what happens when +y and −y add.

When the matching terms have *opposite* signs, like +y and −y, you **add** to make them go to zero. When they have the *same* sign, like 2x in one equation and 2x in the other, you **subtract** one equation from the other so they go to zero. Add for opposites, subtract for matches.

And what if nothing lines up at all, with no pair of matching or opposite coefficients? Then you **scale** first: multiply an entire equation, both sides and every term, by a number that makes one pair line up. Multiplying a whole equation by a positive number is just resizing both pans of the scale by the same amount, so it stays level and the line it describes doesn't change. Once a pair matches or opposes, you're back to the add-or-subtract move.

**New terms:**
- {#7.3.d1} **Elimination (linear combination):** combining two equations so that one variable's terms sum to zero ("go to zero"), removing it.
- {#7.3.d2} **Scaling an equation:** multiplying an *entire* equation by a number. Because both sides are multiplied equally, the line, and the solution, is unchanged (the balance scale stays level when you resize both pans by the same amount).

**Worked examples:**

{#7.3.w1}
*Example 1, add to send a variable to zero.* Solve x + y = 10 and x − y = 4.
The y-terms are +y and −y, opposites, so **add** the two equations to send them to zero:
$$(x + y) + (x - y) = 10 + 4 \;\Rightarrow\; 2x = 14 \;\Rightarrow\; x = 7.$$
Adding down the left: x + x is 2x, and +y plus −y is zero, so 2x is all that's left; on the right, 10 + 4 is 14. Divide by 2 to get x = 7. Now the partner: put x = 7 back into x + y = 10, giving 7 + y = 10, so y = 3. Solution (7, 3). Check both: is 7 + 3 = 10? Yes. Is 7 − 3 = 4? Yes. Solution: (7, 3).

{#7.3.w2}
*Example 2, subtract to send a variable to zero.* Solve 2x + 3y = 12 and 2x − y = 4.
Here the x-terms match: 2x in each, same sign. So **subtract** the second equation from the first to send the 2x to zero:
$$(2x + 3y) - (2x - y) = 12 - 4 \;\Rightarrow\; 4y = 8 \;\Rightarrow\; y = 2.$$
Watch the subtraction carefully, because it's the place a sign goes missing. Subtracting the whole second equation flips the sign of *every* term in it: the 2x becomes −2x (so 2x − 2x is zero), and the −y becomes +y (so 3y + y is 4y). On the right, 12 − 4 is 8. So 4y = 8, and y = 2. Partner: put y = 2 into 2x − y = 4, giving 2x − 2 = 4, so 2x = 6 and x = 3. Solution (3, 2). Check both: is 2(3) + 3(2) = 12? Yes, since 6 + 6 = 12. Is 2(3) − 2 = 4? Yes. Solution: (3, 2).

That sign-flip on subtraction is the classic slip in this lesson. When you subtract the second equation, the −y inside it becomes +y, not −y. Every sign turns over. If you forget and leave it, you'd get 3y − y = 2y instead of 4y, and the answer comes out wrong. A good guard is the check at the end: if your pair doesn't satisfy both equations, a flipped sign in the subtraction is the first place to look.

{#7.3.w3}
*Example 3, subtract, coefficients already matched the other variable.* Solve x + y = 7 and 2x + y = 11.
The y-terms match (a +y in each), so **subtract** to send them to zero. Take the first from the second: (2x + y) − (x + y) = 11 − 7, which gives x = 4 (the y's go to zero, 2x − x is x, and 11 − 7 is 4). Partner: 4 + y = 7, so y = 3. Solution (4, 3). Check both: is 4 + 3 = 7? Yes. Is 2(4) + 3 = 11? Yes. Solution: (4, 3). (This is the same system you solved by substitution in 7.2. Same answer, a different road to it. When two methods both fit, the choice is yours; pick whichever looks cleaner for the system in front of you.)

{#7.3.w4}
*Example 4, scaling required.* Solve 3x + 2y = 16 and x + y = 6.
Nothing matches yet: 3x and x don't agree, and 2y and y don't agree. So **scale** first. Multiply the *entire* second equation by 2, both sides and every term, to make the y-coefficients match: 2(x + y) = 2(6) becomes 2x + 2y = 12. Now the y-terms are both +2y, so subtract this from the first equation:
$$(3x + 2y) - (2x + 2y) = 16 - 12 \;\Rightarrow\; x = 4.$$
The +2y terms go to zero, 3x − 2x is x, and 16 − 12 is 4, so x = 4. Partner: put x = 4 into x + y = 6, giving y = 2. Solution (4, 2). Check both: is 3(4) + 2(2) = 16? Yes, since 12 + 4 = 16. Is 4 + 2 = 6? Yes. Solution: (4, 2).

When you scale, multiply *every* term and *both* sides. Doubling only the left side, or only the x-term, tips the scale and changes the equation. The way to keep it honest is to hand the multiplier to each piece, the same as distributing.

{#7.3.w5}
*Example 5, add, opposite y-coefficients.* Solve 3x + 2y = 12 and 5x − 2y = 4.
The y-terms are +2y and −2y, opposites already, no scaling needed. So **add**:
$$(3x + 2y) + (5x - 2y) = 12 + 4 \;\Rightarrow\; 8x = 16 \;\Rightarrow\; x = 2.$$
Down the left: 3x + 5x is 8x, and +2y plus −2y goes to zero; on the right, 12 + 4 is 16. So 8x = 16 and x = 2. Partner: put x = 2 into 3x + 2y = 12, giving 6 + 2y = 12, so 2y = 6 and y = 3. Solution (2, 3). Check both: is 3(2) + 2(3) = 12? Yes, since 6 + 6 = 12. Is 5(2) − 2(3) = 4? Yes, since 10 − 6 = 4. Solution: (2, 3).

**Check for understanding (transfer):**

1. {#7.3.c1} "In 2x + 3y = 12 and 2x - y = 4, why subtract rather than add? What tells you which to do?" (The x-terms are both +2x, same sign, a match, so subtracting sends them to zero. If they'd been opposites, like +2x and −2x, you'd add instead. Same sign, subtract; opposite signs, add.)
2. {#7.3.c2} "Why is it legal to multiply x + y = 6 by 2? What stays true after you do?" (Because multiplying both sides equally keeps the scale balanced: 2(x + y) really does equal 2(6). The equation still describes the same line and the same solution; you've only rewritten it in a more useful size.)
3. {#7.3.c3} "Given 4x + 3y = 10 and 2x + y = 4, which equation would you scale and by what, to eliminate x? (Don't solve, just plan the move.)" (Scale the second equation by 2: 2(2x + y) = 2(4) gives 4x + 2y = 8. Now both equations have +4x, so subtracting sends x to zero.)

**Practice problems** (solve by elimination; scale first where needed; give (x, y) and verify both):

*Set A: add or subtract directly*
1. x + y = 8 and x - y = 2
2. x + y = 12 and x - y = 6
3. 2x + y = 9 and x - y = 3
4. 3x + y = 14 and x + y = 6
5. 2x + 3y = 13 and 2x + y = 7
6. x + 2y = 11 and x + y = 7

*Set B: scale first*
7. 3x + 2y = 16 and x + 4y = 22
8. 2x + y = 11 and 3x + 2y = 18

**Answer key:**
1. (5, 3) — 5 + 3 = 8, 5 - 3 = 2
2. (9, 3) — 9 + 3 = 12, 9 - 3 = 6
3. (4, 1) — 2(4) + 1 = 9, 4 - 1 = 3
4. (4, 2) — 3(4) + 2 = 14, 4 + 2 = 6
5. (2, 3) — 2(2) + 3(3) = 13, 2(2) + 3 = 7
6. (3, 4) — 3 + 2(4) = 11, 3 + 4 = 7
7. (2, 5) — multiply eq.1 by 2 → 6x+4y=32, subtract eq.2 → 5x=10, x=2, y=5. 3(2)+2(5)=16, 2+4(5)=22
8. (4, 3) — multiply eq.1 by 2 → 4x+2y=22, subtract eq.2 → x=4, y=3. 2(4)+3=11, 3(4)+2(3)=18

---

## Lesson 7.4: Special cases & applications

Two lines usually cross at one point, but not always. Lay any two lines on a plane and exactly one of three things happens: they cross once, they run parallel and never meet, or they sit right on top of each other. This lesson handles the two unusual cases, and then puts the whole toolkit to work on word problems, which are the real reason systems are worth learning.

The three outcomes are easiest to hold as one picture, tied to the slopes you know from Unit 5. Different slopes, and the lines tilt differently, so they have to cross somewhere: that's one solution. Same slope but different intercepts, and they march along parallel forever, never touching: that's no solution. Same slope *and* same intercept, and they're secretly the same line drawn twice, so every point on it works: that's infinitely many solutions.

<!--illus:7-4-parallel-identical-->

| The two lines… | How many solutions | What the algebra leaves |
|---|---|---|
| **cross once** (different slopes) | **one** solution, the (x, y) where they meet | a normal value, e.g. x = 4 |
| **are parallel** (same slope, different intercept) | **no solution**, they never meet | a **false** statement, e.g. 0 = 5 |
| **are the same line** (identical after simplifying) | **infinitely many**, every point on the line works | an always-**true** statement, e.g. 0 = 0 |

These two cases work differently from a normal system, and it catches people off guard the first time. When you solve a normal system, the variables stay around long enough to give you a value. But in these two special cases, the variables all vanish partway through, and what's left over is the signal that tells you which case you're in.

If the leftover statement is **false**, like 0 = 5, no numbers can ever make it true, so there's **no solution**: that's the parallel case. If the leftover is always **true**, like 0 = 0, then every point already works, so there are **infinitely many**: that's the same-line case. So when the x's and y's disappear, don't panic; read the statement they leave behind.

**New terms / the three outcomes:** every pair of lines does exactly one of three things, summarized in the table above.

- **No solution:** the parallel-lines case. Whatever method you use, the variables vanish and you're left with something **false** (like 0 = 5). Nothing can make it true, so nothing solves the system.
- **Infinitely many solutions:** the same-line case (one equation is just a multiple of the other). The variables vanish and you're left with something always **true** (like 0 = 0). Every point on the shared line works.

For the word problems in the second half, the move is the one from Unit 6, now done twice: name your two unknowns, turn the two facts in the story into two equations, solve by whichever method fits, and check your answer against the *story*, not just the algebra. A useful habit when you write the two equations is to keep them on different units: one equation counting *how many* of something, the other counting *dollars* or *amount*. That keeps you from accidentally writing the same fact twice.

**Worked examples:**

{#7.4.w1}
*Example 1, no solution (parallel).* Solve y = 2x + 1 and y = 2x − 3.
Both have y alone, so substitute the first into the second: 2x + 1 = 2x − 3. Now subtract 2x from both sides, and the x's vanish: 1 = −3. That's **false**. No number anywhere makes 1 equal −3. So there's **no solution.** And it lines up with the picture: both lines have slope 2 but different intercepts, so they're parallel and never meet.

{#7.4.w2}
*Example 2, no solution in standard form.* Solve 2x − y = 3 and 4x − 2y = 1.
Scale the first equation by 2 to match the second's x-term: 2(2x − y) = 2(3) gives 4x − 2y = 6. Now subtract the second equation from it: (4x − 2y) − (4x − 2y) = 6 − 1. The whole left side goes to zero, leaving 0 = 5, which is **false**. So **no solution.** (The two lines are parallel; the scaling just made it visible.)

{#7.4.w3}
*Example 3, infinitely many (same line).* Solve x + y = 4 and 2x + 2y = 8.
Look closely: the second equation is just the first one times 2. To confirm with the algebra, scale the first by 2 to get 2x + 2y = 8, then subtract the second: 0 = 0, always **true**. The two equations are the very same line, so there are **infinitely many solutions**. Every point on x + y = 4 works, such as (0, 4), (1, 3), and (4, 0). "Infinitely many" isn't a vague shrug, though; it's a precise set: it's *all* the pairs (x, y) with x + y = 4. Describing it in those plain words is enough.

A warning right where these two cases get mixed up: it's easy to call 0 = 0 "no solution" and 0 = 5 "infinitely many," because both feel like dead ends. They're backwards. A **true** leftover means *everything* works, so infinitely many; a **false** leftover means *nothing* works, so none. Anchor it on the meaning: true says yes to every point, false says yes to no point.

{#7.4.w4}
*Example 4, an application with tickets.* A theater sells adult tickets at $8 and child tickets at $5. One night it sold **200 tickets** for **$1300** total. How many of each?
Start by naming the unknowns and turning each fact into an equation. Let a = adult tickets and c = child tickets. One fact counts tickets, the other counts dollars:
$$a + c = 200 \qquad 8a + 5c = 1300.$$
Substitution is clean here. From the first equation, c = 200 − a. Pour that into the second: 8a + 5(200 − a) = 1300. Distribute the 5 to both terms inside: 8a + 1000 − 5a = 1300. Combine the a's: 3a + 1000 = 1300, so 3a = 300 and a = 100. Partner: c = 200 − 100 = 100. Now check against the story: 100 + 100 = 200 tickets, and 8(100) + 5(100) = 800 + 500 = 1300 dollars. Both fit, so it's **100 adult, 100 child.**

{#7.4.w5}
*Example 5, an application with coins, less symmetric.* A jar has **15 coins**, all quarters and dimes, worth **$2.70** (270 cents). How many of each?
Let q = quarters and d = dimes. One equation counts coins, the other counts cents (a quarter is 25 cents, a dime is 10):
$$q + d = 15 \qquad 25q + 10d = 270.$$
Elimination fits well. Scale the first equation by 10 so the d-terms match: 10q + 10d = 150. Subtract that from the second: (25q + 10d) − (10q + 10d) = 270 − 150, so the d's go to zero and 15q = 120, giving q = 8. Partner: d = 15 − 8 = 7. Check the story: 8 + 7 = 15 coins, and 25(8) + 10(7) = 200 + 70 = 270 cents. Both fit, so it's **8 quarters, 7 dimes.**

{#7.4.w6}
*Example 6, an application with a mixture.* How many liters of a **20%** salt solution and a **50%** salt solution should you mix to make **30 liters** of a **30%** solution?
Let x = liters of the 20% solution and y = liters of the 50% solution. One equation counts liters of liquid, the other counts liters of actual salt. The target, 30 L at 30%, holds 0.30 · 30 = 9 L of salt:
$$x + y = 30 \qquad 0.20x + 0.50y = 9.$$
Decimals are easier to handle cleared, so multiply the salt equation by 10: 2x + 5y = 90. Then scale the liter equation by 2: 2x + 2y = 60. Subtract: (2x + 5y) − (2x + 2y) = 90 − 60, the x's go to zero, and 3y = 30, so y = 10. Partner: x = 30 − 10 = 20. Check the story: 20 + 10 = 30 liters, and the salt is 0.20(20) + 0.50(10) = 4 + 5 = 9 L, which is 30% of 30. Both fit: **20 L of the 20% solution, 10 L of the 50%.** (This is built like a coin problem: one equation counts the amount of liquid, one counts the active ingredient.)

{#7.4.w7}
*Example 7, an application with perimeter.* A rectangle's **length is 4 more than its width**, and its **perimeter is 28**. Find the length and width as a system.
Let l = length and w = width. The two facts become two equations. Perimeter is the distance all the way around, which for a rectangle is twice the length plus twice the width:
$$l = w + 4 \qquad 2l + 2w = 28.$$
Length is already alone, so substitute l = w + 4 into the perimeter equation: 2(w + 4) + 2w = 28. Distribute the 2: 2w + 8 + 2w = 28. Combine: 4w + 8 = 28, so 4w = 20 and w = 5. Partner: l = 5 + 4 = 9. Check the story: length 9 is 4 more than width 5, and the perimeter is 2(9) + 2(5) = 18 + 10 = 28. Both fit: **width 5, length 9.**

One last thing about word-problem answers: check them against the *story*, not only the math. If a system hands you a negative number of tickets or half a coin, the algebra may be flawless but the setup slipped somewhere. That strange answer is a signal to look back at how you wrote the two equations.

**Check for understanding (transfer):**

1. {#7.4.c1} "You solve a system and reach 7 = 7. How many solutions, and what do the graphs look like?" (Infinitely many. A leftover that's always true means every point already works, so the two equations are the same line, one drawn right on top of the other.)
2. {#7.4.c2} "Two lines have the same slope. What two situations are still possible, and how does the algebra tell them apart?" (Either they're parallel with different intercepts, meaning no solution, and the algebra leaves a false statement like 0 = 5. Or they're the same line, meaning infinitely many, and the algebra leaves a true statement like 0 = 0. The leftover statement tells you which.)
3. {#7.4.c3} "A problem says '30 nickels and dimes worth $2.40.' Name your two variables and write the two equations, but don't solve yet." (Let n = nickels and d = dimes. One equation counts coins, one counts cents: n + d = 30 and 5n + 10d = 240.)

**Practice problems:**

*Set A: classify (one solution / none / infinitely many); if one, give it*
1. y = 3x + 2 and y = 3x - 5
2. x + y = 5 and 3x + 3y = 15
3. y = x + 1 and y = -x + 7

*Set B: applications (set up two equations, solve, check the story)*
4. Two numbers add to 30, and one is 6 more than the other. Find the numbers.
5. A snack stand: 2 burgers and 1 fries cost $11; 1 burger and 2 fries cost $10. Find the price of a burger and of fries.
6. A boat goes **20 mph downstream** (with the current) and **4 mph upstream** (against it). Find the boat's speed in still water and the speed of the current. (Hint: with the current the speeds add, against it they subtract.)
7. *(mixture)* How many milliliters of a **10%** acid solution and a **40%** acid solution make **40 mL** of a **25%** solution?
8. *(perimeter)* A rectangle's length is **2 more than its width** and its perimeter is **24**. Find the width and length.

**Answer key:**
1. **No solution** — same slope 3, different intercepts (parallel); substituting gives 2 = -5, false.
2. **Infinitely many** — eq.2 is eq.1 times 3 (same line); reduces to 0 = 0.
3. **One solution, (3, 4)** — 4 = 3 + 1, 4 = -3 + 7.
4. x + y = 30, x = y + 6 → (y + 6) + y = 30 ⇒ y = 12, x = 18. The numbers are **18 and 12** (18 + 12 = 30, 18 = 12 + 6).
5. 2b + f = 11, b + 2f = 10 → eliminate: scale eq.2 by 2 → 2b + 4f = 20, subtract eq.1 → 3f = 9, f = 3, then b = 4. **Burger $4, fries $3** (2(4)+3 = 11, 4 + 2(3) = 10).
6. Let b = boat speed in still water, c = current. Downstream the speeds add, upstream they subtract: b + c = 20, b − c = 4 → add → 2b = 24, b = 12, then c = 8. **Boat 12 mph, current 8 mph** (12 + 8 = 20, 12 − 8 = 4).
7. Let x = mL of 10%, y = mL of 40%; one equation counts mL, one counts acid (25% of 40 = 10 mL): x + y = 40, 0.10x + 0.40y = 10. Clear decimals (×10): x + 4y = 100; subtract x + y = 40 → 3y = 60 ⇒ y = 20, then x = 20. **20 mL of each** (20 + 20 = 40; 0.10(20) + 0.40(20) = 2 + 8 = 10 mL acid).
8. Let l = length, w = width: l = w + 2, 2l + 2w = 24. Substitute → 2(w + 2) + 2w = 24 ⇒ 4w + 4 = 24 ⇒ w = 5, then l = 7. **Width 5, length 7** (perimeter 2(7) + 2(5) = 24, and 7 = 5 + 2).

---

You can now solve a system three ways and tell which fits.

Graphing shows you what a solution means, the one point on both lines, but only reads clean whole-number crossings. Substitution is the short path when a variable is already alone: pour its expression into the other equation and you're down to one unknown. Elimination is the workhorse for equations in standard form: scale if you need to, then add for opposite coefficients or subtract for matching ones, so a variable goes to zero.

When the variables all vanish, read what's left: a false statement means no solution (parallel lines), a true one means infinitely many (the same line). And whichever road you take, the answer is an ordered pair, confirmed by putting it back into both equations.
