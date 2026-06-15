# Unit 6: Modeling & Translation

> This unit is about turning everyday situations into algebra. You'll learn to read a sentence in plain English, write it as an equation, and answer real questions with it. It helps to feel comfortable solving simple equations before you start, but the setup is the new part, and that's what we'll build here.

Up to now you've been handed equations and asked to solve them. This unit is about the step that comes *before* the solving: taking a situation written in plain English and turning it into symbols you can work with.

That turning-into-symbols is a skill of its own, and it's the part this unit teaches. The solving half you can already do. Once a sentence is in symbols, it's an equation like any other, solved the same way you've solved them before.

Before each new lesson, redo two or three problems from a lesson or two back from memory first. It's a small warm-up that pays off more than it looks like it should, and it keeps the solving steps from going rusty while you learn the new setup work.

---

## Lesson 6.1: Translating words into expressions and equations

Solving an equation like 4x − 7 = 9 is a move you can already make. The new skill in this lesson is recognizing when a sentence *is* that equation. You read "7 less than 4 times a number is 9" and you see the algebra hiding inside it. That recognizing-and-rewriting is what we mean by translating, and almost every word problem and real application ahead starts here.

Think of a letter like x as a closed box with a number hidden inside that you don't know yet. When you translate a phrase, the phrase is telling you what to *do* to that box. "Twice a number" means two of the box. "5 more than a number" means the box with 5 added on.

So before you write a single symbol, do the one thing that prevents most setup errors: say what the box is, in words. Write *let x =* and finish the sentence, as in "let x = the number." A box with no English label is where setups go wrong.

Picture it as actions on the box, one at a time. "Twice a number" → two boxes → 2x. "5 more than a number" → the box, then 5 added → x + 5. Say the action out loud, then write it down. The words and the symbols line up.

Now the spot that trips almost everyone: order. Take "3 less than a number." Start with the number, the box. Then take 3 *away from it*. What's left is the box minus 3:

$$x - 3$$

The phrase you read first, the 3, lands second. That feels backwards, so look at why the other reading is a different quantity. If you wrote 3 − x, you'd be saying "3, with the number taken away from it," a different thing entirely.

Here's how to settle it for good: try a number. If the number is 10, then "3 less than 10" is plainly 7. Check both readings against that. The first gives x − 3 = 10 − 3 = 7, which matches, while 3 − x = 3 − 10 = −7, which doesn't. The number test decides it every time, so reach for it whenever an order feels uncertain.

Sentences work the same way, with one extra piece. A verb like *is*, *equals*, *will be*, or *results in* is the equals sign. Everything before it is the left-hand expression; everything after it is the right-hand expression. Translate each side on its own, join them with =, and you've got an equation you can solve with your Unit 2 tools. "7 less than 4 times a number is 9" splits at *is*: the left side is "7 less than 4x," which is 4x − 7, and the right side is 9. That's 4x − 7 = 9.

<!--illus:6-1-phrase-equation-->

One tempting shortcut is a keyword table: "sum" means +, "of" means multiply, "less than" means subtract. Tables like that are fine as a memory aid, but they quietly fail on exactly the comparisons and reversals you just saw. Remember, "3 less than a number" is *not* 3 − x.

So lean on the structure first and keep the words only as a backstop. Read what the sentence is *doing*, not which words it happens to contain.

