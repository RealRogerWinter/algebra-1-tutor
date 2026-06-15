# Unit 11: Factoring

> This unit is about factoring: taking an expression like x²+5x+6 and rewriting it as a product, (x+2)(x+3). It's worth learning because it's the move that makes solving quadratics possible in the next unit, and it has a built-in way to check your own work.
>
> It helps to have multiplying polynomials from Unit 10 fresh in your mind, since factoring is that same work run backward.

Before you start a session, redo two or three problems from a lesson or two back from memory. It's a small warm-up, and it's one of the most useful things you can do to keep a skill from fading.

One idea runs through the whole unit: factoring is multiplying, run backward. In Unit 10 you took two factors and built a product; you filled in the area box. Here you're handed the finished product and asked to rebuild the factors: the same box, but now you're working out the edges.

That backward move has a useful side effect. Because factoring undoes multiplying, you can always check your answer by multiplying it back out, and you must land on exactly what you started with. You'll use that check on every single example. If a factorization doesn't multiply back to the original, it's simply wrong, so you redo it, with no guessing whether it's right.

One ground rule makes "does this factor?" a question with a definite answer: in this unit, we factor over the integers. Every factor you write has whole-number coefficients. So the only honest endings are a clean integer factorization or the verdict **prime**. We don't reach for fractions, decimals, square roots, or anything fancier as factoring tools here. Those belong to Unit 12.

---

## Lesson 11.1: Greatest common factor (GCF)

Start with a picture you can hold. Imagine a row of gift bags, and every bag has a chocolate inside. You can reach into each bag, take out one chocolate, and set them all in a single pile out front. That pile is the chocolates every bag was carrying. What's left stays in the bags.

That's exactly what pulling out a greatest common factor does. Take 6x + 9. Both terms are divisible by 3, so both bags are carrying a 3. The 3 comes out front, and what's left of each term goes inside the parentheses:

$$6x + 9 = 3(2x + 3)$$

This is the first thing to try on any factoring problem. Pulling out a shared factor often shrinks a scary-looking expression into something plain, and it's the exact reverse of the single-term distributing you did in Units 2 and 10. It also gives you the multiply-back check that the rest of the unit leans on.

Here's the same idea as a picture, using the area box from Unit 10 run backward. Think of 4x² + 8x as the *inside* of a one-row box whose left edge is 4x. The top edges are whatever you multiply 4x by to land on each piece:

$$\begin{array}{c|c|c}
 & x & 2 \\ \hline
4x & 4x^2 & 8x
\end{array}\qquad\Rightarrow\qquad 4x^2+8x = 4x(x+2)$$

The left edge, 4x, is the common factor; the top edges, x and 2, are what's left inside.

Now the symbols. Finding the GCF comes in two parts. First the number: the biggest number that divides every coefficient evenly. For 4x² + 8x, that's the biggest number dividing both 4 and 8, which is 4.

Then the variables: the *lowest* power of the variable that shows up in every term. Here you have x² in the first term and x¹ in the second, so the most that *every* term carries is x¹. Multiply the two parts together and the GCF is 4x. Divide each term by 4x to find what stays inside.

One thing to name before it trips you up. When you divide 8x by 4x, you get 2, not 0. The term doesn't vanish; it just gets smaller by the factor you removed. Nothing disappears by magic. The piece is still there, shrunk down to what's left after the common factor came out.

