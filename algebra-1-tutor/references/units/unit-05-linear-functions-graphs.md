# Unit 5: Linear Functions & Their Graphs

> **Prerequisites:** Unit 3 (ratios, rates, **unit rate**) and Unit 4 (functions, f(x) notation, multiple representations). Comfort with negatives (Unit 1.5) and substituting into an expression (Unit 1.6) is assumed throughout.
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
- **Steepness vs. direction** — reading the *sign* of the slope (which only sets uphill/downhill) as if it set steepness, so a line with slope −3 gets called "less steep" than slope +2. Steepness is the *magnitude* |slope|. See `misconceptions.md §8`.

**Visuals:** this unit is visual-heavy. Use `visuals.md` **Template 2** (coordinate plane + line) for every graph. The rules there are non-negotiable: **COMPUTE the points** (plug x-values into the equation, ideally with the code tool), emit the graph as an **SVG artifact** (raw SVG in chat does not render), **label** axes and key points (intercept, slope), and **always pair the artifact with a small table of points** in the chat so it helps even if the panel doesn't open. The coordinate-mapping rule for these graphs is `screenX = 110 + x*20`, `screenY = 110 - y*20` (note the minus — up on the page is larger y); machine-compute every (x,y)→(screenX,screenY) pair from this mapping rather than eyeballing it. **Always plot a THIRD point as a checkpoint:** if the three points aren't collinear, recheck the arithmetic before drawing — a wrong graph is worse than none — so the companion tables should carry three rows, not two.

---

## Lesson 5.1: The coordinate plane

