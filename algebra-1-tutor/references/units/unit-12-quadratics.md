# Unit 12: Quadratic Functions & Equations (the capstone)

> **Prerequisites:** Unit 11 (factoring trinomials, difference of squares) and Unit 10 (exponents, multiplying binomials) — the dependency chain *exponents → square roots → simplest quadratics → quadratic formula* and *FOIL → factoring → solving by factoring* both land here. Unit 5 (coordinate plane, reading a graph) for the parabola lessons. Comfort with negatives (`misconceptions.md §3`) is assumed throughout.
> **By the end, the student can:**
> - Simplify radicals by pulling out perfect-square factors (\(\sqrt{12}=2\sqrt3\)), and recognize an irrational root as an *exact* answer.
> - Solve the simplest quadratics by taking square roots, keeping **both** signs (\(x^2=9\Rightarrow x=\pm 3\)).
> - Solve a quadratic by factoring via the zero-product property.
> - Complete the square on \(x^2+bx+c\) once, and see why it produces the quadratic formula.
> - Apply the quadratic formula and read the discriminant to count real solutions.
> - Graph a parabola: find roots (x-intercepts), vertex, and direction of opening, and explain *why* a quadratic usually has two solutions.

## Teaching this unit (orientation for the tutor)

This is the capstone — every back-half skill composes here. The arc: **12.1** folds in radicals (the inverse of squaring) so the student has the tool to *express* answers; **12.2** introduces the defining surprise of quadratics with the cleanest possible case (\(x^2=9\)); **12.3–12.5** build three ways to solve the general quadratic; **12.6** ties it all to the picture.

**The one recurring theme, stated out loud and often: squaring loses sign information.** \(3^2=9\) and \((-3)^2=9\) — squaring throws away whether you started positive or negative, so undoing a square has to recover *both* origins. That is *why* quadratics usually have **two** solutions, why the \(\pm\) appears in every method, and why the parabola crosses the x-axis twice. Lean on `metaphors.md` → "Quadratics having two solutions" (both angles: A "squaring loses the sign," B "the parabola crossing twice"). Keep saying it; it unifies the whole unit.

**Thread function language.** A quadratic *is* a function: \(y=x^2-4\) and \(f(x)=x^2-4\) are the same object (callback to Units 4–5). The "solutions/roots" are exactly the inputs where \(f(x)=0\) — the x-intercepts of its graph. Narrate this connection whenever you can.

**Biggest misconception traps in this unit:**
- **Dropping a solution** — giving \(x=3\) for \(x^2=9\) and forgetting \(x=-3\). The signature error of the whole unit. Repair with "squaring loses the sign" (`metaphors.md`).
- **\(\sqrt{\,}\) of a non-perfect-square called "wrong."** \(\sqrt7\) *is* the answer — an exact irrational number (callback to Unit 1.2, the number system). Don't let them reach for a rounded decimal as if the radical were a failure.
- **Solving by factoring without setting equal to 0 first** — factoring \(x^2-5x+6=8\) and setting factors to 8. The zero-product property needs a **zero**.
- **Sign and arithmetic slips inside the formula** — especially \(-b\) when \(b\) is already negative, and \(b^2-4ac\) with negatives. `misconceptions.md §3`. Substitute a found root back to check (the `SKILL.md` habit).
- **\(-3^2\) vs \((-3)^2\)** resurfaces constantly in the discriminant; flag it (`misconceptions.md §3`).

**Pacing:** 12.1 and 12.2 are quick and concrete — get the \(\pm\) reflex solid before any factoring. 12.3 is the workhorse (most class quadratics factor). 12.4 is shown *once* for understanding, not drilled. 12.5 is the universal payoff. 12.6 is where the algebra becomes a picture — spend time, use the artifact. Verify every computation with the code tool before showing it (`visuals.md`: a wrong graph teaches a false picture).

---

## Lesson 12.1: Square roots & simplifying radicals

**Goal:** Take square roots of perfect squares, simplify a radical by pulling out perfect-square factors (\(\sqrt{12}=2\sqrt3\)), and treat an irrational root as an exact answer; add like radicals, multiply radicals, and lightly rationalize a denominator.
**Why it matters:** The square root is the *inverse of squaring* — the exact tool we need to undo \(x^2\) in every later lesson. Without it, the answer to \(x^2=7\) has no name.
**New terms:**
- **Square root (\(\sqrt{\;}\)):** the inverse of squaring. \(\sqrt{9}=3\) because \(3^2=9\). The symbol gives the **principal (non-negative) root** — \(\sqrt9\) is \(3\), not \(-3\). (We restore the second sign by hand in 12.2 with \(\pm\).)
- **Radical / radicand:** the \(\sqrt{\;}\) is the *radical*; the number under it is the *radicand*.
- **Perfect square:** a number that's some integer squared — \(1,4,9,16,25,36,49,\dots\)
- **Simplified radical:** no perfect-square factor left under the root. \(\sqrt{12}=\sqrt{4\cdot3}=2\sqrt3\) is simplified; \(\sqrt{12}\) is not.
- **Like radicals:** radicals with the *same* radicand (\(2\sqrt3\) and \(4\sqrt3\)) — they add like the "boxes" of Unit 2's like terms.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** "Squaring asks 'what's the area of a square with this side?' The square root asks the reverse: 'a square has area 9 — what's its side?' Side 3, so \(\sqrt9=3\)." Tie it to Unit 10 exponents: \(\sqrt{\;}\) undoes the \(2\) power.
- **Number system callback (Unit 1.2):** \(\sqrt9=3\) is a tidy integer, but \(\sqrt7\) is **irrational** — it has no exact decimal or fraction. That doesn't make it "unfinished"; \(\sqrt7\) *is* the exact answer, the same way \(\tfrac13\) is exact even though its decimal never stops. Resist rounding unless a decimal is asked for.
- **Symbolic — simplifying:** split the radicand into a *perfect-square factor times the rest*, then the perfect square comes out:
$$\sqrt{12}=\sqrt{4\cdot 3}=\sqrt4\,\sqrt3=2\sqrt3$$
Hunt for the **largest** perfect-square factor so you finish in one step.

