# Unit 7: Systems of Equations

> **Prerequisites:** Unit 5 (coordinate plane, graphing lines, slope, slope-intercept form) and Unit 6 (translating words into equations). Comfort with solving one- and two-step equations (Unit 2) is assumed throughout.
> **By the end, the student can:**
> - Explain that a *system* is two relationships holding at once, and that its solution is the single (x, y) that makes **both** equations true — graphically, the point where the two lines cross.
> - Solve a system by **graphing**, by **substitution**, and by **elimination**, and choose a sensible method for a given system.
> - Recognize the two special cases — **no solution** (parallel lines) and **infinitely many** (the same line) — from both the algebra and the graph.
> - Set up and solve **two-variable word problems** (tickets, coins, mixtures, perimeter) as a system.
> - **Verify** every solution by substituting it back into *both* equations.

## Teaching this unit (orientation for the tutor)

The whole unit rests on one reframing: up to now an equation like y = 2x + 1 had a *whole line* of solutions. A **system** pins it down by demanding a second condition at the same time. The solution is the one (x, y) that satisfies **both** — the meeting point of two lines, two functions agreeing. Keep returning to that picture: *"each equation is a line/function; the solution is where they cross."* This is also where Unit 5's "a line *is* a function, f(x) = 2x+1" pays off — a system is asking "for what input do these two functions give the same output?"

The arc is concrete → symbolic three times over. **7.1 graphing** builds the meaning (you can *see* the crossing) but exposes its weakness: you can't read (2.5, -1.3) off a hand graph. That motivates **7.2 substitution** and **7.3 elimination**, the exact methods. **7.4** handles the two weird cases and lets the student aim the whole toolkit at word problems (callback to Unit 6 translation).

**Biggest misconception traps, named up front:**
- **Solving for only one variable and stopping.** A system's answer is an *ordered pair*. A student who finds x = 3 and walks away has done half the problem. Always finish by finding the partner coordinate.
- **Treating the two equations as unrelated.** Both equations describe the *same* x and the *same* y. The "mystery box" metaphor (`metaphors.md` Variables A) carries over: x is one hidden number shared by both equations.
- **Sign and like-term slips** during substitution/elimination — same roots as `misconceptions.md` §3 (negatives) and §7 (structure). The fix is the unit's own habit: substitute the final pair back into both equations.

**Pacing.** Don't drill graphing to exhaustion — its job is meaning, not precision; once the student *sees* "solution = crossing point," move to substitution. Spend the most time on elimination (the scaling step is the new motor skill). Reserve substitution for systems where a variable is already (or easily) isolated, and elimination for systems lined up in standard form — teach that judgment explicitly in 7.4. Interleave: every solved system ends with the substitution check, which quietly reviews Unit 2 evaluation.

---

## Lesson 7.1: Solving by graphing

