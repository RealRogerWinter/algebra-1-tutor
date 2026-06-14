# Unit 6: Modeling & Translation

> **Prerequisites:** Unit 2 (solving linear equations — two-step, distributive, variables on both sides) and Unit 5 (linear functions, slope, y = mx + b, the coordinate plane).
> **By the end, the student can:**
> - Translate phrases into algebraic expressions and full sentences into equations, defining the variable in words first.
> - Read the *structure* of a situation rather than chasing keyword tricks.
> - Set up and solve classic word problems (number, age, distance, value & relationship) with a repeatable method, and check the answer against the *original* wording.
> - Plot paired data, name the association (positive / negative / none), use a line of best fit to predict, interpret its slope and intercept in context, distinguish interpolation from extrapolation, and state that correlation is not causation — a first taste of Unit A (Data & Statistics).

## Teaching this unit (orientation for the tutor)

This unit is the hinge of the whole course. Up to now the student has been *solving* equations that were handed to them. The real intellectual work of algebra is the step *before* solving: turning a messy English situation into symbols. Make this explicit early — "you already know how to solve 4x - 7 = 9; the new skill is recognizing when a sentence *is* that equation." Solving is the easy half now; setting up is the hard half, and it deserves most of the time.

The single biggest trap is **keyword tricks** — "'of' means multiply," "'more than' means add," "'is' means equals," "'less than' means subtract in the order you read." These shortcuts feel efficient and are wrong often enough to wreck a student (see `misconceptions.md §7` — over-applied tricks; and §2, the letter-as-object reversal, which keyword reading feeds). The two classic disasters:
- **Order reversal:** "3 less than a number" is x - 3, *not* 3 - x. The phrase you read first lands second.
- **The reversal error:** "6 students for every 1 professor" tempts 6s = p; it's actually p = 6s (see `misconceptions.md §2`).

The antidote is the same every lesson and you should enforce it relentlessly: **define the variable in words first** — literally have the student write or say "let x = the number of dimes" before any symbol gets written. A variable with no English definition is the root of most setup errors. Then read the situation's *structure* (what equals what, what's being combined, what's the total) instead of word-by-word substitution.

Pacing: 6.1 builds the translation reflex on small pieces. 6.2 applies it to multi-sentence problems with a fixed four-step method. 6.3 is a deliberately light first taste of data that connects back to Unit 5 — a best-fit line *is* a linear function (`f(x) = mx + b`) fit to messy points. It's the on-ramp to **Unit A (Data & Statistics)**, which is a **core unit of this course, not an optional appendix** — 6.3 previews its line-of-best-fit lesson (Unit A, Lesson A.2), so keep 6.3 light and let Unit A carry the full data treatment (form, correlation strength, two-way tables). Don't try to teach all of statistics here, but *do* point forward: the ideas you plant in 6.3 (association, predicting from a trend line, correlation ≠ causation) get developed in Unit A. Thread function language throughout 6.3: the prediction line is a function you evaluate. Interleave Unit 2 solving (every setup ends in a solve) and Unit 5 graphing (6.3) so those skills stay warm.

---

## Lesson 6.1: Translating words into expressions and equations

**Goal:** Turn phrases into algebraic expressions and full sentences into equations, by reading structure — not keywords — and defining the variable first.

**Why it matters:** Every word problem, every real application, and every later modeling task (systems in Unit 7, inequalities in Unit 8) begins with this translation. It is the gateway skill; if it's shaky, nothing downstream works.

**New terms:**
- **Translate (in algebra):** rewrite an English phrase or sentence as an equivalent algebraic expression or equation.
- **Expression vs. equation (callback to Unit 1):** an *expression* (x + 5) is a quantity with no equals sign — nothing to solve; an *equation* (x + 5 = 12) asserts two quantities are equal and *can* be solved.