**New terms:**
- {#6.1.d1} **Translate (in algebra):** rewrite an English phrase or sentence as an equivalent algebraic expression or equation.
- {#6.1.d2} **Expression vs. equation (callback to Unit 1):** an *expression* (x + 5) is a quantity with no equals sign, so there's nothing to solve; an *equation* (x + 5 = 12) asserts two quantities are equal and *can* be solved.

Read each worked example slowly, a line at a time, and ask why each line follows from the one above before you go on. The first one carries the order trap, so it's the one to study hardest.

**Worked examples:**

{#6.1.w1}
*Example 1: phrase to expression (order trap).* "3 less than 4 times a number." Let x = the number, so you have a name for the box before anything else. "4 times a number" is 4x. Then "3 less than 4x" takes 3 *away from* 4x:
$$4x - 3$$
Not 3 − 4x. That would be starting from 3 and taking 4x away, a different quantity. Check with x = 10: "3 less than 40" is 37, and 4(10) − 3 = 37. The number test agrees, so the order is right.

{#6.1.w2}
*Example 2: phrase to expression (two actions).* "A number doubled, then increased by 7." Let x = the number. Do the actions in order: double it first, which is 2x, then increase that by 7:
$$2x + 7$$

{#6.1.w3}
*Example 3: sentence to equation, then solve.* "7 less than 4 times a number is 9." Let x = the number. The word *is* marks the equals sign. The left side, "7 less than 4x," is 4x − 7; the right side is 9. Now it's an ordinary two-step solve:
$$4x - 7 = 9 \;\Rightarrow\; 4x = 16 \;\Rightarrow\; x = 4$$
Check in the original words, not just the symbols: 4 times 4 is 16; 7 less than 16 is 9. That matches the sentence, so x = 4 is right. (If a check like this ever doesn't match, you haven't failed; the check just caught something before it counted. Go back to your first step and re-run the arithmetic slowly. A mismatch is almost always one sign or one small slip, not the whole method.)

{#6.1.w4}
*Example 4: sentence to equation, then solve.* "The sum of a number and 12 is 20." Let x = the number. "The sum of a number and 12" is x + 12, and "is 20" is the equals sign with 20 on the right:
$$x + 12 = 20 \;\Rightarrow\; x = 8$$
Check: 8 + 12 = 20.

{#6.1.w5}
*Example 5: the reversal trap (a relationship, not a number).* "There are 6 students for every professor; s students, p professors. Write the equation." The tempting move is to read left to right and write 6s = p, but read the structure instead. Students are the bigger group, six times as many of them. The cleanest way to see it is to try the smaller quantity as 1: with 1 professor there are 6 students, so s = 6p. Confirm with another: p = 2 gives s = 12, which is twelve students and two professors, a 6-to-1 ratio. (This is the same "test with a number" move from the order trap, used on a relationship.)

Most of the trouble in this lesson comes from order on "less than" and "subtracted from": "3 less than a number" reads so naturally as 3 − x. After you've set one up correctly, the self-check is the number test from Example 1. Substitute a value and watch the wrong order contradict the plain-English meaning.

A second slip worth knowing, now that you've seen Example 5, is the reversal in a relationship like 6s = p. The same fix catches it, plugging in the smaller quantity as 1.

Try one easy translation before the practice set. Take "twice a number, increased by 1." Let x = the number, double it to 2x, then add 1: 2x + 1. Nothing tricky here: name the box, do the actions in order.

**Check for understanding (transfer):**
1. {#6.1.c1} Translate "8 fewer than twice a number," then explain in one sentence why it isn't 8 − 2x. (It's 2x − 8: start with twice the number and take 8 away from *it*; 8 − 2x would start from 8 instead. Number test: at x = 10, "8 fewer than 20" is 12, and 2(10) − 8 = 12.)
2. {#6.1.c2} A sentence translates to x − 5 = 11. Invent an English sentence that would produce it. (One answer: "5 less than a number is 11." Anything that takes 5 away from the number and sets it equal to 11 works.)
3. {#6.1.c3} "A number divided by 3, then increased by 4, is 10." Set up the equation and say which word told you where the equals sign goes. (x/3 + 4 = 10; the word *is* marks the equals sign. Solving gives x = 18.)

The problems below mix the phrase and sentence types on purpose, which is harder than drilling one kind but makes the skill last. Each has its answer at the end of the lesson. If one stalls you, flip back to the worked example it's built on.

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

The four families in this lesson are number, age, distance, and value problems. Together they cover most of the word problems you'll meet in Algebra 1 and well past it. The four labels matter less than the one method that handles all of them, the same setup routine you'll reuse for systems in Unit 7 and for any real model. (One note on scope: percent-concentration mixtures, the "blend 20% and 50% to get 30%" kind, need two variables and wait for Unit 7. Here "value" means coins, tickets, and the like.)

<!--viz:bar_models#3-->

The method is four steps, and you use it every single time:

1. **Define the variable in words.** Write "let x = ____" and finish the sentence. If two things are unknown, write the second *in terms of* the first, using the relationship the problem gives you. This is the step everything else rests on; don't skip it.
2. **Write the equation** from the structure: what totals to what, what equals what.
3. **Solve** with your Unit 2 tools.
4. **Check in the original words,** not just in your equation. Re-read the problem and confirm the numbers fit the story.

That fourth step matters more than it looks. An answer can perfectly satisfy an equation you built *wrong*, and only re-reading the story catches that. The move in step 1, writing the second unknown in terms of the first, is what keeps everything to one variable and one equation, so a single solve does the whole job.

<!--viz:bar_models#0-->

**New terms:**
- {#6.2.d1} **Consecutive integers:** integers in a row, each one more than the last: n, n+1, n+2, … For consecutive **even** or **odd** integers, the gap is 2: n, n+2, n+4, … (This same gap-of-2 form fits both even and odd runs; which one you get depends only on the starting value n. So if solving gives a non-integer n, say n = 74/3, that total simply has *no* such consecutive run, and the fractional answer is the signal.)
- {#6.2.d2} **Distance-rate-time relationship:** d = rt, where distance equals rate (speed) times time. (Slope from Unit 5 *is* a rate; on a distance-vs-time graph the speed is the slope.)

<!--illus:6-2-drt-->

- {#6.2.d3} **Value problem:** total *value* = (value of each item) × (number of items), summed over the kinds of items (e.g. dimes worth $0.10 each).

As you work through the examples below, watch how every one runs the same four steps even as the stories change. That sameness is the thing you're learning to see.

**Worked examples:**

{#6.2.ex1}
*Example 1: number (consecutive integers).* "Three consecutive integers sum to 33. Find them." First name the unknown: let n = the smallest. Since each is one more than the last, the next two are n + 1 and n + 2. That's the second and third written in terms of the first. Now the structure: the three sum to 33.
$$n + (n + 1) + (n + 2) = 33 \;\Rightarrow\; 3n + 3 = 33 \;\Rightarrow\; 3n = 30 \;\Rightarrow\; n = 10$$
So the integers are 10, 11, 12. Check in words: 10 + 11 + 12 = 33. The story holds.

{#6.2.ex2}
*Example 2: number (consecutive even).* "Three consecutive even integers sum to 78." Let n = the smallest even integer. Consecutive even integers step by 2, so the next two are n + 2 and n + 4.
$$n + (n + 2) + (n + 4) = 78 \;\Rightarrow\; 3n + 6 = 78 \;\Rightarrow\; n = 24$$
Integers: 24, 26, 28. Check: 24 + 26 + 28 = 78, and all three are even.

{#6.2.ex3}
*Example 3: age.* "Sam is 3 years older than Pat. Together their ages total 27. How old is each?" Two unknowns, so define one and write the other in terms of it: let p = Pat's age, then Sam's age is p + 3. Keeping it to one variable is what lets a single equation do the work.
$$p + (p + 3) = 27 \;\Rightarrow\; 2p + 3 = 27 \;\Rightarrow\; 2p = 24 \;\Rightarrow\; p = 12$$
Pat is 12, and Sam is 12 + 3 = 15. Check in words: Sam (15) is 3 more than Pat (12), and 12 + 15 = 27. Both parts of the story check out.

{#6.2.ex4}
*Example 4: distance (d = rt).* "A car travels at 60 mph. How long to go 180 miles?" Let t = the time in hours. Use d = rt with the distance d = 180 and the rate r = 60:
$$60t = 180 \;\Rightarrow\; t = 3$$
3 hours. Check: 60 × 3 = 180 miles.

{#6.2.ex5}
*Example 5: distance (two objects).* "Two cars leave the same point in opposite directions, one at 50 mph and one at 70 mph. After how many hours are they 360 miles apart?" Both cars travel for the same time, so one letter covers both: let t = the time in hours. Going opposite ways, the distance between them is the *sum* of the two distances, 50t + 70t.
$$50t + 70t = 360 \;\Rightarrow\; 120t = 360 \;\Rightarrow\; t = 3$$
3 hours. Check: in 3 hours one car goes 150 miles, the other 210; 150 + 210 = 360.

{#6.2.ex6}
*Example 6: value (coins).* "A jar has 15 coins, all dimes and quarters, worth $2.55 total. How many of each?" Let d = the number of dimes. The rest of the 15 coins are quarters, so that's 15 − d, the second unknown written in terms of the first. Each dime is worth $0.10 and each quarter $0.25, so the total value in dollars is:
$$0.10d + 0.25(15 - d) = 2.55$$
$$0.10d + 3.75 - 0.25d = 2.55 \;\Rightarrow\; -0.15d = -1.20 \;\Rightarrow\; d = 8$$
So 8 dimes and 15 − 8 = 7 quarters. Notice everything stayed in dollars from the start; mixing in cents partway is where value problems usually go wrong. Check in words: that's 15 coins, worth 8(0.10) + 7(0.25) = 0.80 + 1.75 = $2.55.

{#6.2.ex7}
*Example 7: value (tickets).* "100 tickets sold: adult $8, child $5, for $680 total. How many adult tickets?" Let a = the number of adult tickets; the rest are child tickets, 100 − a. Value, all in dollars:
$$8a + 5(100 - a) = 680 \;\Rightarrow\; 8a + 500 - 5a = 680 \;\Rightarrow\; 3a = 180 \;\Rightarrow\; a = 60$$
So 60 adult and 40 child. Check: 60(8) + 40(5) = 480 + 200 = $680.

After a few of these, the place that stays tricky is the second unknown. The natural instinct is to reach for a fresh letter, like q for quarters or s for Sam, and then you're stuck with two letters and one equation. The fix is the relationship already in the problem: "3 older than" or "the rest of the 15" tells you how to write the second quantity in terms of the first.

One more to keep an eye on in distance problems: opposite directions add the distances, the same direction subtracts them, and in both cases the two objects share one time t. A quick sketch of two arrows from a point makes which-is-which obvious.

Walk one short problem before the practice set. "Two consecutive integers sum to 11." Let n = the smaller, so the next is n + 1; then n + (n + 1) = 11, which gives 2n + 1 = 11, so n = 5. The integers are 5 and 6, and 5 + 6 = 11. Same four steps, friendly numbers.

**Check for understanding (transfer):**
1. {#6.2.c1} In Example 3, suppose instead the ages total 41. Without redoing all the algebra from scratch, what changes and what is Pat's new age? (Only the total changes: 2p + 3 = 41, so 2p = 38 and p = 19. Pat is now 19, Sam 22.)
2. {#6.2.c2} Why must the *second* unknown be written in terms of the first rather than as a new letter, if we want a single equation? (A new letter gives two unknowns, which needs two equations; writing it in terms of the first keeps one variable, so one equation solves it.)
3. {#6.2.c3} A value problem gives "0.05n + 0.10(20 − n) = ...". In one sentence, what do n, 20 − n, and the coefficients 0.05 and 0.10 each represent? (n is the number of nickels, 20 − n the number of dimes, which is the rest of 20 coins, and 0.05 and 0.10 are the dollar value of one nickel and one dime.)

The families come shuffled below, so each problem asks you to spot its type before you set it up. Answers are at the end of the lesson. When one stalls you, find the worked example from the same family and compare.

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

Real data is messy. Measure ten people's study hours and quiz scores and the points won't sit on a tidy line. But a *trend* usually shows through anyway, and that trend is often all you need to describe what's going on and make a prediction. This lesson is your first look at handling data that way. Keep it light: it's a preview of Unit A (Data & Statistics), where these ideas get the full treatment. Here we just plant them.

The tool for capturing a trend is one you already have. A line of best fit is the linear function from Unit 5, the y = mx + b form, or f(x) = mx + b, laid through a cloud of scattered points so it summarizes them. So there's nothing new to learn here, just the everyday face of the line you already know how to read.

Begin with something concrete. Picture a handful of students, and for each one a pair of numbers: hours studied and quiz score. Say a couple of the pairs out loud, so they feel like real people before they become dots. One student studied 1 hour and scored 55, another studied 6 hours and scored 92.

Now the picture. Put each pair on a coordinate plane as a single point, the way you plotted points back in Lesson 5.1: one dot per student, and no line joining the dots. Here's that cloud of points with a line drawn through the middle of it {#6.3.f1}. The dots drift from lower-left to upper-right, and the straight line follows that drift without touching every dot.

When you look at a cloud like that, the first question is just its direction: does it rise, fall, or drift with no clear tilt? This one rises left to right, so we call the **association positive**: more study hours tend to go with higher scores.

That trend line through the middle is a single line chosen to summarize the whole cloud. It won't pass through every point, and it isn't meant to. It's a model of messy data, not a path that visits each dot. Because it's sketched by eye to run through the middle, a different reasonable person might draw a slightly different one. (A calculator's line-of-best-fit tool finds the single best one by formula; that's a Unit A job. Ours is close enough to work with.)

Once you have the line, predicting is just evaluating the function, the same skill from Units 4 and 5. If a best-fit line comes out as f(x) = 3x + 2, then predicting at x = 10 is f(10) = 3(10) + 2 = 32.

Two words go with prediction, and they're worth meeting once here. Predicting *inside* the range your data actually covers is **interpolation**, and it's the more trustworthy kind. Predicting *outside* that range is **extrapolation**, and it gets riskier the farther out you reach, because you're trusting the trend to hold where you have no points. Both terms come back in Unit A.

The most useful thing a trend line tells you is usually not the prediction but what the slope and intercept *mean*. Don't stop at the numbers. Take f(x) = 3x + 2 for (hours practiced, free throws made). The slope 3 is a rate: about 3 more free throws made for each extra hour of practice, the same "so much for every one" idea as d = rt in the last lesson. The intercept 2 is the predicted makes with zero practice, the value when x = 0. Reading those two numbers in plain words is what lets a line actually tell you something.

The easiest thing to overclaim here is cause. A trend showing two things move together does not prove one *causes* the other. Ice-cream sales and drownings both climb in summer, but ice cream doesn't cause drownings. Hot weather drives both. A trend is real and useful; it just isn't proof of a cause.

**New terms:**
- {#6.3.d1} **Scatter plot:** a graph of paired data (x, y) plotted as individual points, with no connecting line.
- {#6.3.d2} **Association / correlation:** the overall trend in the cloud of points. **Positive:** as x goes up, y tends to go up (cloud rises left to right). **Negative:** as x goes up, y tends to go down. **No association:** no clear up-or-down trend.
- {#6.3.d3} **Line of best fit (trend line):** a single line drawn to pass as close as possible to all the points, summarizing the trend. It *is* a linear function, so you evaluate it to predict.
- {#6.3.d4} **Correlation is not causation:** two quantities trending together does **not** prove one *causes* the other.

The point table for the scatter plot above is (1,55), (2,60), (2,68), (3,70), (4,80), (5,86), (6,92). The cloud rises, so the association is positive. In the examples below, pay special attention to how each one reads the slope and intercept back into the story.

**Worked examples:**

{#6.3.w1}
*Example 1: read the trend.* The scatter plot above (hours studied vs. quiz score) rises from lower-left to upper-right. So the **association is positive**: more study hours tend to go with higher scores. Note "tend to": not every point obeys, which is exactly why it's a trend and not a rule.

{#6.3.w2}
*Example 2: predict, then interpret slope and intercept.* A study finds the best-fit line f(x) = 3x + 2 for (hours practiced, free throws made). Predict the makes for someone who practices x = 10 hours by evaluating the function:
$$f(10) = 3(10) + 2 = 32 \text{ free throws.}$$
The line *is* the model, so predicting is just the evaluation skill from Unit 5. Now read the parts in context: the slope 3 says about 3 more makes per extra hour practiced (a rate), and the intercept 2 is the predicted makes with no practice. One honest flag: if the data only ran up to a few practice hours, x = 10 reaches past it, so this prediction is an extrapolation. Trust it less than one inside the data's range.

{#6.3.w3}
*Example 3: negative association, prediction, and a causation caution.* A best-fit line for (daily screen-time hours x, hours of sleep y) is f(x) = −0.5x + 9. Predict the sleep for someone with x = 6 hours of screen time:
$$f(6) = -0.5(6) + 9 = 6 \text{ hours of sleep.}$$
The slope is negative, so this is a **negative association**: more of x goes with less of y. In context: the slope −0.5 means roughly half an hour less sleep per extra hour of screen time, and the intercept 9 is the predicted sleep with zero screen time. But hold the caution in mind: a downward trend doesn't *prove* screen time causes less sleep. Some other factor could be driving both. Correlation is not causation.

A natural slip here is reading the *direction* of a cloud off the *signs of its numbers*, calling a falling cloud "positive" because the values happen to be positive. After you've named one correctly, the self-check is to ignore the numbers and just watch the cloud: does it rise or fall left to right? That direction, not the sign of the values, is what positive and negative describe.

Two related habits to keep: don't connect the dots into a zig-zag (you want one summarizing line, not a path through each point), and don't expect every point to land on the line (real data scatters; the line is deliberately close-but-not-through-all).

Run one prediction before the practice set. For f(x) = 2x + 1, predict at x = 5: f(5) = 2(5) + 1 = 11. Substitute and compute, the same evaluation you've done since Unit 4.

**Check for understanding (transfer):**
1. {#6.3.c1} Sketch in words what a scatter plot with **no association** looks like, and give a real pair of quantities you'd expect to show it. (A shapeless cloud with no rise or fall, points scattered every which way. One pair: a person's height and their phone number.)
2. {#6.3.c2} A town finds shoe size and reading level are positively associated in children. Does bigger feet cause better reading? Explain in one sentence what's really going on. (No. Older children have both bigger feet and more reading practice, so age drives both; it's correlation, not causation.)
3. {#6.3.c3} A best-fit line is f(x) = 0.5x + 60. Predict y when x = 20, and say whether the association is positive or negative. (f(20) = 0.5(20) + 60 = 70; the slope is positive, so the association is positive.)
4. {#6.3.c4} For the same best-fit line f(x) = 0.5x + 60 modeling (minutes of exercise x, resting heart-rate-recovery score y), explain in context what the **0.5** and the **60** each tell you. (One sentence each.) (The 0.5 is a rate: about half a point more recovery score per extra minute of exercise. The 60 is the predicted recovery score with zero minutes of exercise.)

A mix of conceptual and prediction problems follows. Conceptual ones ask you to name an association or judge a causation claim; the rest hand you a line to evaluate. Answers are at the end of the lesson, and the matching worked example sits just above if you get stuck.

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

You can now turn a phrase or sentence into algebra by naming the variable in words and reading the structure. You can set up and solve the four classic word-problem families with one method and check against the original wording. And you can read a scatter plot: naming its association, predicting from a best-fit line, saying what its slope and intercept mean, telling interpolation from extrapolation, and remembering that a trend isn't proof of a cause.

Those last data ideas are the on-ramp to Unit A, and the setup habits here are what mature into two equations in two variables in Unit 7.
