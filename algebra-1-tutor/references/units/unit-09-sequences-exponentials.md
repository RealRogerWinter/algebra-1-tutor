# Unit 9: Sequences & Exponential Functions

> **Prerequisites:** Unit 4 (functions, f(x) notation, input → one output, multiple representations). Helped by Unit 5 (linear functions as the "constant rate of change" family) — we contrast against it constantly. Comfort with exponents from Unit 1 and substituting into an expression is assumed.
> **By the end, the student can:**
> - See a sequence as a function: the term number n is the input, the term a_n is the output.
> - Identify a sequence as **arithmetic** (constant common difference d) or **geometric** (constant common ratio r), find d or r, and continue it.
> - Use the rules a_n = a_1 + (n-1)d and a_n = a_1 · r^(n-1) to find a specific term without listing them all.
> - Evaluate an exponential function y = a·bˣ and read off the starting amount a and growth/decay factor b.
> - Tell **linear from exponential** at a glance: constant *difference* (add the same each step) vs. constant *ratio* (multiply by the same each step), including from a table.
> - Identify growth (b>1) vs. decay (0<b<1) and turn a percent change into a factor.

## Teaching this unit (orientation for the tutor)

This is a **lighter, two-lesson unit** that introduces two new *function families* and — most importantly — sets up the one contrast that organizes everything: **linear means a constant DIFFERENCE (you add the same amount each step); exponential means a constant RATIO (you multiply by the same amount each step).** Say that sentence early, repeat it often, and hang both lessons on it.

Thread the **Unit 4 function language** the whole way: a sequence is *literally a function* whose inputs are the counting numbers 1, 2, 3, ... The vending machine / recipe pictures (`metaphors.md` → Functions) still apply — feed in the term number, get back the term. And keep the **Unit 5 callback** alive: a linear function is the "+ the same each step" family they already know; arithmetic sequences are just linear functions sampled at the counting numbers (same common difference d = the slope). Geometric/exponential is the genuinely new behavior.

Look **forward** too: Unit 12 introduces quadratics as yet *another* family (constant *second* difference). Planting "different families behave differently" here pays off there. (Unit 10 will formalize exponent rules; here we only need bˣ for whole-number-ish inputs, so keep exponent mechanics light.)

**Biggest misconception traps in this unit:**
- **Confusing difference with ratio** — calling 2, 6, 18, 54 arithmetic because "it keeps going up," or trying to find a common difference for a geometric sequence. Repair: have them compute *both* the differences and the ratios between consecutive terms and ask which one is *constant*.
- **The n-1 in the rule.** Students use n instead of n-1 (because the first term already *is* a_1, you take only n-1 steps to reach the nth term). Tell: their term is one step too far. Anchor with "term 1 takes *zero* steps."
- **Percent → factor errors.** "+10%" becomes a factor of 1.10 (not 0.10); "−20%" becomes 0.80 (not -0.20 or 1.20). This is the percent-change work of Unit 3 resurfacing. See `misconceptions.md §7` (reading what the expression *says*, e.g. p + 0.10p = 1.10p).
- **Linear-izing exponentials.** Treating y = 2ˣ like y = 2x — a constant-difference reflex applied to a constant-ratio object. The side-by-side table is the cure: exponential pulls away and eventually overtakes *any* line.

**Visuals:** mostly **tables**, not graphs (`visuals.md` → "Pair every visual with words / a small table"). The signature visual of this unit is a **two-column comparison table** showing constant difference vs. constant ratio, and the **linear-vs-exponential side-by-side table**. Compute every entry (verify with the code tool — a wrong table teaches a wrong pattern). If you do graph an exponential, you can reuse `visuals.md` **Template 2**'s coordinate-mapping rule, but a clean table is usually enough here. No new template is required.

There is no dedicated metaphor entry for sequences in `metaphors.md`; build on the **Functions** entries there (the machine fed the counting numbers) plus a plain "interest/doubling" story for exponentials, and walk from the story to the symbols as always (concreteness fading, `pedagogy.md`).

---

## Lesson 9.1: Arithmetic & geometric sequences as functions