**Worked examples:**

1. \(\sqrt{50}=\sqrt{25\cdot 2}=\sqrt{25}\,\sqrt2=5\sqrt2.\)
2. \(\sqrt{18}=\sqrt{9\cdot 2}=3\sqrt2.\) (Not \(\sqrt{2\cdot 9}\) handled as \(\sqrt2\cdot9\) — the perfect square is what comes *out*.)
3. **Add like radicals:** \(2\sqrt3+4\sqrt3=6\sqrt3.\) Same radicand, so add the counts — exactly like \(2x+4x=6x\). (You *cannot* combine \(2\sqrt3+4\sqrt2\); unlike radicals, like unlike terms.)
4. **Multiply radicals:** \(\sqrt2\cdot\sqrt3=\sqrt{2\cdot3}=\sqrt6.\) And \(\sqrt5\cdot\sqrt5=\sqrt{25}=5\) (a root times itself undoes the square).
5. **Rationalize a denominator (lightly):** a radical in the denominator is usually rewritten without one. Multiply top and bottom by \(\sqrt2\):
$$\frac{1}{\sqrt2}=\frac{1}{\sqrt2}\cdot\frac{\sqrt2}{\sqrt2}=\frac{\sqrt2}{2}.$$

**Cube roots in one line:** \(\sqrt[3]{27}=3\) because \(3^3=27\) — the cube root undoes cubing, same idea one power up.

**Watch for:**
- **"\(\sqrt7\) is wrong / unfinished."** It's the exact answer. Tell: they reach straight for \(2.6457\dots\) and treat the radical as an error. Repair via the number-system callback (Unit 1.2): irrational ≠ incorrect.
- **Not pulling the *largest* square** (\(\sqrt{72}=2\sqrt{18}\), left unsimplified). Tell: a perfect square still hides under the root. Cue: "Is there still a perfect-square factor inside?" (\(\sqrt{72}=6\sqrt2\)).
- **Adding unlike radicals** (\(\sqrt2+\sqrt3=\sqrt5\)). Tell: they merged different radicands. Cue: "Could you add \(2x+3y\) into one term? Same thing here." (`misconceptions.md §7`, unlike terms.)
- **\(\sqrt{a}\cdot\sqrt{a}\) mishandled** — writing \(\sqrt5\cdot\sqrt5=\sqrt5\) instead of \(5\).

**Visuals to offer:** none needed (a number line placing \(\sqrt7\) between \(2\) and \(3\) can help the "it's a real, exact number" point — `visuals.md` Template 1).

**Check for understanding (transfer):**
1. "Simplify \(\sqrt{45}\), and tell me how you knew which factor to pull out."
2. "Is \(\sqrt{10}\) a 'finished' answer? How is it like \(\tfrac13\) and unlike \(\sqrt9\)?"
3. "Why can you combine \(5\sqrt2+3\sqrt2\) but not \(5\sqrt2+3\sqrt3\)?"

**Practice problems:**
*Evaluate (perfect squares & cube root):*
1. \(\sqrt{16}\)
2. \(\sqrt{49}\)
3. \(\sqrt{100}\)
4. \(\sqrt[3]{27}\)
*Simplify:*
5. \(\sqrt{8}\)
6. \(\sqrt{20}\)
7. \(\sqrt{45}\)
8. \(\sqrt{72}\)
9. \(\sqrt{48}\)
10. \(\sqrt{75}\)
*Add / multiply / rationalize:*
11. \(3\sqrt5+\sqrt5\)
12. \(\sqrt2\cdot\sqrt8\)

**Answer key:**
1. \(4\) · 2. \(7\) · 3. \(10\) · 4. \(3\) · 5. \(\sqrt{4\cdot2}=2\sqrt2\) · 6. \(\sqrt{4\cdot5}=2\sqrt5\) · 7. \(\sqrt{9\cdot5}=3\sqrt5\) · 8. \(\sqrt{36\cdot2}=6\sqrt2\) · 9. \(\sqrt{16\cdot3}=4\sqrt3\) · 10. \(\sqrt{25\cdot3}=5\sqrt3\) · 11. \(4\sqrt5\) · 12. \(\sqrt{16}=4\).

