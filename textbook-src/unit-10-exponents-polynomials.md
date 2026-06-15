# Unit 10: Exponents & Polynomials

> This unit is about building expressions up: taking small pieces and putting them together into bigger ones. It's the toolkit the rest of the course leans on, and most of it grows from one simple idea you'll meet on the first page.
>
> What helps to have fresh: a little comfort multiplying a number by itself, and the patience to handle a minus sign carefully. That's plenty. Everything else, we'll build here from scratch.

This unit points in one direction: building expressions up. You'll learn to multiply things out, to take (x + 2)(x + 3) and turn it into x² + 5x + 6. The very next unit runs the same machinery backward, so the work you put in here pays off twice.

Before each new lesson, redo two or three problems from a lesson or two earlier from memory. That small warm-up keeps the older moves sharp while the new ones land.

---

## Lesson 10.1: Exponent rules (including zero & negative exponents)

Exponents are just a shorthand for "multiply this by itself a few times." That's the whole idea, and every rule in this lesson comes straight out of it. The trick is to never let the shorthand pull you away from what it's counting.

<!--viz:anatomy#2-->

<!--illus:10-1-repeated-mult-->

When you're unsure what a rule should be, you can always write the factors out and count them. That habit, more than any memorized rule, is what keeps you out of trouble here.

These rules are the grammar of nearly every expression ahead: scientific notation in the next lesson, multiplying polynomials later in this one, and the two units after this. The way to make them stick is to see *why* each one is what it is, so that's how we'll build them.

Here's the first one, built from the ground up. Take x² · x³. Don't reach for a rule yet. Just write out what each piece means and count:
$$x^2\cdot x^3 = (x\cdot x)(x\cdot x\cdot x) = x^5$$
Line up the x's: two of them, then three more, five in all. When you multiply two powers of the same base, you're pooling all their factors into one pile, so the exponents **add**. Hold onto that single picture: pool the factors, count them. Once that habit is in place, the add-versus-multiply mix-up later in this lesson has much less to grab onto.

Division works the same way, read in reverse. Take x⁵ over x²:
$$\frac{x^5}{x^2} = \frac{x\cdot x\cdot x\cdot x\cdot x}{x\cdot x} = x^3$$
Two factors on the bottom pair off with two on the top, and a matched pair goes to one. A factor over itself is just 1. Three factors are left over on top, so x³. Dividing like bases is "how many factors are left after the pairs go to one," which is the same as **subtracting** the exponents.

Now a different move that looks similar but isn't. What about (x²)³, a power *raised to* a power? Write that out too:
$$(x^2)^3 = x^2\cdot x^2\cdot x^2 = x^6$$
Three copies of x², so 2 + 2 + 2 = 6. Here the exponents **multiply**.

Sit with the contrast for a second, because it's the heart of the lesson. x² · x³ is two *separate* powers multiplied, so you add (2 + 3 = 5). (x²)³ is *one* power taken three times, so you multiply (2 · 3 = 6). Same-looking, opposite arithmetic. When you can feel which situation you're in, you've got the lesson.

Gathered up, here are the rules these pictures give you:
$$x^a\cdot x^b=x^{a+b}\qquad\frac{x^a}{x^b}=x^{a-b}\qquad (x^a)^b=x^{ab}\qquad (xy)^a=x^a y^a\qquad x^0=1$$

That fourth one says a power on a product reaches *every* factor inside: (xy)ᵃ hands the exponent to the x and to the y alike. There's a matching version for a quotient, (x/y)ᵃ = xᵃ/yᵃ, with the exponent reaching the top and bottom both. You won't need it for this unit's problems, but it's the natural companion if you ever wonder.

### Where x⁰ = 1 and negative exponents come from

The last two rules look like things you'd just have to memorize. You don't, and seeing why frees you from getting them backward.

Start with x⁰. Take any power over itself, say x³/x³, and read it two ways. By the quotient rule, you subtract the exponents: x³⁻³ = x⁰. But anything divided by itself is plainly 1. Both readings describe the same quantity, so:
$$\frac{x^3}{x^3}=x^{3-3}=x^0 \quad\text{and}\quad \frac{x^3}{x^3}=1 \;\Rightarrow\; x^0=1$$
So x⁰ = 1 isn't a decree someone made up; it's forced. The rule you already trust leaves no other option.

