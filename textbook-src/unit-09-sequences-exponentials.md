# Unit 9: Sequences & Exponential Functions

> This unit is about patterns that grow in a steady way: number lists that climb by a fixed step, and the kind of growth behind money earning interest or a population doubling. It pays off because that second kind, growing by multiplying, shows up everywhere once you can spot it.
>
> It helps to have one thing fresh: working out the value of an expression when you put a number into it. If you'd like a quick warm-up, redo a couple of problems on that from an earlier unit.

This is a shorter unit, and it rests on one idea you can hold in a single sentence. Some patterns grow by **adding the same amount each step**. Others grow by **multiplying by the same amount each step**. That one difference, add the same versus multiply the same, separates the two families you'll meet here, and it's the thing to keep in mind on every page.

You'll start with sequences, which are just ordered lists of numbers, because they make that contrast something you can count on your fingers. Then you'll meet exponential functions, which are the smooth, grown-up version of the multiplying pattern, and the kind of thing that describes money earning interest or a population doubling.

Before each new sitting, redo two or three problems from a lesson or two back from memory first. It's a small warm-up, and it does more for you than re-reading.

---

## Lesson 9.1: Arithmetic & geometric sequences as functions

A sequence is just an ordered list of numbers, like 3, 7, 11, 15, and so on. Nothing exotic. You make lists like this whenever you count by fives or read off a row of dates. What turns it into algebra is one question: what are you *doing* to get from each number to the next?

Here's a way to picture it that connects back to Unit 4. There, a function was a machine: you feed in a number, and out comes exactly one number. A sequence is that same machine, fed the counting numbers in order.

Feed in 1, out comes the 1st number on the list. Feed in 2, out comes the 2nd. The position in the list is the input; the number sitting there is the output. So a sequence really *is* a function. Its inputs just happen to be 1, 2, 3, and so on. We write the 1st term as a_1, the 2nd as a_2, and the term in position n as a_n.

What we're really after is the rule the machine is using. Look at 3, 7, 11, 15. What do you do to get from each term to the next? You add 4, every time. Now look at 2, 6, 18, 54. What's happening here? Each term is the one before times 3. Those are the two behaviors this lesson is built on, and they get names. **Add the same number each step** is an *arithmetic* sequence. **Multiply by the same number each step** is a *geometric* sequence.

Notice that you just said the rule out loud. "Each term is the one before, plus 4" is a complete recipe for building the list, as long as you also know where to start. That little phrase is what we'll call the *recursive* rule in a moment, and you understood it before any symbols showed up. The only catch is that it needs a starting number, or it has nowhere to begin.