**New terms:**
- {#11.1.d1} **Factor (noun):** something multiplied. In 6=2·3, both 2 and 3 are factors of 6. In 3(2x+3), the factors are 3 and (2x+3).
- {#11.1.d2} **Greatest common factor (GCF):** the *largest* factor (biggest number times the most variables) that divides evenly into **every** term.
- {#11.1.d3} **Factor (verb):** to rewrite a sum as a product, i.e. to *undo* distributing.

**Worked examples** (each pulls the GCF, then checks by multiplying back):

*Numbers only:*
{#11.1.w1}
$$6x+9 \;=\; 3(2x+3) \qquad \text{Check: } 3\cdot 2x + 3\cdot 3 = 6x+9$$

*Number and a variable:*
{#11.1.w2}
$$4x^2+8x \;=\; 4x(x+2) \qquad \text{Check: } 4x\cdot x + 4x\cdot 2 = 4x^2+8x$$

*Higher powers, take the lowest power of x:*
{#11.1.w3}
$$15x^3-10x^2 \;=\; 5x^2(3x-2) \qquad \text{Check: } 5x^2\cdot 3x - 5x^2\cdot 2 = 15x^3-10x^2$$
Both terms carry at least x², so x² comes out; the biggest number dividing 15 and 10 is 5, so 5 comes out. Together the GCF is 5x².

*The "stopped too early" trap, done right:*
{#11.1.w4}
$$12x+18 \;=\; 6(2x+3) \qquad \text{Check: } 6\cdot 2x + 6\cdot 3 = 12x+18$$
Here's the slip worth knowing now that you've factored a few cleanly. It's easy to pull out *a* common factor and stop, to write 2(6x + 9) or 3(4x + 6) and call it done. Those are common factors, but not the *greatest* one: look inside the parentheses and the pieces still share a factor. Only pulling the full 6 leaves an inside, 2x + 3, with nothing left to take. A quick self-check: after you factor, glance inside the parentheses and ask whether those terms *still* have something in common. If they do, you didn't take it all.

*Variable factor with a negative inside:*
{#11.1.w5}
$$10x^2-25x \;=\; 5x(2x-5) \qquad \text{Check: } 5x\cdot 2x - 5x\cdot 5 = 10x^2-25x$$
Notice the minus stayed put. When a term is subtracted, keep its sign as you pull the factor out, and the multiply-back check catches a dropped sign instantly.

Two more slips that the multiply-back check will always expose, so you're never relying on memory alone. One is forgetting the variable part: writing 4x² + 8x = 4(x² + 2x) and leaving an x behind. The fix is to ask whether *every* bag has at least one x, and if so, the x comes out too.

The other is taking too high a power: trying to pull x³ out of 15x³ − 10x², when the second term only has x². You can only take the *lowest* power that every term actually has.

Here's a clean one to get the move running before the practice mixes things up. Factor 8x² + 12x. The biggest number dividing 8 and 12 is 4, and both terms carry at least one x, so the GCF is 4x. That leaves 4x(2x + 3). Multiply back: 4x·2x + 4x·3 = 8x² + 12x. It matches. Just the one move, start to finish.

**Check for understanding (transfer):**
1. {#11.1.c1} Factor 8x²+12x, then prove it's right on your own. (The GCF is 4x, giving 4x(2x+3); multiply it back out. 4x·2x + 4x·3 = 8x²+12x, and it matches, so it's right.)
2. {#11.1.c2} Someone writes 6x+9=3(2x+9). Multiply it back. Where did it go wrong? (Multiplying back gives 3·2x + 3·9 = 6x+27, not 6x+9. The 9 inside should be 3, since 3·3 = 9; the right answer is 3(2x+3).)
3. {#11.1.c3} Why can't you pull x² out of 15x³−10x² as x² *and* still leave an x in the second term? (The second term *is* the x² piece. Once you take x² out of −10x², all that's left is the coefficient −10. There's no extra x hiding in it to leave behind.)

You can now find the greatest common factor of a polynomial, the biggest number times the most variables that every term shares, pull it out front, and confirm your work by multiplying back.

Mixed practice feels harder than repeating one kind of problem, and that's the point. It's what makes the skill last. Every problem below has its answer at the end of the lesson, and if one stalls you, flip back to the worked example it's based on. That's what it's there for.

**Practice problems:**

*Numbers only:*
1. 2x+6  2. 5x+15  3. 6x+9  4. 4x-12  5. 8x+20  6. 9x-6

*With a variable:*
7. x²+7x  8. 3x²+6x  9. 10x²-15x  10. 4x²+8x

*Higher powers (take the lowest power):*
11. 6x³-9x²  12. 14x²+21x  13. 12x³+8x²  14. 18x²-12x

**Answer key (multiply each back to confirm):**
1) 2(x+3)  2) 5(x+3)  3) 3(2x+3)  4) 4(x-3)  5) 4(2x+5)  6) 3(3x-2)  7) x(x+7)  8) 3x(x+2)  9) 5x(2x-3)  10) 4x(x+2)  11) 3x²(2x-3)  12) 7x(2x+3)  13) 4x²(3x+2)  14) 6x(3x-2)

---

## Lesson 11.2: Factoring trinomials x²+bx+c