Negative exponents come from the same move, just with more on the bottom than the top. Take x² over x⁵, and again read it two ways. The quotient rule gives x²⁻⁵ = x⁻³. Counting factors gives something you can see: two factors on top pair off with two on the bottom and go to one, leaving three factors stranded *on the bottom*, which is 1/(x³). Same quantity, two descriptions:
$$\frac{x^2}{x^5}=x^{2-5}=x^{-3}\quad\text{and}\quad\frac{x^2}{x^5}=\frac{1}{x^3}\;\Rightarrow\;x^{-3}=\frac{1}{x^3}$$
So a negative exponent means *reciprocal*: flip it to the other floor of the fraction. It does not mean the number is negative. For positive x, x⁻³ is a perfectly ordinary positive number; the minus sign is an instruction to flip, not a sign on the value.

**New terms:**
- {#10.1.d1} **Base** and **exponent:** in x⁵, x is the base, 5 is the exponent; x⁵ means x multiplied by itself 5 times.
- {#10.1.d2} **Zero exponent:** x⁰=1 (for x≠0).
- {#10.1.d3} **Negative exponent:** x⁻ᵃ=1/(xᵃ). A negative exponent means "reciprocal," *not* a negative number.

Read each worked example slowly, a line at a time, and ask why each line follows from the one above before you go on. Each one names the rule it's using, so you can match the move to its reason.

**Worked examples:**

*Product rule, add the exponents:*
{#10.1.w1}
$$x^4\cdot x^3 = x^{4+3}=x^7$$

*The trap, done right (add, don't multiply):*
{#10.1.w2}
$$x^2\cdot x^3 = x^{2+3}=x^5 \quad(\text{not }x^6;\ \text{count: }(xx)(xxx)=xxxxx)$$

*Quotient rule, subtract:*
{#10.1.w3}
$$\frac{x^7}{x^2}=x^{7-2}=x^5$$

*Power of a power, multiply:*
{#10.1.w4}
$$(x^2)^3 = x^{2\cdot 3}=x^6$$

*Power of a product, exponent reaches the coefficient too:*
{#10.1.w5}
$$(2x)^3 = 2^3 x^3 = 8x^3$$

*Zero & negative:*
{#10.1.w6}
$$x^0 = 1 \qquad\qquad x^{-2}=\frac{1}{x^2}$$

*Quotient landing negative (ties the two ideas together):*
{#10.1.w7}
$$\frac{x^3}{x^5}=x^{3-5}=x^{-2}=\frac{1}{x^2}$$

The slip that catches the most people here is using the wrong rule between two that look alike: writing x² · x³ = x⁶, or (x²)³ = x⁵. The pull is to run the same operation in both cases, since the expressions look so similar.

The fix is always the same, and you already have it: write the x's out and count. x² · x³ is (xx)(xxx), five x's, so x⁵. (x²)³ is x² three times over, six x's, so x⁶. The quick check is to ask yourself, "am I multiplying two separate powers, or raising one power to another?" Add for the first, multiply for the second.

One more place to watch is the power-of-a-product rule, because it's easy to leave the coefficient behind. In (2x)³, the exponent greets *everything* inside the parentheses, the 2 included: it's 2³x³ = 8x³, not 2x³. The 3 is sitting on the whole 2x, not just the x.

The same question settles its zero-exponent cousin. In 5x⁰ there are no parentheses, so the exponent touches only the x, giving 5 · 1 = 5. But (5x)⁰ puts the whole 5x under the exponent, giving 1. Before you apply a 0 or a power, ask what the base actually is: just the x, or the whole thing?

Here's a clean case to get the method moving before the practice mixes things up. Simplify y⁵ · y. The lone y is y¹, so add the exponents: y⁵ · y¹ = y⁶. Nothing subtle there: just the product rule, once, with the silent exponent of 1 made visible.

**Check for understanding (transfer):**
1. {#10.1.c1} Why does x² · x³ add the exponents but (x²)³ multiply them? Convince yourself by counting x's, and write the count out. (x² · x³ = (xx)(xxx) = five x's = x⁵; (x²)³ = x² · x² · x² = six x's = x⁶.)
2. {#10.1.c2} Use the quotient rule on x⁴/x⁴ two different ways to explain why x⁰ = 1. (By the rule, x⁴⁻⁴ = x⁰; but anything over itself is 1; so x⁰ = 1.)
3. {#10.1.c3} Suppose someone says x⁻³ is a negative number. What would you show them to fix that? (Re-derive it from x²/x⁵: two factors pair off and go to one, three are left on the bottom, so x⁻³ = 1/(x³), a reciprocal, positive for positive x.)

You can now simplify with all four rules, and you can rebuild the zero and negative cases from scratch whenever memory wobbles. That rebuilding is what keeps you from learning them backward.

The set below mixes the rules together on purpose, which is harder than repeating one kind of problem and also what makes a skill last to next week. Every problem has its answer at the end of the lesson, and if one stalls you, the worked examples just above are built on the same moves. Item 18 is worth a careful look: it runs a negative exponent the *other* direction, as something you start with rather than land on.

**Practice problems:**

*Product rule:*
1. x⁴·x³  2. x²·x³  3. y⁵·y  4. a³·a⁴·a²

*Quotient rule:*
5. (x⁷)/(x²)  6. (y⁶)/(y⁴)  7. (a⁵)/a

*Power rules:*
8. (x²)³  9. (y³)⁴  10. (xy)³  11. (2x)³

*Zero & negative exponents:*
12. x⁰  13. 5x⁰  14. x⁻²  15. (x³)/(x⁵)

*Mixed (combine rules):*
16. (x²·x⁴)/(x³)  17. (3x²)(4x⁵)  18. x⁵·x⁻²

(Item 18 uses a negative exponent as an *input* rather than an answer: x⁵·x⁻² = x⁵⁺⁽⁻²⁾ = x³, the product rule with a negative exponent. It's the reverse of items 14 and 15, where the negative exponent was the *result*. The answer is positive because 5 + (−2) = 3.)

**Answer key:**
1) x⁷  2) x⁵  3) y⁶  4) a⁹  5) x⁵  6) y²  7) a⁴  8) x⁶  9) y¹²  10) x³y³  11) 8x³  12) 1  13) 5  14) 1/(x²)  15) 1/(x²)  16) x³  17) 12x⁷  18) x³