**Teaching arc (concrete → pictorial → symbolic):**
1. **Define the variable first, always.** Before anything: "What is the unknown? Write *let x =* and finish the sentence in words." Make this a non-negotiable ritual. Use the mystery-box metaphor (`metaphors.md`, Variables A): x is a box holding the unknown number; the phrase tells you what to *do* to that box.
2. **Build phrases as actions on the box.** "Twice a number" = two of the box = 2x. "5 more than a number" = the box plus 5 = x + 5. Say the action aloud, then write it.
3. **Confront order directly.** For "3 less than a number," ask: "Start with the number — the box. Now take 3 *away from it*. What's left?" → x - 3. Then show the trap: 3 - x would be "3, with the number taken away from *it*" — a different quantity. Test with a number: if the number is 10, "3 less than 10" is 7, and x - 3 = 7 while 3 - x = -7. The substitution check (`misconceptions.md §7`) settles it every time.
4. **Sentences → equations.** The verb *is / equals / will be / results in* is the =. Everything before it is the left expression, everything after is the right. Translate each side as an expression, join with =, then solve with Unit 2 tools.
5. **Warn off keywords out loud.** "I'm not going to give you a list of 'these words mean these operations' — that backfires. We read what the sentence is *doing*." (`misconceptions.md §7`.) If a student has met a keyword table elsewhere (many textbooks list them — sum → +, "less than" → reverse-order subtraction): acknowledge it rather than contradict it. "Those tables are fine as a memory aid, but they fail on comparisons and reversals (the exact traps below), which is why we read structure first and use the words only as a backstop." This frames our approach as a refinement of the common advice, not a flat rejection of it.

**Worked examples:**

*Example 1 — phrase to expression (order trap).* "3 less than 4 times a number."
Let x = the number. "4 times a number" is 4x. "3 less than 4x" takes 3 *away from* 4x:
$$4x - 3$$
Not 3 - 4x. Check with x = 10: "3 less than 40" is 37, and 4(10) - 3 = 37.

*Example 2 — phrase to expression (two actions).* "A number doubled, then increased by 7."
Let x = the number. Double it: 2x. Increase that by 7:
$$2x + 7$$

*Example 3 — sentence to equation, then solve.* "7 less than 4 times a number is 9."
Let x = the number. Left side: "7 less than 4x" = 4x - 7. The word *is* = 9.
$$4x - 7 = 9 \;\Rightarrow\; 4x = 16 \;\Rightarrow\; x = 4$$
Check in the original words: 4 times 4 is 16; 7 less than 16 is 9.

*Example 4 — sentence to equation, then solve.* "The sum of a number and 12 is 20."
Let x = the number. "The sum of a number and 12" = x + 12; "is 20" = 20.
$$x + 12 = 20 \;\Rightarrow\; x = 8$$
Check: 8 + 12 = 20.

*Example 5 — the reversal trap (relationship, not a number).* "There are 6 students for every professor; s students, p professors. Write the equation."
Don't translate left-to-right into 6s = p. Read the structure: students are the *bigger* group, six times as many. Test with 1 professor: that's 6 students, so s = 6p. (`misconceptions.md §2`.) Confirm: p = 2 gives s = 12 — 12 students, 2 professors, ratio 6-to-1.

**Watch for:**
- **Order reversal** on "less than" / "subtracted from": tell is 3 - x for "3 less than a number." Repair: substitute a number; the wrong order gives a value that contradicts the plain-English meaning (`misconceptions.md §7`).
- **Keyword over-application:** mechanically mapping each word to an operation, e.g. reading "is less than" (a comparison) as subtraction, or auto-multiplying on "of." Repair: re-read for what the sentence *does* (`misconceptions.md §7`).
- **The reversal error** in relationships (6s = p): tell is the equation failing a quick number test. Repair: plug in the smaller quantity = 1 (`misconceptions.md §2`).
- **Skipping the variable definition:** if the student writes symbols before saying what x is, stop and back up — most setup errors trace to here.

**Visuals to offer:** None needed — this lesson is symbolic. The LaTeX area-model boxes from `visuals.md` aren't relevant here.

**Check for understanding (transfer):**
1. Translate "8 fewer than twice a number," then explain in one sentence why it isn't 8 - 2x.
2. A sentence translates to x - 5 = 11. Invent an English sentence that would produce it.
3. "A number divided by 3, then increased by 4, is 10." Set up the equation and say which word told you where the equals sign goes.

**Practice problems:**

*Translate each phrase to an expression (definition: let x = the number):*
1. 5 more than a number.
2. Twice a number.
3. 3 less than a number.
4. A number doubled, then increased by 7.
5. The quotient of a number and 4.
6. 6 less than three times a number.