**Goal:** Find the solution of a system by graphing both lines and reading the point where they intersect.
**Why it matters:** It makes the *meaning* of a system visible — the solution is literally where two relationships meet — and that picture anchors every algebraic method that follows.
**New terms:**
- {#7.1.d1} **System of equations:** two (or more) equations considered together, asking for values that satisfy all of them at once.
- {#7.1.d2} **Solution of a system:** an ordered pair (x, y) that makes **every** equation in the system true. A system may have **one** such pair, **none**, or **infinitely many** (see 7.4) — so don't assume there's exactly one until you've solved it.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete / motivating:** "Equation one says y = x + 1 — a whole line of possibilities. Equation two says y = -x + 5 — another whole line. A *system* asks: is there a point that lives on **both** lines at once?" Each line is a function (Unit 5); we're hunting the input where the two functions return the same output.
- **Pictorial:** Graph both. Use a **coordinate plane + two lines** artifact — see `visuals.md` **Template 2** (run it twice, once per line, on one plane). **Compute the points, don't eyeball them** (`visuals.md` rule 1). Always pair the graph with a small table of computed points and name the crossing.
- **Symbolic:** Read the intersection. Then *verify* by plugging the point into both equations — this is the move that makes graphing trustworthy and seeds the checking habit.

For y = x + 1 and y = -x + 5, compute a short table for each, then map with `screenX = 110 + x*20`, `screenY = 110 - y*20`:

$$\begin{array}{c|c|c}
x & y = x+1 & y = -x+5 \\ \hline
0 & 1 & 5 \\
2 & 3 & 3 \\
4 & 5 & 1
\end{array}$$

Both lines pass through (2, 3) — that shared row *is* the solution.

**Worked examples:**

*Example 1 — the canonical one.* Solve y = x + 1 and y = -x + 5 by graphing.
Graph both (table above). They cross at (2, 3).
Check in **both**: 3 = 2 + 1 and 3 = -2 + 5. Solution: (2, 3).

*Example 2 — a horizontal line.* Solve y = 2x and y = 6.
y = 6 is the flat line at height 6. y = 2x climbs; it reaches height 6 when x = 3. Crossing: (3, 6).
Check: 6 = 2(3) and 6 = 6.

*Example 3.* Solve y = x + 2 and y = -x + 4.
Table: at x = 1, first gives 3, second gives 3. They cross at (1, 3).
Check: 3 = 1 + 2 and 3 = -1 + 4.

*Example 4 — the limitation, on purpose.* Solve y = 2x and y = x + 1 but suppose the answer weren't clean. Here it is clean — they meet at (1, 2): 2 = 2(1), 2 = 1 + 1. Now ask: *"What if two lines crossed at (2.5, -1.3)? Could you read that off a hand-drawn graph?"* You couldn't — and that's exactly why we need substitution and elimination next.

**Watch for:**
- **Reading the picture imprecisely.** Hand graphs only reliably reveal *integer* crossings. If the intersection looks "between the lines," that's the signal to switch to an algebraic method — not to guess a decimal. State this limitation out loud; it's the bridge to 7.2.
- **Naming only one coordinate** ("the answer is 2"). Push for the ordered pair every time — see this unit's lead trap.
- **Misplotting from a sign slip** when building the table (`misconceptions.md` §3). The table-plus-check routine catches it.

**Visuals to offer:** `visuals.md` **Template 2** (coordinate plane + a line), used twice on one plane, as an **SVG artifact** with computed endpoints, the intercepts dotted, the crossing labeled, and the points table beside it. Never paste raw SVG into chat — emit an artifact.

**Check for understanding (transfer):**
1. {#7.1.c1} "Without graphing yet — what does it *mean*, in words, that (2, 3) is the solution of a system? What two things must be true?"
2. {#7.1.c2} "Two lines on the same plane never touch. What does that tell you about how many solutions the system has?" (Sets up 7.4.)
3. {#7.1.c3} "If a system's solution were (1.5, 4.2), why would graphing by hand let you down — and what would you reach for instead?"

**Practice problems** (solve by graphing / finding where the two lines meet; give the ordered pair and check both):

*Set A — one line is horizontal or through the origin*
1. y = x and y = 4
2. y = 2x and y = 6
3. y = -x + 6 and y = x

*Set B — two slanted lines*
4. y = x + 2 and y = -x + 4
5. y = x - 1 and y = -x + 3
6. y = 2x - 1 and y = x + 1

**Answer key (all verified):**
1. (4, 4) — 4 = 4, 4 = 4
2. (3, 6) — 6 = 2(3), 6 = 6
3. (3, 3) — 3 = -3 + 6, 3 = 3
4. (1, 3) — 3 = 1 + 2, 3 = -1 + 4
5. (2, 1) — 1 = 2 - 1, 1 = -2 + 3
6. (2, 3) — 3 = 2(2) - 1, 3 = 2 + 1

---

## Lesson 7.2: Substitution

**Goal:** Solve a system by isolating one variable in one equation and substituting that expression into the other, reducing two equations to a single one-variable equation.
**Why it matters:** It's exact (no graph-reading guesswork) and it shines when one variable is already alone — common in word problems and in any equation written as y = ...
**New terms:**
- {#7.2.d1} **Substitution:** replacing a variable with an expression equal to it. Because each variable denotes the *same* number in both equations, an expression equal to (say) y in one equation may stand in for y in the other.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** "Equation one tells you exactly what y *is* — say y = 2x. The mystery box y is just 2x in disguise. So anywhere the second equation says y, pour in 2x instead." (Mystery-box metaphor, `metaphors.md` Variables A — both equations share the same hidden numbers.)
- **Pictorial:** Substitution is collapsing two lines' worth of information into one equation in one unknown — the crossing point falls out as soon as only one variable remains.
- **Symbolic:** (1) isolate a variable, (2) substitute into the *other* equation, (3) solve the resulting one-variable equation, (4) back-substitute to get the partner, (5) **check both**.

**Worked examples:**

*Example 1.* Solve y = 2x and x + y = 9.
y is already isolated. Substitute 2x for y in the second:
$$x + 2x = 9 \;\Rightarrow\; 3x = 9 \;\Rightarrow\; x = 3.$$
Back-substitute: y = 2(3) = 6. Solution (3, 6).
Check: 6 = 2(3) and 3 + 6 = 9.

*Example 2 — isolate first.* Solve x = y + 1 and 2x + y = 8.
x is isolated. Substitute y + 1 for x:
$$2(y + 1) + y = 8 \;\Rightarrow\; 2y + 2 + y = 8 \;\Rightarrow\; 3y + 2 = 8 \;\Rightarrow\; 3y = 6 \;\Rightarrow\; y = 2.$$
Back-substitute: x = 2 + 1 = 3. Solution (3, 2).
Check: 3 = 2 + 1 and 2(3) + 2 = 8.

*Example 3 — watch the distribution.* Solve y = x - 2 and x + y = 10.
Substitute: x + (x - 2) = 10 ⇒ 2x - 2 = 10 ⇒ 2x = 12 ⇒ x = 6. Then y = 6 - 2 = 4. Solution (6, 4).
Check: 4 = 6 - 2 and 6 + 4 = 10.

*Example 4 — isolate when nothing is alone yet.* Solve x + y = 7 and 2x + y = 11 by substitution.
Isolate y in the first: y = 7 - x. Substitute: 2x + (7 - x) = 11 ⇒ x + 7 = 11 ⇒ x = 4. Then y = 7 - 4 = 3. Solution (4, 3).
Check: 4 + 3 = 7 and 2(4) + 3 = 11. (Note: this same system is a natural fit for elimination — preview 7.3.)

**Watch for:**
- **Substituting back into the *same* equation you isolated from.** That collapses to a true-but-useless statement (e.g. 0 = 0) and finds nothing. Always substitute into the **other** equation.
- **Dropping a sign or skipping distribution** in 2(y+1) → people write 2y + 1 (`misconceptions.md` §7 structure; §3 negatives). Distribute to *everyone* inside (handing-out-flyers, `metaphors.md`).
- **Stopping at one variable.** After x = 3, the problem is *not* done — back-substitute for y.

**Visuals to offer:** None needed; substitution is symbolic. If a student wants to *see* the answer, plot both lines (Template 2) and point to the crossing as confirmation.

**Check for understanding (transfer):**
1. {#7.2.c1} "In y = 2x and x + y = 9, why is it safe to write x + 2x = 9? What justifies swapping y for 2x?"
2. {#7.2.c2} "You isolated y in equation one. Into *which* equation do you substitute, and why not the other?"
3. {#7.2.c3} "Make up a system where substitution is clearly the easier method than elimination, and say why."

**Practice problems** (solve by substitution; give (x, y) and verify both):
1. y = 3x and x + y = 8
2. y = x + 4 and 2x + y = 10
3. x = 2y and x + y = 9
4. y = x - 1 and 3x + y = 11
5. x = y + 3 and x + 2y = 9
6. y = 2x + 1 and x + y = 7
7. y = 4x and 2x + y = 18
8. x = 3y and 2x - y = 10

**Answer key (all verified):**
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

**Goal:** Solve a system by adding or subtracting the two equations (scaling one or both first when needed) so that one variable cancels, leaving a single one-variable equation.
**Why it matters:** It's the workhorse for systems written in standard form ax + by = c, where nothing is isolated. Scaling-then-combining is the core skill that carries into later math.
**New terms:**
- {#7.3.d1} **Elimination (linear combination):** combining two equations so that one variable's terms sum to zero ("go to zero"), removing it.
- {#7.3.d2} **Scaling an equation:** multiplying an *entire* equation by a number. Because both sides are multiplied equally, the line — and the solution — is unchanged (balance scale, `metaphors.md` Equations A).

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** "If one equation says x + y = 10 and another says x - y = 4, stack them and add. The +y and -y are a debt and an equal cash — they cancel to zero (`misconceptions.md` §3). You're left with 2x = 14, one unknown."
- **Pictorial:** Adding two equations produces a *third* true equation — and **when the system has one solution**, that's a new line through the same crossing point. Choosing the right multiplier aims to kill a variable (make its terms go to zero). When **no single crossing point exists**, the combination that kills a variable doesn't leave a line at all — it collapses to a bare *numeric* statement: a **false** one (e.g. 0 = 5) when the lines are parallel, or an always-**true** one (0 = 0) when they're secretly the same line. That leftover statement is exactly the signal we exploit in 7.4, so don't be surprised when the variables vanish there.
- **Symbolic:** (1) line both equations up in ax + by = c form; (2) if neither variable's coefficients match, **scale** one or both so a pair matches; (3) add (to cancel opposite signs) or subtract (to cancel equal signs); (4) solve the one-variable result; (5) back-substitute; (6) **check both**.

Avoid the word "cancel" as magic — say the terms **go to zero** (what literally happens), per `misconceptions.md` §1.

**Worked examples:**

*Example 1 — add to cancel.* Solve x + y = 10 and x - y = 4.
The y-terms are opposites. **Add** the equations:
$$(x + y) + (x - y) = 10 + 4 \;\Rightarrow\; 2x = 14 \;\Rightarrow\; x = 7.$$
Back-substitute into x + y = 10: 7 + y = 10 ⇒ y = 3. Solution (7, 3).
Check: 7 + 3 = 10 and 7 - 3 = 4.

*Example 2 — subtract to cancel.* Solve 2x + 3y = 12 and 2x - y = 4.
The x-terms match (2x each). **Subtract** the second from the first so 2x goes to zero:
$$(2x + 3y) - (2x - y) = 12 - 4 \;\Rightarrow\; 4y = 8 \;\Rightarrow\; y = 2.$$
Back-substitute into 2x - y = 4: 2x - 2 = 4 ⇒ 2x = 6 ⇒ x = 3. Solution (3, 2).
Check: 2(3) + 3(2) = 12 and 2(3) - 2 = 4.

*Example 3 — subtract, coefficients already matched the other variable.* Solve x + y = 7 and 2x + y = 11.
The y-terms match. **Subtract**: (2x + y) - (x + y) = 11 - 7 ⇒ x = 4. Then 4 + y = 7 ⇒ y = 3. Solution (4, 3).
Check: 4 + 3 = 7 and 2(4) + 3 = 11.

*Example 4 — scaling required.* Solve 3x + 2y = 16 and x + y = 6.
Nothing matches yet. **Scale** the second equation by 2 so the y-coefficients agree: 2(x + y) = 2(6) ⇒ 2x + 2y = 12. Now subtract it from the first:
$$(3x + 2y) - (2x + 2y) = 16 - 12 \;\Rightarrow\; x = 4.$$
Back-substitute into x + y = 6: y = 2. Solution (4, 2).
Check: 3(4) + 2(2) = 16 and 4 + 2 = 6.

*Example 5 — add, opposite y-coefficients.* Solve 3x + 2y = 12 and 5x - 2y = 4.
The y-terms are +2y and -2y. **Add**:
$$(3x + 2y) + (5x - 2y) = 12 + 4 \;\Rightarrow\; 8x = 16 \;\Rightarrow\; x = 2.$$
Back-substitute into 3x + 2y = 12: 6 + 2y = 12 ⇒ 2y = 6 ⇒ y = 3. Solution (2, 3).
Check: 3(2) + 2(3) = 12 and 5(2) - 2(3) = 4.

**Watch for:**
- **Adding when you should subtract** (and vice versa). The rule: equal-sign coefficients → *subtract*; opposite-sign coefficients → *add*. A subtraction that forgets to flip *every* sign in the second equation is the classic slip (`misconceptions.md` §3) — e.g. (2x + 3y) - (2x - y) becomes 4y, not 2y.
- **Scaling only one side or only one term.** Multiply the *entire* equation — both sides, every term — or the balance breaks.
- **Stopping at the first variable.** Same trap as the rest of the unit: back-substitute for the partner.

**Visuals to offer:** None required. Optionally graph (Template 2) to confirm the crossing, especially if a student doubts the algebra.

**Check for understanding (transfer):**
1. {#7.3.c1} "In 2x + 3y = 12 and 2x - y = 4, why subtract rather than add? What tells you which to do?"
2. {#7.3.c2} "Why is it legal to multiply x + y = 6 by 2? What stays true after you do?"
3. {#7.3.c3} "Given 4x + 3y = 10 and 2x + y = 4, which equation would you scale and by what, to eliminate x? (Don't solve — just plan the move.)"

**Practice problems** (solve by elimination; scale first where needed; give (x, y) and verify both):

*Set A — add or subtract directly*
1. x + y = 8 and x - y = 2
2. x + y = 12 and x - y = 6
3. 2x + y = 9 and x - y = 3
4. 3x + y = 14 and x + y = 6
5. 2x + 3y = 13 and 2x + y = 7
6. x + 2y = 11 and x + y = 7

*Set B — scale first*
7. 3x + 2y = 16 and x + 4y = 22
8. 2x + y = 11 and 3x + 2y = 18

**Answer key (all verified):**
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

**Goal:** Recognize when a system has **no solution** or **infinitely many**, and use systems to solve two-variable word problems.
**Why it matters:** Not every pair of lines crosses once. And the real payoff of systems is modeling: two unknowns tied by two facts — tickets, coins, mixtures — solved exactly.
**New terms / the three outcomes:** every pair of lines does exactly one of three things. Teach it as this clean 3-row summary, not as a single either/or label:

| The two lines… | How many solutions | What the algebra leaves |
|---|---|---|
| **cross once** (different slopes) | **one** solution — the (x, y) where they meet | a normal value, e.g. x = 4 |
| **are parallel** (same slope, different intercept) | **no solution** — they never meet | a **false** statement, e.g. 0 = 5 |
| **are the same line** (identical after simplifying) | **infinitely many** — every point on the line works | an always-**true** statement, e.g. 0 = 0 |

- **No solution:** the parallel-lines case. Whatever method you use, the variables vanish and you're left with something **false** (like 0 = 5) — nothing can make it true, so nothing solves the system.
- **Infinitely many solutions:** the same-line case (one equation is just a multiple of the other). The variables vanish and you're left with something always **true** (like 0 = 0) — every point on the shared line works.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete / pictorial:** "Two lines on a plane do one of three things: cross once (one solution), run parallel forever (none), or sit exactly on top of each other (infinitely many)." Tie slopes to Unit 5: *same slope, different intercept → parallel → no solution; same slope, same intercept → identical → infinitely many.*
- **Symbolic tell:** When you eliminate/substitute, the *variables themselves* vanish. If what's left is **false** (0 = 5) → no solution. If it's **true** (0 = 0) → infinitely many. This is the diagnostic — teach the student to *read the leftover statement*.
- **Applications:** name the two unknowns, write two equations from the two facts (Unit 6 translation), then solve by whichever method fits, and **check both** against the story.

**Worked examples:**

*Example 1 — no solution (parallel).* Solve y = 2x + 1 and y = 2x - 3.
Substitute: 2x + 1 = 2x - 3. Subtract 2x from both sides: 1 = -3 — **false**. No (x, y) can fix that. **No solution.** (Both have slope 2, different intercepts → parallel, per Unit 5.)

*Example 2 — no solution in standard form.* Solve 2x - y = 3 and 4x - 2y = 1.
Scale eq.1 by 2: 4x - 2y = 6. Subtract eq.2: (4x - 2y) - (4x - 2y) = 6 - 1 ⇒ 0 = 5 — **false**. **No solution.**

*Example 3 — infinitely many (same line).* Solve x + y = 4 and 2x + 2y = 8.
Eq.2 is just eq.1 times 2. Scale eq.1 by 2: 2x + 2y = 8. Subtract eq.2: 0 = 0 — always **true**. The two equations are the same line; **infinitely many solutions** (every point on x + y = 4, e.g. (0,4), (1,3), (4,0)). "Infinitely many" isn't vague — it's a *precise* set: **all (x, y) with x + y = 4**. (For a stronger student you can write that as {(x, y) | x + y = 4}, but the plain-English description is enough.)

*Example 4 — application (tickets).* A theater sells adult tickets at $8 and child tickets at $5. One night it sold **200 tickets** for **$1300** total. How many of each?
Let a = adult tickets, c = child tickets.
$$a + c = 200 \qquad 8a + 5c = 1300.$$
Solve by substitution: c = 200 - a, so 8a + 5(200 - a) = 1300 ⇒ 8a + 1000 - 5a = 1300 ⇒ 3a = 300 ⇒ a = 100. Then c = 100.
Check: 100 + 100 = 200 and 8(100) + 5(100) = 800 + 500 = 1300. **100 adult, 100 child.**

*Example 5 — application (coins, less symmetric).* A jar has **15 coins**, all quarters and dimes, worth **$2.70** (270 cents). How many of each?
Let q = quarters, d = dimes.
$$q + d = 15 \qquad 25q + 10d = 270.$$
Eliminate d: scale eq.1 by 10 → 10q + 10d = 150; subtract from eq.2 → 15q = 120 ⇒ q = 8. Then d = 7.
Check: 8 + 7 = 15 and 25(8) + 10(7) = 200 + 70 = 270. **8 quarters, 7 dimes.**

*Example 6 — application (mixture).* This is the true *mixture* the objectives promise — two strengths blended to a target strength. "How many liters of a **20%** salt solution and a **50%** salt solution should you mix to make **30 liters** of a **30%** solution?"
Let x = liters of 20% solution, y = liters of 50% solution. One equation counts **liters**, the other counts **salt** (the 30 L of 30% holds 0.30 · 30 = 9 L of salt):
$$x + y = 30 \qquad 0.20x + 0.50y = 9.$$
Elimination is cleanest if you first clear decimals — multiply the salt equation by 10: 2x + 5y = 90. Scale the liter equation by 2: 2x + 2y = 60. Subtract: (2x + 5y) − (2x + 2y) = 90 − 60 ⇒ 3y = 30 ⇒ y = 10. Then x = 30 − 10 = 20.
Check in the story: 20 + 10 = 30 liters, and salt 0.20(20) + 0.50(10) = 4 + 5 = 9 L = 30% of 30. **20 L of the 20% solution, 10 L of the 50%.** (Same structure as a coin problem: one equation counts the *amount*, one counts the *active ingredient*.)

*Example 7 — application (perimeter).* A rectangle's **length is 4 more than its width**, and its **perimeter is 28**. Find the length and width as a system.
Let l = length, w = width. The two facts give two equations:
$$l = w + 4 \qquad 2l + 2w = 28.$$
Length is already isolated, so **substitute** (l = w + 4) into the perimeter equation: 2(w + 4) + 2w = 28 ⇒ 4w + 8 = 28 ⇒ 4w = 20 ⇒ w = 5. Then l = 5 + 4 = 9.
Check in the story: length 9 is 4 more than width 5, and perimeter 2(9) + 2(5) = 18 + 10 = 28. **Width 5, length 9.**

**Watch for:**
- **Calling 0 = 0 "no solution" or 0 = 5 "infinitely many."** They're swapped constantly. Anchor it: a **true** leftover means *everything* works (infinite); a **false** leftover means *nothing* works (none).
- **Reversing the two relationships in word problems** — writing 8a = total instead of counting tickets vs. counting dollars. Keep the two equations on different *units* (one counts items, one counts money) and label them (`misconceptions.md` §2 letter-as-object / variable reversal).
- **Forgetting to check against the story**, not just the algebra — negative or fractional tickets signal a setup error.

**Visuals to offer:** For the special cases, a quick **Template 2** artifact showing the two **parallel** lines (no crossing) or the two lines **coincident** (one on top of the other) makes "none" and "infinitely many" visible. Compute endpoints; label slopes/intercepts.

**Check for understanding (transfer):**
1. {#7.4.c1} "You solve a system and reach 7 = 7. How many solutions, and what do the graphs look like?"
2. {#7.4.c2} "Two lines have the same slope. What two situations are still possible, and how does the algebra tell them apart?"
3. {#7.4.c3} "A problem says '30 nickels and dimes worth $2.40.' Name your two variables and write the two equations — don't solve yet."

**Practice problems:**

*Set A — classify (one solution / none / infinitely many); if one, give it*
1. y = 3x + 2 and y = 3x - 5
2. x + y = 5 and 3x + 3y = 15
3. y = x + 1 and y = -x + 7

*Set B — applications (set up two equations, solve, check the story)*
4. Two numbers add to 30, and one is 6 more than the other. Find the numbers.
5. A snack stand: 2 burgers and 1 fries cost $11; 1 burger and 2 fries cost $10. Find the price of a burger and of fries.
6. A boat goes **20 mph downstream** (with the current) and **4 mph upstream** (against it). Find the boat's speed in still water and the speed of the current. (Hint: with the current the speeds add, against it they subtract.)
7. *(mixture)* How many milliliters of a **10%** acid solution and a **40%** acid solution make **40 mL** of a **25%** solution?
8. *(perimeter)* A rectangle's length is **2 more than its width** and its perimeter is **24**. Find the width and length.

**Answer key (all verified):**
1. **No solution** — same slope 3, different intercepts (parallel); substituting gives 2 = -5, false.
2. **Infinitely many** — eq.2 is eq.1 times 3 (same line); reduces to 0 = 0.
3. **One solution, (3, 4)** — 4 = 3 + 1, 4 = -3 + 7.
4. x + y = 30, x = y + 6 → (y + 6) + y = 30 ⇒ y = 12, x = 18. The numbers are **18 and 12** (18 + 12 = 30, 18 = 12 + 6).
5. 2b + f = 11, b + 2f = 10 → eliminate: scale eq.2 by 2 → 2b + 4f = 20, subtract eq.1 → 3f = 9, f = 3, then b = 4. **Burger $4, fries $3** (2(4)+3 = 11, 4 + 2(3) = 10).
6. Let b = boat speed in still water, c = current. Downstream the speeds add, upstream they subtract: b + c = 20, b − c = 4 → add → 2b = 24, b = 12, then c = 8. **Boat 12 mph, current 8 mph** (12 + 8 = 20, 12 − 8 = 4).
7. Let x = mL of 10%, y = mL of 40%; one equation counts mL, one counts acid (25% of 40 = 10 mL): x + y = 40, 0.10x + 0.40y = 10. Clear decimals (×10): x + 4y = 100; subtract x + y = 40 → 3y = 60 ⇒ y = 20, then x = 20. **20 mL of each** (20 + 20 = 40; 0.10(20) + 0.40(20) = 2 + 8 = 10 mL acid).
8. Let l = length, w = width: l = w + 2, 2l + 2w = 24. Substitute → 2(w + 2) + 2w = 24 ⇒ 4w + 4 = 24 ⇒ w = 5, then l = 7. **Width 5, length 7** (perimeter 2(7) + 2(5) = 24, and 7 = 5 + 2).

---

## Wrap-up & interleaving

**Consolidate:** A system is two relationships at once; in the usual case its solution is the single (x, y) that satisfies **both** — the crossing point of two lines/functions (and sometimes there's none, or infinitely many — the 7.4 special cases). Three methods, each exact except graphing: **graph** (best for meaning and integer crossings), **substitution** (best when a variable is isolated), **elimination** (best for standard form, with scaling as the key move). Two special cases: **parallel → no solution → false statement**; **same line → infinitely many → true statement**. The non-negotiable habit: **substitute the final pair back into both equations.**

**Mix back in (spaced review, per `pedagogy.md`):**
- **Unit 5** — read off slope and intercept to *predict* before solving: "same slope? then expect parallel or identical." Graphing a system is pure Unit 5 graphing, twice.
- **Unit 6** — every application is a Unit 6 translation with *two* unknowns and *two* facts; warm up with one-variable translation before a two-variable one.
- **Unit 2** — the one-variable equation left after substitution/elimination is exactly a Unit 2 solve; slip in a two-step solve as a warm-up.
- Choosing a *method* is itself a skill — give a mixed set and ask "graph, substitution, or elimination, and why?" before solving. Teach the read explicitly:
  - **A variable is already isolated** (y = …, x = …) or trivially isolatable (coefficient 1, like x + y = 7) → **substitution** is cleaner — pour the expression straight in.
  - **Both equations are in standard form** ax + by = c, **especially with a matching or opposite coefficient pair** (e.g. both 2x, or +3y and −3y) → **elimination** is cleaner — add or subtract to kill that variable on sight; if coefficients don't line up, scale one equation first.
  - **You only need to *see* / estimate the crossing, or to confirm a special case visually** → **graph** — but switch to algebra the moment the answer isn't a clean integer pair.
  - Worth a 10-second look before committing: e.g. y = 2x + 1 with 3x + y = 11 *screams* substitution (y is alone), while 3x + 2y = 12 with 5x − 2y = 4 *screams* elimination (the +2y/−2y add away).

**Progress Card should note:** which methods are fluent vs. shaky (especially the **scaling** step in elimination); whether the student reliably **finishes to the ordered pair** rather than stopping at one variable; whether they **check in both equations** automatically; and whether they correctly read 0 = 0 vs. 0 = 5 for the special cases. Flag any lingering sign slips during subtraction-elimination (`misconceptions.md` §3) for targeted warm-ups.