---

## Lesson 10.2: Scientific notation

Some numbers are too long to read comfortably: the distance to a star, the width of an atom. Scientific notation is a tidy way to write them, with one digit, a decimal tail, and a power of ten that records how big the number really is.

You already did the hard part last lesson. Multiplying and dividing these numbers is just the exponent rules from 10.1, applied to powers of ten.

Start with what a power of ten actually does. Multiplying by 10 slides the decimal point one place to the right; dividing by 10 slides it one place left. So 10ⁿ is really a record of *how many places the point moved*. Take 5300. Picture the decimal point starting after the 5, at 5.3, and ask how far it has to travel to rebuild the full number: three places right gets you back to 5300. So 5300 = 5.3 × 10³. The exponent 3 is just the count of slides.

<!--illus:10-2-sliding-decimal-->

Small numbers work the same way, and this is where the negative exponents from last lesson come back. Take 0.00042. To get up to a single nonzero digit, 4.2, you slide the point four places to the *right*. But sliding right makes a number bigger, so to keep the value the same you must have started by dividing, and that's a negative exponent: 0.00042 = 4.2 × 10⁻⁴.

The negative power of ten is the same reciprocal idea as x⁻ᵃ = 1/(xᵃ): it's a division written as an exponent.

Once a number is in this form, multiplying and dividing splits into two easy jobs. Handle the front numbers (the coefficients) on their own, and handle the powers of ten with the rules you already know: multiplying tens adds the exponents, dividing tens subtracts them. Then, if the front number lands outside its allowed range, slide it back and adjust the power of ten to match.