This is the lesson the unit builds toward, so give it the most time. It's the exact reverse of multiplying two binomials in Unit 10, and it's the move that makes solving quadratics in Unit 12 possible. Once you can turn x²+5x+6 into (x+2)(x+3), setting it equal to zero and reading off the answers is one short step away.

Picture the area box from Unit 10 again, but backward. When you multiplied (x+2)(x+3), the box filled in: the corner cells came out x² and 6, and the two middle cells, 2x and 3x, added to 5x. Factoring runs that in reverse. Now you're handed the inside of the box, with the x², the middle, and the corner, and you have to find the edges:

$$\begin{array}{c|c|c}
 & x & \,? \\ \hline
x & x^2 & ?x \\ \hline
? & ?x & 6
\end{array}$$

The two unknown edges have to multiply to 6 (that's the corner cell), and their x-terms have to add to 5x (that's the middle). Which is exactly one question, and it's the question behind every trinomial: what two numbers multiply to c and add to b?

So the method is a search for two numbers. List the pairs that multiply to c, and pick the pair that adds to b. For x²+5x+6, the pairs multiplying to 6 are 1·6 and 2·3; only 2 + 3 gives 5. So the factors are (x+2)(x+3).

The part that takes real care is the signs, and they aren't a guess: the signs of c and b *tell* you the signs of the two numbers. Here's how to read them. Look first at c.

When c is positive, the two numbers have the *same* sign, because their product came out positive. Then b breaks the tie: if b is positive too, both numbers are positive, and if b is negative, both are negative.

When c is negative, the two numbers have *opposite* signs, because their product is negative. Then the number with the larger size carries the sign of b.

Take the signs slowly, in that order: c first, then b. And if one slips, the multiply-back check catches it, since the middle term comes out wrong.

| signs | c | b | the two numbers | example |
|---|---|---|---|---|
| both + | + | + | both positive | x^2+5x+6=(x+2)(x+3) |
| both - | + | - | both negative | x^2-5x+6=(x-2)(x-3) |
| opposite, sum + | - | + | bigger one positive | x^2+x-6=(x+3)(x-2) |
| opposite, sum - | - | - | bigger one negative | x^2-x-6=(x-3)(x+2) |