---

## Lesson 12.2: The simplest quadratics (\(x^2=9\) → two solutions)

**Goal:** Solve \(x^2=k\) (and equations that rearrange to it) by isolating \(x^2\) and taking the square root of **both** signs: \(x=\pm\sqrt{k}\).
**Why it matters:** This is the unit's defining idea in its purest form — *two* solutions, and *why*. No factoring or formula yet; just the inverse of squaring done honestly.
**New terms:**
- **\(\pm\) ("plus or minus"):** shorthand for *two* answers at once. \(x=\pm3\) means \(x=3\) **or** \(x=-3\).
- **Quadratic equation:** an equation with an \(x^2\) term (and no higher power). Standard form is \(ax^2+bx+c=0\) with \(a\ne0\) — these are the special case where \(b=0\).

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete — the core metaphor:** "\(x^2=9\) asks: *what number, squared, gives 9?* Try \(3\): yes. But try \(-3\): \((-3)^2=9\) — also yes! Squaring **lost the sign** (`metaphors.md` → Quadratics A), so two different starts land on 9. We have to report both." This is the whole unit in one sentence.
- **Pictorial (optional):** the parabola \(y=x^2-9\) crosses the x-axis at \(-3\) *and* \(3\) (preview of 12.6, `metaphors.md` → Quadratics B).
- **Symbolic:** isolate \(x^2\), then apply \(\pm\sqrt{\;}\):
$$x^2=9\;\Rightarrow\; x=\pm\sqrt9=\pm3.$$
When \(k\) isn't a perfect square, the answer stays in radical form (12.1): \(x^2=7\Rightarrow x=\pm\sqrt7\).

**Worked examples:**

1. \(x^2=9\Rightarrow x=\pm3\), i.e. \(x=3\) or \(x=-3\). Check both: \(3^2=9\), \((-3)^2=9\).
2. \(x^2=16\Rightarrow x=\pm4.\)
3. \(x^2-7=0\Rightarrow x^2=7\Rightarrow x=\pm\sqrt7\) (exact, irrational — *not* "unfinished," per 12.1).
4. \(2x^2=50\Rightarrow x^2=25\Rightarrow x=\pm5.\) (Isolate \(x^2\) **first** — divide by 2 — before rooting.)
5. \(x^2-3=0\Rightarrow x^2=3\Rightarrow x=\pm\sqrt3.\)

**Watch for:**
- **Dropping the negative root** (answering just \(x=3\)). The signature error of the unit. Tell: a single answer to \(x^2=k\). Repair: "What's \((-3)^2\)? So is \(-3\) also a valid start? Squaring hid its sign." (`metaphors.md` → Quadratics A.)
- **Rooting before isolating** (\(2x^2=50\to x=\pm\sqrt{50}\)). Tell: \(x=\pm5\sqrt2\) instead of \(\pm5\). Cue: "Get \(x^2\) by itself first — what undoes the \(\times2\)?"
- **Calling \(\sqrt7\) wrong.** Carryover from 12.1 — it's the exact answer.
- **Sign of \(k\):** if isolating gives \(x^2=-4\), there's **no real solution** (no real number squares to a negative). Flag it gently; it returns in 12.5 as the discriminant.

**Visuals to offer:** none needed (optionally a parabola preview, `visuals.md` Template 3).

**Check for understanding (transfer):**
1. "Solve \(x^2=49\). How many answers, and why isn't it just one?"
2. "A classmate says \(x^2=20\) has answer \(x=\sqrt{20}\). What did they leave out, and can you simplify the radical too?"
3. "Solve \(3x^2=27\). What has to happen *before* you take a square root?"

**Practice problems:**
*Solve (keep both signs; leave irrationals exact):*
1. \(x^2=25\)
2. \(x^2=49\)
3. \(x^2=1\)
4. \(x^2-11=0\)
5. \(x^2-2=0\)
6. \(3x^2=27\)
7. \(5x^2=45\)
8. \(2x^2=18\)
9. \(x^2-100=0\)
10. \(x^2=5\)

**Answer key:**
1. \(x=\pm5\) · 2. \(x=\pm7\) · 3. \(x=\pm1\) · 4. \(x^2=11,\ x=\pm\sqrt{11}\) · 5. \(x^2=2,\ x=\pm\sqrt2\) · 6. \(x^2=9,\ x=\pm3\) · 7. \(x^2=9,\ x=\pm3\) · 8. \(x^2=9,\ x=\pm3\) · 9. \(x^2=100,\ x=\pm10\) · 10. \(x=\pm\sqrt5\).

---

## Lesson 12.3: Solving by factoring (zero-product property)

