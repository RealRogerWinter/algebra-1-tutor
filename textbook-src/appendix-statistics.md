# Unit A: Data & Statistics

> **What you need first:** arithmetic and fractions/percents (Unit 3) carry Lessons A.1 and A.3. Lesson A.2 leans on Unit 5 — graphing lines and f(x) = mx + b.
> **By the end of this unit, you'll be able to:**
> - Compute and read the **mean, median, mode, and range** of a small list, spot an **outlier** and what it does, and say when the median is the fairer "center."
> - Read a **scatter plot**, **check whether its shape is roughly a line** before fitting one, describe its association, use a given **line of best fit** to predict, read a correlation by eye, and explain why **correlation isn't causation**.
> - Organize yes/no data in a **two-way table**, find row and column totals, read a count and a **relative frequency**, and compare **conditional rates** across groups to decide whether two things are **associated**.

This is the unit where the algebra you've built starts answering everyday questions about real piles of data — test scores, prices, survey answers. It's three short, mostly separate lessons, and they lean more on judgment than on heavy arithmetic. The biggest idea in the whole unit is one sentence in Lesson A.2: two things moving together doesn't prove one causes the other. If you take only that away, the unit has paid for itself.

A reminder that holds for the whole book: you don't have to finish a lesson in one sitting, and when you come back, redoing two or three problems from an earlier lesson from memory is a good way to warm up.

---

## Lesson A.1: One-variable statistics — center & spread

Picture five friends comparing quiz scores. Two questions come up almost on their own: what's a *typical* score, and were they all close together or all over the place? Those are the two questions you ask of any pile of numbers, and statistics has a small toolkit for each. The first question is about the **center** of the data; the second is about its **spread**. This lesson builds four numbers that answer them, and shows you when one of them tells the truer story than the others.

Here's a way to see all of it at once. Imagine dropping the scores onto a number line, one dot per score. The whole picture of "typical versus spread out" is right there: where the dots pile up is the center, and how far they reach is the spread. The **mean** is the balance point of that line — the spot where the dots would balance if the line were a seesaw. The **median** is the dot with equal counts of dots on either side of it. And whether the dots sit in a tight clump or stretch far apart *is* the spread.

Now the symbols, which are just shorthand for those pictures. The mean is the "fair share": add every value and divide by how many there are, the way you'd split a bill evenly. The median is the middle value once you put the list **in order**. The range is the biggest value minus the smallest — a first, quick measure of how far the data reaches.

That ordering step in the median is small and easy to skip, so make it a habit from the start: line the numbers up smallest to largest *first*, then point to the middle. If there's an even count, there's no single middle dot, so you average the two middle ones.