*Translate each sentence to an equation, then solve:*
7. The sum of a number and 12 is 20.
8. 7 less than 4 times a number is 9.
9. A number doubled and then increased by 7 is 23.
10. 3 less than a number is 10.
11. Three times a number is 21.
12. Half of a number, increased by 5, is 11.
13. 4 less than 5 times a number is 26.
14. Twice the sum of a number and 3 is 16.
15. A number increased by 8 equals three times the number.

**Answer key:**
1. x + 5 · 2. 2x · 3. x - 3 (not 3 - x) · 4. 2x + 7 · 5. x/4 · 6. 3x - 6 (not 6 - 3x)
7. x + 12 = 20 ⇒ x = 8
8. 4x - 7 = 9 ⇒ x = 4
9. 2x + 7 = 23 ⇒ x = 8
10. x - 3 = 10 ⇒ x = 13
11. 3x = 21 ⇒ x = 7
12. x/2 + 5 = 11 ⇒ x = 12
13. 5x - 4 = 26 ⇒ x = 6
14. 2(x + 3) = 16 ⇒ x = 5
15. x + 8 = 3x ⇒ x = 4

---

## Lesson 6.2: Classic word problems (number, age, distance, value & relationship)

**Goal:** Solve number, age, distance, and value/relationship problems with one repeatable method, and check the answer against the original words. (Percent-*concentration* mixtures — "blend 20% and 50% to get 30%" — are a two-variable *systems* topic and are deferred to Unit 7; here "value" means coins/tickets and the like.)

**Why it matters:** These four families cover most of the word problems in Algebra 1 and beyond, and the *method* — not the memorized type — is what transfers to systems (Unit 7) and any real model. A reliable setup routine is the deliverable here.

**New terms:**
- **Consecutive integers:** integers in a row, each one more than the last: n, n+1, n+2, … For consecutive **even** or **odd** integers, the gap is 2: n, n+2, n+4, … (This same gap-of-2 form fits both even and odd runs; which one you get depends only on the starting value n. So if solving gives a non-integer n — say n = 74/3 — that total simply has *no* such consecutive run, and the fractional answer is the signal.)
- **Distance–rate–time relationship:** d = rt — distance equals rate (speed) times time. (Slope from Unit 5 *is* a rate; on a distance-vs-time graph the speed is the slope — `metaphors.md`, Slope B.)
- **Value problem:** total *value* = (value of each item) × (number of items), summed over the kinds of items (e.g. dimes worth $0.10 each).

**Teaching arc — the four-step method (use it every time):**
1. **Define the variable in words.** "Let x = ____." If two quantities are unknown, express the second *in terms of* the first using the relationship in the problem (e.g. "Sam is 3 older than Pat" → Pat = p, Sam = p + 3). This is the heart of the method; don't skip it.
2. **Write the equation** from the structure: what totals to what, what equals what.
3. **Solve** with Unit 2 tools.
4. **Check in the ORIGINAL words** — not just in your equation. Re-read the problem and confirm the numbers fit the story. This catches setup errors a symbolic check can't.

Narrate that defining the *second* unknown in terms of the first is what keeps everything to a single variable (one equation, one unknown) — the same move that later makes substitution natural in Unit 7.

**Worked examples:**

*Example 1 — number (consecutive integers).* "Three consecutive integers sum to 33. Find them."
Let n = the smallest. The next two are n + 1 and n + 2.
$$n + (n + 1) + (n + 2) = 33 \;\Rightarrow\; 3n + 3 = 33 \;\Rightarrow\; 3n = 30 \;\Rightarrow\; n = 10$$
So the integers are 10, 11, 12. Check in words: 10 + 11 + 12 = 33.

*Example 2 — number (consecutive even).* "Three consecutive even integers sum to 78."
Let n = the smallest even integer; the next even integers are n + 2 and n + 4.
$$n + (n + 2) + (n + 4) = 78 \;\Rightarrow\; 3n + 6 = 78 \;\Rightarrow\; n = 24$$
Integers: 24, 26, 28. Check: 24 + 26 + 28 = 78, and all even.

*Example 3 — age.* "Sam is 3 years older than Pat. Together their ages total 27. How old is each?"
Let p = Pat's age. Then Sam's age = p + 3 (second unknown in terms of the first).
$$p + (p + 3) = 27 \;\Rightarrow\; 2p + 3 = 27 \;\Rightarrow\; 2p = 24 \;\Rightarrow\; p = 12$$
Pat is 12, Sam is 12 + 3 = 15. Check in words: Sam (15) is 3 more than Pat (12), and 12 + 15 = 27.