**Goal:** Solve a quadratic by writing it as \((\text{factor})(\text{factor})=0\), then setting each factor to zero — the zero-product property.
**Why it matters:** This is the everyday method for the quadratics that factor (most of the ones you'll meet). It directly cashes in the factoring from Unit 11.
**New terms:**
- **Zero-product property:** if a product equals \(0\), then *at least one* factor is \(0\). If \(A\cdot B=0\), then \(A=0\) or \(B=0\). (No other number forces a product to zero — this is special to \(0\).)
- **Root / solution:** a value of \(x\) that makes the equation true — the same "roots" that are x-intercepts in 12.6.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** "If I multiply two numbers and get \(0\), one of them *had* to be \(0\) — there's no other way. (Two non-zeros never multiply to zero.) So if \((x-2)(x-3)=0\), either \(x-2=0\) or \(x-3=0\)." Stress this only works against **0** — that's why we move everything to one side first.
- **Pictorial:** factoring is the reverse-distribute / area-box from Unit 11 (`metaphors.md` → Factoring A). Once factored, each factor being zero is a separate little one-step equation.
- **Symbolic — the procedure:** (1) get the equation into \(ax^2+bx+c=0\) form (one side is \(0\)); (2) factor (Unit 11); (3) set each factor \(=0\); (4) solve each.

**Worked examples:**

1. \((x-2)(x-3)=0\). Already factored and equal to 0. Set each: \(x-2=0\Rightarrow x=2\); \(x-3=0\Rightarrow x=3\). **\(x=2\) or \(x=3\).** Check: \((2-2)(2-3)=0\cdot(-1)=0\).
2. \(x^2-5x+6=0\). Factor (what multiplies to \(+6\), adds to \(-5\)? \(-2,-3\)): \((x-2)(x-3)=0\Rightarrow x=2\) or \(3\).
3. \(x^2+x-6=0\). (Multiply to \(-6\), add to \(+1\): \(+3,-2\).) \((x+3)(x-2)=0\Rightarrow x=-3\) or \(2\).
4. \(x^2-9=0\). Difference of squares (Unit 11.3): \((x-3)(x+3)=0\Rightarrow x=\pm3\). (Same answer 12.2 gives — two routes, one truth.)
5. **Must equal 0 first:** \(x^2-5x=-6\) is *not* ready. Move the \(-6\) over: \(x^2-5x+6=0\), then factor as in #2 → \(x=2,3\). Setting factors of \(x^2-5x=-6\) to numbers is meaningless.

**Watch for:**
- **Not setting equal to 0** (factoring \(x^2-5x+6=8\) and writing \(x-2=8\)). The zero-product property needs a **zero**; \(8\) gives you nothing. Tell: factors set to a non-zero number. Cue: "What does our property require on the right side?" Move everything over first.
- **Solving only one factor** (stopping at \(x=2\)). Each factor gives a root — two factors, (usually) two roots. Ties back to the unit theme.
- **Factoring errors from Unit 11** (sign of the constants). Repair at the factoring step, and **check by expanding** back (`factor_check` habit) or substituting the root.
- **Confusing "set factor to 0" with the answer's sign:** \(x+3=0\) gives \(x=-3\), not \(+3\). `misconceptions.md §3`.

**Visuals to offer:** area-model box for the factoring step (`visuals.md` "Area-model boxes", LaTeX `array`); the parabola preview if they want to *see* the two roots (12.6).

**Check for understanding (transfer):**
1. "Solve \((x+5)(x-1)=0\) without expanding. What lets you split it into two easy equations?"
2. "A student factors \(x^2-2x-8=0\) into \((x-4)(x+2)\) and stops at \(x=4\). What did they miss?"
3. "Why must \(x^2-3x=10\) be rewritten as \(x^2-3x-10=0\) before factoring to solve?"

**Practice problems:**
*Solve (already factored):*
1. \((x-1)(x-4)=0\)
2. \((x+5)(x-2)=0\)
*Factor, then solve:*
3. \(x^2-7x+12=0\)
4. \(x^2+5x+6=0\)
5. \(x^2-2x-8=0\)
6. \(x^2+7x+10=0\)
7. \(x^2-x-12=0\)
8. \(x^2-8x+15=0\)
9. \(x^2+3x=0\)  *(GCF: \(x(x+3)\))*
*Special patterns:*
10. \(x^2-16=0\)
11. \(x^2-6x+9=0\)  *(perfect square)*
12. \(x^2-3x-10=0\)

**Answer key:**
1. \(x=1,4\) · 2. \(x=-5,2\) · 3. \((x-3)(x-4),\ x=3,4\) · 4. \((x+2)(x+3),\ x=-2,-3\) · 5. \((x-4)(x+2),\ x=-2,4\) · 6. \((x+2)(x+5),\ x=-2,-5\) · 7. \((x-4)(x+3),\ x=-3,4\) · 8. \((x-3)(x-5),\ x=3,5\) · 9. \(x(x+3),\ x=0,-3\) · 10. \((x-4)(x+4),\ x=\pm4\) · 11. \((x-3)^2,\ x=3\) (one repeated root) · 12. \((x-5)(x+2),\ x=-2,5\).

---

## Lesson 12.4: Completing the square

**Goal:** Turn \(x^2+bx\) into a perfect-square trinomial by adding \((b/2)^2\), and use it to solve a quadratic — shown **once**, to build understanding and to set up the quadratic formula.
**Why it matters:** It's the method that *works even when factoring fails*, and — crucially — it's where the quadratic formula comes from. Seeing it once makes 12.5 feel earned, not handed down.
**New terms:**
- **Perfect-square trinomial:** a trinomial that factors as something squared — \(x^2+6x+9=(x+3)^2\) (Unit 11.3).
- **Completing the square:** adding the exact number, \((b/2)^2\), that turns \(x^2+bx\) into a perfect square.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete / the key fact:** "\((x+3)^2=x^2+6x+9\). Notice the constant \(9\) is \((6/2)^2\) — half the middle coefficient, squared. So to *manufacture* a perfect square from \(x^2+6x\), add \(9\)." Have them verify \((6/2)^2=9\) and expand \((x+3)^2\) to confirm.
- **Pictorial:** the literal "square" — \(x^2+6x\) is an \(x\)-by-\(x\) square plus two \(3\)-by-\(x\) strips; the missing corner is a \(3\)-by-\(3\) block of area \(9\). Adding it *completes the square*.
- **Symbolic — the move (keep the equation balanced):** add \((b/2)^2\) to **both sides**, factor the left as a square, then finish with the \(\pm\sqrt{\;}\) of 12.2.

**Worked examples:**

1. \(x^2+6x+5=0\).
$$x^2+6x=-5 \;\xrightarrow{+\,(6/2)^2=9}\; x^2+6x+9=-5+9 \;\Rightarrow\; (x+3)^2=4$$
$$x+3=\pm2 \;\Rightarrow\; x=-3\pm2 \;\Rightarrow\; x=-1 \text{ or } x=-5.$$
Check: \((-1)^2+6(-1)+5=0\), \((-5)^2+6(-5)+5=0\).

2. \(x^2+4x-5=0\). Move: \(x^2+4x=5\). Add \((4/2)^2=4\): \((x+2)^2=9\Rightarrow x+2=\pm3\Rightarrow x=1\) or \(-5\).

3. \(x^2-2x-3=0\). Move: \(x^2-2x=3\). Add \((-2/2)^2=1\): \((x-1)^2=4\Rightarrow x-1=\pm2\Rightarrow x=3\) or \(-1\).

4. **Where it earns its keep (factoring fails):** \(x^2-4x+1=0\). Move: \(x^2-4x=-1\). Add \((-4/2)^2=4\): \((x-2)^2=3\Rightarrow x-2=\pm\sqrt3\Rightarrow x=2\pm\sqrt3\). No integer factoring could have found this — but completing the square (and 12.5) does.

**Watch for:**
- **Adding \((b/2)^2\) to one side only** — that changes the equation. Tell: a wrong root. Cue: "We added \(9\) on the left; to keep the balance (`metaphors.md` → balance scale), what must we do on the right?"
- **Forgetting to halve before squaring** (adding \(b^2\) instead of \((b/2)^2\)). Tell: the left doesn't factor to a clean square. Cue: "Half of \(b\) first, *then* square."
- **\(\pm\) dropped at the root step** (the unit theme again) — \(x+3=2\) only, losing \(x=-5\).
- **Sign of \(b/2\) when \(b\) is negative** — \((-2/2)^2=1\), and the square is \((x-1)^2\), not \((x+1)^2\). `misconceptions.md §3`.

**Visuals to offer:** the area "completing the square" picture (a labeled `array`/sketch) helps the name land; otherwise none needed.

**Check for understanding (transfer):**
1. "To complete the square on \(x^2+10x\), what number do you add, and how did you get it?"
2. "Solve \(x^2+8x+7=0\) by completing the square. Show the balanced step on both sides."
3. "Why does completing the square solve \(x^2-4x+1=0\) when factoring can't?"

**Practice problems:**
*State the number that completes the square for:*
1. \(x^2+6x\)
2. \(x^2-10x\)
*Solve by completing the square:*
3. \(x^2+8x+7=0\)
4. \(x^2-6x+8=0\)
5. \(x^2+2x-8=0\)
6. \(x^2-2x-3=0\)

**Answer key:**
1. \((6/2)^2=9\) · 2. \((-10/2)^2=25\) · 3. \(x^2+8x=-7;\ +16:\ (x+4)^2=9;\ x=-4\pm3;\ x=-1,-7\) · 4. \(x^2-6x=-8;\ +9:\ (x-3)^2=1;\ x=3\pm1;\ x=2,4\) · 5. \(x^2+2x=8;\ +1:\ (x+1)^2=9;\ x=-1\pm3;\ x=2,-4\) · 6. \(x^2-2x=3;\ +1:\ (x-1)^2=4;\ x=1\pm2;\ x=3,-1\).

---

## Lesson 12.5: The quadratic formula & the discriminant

**Goal:** Solve any quadratic \(ax^2+bx+c=0\) with the quadratic formula, and use the discriminant \(b^2-4ac\) to predict the number of real solutions.
**Why it matters:** This is the **universal** method — it solves *every* quadratic, factorable or not, rational or irrational. It is exactly "completing the square, done once in general," so 12.4 was its origin story.
**New terms:**
- **Quadratic formula:** for \(ax^2+bx+c=0\) (with \(a\ne0\)),
$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}.$$
The \(\pm\) is the same two-solutions \(\pm\) as always — recovering the sign squaring destroyed.
- **Discriminant:** the inside-the-root part, \(b^2-4ac\). Its **sign** counts the real solutions before you finish:
  - \(b^2-4ac>0\): **two** real solutions (root of a positive → \(\pm\) two values).
  - \(b^2-4ac=0\): **one** real solution (\(\pm0\) collapses to one — the parabola's vertex sits on the axis).
  - \(b^2-4ac<0\): **no real** solution (no real square root of a negative — the parabola misses the axis).

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete:** "Factoring is elegant when it works; completing the square always works but is fiddly. The formula is completing-the-square done *once, in general*, so you never have to redo it — just read off \(a,b,c\) and plug in."
- **Identify \(a,b,c\) carefully (sign and all):** for \(2x^2+3x-2=0\), \(a=2,\ b=3,\ c=-2\). The sign travels with the number.
- **Symbolic:** substitute, simplify the discriminant first, then take its root and resolve the \(\pm\). Verify a root by substitution.

**Worked examples:**

1. \(x^2-5x+6=0\): \(a=1,b=-5,c=6\). Discriminant \((-5)^2-4(1)(6)=25-24=1>0\) → two solutions.
$$x=\frac{-(-5)\pm\sqrt1}{2}=\frac{5\pm1}{2}=\{3,\,2\}.$$
(Matches the factoring answer from 12.3 — every method agrees.)

2. \(2x^2+3x-2=0\): \(a=2,b=3,c=-2\). Discriminant \(3^2-4(2)(-2)=9+16=25\) → two.
$$x=\frac{-3\pm\sqrt{25}}{4}=\frac{-3\pm5}{4}=\left\{\tfrac{2}{4}=\tfrac12,\ \tfrac{-8}{4}=-2\right\}.$$

3. \(x^2-4x+4=0\): \(a=1,b=-4,c=4\). Discriminant \((-4)^2-4(1)(4)=16-16=0\) → **one** solution.
$$x=\frac{4\pm\sqrt0}{2}=\frac{4}{2}=2.$$
(A repeated root — the perfect square \((x-2)^2=0\).)

4. \(x^2+x+1=0\): \(a=1,b=1,c=1\). Discriminant \(1^2-4(1)(1)=1-4=-3<0\) → **no real solution** (can't take a real square root of \(-3\)). We stop here.

**Watch for:**
- **\(-b\) when \(b\) is negative** — for \(b=-5\), \(-b=+5\), not \(-5\). The single most common slip. `misconceptions.md §3`. Cue: "\(-b\) means *the opposite of* \(b\); \(b\) is \(-5\), so \(-b\) is...?"
- **Discriminant sign errors** — especially \(-4ac\) when \(c\) is negative makes it *add* (example 2: \(-4(2)(-2)=+16\)). And \(b^2\) is always positive even if \(b\) is negative (\((-5)^2=25\), the \(-3^2\) vs \((-3)^2\) trap). `misconceptions.md §3`.
- **Dividing only part of the numerator by \(2a\)** — the whole \(-b\pm\sqrt{\;}\) is over \(2a\). Keep the fraction bar full-width.
- **Calling "no real solution" a mistake.** A negative discriminant is a *real, correct finding* (the parabola doesn't cross — 12.6), not an error to fix.

**Visuals to offer:** the parabola (12.6) makes the three discriminant cases visible — crosses twice / touches once / misses. `visuals.md` Template 3.

**Check for understanding (transfer):**
1. "Use the formula on \(x^2-2x-5=0\). What's the discriminant, and what does its sign tell you before you finish?"
2. "Without solving, how many real solutions does \(x^2+x+5=0\) have? How can you tell?"
3. "In \(2x^2-7x+3=0\), what are \(a\), \(b\), and \(c\) — signs included — and what is \(-b\)?"

**Practice problems:**
*Find the discriminant and state the number of real solutions:*
1. \(x^2-3x-10=0\)
2. \(x^2+6x+9=0\)
3. \(x^2+x+5=0\)
4. \(x^2-6x+10=0\)
*Solve with the quadratic formula:*
5. \(x^2-5x+6=0\)
6. \(2x^2+3x-2=0\)
7. \(x^2-4x+4=0\)
8. \(3x^2-5x-2=0\)
9. \(2x^2-7x+3=0\)
10. \(x^2-2x-5=0\)  *(irrational roots — leave exact)*

**Answer key:**
1. \(9+40=49>0\), two solutions (\(x=5,-2\)) · 2. \(36-36=0\), one solution (\(x=-3\)) · 3. \(1-20=-19<0\), **no real solutions** · 4. \(36-40=-4<0\), **no real solutions** · 5. \(\frac{5\pm\sqrt1}{2}=3,2\) · 6. \(\frac{-3\pm\sqrt{25}}{4}=\tfrac12,-2\) · 7. \(\frac{4\pm\sqrt0}{2}=2\) · 8. \(\frac{5\pm\sqrt{49}}{6}=\frac{5\pm7}{6}=2,-\tfrac13\) · 9. \(\frac{7\pm\sqrt{25}}{4}=\frac{7\pm5}{4}=3,\tfrac12\) · 10. \(\frac{2\pm\sqrt{24}}{2}=1\pm\sqrt6\).

---

## Lesson 12.6: Graphing parabolas

**Goal:** Graph a quadratic as a parabola: find its roots (x-intercepts), its vertex and axis of symmetry, and its direction of opening — and explain *why* a quadratic usually has two solutions.
**Why it matters:** The picture is the payoff. It makes "two solutions" obvious (the U crosses the axis twice), explains the rare one/none cases, and ties the whole unit — radicals, roots, discriminant — into one image.
**New terms:**
- **Parabola:** the U-shaped graph of a quadratic \(y=ax^2+bx+c\).
- **Roots / x-intercepts:** where the parabola crosses the x-axis — exactly the solutions of \(ax^2+bx+c=0\) (12.3–12.5). This is *why* a quadratic usually has two.
- **Vertex:** the turning point (bottom of the U if it opens up, top if down). Its x-coordinate is \(x=-\dfrac{b}{2a}\).
- **Axis of symmetry:** the vertical line \(x=-\dfrac{b}{2a}\) through the vertex; the parabola is a mirror image across it.
- **Opens up / down:** **up if \(a>0\)**, **down if \(a<0\)**.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete / the unifying picture (`metaphors.md` → Quadratics B):** "A quadratic graphs as a U. The solutions are where it crosses the x-axis — and a U usually crosses *twice* (once going down, once coming back up). That's the two solutions, drawn. One solution = the U just *kisses* the axis at its vertex (discriminant 0); none = it floats entirely above or below (discriminant < 0)." This visually re-explains 12.5.
- **Pictorial / building it:** **compute** a small table of points (plug \(x\)-values into the equation — use the code tool), plot, join into a smooth U. Mark roots and vertex. Emit as an **SVG artifact** (`visuals.md` **Template 3** — raw SVG in chat won't render), labeled, with the companion table.
- **Symbolic — the quick read:** roots by solving \(y=0\) (any method from 12.3–12.5); vertex x at \(x=-\tfrac{b}{2a}\), then plug back for its y; direction from the sign of \(a\). For a symmetric parabola, the vertex sits exactly **between** the two roots.

**Worked examples:**

1. \(y=x^2-4\) (here \(a=1,b=0,c=-4\)).
   - Direction: \(a=1>0\) → opens **up**.
   - Roots: \(x^2-4=0\Rightarrow x=\pm2\) → crosses at \((-2,0)\) and \((2,0)\).
   - Vertex: \(x=-\tfrac{0}{2}=0\), \(y=0^2-4=-4\) → \((0,-4)\).
   - Table (computed): 

| \(x\) | \(-3\) | \(-2\) | \(-1\) | \(0\) | \(1\) | \(2\) | \(3\) |
|---|---|---|---|---|---|---|---|
| \(y=x^2-4\) | \(5\) | \(0\) | \(-3\) | \(-4\) | \(-3\) | \(0\) | \(5\) |

   Artifact (Template 3 mapping, origin \((110,150)\), 20 px/unit): \((-3,5)\to(50,50)\), \((-2,0)\to(70,150)\), \((-1,-3)\to(90,210)\), \((0,-4)\to(110,230)\), \((1,-3)\to(130,210)\), \((2,0)\to(150,150)\), \((3,5)\to(170,50)\). Roots dotted at \((70,150)\) and \((150,150)\); vertex labeled at \((110,230)\). (This is exactly the worked example in `visuals.md` Template 3.)

2. \(y=x^2-2x-3\) (\(a=1,b=-2,c=-3\)).
   - Direction: opens **up** (\(a>0\)).
   - Roots: \(x^2-2x-3=0\Rightarrow(x-3)(x+1)=0\Rightarrow x=3,-1\) → \((3,0)\) and \((-1,0)\).
   - Vertex: \(x=-\tfrac{-2}{2}=1\), \(y=1^2-2(1)-3=-4\) → \((1,-4)\). (Note \(1\) is midway between roots \(-1\) and \(3\) — the symmetry.)
   - Table (computed):

| \(x\) | \(-2\) | \(-1\) | \(0\) | \(1\) | \(2\) | \(3\) | \(4\) |
|---|---|---|---|---|---|---|---|
| \(y\) | \(5\) | \(0\) | \(-3\) | \(-4\) | \(-3\) | \(0\) | \(5\) |

   Artifact (origin \((110,110)\), 20 px/unit): \((-1,0)\to(90,110)\), \((3,0)\to(170,110)\) are the roots; vertex \((1,-4)\to(130,190)\).

**Watch for:**
- **Eyeballing the curve.** A misshapen parabola teaches a false picture. Always **compute** the table (code tool) and build the artifact from numbers (`visuals.md` rule 1).
- **Wrong opening direction** — reading \(y=-x^2+4\) as opening up. Tell: vertex on the wrong side. Cue: "What's the sign of \(a\)? Negative → opens down."
- **Vertex-x sign slip** in \(-\tfrac{b}{2a}\), especially when \(b<0\): for \(b=-2\), \(-\tfrac{-2}{2}=+1\). `misconceptions.md §3`.
- **Confusing roots with the vertex**, or thinking the y-intercept \((0,c)\) is a root. Roots are where \(y=0\); the vertex is the turn; \((0,c)\) is where it meets the y-axis.

**Visuals to offer:** `visuals.md` **Template 3** (parabola) — computed sample points joined by a `<polyline>`, roots and vertex dotted and labeled, companion table always in the chat.

**Check for understanding (transfer):**
1. "For \(y=x^2-6x+8\), find the roots and the vertex. How are the roots and the vertex's x-coordinate related?"
2. "A parabola opens downward and never touches the x-axis. What can you say about its \(a\) and about its discriminant?"
3. "Why are the x-intercepts of \(y=x^2-9\) exactly the solutions of \(x^2-9=0\)?"

**Practice problems:**
*For each, find the roots, the vertex, and the direction it opens (then sketch):*
1. \(y=x^2-1\)
2. \(y=x^2-9\)
3. \(y=x^2-4\)
4. \(y=x^2+4x+3\)
5. \(y=x^2-6x+8\)
6. \(y=x^2+2x-3\)
7. \(y=-x^2+4\)
8. Sketch \(y=x^2-2x-3\) using its roots and vertex.

**Answer key:**
1. roots \(x=\pm1\); vertex \((0,-1)\); opens up · 2. roots \(x=\pm3\); vertex \((0,-9)\); opens up · 3. roots \(x=\pm2\); vertex \((0,-4)\); opens up · 4. \((x+1)(x+3)\), roots \(x=-1,-3\); vertex \(x=-2,\ y=-1\) → \((-2,-1)\); opens up · 5. \((x-2)(x-4)\), roots \(x=2,4\); vertex \(x=3,\ y=-1\) → \((3,-1)\); opens up · 6. \((x+3)(x-1)\), roots \(x=-3,1\); vertex \(x=-1,\ y=-4\) → \((-1,-4)\); opens up · 7. roots \(x=\pm2\); vertex \((0,4)\); opens **down** (\(a=-1\)) · 8. roots \(x=-1,3\); vertex \((1,-4)\); opens up — U through \((-1,0),(1,-4),(3,0)\).

---

## Quadratics reference (the three solving methods)

Keep this box handy; offer it when a student asks "which method should I use?"

- **Factoring (12.3) — elegant, but not always possible.** Fastest when the quadratic factors with nice integers. Get one side to \(0\), factor, set each factor \(=0\). Fails on most irrational-root quadratics.
- **Quadratic formula (12.5) — universal.** \(x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}\). Works on *every* quadratic; read \(a,b,c\) (signs included) straight off \(ax^2+bx+c=0\). The discriminant \(b^2-4ac\) pre-counts the real solutions (\(>0\) two, \(=0\) one, \(<0\) none).
- **Completing the square (12.4) — the formula's origin.** Add \((b/2)^2\) to both sides to build a perfect square, then \(\pm\sqrt{\;}\). Rarely the quickest for a numeric answer, but it's *where the formula comes from* and is worth seeing once.

The \(\pm\) runs through all three, and the parabola (12.6) shows why: a U usually crosses the x-axis **twice** because **squaring lost the sign** — the single idea this whole unit recovers.

---

## Wrap-up & interleaving

**Consolidate:** the four solving lessons are four roads to the same place — confirm a student can pick factoring for clean integer roots, reach for the formula when it won't factor, and *read the discriminant* to know how many real answers to expect before grinding. The parabola (12.6) should now be the mental image behind "two solutions."

**Mix back in:**
- **Unit 11 (factoring):** every 12.3 problem *is* a factoring problem with one extra step. Slip in a difference-of-squares (\(x^2-9=0\)) and a perfect-square (\(x^2-6x+9=0\)) to keep 11.3 warm.
- **Unit 10 (exponents / binomials):** "check by expanding" turns a factored answer back into the original — reuse FOIL/the area model.
- **Unit 5 (graphing):** the parabola lives on the same coordinate plane; reading roots off a graph reuses the x-intercept idea, and the vertex is a point \((x,y)\) like any other.
- **Unit 1.2 (number system):** irrational roots (\(\sqrt7\), \(1\pm\sqrt6\)) are exact answers — revisit whenever a student wants to round prematurely.
- **Negatives (`misconceptions.md §3`):** the dominant error source — the lost \(-\) root, \(-b\) with negative \(b\), \(b^2-4ac\) signs, \((-3)^2\) vs \(-3^2\). Keep a negative-laden problem in every set and model the substitute-back check.

**Looking ahead / closure:** this is the capstone — the back-half dependency chains (exponents → roots → quadratics, and FOIL → factoring → solving) both terminate here. A student who can move fluidly among the three methods *and* picture the parabola has closed the loop on Algebra 1.

**Progress Card should note:** which lessons are mastered (12.1–12.6); whether the **\(\pm\) / two-solutions reflex** is automatic; whether they keep irrational roots exact (vs. rounding); whether they reliably set a quadratic to \(0\) before factoring; whether they handle signs inside the formula and the discriminant; and whether they can produce a correct, labeled parabola (roots + vertex + direction). Flag any lingering negative-sign shakiness to warm up next time.