**New terms:**
- {#10.2.d1} **Scientific notation:** a number written as a×10ⁿ, where a (the **coefficient**) satisfies 1≤|a|<10 and n is an integer. (Plain English: exactly one nonzero digit before the decimal point. The absolute-value bars let the coefficient be negative for a negative number, e.g. -5300 = -5.3×10³, where |-5.3|=5.3 is in range. Every example in this lesson is positive, so 1≤a<10 is the working form here, but state the rule with |a| so it stays true for negatives.)
- {#10.2.d2} **Standard form** (here): the ordinary way to write the number, e.g. 5300.

**Worked examples:**

*Large number → scientific notation:*
{#10.2.w1}
$$5300 = 5.3\times 10^3 \qquad(\text{check: } 5.3\times 1000 = 5300)$$

*Small number → scientific notation (negative exponent):*
{#10.2.w2}
$$0.00042 = 4.2\times 10^{-4} \qquad(\text{check: } 4.2\div 10^{4}=0.00042)$$

*Multiply, multiply the a's and add the exponents:*
{#10.2.w3}
$$(3\times 10^4)(2\times 10^3) = (3\cdot 2)\times 10^{4+3} = 6\times 10^7$$

*Divide, divide the a's and subtract the exponents:*
{#10.2.w4}
$$\frac{8\times 10^5}{2\times 10^2} = \frac{8}{2}\times 10^{5-2} = 4\times 10^3$$

*Mixed signs in the exponent (callback to 10.1):*
{#10.2.w5}
$$(4\times 10^6)(2\times 10^{-2}) = 8\times 10^{6+(-2)} = 8\times 10^4$$

*Renormalize UP, the coefficient product reaches 10 or more:*
{#10.2.w6}
$$(6\times 10^4)(5\times 10^3) = (6\cdot 5)\times 10^{4+3} = 30\times 10^7$$
Stop. 30 is **not** in [1,10), so 30×10⁷ is not yet scientific notation. Renormalize: write 30 as 3.0×10¹, then fold that extra power of ten into the exponent (the product rule again):
$$30\times 10^7 = 3.0\times 10^1\times 10^7 = 3\times 10^8$$
The decimal slid one place left (30→3.0), so the exponent went **up** by 1 (7→8). Sanity check: bigger coefficient shrunk ⇒ exponent must grow to keep the value the same. (Verify: 30×10⁷ = 300,000,000 = 3×10⁸.)

*Renormalize DOWN, a division coefficient drops below 1:*
{#10.2.w7}
$$\frac{2\times 10^3}{8\times 10^5} = \frac{2}{8}\times 10^{3-5} = 0.25\times 10^{-2}$$
Stop. 0.25 is **below** 1, so this isn't scientific notation either. Renormalize the other way: 0.25 = 2.5×10⁻¹, and folding in that 10⁻¹ drops the exponent by 1:
$$0.25\times 10^{-2} = 2.5\times 10^{-1}\times 10^{-2} = 2.5\times 10^{-3}$$
The decimal slid one place right (0.25→2.5), so the exponent went **down** by 1 (-2→-3). Same sanity check, reversed: coefficient grew ⇒ exponent must shrink. (Verify: 0.25×10⁻² = 0.0025 = 2.5×10⁻³.)

The rule running underneath all of this is the coefficient window: a proper coefficient sits at 1 or above and below 10, exactly one nonzero digit before the decimal point. If your arithmetic lands outside that window, slide the decimal back into it and adjust the power of ten by the number of places you slid: a left slide bumps the exponent up, a right slide drops it down.

Now that you've seen it done, two slips are worth naming. The first is leaving the coefficient out of range. You might write 53 × 10² or 0.53 × 10⁴ for 5300, and both *equal* 5300, but neither is scientific notation, because the coefficient has to be at least 1 and under 10.

The second shows up after multiplying or dividing: it's tempting to stop at 30 × 10⁷ and call it done, since the value is right. The value is right; the form isn't. Ask yourself the window question every time. Is my coefficient at least 1 and under 10? If not, slide and adjust.

And for small numbers, the sign of the exponent is easy to get backward, so run a quick test: is the number bigger or smaller than 1? Smaller than 1 means a negative power of ten.

One clean problem to reset on before the practice. Write 720,000 in scientific notation. The decimal sits after the last zero; slide it left to land just after the 7, giving 7.2, and count the slides: five places. Sliding left means the original was bigger, so the exponent is positive: 7.2 × 10⁵. One coefficient, one count of the slides, and you're there.

**Check for understanding (transfer):**
1. {#10.2.c1} Is 42×10³ in proper scientific notation? If not, fix it and explain the rule. (No. 42 is out of range; slide one place left and bump the exponent: 4.2×10⁴. The coefficient must be at least 1 and under 10.)
2. {#10.2.c2} Without computing the full number, what's (2×10⁵)(4×10³)? Which exponent rule did you just use? (Multiply the coefficients, add the exponents: 8×10⁸, the product rule on base 10.)
3. {#10.2.c3} Why does a number *smaller* than 1 get a *negative* power of ten? (You divide by tens to make a number that small, and a negative exponent is exactly that division: 10⁻ⁿ = 1/10ⁿ.)

You can now move a number between standard and scientific form by counting decimal slides, multiply and divide in scientific form with the exponent rules, and catch a result that's slipped out of the coefficient window and slide it back.

These problems jump between converting, multiplying, and dividing, and that switching is what makes the skill stick past today. The answers are all at the end of the lesson, and every move here appears in a worked example above, so when one stalls you, go back and reread the matching one. The last three deliberately push the coefficient out of range so you get practice sliding it home.

**Practice problems:**

*Convert to standard form (write the full number):*
1. 5.3×10³  2. 6.7×10⁴  3. 4.2×10⁻⁴  4. 9.1×10⁻³

*Convert to scientific notation:*
5. 720,000  6. 0.0305

*Multiply or divide (leave in scientific notation):*
7. (3×10⁴)(2×10³)  8. (8×10⁵)/(2×10²)  9. (4×10⁶)(2×10⁻²)  10. (9×10⁸)/(3×10⁵)

*Multiply or divide, then renormalize so 1≤coefficient<10:*
11. (4×10⁵)(5×10⁶)  12. (7×10²)(8×10³)  13. (3×10⁵)/(6×10²)

**Answer key:**
1) 5300  2) 67,000  3) 0.00042  4) 0.0091  5) 7.2×10⁵  6) 3.05×10⁻²  7) 6×10⁷  8) 4×10³  9) 8×10⁴  10) 3×10³  11) 2×10¹² (from 20×10¹¹ — slide left, exponent +1)  12) 5.6×10⁶ (from 56×10⁵ — slide left, exponent +1)  13) 5×10² (from 0.5×10³ — slide right, exponent −1)

