# Unit 12: Quadratic Functions & Equations (the capstone)

> This unit is about equations with a squared term, the kind that shape a thrown ball's arc or the size of a rectangle. They are worth learning because they show up everywhere a quantity grows and then turns back, and because solving them ties together a lot of what you've already done. It helps to have a little practice with squaring numbers fresh in mind before you start.

This unit pulls together most of what came before. It rests on one small, steady idea that you'll meet in the very first lesson and then see everywhere: squaring throws away a sign. Once that idea is in your hands, a few surprises ahead all turn out to be the same fact wearing different clothes.

Those surprises are that a squared equation usually has two answers, that a little ± sign shows up in every method, and that the graph is a U shape. They are one idea, not three separate rules.

<!--viz:reference_cards#1-->

A word before you start, and it holds for every lesson here. You don't have to finish a lesson in one sitting. If a page stops landing, take a break and come back. A rest helps, and you lose nothing. And when you return for a new lesson, redo two or three problems from a lesson or two back from memory first. That small warm-up is one of the most useful habits you can keep.

---

## Lesson 12.1: Square roots & simplifying radicals

Here's a picture to start from. A square has area 9. What's the length of one side? You're looking for a number that, multiplied by itself, gives 9. That's 3, because 3 × 3 = 9. Squaring a number asks "what's the area of a square with this side?" The **square root** asks the reverse: "the area is 9, so what's the side?" That reverse question is the idea of this lesson, and it's the exact tool you'll need later to undo an x². Without it, the answer to x² = 7 would have no name to write down.

<!--illus:12-1-area-to-side-->

Squaring and taking a square root undo each other, the same way the 2 power and the root sit on opposite sides of the move. So √9 = 3 because 3² = 9, and √25 = 5 because 5² = 25. When the number under the root is a perfect square, meaning some whole number squared, the root comes out as a tidy whole number.

But not every number is that friendly. √9 is a clean 3, yet √7 is **irrational**: its decimal runs on forever without ever repeating, so no fraction lands exactly on it. That doesn't make √7 unfinished or wrong. √7 *is* the exact answer, the same way 1/3 is exact even though its decimal never stops.

A whole number system holds numbers like these, fractions, and the radicals alongside the plain whole numbers. Reach for a rounded decimal like 2.6457 only when a problem actually asks for one. Otherwise the radical is the finished, honest answer.

When a radical isn't a perfect square, you can often make it simpler without rounding it at all. The move is to split the number under the root into a perfect-square factor times whatever is left. The perfect square can then step outside the root:

$$\sqrt{12}=\sqrt{4\cdot 3}=\sqrt4\,\sqrt3=2\sqrt3$$

Read that left to right: 12 is 4 times 3, the √4 becomes a plain 2 out front, and the √3 stays behind because 3 has no perfect-square factor to give up. One tip that saves steps: hunt for the *largest* perfect-square factor. If you pull out 4 from √72 you get 2√18 and you're not done. Pull out 36 and you land on 6√2 in one step. Either route reaches the same place. Pulling the largest just gets there fastest.

Read each worked example slowly, one line at a time, and ask why each line follows from the one above before you go on. That's what makes a worked example teach.