When you're not sure which kind of sequence you're looking at, there's one small tool that settles it every time. Write the terms in a row, and underneath, write the jumps between them. Do this two ways: write the *differences* (what you'd add) and the *ratios* (what you'd multiply by). Whichever one stays the same tells you the type.

| term n | 1 | 2 | 3 | 4 |
|----|----|----|----|----|
| 3,7,11,15 (arith) | 3 | 7 | 11 | 15 |
| difference |  | +4 | +4 | +4 |
| 2,6,18,54 (geo) | 2 | 6 | 18 | 54 |
| ratio |  | x3 | x3 | x3 |

For the first list the differences are all +4, while the ratios aren't constant, so it's arithmetic. For the second the ratios are all ×3, so it's geometric. When a sequence has you guessing, compute both rows and look for the one that holds steady. That table is the whole classification tool.

There are two ways to write any of these sequences in symbols. They describe the same list; they just answer different questions.

The first is the *step-by-step* way, the one you already spoke aloud. It says how to get each term from the one right before it. For an arithmetic sequence with common difference d, that's a_n = a_{n−1} + d, and you have to state the first term a_1 separately so it has somewhere to start. For a geometric sequence with common ratio r, it's a_n = r·a_{n−1}, again with a_1 given. This is called the **recursive** rule, and it mirrors exactly what you do by hand: take the last number, do the one move, write the next number.

The second way skips the walk. Suppose you want the 100th term and you don't fancy listing 99 numbers first. The *jump-ahead* rule, called the **explicit** rule, takes you straight there from the term number alone. Here's where it comes from. To reach term n, you start at a_1 and take steps. But term 1 takes *zero* steps, because you're already there. Term 2 is one step out, term 3 is two steps out, so term n is n−1 steps out. That's the whole reason an n−1 shows up:

$$\text{arithmetic:}\quad a_n = a_{n-1} + d,\ a_1\text{ given}\qquad\Longleftrightarrow\qquad a_n = a_1 + (n-1)\,d$$
$$\text{geometric:}\quad a_n = r\cdot a_{n-1},\ a_1\text{ given}\qquad\Longleftrightarrow\qquad a_n = a_1\cdot r^{\,n-1}$$

Moving between the two forms is easier than it looks, because they share their parts. The d (or r) in the step-by-step rule is the *same* d (or r) in the jump-ahead rule, and a_1 is the same in both. So once you've read off the first term and the common difference or ratio, you can write either form.

One more thing, and it's the precise reason a sequence isn't quite the same as the line or curve it resembles. The inputs to a sequence are only the counting numbers: 1, 2, 3, and so on. There's no "term 1.5." You can't ask the machine for a number it has no button for.

So if you plot the terms of 3, 7, 11, 15 as points (1, 3), (2, 7), (3, 11), (4, 15), you get a row of **separate dots**, not a connected line. The dots happen to sit exactly on the line y = 4n − 1, but the sequence is only the dots. This is what we mean by a **discrete domain**: the inputs come in separate, countable steps with nothing in between.

The line that runs through the dots is a continuous parent that fills in the gaps; the sequence itself doesn't. An arithmetic sequence is a linear function looked at only on the counting numbers. A geometric sequence is an exponential function looked at only on those same whole-number inputs.

**New terms:**
- {#9.1.d1} **Sequence:** an ordered list of numbers, called **terms**. The 1st term is a_1, the 2nd is a_2, and the nth is a_n.
- {#9.1.d2} **Term number n:** the position in the list: 1, 2, 3, ... This is the **input**; the term a_n is the **output**. So a sequence *is a function* whose domain is the counting numbers.
- {#9.1.d3} **Discrete domain:** because the inputs are only the counting numbers 1, 2, 3, … (you can't ask for "term 1.5"), the sequence's graph is a set of **separate dots**, not a connected curve. This is what distinguishes a sequence from the linear/exponential function it resembles (whose domain is *all* real numbers).
- {#9.1.d4} **Arithmetic sequence:** each term is the previous one **plus a fixed number**, the **common difference d**. (Constant *difference*.)
- {#9.1.d5} **Geometric sequence:** each term is the previous one **times a fixed number**, the **common ratio r** (with r ≠ 0 and a_1 ≠ 0: since we're multiplying, a 0 anywhere would kill the pattern). (Constant *ratio*.)
- {#9.1.d6} **Recursive vs. explicit rule:** a **recursive** rule says how to get each term *from the one before* (you must already know the previous term): arithmetic a_n = a_{n-1} + d, geometric a_n = r·a_{n-1}, with the **first term a_1 stated separately**. An **explicit** rule *jumps straight to term n* from the term number alone: arithmetic a_n = a_1 + (n-1)d, geometric a_n = a_1 · r^(n-1). They describe the *same* sequence. The recursive one is the "step-by-step" view, the explicit one is the "skip ahead" view, and you should be able to translate between them.

Read each worked example slowly, a line at a time, and ask why each line follows from the one above before you go on. The first two show the explicit rule doing its job; the last two show how the diagnostic table decides the type.

**Worked examples:**

1. **Arithmetic** 3, 7, 11, 15, ...: consecutive differences 7-3=4, 11-7=4, 15-11=4 are all 4, so d=4, a_1=3. Find a_10:
$$a_{10} = 3 + (10-1)\cdot 4 = 3 + 9\cdot 4 = 3 + 36 = 39$$
The (10−1) is the nine steps from the first term out to the tenth. To be sure, you could list all ten and land on 39 the slow way; the formula just spares you the listing.

2. **Geometric** 2, 6, 18, 54, ...: consecutive ratios 6/2=3, 18/6=3, 54/18=3 are all 3, so r=3, a_1=2. Find a_5:
$$a_5 = 2\cdot 3^{\,5-1} = 2\cdot 3^{4} = 2\cdot 81 = 162$$
The exponent is 5−1=4 because reaching the 5th term means multiplying by 3 four times. Check by walking it: 2 → 6 → 18 → 54 → 162. Same answer.

3. **Which type?** 5, 8, 11, 14, ...: differences are all +3 and the ratios (8/5, 11/8, ...) are *not* constant → **arithmetic**, d=3. Next term: 14+3 = 17.

4. **Which type?** 4, 12, 36, 108, ...: ratios are all ×3 (differences 8, 24, 72 are not constant) → **geometric**, r=3. Next term: 108·3 = 324.

5. **A descending arithmetic sequence** 10, 7, 4, 1, ...: d = -3. Find a_8:
$$a_8 = 10 + (8-1)(-3) = 10 + 7(-3) = 10 - 21 = -11$$
The sequence is going *down*, so d is negative. Keep the minus attached to the 3 all the way through, and the answer lands below zero, which is exactly right for a list that's still dropping.

6. **Arithmetic, both forms (recursive ↔ explicit).** 4, 9, 14, 19, ...: differences are all +5, so a_1=4, d=5. **Recursive:** a_1 = 4, a_n = a_{n-1} + 5. **Explicit:** a_n = 4 + (n-1)·5. Find a_6 **both ways** and confirm they match.
$$\text{recursive: } 4 \to 9 \to 14 \to 19 \to 24 \to 29 \quad(\text{step +5 five times, } a_6=29)$$
$$\text{explicit: } a_6 = 4 + (6-1)\cdot 5 = 4 + 5\cdot 5 = 4 + 25 = 29 \checkmark$$
Same answer, 29. The recursive form walks term by term; the explicit form skips straight to it.

7. **Geometric, both forms (recursive ↔ explicit).** 3, 6, 12, 24, ...: ratios are all ×2, so a_1=3, r=2. **Recursive:** a_1 = 3, a_n = 2·a_{n-1}. **Explicit:** a_n = 3·2^(n-1). Find a_5 **both ways**:
$$\text{recursive: } 3 \to 6 \to 12 \to 24 \to 48 \quad(\times 2 \text{ four times, } a_5=48)$$
$$\text{explicit: } a_5 = 3\cdot 2^{\,5-1} = 3\cdot 2^{4} = 3\cdot 16 = 48 \checkmark$$
The translation is just reading off the shared a_1 and r: r=2 is both the recursive multiplier and the explicit base.

Notice the same two moves under every example: find what's constant (a difference or a ratio), then read off a_1 and that constant. With those in hand, either form is yours to write.

Once a list keeps climbing, it's tempting to call it arithmetic just because the numbers are getting bigger. But 2, 6, 18, 54 climbs by *multiplying*, not by adding. The differences are 4, 12, 36, which aren't equal, while the ratios are a steady ×3.

The fix is the diagnostic table: when in doubt, compute *both* the jumps and the ×-factors between terms, and see which one stays the same. "Going up" doesn't decide it; "going up by the same amount" versus "going up by the same multiple" does.

A second slip hides in the n−1. You'd expect the 10th term to use a 10 somewhere, so it's natural to write a_10 = 3 + 10·4. But term 1 takes zero steps, so the 10th term is only nine steps out from the first, and the rule gives 3 + 9·4. If an answer comes out exactly one d too big (or one extra factor of r), this is almost always why. Say it to yourself: a_1 is the *first* term, already sitting there for free.

One more, quieter than the others. A recursive rule on its own, say a_n = a_{n−1} − 2, can't actually produce a single number, because nothing tells it where to start. It's a complete machine missing its first input. So a recursive rule always needs its first term named alongside it; without a_1, there's nothing to step away from.

Try one clean example first, while the practice is still all one type. Take the arithmetic sequence 2, 5, 8, 11. The difference is +3, the first term is 2, so the next term is just 11 + 3 = 14. No formula needed: only the one move, once. If you want, write its explicit rule too: a_n = 2 + (n−1)·3.

**Check for understanding (transfer):**
1. {#9.1.c1} "Is 1, 5, 25, 125, ... arithmetic or geometric, and how can you *prove* it from the numbers, not just by feel?"
2. {#9.1.c2} "An arithmetic sequence starts at 6 with d = 4. Without listing all of them, what's the 20th term, and why is it 6 + 19·4 and not 6 + 20·4?"
3. {#9.1.c3} "Two sequences both start 2, ... One is arithmetic with d=2, the other geometric with r=2. Write the first four terms of each. Where do they split apart?"
4. {#9.1.c4} "An arithmetic sequence is given recursively as a_1 = 9, a_n = a_{n-1} − 2. Write its **explicit** rule, and explain how you read d and a_1 straight off the recursive form."

These have short reachable answers. For the first, compute both the differences (4, 20, 100, not constant) and the ratios (5, 5, 5, constant), so it's geometric with r = 5; that's what "prove it from the numbers" means.

For the second, the 20th term is 19 steps from the first, so a_20 = 6 + 19·4 = 82, and using 20 would count one step too many.

For the third, the arithmetic one is 2, 4, 6, 8 and the geometric one is 2, 4, 8, 16. They agree through the first two terms and split at the third, where adding 2 gives 6 but doubling gives 8.

For the fourth, the recursive form shows a_1 = 9 and the step is −2, so d = −2, giving the explicit rule a_n = 9 + (n−1)(−2).

Mixed practice feels harder than repeating one kind of problem, and that's the point. It's what makes a skill last to next week. Every problem below has its answer at the end of the lesson, and if one stalls you, flip back to the worked example it's based on. That's what it's there for. Watch the first group especially: consecutive problems switch between arithmetic and geometric on purpose, so you have to decide the type before you do anything else.

**Practice problems:**
*Find the common difference d or ratio r, and state the type:*
1. 5, 8, 11, 14, ...
2. 3, 6, 12, 24, ...
3. 10, 7, 4, 1, ...
4. 1, 5, 25, 125, ...
*Continue the sequence (give the next two terms):*
5. 2, 9, 16, 23, ...
6. 4, 12, 36, ...
7. 100, 90, 80, ...
*Find the requested term using the rule:*
8. Arithmetic 5, 8, 11, 14, ...: find a_10.
9. Geometric 2, 6, 18, 54, ...: find a_5.
10. Geometric 3, 6, 12, 24, ...: find a_7.
11. Arithmetic 10, 7, 4, 1, ...: find a_8.
12. Geometric 2, 4, 8, 16, ...: find a_10.
*Write the recursive rule, then find the term explicitly:*
13. Arithmetic 6, 11, 16, 21, ...: write the recursive rule (with a_1), then find a_8 with the explicit rule.
14. Geometric 2, 10, 50, 250, ...: write the recursive rule (with a_1), then find a_5 with the explicit rule.
*Given the recursive rule, find the requested term:*
15. Arithmetic given by a_1 = 20, a_n = a_{n-1} − 4: find a_6.
16. Geometric given by a_1 = 1, a_n = 3·a_{n-1}: find a_5.

**Answer key:**
1. d = 3, **arithmetic** · 2. r = 2, **geometric** · 3. d = -3, **arithmetic** · 4. r = 5, **geometric** · 5. d=7 → next two: 30, 37 · 6. r=3 → next two: 108, 324 · 7. d=-10 → next two: 70, 60 · 8. a_10 = 5 + (10-1)·3 = 32 · 9. a_5 = 2·3⁴ = 162 · 10. a_7 = 3·2⁶ = 192 · 11. a_8 = 10 + 7(-3) = -11 · 12. a_10 = 2·2⁹ = 1024 · 13. recursive a_1 = 6, a_n = a_{n-1} + 5; explicit a_8 = 6 + (8-1)·5 = 41 · 14. recursive a_1 = 2, a_n = 5·a_{n-1}; explicit a_5 = 2·5⁴ = 1250 · 15. a_6 = 20 + (6-1)(-4) = 0 · 16. a_5 = 1·3⁴ = 81.

---

## Lesson 9.2: Exponential growth & decay; linear vs. exponential

The last lesson's geometric sequence, the kind where you multiply by the same number each step, was a row of separate dots. This lesson fills in the gaps between them and lets the input be any number, not just 1, 2, 3. That smooth version is an **exponential function**, and it's how you describe money earning interest, a population breeding, or a phone losing value year after year.

Start with the contrast, in money. A linear pattern is repeated *adding*: you put $5 under the mattress every week, the same five dollars each time. An exponential pattern is repeated *multiplying*: your money grows by the same *percent* each step, so the actual dollar amount you add gets bigger and bigger, because a percent of a larger pile is more dollars.

Two quick stories to hold onto. Five bacteria become 10, then 20, then 40: doubling, so you multiply by 2 each step. And an $80 phone that loses half its value a year goes 80, 40, 20, 10, multiplying by 0.5 each step. One climbs, one falls, but both *multiply*.

Before the function itself, here's the one move that most often goes wrong: turning a percent change into a number you multiply by. If something grows 10%, you don't multiply by 0.10. Think about what "+10%" actually means. You keep the whole 100% you already have *and* add another 10% on top. That's 110% of what you started with, which is ×1.10.

The same logic runs the other way: "−20%" means you lose a fifth and *keep* the other 80%, so it's ×0.80, not 0.20 and not 1.20. The factor is always "how much of the previous amount you've got afterward." A useful way to see it: +10% is p + 0.10p = 1.10p, the original plus a tenth of it.

An exponential function is written y = a·bˣ. The a is the amount you start with, and the b is what you multiply by each step. The thing that makes it *exponential* rather than linear is where the x sits: up in the exponent. In a linear function the variable is multiplied; here it's the power, so each step multiplies the whole running total again.

There's a fence around which a and b are allowed, and each part of the fence earns its place. The starting amount a can't be 0, because 0·bˣ is just 0 forever: no growth, nothing to model.

The base b has to be greater than 0, because a negative base stops being a real number at some inputs (with b = −4, asking for x = ½ means √(−4), which isn't a real number). And b can't be 1, because 1 to any power is 1, so y would just sit at a and never move. So the well-behaved exponential lives where a ≠ 0, b > 0, and b ≠ 1.

The reason b is worth interpreting and not just plugging in is that it reads off the percent change directly. Since b is the fraction of the previous amount you keep, b = 1.05 means you keep 100% and add 5%, that's +5% per period. b = 1.20 is +20%. b = 0.90 means you keep only 90%, so it's −10% per period. b = 0.5 halves, a −50% drop. The percent change lives in the digits past the 1: above 1 is growth, below 1 is a loss of whatever 1 − b comes to.

And a, the starting amount, is the value before anything has happened: the deposit before interest, the population in year 0, the price when new (you get it by setting x = 0, since b⁰ = 1 makes y = a).

The clearest way to feel the difference between the two families is to set them side by side and watch them row by row.

| x | linear y=2x | exponential y=2^x |
|----|----|----|
| 0 | 0 | 1 |
| 1 | 2 | 2 |
| 2 | 4 | 4 |
| 3 | 6 | 8 |
| 4 | 8 | 16 |
| 5 | 10 | 32 |
| 6 | 12 | 64 |

Read down the columns. The line adds 2 every row, a constant difference. The exponential *doubles* every row, a constant ratio. They're equal in two places, at x = 1 and again at x = 2 (the rows where both read 2, and both read 4). Between those two points the curve actually dips a hair below the line. At x = 1.5 the line is at 3 but 2^1.5 is about 2.83. You can't see that in a whole-number table, but it's real if you graph it.

Then from x = 3 onward the exponential pulls ahead and never looks back: 8 beats 6, and the gap only widens after that. That's the headline about growth: an *increasing* exponential (b > 1) eventually overtakes *any* straight line, no matter how steep the line is. A *decaying* exponential (0 < b < 1) does the reverse: it sinks toward 0 and overtakes nothing that's rising.

To classify a table on your own, use the exact tool from the last lesson, now with family names attached. Check whether consecutive outputs share a constant *difference* (that's linear) or a constant *ratio* (that's exponential). Same diagnostic, new vocabulary.

**New terms:**
- {#9.2.d1} **Exponential function (well-defined):**
  > **f(x) = a·bˣ**, where **a ≠ 0** is the starting amount and **b** is the growth/decay factor, a number with **b > 0 and b ≠ 1**.
  >
  > Each restriction earns its place: **a ≠ 0** (if a = 0 then a·bˣ = 0 for every x, so it collapses to the constant 0, not a growth model); **b > 0** (if b ≤ 0 then bˣ isn't a real number for some inputs, e.g. with b = −4 the input x = ½ asks for √(−4), which is not a real number); **b ≠ 1** (if b = 1 then bˣ = 1 always, so f(x) = a, the constant a, with nothing growing or decaying).
  
  The variable is in the **exponent**. That's what makes it exponential, not linear.
- {#9.2.d2} **Starting amount a:** the value when x=0 (since b⁰=1, f(0)=a). Like the y-intercept's role, but now it's a *multiplier* the growth builds on. **Interpret it in context:** a is the amount you start with *before any growth/decay*: the initial population, the price when new, the deposit before interest.
- {#9.2.d3} **Growth/decay factor b:** what you **multiply by** each step (the continuous-function analogue of the common ratio r, same role, now allowed at every real x). b>1 → **growth**; 0<b<1 → **decay**. **Interpret it in context:** b is "what fraction of the previous amount you have after one period," so it directly *reads off* the percent change: **b = 1.05 means +5% per period** (you keep 100% and add 5%), **b = 1.20 means +20%**, **b = 0.90 means −10%** (you keep 90%, lose 10%), **b = 0.5 means −50%** (halves). The "+5%" lives in the *digits past the 1*; a b below 1 is a *loss* of (1 − b).
- {#9.2.d4} **Percent ↔ factor:** "+p%" → b = 1 + p/100 (e.g. +10% → 1.10); "−p%" → b = 1 - p/100 (e.g. −20% → 0.80). Run it backward too: given b, the per-period change is (b − 1)·100% (positive = growth, negative = decay).

Read these slowly too. Notice the check sitting inside several of them. Substituting back is how you know the value is right, not a chore added at the end.

**Worked examples:**

1. **Growth, +10% per year.** $100 invested at +10%/yr → a=100, b=1.10, so y = 100·1.1ˣ. Value after 3 years:
$$y = 100\cdot 1.1^{3} = 100\cdot 1.331 = 133.10$$
So $133.10. (Note b=1.10, *not* 0.10: you keep your 100% and add 10%.) **Interpret:** a=100 is the deposit before any interest; b=1.10 says the balance is 110% of the year before, i.e. +10% each year. **Rounding discipline:** here 1.1³ = 1.331 *exactly*, so the value is exactly $133.10. It happens to land on a whole cent. In general, carry the **exact** value through and round money to the nearest cent only at the *very end* (this is the "decimal drift" rule below, at its natural home).

2. **Doubling population.** 5, 10, 20, 40, ...: multiply by 2 each year → a=5, b=2, y = 5·2ˣ. Check: x=3 ⇒ 5·2³ = 40. This is the geometric sequence of 9.1 (a₁=5, r=2) as its **continuous** function: the sequence is just the dots at x = 1, 2, 3, …, and y = 5·2ˣ is the curve filling in every x between them (here r becomes the base b).

3. **Decay, halving.** An $80 value halved each year → a=80, b=0.5, y = 80·0.5ˣ: 80, 40, 20, 10, ... Since 0<0.5<1, it's **decay**. Value after 3 years: 80·0.5³ = 80·0.125 = 10.

4. **Percent → factor drill.** "+5%" → b=1.05; "−20%" → b=0.80; "doubles" → b=2; "halves" → b=0.5. E.g. a town of 1000 growing 5%/yr after 2 yr: 1000·1.05² = 1102.50.

5. **Classify a table.** 3, 6, 12, 24: differences 3,6,12 (not constant) but ratios 2,2,2 (constant) → **exponential**, b=2. Versus 3, 6, 9, 12: differences 3,3,3 constant → **linear**, slope 3.

6. **Interpret in context (read what a and b *mean*).** A town's population is y = 1500·1.05ˣ, with x in years. Don't just compute. *Say what the model claims*: a=1500 is the **starting population** (year 0, before any growth); b=1.05 means each year the population is **105% of the year before**, i.e. it **grows 5% per year**. Value after 2 years: 1500·1.05² = 1653.75 ≈ 1654 people. Contrast a decay model y = 2000·0.9ˣ (a piece of equipment): a=2000 is the **value when new**, b=0.9 means it keeps **90% of its value each year**, i.e. **loses 10% per year**; after 2 years 2000·0.9² = 1620. The skill: turn b into a sentence, "+5% a year" or "−10% a year", and a into "the amount before anything happens."

If one of your own answers ever fails its check, where you put a number back and the two sides don't agree, that's not failure, it's the check doing its job and catching something before it counted. Go back to your first step and re-run the arithmetic slowly. With these, a mismatch is almost always rounding too early or slipping on the percent-to-factor step, not the whole method.

With the method working, here are the slips to watch for. The most common is the percent-to-factor one from the top of the lesson, resurfacing under pressure: using 0.10 for "+10%" (which forgets the 100% you already have) or −0.20 / 1.20 for "−20%." Anchor it back to keeping: "+10%" means you still have all of it *plus* a tenth, so ×1.10; "−20%" means you *keep* 80%, so ×0.80.

The next one is treating 2ˣ as if it were 2x, applying the "add the same each step" reflex to a "multiply the same each step" object. You'd expect this to give 2, 4, 6, 8; the exponential actually gives 2, 4, 8, 16. The cure is the side-by-side table you just read: ask whether the *jump* is the same or the *×-factor* is the same.

A close cousin is mixing up the factor and the percent itself: reading b = 1.05 as "105% growth," or b = 0.9 as "90% decay." The factor is what you keep-plus-add; the *change* is b − 1. So b = 1.05 is +5% (not 105%), and b = 0.9 is −10% (you keep 90%, you lose ten). Practice both directions, percent to factor and factor back to percent, until they feel like two readings of the same fact.

A couple of smaller ones round it out. When you evaluate a·bˣ, do the exponent *first*, then multiply by a. It's a·(bˣ), not (a·b)ˣ. And keep the growth-versus-decay direction straight: b above 1 grows, b between 0 and 1 shrinks, so b = 0.5 is decay, never growth. Finally, the well-defined fence is there to stop you from calling things exponential that aren't: y = (−2)ˣ, y = 1ˣ, and y = 0·2ˣ all break a rule (a negative base isn't real at fractional inputs, b = 1 is just the constant a, and a = 0 is just the constant 0).

One last habit, the decimal one, because it's where careful work quietly goes wrong. Don't round in the middle. Round only at the end. In the first worked example, 1.1³ is *exactly* 1.331, so the balance is exactly $133.10; if you'd rounded 1.1³ to, say, 1.33 partway through, you'd drift off the true value. Carry the exact number through your arithmetic and round money to the nearest cent only at the very last step.

Here's a clean case to settle the method before the practice mixes things up. Evaluate y = 3·2ˣ at x = 2. The exponent first: 2² = 4. Then multiply by the 3: 3·4 = 12. Exponent, then multiply: that order, every time.

**Check for understanding (transfer):**
1. {#9.2.c1} "A $200 laptop loses 20% of its value each year. Write the function y = a·bˣ, and find its value after 2 years. What's b, and why isn't it 0.20?"
2. {#9.2.c2} "Here are two tables. A: 4, 7, 10, 13. B: 4, 8, 16, 32. Which is linear, which is exponential, and what's the giveaway in each?"
3. {#9.2.c3} "Linear y = 100x starts way ahead of exponential y = 2ˣ at x=1. Will the line stay ahead forever? Explain what eventually happens."

Worked solutions, so a wrong turn shows you where. For the first, losing 20% means keeping 80%, so b = 0.80 (not 0.20, which would be the part lost, not the part kept), the function is y = 200·0.8ˣ, and after 2 years y = 200·0.8² = 200·0.64 = 128.

For the second, table A adds 3 each step (constant difference), so it's linear; table B doubles each step (constant ratio), so it's exponential. The giveaway is difference-versus-ratio.

For the third, no: even though y = 100x starts far ahead, an increasing exponential overtakes any line eventually, so 2ˣ will pass 100x and then pull away for good. The doubling keeps compounding while the line only adds a fixed 100 each step.

As in the last lesson, the set ahead mixes problem types on purpose, which feels harder and is exactly what makes the skill hold; the answers are at the end, and the worked example behind a problem is there when one stalls you. The classify-the-table pair and the percent-and-factor groups sit next to each other so you keep switching between "is it a difference or a ratio?" and "is this growth or decay?"

**Practice problems:**
*Evaluate the exponential function:*
1. y = 5·2ˣ at x=3.
2. y = 80·0.5ˣ at x=3.
3. y = 100·1.1ˣ at x=2.
4. y = 200·0.8ˣ at x=2.
5. y = 3·2ˣ at x=4.
6. y = 100·1.1ˣ at x=3.
*Growth or decay? Give the factor b:*
7. A quantity that **doubles** each step.
8. A quantity that **−20%** each step.
9. A quantity that **+5%** each step.
10. A quantity that **halves** each step.
*Linear or exponential? (classify the table)*
11. 2, 5, 8, 11, ...
12. 2, 6, 18, 54, ...
*Interpret in context (say what a and b mean, then evaluate):*
13. A population is y = 1500·1.05ˣ (x in years). What is the starting population, what does b say about the yearly change (in %), and what's the population after 2 years?
14. A machine's value is y = 2000·0.9ˣ (x in years). What is its value when new, what does b say about the yearly change (in %), and what's its value after 2 years?
*Read the factor back as a percent (growth or decay, and how much per period):*
15. b = 1.20.
16. b = 0.85.

**Answer key:**
1. 5·2³ = 40 · 2. 80·0.5³ = 10 · 3. 100·1.1² = 121 · 4. 200·0.8² = 128 · 5. 3·2⁴ = 48 · 6. 100·1.1³ = 133.10 · 7. **growth**, b = 2 · 8. **decay**, b = 0.80 · 9. **growth**, b = 1.05 · 10. **decay**, b = 0.5 · 11. **linear** (constant difference +3) · 12. **exponential** (constant ratio ×3) · 13. start = **1500** people; b=1.05 → **+5% per year** (growth); after 2 yr 1500·1.05² = **1653.75 ≈ 1654** · 14. value when new = **$2000**; b=0.9 → **−10% per year** (decay); after 2 yr 2000·0.9² = **1620** ($1620) · 15. **growth, +20%** per period (since b − 1 = 0.20) · 16. **decay, −15%** per period (since b − 1 = −0.15).

---

You can now spot the one contrast this unit is built on: add the same each step is linear, multiply by the same each step is exponential. And you can work both sides of it: classify a list or table, write a sequence step by step or in one jump and move between the two, reach any term with a_n = a_1 + (n−1)d or a_n = a_1·r^(n−1), and turn a percent into a factor b and read a factor back as a percent.

Keep the exponential fence in view as you go: y = a·bˣ needs a ≠ 0, b > 0, and b ≠ 1.
