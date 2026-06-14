# Unit 5: Linear Functions & Their Graphs

> **Prerequisites:** Unit 3 (ratios, rates, **unit rate**) and Unit 4 (functions, f(x) notation, multiple representations). Comfort with negatives (Unit 1.4) and substituting into an expression (Unit 1.5) is assumed throughout.
> **By the end, the student can:**
> - Plot and name ordered pairs and identify the four quadrants.
> - Graph a linear equation from a table of values and test whether a point lies on a line.
> - Compute slope from two points and recognize the four cases (positive, negative, zero, undefined).
> - Read slope and y-intercept from y = mx + b (and f(x) = mx + b) and graph a line quickly from them.
> - Write the equation of a line from a point and a slope, or from two points, and recognize parallel / perpendicular lines.

## Teaching this unit (orientation for the tutor)

This is where the abstract idea of a function from Unit 4 becomes a **picture you can read**. The throughline: **a line is a linear function**, and y = mx + b and f(x) = mx + b are the *same object* named two ways. Say this out loud and often — the y and the f(x) are interchangeable; the function machine from Unit 4 (`metaphors.md` → Functions) is now drawn as a straight line.

The single most important callback is **slope = rate of change = the unit rate from Unit 3**. Slope is not a new mysterious thing; it's "how much y changes per 1 step in x" — exactly the per-unit rate they already met. Lean hard on the stairs/ramp and speed metaphors (`metaphors.md` → Slope) and tie them back to Unit 3 explicitly.