**New terms:**
- {#11.2.d1} **Trinomial:** a polynomial with three *unlike* terms (after combining like terms), here x²+bx+c: a squared term, an x term, and a constant.
- {#11.2.d2} **Prime (irreducible over the integers):** a trinomial that **cannot** be written as a product of two binomials with integer coefficients. When the two-number search comes up empty, the trinomial is prime. That's a real answer, not a failure.
- {#11.2.d3} **Monic:** leading coefficient 1, i.e. the x² has no number in front (just x², not 3x²). Every trinomial in this lesson is monic. Trinomials like 2x²+7x+3, where the leading coefficient is not 1, factor by an extension of this method covered later.

These cover all four sign cases. The check on each is just a Unit 10 expansion, run back to front.

**Worked examples** (covering all sign cases; each checked by expanding back):

*Both positive (c>0, b>0):*
{#11.2.w1}
$$x^2+5x+6=(x+2)(x+3) \qquad \text{Check: } x^2+3x+2x+6 = x^2+5x+6$$
(2·3=6, 2+3=5.)

*Both negative (c>0, b<0):*
{#11.2.w2}
$$x^2-5x+6=(x-2)(x-3) \qquad \text{Check: } x^2-3x-2x+6 = x^2-5x+6$$
(c is positive, so same sign; b is negative, so both negative. (−2)(−3)=6, and (−2)+(−3)=−5.)

*Opposite signs, sum positive (c<0, b>0):*
{#11.2.w3}
$$x^2+x-6=(x+3)(x-2) \qquad \text{Check: } x^2-2x+3x-6 = x^2+x-6$$
(c is negative, so opposite signs; you need a product of −6 and a sum of +1, which is +3 and −2.)

*Opposite signs, sum negative (c<0, b<0):*
{#11.2.w4}
$$x^2-x-6=(x-3)(x+2) \qquad \text{Check: } x^2+2x-3x-6 = x^2-x-6$$
(Opposite signs again; product −6, sum −1, so the bigger number, 3, is the negative one.)

*A bigger both-positive one:*
{#11.2.w5}
$$x^2+7x+12=(x+3)(x+4) \qquad \text{Check: } x^2+4x+3x+12 = x^2+7x+12$$
(Pairs of 12: 1·12, 2·6, 3·4; only 3 + 4 gives 7.)

*Opposite signs, larger gap:*
{#11.2.w6}
$$x^2-2x-15=(x-5)(x+3) \qquad \text{Check: } x^2+3x-5x-15 = x^2-2x-15$$
(Product −15, sum −2, so −5 and +3; the bigger one, 5, is negative because b is negative.)

With a few correct ones behind you, here's a slip that's easy to make. The mix-up is reasoning the signs backward: writing x²−5x+6 as (x+2)(x+3) when both numbers should be negative, or putting the minus on the wrong number in x²+x−6. When this happens, the multiply-back check gives the wrong middle term, which is your signal.

To set it right, walk the signs again in order: is c positive or negative, so same sign or opposite? Then which sign does b force? A close cousin is swapping the targets, hunting for numbers that *add* to c and *multiply* to b. The constant sitting on its own is always the *product* target; b is the sum.

### When nothing fits: prime trinomials

Not every trinomial factors over the integers, and saying so plainly matters, because the alternative is hunting forever for an answer that isn't there. The two-number search has a *finite* list to check, just the factor pairs of c, so it can genuinely run out. When it does, the trinomial is **prime**, and that's the correct, complete answer, not a sign you failed.

Here's the rule that tells you when to stop. To factor x²+bx+c, list every integer pair that multiplies to c, then check each pair's sum against b. If no pair sums to b, stop: the trinomial is **prime (irreducible over the integers)**. Working through the whole list *is* the proof. It's the same "I actually checked" spirit as multiplying back, turned on the search itself. The key is that the list has to be *exhausted*: you've earned the word "prime" only after every pair has been tried, including the negative pairs when the signs call for them.

*A prime one (c>0, b>0):*
{#11.2.w7}
$$x^2+2x+5 \;\Rightarrow\; \text{prime (irreducible over the integers)}$$
Since c = 5 is positive, the two numbers would share a sign, and since b is positive, both would be positive. The only positive pair multiplying to 5 is 1·5, and that sums to 6, not 2. There's no other pair. The search is exhausted, so it's prime. There's nothing to multiply back here, and that's fine, because the finished list is the proof.

*Another prime one:*
{#11.2.w8}
$$x^2+x+1 \;\Rightarrow\; \text{prime (irreducible over the integers)}$$
Here c = 1 and b = 1. The only integer pairs multiplying to 1 are 1·1 (sum 2) and (−1)(−1) (sum −2); neither sums to 1. List exhausted, so it's prime.

Two honest cautions about "prime." First, "prime" doesn't mean "I gave up." It means you finished a finite search and it came up empty, so always list the pairs and read off the sums, the way the examples above do.

Second, don't reach for non-integers to rescue a near-miss. You might notice that x²+5x+9 *almost* works and feel tempted to try fractions or decimals. Hold the line: over the integers it's prime, full stop. Other tools for these come in Unit 12.

And one trap that hides a prime answer: a GCF can disguise things. Take 2x²+4x+10. As written it looks unfactorable, but it isn't prime. Pull the 2 out first to get 2(x²+2x+5), and *then* the inside, x²+2x+5, is prime. So "factor completely" here means 2(x²+2x+5): the GCF out front, the prime piece left intact.

This is the reason for a habit worth adopting now: always try the GCF before the two-number search. Pulling the shared factor leaves a smaller, friendlier trinomial inside, and it keeps you from wrongly calling something prime.

A couple more places people stumble, both caught by the same multiply-back habit. One is declaring "prime" too soon: quitting after one or two pairs instead of all of them, or forgetting the negative pairs when c is positive and b is negative. Only an exhausted list earns the word.

The other is skipping the check entirely, accepting, say, (x+2)(x+3) for x²+6x+6 without expanding. Always multiply back, because the middle term is where errors surface. (And as it happens, x²+6x+6 is itself prime: no integer pair multiplies to 6 and adds to 6.)

If a problem still isn't landing after you've walked the signs and the pairs, it's fine to leave it and come back tomorrow. A break genuinely helps, and you haven't lost anything. When you return, re-read the area-box picture at the top of the lesson first; that's the version of this idea everything else is built on.

**Check for understanding (transfer):**
1. {#11.2.c1} Factor x²+8x+15, and say *why* both numbers are positive. (The pairs of 15 are 1·15 and 3·5; only 3 + 5 gives 8, so it's (x+3)(x+5). Both numbers are positive because c is positive, so they share a sign, and b is positive too, which forces both to be positive.)
2. {#11.2.c2} What changes between x²+2x−8 and x²−2x−8? Factor both. (Both have c negative, so opposite signs; the pair is 4 and 2. The sign of b decides which one is negative: x²+2x−8=(x+4)(x−2), and x²−2x−8=(x−4)(x+2). Flipping b's sign flips which number carries the minus.)
3. {#11.2.c3} Someone says x²−7x+12=(x+3)(x+4). Multiply it back. What's wrong, and what's the fix? (Multiplying back gives x²+7x+12, a +7x where you need −7x. Since c is positive and b is negative, both factors should be negative: (x−3)(x−4).)
4. {#11.2.c4} Is x²+3x+5 factorable over the integers? List the pairs out loud and decide. (The only pair multiplying to 5 is 1·5, which sums to 6, not 3, and there's no other pair. The list is exhausted, so it's **prime**.)

You can now factor a monic trinomial by finding the two numbers that multiply to c and add to b, reason out their signs from the signs of c and b, and recognize honestly when a trinomial is prime. And you can confirm every answer by multiplying it back.

**Practice problems:**

*Both positive (c>0, b>0):*
1. x²+5x+6  2. x²+7x+10  3. x²+8x+15  4. x²+9x+20

*Both negative (c>0, b<0):*
5. x²-5x+6  6. x²-7x+12  7. x²-8x+15  8. x²-6x+8

*Opposite signs, sum positive (c<0, b>0):*
9. x²+x-6  10. x²+2x-8  11. x²+3x-10

*Opposite signs, sum negative (c<0, b<0):*
12. x²-x-6  13. x²-2x-15  14. x²-4x-12

*Factorable **or** prime? (decide for each; some don't factor over the integers):*
15. x²+10x+21  16. x²+x+1  17. x²-x-12  18. x²+2x+5  19. x²+4x+3  20. x²+3x+5  21. x²-9x+18  22. x²-3x+10

**Answer key (multiply each back; watch the middle term):**
1) (x+2)(x+3)  2) (x+2)(x+5)  3) (x+3)(x+5)  4) (x+4)(x+5)  5) (x-2)(x-3)  6) (x-3)(x-4)  7) (x-3)(x-5)  8) (x-2)(x-4)  9) (x+3)(x-2)  10) (x+4)(x-2)  11) (x+5)(x-2)  12) (x-3)(x+2)  13) (x-5)(x+3)  14) (x-6)(x+2)
15) (x+3)(x+7)  16) **prime (irreducible over the integers)**  17) (x-4)(x+3)  18) **prime (irreducible over the integers)**  19) (x+1)(x+3)  20) **prime (irreducible over the integers)**  21) (x-3)(x-6)  22) **prime (irreducible over the integers)**