---

## Lesson 10.3: Polynomials — terms, degree, standard form; add & subtract

A polynomial is just a sum of terms like 3x² + 2x − 1: number-times-a-power pieces, added up. It's the noun the next three units are about, so this lesson gives the parts their names and then does the two easiest things you can do with them: add and subtract.

The adding is nothing new; it's Unit 2's "combine like terms" with fresh vocabulary. The subtracting hides one genuine trap, and most of the lesson's care goes there.

First, the vocabulary, all on one example. Take 5x² − 3x + 2. It has three pieces, so it's a **trinomial**. Its highest power is 2, so its **degree** is 2. The number riding the highest-power term is its **leading coefficient**, here 5. And it's already in **standard form**, meaning its terms run from highest power down to lowest. A useful way to see why the plain number sits last: think of 2 as 2x⁰, since x⁰ = 1. That makes it the lowest-degree term, so it naturally ends the line.

Now adding. Like terms have to match the variable *and* its power: 3x² and x² are both "x²-pieces," so they combine, while 3x² and 3x are different kinds and don't. Picture the x²-pieces and the x-pieces as two different kinds of box: you can only stack a box with its own kind. Add the coefficients within each kind and keep them sorted by degree:
$$(3x^2+2x-1)+(x^2-5x+4) = (3+1)x^2+(2-5)x+(-1+4) = 4x^2-3x+3$$
Nothing fancy: x²-pieces with x²-pieces, x-pieces with x-pieces, plain numbers with plain numbers.

<!--illus:10-3-algebra-tiles-->

Subtraction is the same idea with one step that's easy to fumble, so go slow here. Subtracting a whole polynomial means a −1 shakes hands with *every* term inside the second parentheses: every sign flips, not just the first. This is the exact "hand the minus to everyone" move from Unit 2, wearing new clothes:
$$(2x^2+3x)-(x^2-x+2) = 2x^2+3x \;\underbrace{-x^2+x-2}_{\text{every sign flipped}} = x^2+4x-2$$
Watch the two that bite: the −x inside became +x, and the +2 became −2. The first term flipping is obvious; it's these later ones that get left alone by accident.

Here's the move that catches it for you: put a simple number in for x and check both sides. At x = 1, the original is (2 + 3) − (1 − 1 + 2) = 5 − 2 = 3, and the result is 1 + 4 − 2 = 3. They match, so the signs are right.

If they *hadn't* matched, that wouldn't be a failure. Your check would have just caught a slipped sign before it cost you anything. The next move would be to go back and re-run the flips one term at a time, because a mismatch here is almost always one sign left unflipped, not a broken method.