**Goal:** Recognize a sequence as a function on the counting numbers, classify it as arithmetic (constant d) or geometric (constant r), and find any term with the rule a_n = a_1 + (n-1)d or a_n = a_1 · r^(n-1).
**Why it matters:** Sequences are the gentlest on-ramp to a new function family, and they make the central contrast — *add the same* vs. *multiply the same* — concrete and countable before we dress it up as y = a·bˣ in 9.2.
**New terms:**
- **Sequence:** an ordered list of numbers, called **terms**. The 1st term is a_1, the 2nd is a_2, and the nth is a_n.
- **Term number n:** the position in the list — 1, 2, 3, ... This is the **input**; the term a_n is the **output**. So a sequence *is a function* whose domain is the counting numbers.
- **Arithmetic sequence:** each term is the previous one **plus a fixed number**, the **common difference d**. (Constant *difference*.)
- **Geometric sequence:** each term is the previous one **times a fixed number**, the **common ratio r**. (Constant *ratio*.)

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete / function callback:** "A sequence is the Unit 4 function machine (`metaphors.md` → Functions) fed the counting numbers: input 1 → 1st term, input 2 → 2nd term. The *rule* of the machine is what we're after." Start with the list 3, 7, 11, 15, ... and ask: "what do you do to get from each term to the next?" (add 4). Then 2, 6, 18, 54, ...: "and here?" (times 3). Name the two behaviors: **add the same** = arithmetic, **multiply the same** = geometric.
- **Pictorial / the diagnostic table:** write the terms in a row and the *jumps* underneath. For arithmetic show the **differences** are all equal; for geometric show the **ratios** are all equal. This little table *is* the classification tool — always compute both when unsure.

  | term n | 1 | 2 | 3 | 4 |
  |----|----|----|----|----|
  | 3,7,11,15 (arith) | 3 | 7 | 11 | 15 |
  | difference | — | +4 | +4 | +4 |
  | 2,6,18,54 (geo) | 2 | 6 | 18 | 54 |
  | ratio | — | x3 | x3 | x3 |