*Sign spot-checks:* #5: (-2)(-3)=6, (-2)+(-3)=-5. #11: (+5)(-2)=-10, 5+(-2)=+3. #14: (-6)(+2)=-12, -6+2=-4.
*Prime spot-checks (show the search is exhausted):* #16 pairs of 1: 1+1=2, (-1)+(-1)=-2 — neither is 1. #18 pairs of 5: 1+5=6 — not 2. #20 pairs of 5: 1+5=6 — not 3. #22 c=10, b=-3 needs a negative pair: -1-10=-11, -2-5=-7 — neither is -3.

---

## Lesson 11.3: Special patterns

Two kinds of factoring show up so often that it pays to recognize them on sight, without running the full two-number search each time. The first is a **difference of squares**, like x²−9. The second is a **perfect-square trinomial**, like x²+6x+9. Learning to spot them saves you the whole two-number search.

Start with the difference of squares, and build it rather than just state it. Multiply (a+b)(a−b) with the area box from Unit 10:

$$\begin{array}{c|c|c}
 & a & -b \\ \hline
a & a^2 & -ab \\ \hline
b & ab & -b^2
\end{array}\qquad\Rightarrow\qquad a^2 - ab + ab - b^2 = a^2-b^2$$

Look at the two middle cells: +ab and −ab. They add to zero, so the middle term goes to zero and disappears, leaving just a²−b². Run that backward and you have your factoring rule.