**New terms:**
- {#10.3.d1} **Polynomial:** a sum of terms, each a real number (the coefficient) times a whole-number power of a variable (e.g. 3x²+2x-1). The "whole-number power" part is what matters most: it rules out negative and fractional exponents, which is exactly what separates a polynomial from the rational/radical expressions seen in 10.1.
- {#10.3.d2} **Term / coefficient:** a single piece separated by + or -; the coefficient is its number part (in 3x², the coefficient is 3).
- {#10.3.d3} **Monomial / binomial / trinomial:** a polynomial with 1 / 2 / 3 terms.
- {#10.3.d4} **Degree:** the highest exponent in the polynomial (3x²+2x-1 has degree 2). The degree of a single term is its exponent; a nonzero constant has degree 0 (read it as cx⁰, since x⁰=1, so the 2 in 3x²+2x-1 is a degree-0 term, and a lone "7" has degree 0). This is *why* the constant sits last in standard form: it's the lowest-degree (x⁰) term.
- {#10.3.d5} **Standard form:** terms written in **descending** order of degree (highest power first).
- {#10.3.d6} **Leading coefficient:** the coefficient of the highest-degree term (once in standard form).

**Worked examples:**

{#10.3.w1}
*Naming (no arithmetic):* 3x²-7 → binomial, degree 2, leading coefficient 3.

*Standard form:*
{#10.3.w2}
$$2+5x^2-3x \;\Rightarrow\; 5x^2-3x+2$$

*Add:*
{#10.3.w3}
$$(3x^2+2x-1)+(x^2-5x+4) = 4x^2-3x+3$$

*Add (a term cancels to zero):*
{#10.3.w4}
$$(x^2+6x+2)+(3x^2-6x-7) = 4x^2+0x-5 = 4x^2-5$$

*Subtract, distribute the negative (the #1 trap here):*
{#10.3.w5}
$$(2x^2+3x)-(x^2-x+2) = x^2+4x-2 \qquad\text{Check at }x=1:\; 5-2=3 \;\text{ and }\; 1+4-2=3$$

*Subtract, three terms each:*
{#10.3.w6}
$$(5x^2-2x+1)-(2x^2+3x-4) = 3x^2-5x+5$$

In that fourth example, notice the 6x and the −6x added to nothing and the term simply dropped out: 4x² + 0x − 5 is just 4x² − 5. A term going to zero isn't something missing; it's a real result, and you write what's left.

The slip to keep an eye on is the one the subtraction examples are built around: flipping only the first sign after a minus. It's easy to write (2x² + 3x) − (x² − x + 2) as x² + 2x + 2, leaving the −x and the +2 alone. The cause is natural: the parentheses make it feel like the minus belongs to the whole group rather than to each piece. The cure is the substitution check you just saw, where a mismatch at x = 1 points straight at a sign you didn't flip.

The other thing people do is fuse unlike terms, writing 3x² + 2x as 5x² or 5x³. Those are different kinds of box; an x²-piece and an x-piece can't be stacked, so 3x² + 2x just stays as it is.

Read one straightforward case off the page before the set starts mixing. Name the type, degree, and leading coefficient of 7x⁵. One term, so it's a monomial; its highest (and only) power is 5, so degree 5; and the number on that term is 7, the leading coefficient. You're just reading the parts off the page.

**Check for understanding (transfer):**
1. {#10.3.c1} Name the type, degree, and leading coefficient of 4x³ − x + 9, then put 7 − 2x² in standard form. (Trinomial, degree 3, leading coefficient 4; and 7 − 2x² becomes −2x² + 7.)
2. {#10.3.c2} Subtract (x² − 4x + 5) − (2x² − 4x − 1), then prove the signs are right by testing x = 1. (Flip every sign in the second group: x² − 4x + 5 − 2x² + 4x + 1 = −x² + 6. Check at x = 1: original (1 − 4 + 5) − (2 − 4 − 1) = 2 − (−3) = 5, and −1 + 6 = 5.)
3. {#10.3.c3} Why can't 3x² and 3x be combined, even though both have a 3 and an x? (They're different kinds of term, one an x²-piece and the other an x-piece, and only terms with the same variable *and* the same power combine.)

You can now name a polynomial's parts, write it in standard form, add by combining like terms, and subtract with every sign flipped. Then check that subtraction with a quick substitution, so a missed sign never slips past you.

The problems below shuffle naming, adding, and subtracting together, and that mix is harder on purpose: choosing the right first move each time is what makes the skill last. You'll find every answer at the end of the lesson, with a worked example above for each problem, so lean on those if one stops you. The subtraction problems are where the sign trap lives, so run a substitution check on each one. That habit is the main thing this lesson is teaching.

**Practice problems:**

*Name the type, degree, and leading coefficient:*
1. 3x-7  2. x²-4x+1  3. 7x⁵

*Write in standard form:*
4. 2+5x²-3x  5. 4x-1+x³

*Add:*
6. (3x²+2x-1)+(x²-5x+4)  7. (2x²+3x)+(4x²-x+5)  8. (x²+6x+2)+(3x²-6x-7)

*Subtract (distribute the negative to every term):*
9. (2x²+3x)-(x²-x+2)  10. (5x²-2x+1)-(2x²+3x-4)  11. (4x²+x)-(x²+x-6)  12. (x³+2x-3)-(x³-x+5)

**Answer key:**
1) binomial, degree 1, leading coefficient 3.  2) trinomial, degree 2, leading coefficient 1.  3) monomial, degree 5, leading coefficient 7.  4) 5x²-3x+2  5) x³+4x-1  6) 4x²-3x+3  7) 6x²+2x+5  8) 4x²-5  9) x²+4x-2  10) 3x²-5x+5  11) 3x²+6  12) 3x-8

*Substitution spot-checks:* #9 at x=1: 5-2=3, 1+4-2=3. #12 at x=1: (1+2-3)-(1-1+5)=0-5=-5, and 3(1)-8=-5 (the x³'s subtract to zero).

---

## Lesson 10.4: Multiplying polynomials

This is the forward direction of the course's main thread: you take (x + 2)(x + 3) and multiply it out to x² + 5x + 6. The next unit hands you x² + 5x + 6 and asks you to find the pieces it came from, so multiplying out now is the very thing you'll learn to undo.

There's one spot where almost everyone loses a piece, the *middle* term, and the area box in this lesson is built to make that piece impossible to miss.

Start with the simpler case: a single term times a polynomial. The factor outside the parentheses hands a flyer to *everyone* inside, skipping no one. So 3x(x + 4) gives 3x · x and 3x · 4:
$$3x(x+4)=3x\cdot x+3x\cdot 4=3x^2+12x$$
The exponents follow last lesson's product rule: x · x is x², and the coefficient 3 rides along.

Now two binomials, where the middle term lives. Think of (x + 2)(x + 3) as the area of a rectangle whose width is x + 2 and whose height is x + 3. Slice the width into its two parts and the height into its two parts, and the rectangle breaks into four smaller cells. Each cell's area is one little product, and the whole area is all four added up:
$$\begin{array}{c|c|c}
 & x & 3 \\ \hline
x & x^2 & 3x \\ \hline
2 & 2x & 6
\end{array}\qquad\Rightarrow\qquad x^2 + \underbrace{3x+2x}_{=\,5x} + 6 = x^2+5x+6$$
There they are: four cells, x², 3x, 2x, and 6. The two in the middle, 3x and 2x, are the ones people drop, and they add up to the 5x that makes this a trinomial instead of just x² + 6.

<!--illus:10-4-area-grid-->

These same four products, taken in a fixed order, are sometimes called FOIL. The box is worth preferring, because it *shows you why a middle term exists* and keeps working when the pieces get bigger, where that shortcut runs out.

<!--viz:area_models#1-->

If the grid isn't your thing, there's a second way to see the same thing: distribute twice. First the x greets both terms in the second parentheses, then the 2 greets both:
$$x(x+3)+2(x+3)=x^2+3x+2x+6=x^2+5x+6$$
Same four products, same middle term, no grid. Pick whichever picture you find easier to keep straight. They give the same answer because they *are* the same work.

**New terms:** none new. This is the distributive property (Unit 2) applied once (monomial × polynomial) or twice (binomial × binomial).

**Worked examples:**

*Monomial × binomial, distribute:*
{#10.4.w1}
$$3x(x+4)=3x^2+12x$$

*Binomial × binomial, the area box:*
{#10.4.w2}
$$(x+2)(x+3)=x^2+5x+6 \quad(\text{middle term }3x+2x=5x)$$

*A negative in one binomial (watch signs):*
{#10.4.w3}
$$(x-3)(x-4)=x^2-4x-3x+12=x^2-7x+12$$

*Difference of squares, the middle term vanishes:*
{#10.4.w4}
$$(x-4)(x+4)=x^2+4x-4x-16=x^2-16$$
The +4x and -4x cancel, and that's *why* (a-b)(a+b)=a²-b².

*Squaring a binomial, the middle term is doubled:*
{#10.4.w5}
$$(x+3)^2=(x+3)(x+3)=x^2+3x+3x+9=x^2+6x+9$$
Note that (x+3)²≠x²+9. The middle 6x is the whole point.

Two of those deserve a second look. In the difference-of-squares example, the two middle cells, +4x and −4x, go to zero together, which is the whole reason (x − 4)(x + 4) collapses to just x² − 16.

And in the last one, squaring a binomial, the tempting move is to square each piece and write x² + 9. But (x + 3)² means (x + 3)(x + 3), and running the box gives a middle term of 3x + 3x = 6x. So (x + 3)² is x² + 6x + 9; the 6x is exactly the part that gets dropped, and catching it is what the example is for.

Across all of these, the error to watch for is the missing middle term: writing (x + 2)(x + 3) as x² + 6, or (x + 3)² as x² + 9. It happens when only the first-and-last products get written down.

The box is the cure, because it makes the question concrete. Every part of the width meets every part of the height, so there are *four* cells, not two; if you only have two terms, ask where the middle cells went. When a sign is in play, fill each cell with its *signed* product (x · −4 is −4x) and then add, and a substitution check at x = 1 will flag any sign that went astray.

Run the box once on a friendly case to feel it click. Expand (x + 5)(x + 1). The four cells are x², x, 5x, and 5; the middle two, x and 5x, add to 6x; so it's x² + 6x + 5. Four cells, then collect the middle pair, and that's the whole method.

**Check for understanding (transfer):**
1. {#10.4.c1} Expand (x + 2)(x + 5) with the area box, and point to where the middle term 7x comes from. (Four cells: x², 5x, 2x, 10; the middle pair 5x + 2x is the 7x, giving x² + 7x + 10.)
2. {#10.4.c2} Why does (x − 5)(x + 5) have *no* middle term, but (x − 5)(x − 5) does? (In the first, the middle cells are −5x and +5x, which go to zero, leaving x² − 25; in the second they're −5x and −5x, which add to −10x, giving x² − 10x + 25.)
3. {#10.4.c3} Suppose someone writes (x + 4)² = x² + 16. Using the box, show them exactly what they dropped. (Running (x + 4)(x + 4) gives middle cells 4x and 4x; they add to 8x, so the answer is x² + 8x + 16, and the dropped piece is the 8x.)

You can now multiply a single term across a polynomial, multiply two binomials with the area box, and reliably produce the middle term, including the cases where it doubles or vanishes. Hold onto each (x + 2)(x + 3) → x² + 5x + 6 you do: the next unit starts from the right-hand side and hunts for the left, and this same box is the tool you'll fill in reverse.

The set below mixes monomial products with binomial products instead of grouping them, harder in the moment but better for remembering. The answers wait at the end of the lesson, and each problem matches one of the worked examples above, so reread the right one whenever you get stuck. The last three are the special patterns: watch for a vanishing middle term in one and a doubled one in the others.

**Practice problems:**

*Monomial × polynomial (distribute):*
1. 3x(x+4)  2. 2x(3x-5)  3. -4x(x²-2x+1)

*Binomial × binomial (use the area box):*
4. (x+2)(x+3)  5. (x+5)(x+1)  6. (x-2)(x+7)  7. (x-3)(x-4)

*With a leading coefficient:*
8. (2x+1)(x+3)  9. (3x-2)(x+5)

*Special patterns (preview of Unit 11):*
10. (x-4)(x+4)  11. (x+3)²  12. (x-5)²

**Answer key:**
1) 3x²+12x  2) 6x²-10x  3) -4x³+8x²-4x  4) x²+5x+6  5) x²+6x+5  6) x²+5x-14  7) x²-7x+12  8) 2x²+7x+3  9) 3x²+13x-10  10) x²-16  11) x²+6x+9  12) x²-10x+25

*Substitution spot-checks at x=1:* #6: (-1)(8)=-8, and 1+5-14=-8. #9: (1)(6)=6, and 3+13-10=6. #11: (4)²=16, and 1+6+9=16.

---

You've reached the end of building expressions up. You can simplify with the exponent rules and rebuild the zero and negative cases when memory slips; move a number between standard and scientific form and compute in scientific form; name and add and subtract polynomials with the subtraction signs handled; and multiply binomials with the area box, middle term and all. The next unit takes that last box and runs it backward: you'll be handed the finished area and asked to find the edges. Every (x + 2)(x + 3) → x² + 5x + 6 you practiced is one you're about to learn to read from right to left.