**New terms:**
- {#12.1.d1} **Square root (√( )):** the inverse of squaring. √9=3 because 3²=9. The symbol gives the **principal (non-negative) root**: √9 is 3, not -3. (We restore the second sign by hand in 12.2 with ±.)
- {#12.1.d2} **Radical / radicand:** the √( ) is the *radical*; the number under it is the *radicand*.
- {#12.1.d3} **Perfect square:** a number that's some integer squared, like 1,4,9,16,25,36,49,...
- {#12.1.d4} **Simplified radical:** no perfect-square factor left under the root. √12=√(4·3)=2√3 is simplified; √12 is not.
- {#12.1.d5} **Like radicals:** radicals with the *same* radicand (2√3 and 4√3). They add like the "boxes" of like terms: 2 of a thing plus 4 of the same thing is 6 of it.

**Worked examples:**

1. √50=√(25·2)=√25 √2=5√2. Here 50 is 25 times 2, and 25 is the largest perfect square hiding inside, so the √25 steps out as 5 and the √2 stays.
2. √18=√(9·2)=3√2. The perfect square is what comes *out*: 9 becomes a 3 in front. So write the split as 9·2, not 2·9, to keep the square in plain view.
3. **Add like radicals:** 2√3+4√3=6√3. Same radicand, so add the counts, exactly like 2x+4x=6x. (You *cannot* combine 2√3+4√2; unlike radicals, like unlike terms.)
4. **Multiply radicals:** √2·√3=√(2·3)=√6. And √5·√5=√25=5 (a root times itself undoes the square).
5. **Rationalize a denominator (lightly):** a radical in the denominator is usually rewritten without one. Multiply top and bottom by √2:
$$\frac{1}{\sqrt2}=\frac{1}{\sqrt2}\cdot\frac{\sqrt2}{\sqrt2}=\frac{\sqrt2}{2}.$$
This "multiply by the radical over itself" trick is for a *single* radical in the denominator. Denominators like 2+√3 come later (Intermediate Algebra) and use a different move (the conjugate), so don't over-generalize this one.

One more, one power up, so you've seen it: a cube root undoes cubing. ∛27 = 3 because 3³ = 27. Same idea, just the 3 power instead of the 2.

Here's a clean case to get the method moving before the practice mixes things up. Simplify √20. It's 4 times 5, and 4 is a perfect square, so √20 = √(4·5) = 2√5. One factor out, one left behind. That's the whole move.

Two slips are worth naming now that you've done a few correctly. The first: treating √7 as a mistake and reaching for 2.6457. It isn't a mistake. It's the exact number, in the same family as 1/3, whose decimal also never stops. The cure is to leave the radical alone unless a decimal is asked for.

The second: stopping before the radical is fully simplified, like writing √72 = 2√18 and walking away. There's still a perfect square (9) hiding under that √18. A quick self-check after any simplify: ask "is there *still* a perfect-square factor inside?" If yes, keep pulling: √72 = 2√18 = 2·3√2 = 6√2, until none is left. (One radicand won't combine with a different one, by the way: √2 + √3 isn't √5, the same reason 2x + 3y won't fold into one term.)

**Check for understanding (transfer):**
1. {#12.1.c1} Simplify √45, and say how you knew which factor to pull out. (√45 = √(9·5) = 3√5; you look for the largest perfect-square factor, and 9 is a perfect square that divides 45 while 5 has none left to give.)
2. {#12.1.c2} Is √10 a "finished" answer? Say how it's like 1/3 and unlike √9. (Yes, it's finished. √10 is irrational, an exact number whose decimal never settles, just like 1/3 is exact even though its decimal repeats forever. It's unlike √9, which lands on the whole number 3.)
3. {#12.1.c3} Why can you combine 5√2 + 3√2 but not 5√2 + 3√3? (The first pair shares the radicand √2, so you add the counts to get 8√2, like 5x + 3x. The second pair has different radicands, so there's nothing matching to add, just as 5x + 3y stays apart.)

You can now read √( ) as the side of a square with a given area, simplify a radical by pulling out its largest perfect-square factor, add radicals that share a radicand, and treat an irrational root as the exact answer it is.

Mixed practice feels harder than repeating one kind of problem, and that's the point. It's what makes a skill last to next week. Every problem below has its answer at the end of the lesson, and if one stalls you, flip back to the worked example it's based on. That's what it's there for.

**Practice problems:**
*Evaluate (perfect squares & cube root):*
1. √16
2. √49
3. √100
4. ∛27
*Simplify:*
5. √8
6. √20
7. √45
8. √72
9. √48
10. √75
*Add / multiply / rationalize:*
11. 3√5+√5
12. √2·√8
*Locate between two consecutive integers (keep the exact radical):*
13. √45 is between which two consecutive integers?
14. √10 is between which two consecutive integers?

**Answer key:**
1. 4 · 2. 7 · 3. 10 · 4. 3 · 5. √(4·2)=2√2 · 6. √(4·5)=2√5 · 7. √(9·5)=3√5 · 8. √(36·2)=6√2 · 9. √(16·3)=4√3 · 10. √(25·3)=5√3 · 11. 4√5 · 12. √16=4 · 13. between **6 and 7** (36<45<49) · 14. between **3 and 4** (9<10<16).

---

## Lesson 12.2: The simplest quadratics (x²=9 → two solutions)

Here's the surprise that runs through the rest of the unit, in its plainest form. The equation x² = 9 asks: what number, squared, gives 9? Try 3: yes, 3² = 9. But now try −3: (−3)² is also 9. Two different starting numbers, one ended-up answer. Squaring *lost the sign*: it threw away whether you began on the positive side or the negative side, so both 3 and −3 are honest answers, and you have to report both.

That one fact, squaring loses the sign, is the whole unit in a sentence. It's why a quadratic usually has *two* solutions, why a little ± shows up in every method ahead, and (in the last lesson) why the U-shaped graph crosses the axis twice. Keep it in mind and the rest will feel like one idea, not a pile of separate rules.

So to solve x² = 9 you take the square root of both sides, but you write the ± yourself to put back the sign that squaring erased:

$$x^2=9\;\Rightarrow\; x=\pm\sqrt9=\pm3.$$

That ± is just shorthand for "two answers at once": x = ±3 means x = 3 or x = −3 {#12.2.f1}. This whole move has a name, the **Square-Root Property**, and it has two branches, depending on the sign of the number you're taking the root of.

When that number is zero or positive, you get the two roots (collapsing to a single x = 0 when the number is 0). When it's negative, there's no real solution at all, because no real number squared can land on a negative. That second branch isn't a special exception to patch over later. It's half of the rule, and you'll lean on it again before the unit is out.

The negative branch is worth seeing once now so it doesn't rattle you later. Take x² = −4. No real number squared gives −4, because every real square is zero or positive (2² = 4 and (−2)² = 4; nothing real reaches −4). So the answer is "no real solution," and that *is* the answer. It's a finished, correct result, not a sign you did something wrong.

Two practical notes before the examples. First, isolate the x² *before* you take a root. If you see 2x² = 50, divide by 2 first to get x² = 25, then root to get x = ±5. Don't root the whole thing while the 2 is still attached. Second, when the number isn't a perfect square, the answer stays in radical form, exactly as in Lesson 12.1: x² = 7 gives x = ±√7, and that's exact and done.

**New terms:**
- {#12.2.d1} **±("plus or minus"):** shorthand for *two* answers at once. x=±3 means x=3 **or** x=-3.
- {#12.2.d2} **Quadratic equation:** an equation with an x² term (and no higher power). Standard form is ax²+bx+c=0 with a≠0. These are the special case where b=0.
- {#12.2.d3} **Square-Root Property (the rule of this lesson, worth boxing):** for x²=k,
  - **if k≥0, then x=±√k** (i.e. x=√k or x=-√k, two real solutions, collapsing to the single x=0 when k=0);
  - **if k<0, there is no real solution** (no real number squares to a negative).

  Stated once, conditional and complete: *x²=k ⇒ x=±√k when k≥0; no real solution when k<0.* The k<0 branch is not a side-exception to patch later. It is half of the rule, and it returns in 12.5 as the discriminant's sign.

**Worked examples:**

1. x²=9 ⇒ x=±3, i.e. x=3 or x=-3. Check both: 3²=9, (-3)²=9. Both starting numbers square to 9, which is exactly why both are answers.
2. x²=16 ⇒ x=±4. Same move: 16 is 4², so the two roots are 4 and −4.
3. x²-7=0 ⇒ x²=7 ⇒ x=±√7 (exact, irrational, *not* "unfinished," per 12.1). Add 7 to both sides to isolate x², then root; 7 isn't a perfect square, so √7 stays.
4. 2x²=50 ⇒ x²=25 ⇒ x=±5. (Isolate x² **first**, dividing by 2, before rooting.) If you rooted before dividing you'd drag along an extra radical and land on ±5√2, which is wrong here.
5. x²-3=0 ⇒ x²=3 ⇒ x=±√3. Isolate, then root; 3 isn't a perfect square, so leave the radical.
6. **The k<0 branch (no real solution):** x²=-4. Here k=-4<0. By the Square-Root Property there is **no real solution**, because no real number squares to -4, since any real square is ≥0. (Check the intuition: 2²=4 and (-2)²=4; nothing real lands on -4.) The answer is "no real solution," full stop. Same for x²+4=0 ⇒ x²=-4: isolate first, see the negative, stop.

The substitution check above is how you'll know you're right when no one's there to tell you. If you put an answer back and the two sides *don't* match, you haven't failed. Your check just did its job and caught something before it counted. Go back to your first step and re-run the arithmetic slowly; a mismatch is almost always one sign or one small slip, not the whole method.

Here's a clean one to get the rhythm before the set turns mixed: solve x² = 1. The square root of 1 is 1, so x = ±1, meaning x = 1 or x = −1. Check: 1² = 1 and (−1)² = 1. Both land, both count.

One slip deserves a callout now that you've done several correctly: writing only x = 3 for x² = 9 and stopping. That's the most natural mistake here, and it comes from forgetting that squaring hid a sign. The fix is built into the method. Whenever you undo a square, write the ± first, before you fill in the number, so the second root can't slip away. (And if isolating ever leaves you with x² equal to a negative, don't force a ± onto it; the negative branch already told you the honest answer is "no real solution.")

**Check for understanding (transfer):**
1. {#12.2.c1} Solve x² = 49. How many answers, and why isn't it just one? (x = ±7, so two answers, x = 7 or x = −7, because both 7² and (−7)² equal 49; squaring lost the sign, so both starts are valid.)
2. {#12.2.c2} A friend says x² = 20 has answer x = √20. What did they leave out, and can you simplify the radical too? (They left out the negative root: it's x = ±√20. And √20 = √(4·5) = 2√5, so the full answer is x = ±2√5.)
3. {#12.2.c3} Solve 3x² = 27. What has to happen *before* you take a square root? (Divide both sides by 3 to isolate x², giving x² = 9, and only then root: x = ±3. Isolating the x² comes first.)

You can now solve x² = k by isolating the x², writing the ± to keep both signs when k is zero or positive, and recognizing "no real solution" as the correct, finished answer when k is negative.

Mixed practice feels harder, and that's the point. It's what makes this stick. Every problem has its answer at the end of the lesson; if one stalls you, flip back to the worked example it's based on.

**Practice problems:**
*Solve (keep both signs; leave irrationals exact):*
1. x²=25
2. x²=49
3. x²=1
4. x²-11=0
5. x²-2=0
6. 3x²=27
7. 5x²=45
8. 2x²=18
9. x²-100=0
10. x²=5
*No real solution (the k<0 branch). State it and say why:*
11. x²=-9
12. x²+16=0

**Answer key:**
1. x=±5 · 2. x=±7 · 3. x=±1 · 4. x²=11, x=±√11 · 5. x²=2, x=±√2 · 6. x²=9, x=±3 · 7. x²=9, x=±3 · 8. x²=9, x=±3 · 9. x²=100, x=±10 · 10. x=±√5 · 11. **no real solution** (k=-9<0; no real number squares to -9) · 12. x²=-16, **no real solution** (k=-16<0).

---

## Lesson 12.3: Solving by factoring (zero-product property)

Start with something you already trust about multiplying. If you multiply two numbers and the result is 0, one of them *had* to be 0. There's no other way to reach zero. Two non-zero numbers never multiply to zero. That small, obvious fact is the engine of this lesson.

Turn it on an equation. Suppose (x − 2)(x − 3) = 0. You've got two things multiplied together giving 0, so one of them must be 0: either x − 2 = 0 or x − 3 = 0. Each of those is a little one-step equation you can solve: x = 2 from the first, x = 3 from the second. So the quadratic has two solutions, 2 and 3, and you found them by reading off the factors {#12.3.f1}. This is the **zero-product property**, and it's the everyday method for the many quadratics that factor.

<!--viz:example_graphs#1-->

The one thing to hold onto: this trick works *only against zero*. Zero is special. It's the single value a product can reach only by one of its parts being zero. A product equal to 8 tells you nothing useful about the factors, because lots of pairs multiply to 8. So the first move, always, is to get the equation into the form (something) = 0, with everything on one side.

Each factor-equals-zero gives a genuine solution, not just a candidate. Here's why: the property runs both ways. Forward: if the product is 0, some factor is 0, and that's what finds your x-values. Backward: if a factor *is* 0, then the whole product is 0, so that x truly makes the equation true. The substitution check at the end is exactly that backward direction confirming the root is real.

And the factoring step itself is the reverse-distribute, area-box move from Unit 11, run to find the edges; once you've got the factors, each one set to zero is its own tiny equation.

So the procedure has four beats: get one side to 0 in the form ax² + bx + c = 0, factor the quadratic (Unit 11), set each factor equal to 0, and solve each little equation.

**New terms:**
- {#12.3.d1} **Zero-product property:** if a product equals 0, then *at least one* factor is 0. If A·B=0, then A=0 or B=0. (No other number forces a product to zero; this is special to 0.)
- {#12.3.d2} **Root / solution:** a value of x that makes the equation true. These are the same "roots" that are x-intercepts in 12.6.

**Worked examples:**

1. (x-2)(x-3)=0. Already factored and equal to 0. Set each: x-2=0 ⇒ x=2; x-3=0 ⇒ x=3. **x=2 or x=3.** Check: (2-2)(2-3)=0·(-1)=0. The first factor went to zero, which is enough to make the whole product zero.
2. x²-5x+6=0. Factor first (what multiplies to +6, adds to -5? -2,-3): (x-2)(x-3)=0 ⇒ x=2 or 3. Same two roots as #1, reached by factoring before reading them off.
3. x²+x-6=0. (Multiply to -6, add to +1: +3,-2.) (x+3)(x-2)=0 ⇒ x=-3 or 2. Notice x+3=0 gives x=-3, not +3: the factor and its root carry opposite signs.
4. x²-9=0. Difference of squares (Unit 11.3): (x-3)(x+3)=0 ⇒ x=±3. (Same answer 12.2 gives: two routes, one truth.)
5. **Must equal 0 first:** x²-5x=-6 is *not* ready. Move the -6 over: x²-5x+6=0, then factor as in #2 → x=2,3. Setting factors of x²-5x=-6 to numbers is meaningless, because the zero-product property only works against 0.

Here's a clean case to settle the method before the set mixes things up: x² − x = 0. Both terms share an x, so factor it out: x(x − 1) = 0. Then x = 0 or x − 1 = 0, giving x = 0 or x = 1. Check: 0² − 0 = 0, and 1² − 1 = 0. Two roots, and one of them is zero itself, which is perfectly allowed.

Now that several are solved, two slips are worth a word. The first is setting factors equal to the wrong number, factoring x² − 5x + 6 = 8 and writing x − 2 = 8. The property needs a zero on the other side; an 8 gives you nothing, so move everything over first to make that side 0.

The second is stopping after one factor, reporting x = 2 and forgetting x = 3. Each factor is its own equation and (usually) its own root, so finish both: two factors, two answers. (If your factoring ever feels shaky, you can always check it by expanding the factors back out, or by substituting a root into the original; both catch a sign error at the factoring step.)

**Check for understanding (transfer):**
1. {#12.3.c1} Solve (x + 5)(x − 1) = 0 without expanding. What lets you split it into two easy equations? (The zero-product property: the product is 0, so a factor is 0. That means x + 5 = 0 or x − 1 = 0, giving x = −5 or x = 1.)
2. {#12.3.c2} A solution factors x² − 2x − 8 = 0 into (x − 4)(x + 2) and stops at x = 4. What's missing? (The second factor: x + 2 = 0 gives x = −2, so the full answer is x = 4 or x = −2. Each factor yields a root.)
3. {#12.3.c3} Why must x² − 3x = 10 be rewritten as x² − 3x − 10 = 0 before factoring to solve? (Because the zero-product property only works when the product equals 0. Against 10 the factors tell you nothing; moving the 10 over makes the right side 0 so the property applies.)

You can now solve a quadratic that factors by getting one side to 0, factoring it, setting each factor to 0, and solving. Then check by putting a root back in.

Mixed practice feels harder, and that's what makes it last. Every problem's answer is at the end of the lesson; if one stalls you, flip back to the worked example it's based on.

**Practice problems:**
*Solve (already factored):*
1. (x-1)(x-4)=0
2. (x+5)(x-2)=0
*Factor, then solve:*
3. x²-7x+12=0
4. x²+5x+6=0
5. x²-2x-8=0
6. x²+7x+10=0
7. x²-x-12=0
8. x²-8x+15=0
9. x²+3x=0  *(GCF: x(x+3))*
*Special patterns:*
10. x²-16=0
11. x²-6x+9=0  *(perfect square)*
12. x²-3x-10=0

**Answer key:**
1. x=1,4 · 2. x=-5,2 · 3. (x-3)(x-4), x=3,4 · 4. (x+2)(x+3), x=-2,-3 · 5. (x-4)(x+2), x=-2,4 · 6. (x+2)(x+5), x=-2,-5 · 7. (x-4)(x+3), x=-3,4 · 8. (x-3)(x-5), x=3,5 · 9. x(x+3), x=0,-3 · 10. (x-4)(x+4), x=±4 · 11. (x-3)², x=3 (one repeated root) · 12. (x-5)(x+2), x=-2,5.

---

## Lesson 12.4: Completing the square

Start with a fact you can check by hand: (x + 3)² = x² + 6x + 9. Look at that constant, the 9. It's exactly (6/2)², half of the middle coefficient, squared. That's not a coincidence, and it's the lever for this whole lesson. If you're handed x² + 6x and want to *make* it into a perfect square, you now know precisely what to add: 9. Adding the right number to turn x² + bx into something-squared is called **completing the square**.

There's a literal picture behind the name. Think of x² + 6x as an x-by-x square sitting next to two strips, each 3 by x (the 6x split into two 3x pieces laid along two sides). Those pieces almost form a bigger square, but there's a corner missing: a 3-by-3 block, area 9. Drop that block in and the figure becomes a complete square, (x + 3) on each side. The algebra is doing the same thing the picture is: filling in the missing corner.

<!--viz:area_models#4-->

Why bother? Two reasons. It solves quadratics that won't factor with nice integers, and it's where the quadratic formula in the next lesson actually comes from. Seeing it once makes that formula feel earned instead of dropped on you.

The move itself, on an equation, is short. Get the x² and x terms alone on one side, add (b/2)² to *both* sides so the two sides stay equal, factor the left side as a square, and finish with the ±√( ) of Lesson 12.2. Watch the worked examples for how both sides are kept equal on every line.

**New terms:**
- {#12.4.d1} **Perfect-square trinomial:** a trinomial that factors as something squared, like x²+6x+9=(x+3)² (Unit 11.3).
- {#12.4.d2} **Completing the square:** adding the exact number, (b/2)², that turns x²+bx into a perfect square.

**Worked examples:**

1. x²+6x+5=0. First move the constant aside and add (6/2)²=9 to both sides to build a perfect square on the left:
$$x^2+6x=-5 \;\xrightarrow{+\,(6/2)^2=9}\; x^2+6x+9=-5+9 \;\Rightarrow\; (x+3)^2=4$$
$$x+3=\pm2 \;\Rightarrow\; x=-3\pm2 \;\Rightarrow\; x=-1 \text{ or } x=-5.$$
Adding 9 to both sides keeps the equation balanced, the left collapses to (x+3)², and the ± at the root step recovers both solutions. Check: (-1)²+6(-1)+5=0, (-5)²+6(-5)+5=0.

2. x²+4x-5=0. Move: x²+4x=5. Add (4/2)²=4 to both sides: (x+2)²=9 ⇒ x+2=±3 ⇒ x=1 or -5. Half of 4 is 2, squared is 4, and that's the number that completes the square.

3. x²-2x-3=0. Move: x²-2x=3. Add (-2/2)²=1 to both sides: (x-1)²=4 ⇒ x-1=±2 ⇒ x=3 or -1. Note half of -2 is -1, so the square is (x-1)², minus sign and all.

4. **Where it earns its keep (factoring fails):** x²-4x+1=0. Move: x²-4x=-1. Add (-4/2)²=4 to both sides: (x-2)²=3 ⇒ x-2=±√3 ⇒ x=2±√3. No integer factoring could have found this, but completing the square does, and the answer stays exact in radical form.

A clean case to lock the move in before the practice: complete the square on x² + 6x (just the expression, no equation to solve). Half of 6 is 3, and 3² = 9, so you add 9, giving x² + 6x + 9 = (x + 3)². That's the heart of every example above, on its own.

You've worked the move; here are the spots people stumble. The most common is adding (b/2)² to only one side, which quietly changes the equation and breaks the answer; whatever you add on the left you must add on the right, to keep the balance.

The next is forgetting to halve before squaring, adding b² instead of (b/2)²; the tell is that the left side won't fold into a clean square, so the rule is *half of b first, then square*.

And the unit's usual one returns at the root step: write the ± so x + 3 = ±2 instead of just x + 3 = 2, or you'll lose the second root. (When b is negative, halving carries the sign: half of −2 is −1, so the square is (x − 1)², not (x + 1)².)

**Check for understanding (transfer):**
1. {#12.4.c1} To complete the square on x² + 10x, what number do you add, and how did you get it? (You add 25: half of 10 is 5, and 5² = 25. That makes x² + 10x + 25 = (x + 5)².)
2. {#12.4.c2} Solve x² + 8x + 7 = 0 by completing the square. Show the balanced step on both sides. (Move: x² + 8x = −7. Add (8/2)² = 16 to both sides: x² + 8x + 16 = −7 + 16, so (x + 4)² = 9. Then x + 4 = ±3, giving x = −1 or x = −7.)
3. {#12.4.c3} Why does completing the square solve x² − 4x + 1 = 0 when factoring can't? (No two integers multiply to 1 and add to −4, so it won't factor over the integers. Completing the square doesn't need integer factors. It builds (x − 2)² = 3 directly, giving the exact roots x = 2 ± √3.)

You can now complete the square on x² + bx by adding (b/2)² to both sides, factor the result, and solve with the ±. You've also seen why this is the method that still works when factoring can't.

Mixed practice feels harder on purpose, and that's what makes it last. Every answer is at the end of the lesson; if one stalls you, flip back to the worked example it's based on.

**Practice problems:**
*State the number that completes the square for:*
1. x²+6x
2. x²-10x
*Solve by completing the square:*
3. x²+8x+7=0
4. x²-6x+8=0
5. x²+2x-8=0
6. x²-2x-3=0

**Answer key:**
1. (6/2)²=9 · 2. (-10/2)²=25 · 3. x²+8x=-7; +16: (x+4)²=9; x=-4±3; x=-1,-7 · 4. x²-6x=-8; +9: (x-3)²=1; x=3±1; x=2,4 · 5. x²+2x=8; +1: (x+1)²=9; x=-1±3; x=2,-4 · 6. x²-2x=3; +1: (x-1)²=4; x=1±2; x=3,-1.

---

## Lesson 12.5: The quadratic formula & the discriminant

Factoring is quick when it works, and completing the square always works but is fiddly to redo every time. The quadratic formula is the way out: it's completing the square done *once, in general*, so you never have to grind through it again. You just read the three numbers a, b, and c off the equation and drop them in. It solves *every* quadratic, factorable or not, with rational answers or irrational ones. That's why it's the universal tool.

<!--viz:flowcharts#2-->

For any quadratic written as ax² + bx + c = 0,

$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}.$$

That ± is the same one from every lesson in this unit: it's recovering the sign that squaring threw away. To use the formula well, read a, b, and c carefully, *with their signs*: for 2x² + 3x − 2 = 0, a = 2, b = 3, and c = −2, where the minus belongs to the c.

Here's where the 2a on the bottom comes from, if you're curious. The general derivation first divides everything by a so the x² coefficient becomes 1, then completes the square (Lesson 12.4), and that division is exactly what leaves the 2a in the denominator. You don't have to redo it; the formula already did.

There's a bonus tucked inside the formula. The part under the root, b² − 4ac, is the **discriminant**, and its *sign* tells you how many real solutions you'll get before you finish the arithmetic.

If it's positive, the root of a positive number gives two different values, so two real solutions {#12.5.f1}. If it's zero, the ± adds and subtracts nothing, so the two solutions collapse into one (a repeated root). If it's negative, there's no real square root to take, so no real solution. That negative case is the same "no real solution" branch you met in Lesson 12.2, now showing up as the sign of the discriminant.

One refinement when the discriminant is positive, worth knowing because it explains a pattern you've already seen. If b² − 4ac is itself a perfect square, the root comes out whole and the two answers are *rational*, which means the quadratic would have factored over the integers (the Lesson 12.3 case). If it's positive but not a perfect square, the answers keep a radical and are *irrational*.

That's exactly why some quadratics factor cleanly and others only yield to the formula. (For instance: x² − 3x − 10 = 0 has discriminant 49 = 7², so rational roots 5 and −2; x² − 2x − 5 = 0 has discriminant 24, so irrational roots 1 ± √6.)

The working order is steady: substitute a, b, c; simplify the discriminant first; then take its root and resolve the ±. Then check a root by putting it back in.

**New terms:**
- {#12.5.d1} **Quadratic formula:** for ax²+bx+c=0 (with a≠0),
$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}.$$
The ± is the same two-solutions ± as always, recovering the sign squaring destroyed.
- {#12.5.d2} **Discriminant:** the inside-the-root part, b²-4ac. For a real quadratic (a≠0, real coefficients) its **sign** counts the real solutions before you finish:
  - b²-4ac>0: **two** real solutions (root of a positive → ± two values).
  - b²-4ac=0: **one** real solution, a **repeated (double) root** (±0 collapses to one; the parabola's vertex sits on the axis).
  - b²-4ac<0: **no real** solution (no real square root of a negative; the parabola misses the axis).
  - *One refinement when b²-4ac>0 (optional, real-only):* a **perfect-square** discriminant means the two roots are **rational**, because the √ comes out whole, so the quadratic factored over the rationals (the 12.3 case). A **non-perfect-square** discriminant means the two roots are **irrational**, keeping a radical (12.5's payoff, e.g. 1±√6). This is exactly *why* some quadratics factor cleanly and others only yield to the formula. (Concretely: x²-3x-10=0 has discriminant 49=7², rational roots 5,-2; x²-2x-5=0 has discriminant 24, irrational roots 1±√6.)

**Worked examples:**

1. x²-5x+6=0: a=1,b=-5,c=6. Discriminant (-5)²-4(1)(6)=25-24=1>0 → two solutions. Note -b is +5 here because b is -5, and (-5)² is +25.
$$x=\frac{-(-5)\pm\sqrt1}{2}=\frac{5\pm1}{2}=\{3,\,2\}.$$
(Matches the factoring answer from 12.3; every method agrees.)

2. 2x²+3x-2=0: a=2,b=3,c=-2. Discriminant 3²-4(2)(-2)=9+16=25 → two. Watch the -4ac: with c negative, -4(2)(-2) *adds* 16.
$$x=\frac{-3\pm\sqrt{25}}{4}=\frac{-3\pm5}{4}=\left\{\tfrac{2}{4}=\tfrac12,\ \tfrac{-8}{4}=-2\right\}.$$

3. x²-4x+4=0: a=1,b=-4,c=4. Discriminant (-4)²-4(1)(4)=16-16=0 → **one** solution.
$$x=\frac{4\pm\sqrt0}{2}=\frac{4}{2}=2.$$
(A repeated root: the perfect square (x-2)²=0. The ± adds nothing because √0 is 0.)

4. x²+x+1=0: a=1,b=1,c=1. Discriminant 1²-4(1)(1)=1-4=-3<0 → **no real solution** (can't take a real square root of -3). We stop here, and that's the finished, correct answer.

A clean one to settle the formula before the set mixes things up: solve x² − 5x + 4 = 0. Here a = 1, b = −5, c = 4, so the discriminant is (−5)² − 4(1)(4) = 25 − 16 = 9, a perfect square, so expect two rational roots. Then x = (5 ± √9)/2 = (5 ± 3)/2, giving x = 4 or x = 1. Check: 4² − 5(4) + 4 = 0, and 1² − 5(1) + 4 = 0.

Now the slips this formula invites, named after a few clean runs. The biggest by far is −b when b is already negative: −b means *the opposite of* b, so if b = −5 then −b = +5, not −5.

Next, sign errors in the discriminant, especially −4ac when c is negative, which makes that piece *add* (as in example 2). And remember that b² is always positive even when b is negative ((−5)² = 25; this is the same care as telling −3² from (−3)²).

Another is dividing only part of the top by 2a: the entire −b ± √( ) sits over 2a, so keep the fraction bar running full width. And the negative-discriminant result, "no real solution," is a real and correct finding, not a mistake to fix; the graph in the next lesson will show the U missing the axis entirely.

If a check ever comes out wrong, that's the safety net working, not a verdict. Re-run the arithmetic from the first step. Most often it's a single sign, the −b or one piece of the discriminant, that slipped.

**Check for understanding (transfer):**
1. {#12.5.c1} Use the formula on x² − 2x − 5 = 0. What's the discriminant, and what does its sign tell you before you finish? (a = 1, b = −2, c = −5; discriminant (−2)² − 4(1)(−5) = 4 + 20 = 24 > 0, so two real solutions, and since 24 isn't a perfect square they'll be irrational. Finishing: x = (2 ± √24)/2 = 1 ± √6.)
2. {#12.5.c2} Without solving, how many real solutions does x² + x + 5 = 0 have? How can you tell? (Discriminant 1² − 4(1)(5) = 1 − 20 = −19 < 0, so no real solutions. A negative discriminant means there's no real square root to take.)
3. {#12.5.c3} In 2x² − 7x + 3 = 0, what are a, b, and c, signs included, and what is −b? (a = 2, b = −7, c = 3; and −b = −(−7) = +7. The sign travels with each number.)

You can now solve any quadratic with the formula by reading off a, b, c with their signs, simplifying the discriminant first, and resolving the ±. And you can read the discriminant's sign to know how many real solutions to expect, and whether they're rational or irrational.

Mixed practice feels harder on purpose, and that's what makes it last to next week. Every answer is at the end of the lesson; if one stalls you, flip back to the worked example it's based on.

**Practice problems:**
*Find the discriminant and state the number of real solutions:*
1. x²-3x-10=0
2. x²+6x+9=0
3. x²+x+5=0
4. x²-6x+10=0
*Solve with the quadratic formula:*
5. x²-5x+6=0
6. 2x²+3x-2=0
7. x²-4x+4=0
8. 3x²-5x-2=0
9. 2x²-7x+3=0
10. x²-2x-5=0  *(irrational roots: leave exact)*

**Answer key:**
1. 9+40=49>0, two solutions (x=5,-2) · 2. 36-36=0, one solution (x=-3) · 3. 1-20=-19<0, **no real solutions** · 4. 36-40=-4<0, **no real solutions** · 5. (5±√1)/2=3,2 · 6. (-3±√25)/4=1/2,-2 · 7. (4±√0)/2=2 · 8. (5±√49)/6=(5±7)/6=2,-1/3 · 9. (7±√25)/4=(7±5)/4=3,1/2 · 10. (2±√24)/2=1±√6.

---

## Lesson 12.6: Graphing parabolas

Here's the picture the whole unit has been pointing at. A quadratic, graphed, is a smooth U, called a **parabola**. The solutions you've been finding are where that U crosses the x-axis, and a U usually crosses *twice*: once on the way down, once on the way back up. There are your two solutions, drawn.

<!--viz:interactive_graph#2-->

When a quadratic has just one solution, the U barely touches the axis at its lowest point (the discriminant was 0). When it has none, the whole U floats clear of the axis, above it or below it (the discriminant was negative). The graph re-explains everything from Lesson 12.5 in one image.

That's the deep reason a quadratic usually has two solutions, and it ties the unit together: radicals, roots, the discriminant, and now the curve are all the same story. A quadratic is also just a function from Units 4 and 5: y = x² − 4 and f(x) = x² − 4 are the same object, and the "roots" are simply the inputs where the output is 0, which is where the graph meets the x-axis.

To draw one well, work from numbers rather than guessing the shape. Pick a handful of x-values, compute the matching y for each, plot the points, and join them into a smooth U. The example below shows the line through those points {#12.6.f1}, with the roots and vertex marked, alongside the table the curve was built from.

Three features tell you most of what you need. The **direction** comes from the sign of a: a > 0 opens up (a valley), a < 0 opens down (a hill). The **roots** are where y = 0; solve the quadratic by any method from 12.3 to 12.5. The **vertex** is the turning point, the bottom of a valley or top of a hill; its x-coordinate is x = −b/(2a), and you plug that back in for its y.

One handy check: when there are two real roots, the vertex sits exactly halfway between them, so the average of the roots gives the vertex's x. That follows from the U being a mirror image across the vertical line through its vertex, the **axis of symmetry**. The −b/(2a) formula stays the general tool, though; it works even when the roots are irrational or absent.

**New terms:**
- {#12.6.d1} **Parabola:** the U-shaped graph of a quadratic y=ax²+bx+c.
- {#12.6.d2} **Roots / x-intercepts:** where the parabola crosses the x-axis, exactly the solutions of ax²+bx+c=0 (Lessons 12.3 to 12.5). This is *why* a quadratic usually has two.
- {#12.6.d3} **Vertex:** the turning point (bottom of the U if it opens up, top if down). Its x-coordinate is x=-b/2a.
- {#12.6.d4} **Axis of symmetry:** the vertical line x=-b/2a through the vertex; the parabola is a mirror image across it.
- {#12.6.d5} **Opens up / down:** **up if a>0**, **down if a<0**.

**Worked examples:**

1. y=x²-4 (here a=1,b=0,c=-4). Read it feature by feature. Direction: a=1>0, so it opens **up**. Roots: set y=0, so x²-4=0 ⇒ x=±2, crossing at (-2,0) and (2,0). Vertex: x=-0/2=0, and y=0²-4=-4, so (0,-4). Now compute a small table and plot it:

| x | -3 | -2 | -1 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|---|---|
| y=x^2-4 | 5 | 0 | -3 | -4 | -3 | 0 | 5 |

Plot those seven points and join them into a smooth U: it dips to (0,-4) at the bottom and rises symmetrically, crossing the axis at the two roots. The table is symmetric around x=0, which matches the vertex sitting on the axis of symmetry there.

2. y=x²-2x-3 (a=1,b=-2,c=-3). Direction: a>0, opens **up**. Roots: x²-2x-3=0 ⇒ (x-3)(x+1)=0 ⇒ x=3,-1, so (3,0) and (-1,0). Vertex: x=-(-2)/2=1, and y=1²-2(1)-3=-4, so (1,-4). Notice 1 is exactly midway between the roots -1 and 3, which is the symmetry working as a check. Table:

| x | -2 | -1 | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|---|
| y | 5 | 0 | -3 | -4 | -3 | 0 | 5 |

Join these into a smooth U through the two roots and down to the vertex at (1,-4).

A clean case to get the reading-off motion before the practice: sketch y = x² − 1. It opens up (a = 1 > 0); the roots come from x² − 1 = 0, so x = ±1, at (−1, 0) and (1, 0); and the vertex is at x = 0, y = −1, so (0, −1). A U dipping to (0, −1) and crossing at ±1: direction, roots, vertex, done.

With a couple of graphs behind you, here are the slips to watch. Don't eyeball the curve into shape; compute the table and let the points decide it, or the U comes out lopsided and teaches you a false picture.

Watch the opening direction: y = −x² + 4 opens *down*, because a is negative; read the sign of a before you draw. The vertex-x can trip a sign when b is negative: for b = −2, −b/(2a) is −(−2)/2 = +1, not −1.

And keep three things distinct: the roots are where y = 0, the vertex is the turn, and the y-intercept (0, c) is where the curve meets the y-axis. The y-intercept generally isn't a root.

**Check for understanding (transfer):**
1. {#12.6.c1} For y = x² − 6x + 8, find the roots and the vertex. How are the roots and the vertex's x-coordinate related? (Roots: x² − 6x + 8 = 0 ⇒ (x − 2)(x − 4) = 0 ⇒ x = 2, 4. Vertex: x = −(−6)/2 = 3, y = 3² − 6(3) + 8 = −1, so (3, −1). The vertex's x, 3, is the average of the roots 2 and 4, so it sits exactly between them.)
2. {#12.6.c2} A parabola opens downward and never touches the x-axis. What can you say about its a and about its discriminant? (a < 0, since it opens down; and the discriminant is negative, since it has no real roots and never meets the axis.)
3. {#12.6.c3} Why are the x-intercepts of y = x² − 9 exactly the solutions of x² − 9 = 0? (The x-intercepts are the points where y = 0, and setting y = 0 gives x² − 9 = 0, the very same equation. So its solutions, x = ±3, are precisely where the graph crosses the x-axis.)

You can now graph a quadratic by reading its direction from the sign of a, its roots from y = 0, and its vertex from x = −b/(2a), building the curve from a computed table. And you can explain why the U usually crosses the axis twice.

Mixed practice feels harder on purpose, and that's what makes it last. Every answer is at the end of the lesson; if one stalls you, flip back to the worked example it's based on.

**Practice problems:**
*For each, find the roots, the vertex, and the direction it opens (then sketch):*
1. y=x²-1
2. y=x²-9
3. y=x²-4
4. y=x²+4x+3
5. y=x²-6x+8
6. y=x²+2x-3
7. y=-x²+4
8. Sketch y=x²-2x-3 using its roots and vertex.

**Answer key:**
1. roots x=±1; vertex (0,-1); opens up · 2. roots x=±3; vertex (0,-9); opens up · 3. roots x=±2; vertex (0,-4); opens up · 4. (x+1)(x+3), roots x=-1,-3; vertex x=-2, y=-1 → (-2,-1); opens up · 5. (x-2)(x-4), roots x=2,4; vertex x=3, y=-1 → (3,-1); opens up · 6. (x+3)(x-1), roots x=-3,1; vertex x=-1, y=-4 → (-1,-4); opens up · 7. roots x=±2; vertex (0,4); opens **down** (a=-1) · 8. roots x=-1,3; vertex (1,-4); opens up — U through (-1,0),(1,-4),(3,0).

---

## A short word problems strand (where the two solutions mean something)

Try these once the methods feel solid. The algebra isn't harder here. A quadratic from a real situation still gives you two roots, and you keep the one that fits the question. Sometimes both roots are real and only one makes sense; that's the "reject the impossible root" move, and it's where "two solutions" and "no real solution" stop being mechanics and start to mean something. Solve each by whichever method is cleanest (factoring is enough for all three below), then read your answer back into the story.

**Worked example (model it, then reject a root):** *A ball is thrown straight up; its height in feet after t seconds is h=-16t²+32t. When does it hit the ground (h=0)?*
Set -16t²+32t=0, factor -16t(t-2)=0 ⇒ t=0 or t=2. Both are real, but in context **t=0 is the launch instant** (height 0 because it just left the hand) and **t=2 is the landing**, so it hits the ground at t=2 seconds. Two roots came out of the math; only one answers the question. Before you start one of these, it helps to name your plan in a sentence: what are you solving for, and which root fits the story?

**Application practice (state both roots, then the one that fits, and why):**
1. A ball's height is h=-16t²+48t feet after t seconds. Find both times its height is 0, and say which is the launch and which is the landing.
2. Two consecutive positive integers have a product of 56. Set up n(n+1)=56 and find them; explain why the negative-integer pair is rejected.
3. A rectangle's length is 3 more than its width, and its area is 40. Find the width (let the width be w, so w(w+3)=40); explain why one root is impossible.

**Answer key:**
1. -16t²+48t=0 ⇒ -16t(t-3)=0 ⇒ t=0 or t=3; **t=0 launch, t=3 landing** (hits the ground at 3 s). · 2. n(n+1)=56 ⇒ n²+n-56=0 ⇒ (n-7)(n+8)=0 ⇒ n=7 or n=-8; keep **n=7 → integers 7 and 8** (the problem says *positive*, so reject n=-8). · 3. w(w+3)=40 ⇒ w²+3w-40=0 ⇒ (w-5)(w+8)=0 ⇒ w=5 or w=-8; a width can't be negative, so **w=5** (rectangle 5 by 8). 

---

## Quadratics reference (choosing a solving method)

Keep this box handy for when you're staring at a quadratic and wondering which tool to grab. The first job is triage: pick the cleanest method for the shape in front of you, then solve. You have four tools, and the choice is yours. Picking one on purpose, rather than always defaulting to the same one, is part of the skill.

**Pick by the shape of the equation:**
- **Looks like (something)² = k, with no plain x term?** Use the **Square-Root Property (12.2)**: isolate the square, then x = ±√k if k ≥ 0 (no real solution if k < 0). Cleanest for x² = 9 (→ x = ±3), 3x² = 27, (x + 1)² = 5. No need to drag the formula into these.
- **Factors with nice integers?** Use **factoring (12.3)**. Best for tidy integer roots like x² + 5x + 6 = 0 (→ x = −2, −3) or x² − 9 = 0. Quick test: does the discriminant b² − 4ac come out a perfect square? Then it factors over the rationals and factoring will be fast.
- **Messy, or it won't factor, or you just want a guaranteed route?** Use the **quadratic formula (12.5)**. It solves *every* quadratic, for example x² − 2x − 5 = 0 (→ 1 ± √6, discriminant 24, not a perfect square) or any case where a isn't 1, like 2x² + 3x − 2 = 0.
- A rule of thumb: try square-root property, then factoring, then formula, in that order of "is it clean here?" When in doubt, the formula never fails.

**The four tools at a glance:**
- **Square-Root Property (12.2), for (something)² = k.** Isolate the square, apply ±√( ) when k ≥ 0; k < 0 gives no real solution. The narrow but cleanest case.
- **Factoring (12.3), clean but not always possible.** Fastest when the quadratic factors with nice integers. Get one side to 0, factor, set each factor = 0. Won't work on most irrational-root quadratics (those whose discriminant isn't a perfect square).
- **Quadratic formula (12.5), universal.**
$$x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$$
Works on *every* quadratic; read a, b, c (signs included) straight off ax² + bx + c = 0. The discriminant b² − 4ac pre-counts the real solutions (> 0 two, with a perfect square → rational, else irrational; = 0 one repeated root; < 0 none).
- **Completing the square (12.4), the formula's origin.** Add (b/2)² to both sides to build a perfect square, then ±√( ). Rarely the quickest for a numeric answer, but it's the move the quadratic formula is built from.

The ± runs through all four, and the parabola (12.6) shows why: a U usually crosses the x-axis **twice** because **squaring lost the sign**, the single idea this whole unit recovers.

You've now closed the loop on Algebra 1. The two long threads of the course both end right here: exponents to roots to quadratics, and multiplying binomials to factoring to solving. You can move among the solving methods, read the discriminant to know what to expect, and picture the parabola behind it all. If a piece of this unit ever goes hazy later, come back to the one sentence everything hangs on: squaring loses the sign, so undoing it gives you back both.