How do you recognize one? Two perfect squares with a *minus* between them. Then a is the square root of the first, b is the square root of the last, and it splits into (a+b)(a−b):

$$x^2-9=(x)^2-(3)^2=(x+3)(x-3)$$

Now the warning. A *sum* of squares, x²+9, with a *plus*, does not factor over the integers. Difference of squares needs the minus. You can see why with the unit's own multiply-back move: tempted to write (x+3)(x−3) for x²+9? Multiply it back and you get x²−9, a minus, so that product factors x²−9, never x²+9. The two-number search says the same thing: you'd need two numbers multiplying to +9 and adding to 0, and no integer pair does that. So x²+9 is prime.

Now the perfect-square trinomial. These are what you get when you square a binomial: (x+3)² works out to x²+6x+9. How do you recognize one? The first and last terms are both perfect squares, *and* the middle term equals 2 times the two square roots multiplied.

Check x²+6x+9: the square root of x² is x, the square root of 9 is 3, and 2·x·3 = 6x, which matches the middle, so it's (x+3)². The sign in the middle becomes the sign inside the parentheses: x²−10x+25 is (x−5)².

These two patterns are really just *special cases* of Lesson 11.2. For a perfect square the two numbers are equal, and for a difference of squares they're opposites. So the multiply-back check is the same one you already know, and it's just as mandatory here.