*Example 4 — distance (d = rt).* "A car travels at 60 mph. How long to go 180 miles?"
Let t = the time in hours. Using d = rt with d = 180, r = 60:
$$60t = 180 \;\Rightarrow\; t = 3$$
3 hours. Check: 60 × 3 = 180 miles.

*Example 5 — distance (two objects).* "Two cars leave the same point in opposite directions, one at 50 mph and one at 70 mph. After how many hours are they 360 miles apart?"
Let t = the time in hours. Distance apart = sum of the two distances = 50t + 70t.
$$50t + 70t = 360 \;\Rightarrow\; 120t = 360 \;\Rightarrow\; t = 3$$
3 hours. Check: in 3 hours one goes 150 mi, the other 210 mi; 150 + 210 = 360.

*Example 6 — value (coins).* "A jar has 15 coins, all dimes and quarters, worth $2.55 total. How many of each?"
Let d = the number of dimes. Then the number of quarters = 15 - d (the rest of the 15). Value in dollars:
$$0.10d + 0.25(15 - d) = 2.55$$
$$0.10d + 3.75 - 0.25d = 2.55 \;\Rightarrow\; -0.15d = -1.20 \;\Rightarrow\; d = 8$$
8 dimes, 15 - 8 = 7 quarters. Check in words: 15 coins; value 8(0.10) + 7(0.25) = 0.80 + 1.75 = $2.55.

*Example 7 — value (tickets).* "100 tickets sold: adult $8, child $5, for $680 total. How many adult tickets?"
Let a = the number of adult tickets; child tickets = 100 - a.
$$8a + 5(100 - a) = 680 \;\Rightarrow\; 8a + 500 - 5a = 680 \;\Rightarrow\; 3a = 180 \;\Rightarrow\; a = 60$$
60 adult, 40 child. Check: 60(8) + 40(5) = 480 + 200 = $680.

**Watch for:**
- **Two unknowns, one variable:** students introduce a fresh letter for the second quantity and stall. Repair: re-read for the relationship ("3 older than," "the rest of the 15") and write the second in terms of the first.
- **Mixing units in value problems:** adding cents to dollars, e.g. 10d (cents) plus 0.25q (dollars). Repair: pick one unit for the whole equation and state it.
- **Distance setups:** confusing "same direction (difference of distances)" with "opposite directions (sum)," or forgetting both objects share the same t. Repair: a quick picture and the d = rt table.
- **Checking only the equation, not the story:** an answer can satisfy a *wrongly built* equation. Always re-read the original (`misconceptions.md §1` — = as a real relationship, not just a compute step).

**Visuals to offer:** For distance problems, a simple labeled sketch (two arrows from a point) clarifies sum-vs-difference — a plain ASCII sketch in chat is enough; no `visuals.md` artifact required. The coordinate-plane artifact belongs in 6.3.

**Check for understanding (transfer):**
1. In Example 3, suppose instead the ages total 41. Without redoing all the algebra from scratch, what changes and what is Pat's new age?
2. Why must the *second* unknown be written in terms of the first rather than as a new letter, if we want a single equation?
3. A value problem gives "0.05n + 0.10(20 − n) = ...". In one sentence, what do n, 20 - n, and the coefficients 0.05 and 0.10 each represent?

**Practice problems:**

*Number:*
1. Two consecutive integers sum to 47. Find them.
2. Two consecutive **odd** integers sum to 56. Find them.

*Age:*
3. Maya is 5 years older than her brother. Their ages total 33. How old is each?
4. A mother is 4 times as old as her daughter. The mother is 18 years older than the daughter. How old is each?

*Distance:*
5. A cyclist rides at 45 mph (assume) for some hours and covers 225 miles. How many hours?
6. A train covers 220 miles in 4 hours. What is its speed?

*Value (coins):*
7. A purse holds 20 coins, all nickels and dimes, worth $1.55. How many of each?

*Geometry / relationship:*
8. A rectangle's length is 5 more than its width, and its perimeter is 46. Find the width and length.