Pacing: 5.1 is quick and concrete (most adults half-know the coordinate plane — don't belabor it, but nail the *order* of the pair and the quadrant signs). 5.2 builds the table→graph habit. 5.3 (slope) is the conceptual heart — spend the most time here. 5.4 and 5.5 are payoff lessons where everything composes.

**Biggest misconception traps in this unit:**
- **Reversing the ordered pair** — plotting (3,2) as "up 3, right 2." Always re-say "x first (across), then y (up/down)."
- **The slope fraction upside down** — computing run/rise instead of rise/run, or mismatching which point is "first" in numerator vs. denominator. See `misconceptions.md §3` (negatives in the differences are a common slip too) and have them *subtract in the same order* top and bottom.
- **Sign and negative-coefficient errors** in y = mx + b (e.g. calling the intercept of y = -3x + 5 "−5"). This is the negatives work of `misconceptions.md §3` resurfacing in a new costume.
- **Zero vs. undefined slope** confusion (horizontal is 0; vertical is undefined). Anchor with the ramp/wall picture.

**Visuals:** this unit is visual-heavy. Use `visuals.md` **Template 2** (coordinate plane + line) for every graph. The rules there are non-negotiable: **COMPUTE the points** (plug x-values into the equation, ideally with the code tool), emit the graph as an **SVG artifact** (raw SVG in chat does not render), **label** axes and key points (intercept, slope), and **always pair the artifact with a small table of points** in the chat so it helps even if the panel doesn't open. The coordinate-mapping rule for these graphs is `screenX = 110 + x*20`, `screenY = 110 - y*20` (note the minus — up on the page is larger y).

---

## Lesson 5.1: The coordinate plane

**Goal:** Plot and name ordered pairs (x, y) and identify which of the four quadrants (or axis) a point lies in.
**Why it matters:** Every graph in the rest of algebra lives here. A function's table of inputs/outputs becomes *points*, and a line is just infinitely many of them.
**New terms:**
- **Coordinate plane:** a flat grid made by two number lines crossing at right angles.
- **x-axis / y-axis:** the horizontal and vertical number lines. They cross at the **origin**, (0,0).
- **Ordered pair (x, y):** an address for a point — *x first* (how far across, right is +), *then y* (how far up/down, up is +). Order matters: (3,2)≠(2,3).
- **Quadrant:** one of the four regions the axes cut the plane into, numbered **I, II, III, IV** counter-clockwise starting top-right.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** "It's a street map. The x-coordinate is how many blocks east/west; the y-coordinate is how many blocks north/south. You always say the east-west one first." Ask them to give *you* directions to a point before you give them any.
- **Pictorial:** Offer the labeled-plane SVG artifact (Template 2 skeleton — axes only, then drop in the points). Show the four quadrants and the sign pattern. Have them predict the quadrant *before* plotting, from the signs alone.
- **Symbolic:** Connect to the sign rule:

$$\text{I: }(+,+)\qquad \text{II: }(-,+)\qquad \text{III: }(-,-)\qquad \text{IV: }(+,-)$$

A point with a 0 coordinate sits *on an axis*, not in a quadrant — flag this, it's a favorite trick.

**Worked examples:** Plot (3,2), (-1,4), (0,-3), (-2,-2) and name each quadrant.

- (3,2): x is +, y is + → right 3, up 2 → **Quadrant I**.
- (-1,4): x is −, y is + → left 1, up 4 → **Quadrant II**.
- (0,-3): x is 0 → no left/right; down 3 → sits **on the y-axis** (no quadrant).
- (-2,-2): both − → left 2, down 2 → **Quadrant III**.

Offer the artifact (computed screen coords, Template 2 mapping): (3,2)→(170,70), (-1,4)→(90,30), (0,-3)→(110,170), (-2,-2)→(70,150). Always include the companion table:

| Point | x | y | Location |
|-------|----|----|----------|
| (3,2) | +3 | +2 | Quadrant I |
| (-1,4) | −1 | +4 | Quadrant II |
| (0,-3) | 0 | −3 | y-axis |
| (-2,-2) | −2 | −2 | Quadrant III |

**Watch for:** **Reversing the pair** (the #1 error here) — plotting (-1,4) as left-4-up-1. Tell: their point lands in the wrong quadrant for the signs, or they hesitate over which number moves which way. Repair with a transfer, not a repeat: "Read me the address again — which number is *across*?" Also watch the **axis-point trap**: (0,-3) is *not* in a quadrant. (These are surface-level, but the negative-sign care of `misconceptions.md §3` applies to reading the signs.)

**Visuals to offer:** `visuals.md` **Template 2** (coordinate plane). Use the axes-only skeleton, then add a small `<circle>` + label per point. Computed, labeled, with the table above.

**Check for understanding (transfer):**
1. "Without plotting, which quadrant is (-7, -2) in, and how do the signs tell you?"
2. "I plotted a point in Quadrant IV. What can you say about the signs of its coordinates?"
3. "Where does (4, 0) live — and why isn't it in a quadrant?"

**Practice problems:**
*Name the quadrant (or axis):*
1. (5, 3)
2. (-4, -1)
3. (-2, 6)
4. (3, -5)
5. (8, -2)
6. (-6, 1)
7. (4, 0)
8. (0, 7)
9. (0, 0)
*Plot & locate:*
10. Plot (-3, 1) and name its quadrant.

**Answer key:**
1. Quadrant I · 2. Quadrant III · 3. Quadrant II · 4. Quadrant IV · 5. Quadrant IV · 6. Quadrant II · 7. on the x-axis (no quadrant) · 8. on the y-axis (no quadrant) · 9. the origin (no quadrant) · 10. left 3, up 1 → Quadrant II.

---

## Lesson 5.2: Graphing linear equations from a table

**Goal:** Build a table of values from a linear equation, plot the points, connect them into a line, and test whether a given point lies *on* the line by substitution.
**Why it matters:** This is the bridge from "equation" to "picture." It also teaches the meaning of a solution to a two-variable equation — every point on the line is a solution; everything off it is not.
**New terms:**
- **Table of values:** a list of x inputs and their computed y outputs — exactly the input→output table from Unit 4.3, now plotted.
- **"On the line":** a point (a,b) is on the line when its coordinates make the equation true — i.e. substituting x=a gives y=b.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete / function callback:** "This equation is a function machine (`metaphors.md` → Functions). Feed it x-values, it returns y-values. y = 2x-1 *is* f(x) = 2x-1 — same machine, two names." Have them compute a couple of outputs.
- **Pictorial:** Plot the computed points; they fall in a straight row → connect into a line. Emphasize the line is *all* such points, not just the four you plotted. Offer the SVG artifact.
- **Symbolic:** Test membership by substitution: is (3,5) on y=2x-1? Compute 2(3)-1 = 5; it matches → yes. This is the substitute-and-check habit from `SKILL.md`, reused.

**Worked examples:** Graph y = 2x - 1; then test (3,5) and (3,4).

Table (compute each y — verify with the code tool):

| x | 2x-1 | y |
|----|--------|----|
| −1 | 2(-1)-1 | −3 |
| 0 | 2(0)-1 | −1 |
| 1 | 2(1)-1 | 1 |
| 2 | 2(2)-1 | 3 |

Points (-1,-3),(0,-1),(1,1),(2,3) lie in a straight line. Artifact (Template 2): pick two convenient endpoints (-2,-5)→(70,210) and (3,5)→(170,10); mark the y-intercept (0,-1)→(110,130); label the line y=2x-1.

Membership tests:
- (3,5): 2(3)-1 = 5. 5 = 5 → **on the line**.
- (3,4): 2(3)-1 = 5, but the point says y=4. 5 ≠ 4 → **not on the line**.

**Watch for:**
- **Plotting from a sign-slipped table** — e.g. getting y=-3 wrong because of the negative input. This is `misconceptions.md §3` again; have them verify the table with the code tool before plotting a wrong picture (`visuals.md`: a wrong graph is worse than none).
- **Thinking "close" counts** for membership. It's exact: the substitution either matches or it doesn't.
- **Connecting points in the wrong order / freehand bowing** — for a *linear* equation the points are collinear; if one is off the line, recheck its arithmetic, don't bend the line to fit.

**Visuals to offer:** `visuals.md` **Template 2** — line from two computed endpoints, intercept dotted and labeled, companion table always included.

**Check for understanding (transfer):**
1. "Without graphing, is (4, 7) on y = 2x - 1? Show me how you know."
2. "Two of these are on y = 3x + 2: (1, 5), (2, 8), (0, 3). Which one isn't, and why?"
3. "If (a, b) is on the line and you change only b, is it still on the line? What does that mean about the point?"

**Practice problems:**
*Build the table for y = 3x + 2 (problems 1–4: find y for each x):*
1. x = -1
2. x = 0
3. x = 1
4. x = 2
*Build the table for y = -x + 4:*
5. x = 1
6. x = 2
*Test membership:*
7. Is (2, 8) on y = 3x + 2?
8. Is (1, 4) on y = 3x + 2?

**Answer key:**
1. 3(-1)+2 = -1 · 2. 3(0)+2 = 2 · 3. 3(1)+2 = 5 · 4. 3(2)+2 = 8 · 5. -(1)+4 = 3 · 6. -(2)+4 = 2 · 7. 3(2)+2 = 8; 8=8 → **yes, on the line** · 8. 3(1)+2 = 5≠4 → **no, not on the line**.

---

## Lesson 5.3: Slope

**Goal:** Compute slope as a rate of change, m = rise/run = (y₂ - y₁)/(x₂ - x₁), and recognize the four cases: positive, negative, zero (horizontal), and undefined (vertical).
**Why it matters:** Slope is the steepness *and direction* of a line, and it's the single number that drives everything in 5.4–5.5. It's also the direct graphical face of the **unit rate** from Unit 3.
**New terms:**
- **Slope (m):** how much y changes for each 1-unit increase in x — the line's rate of change.
- **Rise:** vertical change (y₂ - y₁). **Run:** horizontal change (x₂ - x₁).

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete / Unit 3 callback:** "Slope is a rate. In Unit 3, '60 miles per **1** hour' was a unit rate; on a distance-vs-time graph that *is* the slope (`metaphors.md` → Slope B, speed). Slope is just rise per 1 run." Then the **stairs/ramp** picture (`metaphors.md` → Slope A): steep stairs = big slope, gentle ramp = small, downhill = negative, flat landing = 0, a wall = undefined (you can't go forward at all).
- **Pictorial:** On a graph, draw the right triangle between two points: go *up* the rise, *across* the run. Offer an artifact if it helps them see the triangle.
- **Symbolic:** $$m = \frac{y_2 - y_1}{x_2 - x_1}$$ Stress: **subtract the y's and the x's in the *same order*** (same point first in both). Verify computations with the code tool.

**Worked examples:**

1. Through (1,2) and (3,8):
$$m = \frac{8 - 2}{3 - 1} = \frac{6}{2} = 3$$
Positive → uphill left-to-right. (Artifact: (1,2)→(130,70), (3,8) runs off the small viewBox — pick on-screen endpoints like (1,2) and (2,5)→(150,50) if you graph it, and say so.)

2. Through (0,5) and (2,1):
$$m = \frac{1 - 5}{2 - 0} = \frac{-4}{2} = -2$$
Negative → downhill.

3. Horizontal line y = 4: every point has y=4, so rise = 0: m = 0/run = 0. **Slope 0.**

4. Vertical line x = 3: every point has x=3, so run = 0: m = rise/0, division by zero → **undefined slope.**

Anchor cases with the ramp/wall: zero = flat landing, undefined = wall.

**Watch for:**
- **Rise/run flipped** (computing (x₂-x₁)/(y₂-y₁)). Tell: their slope is the reciprocal of the right answer. Cue: "Which is the *rise* — the up-down change or the across change?"
- **Inconsistent subtraction order** — e.g. y₂ - y₁ on top but x₁ - x₂ on bottom, flipping the sign. This collides with `misconceptions.md §3` (sign errors in the differences). Have them label point 1 and point 2 and subtract the same way both times; verify with code.
- **Zero ↔ undefined swap.** Tell: they call a vertical line "slope 0" or a horizontal line "undefined." Repair with the wall (can't move forward → undefined) vs. flat landing (no rise → 0).

**Visuals to offer:** `visuals.md` **Template 2** with the rise/run right triangle drawn between two computed points; label rise, run, and m. Companion table of the two points always included.

**Check for understanding (transfer):**
1. "A line goes through (2,3) and (6,11). Find the slope, and tell me in words what it says about how y changes."
2. "One line has slope 5, another has slope 1/2. Which is steeper, and how do you know?"
3. "What's the slope of a perfectly horizontal line? A perfectly vertical one? Why is one a number and the other 'undefined'?"

**Practice problems (find the slope through the two points):**
1. (1,2) and (3,8)
2. (0,5) and (2,1)
3. (2,3) and (6,11)
4. (-1,4) and (2,-2)
5. (0,0) and (4,8)
6. (1,1) and (5,3)
7. (-2,-3) and (2,5)
8. (3,7) and (3,2)
9. (-1,2) and (4,2)
10. (2,5) and (6,5)
11. (1,6) and (4,0)
12. (1,-1) and (3,-7)

**Answer key:**
1. (8-2)/(3-1)=3 · 2. (1-5)/(2-0)=-2 · 3. (11-3)/(6-2)=2 · 4. (-2-4)/(2-(-1))=-6/3=-2 · 5. (8-0)/(4-0)=2 · 6. (3-1)/(5-1)=1/2 · 7. (5-(-3))/(2-(-2))=8/4=2 · 8. run =3-3=0 → **undefined** (vertical) · 9. (2-2)/(4-(-1))=0 (horizontal) · 10. (5-5)/(6-2)=0 (horizontal) · 11. (0-6)/(4-1)=-6/3=-2 · 12. (-7-(-1))/(3-1)=-6/2=-3.

---

## Lesson 5.4: Slope-intercept form y = mx + b

**Goal:** Read slope m and y-intercept (0,b) directly from y = mx + b (and the function form f(x) = mx + b), and graph a line fast by plotting b then using rise/run.
**Why it matters:** This is the workhorse form. Once a line is in it, you can graph it in seconds and read its behavior at a glance — no table needed.
**New terms:**
- **Slope-intercept form:** y = mx + b, where m is the slope and b is the **y-intercept** — the y-value where the line crosses the y-axis, at the point (0, b).
- **Function form:** f(x) = mx + b — the same line, named as a function. "b is the starting output at x=0; m is how fast the output climbs."

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** "b is your *starting point* on the y-axis; m is your *rate* of climbing from there — your Unit-3 rate again." Tie f(0) = b: feeding 0 to the machine returns the intercept.
- **Pictorial:** Graph by hand: plot (0,b), then from there step the slope — for m = 2 = 2/1, go up 2, right 1, mark the next point, connect. Offer the artifact.
- **Symbolic:** Read m and b straight off. Caution: the sign travels with the number — in y = -3x + 5, m = -3 (not 3), b = 5.

**Worked examples:**

1. y = 2x + 1: slope m = 2, y-intercept (0, 1). Graph: plot (0,1), up 2 right 1 to (1,3). Artifact endpoints (-2,-3)→(70,170), (2,5)→(150,10); intercept (0,1)→(110,90).

2. y = -3x + 5: slope m = -3 (down 3 for each right 1), y-intercept (0, 5). The minus sign is part of the slope — the classic trap.

3. f(x) = (1/2)x - 2: slope m = 1/2, y-intercept (0, -2). As a function: f(0) = -2 (the intercept), f(4) = (1/2)(4) - 2 = 0. Artifact: (0,-2)→(110,150), (4,0)→(190,110). Companion table:

| x | f(x)=(1/2)x-2 | point |
|----|----|----|
| 0 | −2 | (0,-2) intercept |
| 2 | −1 | (2,-1) |
| 4 | 0 | (4,0) x-intercept |

**Watch for:**
- **Dropping the sign of m or b** (calling y=-3x+5's slope "3" or intercept "−5"). `misconceptions.md §3`. Cue: "Read the sign that's *attached* to the number."
- **Swapping m and b** — reading y = 2x + 1 as "slope 1, intercept 2." Anchor: m rides *with the x*; b stands alone.
- **Forgetting the intercept is a *point* (0,b)**, not just a number — matters when they plot.
- **Form not solved for y yet:** if it's 2x + y = 5, they must isolate y first (y = -2x + 5) — callback to Unit 2 solving.

**Visuals to offer:** `visuals.md` **Template 2** — plot the intercept, draw the line through a second computed point, label slope and intercept, table alongside.

**Check for understanding (transfer):**
1. "In y = -4x + 7, what's the slope and where does the line cross the y-axis? Which way does it tilt?"
2. "Write the equation of the line with slope 1/3 and y-intercept (0, -5)."
3. "For f(x) = (1/2)x - 2, what is f(0), and why is that the y-intercept?"

**Practice problems:**
*Identify slope and y-intercept:*
1. y = 4x - 7
2. y = -x + 6
3. f(x) = (2/3)x + 1
4. y = 5x
*Write the equation given m and b:*
5. m = 3, b = -4
6. m = -2, b = 1
*Find a point on the line (evaluate):*
7. For y = 2x + 1, find y when x = 3.
8. For y = -3x + 5, find y when x = 2.
9. For f(x) = (1/2)x - 2, find f(4).
10. For f(x) = (1/2)x - 2, find f(-2).

**Answer key:**
1. slope 4, y-intercept (0,-7) · 2. slope -1, y-intercept (0,6) · 3. slope 2/3, y-intercept (0,1) · 4. slope 5, y-intercept (0,0) · 5. y = 3x - 4 · 6. y = -2x + 1 · 7. 2(3)+1 = 7 · 8. -3(2)+5 = -1 · 9. (1/2)(4)-2 = 0 · 10. (1/2)(-2)-2 = -3.

---

## Lesson 5.5: Writing equations of lines

**Goal:** Write a line's equation from a point and a slope, or from two points; recognize and use parallel (equal slopes) and perpendicular (negative-reciprocal slopes) relationships.
**Why it matters:** This is "modeling with lines" — given any two facts that pin a line down, produce its equation. It feeds directly into Unit 6 (modeling) and Unit 7 (systems).
**New terms:**
- **Point-slope form:** y - y₁ = m(x - x₁) — build a line from one point (x₁,y₁) and a slope m. (Then tidy into y = mx + b if desired.)
- **Parallel lines:** never meet; **equal slopes** (m₁ = m₂), different intercepts.
- **Perpendicular lines:** cross at a right angle; slopes are **negative reciprocals** (m₂ = -1/m₁), so their product is -1.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** "A slope alone gives infinitely many parallel lines; a slope *plus one point it passes through* nails down exactly one." Point-slope is the tool that uses exactly those two facts.
- **Pictorial:** Show two parallel lines (same tilt, shifted) and two perpendicular lines (one tilts up, the other down and 'sideways-flipped'). The negative reciprocal of 2 is -1/2: flip 2 to 1/2, negate.
- **Symbolic:** From two points: first find m (Lesson 5.3), then plug m and *either* point into point-slope, then simplify to slope-intercept. Verify the final line by checking it passes through the given point(s) — substitute (the `SKILL.md` habit). A clean shortcut once m is known: b = y₁ - m x₁.

**Worked examples:**

1. Through (2,3) with slope 4:
$$y - 3 = 4(x - 2) \;\Rightarrow\; y - 3 = 4x - 8 \;\Rightarrow\; y = 4x - 5$$
Check: at x=2, 4(2)-5 = 3.

2. Through (1,2) and (3,8): first m = (8-2)/(3-1) = 3. Then with (1,2):
$$y - 2 = 3(x - 1) \;\Rightarrow\; y = 3x - 1$$
Check: at x=3, 3(3)-1 = 8.

3. Parallel to y = 2x + 1 through (0,4): parallel ⇒ same slope m = 2. It crosses the y-axis at (0,4), so b = 4:
$$y = 2x + 4$$

4. Perpendicular to y = 2x through (0,0): perpendicular ⇒ slope is the negative reciprocal of 2, i.e. -1/2. Through the origin b = 0:
$$y = -\tfrac12 x$$

**Watch for:**
- **Sign slips in point-slope expansion** — y - 3 = 4(x-2) becoming y = 4x - 8 + 3 handled wrong, or distributing the 4 onto only the x. `misconceptions.md §3` and §7 (distribution — `metaphors.md` flyers). Have them distribute carefully and **substitute the point back** to verify.
- **Negative reciprocal half-done** — taking just the reciprocal (1/2) or just the negative (-2) instead of *both* (-1/2). Cue: "flip *and* change the sign — what's -1/2?" Check: m₁ · m₂ should equal -1.
- **Mixing up which is parallel vs. perpendicular** (equal slope vs. negative reciprocal). Anchor: parallel = same tilt = same m; perpendicular = right angle = flipped-and-negated.
- **Subtraction-order slip when finding m** from two points (carryover from 5.3).

**Visuals to offer:** `visuals.md` **Template 2**. For parallel/perpendicular, graph both lines on one plane (computed endpoints) so the equal tilt / right angle is visible; label each line's equation. Table of the defining points alongside.

**Check for understanding (transfer):**
1. "Write the equation of the line through (1, 5) with slope -2. Then verify it actually passes through that point."
2. "A line is perpendicular to y = (1/3)x + 2. What's its slope, and how did you get it?"
3. "Two lines: y = 5x - 1 and y = 5x + 4. Parallel, perpendicular, or neither? How can you tell without graphing?"

**Practice problems:**
*Write the equation (point + slope):*
1. Through (3,1), slope 2.
2. Through (-1,4), slope -3.
*Write the equation (two points — find m first):*
3. Find the slope through (2,5) and (4,11).  4. Then write the line's equation.
5. Find the slope through (0,-2) and (3,7).  6. Then write the line's equation.
*Parallel & perpendicular:*
7. What is the slope of any line parallel to y = 3x - 2?
8. What is the slope of any line perpendicular to y = 2x + 1?
9. Write the line perpendicular to y = 2x passing through (4, 0).
10. Are y = 4x + 3 and y = 4x - 7 parallel, perpendicular, or neither? What about y = 4x + 3 and y = -(1/4)x?

**Answer key:**
1. y - 1 = 2(x-3) ⇒ y = 2x - 5 · 2. y - 4 = -3(x+1) ⇒ y = -3x + 1 · 3. m = (11-5)/(4-2) = 3 · 4. y - 5 = 3(x-2) ⇒ y = 3x - 1 · 5. m = (7-(-2))/(3-0) = 3 · 6. b = -2, so y = 3x - 2 · 7. slope 3 (equal slopes) · 8. slope -1/2 (negative reciprocal of 2) · 9. slope -1/2, through (4,0): b = 0 - (-1/2)(4) = 2, so y = -(1/2)x + 2 · 10. y=4x+3 and y=4x-7 are **parallel** (both slope 4); y=4x+3 and y=-(1/4)x are **perpendicular** (4 · -1/4 = -1).

---

## Wrap-up & interleaving

**Consolidate:** the five representations of a line now hang together — a *table* (5.2) gives points, the *graph* (5.1–5.2) shows them, the *slope* (5.3) is the rate between them, y=mx+b (5.4) reads slope and intercept at a glance, and *point-slope* (5.5) builds the equation from scratch. Keep saying the line **is a function**: y = mx+b and f(x)=mx+b are one object.

**Mix back in:**
- **Unit 3 (rate):** every time slope appears, name it as the unit rate / rate of change — that's the conceptual glue.
- **Unit 4 (functions):** evaluate f(0) to find the intercept; read a line off a table; use the vertical-line-test framing if a "line" is actually vertical (x=3 is not a function).
- **Unit 2 (solving):** to graph 2x + y = 5 they must solve for y first; point-slope expansion reuses the distributive property (Unit 2.3, `misconceptions.md §7`).
- **Negatives (Unit 1.4 / `misconceptions.md §3`):** the dominant error source here — slope sign, intercept sign, differences in the slope formula. Slip in a negative-laden problem regularly.

**Looking ahead:** Unit 6 turns words into these equations (modeling); Unit 7 graphs *two* lines to solve systems; Unit 8 shades regions bounded by lines. Solid slope-intercept fluency pays off in all three.

**Progress Card should note:** which lessons are mastered (5.1–5.5), whether slope sign-handling and the zero-vs-undefined distinction are solid, whether they can move fluidly between table ↔ graph ↔ y=mx+b, and any lingering negative-sign shakiness to warm up next time.