**New terms:**
- {#11.3.d1} **Perfect square:** a quantity that is something squared. 9=3², x²=(x)², 4x²=(2x)² are perfect squares; 7 and x are not.
- {#11.3.d2} **Difference of squares:** one perfect square *minus* another, a²-b².
- {#11.3.d3} **Perfect-square trinomial:** a trinomial that is exactly (a±b)² multiplied out.

In each example below, the recognition step comes first: confirm the pattern against the rule before writing the factors.

**Worked examples** (each checked by multiplying back):

*Difference of squares, basic:*
{#11.3.w1}
$$x^2-9=(x+3)(x-3) \qquad \text{Check: } x^2-3x+3x-9 = x^2-9$$

*Difference of squares, larger:*
{#11.3.w2}
$$x^2-25=(x+5)(x-5) \qquad \text{Check: } x^2-5x+5x-25 = x^2-25$$

*Difference of squares with a coefficient (4x²=(2x)²):*
{#11.3.w3}
$$4x^2-1=(2x+1)(2x-1) \qquad \text{Check: } 4x^2-2x+2x-1 = 4x^2-1$$

*Perfect-square trinomial (plus):*
{#11.3.w4}
$$x^2+6x+9=(x+3)^2 \qquad \text{Check: } (x+3)(x+3)=x^2+3x+3x+9 = x^2+6x+9$$
(√(x²)=x, √9=3, 2·x·3=6x.)

*Perfect-square trinomial (minus):*
{#11.3.w5}
$$x^2-10x+25=(x-5)^2 \qquad \text{Check: } (x-5)(x-5)=x^2-5x-5x+25 = x^2-10x+25$$
(√(x²)=x, √25=5, 2·x·5=10x; the minus makes it (x−5)².)

Four slips to watch for once the patterns are working for you.

The first is trying to factor a sum of squares, writing x²+9 as (x+3)(x−3); multiply your answer back and you'll see it gives x²−9, with a minus, so it's the wrong starting point. A sum of squares is prime over the integers.

The second is mistaking a near-miss for a perfect square: x²+5x+9 has square ends, but 2·x·3 = 6x, not 5x, so it is *not* (x+3)². When the middle doesn't equal twice the roots multiplied, fall back to the 11.2 search, and here that search comes up empty (pairs of 9: 1+9=10, 3+3=6, neither is 5), so x²+5x+9 is prime.

The third is dropping a coefficient's square root, writing 4x²−1 as (4x+1)(4x−1); the square root of 4x² is 2x, not 4x, and multiplying back shows it.

And the last is ignoring the middle sign in a perfect square, calling x²−10x+25 an (x+5)²; the middle sign carries inside, so it's (x−5)².

### Putting it together: GCF first, then the pattern

Here's where "always try the GCF first" pays off most. Pulling a common factor can turn a messy expression into a clean pattern that wasn't visible before, and forgetting to keep that GCF in your final answer is the classic "not fully factored" slip. Two worked-through examples, each done end to end.

*GCF, then a perfect square:*
{#11.3.w6}
$$2x^2+12x+18 \;=\; 2(x^2+6x+9) \;=\; 2(x+3)^2 \qquad \text{Check: } 2(x^2+6x+9)=2x^2+12x+18$$
Pull the 2, since every coefficient is even. The inside, x²+6x+9, is now a perfect square (√(x²)=x, √9=3, 2·x·3=6x). The 2 stays out front: 2(x+3)² is fully factored, and (x+3)² alone would be missing the 2.

*GCF, then a difference of squares:*
{#11.3.w7}
$$3x^2-12 \;=\; 3(x^2-4) \;=\; 3(x+2)(x-2) \qquad \text{Check: } 3(x+2)(x-2)=3(x^2-4)=3x^2-12$$
Pulling out 3 exposes x²−4, a difference of squares. Neither step was visible before the GCF came out, which is exactly why the GCF goes first.

So how do you know you're done? A factorization is finished only when no piece can be factored again. After each split, look at every factor and ask: can this one be factored? Is there a leftover difference of squares, a trinomial that still factors, a GCF you missed? Stop only when each piece is a single term, a prime trinomial, or a binomial that can't be broken down further.

**Check for understanding (transfer):**
1. {#11.3.c1} Is x²−16 a difference of squares? Factor it, then multiply back to prove it. (Yes: x² and 16 are both perfect squares with a minus between them, so it's (x+4)(x−4); multiplying back gives x²−4x+4x−16 = x²−16.)
2. {#11.3.c2} Can x²+16 be factored the same way? Why or why not? (No: that's a *sum* of squares, which is prime over the integers. (x+4)(x−4) would multiply back to x²−16, a minus, so it can't be the factoring of x²+16.)
3. {#11.3.c3} How do you tell x²+6x+9 (a perfect square) from x²+6x+8 (not one)? Factor each. (Check the middle against twice the roots: for x²+6x+9, 2·x·3 = 6x matches, so it's (x+3)². For x²+6x+8, the ends aren't a matching square pair, so run the two-number search: 2 and 4 multiply to 8 and add to 6, giving (x+2)(x+4).)

You can now spot a difference of squares and a perfect-square trinomial on sight, factor each one, recognize that a sum of squares is prime, and factor completely by pulling the GCF first and checking every remaining piece.

The order of attack worth carrying out of this unit, into Unit 12 and beyond: always pull the GCF first, then count the terms. Two terms means look for a difference of squares (and remember a sum of squares is prime). Three terms means glance for a perfect square and otherwise run the two-number search (and if no integer pair works, it's prime). Then factor completely, checking every piece, and multiply back every time.

The thread tying it all together is that factoring is multiplying backward, so Unit 10 is your answer key, which is what makes the check feel natural instead of like extra work. And you've already done the hard part for next unit: once x²+5x+6 is (x+2)(x+3), reading off the answers to a quadratic is one short step away.

**Practice problems:**

*Difference of squares:*
1. x²-9  2. x²-16  3. x²-25  4. x²-49  5. x²-1  6. 4x²-9  7. 9x²-1

*Perfect-square trinomials:*
8. x²+6x+9  9. x²-10x+25  10. x²+8x+16  11. x²-4x+4  12. x²+2x+1

*GCF first, then factor completely (each needs a common factor pulled before the pattern shows):*
13. 2x²+12x+18  14. 3x²-12  15. 2x²+10x+12

**Answer key (multiply each back):**
1) (x+3)(x-3)  2) (x+4)(x-4)  3) (x+5)(x-5)  4) (x+7)(x-7)  5) (x+1)(x-1)  6) (2x+3)(2x-3)  7) (3x+1)(3x-1)  8) (x+3)²  9) (x-5)²  10) (x+4)²  11) (x-2)²  12) (x+1)²
13) 2(x+3)²  14) 3(x+2)(x-2)  15) 2(x+2)(x+3)

*Spot-checks:* #6: (2x+3)(2x-3)=4x²-9. #10: 2·x·4=8x, so (x+4)². #11: middle -4x=2·x·(-2), so (x-2)². #13: 2(x+3)²=2(x²+6x+9)=2x²+12x+18 (keep the 2!). #14: 3(x²-4)=3x²-12.