**Answer key:**
1. n + (n+1) = 47 ⇒ n = 23: the integers are **23 and 24**. Check 23 + 24 = 47.
2. n + (n+2) = 56 ⇒ n = 27: **27 and 29** (both odd). Check 27 + 29 = 56.
3. Let brother = b, Maya = b + 5: b + (b+5) = 33 ⇒ b = 14. Brother **14**, Maya **19**. Check 14 + 19 = 33.
4. Let daughter = d, mother = 4d; difference 18: 4d - d = 18 ⇒ d = 6. Daughter **6**, mother **24**. Check 24 - 6 = 18 and 24 = 4 × 6.
5. 45t = 225 ⇒ t = 5 hours. Check 45 × 5 = 225.
6. r · 4 = 220 ⇒ r = 55 mph. Check 55 × 4 = 220.
7. Let n = nickels, dimes = 20 - n: 0.05n + 0.10(20 - n) = 1.55 ⇒ n = 9. **9 nickels, 11 dimes**. Check 9(0.05) + 11(0.10) = 0.45 + 1.10 = $1.55.
8. Let w = width, length = w + 5: 2(w + (w+5)) = 46 ⇒ w = 9. Width **9**, length **14**. Check perimeter 2(9 + 14) = 46.

---

## Lesson 6.3: Scatter plots & line of best fit (a first taste of data)

**Goal:** Plot paired data, name the association, use a line of best fit to predict (and read what its slope and intercept *mean* in context), and recognize that correlation is not causation. Keep it light — this is the **first taste** of data that previews **Unit A (Data & Statistics)**, the course's core data unit; Unit A is where these ideas get the full treatment.

**Why it matters:** Real data is messy and rarely sits on a perfect line, yet a *trend* is often clear and useful. A line of best fit is exactly the linear function from Unit 5 — y = mx + b, or f(x) = mx + b — fit to scattered points so we can summarize and predict. This is the everyday face of linear functions. And because it's that same line, its **slope and intercept carry real meaning**: the slope is a *rate* (how much y changes per unit of x — the same rate idea as d = rt in 6.2), and the intercept is the predicted y when x = 0. Reading those in context is what makes a trend line meaningful rather than a black box, and it's exactly what Unit A builds on.

**New terms:**
- **Scatter plot:** a graph of paired data (x, y) plotted as individual points — no connecting line.
- **Association / correlation:** the overall trend in the cloud of points. **Positive:** as x goes up, y tends to go up (cloud rises left to right). **Negative:** as x goes up, y tends to go down. **No association:** no clear up-or-down trend.
- **Line of best fit (trend line):** a single line drawn to pass as close as possible to all the points, summarizing the trend. It *is* a linear function — you evaluate it to predict.
- **Correlation is not causation:** two quantities trending together does **not** prove one *causes* the other.

**Teaching arc (concrete → pictorial → symbolic):**
1. **Start with a story and a table.** E.g. hours studied vs. quiz score for a handful of students. Read two or three rows aloud so the pairs feel concrete.
2. **Plot the points** on a coordinate plane (callback to Unit 5.1) — offer the SVG artifact below (coordinates **computed**, never eyeballed, per `visuals.md`). Each dot is one student; no line connecting dots.
3. **Name the association** by eye: does the cloud rise, fall, or drift? Here it rises → positive.
4. **Lay a line of best fit through the cloud** — "the line that best summarizes the trend." Emphasize it won't hit every point, and that's the *point*: it's a model of messy data. This is Unit 5's y = mx + b again.
5. **Predict by evaluating the function.** Given a best-fit line like f(x) = 3x + 2, predicting at x = 10 is just f(10) = 32 — the same evaluation skill from Unit 4/5. Name the two prediction zones once: predicting *inside* the data's x-range is **interpolation** (more trustworthy); predicting *outside* it is **extrapolation** (riskier the farther out you reach). Both terms come back in Unit A.
6. **Read the slope and intercept in context.** Don't stop at the number — say what the line *means*. For f(x) = 3x + 2 (hours practiced → free throws made): the **slope 3** means about 3 more free throws for each extra hour of practice (a rate, just like 6.2's d = rt); the **intercept 2** is the predicted makes with zero practice. This is the most useful thing a trend line tells you, and Unit A leans on it.
7. **One cautionary sentence on causation:** "Ice-cream sales and drownings both rise in summer — but ice cream doesn't cause drownings; hot weather drives both. A trend is not proof of cause."