**New terms:**
- {#A.1.d1} **Mean (average):** add all the values, divide by how many there are. The "fair share" if everyone got the same.
- {#A.1.d2} **Median:** the **middle** value once the data is **put in order**. With an even count, average the two middle ones.
- {#A.1.d3} **Mode:** the value that appears **most often**. A set can have one mode, two or more, or — when nothing repeats — **none**. (That "nothing repeats → no mode" is a labeling convention; some books instead say *every* value is a mode. We'll use "no mode" here.)
- {#A.1.d4} **Range:** max − min — how far the biggest is from the smallest. A first measure of **spread**.
- {#A.1.d5} **Outlier:** a value sitting **far above or below where the rest of the numbers cluster** — an unusually huge or tiny entry compared with its neighbors. Outliers are the reason the mean and median can disagree (see below).
- {#A.1.d6} **Spread (intuition):** are the numbers **clustered** tightly together or **scattered** widely apart? Range is the quick version; **standard deviation** is just *a single number summarizing the typical distance of values from the mean* (a special kind of averaged distance) — bigger means more spread out. (We name it for vocabulary only; no need to compute it here.)

Read each worked example slowly, one line at a time, and ask why each line follows before you go on. The first one finds all four numbers for a small list.

**Worked examples:**

1. Data set {4, 8, 6, 5, 2} (5 values). For the **mean**, add and divide by the count: (4+8+6+5+2)/5 = 25/5 = 5. For the **median**, order it first — 2, 4, 5, 6, 8 — and the middle value is 5. For the **range**, take max − min: 8 − 2 = 6. No value repeats, so there's **no mode**. (Notice the median needed the ordering step; the unordered "middle" would have been 6, which is wrong.)
2. Data set {2, 2, 3, 9} (4 values — an even count). The **mean** is (2+2+3+9)/4 = 16/4 = 4. For the **median**, order it (2, 2, 3, 9) and, because the count is even, average the two middle values: (2+3)/2 = 2.5. The **mode** is 2, the only value that appears twice, and the **range** is 9 − 2 = 7. Look at the gap the **9** opens up: it's an outlier, and it pulls the mean (4) up above the median (2.5). The median describes "typical" better here.
3. Data set {3, 4, 5, 6, 30}. Spotting an outlier and watching what it does. Ordered, it's already 3, 4, 5, 6, **30** — four values clustered near 3 to 6, then one sitting far above the rest, so **30 is the outlier**. The **mean** is (3+4+5+6+30)/5 = 48/5 = 9.6, and the **median** is the middle of the ordered list, **5**. Already the mean (9.6) sits well above the median and above *every* clustered value — that gap is the outlier talking. Now drop the 30 and recompute on 3, 4, 5, 6: the mean falls all the way to (3+4+5+6)/4 = 18/4 = 4.5, while the median only shifts from 5 to (4+5)/2 = 4.5. So removing the outlier moved the mean by 5.1 but the median by only 0.5. The outlier dragged the *mean*; the *median* barely budged. That's exactly why the median is the fairer "typical" when an outlier is in the data.

So the mean and the median can tell different stories, and the reason is always an outlier — a value sitting far from where the rest cluster. One ordinary salary list with a single CEO's pay tacked on is the classic case: the *mean* salary looks high, but the *median* reports the truer "typical" pay. Use the median when the data is **skewed** or has outliers. This doesn't make the mean wrong. If those extreme values genuinely count — a total bill, say — the mean is the right summary. It's "typical" specifically that the median reports better.

Two small habits keep the mode from tripping you. First, "most often" can come up empty: if nothing repeats, there's no mode, and that's a normal answer, not a missed step. Second, a set can have more than one mode if two values tie for most frequent.

Here's a clean case to get the method moving before the practice mixes things up. Find all four for {5, 5, 8}. Mean: (5+5+8)/3 = 18/3 = 6. Median: it's already ordered, and the middle value is 5. Mode: 5, which appears twice. Range: 8 − 5 = 3. Nothing tricky — just the four moves, once each.

**Check for understanding (transfer):**
1. {#A.1.c1} A house on your street sells for $50,000, $60,000, and $55,000, and one mansion sells for $2,000,000. Would you describe the "typical" price with the mean or the median, and why? (The median — about $57,500 — because the $2,000,000 sale is an outlier that drags the mean far above what's typical for the street.)
2. {#A.1.c2} You have five numbers with a mean of 10. If you add a sixth number equal to 10, does the mean change? What if you add a 40 instead? (Adding another 10 keeps the mean at 10 — it's already the fair share. Adding a 40 pulls the mean up, to (50+40)/6 = 15, because 40 sits well above the others.)
3. {#A.1.c3} Two classes both averaged 80 on a test, but one class's scores sat near 80 while the other's ranged from 50 to 100. Which fact is about *center*, and which is about *spread*? (The matching average of 80 is the center; the range from 50 to 100 versus "all near 80" is the spread.)
4. {#A.1.c4} In the set {3, 4, 5, 6, 30}, which value is the outlier, and what does it do to the mean compared with the median? If you removed it, which of the two would change a lot and which would barely move? (30 is the outlier; it pulls the mean up to 9.6 while the median stays at 5. Remove it and the mean drops to 4.5 — a big move — while the median barely shifts, also to 4.5.)

You can now find the mean, median, mode, and range of a small list, and say which measure of center to trust when an outlier shows up.

Mixed practice feels harder than repeating one kind of problem, and that's the point — it's what makes the skill stick to next week. Every problem below has its answer at the end of the lesson, and if one stalls you, flip back to the worked example it's based on. That's what it's there for.

**Practice problems** (for each set, find the mean, median, mode, and range):
1. {3, 7, 7, 9, 4}
2. {10, 12, 14, 12}
3. {1, 2, 2, 2, 8}
4. {5, 5, 6, 8}
5. {15, 25, 25, 35}
6. {6, 6, 6, 6}
7. {2, 4, 4, 6, 9}
8. {2, 5, 5, 8, 10}
9. {1, 1, 2, 4}
10. {3, 3, 7, 8, 9}
11. {2, 4, 5, 6, 8}  *(which mode case is this?)*
12. {3, 3, 7, 7, 30}  *(spot the outlier — what does it do to the mean vs. the median?)*

**Answer key** (mean · median · mode · range):
1. 6 · 7 · 7 · 6
2. 12 · 12 · 12 · 4
3. 3 · 2 · 2 · 7
4. 6 · 5.5 · 5 · 3
5. 25 · 25 · 25 · 20
6. 6 · 6 · 6 · 0
7. 5 · 4 · 4 · 7
8. 6 · 5 · 5 · 8
9. 2 · 1.5 · 1 · 3
10. 6 · 7 · 3 · 6
11. 5 · 5 · **no mode** · 6 — nothing repeats, so there's no mode.
12. 10 · 7 · **3 and 7** (bimodal) · 27 — **30 is the outlier**: it drags the mean up to 10 while the median stays at 7.

---

## Lesson A.2: Two-variable data — line of best fit, correlation vs. causation

So far each data point has been a single number. Now each point pairs two numbers — hours studied *and* the score that went with them, for one student. Plot every such pair as a dot on the coordinate plane and you get a **scatter plot**: a cloud of dots, one per student. Real data never lands on a neat line, but you can usually *see* a trend in the cloud, and you can draw the straight line that threads through it best. That line is the payoff of this lesson, because it's the same f(x) = mx + b from Unit 5 — now earning its keep on messy, real data, where you use it to predict.

Picture that cloud and a line drawn through the middle of it. The line doesn't have to touch a single dot; it captures the *overall* direction the dots lean. While the picture is in front of you, you can read two different things off it by eye.

The first is the **direction** of the lean, which has a name: the **association**. If the dots rise from left to right — more hours, higher scores — that's a **positive** association. If they fall from left to right, that's **negative**. If there's no clear up-or-down lean at all, there's **no association**. Here's a scatter of (hours studied, score) with a best-fit line running through it, climbing to the right {#A.2.f1}; that upward lean is a positive association.

The second thing you can read is how *tightly* the dots hug that line — the **strength** of the correlation. A narrow band of dots pressed close to the line is a **strong** correlation; a loose, fat scatter around it is a **weak** one. Strength and direction are separate questions: a weak positive and a strong positive both lean up; they just differ in how tightly the dots cling. You read both of these by eye here — you don't compute a number for either.

There's one check to do *before* you trust any line, and it's the move people skip. Glance at the cloud and ask: **is this roughly straight?** A line of best fit only makes sense when the dots actually run along a line. If the cloud bends — curving like a U or an arch — or if it's a shapeless blob, then a straight line is the wrong model, and forcing one through would summarize and predict badly no matter how carefully you draw it. This shape question has its own name, the **form**, and it's separate from direction. So the order is always: see the dots, check the form is linear, *then* fit or use a line. (While you're looking, scan for an outlier too — a single dot sitting far off the trend can tilt the whole line.)

Once you've confirmed a line is appropriate and you have f(x) = mx + b, predicting is nothing new. It's just **evaluating the function** from Unit 5.4: plug in an x, read off the predicted y. Same machine, pointed at data.

**New terms:**
- {#A.2.d1} **Scatter plot:** a coordinate-plane graph of **paired data** — each data point is one (x, y) dot (e.g. hours studied vs. test score).
- {#A.2.d2} **Association:** the overall trend in the cloud of dots:
  - **Positive** — as x goes up, y tends to go up (dots rise left-to-right).
  - **Negative** — as x goes up, y tends to go down (dots fall).
  - **No association** — no clear up-or-down trend.
- {#A.2.d3} **Form:** the *shape* of the cloud — does it run roughly along a **straight line** (linear) or does it **curve / bend** (nonlinear)? Form is a separate question from direction, and it's the one that decides whether a *line* is even the right summary.
- {#A.2.d4} **Line of best fit:** a straight line f(x)=mx+b drawn to pass as close as possible to all the dots — **the same linear function from Unit 5**, now fit to data that doesn't sit perfectly on any line. Used to **predict** a y for a new x. (A line is only appropriate when the form is roughly linear — check that first.)
- {#A.2.d5} **Correlation:** a measured tendency for two variables to move together. Read it **qualitatively** here: its **direction** (positive or negative, from which way the cloud leans) and its **strength** — *strong* if the dots hug the line tightly, *weak* if they're loosely scattered around it. **Causation:** one variable actually *makes* the other change. **Correlation and causation are not the same.**

Now the idea this whole unit is built around. Two things can move together for a reason that has nothing to do with one causing the other. In summer, ice cream sales and drowning incidents both climb. They're correlated — they really do rise together. But ice cream doesn't cause drownings. A hidden third cause, hot weather, drives both: heat sends people out for ice cream *and* into the water. Statisticians have a name for that hidden third factor — a **lurking** (or **confounding**) **variable** — but the everyday idea is what matters. Two things moving together never, on its own, proves one causes the other. The question to ask every time is: could some third factor explain both? Could it just be coincidence?

The worked examples below put each of these moves into practice — predicting from a line, naming an association, catching a false cause, checking the form, and reading strength.

**Worked examples:**

1. A line of best fit for some data is y = 2x + 3. Predict y when x = 5. This is just evaluating the function at x = 5, written out:
   $$y = 2(5) + 3 = 10 + 3 = 13.$$
   So we'd predict about 13 — and "about" is the honest word, because a best-fit prediction is an estimate, not a guarantee. (It's the same as finding f(5) for f(x) = 2x + 3, the move from Unit 5.4.)
2. Describing the association. A scatter of (hours studied, test score) shows dots that climb left-to-right — students who studied more generally scored higher — so that's a **positive** association. A scatter of (hours of TV, test score) whose dots drift downward would be a **negative** association. And a scatter of (shoe size, test score) with dots flung every which way, no lean at all, shows **no** association. The single question each time: as x increases, does y tend to go up, go down, or do neither?
3. Correlation versus causation. "Towns with more firefighters at a blaze tend to have more fire damage." Does sending more firefighters *cause* more damage? No — the **lurking variable** is the size of the fire. A bigger fire causes *both* more firefighters being called *and* more damage. The two move together, but neither one causes the other; the third factor drives both.
4. Checking the form before fitting a line. Compare two scatters. In the first, (hours studied, score) dots run in a roughly straight, rising band — the form is **linear**, so a line of best fit is a sensible summary; go ahead and fit it. In the second, (hours of practice, score) dots rise quickly and then *level off*, bending into an arch — the form is **nonlinear**. A straight line is the wrong model here: it would overshoot the part that flattens out and predict badly. A shapeless blob is the same story — no line summarizes it. The move is always: look at the form first, and only fit a line when the cloud is roughly straight.
5. Reading a correlation by eye. Two scatters both lean upward, so both are positive. In the first, the dots sit in a tight, narrow band right along the trend; in the second, they're loosely scattered in a fat cloud around it. Both are positive, but the first shows a **strong** correlation and the second a **weak** one — strength is simply how tightly the dots hug the line. You read this by eye; you don't compute a number for it at this level.

It's easy to read "two things are correlated" as "one causes the other"; the mind reaches for a cause automatically. But correlation only says they move together. Before you believe a cause, ask whether a third factor could be driving both (heat behind the ice cream and the drownings; fire size behind the firefighters and the damage), or whether it's coincidence. If a lurking variable fits, the correlation isn't evidence of cause.

One smaller point, too: real data doesn't sit *on* the line. The dots scatter around it, and the best-fit line is a summary of the crowd, not a promise about any one dot. And a prediction from that line is most trustworthy *near* the data it came from. Reaching far past the data — predicting a score for 20 hours of study when nobody studied more than 6 — stretches the line into territory it never saw, so trust those far-out predictions less.

**Visuals reminder for this lesson:** if it helps, sketch the scatter and run a straight line through the middle of the cloud, then read its lean and how tightly the dots hug it.

**Check for understanding (transfer):**
1. {#A.2.c1} A best-fit line is y = −(1/2)x + 10. Predict y at x = 4, and say whether the association is positive or negative — how can you tell from the equation? (y = −(1/2)(4) + 10 = −2 + 10 = 8. The association is **negative**, because the slope −1/2 is negative: as x rises, y falls.)
2. {#A.2.c2} Sales of sunglasses and the number of people getting sunburned both rise in July. Are they correlated? Does one cause the other? What's really going on? (They're correlated — they rise together — but neither causes the other. The lurking variable is sunny, hot weather, which drives both more sunglasses sales and more time outdoors getting burned.)
3. {#A.2.c3} Two scatter plots: in one the dots rise steadily; in the other they're a shapeless blob. Describe each association. (The rising one is a **positive** association; the shapeless blob shows **no** association.)
4. {#A.2.c4} Before you draw a line of best fit, what should you check about the *shape* of the scatter? Describe a cloud where a straight line would be the wrong summary, and say why. (Check the form — is the cloud roughly straight? A cloud that curves, like an arch that rises then levels off, is the wrong fit for a line: the line would overshoot the flat part and predict badly.)
5. {#A.2.c5} Two scatters both lean upward, but one is a tight narrow band and the other a loose fat cloud. Which shows the *stronger* correlation, and does "stronger" change whether it's positive or negative? (The tight narrow band shows the stronger correlation. "Stronger" is about how tightly the dots hug the line — it doesn't change the direction; both are still positive.)

You can now read a scatter plot, check its form before trusting a line, describe its association and strength by eye, predict from a best-fit line, and keep correlation and causation apart.

Mixed practice feels harder, and that's the point. Every problem has its answer at the end of the lesson, and the worked example it's based on is right above if one stalls you.

**Practice problems:**
*Predict using the given line of best fit. The line in 1–2 was built from data that ran from x = 1 to x = 6:*
1. y = 2x + 3; predict y at x = 5. Is this prediction inside the data range or outside it?
2. y = 2x + 3; predict y at x = 10. Inside or outside the data range — and which of 1 or 2 is the more trustworthy prediction, and why?
3. y = 3x - 1; predict y at x = 4.
4. y = -2x + 10; predict y at x = 3. Then say whether the association is **positive or negative**, and how the equation tells you.
5. y = (1/2)x + 1; predict y at x = 6.
*Conceptual (describe / explain):*
6. A scatter of (hours studied, score) has dots climbing left-to-right. Positive, negative, or no association?
7. A scatter of (hours of TV, score) has dots drifting downward left-to-right. Which association is that?
8. "Children with bigger feet tend to read better." Is bigger feet *causing* better reading? Name a likely third factor (the lurking variable).
9. A scatter's dots rise steeply, then flatten out into an arch — they clearly *curve* rather than run straight. Should you summarize this with a line of best fit? Why or why not?
10. Two scatters both lean upward; in one the dots sit in a tight narrow band, in the other a loose fat cloud. Which has the **stronger** correlation? Are both still **positive**?

**Answer key:**
1. 2(5)+3 = **13**. **Inside** the data range (x = 5 is within 1–6) — an interpolation.
2. 2(10)+3 = **23**. **Outside** the range (x = 10 is past 6) — an extrapolation. **Problem 1 is more trustworthy**: a best-fit line predicts best near the data it came from; x = 10 reaches well beyond it.
3. 3(4)-1 = **11**.
4. -2(3)+10 = **4**. **Negative** association — the slope is **negative** (-2), so as x rises, y falls.
5. 1/2(6)+1 = **4**.
6. **Positive** association (as x rises, y rises).
7. **Negative** association (as x rises, y falls).
8. **No** — correlation, not causation. The hidden third factor (lurking variable) is **age**: older children have bigger feet *and* read better.
9. **No** — the form is **nonlinear** (it curves), so a straight line is the wrong model; it would fit and predict poorly. Check the form is roughly straight *before* fitting a line.
10. The **tight narrow band** shows the **stronger** correlation. **Yes, both are still positive** — strength (tight vs. loose) is a separate question from direction (up vs. down).

---

## Lesson A.3: Two-way tables

Some data isn't a number at all — it's a label. "Owns a pet?" is yes or no; "lives in an apartment or a house?" is one or the other. Data sorted into groups like this is **categorical**, and when you've got two such labels for each person, a **two-way table** is the clean way to see how they interact. Picture a survey of 50 people, each answering both questions. Every person falls into one of four buckets — pet-and-apartment, pet-and-house, no-pet-and-apartment, no-pet-and-house — and a two-way table is just a grid with one bucket per inner cell.

Lay it out as a grid with the totals written along the edges, and a useful check comes for free: the row totals and the column totals both have to add up to the same grand total. If they don't, a cell got misread.

Reading the table is two moves. A **count** you read straight off a cell — how many people are in that bucket. A **relative frequency** turns a count into a fraction or percent of some total. The one thing to get right is *which* total you divide by, because that changes with the question. "What share of everyone owns a pet?" divides by the grand total. "Of the apartment dwellers, what share owns a pet?" divides by the apartment column's total — a rate *within one group*. Same cell sometimes, different denominator, different question.

That second kind — a rate within one group — is a **conditional relative frequency**, and it's the one that answers the real question a two-way table is for: *does one category go with the other?* You answer it by comparing the conditional rate across groups. If apartment dwellers own pets at a clearly different rate than house dwellers do, then where you live and owning a pet are **associated**. If the two rates come out about equal, there's little or no association. That's the same idea as the positive/negative association from the scatter plots in A.2, now told with counts instead of dots.

**New terms:**
- {#A.3.d1} **Categorical data:** data sorted into **groups/labels** (yes/no, apartment/house), not measured numbers.
- {#A.3.d2} **Two-way table:** a grid with one category across the **rows** and another across the **columns**; each inner cell holds a **count**.
- {#A.3.d3} **Row total / column total (marginals):** the sum across a row or down a column. The corner **grand total** is everyone.
- {#A.3.d4} **Relative frequency:** a count expressed as a **fraction or percent of a total** — count/total. Which total you divide by depends on the question:
  - **Joint relative frequency** — a single cell over the **grand total** (e.g. "owns a pet *and* lives in an apartment, out of everyone").
  - **Conditional relative frequency** — a cell over its **row or column total**, i.e. a rate *within one group* (e.g. "of the apartment dwellers, the share who own a pet"). These are the ones you compare to detect association.
- {#A.3.d5} **Association (for two categories):** two categorical variables are **associated** when a **conditional relative frequency differs across groups** — e.g. if the pet-ownership rate among apartment dwellers is clearly different from the rate among house dwellers, then *where you live* and *owning a pet* are associated. If those rates are about equal, there's little or no association. (This is the categorical-data echo of A.2's positive/negative association for scatter plots.)

Here's the survey laid out, with 50 people sorted by whether they own a pet (rows) and whether they live in an apartment (columns):

$$\begin{array}{c|c|c|c}
 & \text{Apartment} & \text{House} & \textbf{Total} \\ \hline
\text{Pet: Yes} & 6 & 24 & \mathbf{30} \\ \hline
\text{Pet: No} & 14 & 6 & \mathbf{20} \\ \hline
\textbf{Total} & \mathbf{20} & \mathbf{30} & \mathbf{50}
\end{array}$$

Read the single worked example below slowly — it walks every move on this one table, from totals to the association question.

**Worked example:** Working the pet/apartment table above. The **row totals** add across: Pet-Yes is 6+24 = 30, and Pet-No is 14+6 = 20. The **column totals** add down: Apartment is 6+14 = 20, and House is 24+6 = 30. The **grand total** is 30+20 = 50, and the columns check it: 20+30 = 50 as well. To **read a count**, go straight to a cell — the people who own a pet *and* live in an apartment number 6, the top-left cell. For a **joint relative frequency** (a share of everyone), the fraction who own a pet is 30/50 = 3/5 = 60%. For a **conditional relative frequency** (a rate within one group), of the 20 apartment dwellers, the fraction who own a pet is 6/20 = 3/10 = 30%. Notice that the total you divide by changed with the question — the grand total 50 for "of everyone," the column total 20 for "of the apartment dwellers."

Now the question the table is really for: does owning a pet go with where you live? Compare the two conditional rates. Among apartment dwellers, the pet rate is 6/20 = 3/10 = **30%**. Among house dwellers, it's 24/30 = 4/5 = **80%**. Those are very different — 30% against 80% — so owning a pet and where you live **are associated**: house dwellers are far more likely to own a pet. (Each group also sits well off the overall 60%, which is another sign they differ.) If both groups had instead landed near 60%, the rates would be about equal and we'd say there's little or no association. Comparing the rates across rows or columns like this is exactly how a two-way table reveals association — the categorical cousin of A.2's positive/negative association.

The most common slip here is the denominator: when the question says "of the apartment dwellers," divide by that group's total, not the grand total. The phrase "out of *which* group?" points you to the right denominator every time. Reading "and" is its own question: "owns a pet *and* lives in an apartment" is a single cell over the grand total — a joint rate — while "of apartment dwellers, owns a pet" is that cell over the column total — a conditional rate. Different denominators, different questions.

And one note on the association itself: a single conditional rate tells you nothing on its own. "30% of apartment dwellers own pets" isn't high or low until you have the other group to compare it to. Association is about whether the rate *differs* between groups, so always compute *both* rates and put them side by side. (Turning these fractions into percents is the Unit 3 move: 3/5 = 0.6 = 60%.)

**Check for understanding (transfer):**
1. {#A.3.c1} Using the table, what fraction of **house** dwellers own a pet? Which total did you divide by, and why? (24/30 = 4/5 = 80%. Divide by the House column total, 30, because the question asks "of the house dwellers" — that group is the denominator.)
2. {#A.3.c2} If you were told the four inner counts but no totals, how would you find the grand total two different ways — and what does it mean if they disagree? (Add the row totals, or add the column totals; both should give the same grand total. If they disagree, a cell was misread or miscounted.)
3. {#A.3.c3} What's the difference between "owns a pet *and* lives in a house" (a joint relative frequency) and "of house dwellers, the share who own a pet" (a conditional one)? (The joint rate divides that cell by the grand total — a share of everyone. The conditional rate divides it by the House column total — a share within just the house dwellers. Same cell, different denominator.)
4. {#A.3.c4} The apartment dwellers own pets 30% of the time and the house dwellers 80% of the time. From comparing those two rates, are *owning a pet* and *where you live* associated? How would the rates look if they were **not** associated? (Yes — 30% versus 80% is a big difference, so they're associated. If they weren't, the two rates would be about equal.)

You can now build and read a two-way table, turn its counts into joint and conditional rates with the right denominator, and compare conditional rates across groups to decide whether two categories are associated.

Mixed practice feels harder, and that's the point. Every problem has its answer at the end of the lesson, and the worked example above is the one to flip back to if a step stalls you.

**Practice problems** — use this table of 50 students, *plays a sport* (rows) × *wears glasses* (columns):

$$\begin{array}{c|c|c|c}
 & \text{Glasses} & \text{No Glasses} & \textbf{Total} \\ \hline
\text{Sport: Yes} & 14 & 6 & ? \\ \hline
\text{Sport: No} & 6 & 24 & ? \\ \hline
\textbf{Total} & ? & ? & ?
\end{array}$$

1. Find the row total for **Sport: Yes**.
2. Find the column total for **Glasses**.
3. Find the **grand total**.
4. How many students **play a sport and wear glasses**?
5. What percent of **all** students wear glasses?
6. Of the students who **wear glasses**, what percent **play a sport**? (a conditional relative frequency)
7. Of the students who **don't wear glasses**, what percent **play a sport**? Compare this with your answer to #6 — are **playing a sport** and **wearing glasses** associated? Explain.

**Answer key:**
1. 14+6=20
2. 14+6=20
3. 50 — add the row totals (20+30) or the column totals (20+30); both give 50.
4. 14 (top-left cell)
5. 20/50=2/5=40%
6. 14/20=7/10=70%
7. 6/30=1/5=20%. The two conditional rates are **far apart — 70% (glasses) vs. 20% (no glasses)** — so **yes, playing a sport and wearing glasses are associated** here (sport-players are much more likely to wear glasses). If the two rates had been about equal, there'd be little or no association.

---

You've now got a small statistics toolkit. For one variable, you can find the center and spread of a list and spot an outlier pulling on the mean (A.1). For two number variables, you can read a scatter plot, check its form before fitting a line, use a best-fit line to predict, read a correlation by eye, and keep correlation apart from causation (A.2). For categorical data, you can build a two-way table, turn counts into relative frequencies, and compare conditional rates to detect association (A.3). The thread tying it to the rest of the course is A.2's punchline: a line of best fit is just f(x) = mx + b from Unit 5, fit to messy data and used to predict — once you've checked a line is the right shape for the cloud. And "association" turned up twice, as the lean of a scatter and as conditional rates differing across groups.
