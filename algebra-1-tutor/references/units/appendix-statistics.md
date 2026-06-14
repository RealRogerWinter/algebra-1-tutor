# Appendix A: Data & Statistics

> **⚠️ OPTIONAL — OFF THE MAIN PATH.** This appendix is **enrichment, not a gate.** Nothing later in the course depends on it, and a student can finish Algebra 1 without it. **Offer it, don't impose it:** mention it as a "want to see where lines show up in real data?" detour, ideally after Unit 5, and only if the student is curious or has time. Never block progress on it. Keep the tone light and accessible — this is the friendly, applied corner of the course.

> **Prerequisites:** Unit 5 (graphing lines, \(f(x)=mx+b\)) for Lesson A.2. Lessons A.1 and A.3 need only arithmetic and fractions/percents (Unit 3).
> **By the end, the student can:**
> - Compute and interpret **mean, median, mode, and range** for a small data set, and say when the median is the fairer "center."
> - Read a **scatter plot**, describe its association, use a given **line of best fit** to predict, and explain why **correlation ≠ causation**.
> - Organize categorical data in a **two-way table**, find row/column totals, and read a count and a simple **relative frequency** (fraction or percent).

## Teaching this appendix (orientation for the tutor)

This is the "where does algebra show up in real life" appendix, so lead with relevance and keep it concrete. Three short, mostly independent lessons: A.1 (one-variable center & spread) and A.3 (two-way tables) are pure arithmetic-and-fractions and can be offered any time after Unit 3; A.2 (line of best fit) is the payoff — it reuses Unit 5's \(f(x)=mx+b\) on *messy* real data, so offer it after Unit 5.

Because it's optional and applied, **don't drill**. A couple of worked examples and a handful of practice problems per lesson is plenty; let the student stop whenever the curiosity is satisfied. The biggest conceptual win here is **correlation vs. causation** in A.2 — that's the one idea worth making sure lands, because it's a lifelong critical-thinking tool.

Keep the standard habits from `SKILL.md` (verify arithmetic, never yes/no checks). The main misconception traps are light: forgetting to **order the data before taking the median**, treating "the average" as always the fair center, and reading "two things move together" as "one causes the other." Lean on everyday framings rather than formulas — define standard deviation only in words, don't compute it.

---

## Lesson A.1: One-variable statistics — center & spread

**Goal:** Given a small list of numbers, compute the **mean, median, mode,** and **range**, and judge when the median describes the "typical" value better than the mean.
**Why it matters:** "What's typical?" and "how spread out is it?" are the two questions you ask of *any* pile of numbers — test scores, prices, wait times. These four numbers are the everyday toolkit.
**New terms:**
- **Mean (average):** add all the values, divide by how many there are. The "fair share" if everyone got the same.
- **Median:** the **middle** value once the data is **put in order**. With an even count, average the two middle ones.
- **Mode:** the value that appears **most often** (there can be none, or more than one).
- **Range:** \(\text{max} - \text{min}\) — how far the biggest is from the smallest. A first measure of **spread**.
- **Spread (intuition):** are the numbers **clustered** tightly together or **scattered** widely apart? Range is the quick version; **standard deviation** is just *a single number summarizing the typical distance of values from the mean* — bigger means more spread out. (We name it for vocabulary only; no need to compute it here.)

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** "Five friends' quiz scores — what's a typical score, and were they all close or all over the place?" *Typical* = center (mean/median/mode); *all over the place* = spread (range).
- **Pictorial:** Drop the values on a number line. The mean is the **balance point**; the median is the one with **equal counts on each side**; clustering vs. scattering is visible at a glance.
- **Symbolic:** mean \(=\dfrac{\text{sum}}{\text{count}}\); median = middle of the **ordered** list; range \(=\max-\min\).