**Visuals to offer:** `visuals.md` — coordinate plane with plotted points (SVG artifact). Below is a ready scatter plot with **computed** screen coordinates (hours studied x vs. quiz score y; map sₓ = 40 + 30x, s_y = 170 - 1.4y), including a best-fit line y = 7x + 50 drawn from its computed endpoints (0,50) and (6,92). Always pair it with the table of points in chat. Tell the student this trend line is **an estimate sketched by eye to run through the middle of the cloud** — a different reasonable person might draw a slightly different one, and that's fine. (A calculator's line-of-best-fit tool finds the single optimal one; ours is close. Computing it by formula is a Unit A / technology job, not something to do here.)

```svg
<svg viewBox="0 0 250 200" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="10">
  <!-- axes -->
  <line x1="40" y1="170" x2="235" y2="170" stroke="#888"/>   <!-- x-axis -->
  <line x1="40" y1="10"  x2="40"  y2="170" stroke="#888"/>   <!-- y-axis -->
  <text x="120" y="192" text-anchor="middle" fill="#555">hours studied</text>
  <text x="12" y="90" fill="#555" transform="rotate(-90 12 90)">quiz score</text>
  <!-- best-fit line y = 7x + 50, endpoints (0,50)->(40,100) and (6,92)->(220,41.2) -->
  <line x1="40" y1="100" x2="220" y2="41.2" stroke="#2980b9" stroke-width="2"/>
  <text x="150" y="55" fill="#2980b9">best fit: y = 7x + 50</text>
  <!-- data points (computed) -->
  <circle cx="70"  cy="93"   r="3.5" fill="#c0392b"/>  <!-- (1,55) -->
  <circle cx="100" cy="86"   r="3.5" fill="#c0392b"/>  <!-- (2,60) -->
  <circle cx="100" cy="74.8" r="3.5" fill="#c0392b"/>  <!-- (2,68) -->
  <circle cx="130" cy="72"   r="3.5" fill="#c0392b"/>  <!-- (3,70) -->
  <circle cx="160" cy="58"   r="3.5" fill="#c0392b"/>  <!-- (4,80) -->
  <circle cx="190" cy="49.6" r="3.5" fill="#c0392b"/>  <!-- (5,86) -->
  <circle cx="220" cy="41.2" r="3.5" fill="#c0392b"/>  <!-- (6,92) -->
</svg>
```

Point table to show alongside it: (1,55),(2,60),(2,68),(3,70),(4,80),(5,86),(6,92) — the cloud rises, so the association is **positive**.

**Worked examples:**

*Example 1 — read the trend.* The scatter plot above (hours studied vs. quiz score) rises from lower-left to upper-right. **Association: positive** — more study hours tend to go with higher scores. (Tend to — not every point obeys; that's why it's a trend, not a rule.)

*Example 2 — predict, then interpret slope and intercept.* A study finds the best-fit line f(x) = 3x + 2 for (hours practiced, free throws made). Predict the makes for someone who practices x = 10 hours:
$$f(10) = 3(10) + 2 = 32 \text{ free throws.}$$
This is just evaluating the linear function from Unit 5 — the line *is* the model. Now read the parts in context: the **slope 3** says about 3 more makes per extra hour practiced (a rate); the **intercept 2** is the predicted makes with no practice. And note the x = 10 prediction is likely an **extrapolation** — if the data only ran up to a few practice hours, x = 10 reaches past it, so trust it less than a within-range prediction.

*Example 3 — negative association + prediction + causation caution.* A best-fit line for (daily screen-time hours x, hours of sleep y) is f(x) = -0.5x + 9. Predict the sleep for someone with x = 6 hours of screen time:
$$f(6) = -0.5(6) + 9 = 6 \text{ hours of sleep.}$$
The negative slope means a **negative association** — more of x goes with less of y. In context: the **slope −0.5** says roughly half an hour less sleep per extra hour of screen time; the **intercept 9** is the predicted sleep with zero screen time. But caution: a downward trend doesn't *prove* screen time *causes* less sleep — some other factor could drive both. Correlation is not causation.

**Watch for:**
- **Connecting the dots:** drawing a zig-zag through every point instead of one straight trend line. Repair: "we want *one* line that summarizes all of them, not a path that visits each."
- **Treating the best-fit line as exact:** expecting every data point to lie on it. Repair: "real data scatters; the line is a model, deliberately close-but-not-through-all."
- **Causation overclaim:** "the graph proves x causes y." Repair: the ice-cream/drownings example.
- **Reading association backwards:** calling a falling cloud "positive because the numbers are positive." Repair: association is about *direction of the trend*, not the sign of the values — does the cloud rise or fall left to right?