- **Symbolic:** to reach the nth term you start at a_1 and take n-1 steps (term 1 takes **zero** steps — that's where the n-1 comes from):
  $$a_n = a_1 + (n-1)\,d \qquad\text{(arithmetic)}\qquad\qquad a_n = a_1\cdot r^{\,n-1}\quad\text{(geometric)}$$
  Verify any specific term with the code tool.

**Worked examples:**

1. **Arithmetic** 3, 7, 11, 15, ...: consecutive differences 7-3=4, 11-7=4, 15-11=4 are all 4, so d=4, a_1=3. Find a_10:
$$a_{10} = 3 + (10-1)\cdot 4 = 3 + 9\cdot 4 = 3 + 36 = 39$$

2. **Geometric** 2, 6, 18, 54, ...: consecutive ratios 6/2=3, 18/6=3, 54/18=3 are all 3, so r=3, a_1=2. Find a_5:
$$a_5 = 2\cdot 3^{\,5-1} = 2\cdot 3^{4} = 2\cdot 81 = 162$$

3. **Which type?** 5, 8, 11, 14, ...: differences are all +3 and the ratios (8/5, 11/8, ...) are *not* constant → **arithmetic**, d=3. Next term: 14+3 = 17.

4. **Which type?** 4, 12, 36, 108, ...: ratios are all ×3 (differences 8, 24, 72 are not constant) → **geometric**, r=3. Next term: 108·3 = 324.

5. **A descending arithmetic sequence** 10, 7, 4, 1, ...: d = -3. Find a_8:
$$a_8 = 10 + (8-1)(-3) = 10 + 7(-3) = 10 - 21 = -11$$

**Watch for:**
- **Difference vs. ratio mix-up** — the headline trap. Tell: they call a doubling list "arithmetic," or hunt for a common difference in 2,6,18. Repair (don't restate): "Compute *both* the jumps *and* the ×-factors between terms — which one stays the same?" (`misconceptions.md §7` — read what the pattern actually does.)
- **The n-1 slip** — using n instead of n-1 (e.g. a_10=3+10·4). Tell: the answer is exactly one d (or one factor of r) too big. Anchor: "term 1 takes zero steps; the 10th term is 9 steps from the first."
- **Off-by-one when counting which term.** Have them say "a_1 is the *first* term" out loud and index carefully.
- **Negative d handled as positive** in a descending sequence — a `misconceptions.md §3` negatives slip; have them keep the sign of d attached.

**Visuals to offer:** the **difference/ratio diagnostic table** above (in-chat, always renders). No SVG needed.

**Check for understanding (transfer):**
1. "Is 1, 5, 25, 125, ... arithmetic or geometric, and how can you *prove* it from the numbers — not just by feel?"
2. "An arithmetic sequence starts at 6 with d = 4. Without listing all of them, what's the 20th term, and why is it 6 + 19·4 and not 6 + 20·4?"
3. "Two sequences both start 2, ... — one is arithmetic with d=2, the other geometric with r=2. Write the first four terms of each. Where do they split apart?"

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

**Answer key:**
1. d = 3, **arithmetic** · 2. r = 2, **geometric** · 3. d = -3, **arithmetic** · 4. r = 5, **geometric** · 5. d=7 → next two: 30, 37 · 6. r=3 → next two: 108, 324 · 7. d=-10 → next two: 70, 60 · 8. a_10 = 5 + (10-1)·3 = 32 · 9. a_5 = 2·3⁴ = 162 · 10. a_7 = 3·2⁶ = 192 · 11. a_8 = 10 + 7(-3) = -11 · 12. a_10 = 2·2⁹ = 1024.

---

## Lesson 9.2: Exponential growth & decay; linear vs. exponential

**Goal:** Evaluate an exponential function y = a·bˣ, read its starting amount a and factor b, classify growth (b>1) vs. decay (0<b<1), turn a percent change into a factor, and distinguish linear from exponential from a table.
**Why it matters:** Exponential models real growth and decay — money at interest, populations, half-lives — and the linear-vs-exponential distinction is one of the most useful "read the situation" skills in all of algebra. It's also the smooth-function version of 9.1's geometric sequence.
**New terms:**
- **Exponential function:** y = a·bˣ (also f(x) = a·bˣ). The variable is in the **exponent** — that's what makes it exponential, not linear.
- **Starting amount a:** the value when x=0 (since b⁰=1, f(0)=a). Like the y-intercept's role, but now it's a *multiplier* the growth builds on.
- **Growth/decay factor b:** what you **multiply by** each step (the smooth cousin of the common ratio r). b>1 → **growth**; 0<b<1 → **decay**.
- **Percent ↔ factor:** "+p%" → b = 1 + p/100 (e.g. +10% → 1.10); "−p%" → b = 1 - p/100 (e.g. −20% → 0.80).

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** "Linear is repeated **addition** — +$5 a week, the same dollars each step (Unit 5's slope). Exponential is repeated **multiplication** — your money grows by *the same percent*, so the dollar amount itself gets bigger each step." Use a doubling story (5 bacteria → 10 → 20 → 40, b=2) and a halving/decay story (an $80 phone losing half its value each year, b=0.5).
- **Pictorial / the two killer tables.** First, the **percent → factor** move: +10% means "keep the 100% you have *and* add 10%," i.e. ×1.10 — this is p + 0.10p = 1.10p from `misconceptions.md §7`. Second, the **linear-vs-exponential side-by-side** table — the signature visual of the unit:

  | x | linear y=2x | exponential y=2^x |
  |----|----|----|
  | 0 | 0 | 1 |
  | 1 | 2 | 2 |
  | 2 | 4 | 4 |
  | 3 | 6 | 8 |
  | 4 | 8 | 16 |
  | 5 | 10 | 32 |
  | 6 | 12 | 64 |

  Point at it: the line adds 2 each row (**constant difference**); the exponential *doubles* each row (**constant ratio**), is tied at x=2, then pulls away and overtakes — and an exponential overtakes **any** line eventually.
- **Symbolic:** evaluate y = a·bˣ by substituting x. To classify a table, check whether consecutive outputs share a constant **difference** (linear) or a constant **ratio** (exponential) — the exact 9.1 diagnostic, now naming the family. Verify all values with the code tool (watch decimals — keep exact values).

**Worked examples:**

1. **Growth, +10% per year.** $100 invested at +10%/yr → a=100, b=1.10, so y = 100·1.1ˣ. Value after 3 years:
$$y = 100\cdot 1.1^{3} = 100\cdot 1.331 = 133.10$$
So $133.10. (Note b=1.10, *not* 0.10: you keep your 100% and add 10%.)

2. **Doubling population.** 5, 10, 20, 40, ... — multiply by 2 each year → a=5, b=2, y = 5·2ˣ. Check: x=3 ⇒ 5·2³ = 40. This is the geometric sequence of 9.1 written as a function.

3. **Decay, halving.** An $80 value halved each year → a=80, b=0.5, y = 80·0.5ˣ: 80, 40, 20, 10, ... Since 0<0.5<1, it's **decay**. Value after 3 years: 80·0.5³ = 80·0.125 = 10.

4. **Percent → factor drill.** "+5%" → b=1.05; "−20%" → b=0.80; "doubles" → b=2; "halves" → b=0.5. E.g. a town of 1000 growing 5%/yr after 2 yr: 1000·1.05² = 1102.50.

5. **Classify a table.** 3, 6, 12, 24: differences 3,6,12 (not constant) but ratios 2,2,2 (constant) → **exponential**, b=2. Versus 3, 6, 9, 12: differences 3,3,3 constant → **linear**, slope 3.

**Watch for:**
- **Percent → factor errors** — using 0.10 for "+10%" (forgetting the base 100%), or -0.20/1.20 for "−20%." `misconceptions.md §7`. Repair: "+10% of what you have means you still have all of it *plus* a tenth → ×1.10." Decay: "−20% means you *keep* 80% → ×0.80."
- **Treating 2ˣ like 2x** — the constant-difference reflex on a constant-ratio object. Tell: their table goes 2, 4, 6, 8 instead of 2, 4, 8, 16. Cure: the side-by-side table; "is the *jump* the same, or the *×-factor* the same?"
- **Order-of-operations on a·bˣ** — computing (a·b)ˣ instead of a·(bˣ). Exponent first, *then* multiply by a. (`misconceptions.md §5` order of operations.)
- **Growth/decay backwards** — calling b=0.5 "growth." Anchor: b>1 grows, b between 0 and 1 shrinks.
- **Decimal drift** — rounding 1.1³ early. Keep exact values (it's exactly 1.331, so $133.10); verify with the code tool.

**Visuals to offer:** the **linear-vs-exponential side-by-side table** and the **percent→factor** mini-table above (in-chat, always render). A graph isn't required; if offered, reuse `visuals.md` Template 2's mapping and always pair it with the table.

**Check for understanding (transfer):**
1. "A $200 laptop loses 20% of its value each year. Write the function y = a·bˣ, and find its value after 2 years. What's b, and why isn't it 0.20?"
2. "Here are two tables. A: 4, 7, 10, 13. B: 4, 8, 16, 32. Which is linear, which is exponential, and what's the giveaway in each?"
3. "Linear y = 100x starts way ahead of exponential y = 2ˣ at x=1. Will the line stay ahead forever? Explain what eventually happens."

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

**Answer key:**
1. 5·2³ = 40 · 2. 80·0.5³ = 10 · 3. 100·1.1² = 121 · 4. 200·0.8² = 128 · 5. 3·2⁴ = 48 · 6. 100·1.1³ = 133.10 · 7. **growth**, b = 2 · 8. **decay**, b = 0.80 · 9. **growth**, b = 1.05 · 10. **decay**, b = 0.5 · 11. **linear** (constant difference +3) · 12. **exponential** (constant ratio ×3).

---

## Wrap-up & interleaving

**Consolidate:** the organizing idea of the unit is one sentence — **linear = constant difference (add the same each step); exponential = constant ratio (multiply the same each step)** — with sequences as the discrete version (arithmetic ↔ linear, geometric ↔ exponential) and y = a·bˣ as the smooth version. Make sure the student can (1) classify a list or table both ways, (2) use a_n = a_1+(n-1)d and a_n = a_1·r^(n-1) without re-listing, and (3) turn a percent change into a factor b.

**Mix back in:**
- **Unit 4 (functions):** keep naming a sequence "a function on the counting numbers" and exponentials with f(x) = a·bˣ; evaluate f(0)=a just like the intercept idea.
- **Unit 5 (linear):** every time arithmetic/linear appears, call d the *slope* and "add the same each step" the *constant rate of change* — the contrast with geometric/exponential is the whole point.
- **Unit 3 (percent change):** the percent→factor move (+10% → 1.10, -20% → 0.80) is Unit 3 resurfacing; slip in a percent-change problem as warm-up.
- **Negatives (`misconceptions.md §3`):** descending arithmetic sequences (negative d) are the natural place to keep sign-handling warm.

**Looking ahead:** Unit 10 formalizes exponent rules (so bˣ gets a fuller toolkit) and Unit 12 introduces **quadratics as yet another function family** (constant *second* difference, a U-shaped graph). The habit planted here — "ask which family this is before you compute" — is exactly the reflex Unit 12 rewards.

**Progress Card should note:** whether the student reliably separates **difference vs. ratio** (the headline skill), handles the n-1 in the sequence rules, converts **percent ↔ factor** cleanly, and reads **growth vs. decay** from b. Note any lingering "treats 2ˣ like 2x" reflex or percent-to-factor slips to warm up next session.