**When the median beats the mean:** one **outlier** (an unusually huge or tiny value) drags the mean toward itself but barely moves the median. Classic case: a few ordinary salaries plus one CEO's — the *mean* salary looks high, the *median* tells the truer "typical" story. Use the median when the data is **skewed** or has outliers.

**Worked examples:**

1. Data set \(\{4, 8, 6, 5, 2\}\) (5 values).
   - **Mean:** \(\dfrac{4+8+6+5+2}{5} = \dfrac{25}{5} = 5\).
   - **Median:** order it → \(2, 4, 5, 6, 8\); the middle value is \(5\).
   - **Range:** \(8 - 2 = 6\).
   - (No value repeats, so there's **no mode**.)

2. Data set \(\{2, 2, 3, 9\}\) (4 values — even count).
   - **Mean:** \(\dfrac{2+2+3+9}{4} = \dfrac{16}{4} = 4\).
   - **Median:** ordered \(2, 2, 3, 9\); average the two middle values: \(\dfrac{2+3}{2} = 2.5\).
   - **Mode:** \(2\) (appears twice).
   - **Range:** \(9 - 2 = 7\).
   - Note the **9** is an outlier: it pulls the mean (4) above the median (2.5). The median better describes "typical" here.

**Watch for:**
- **Taking the median without ordering first** — the single most common slip. Tell: their "middle" value isn't actually in the center once sorted. Cue: "Line them up smallest to largest *first*, then point to the middle."
- **Even-count median** — forgetting to average the **two** middle values.
- **Mode confusion** — assuming every set has exactly one mode (it can have none, or several). "Most frequent — and sometimes nothing repeats."
- **Calling the mean 'the' answer for typical** when an outlier is present — that's the median's job.

**Visuals to offer:** none needed (a number line sketched in ASCII per `visuals.md` can show the balance/middle idea if it helps; keep it light).

**Check for understanding (transfer):**
1. "A house on your street sells for \\$50{,}000, \\$60{,}000, \\$55{,}000, and one mansion for \\$2{,}000{,}000. Would you describe 'typical' with the mean or the median, and why?"
2. "I have five numbers with mean 10. If I add a sixth number equal to 10, does the mean change? What if I add a 40?"
3. "Two classes both averaged 80 on a test, but one class's scores were all near 80 and the other's ranged from 50 to 100. Which fact is about *center* and which is about *spread*?"

**Practice problems** (for each set, find the mean, median, mode, and range):
1. \(\{3, 7, 7, 9, 4\}\)
2. \(\{10, 12, 14, 12\}\)
3. \(\{1, 2, 2, 2, 8\}\)
4. \(\{5, 5, 6, 8\}\)
5. \(\{15, 25, 25, 35\}\)
6. \(\{6, 6, 6, 6\}\)
7. \(\{2, 4, 4, 6, 9\}\)
8. \(\{2, 5, 5, 8, 10\}\)
9. \(\{1, 1, 2, 4\}\)
10. \(\{3, 3, 7, 8, 9\}\)

**Answer key** (mean · median · mode · range):
1. \(6\) · \(7\) · \(7\) · \(6\)
2. \(12\) · \(12\) · \(12\) · \(4\)
3. \(3\) · \(2\) · \(2\) · \(7\)
4. \(6\) · \(5.5\) · \(5\) · \(3\)
5. \(25\) · \(25\) · \(25\) · \(20\)
6. \(6\) · \(6\) · \(6\) · \(0\)
7. \(5\) · \(4\) · \(4\) · \(7\)
8. \(6\) · \(5\) · \(5\) · \(8\)
9. \(2\) · \(1.5\) · \(1\) · \(3\)
10. \(6\) · \(7\) · \(3\) · \(6\)

---

## Lesson A.2: Two-variable data — line of best fit, correlation vs. causation

**Goal:** Read a **scatter plot** of paired data, describe its **association**, use a given **line of best fit** to make a prediction, and explain why **correlation does not prove causation**.
**Why it matters:** This is where Unit 5's lines earn their keep on **real, messy data**: a line of best fit lets you summarize a cloud of points and predict beyond it. And spotting correlation-vs-causation is one of the most useful thinking skills algebra gives you.
**New terms:**
- **Scatter plot:** a coordinate-plane graph of **paired data** — each data point is one \((x, y)\) dot (e.g. hours studied vs. test score).
- **Association:** the overall trend in the cloud of dots:
  - **Positive** — as \(x\) goes up, \(y\) tends to go up (dots rise left-to-right).
  - **Negative** — as \(x\) goes up, \(y\) tends to go down (dots fall).
  - **No association** — no clear up-or-down trend.
- **Line of best fit:** a straight line \(f(x)=mx+b\) drawn to pass as close as possible to all the dots — **the same linear function from Unit 5**, now fit to data that doesn't sit perfectly on any line. Used to **predict** a \(y\) for a new \(x\).
- **Correlation:** a measured tendency for two variables to move together. **Causation:** one variable actually *makes* the other change. **They are not the same.**

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** "Plot every (hours studied, score) pair as a dot. They won't land on one neat line — real data is messy. But you can *see* a trend, and draw the line that best threads through the cloud."
- **Pictorial:** Show a small scatter and a line running through the middle of it (`visuals.md` **Template 2** mapping — coordinate plane with **computed** plotted points, then the best-fit line on top; always pair it with the table of points). The line need not hit any single dot; it captures the *overall* direction.
- **Symbolic — callback to Unit 5:** Once you have the line \(f(x)=mx+b\), prediction is just **evaluating the function** (Unit 5.4): plug in an \(x\), read off the predicted \(y\). Same machine, applied data.

**Correlation ≠ causation (make this land):** In summer, **ice cream sales** and **drowning incidents** both rise — they're *correlated*. But ice cream doesn't cause drownings; a hidden third cause, **hot weather**, drives both (more ice cream *and* more swimming). So "two things move together" never by itself proves "one causes the other." Always ask: *could a third factor explain both? could it be coincidence?*

**Worked examples:**

1. A line of best fit for some data is \(y = 2x + 3\). **Predict** \(y\) when \(x = 5\):
   $$y = 2(5) + 3 = 10 + 3 = 13.$$
   (Same as evaluating \(f(5)\) for \(f(x)=2x+3\) — Unit 5.4.) So we'd predict about **13**. Stress "about": a best-fit prediction is an estimate, not a guarantee.

2. **Describe the association.** A scatter of (hours studied, test score) shows dots that climb left-to-right — students who studied more generally scored higher. That's a **positive association**. A scatter of (hours of TV, test score) whose dots drift downward would be a **negative association**. A scatter of (shoe size, test score) with dots scattered every which way shows **no association**.

3. **Correlation vs. causation.** "Towns with more firefighters at a blaze tend to have more fire damage." Does sending firefighters cause damage? No — **bigger fires** (the third factor) cause *both* more firefighters being called *and* more damage. Correlation, not causation.

**Watch for:**
- **"Correlation proves causation"** — the headline trap. Tell: the student leaps from "they move together" to "X causes Y." Repair with the ice-cream/drowning or firefighter example and the "is there a third cause?" question.
- **Expecting points to sit exactly on the line** — real data is scattered; the best-fit line is a summary, not a perfect fit.
- **Reversing the association** (calling a downward trend "positive"). Cue: "As \(x\) increases, does \(y\) go up or down?"
- **Over-trusting predictions far outside the data** — a best-fit line predicts best *near* the data it came from.

**Visuals to offer:** `visuals.md` **Template 2** (coordinate plane + line). **Compute the plotted points** and the two line endpoints (don't eyeball), emit as an **SVG artifact**, label the axes and the line equation, and always include the companion **table of points** in chat. A scatter is just the plane with several small `<circle>` dots plus the best-fit line drawn through them.

**Check for understanding (transfer):**
1. "A best-fit line is \(y = -\tfrac12 x + 10\). Predict \(y\) at \(x = 4\), and say whether the association is positive or negative — how can you tell from the equation?"
2. "Sales of sunglasses and the number of people getting sunburned both rise in July. Are they correlated? Does one cause the other? What's really going on?"
3. "Two scatter plots: in one the dots rise steadily; in the other they're a shapeless blob. Describe each association in words."

**Practice problems:**
*Predict using the given line of best fit:*
1. \(y = 2x + 3\); predict \(y\) at \(x = 5\).
2. \(y = 2x + 3\); predict \(y\) at \(x = 10\).
3. \(y = 3x - 1\); predict \(y\) at \(x = 4\).
4. \(y = -2x + 10\); predict \(y\) at \(x = 3\).
5. \(y = \tfrac12 x + 1\); predict \(y\) at \(x = 6\).
*Conceptual (describe / explain):*
6. A scatter of (hours studied, score) has dots climbing left-to-right. Positive, negative, or no association?
7. A scatter of (hours of TV, score) has dots drifting downward left-to-right. Which association is that?
8. "Children with bigger feet tend to read better." Is bigger feet *causing* better reading? Name a likely third factor.

**Answer key:**
1. \(2(5)+3 = 13\)
2. \(2(10)+3 = 23\)
3. \(3(4)-1 = 11\)
4. \(-2(3)+10 = 4\)
5. \(\tfrac12(6)+1 = 4\)
6. **Positive** association (as \(x\) rises, \(y\) rises).
7. **Negative** association (as \(x\) rises, \(y\) falls).
8. **No** — correlation, not causation. The hidden third factor is **age**: older children have bigger feet *and* read better.

---

## Lesson A.3: Two-way tables

**Goal:** Organize **categorical** data (yes/no, type A/type B) in a two-way table, compute **row and column totals**, and read off a **count** and a simple **relative frequency** (a fraction or percent of a total).
**Why it matters:** Survey and yes/no data ("owns a pet? lives in an apartment?") is everywhere, and a two-way table is the clean way to see how two categories interact and to turn raw counts into percentages.
**New terms:**
- **Categorical data:** data sorted into **groups/labels** (yes/no, apartment/house), not measured numbers.
- **Two-way table:** a grid with one category across the **rows** and another across the **columns**; each inner cell holds a **count**.
- **Row total / column total (marginals):** the sum across a row or down a column. The corner **grand total** is everyone.
- **Relative frequency:** a count expressed as a **fraction or percent of a total** — \(\dfrac{\text{count}}{\text{total}}\). Which total (grand, row, or column) depends on the question.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** "We surveyed 50 people: does each own a pet, and do they live in an apartment? Sort them into four buckets." Each bucket is a cell.
- **Pictorial:** Lay it out as a grid with a totals row and column. Seeing the marginals add up to the grand total is a built-in check.
- **Symbolic:** A count is read straight from a cell. A relative frequency is \(\dfrac{\text{cell (or total)}}{\text{chosen total}}\), then converted to a percent.

**Worked example:** 50 people surveyed — *owns a pet* (rows) × *lives in an apartment* (columns):

$$\begin{array}{c|c|c|c}
 & \text{Apartment} & \text{House} & \textbf{Total} \\ \hline
\text{Pet: Yes} & 12 & 18 & \mathbf{30} \\ \hline
\text{Pet: No} & 8 & 12 & \mathbf{20} \\ \hline
\textbf{Total} & \mathbf{20} & \mathbf{30} & \mathbf{50}
\end{array}$$

- **Row totals:** Pet-Yes \(=12+18=30\); Pet-No \(=8+12=20\).
- **Column totals:** Apartment \(=12+8=20\); House \(=18+12=30\).
- **Grand total:** \(30+20=50\) (check: \(20+30=50\)).
- **Read a count:** people who own a pet **and** live in an apartment \(=\mathbf{12}\) (top-left cell).
- **Relative frequency (of everyone):** fraction who own a pet \(=\dfrac{30}{50}=\dfrac{3}{5}=\mathbf{60\%}\).
- **Relative frequency (within a column):** of the 20 apartment dwellers, the fraction owning a pet \(=\dfrac{12}{20}=\dfrac{3}{5}=\mathbf{60\%}\). (Note how the *total you divide by* changes with the question.)

**Watch for:**
- **Wrong denominator** — dividing by the grand total when the question asks "of the apartment dwellers…" (use the **column** total there). Cue: "Out of *which* group? That group's total is your denominator."
- **Totals that don't reconcile** — row totals and column totals must both sum to the same grand total; if not, a cell was misread.
- **Confusing 'and' with a conditional** — "owns a pet **and** in an apartment" (a single cell over the grand total) vs. "of apartment dwellers, owns a pet" (cell over the column total).
- **Fraction → percent** slips — reuse Unit 3 (\(\tfrac{3}{5}=0.6=60\%\)).

**Visuals to offer:** none needed — the LaTeX `array` table above renders cleanly in chat (per `visuals.md`, area-model/table boxes use LaTeX, not an artifact).

**Check for understanding (transfer):**
1. "Using the table, what fraction of **house** dwellers own a pet? Which total did you divide by, and why?"
2. "If I told you the four inner counts but no totals, how would you find the grand total two different ways — and what does it mean if they disagree?"
3. "What's the difference between 'owns a pet *and* lives in a house' and 'of house dwellers, the share who own a pet'?"

**Practice problems** — use this table of 50 students, *plays a sport* (rows) × *wears glasses* (columns):

$$\begin{array}{c|c|c|c}
 & \text{Glasses} & \text{No Glasses} & \textbf{Total} \\ \hline
\text{Sport: Yes} & 9 & 21 & ? \\ \hline
\text{Sport: No} & 6 & 14 & ? \\ \hline
\textbf{Total} & ? & ? & ?
\end{array}$$

1. Find the row total for **Sport: Yes**.
2. Find the column total for **Glasses**.
3. Find the **grand total**.
4. How many students **play a sport and wear glasses**?
5. What percent of **all** students wear glasses?
6. Of the students who **wear glasses**, what percent **play a sport**?

**Answer key:**
1. \(9+21=30\)
2. \(9+6=15\)
3. \(30+20=50\) (or \(15+35=50\)) \(=50\)
4. \(9\) (top-left cell)
5. \(\dfrac{15}{50}=\dfrac{3}{10}=30\%\)
6. \(\dfrac{9}{15}=\dfrac{3}{5}=60\%\)

---

## Wrap-up & interleaving

**Consolidate:** the student now has a small statistics toolkit — **center & spread** for one variable (A.1), **scatter plots + best-fit lines + correlation/causation** for two (A.2), and **two-way tables + relative frequency** for categorical data (A.3). The unifying algebra idea is A.2's punchline: **a line of best fit is just \(f(x)=mx+b\) from Unit 5, fit to messy data and used to predict.**

**Mix back in:**
- **Unit 3 (fractions, percents, rates):** relative frequencies in A.3 and the "average rate" feel of slope in A.2 are Unit 3 skills reused.
- **Unit 5 (lines & \(f(x)\)):** A.2 is a direct application — predicting is *evaluating the function*; describing positive/negative association is *reading the sign of the slope*.

**Because this is optional:** don't push a student to "finish" it. Treat any of the three lessons as a self-contained, satisfying detour. If they enjoyed A.2, that's a great sign their Unit 5 function-sense is solid.

**Progress Card should note:** that this enrichment was **offered** and which lessons (if any) the student explored — but **never** mark the appendix as a requirement or a gap. The one idea worth recording as "learned" if it came up: **correlation ≠ causation.**