**Check for understanding (transfer):**
1. Sketch in words what a scatter plot with **no association** looks like, and give a real pair of quantities you'd expect to show it.
2. A town finds shoe size and reading level are positively associated in children. Does bigger feet cause better reading? Explain in one sentence what's really going on.
3. A best-fit line is f(x) = 0.5x + 60. Predict y when x = 20, and say whether the association is positive or negative.
4. For the same best-fit line f(x) = 0.5x + 60 modeling (minutes of exercise x, resting heart-rate-recovery score y), explain in context what the **0.5** and the **60** each tell you. (One sentence each.)

**Practice problems:**

*Conceptual:*
1. For each, name the likely association (positive / negative / none): (a) hours of exercise per week vs. resting heart rate; (b) a car's age vs. its resale price; (c) a person's height vs. their phone number.
2. In your own words, what does a line of best fit *do*, and why won't it pass through every point?
3. True or false, with a one-sentence reason: "If two quantities are strongly correlated, one must cause the other."
4. A scatter plot's cloud falls from upper-left to lower-right. Positive, negative, or no association?

*Predictions (evaluate the given best-fit line):*
5. Best-fit line f(x) = 3x + 2. Predict y at x = 4.
6. Best-fit line f(x) = -2x + 50. Predict y at x = 15.
7. Best-fit line f(x) = 0.5x + 60. Predict y at x = 20.

*Interpret & range (in context):*
8. A best-fit line for (hours worked x, dollars earned y) is f(x) = 12x + 0. In context, what does the **slope 12** mean, and what does the **intercept 0** mean?
9. The line in problems 5 was built from data running from x = 1 to x = 6. Is predicting at x = 4 an **interpolation** or an **extrapolation**, and which kind of prediction is more trustworthy?

**Answer key:**
1. (a) **negative** (more exercise tends to lower resting heart rate); (b) **negative** (older car, lower price); (c) **none** (height and phone number are unrelated).
2. It draws a single straight line that best summarizes the overall trend so you can describe it and predict; it won't hit every point because real data scatters — the line is a model of messy data, not a connect-the-dots path.
3. **False** — correlation shows two things trend together, but a hidden third factor (or coincidence) can cause the trend; correlation is not causation.
4. **Negative association** (the trend falls as x increases).
5. f(4) = 3(4) + 2 = 14.
6. f(15) = -2(15) + 50 = 20.
7. f(20) = 0.5(20) + 60 = 70.
8. **Slope 12:** each extra hour worked adds about \$12 to earnings (a rate, \$12 per hour); **intercept 0:** with 0 hours worked, predicted earnings are \$0.
9. **Interpolation** — x = 4 sits inside the data's range (1 to 6), so it's the more trustworthy kind of prediction; an extrapolation reaches outside the data and is riskier.

---

## Wrap-up & interleaving

**Consolidate:** the order of this unit is the lesson — *define the variable in words → read the structure → write the equation → solve → check in the original words.* Reinforce that translation is its own skill, separate from (and harder than) solving, and that keyword tricks are a trap to read *structure* instead (`misconceptions.md §7`, §2). 6.3 lands the idea that a line of best fit is just a Unit 5 linear function fit to real, messy data — and that a trend never proves a cause.

**Mix back in:** every 6.2 setup ends in a Unit 2 solve (two-step, distributive, variables on both sides) — keep those reps live. 6.3 reuses Unit 5 (plotting points, y = mx + b, evaluating a function) and Unit 4 function notation, and it **feeds Unit A (Data & Statistics)** — the association/best-fit/correlation ideas planted here are picked up and extended there (form, correlation strength, two-way tables). When the student is fluent here, they're ready for Unit 7 (systems), where defining a *second* unknown in terms of the first matures into two equations in two variables.

**Progress Card should note:**
- Does the student **define the variable in words** unprompted? (The key habit of this unit.)
- Can they avoid the **order-reversal** ("3 less than x" = x - 3) and **relationship-reversal** (s = 6p) traps?
- Which word-problem families are solid vs. shaky (number / age / distance / value & relationship)?
- Can they name an association, predict from a best-fit line, **interpret its slope and intercept in context**, tell **interpolation from extrapolation**, and correctly say **correlation ≠ causation**? (These preview Unit A.)