**Goal:** Plot and name ordered pairs (x, y) and identify which of the four quadrants (or axis) a point lies in.
**Why it matters:** Every graph in the rest of algebra lives here {#5.1.f1}. A function's table of inputs/outputs becomes *points*, and a line is just infinitely many of them.
**New terms:**
- {#5.1.d1} **Coordinate plane:** a flat grid made by two number lines crossing at right angles.
- {#5.1.d2} **x-axis / y-axis:** the horizontal and vertical number lines. They cross at the **origin**, (0,0).
- {#5.1.d3} **Ordered pair (x, y):** an address for a point — *x first* (how far across, right is +), *then y* (how far up/down, up is +). Order matters: (3,2)≠(2,3).
- {#5.1.d4} **Quadrant:** one of the four regions the axes cut the plane into, numbered **I, II, III, IV** counter-clockwise starting top-right.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** "It's a street map. The x-coordinate is how many blocks east/west; the y-coordinate is how many blocks north/south. You always say the east-west one first." Ask them to give *you* directions to a point before you give them any.
- **Pictorial:** Offer the labeled-plane SVG artifact (Template 2 skeleton — axes only, then drop in the points). Show the four quadrants and the sign pattern. Have them predict the quadrant *before* plotting, from the signs alone.
- **Symbolic:** Connect to the sign rule:

$$\text{I: }(+,+)\qquad \text{II: }(-,+)\qquad \text{III: }(-,-)\qquad \text{IV: }(+,-)$$

A point with a 0 coordinate sits *on an axis*, not in a quadrant — flag this, it's a favorite trick.

**Worked examples:** Plot (3,2), (-1,4), (0,-3), (-2,-2) and name each quadrant.

{#5.1.w1}
- (3,2): x is +, y is + → right 3, up 2 → **Quadrant I**.
{#5.1.w2}
- (-1,4): x is −, y is + → left 1, up 4 → **Quadrant II**.
{#5.1.w3}
- (0,-3): x is 0 → no left/right; down 3 → sits **on the y-axis** (no quadrant).
{#5.1.w4}
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
1. {#5.1.c1} "Without plotting, which quadrant is (-7, -2) in, and how do the signs tell you?"
2. {#5.1.c2} "I plotted a point in Quadrant IV. What can you say about the signs of its coordinates?"
3. {#5.1.c3} "Where does (4, 0) live — and why isn't it in a quadrant?"

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
- {#5.2.d1} **Table of values:** a list of x inputs and their computed y outputs — exactly the input→output table from Unit 4.4, now plotted.
- {#5.2.d2} **"On the line":** a point (a,b) is on the line when its coordinates make the equation true — i.e. substituting x=a gives y=b.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete / function callback:** "This equation is a function machine (`metaphors.md` → Functions). Feed it x-values, it returns y-values. y = 2x-1 *is* f(x) = 2x-1 — same machine, two names." Have them compute a couple of outputs.
- **Pictorial:** Plot the computed points; they fall in a straight row → connect into a line. Emphasize the line is *all* such points, not just the four you plotted. Offer the SVG artifact.
- **Symbolic:** Test membership by substitution: is (3,5) on y=2x-1? Compute 2(3)-1 = 5; it matches → yes. This is the substitute-and-check habit from `SKILL.md`, reused.

**Worked examples:** Graph y = 2x - 1; then test (3,5) and (3,4).

Table (compute each y — verify with the code tool):

{#5.2.w1}
{#5.2.w2}
{#5.2.w3}
{#5.2.w4}

| x | 2x-1 | y |
|----|--------|----|
| −1 | 2(-1)-1 | −3 |
| 0 | 2(0)-1 | −1 |
| 1 | 2(1)-1 | 1 |
| 2 | 2(2)-1 | 3 |

Points (-1,-3),(0,-1),(1,1),(2,3) lie in a straight line. Artifact (Template 2): pick two convenient endpoints (-2,-5)→(70,210) and (3,5)→(170,10); mark the y-intercept (0,-1)→(110,130); label the line y=2x-1.

Membership tests:
{#5.2.w5}
- (3,5): 2(3)-1 = 5. 5 = 5 → **on the line**.
{#5.2.w6}
- (3,4): 2(3)-1 = 5, but the point says y=4. 5 ≠ 4 → **not on the line**.

**Watch for:**
- **Plotting from a sign-slipped table** — e.g. getting y=-3 wrong because of the negative input. This is `misconceptions.md §3` again; have them verify the table with the code tool before plotting a wrong picture (`visuals.md`: a wrong graph is worse than none).
- **Thinking "close" counts** for membership. It's exact: the substitution either matches or it doesn't.
- **Connecting points in the wrong order / freehand bowing** — for a *linear* equation the points are collinear; if one is off the line, recheck its arithmetic, don't bend the line to fit.

**Visuals to offer:** {#5.2.f1} `visuals.md` **Template 2** — line from two computed endpoints, intercept dotted and labeled, companion table always included.

**Check for understanding (transfer):**
1. {#5.2.c1} "Without graphing, is (4, 7) on y = 2x - 1? Show me how you know."
2. {#5.2.c2} "Two of these are on y = 3x + 2: (1, 5), (2, 8), (0, 3). Which one isn't, and why?"
3. {#5.2.c3} "If (a, b) is on the line and you change only b, is it still on the line? What does that mean about the point?"

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
- {#5.3.d1} **Slope (m):** how much y changes for each 1-unit increase in x — the line's rate of change.
- {#5.3.d2} **Rise:** vertical change (y₂ - y₁). **Run:** horizontal change (x₂ - x₁).

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete / Unit 3 callback:** "Slope is a rate. In Unit 3, '60 miles per **1** hour' was a unit rate; on a distance-vs-time graph that *is* the slope (`metaphors.md` → Slope B, speed). Slope is just rise per 1 run." Then the **stairs/ramp** picture (`metaphors.md` → Slope A): steep stairs = big slope, gentle ramp = small, downhill = negative, flat landing = 0, a wall = undefined (you can't go forward at all).
- **Pictorial:** On a graph, draw the right triangle between two points: go *up* the rise, *across* the run. Offer an artifact if it helps them see the triangle.
- **Symbolic:** $$m = \frac{y_2 - y_1}{x_2 - x_1}$$ Stress: **subtract the y's and the x's in the *same order*** (same point first in both). Verify computations with the code tool.

**The defining property — constant rate of change.** What makes a linear function *linear* is that its rate of change is **constant**: pick *any* two points on the line and the slope comes out the same. That's the whole reason the points fall in a straight line, and the reason the slope formula gives one well-defined m no matter which two points you feed it. Said in steps: **equal steps in x always produce equal steps in y.** For y = 2x - 1, stepping x by 1 (x = 0,1,2,3 → y = -1,1,3,5) bumps y by 2 every time — that fixed +2 per +1 *is* the slope. (This is the OpenStax / LibreTexts "constant rate of change" definition of a linear function; it's also what separates a line from a curve, where the rate keeps changing.) Use this to justify slope rather than presenting it as a recipe — and call back to 5.2: this constant rate is *why* the table's points were collinear.

**Worked examples:**

1. Through (1,2) and (3,8):
$$m = \frac{8 - 2}{3 - 1} = \frac{6}{2} = 3$$
Positive → uphill left-to-right. (Artifact: (1,2)→(130,70), (3,8) runs off the small viewBox — pick on-screen endpoints like (1,2) and (2,5)→(150,10) if you graph it, and say so.)

2. Through (0,5) and (2,1):
$$m = \frac{1 - 5}{2 - 0} = \frac{-4}{2} = -2$$
Negative → downhill.

3. Horizontal line y = 4: every point has y=4, so rise = 0: m = 0/run = 0. **Slope 0.**

4. Vertical line x = 3: every point has x=3, so run = 0: m = rise/0, division by zero → **undefined slope.**

Anchor cases with the ramp/wall: zero = flat landing, undefined = wall.

5. **Slope in context (with units).** A line on a cost(\$)-vs-time(hours) graph passes through (0, 20) and (4, 80). Find the slope and say what it *means*.
$$m = \frac{80 - 20}{4 - 0} = \frac{60}{4} = 15$$
The slope is **15 dollars per hour** — the cost climbs \$15 for each additional hour. Read its *units* off the axes: (dollars)/(hour). The intercept carries meaning too: the point (0, 20) says the cost is already \$20 at 0 hours — a \$20 starting charge. Constant-rate check: at (2, 50), (50 - 20)/(2 - 0) = 15 too, so the rate really is steady. This is the **rate of change** framing made concrete — slope always *means* "so much output per 1 of input," and naming the units turns a bare number into a rate you can read aloud. (Primes Unit 6 modeling.)

6. **Slope two ways — graph vs. formula.** For the line through (1, 2) and (4, 8), compute the slope both ways and compare.
   - *From the graph (rise/run):* draw the right triangle between the points — go **up 6** (from y = 2 to y = 8) and **across 3** (from x = 1 to x = 4), so m = rise/run = 6/3 = **2**.
   - *From the formula:* $$m = \frac{8 - 2}{4 - 1} = \frac{6}{3} = 2$$
   Same answer, as it must be — rise/run and (y₂ - y₁)/(x₂ - x₁) are the *same* subtraction, just one read off a picture and one off the coordinates. **When is each handier?** Rise/run is quickest when you already have a graph and can *count* boxes; the formula is safer when the points are given as numbers (especially negatives or fractions), where counting on a grid is error-prone. Teach both and let the student pick the tool that fits what they're handed.

**Watch for:**
- **Rise/run flipped** (computing (x₂-x₁)/(y₂-y₁)). Tell: their slope is the reciprocal of the right answer. Cue: "Which is the *rise* — the up-down change or the across change?"
- **Inconsistent subtraction order** — e.g. y₂ - y₁ on top but x₁ - x₂ on bottom, flipping the sign. This collides with `misconceptions.md §3` (sign errors in the differences). Have them label point 1 and point 2 and subtract the same way both times; verify with code.
- **Zero ↔ undefined swap.** Tell: they call a vertical line "slope 0" or a horizontal line "undefined." Repair with the wall (can't move forward → undefined) vs. flat landing (no rise → 0).
- **The ambiguous phrase "no slope."** Avoid it for vertical lines — some students hear "no slope" as "slope 0." Say **"undefined slope"** for vertical and **"zero slope"** for horizontal, so the two never blur.

**Visuals to offer:** {#5.3.f1} `visuals.md` **Template 2** with the rise/run right triangle drawn between two computed points; label rise, run, and m. Companion table of the two points always included.

**Check for understanding (transfer):**
1. {#5.3.c1} "A line goes through (2,3) and (6,11). Find the slope, and tell me in words what it says about how y changes."
2. {#5.3.c2} "One line has slope 5, another has slope 1/2. Which is steeper, and how do you know?"
3. {#5.3.c3} "What's the slope of a perfectly horizontal line? A perfectly vertical one? Why is one a number and the other 'undefined'?"
4. {#5.3.c4} "A savings graph passes through (0, 50) and (4, 90), where x is weeks and y is dollars. What is the slope *with its units*, and what does it tell you about the saving? What does the 50 mean?"
5. {#5.3.c5} **Spot the error.** A student says: "Line A has slope -3 and line B has slope 2. Since -3 is less than 2, line A is less steep than line B." What did they get wrong, and which line is actually steeper?

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
*In context (give the slope with its meaning):*
13. A distance(miles)-vs-time(hours) graph passes through (1, 30) and (3, 150). Find the slope and state what it means in words.
14. A candle's height(cm)-vs-time(min) graph passes through (0, 20) and (10, 15). Find the slope and say what it means (mind the sign).

**Answer key:**
1. (8-2)/(3-1)=3 · 2. (1-5)/(2-0)=-2 · 3. (11-3)/(6-2)=2 · 4. (-2-4)/(2-(-1))=-6/3=-2 · 5. (8-0)/(4-0)=2 · 6. (3-1)/(5-1)=1/2 · 7. (5-(-3))/(2-(-2))=8/4=2 · 8. run =3-3=0 → **undefined** (vertical) · 9. (2-2)/(4-(-1))=0 (horizontal) · 10. (5-5)/(6-2)=0 (horizontal) · 11. (0-6)/(4-1)=-6/3=-2 · 12. (-7-(-1))/(3-1)=-6/2=-3 · 13. (150-30)/(3-1)=120/2=**60 miles per hour** — the distance grows 60 miles each hour (a speed of 60 mph) · 14. (15-20)/(10-0)=-5/10=**-1/2 cm per minute** — the candle *shrinks* half a centimeter each minute (negative = decreasing).

---

## Lesson 5.4: Slope-intercept form y = mx + b

**Goal:** Read slope m and y-intercept (0,b) directly from y = mx + b (and the function form f(x) = mx + b), and graph a line fast by plotting b then using rise/run.
**Why it matters:** This is the workhorse form. Once a line is in it, you can graph it in seconds and read its behavior at a glance — no table needed.
**New terms:**
- {#5.4.d1} **Slope-intercept form:** y = mx + b, where m is the slope and b is the **y-intercept** — the y-value where the line crosses the y-axis, at the point (0, b).
- {#5.4.d2} **Function form:** f(x) = mx + b — the same line, named as a function. "b is the starting output at x=0; m is how fast the output climbs."
- {#5.4.d3} **Standard form (recognition):** the same line can also be written Ax + By = C (A, B, C integers) — e.g. 2x + y = 5. It hides the slope and intercept, so to read them you solve for y first. Full treatment, plus graphing from intercepts, is Lesson 5.6.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** "b is your *starting point* on the y-axis; m is your *rate* of climbing from there — your Unit-3 rate again." Tie f(0) = b: feeding 0 to the machine returns the intercept. **In a real context each letter has a concrete meaning:** b is the **starting value** (the output before anything happens, at x = 0) and m is the **rate** (how much the output changes per 1 step of input). For a phone bill c = 5t + 30, the 30 is a \$30 base charge and the 5 is \$5 per GB — read m and b as "rate" and "starting amount," not just numbers.
- **Pictorial:** Graph by hand: plot (0,b), then from there step the slope — for m = 2 = 2/1, go up 2, right 1, mark the next point, connect. Offer the artifact.
- **Symbolic:** Read m and b straight off. Caution: the sign travels with the number — in y = -3x + 5, m = -3 (not 3), b = 5.

**Worked examples:**

1. y = 2x + 1: slope m = 2, y-intercept (0, 1). Graph: plot (0,1), up 2 right 1 to (1,3). Artifact endpoints (-2,-3)→(70,170), (2,5)→(150,10); intercept (0,1)→(110,90).

2. y = -3x + 5: slope m = -3 (down 3 for each right 1), y-intercept (0, 5). The minus sign is part of the slope — the classic trap. This is the flagship negative-slope picture, so graph it: plot the intercept (0,5), then step **down 3, right 1** to (1,2), again to (2,-1). Artifact: (0,5)→(110,10), (1,2)→(130,70), (2,-1)→(150,130). Companion table:

| x | y = -3x + 5 | point |
|----|----|----|
| 0 | 5 | (0,5) intercept |
| 1 | 2 | (1,2) — down 3, right 1 |
| 2 | −1 | (2,-1) — down 3 again |

3. f(x) = (1/2)x - 2: slope m = 1/2, y-intercept (0, -2). As a function: f(0) = -2 (the intercept), f(4) = (1/2)(4) - 2 = 0. Artifact: (0,-2)→(110,150), (4,0)→(190,110). Companion table:

| x | f(x)=(1/2)x-2 | point |
|----|----|----|
| 0 | −2 | (0,-2) intercept |
| 2 | −1 | (2,-1) |
| 4 | 0 | (4,0) x-intercept |

4. **Read the meaning off the equation.** A savings account follows s = 8w + 50, where w is weeks and s is dollars. Identify the slope and intercept and say what each *means*.
   - y-intercept (0, 50): slope-intercept gives b = 50, so at w = 0 there's already **\$50 saved** — the **starting amount**.
   - slope m = 8: \$8 is added each week — the saving **rate**, \$8 per week.
   So s = 8w + 50 reads "start with \$50, add \$8 a week." Evaluate to predict: s(5) = 8(5) + 50 = \$90 after 5 weeks. Naming b as the starting value and m as the rate is the same move you'll use all through Unit 6.

**Watch for:**
- **Dropping the sign of m or b** (calling y=-3x+5's slope "3" or intercept "−5"). `misconceptions.md §3`. Cue: "Read the sign that's *attached* to the number."
- **Swapping m and b** — reading y = 2x + 1 as "slope 1, intercept 2." Anchor: m rides *with the x*; b stands alone.
- **Forgetting the intercept is a *point* (0,b)**, not just a number — matters when they plot.
- **Form not solved for y yet:** if it's 2x + y = 5, they must isolate y first (y = -2x + 5) — callback to Unit 2 solving.

**Visuals to offer:** {#5.4.f1} `visuals.md` **Template 2** — plot the intercept, draw the line through a second computed point, label slope and intercept, table alongside.

**Check for understanding (transfer):**
1. {#5.4.c1} "In y = -4x + 7, what's the slope and where does the line cross the y-axis? Which way does it tilt?"
2. {#5.4.c2} "Write the equation of the line with slope 1/3 and y-intercept (0, -5)."
3. {#5.4.c3} "For f(x) = (1/2)x - 2, what is f(0), and why is that the y-intercept?"
4. {#5.4.c4} "A pool drains by d = -20t + 300 (gallons after t minutes). What do the -20 and the 300 *mean* about the pool? Is it filling or draining, and how fast?"

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
*Interpret in context (state what m and b mean):*
11. A gym membership costs c = 25m + 40 dollars after m months. What does the 40 mean, and what does the 25 mean?
12. A tank holds w = 8h + 5 liters after h hours of filling. State the starting amount and the rate, then find the amount after 6 hours.

**Answer key:**
1. slope 4, y-intercept (0,-7) · 2. slope -1, y-intercept (0,6) · 3. slope 2/3, y-intercept (0,1) · 4. slope 5, y-intercept (0,0) · 5. y = 3x - 4 · 6. y = -2x + 1 · 7. 2(3)+1 = 7 · 8. -3(2)+5 = -1 · 9. (1/2)(4)-2 = 0 · 10. (1/2)(-2)-2 = -3 · 11. the 40 is a \$40 starting/joining fee (cost at 0 months); the 25 is the rate, \$25 per month · 12. starting amount 5 liters (at h = 0), rate 8 liters per hour; after 6 hours w = 8(6) + 5 = 53 liters.

---

## Lesson 5.5: Writing equations of lines

**Goal:** Write a line's equation from a point and a slope, or from two points; recognize and use parallel (equal slopes) and perpendicular (negative-reciprocal slopes) relationships.
**Why it matters:** This is "modeling with lines" — given any two facts that pin a line down, produce its equation. It feeds directly into Unit 6 (modeling) and Unit 7 (systems).
**New terms:**
- {#5.5.d1} **Point-slope form:** y - y₁ = m(x - x₁) — build a line from one point (x₁,y₁) and a slope m. (Then tidy into y = mx + b if desired.)
- {#5.5.d2} **Parallel lines:** never meet; **equal slopes** (m₁ = m₂), different intercepts. (Same slope but a *different* y-intercept → parallel; same slope *and* same y-intercept → they're the **same line** (coincident), not two parallel lines — you'll meet this case again in Unit 7 systems.)
- {#5.5.d3} **Perpendicular lines:** cross at a right angle; slopes are **negative reciprocals** (m₂ = -1/m₁), so their product is -1. (This negative-reciprocal rule is for **nonvertical** lines; separately, any **horizontal** line and any **vertical** line are perpendicular — one has slope 0, the other undefined, so the "product = -1" test doesn't apply to that pair.)

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** "A slope alone gives infinitely many parallel lines; a slope *plus one point it passes through* nails down exactly one." Point-slope is the tool that uses exactly those two facts.
- **Pictorial:** Show two parallel lines (same tilt, shifted) and two perpendicular lines (one tilts up, the other down and 'sideways-flipped'). The negative reciprocal of 2 is -1/2: flip 2 to 1/2, negate.
- **Symbolic:** From two points: first find m (Lesson 5.3), then plug m and *either* point into point-slope, then simplify to slope-intercept. Verify the final line by checking it passes through the given point(s) — substitute (the `SKILL.md` habit). A clean shortcut once m is known: b = y₁ - m x₁.

**Worked examples:**

1. Through (2,3) with slope 4:
$$y - 3 = 4(x - 2) \;\Rightarrow\; y - 3 = 4x - 8 \;\Rightarrow\; y = 4x - 5$$
Check: at x=2, 4(2)-5 = 3 {#5.5.f1}.

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
1. {#5.5.c1} "Write the equation of the line through (1, 5) with slope -2. Then verify it actually passes through that point."
2. {#5.5.c2} "A line is perpendicular to y = (1/3)x + 2. What's its slope, and how did you get it?"
3. {#5.5.c3} "Two lines: y = 5x - 1 and y = 5x + 4. Parallel, perpendicular, or neither? How can you tell without graphing?"

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

## Lesson 5.6: x-intercepts, graphing by intercepts & standard form

**Goal:** Find a line's **x-intercept** by setting y = 0, graph a line from its two intercepts, and work with **standard form Ax + By = C** — convert it to and from slope-intercept form and read both intercepts straight off it.
**Why it matters:** Two points fix a line, and the two intercepts are usually the easiest two to find — so intercepts are the fastest way to graph a line that arrives in standard form (where no slope or intercept is sitting in plain sight). Standard form is also how lines show up in Unit 7 (systems) and Unit 8 (regions), so meeting it now pays off there.
**New terms:**
- {#5.6.d1} **x-intercept:** the point (a, 0) where the line crosses the x-axis. Because every point on the x-axis has y = 0, you find it by setting y = 0 and solving for x. (Mirror of the y-intercept (0, b) from 5.4, where x = 0.)
- {#5.6.d2} **Standard form:** Ax + By = C, with A, B, C integers (and A ≥ 0 by convention). It treats x and y even-handedly — neither is solved for. To read slope and y-intercept, solve for y; to graph fast, use the two intercepts.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** "An intercept is where the line *crosses an axis*. On the x-axis you haven't gone up or down at all, so y = 0 there; on the y-axis you haven't gone across, so x = 0 there. Set the *other* coordinate to 0 and solve for what's left." Tie back to 5.4: they already find the y-intercept by putting x = 0 (that's f(0) = b); the x-intercept is the same move with the roles swapped.
- **Pictorial:** Two intercepts are two points — plot them and draw the line through them. Offer the Template 2 artifact. (Best practice: compute a *third* point as a checkpoint; if it isn't collinear with the two intercepts, recheck the arithmetic before drawing — a wrong graph is worse than none, per `visuals.md`.)
- **Symbolic:** From standard form Ax + By = C, the intercepts come out cleanly: set y = 0 → x-intercept; set x = 0 → y-intercept. To get slope, isolate y (a Unit 2 / Unit 5.4 move): Ax + By = C ⇒ y = -(A/B)x + C/B, so the slope is -A/B and the y-intercept is C/B. Verify conversions with the code tool.

**Worked examples:**

1. Find the x-intercept of y = 2x - 6. Set y = 0:
$$0 = 2x - 6 \;\Rightarrow\; 2x = 6 \;\Rightarrow\; x = 3$$
x-intercept **(3, 0)**. (Its y-intercept, for contrast, is (0, -6): put x = 0.) Notice the two intercepts are found by the *same* move — zero out the other variable.

2. Graph y = -2x + 4 from its two intercepts.
   - x-intercept: set y = 0 → 0 = -2x + 4 → x = 2 → **(2, 0)**.
   - y-intercept: set x = 0 → y = 4 → **(0, 4)** (or just read b = 4).
   Plot those two points and draw the line. Checkpoint third point at x = 1: -2(1)+4 = 2, so (1, 2) — collinear with the two intercepts, good. Artifact (Template 2): (2,0)→(150,110), (0,4)→(110,30), checkpoint (1,2)→(130,70); label the intercepts.

| x | y = -2x + 4 | point |
|----|----|----|
| 0 | 4 | (0,4) y-intercept |
| 1 | 2 | (1,2) checkpoint |
| 2 | 0 | (2,0) x-intercept |

3. Standard form 3x + 4y = 12 — read both intercepts, then convert to slope-intercept.
   - x-intercept (y = 0): 3x = 12 → x = 4 → **(4, 0)**.
   - y-intercept (x = 0): 4y = 12 → y = 3 → **(0, 3)**.
   - Solve for y: 3x + 4y = 12 → 4y = -3x + 12 → $$y = -\tfrac34 x + 3$$ slope -3/4, y-intercept (0, 3) — matching the intercept above. Artifact: (4,0)→(190,110), (0,3)→(110,50).

4. Convert y = (3/4)x - 2 to standard form. Clear the fraction (multiply by 4), then collect x and y on the left:
$$y = \tfrac34 x - 2 \;\Rightarrow\; 4y = 3x - 8 \;\Rightarrow\; 3x - 4y = 8$$
(Standard form wants A ≥ 0, so keep the x-term positive.) Check: at x = 0, -4y = 8 → y = -2, the original intercept. ✓

5. Read intercepts straight off standard form 2x + 5y = 10 (think: \$2 items and \$5 items totaling \$10 — a budget line).
   - x-intercept: 2x = 10 → **(5, 0)** (all \$2 items: five of them).
   - y-intercept: 5y = 10 → **(0, 2)** (all \$5 items: two of them).
   Standard form is tidy for this because each intercept just divides C by one coefficient.

**Watch for:**
- **Confusing which variable to zero out.** For the *x*-intercept set *y* = 0 (not x = 0). Tell: they "find the x-intercept" by setting x = 0 and get the y-intercept instead. Cue: "On the x-axis, how far up are you? So what's y there?"
- **Standard form not converted before reading slope.** From 3x + 4y = 12 a student may call the slope "3" (the coefficient of x as-is). The slope is -A/B = -3/4 only *after* solving for y. Anchor: "Is it solved for y yet? Slope-intercept reading only works once y is alone." (Callback to 5.4's "solve for y first.")
- **Sign of A/B/C when rearranging.** Moving the x-term across flips its sign (Unit 2). Have them substitute an intercept back to confirm, and keep A ≥ 0 so different students land on the *same* standard form.
- **A line through the origin has both intercepts at one point.** y = 2x crosses both axes at (0, 0); the two-intercept method then gives only one point, so pick a second point another way (plug in any x). Tell: they're stuck because "both intercepts are the same."

**Visuals to offer:** {#5.6.f1} `visuals.md` **Template 2** — plot the two intercepts, draw the line, label each intercept, include a companion table (with a third checkpoint row). For standard-form examples, show the converted y = mx + b beside the graph.

**Check for understanding (transfer):**
1. {#5.6.c1} "For 5x + 2y = 20, find both intercepts and say which two points you'd plot to graph it."
2. {#5.6.c2} "A classmate sets x = 0 to find the *x*-intercept. What did they actually find, and what should they have done?"
3. {#5.6.c3} "Put y = (2/3)x - 1 into standard form Ax + By = C with integer coefficients. What are A, B, and C?"

**Practice problems:**
*Find the x-intercept (set y = 0):*
1. y = 2x - 8
2. y = -x + 5
3. y = 3x + 12
4. y = (1/2)x - 4
*Find BOTH intercepts of the standard-form line:*
5. 4x + 3y = 12
6. 2x - 5y = 10
*Convert standard form to slope-intercept (solve for y); give slope and y-intercept:*
7. 2x + y = 7
8. 3x - 4y = 8
*Convert to standard form Ax + By = C (integer coefficients, A ≥ 0):*
9. y = 2x + 3
10. y = (2/3)x - 1
*Graph from intercepts / mixed:*
11. For 5x + 2y = 20, name the two intercept points you'd plot.
12. A line crosses the x-axis at (4, 0) and the y-axis at (0, -2). Find its slope, then its slope-intercept equation.

**Answer key:**
1. 0 = 2x - 8 → x = 4 → **(4, 0)** · 2. 0 = -x + 5 → x = 5 → **(5, 0)** · 3. 0 = 3x + 12 → x = -4 → **(-4, 0)** · 4. 0 = (1/2)x - 4 → x = 8 → **(8, 0)** · 5. x-int (3, 0), y-int (0, 4) · 6. x-int (5, 0), y-int (0, -2) · 7. y = -2x + 7; slope -2, y-intercept (0, 7) · 8. y = (3/4)x - 2; slope 3/4, y-intercept (0, -2) · 9. -2x + y = 3 ⇒ **2x - y = -3** · 10. multiply by 3: 3y = 2x - 3 ⇒ **2x - 3y = 3** · 11. (4, 0) and (0, 10) · 12. slope = (-2 - 0)/(0 - 4) = 1/2; y = (1/2)x - 2.

---

## Wrap-up & interleaving

**Consolidate:** the representations of a line now hang together — a *table* (5.2) gives points, the *graph* (5.1–5.2) shows them, the *slope* (5.3) is the (constant) rate between them, y=mx+b (5.4) reads slope and intercept at a glance, *point-slope* (5.5) builds the equation from scratch, and *standard form* with *intercepts* (5.6) graphs fast when the equation isn't solved for y. Keep saying the line **is a function**: y = mx+b and f(x)=mx+b are one object, and its defining trait is a **constant rate of change**. Where a context is attached, always read m as the *rate* and b as the *starting value*.

**Mix back in:**
- **Unit 3 (rate):** every time slope appears, name it as the unit rate / rate of change — that's the conceptual glue.
- **Unit 4 (functions):** evaluate f(0) to find the intercept; read a line off a table; use the vertical-line-test framing if a "line" is actually vertical (x=3 is not a function).
- **Unit 2 (solving):** to graph 2x + y = 5 (standard form, 5.6) they must solve for y first; point-slope expansion reuses the distributive property (Unit 2.3, `misconceptions.md §7`).
- **Negatives (Unit 1.5 / `misconceptions.md §3`):** the dominant error source here — slope sign, intercept sign, differences in the slope formula. Slip in a negative-laden problem regularly. The new **steepness-vs-direction** slope misconception (`misconceptions.md §8`) lives right here: sign is direction, magnitude is steepness.

**Looking ahead:** Unit 6 turns words into these equations (modeling) — the m-as-rate / b-as-starting-value reading from 5.3–5.4 is exactly that bridge; Unit 7 graphs *two* lines to solve systems (and standard form from 5.6 is the form they often arrive in); Unit 8 shades regions bounded by lines. Solid slope-intercept fluency pays off in all three.

**Progress Card should note:** which lessons are mastered (5.1–5.6), whether slope sign-handling and the zero-vs-undefined distinction are solid, whether the student reads slope/intercept *in context* (rate and starting value) and can find an x-intercept / handle standard form, whether they can move fluidly between table ↔ graph ↔ y=mx+b ↔ standard form, and any lingering negative-sign shakiness to warm up next time.
