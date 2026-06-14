# Unit 10: Exponents & Polynomials

> **Prerequisites:** Unit 1 — exponents as repeated multiplication and order of operations (§1.3), including the \(-3^2\) vs. \((-3)^2\) distinction (misconceptions.md §3). Unit 2 — the distributive property and combining like terms (§2.3), and the "distribute the negative to *everyone*" sign trap.
> **By the end, the student can:**
> - Simplify expressions using the product, quotient, power, and power-of-a-product rules, and explain *why* \(x^0=1\) and \(x^{-a}=\tfrac{1}{x^a}\) follow from the quotient rule.
> - Write large and small numbers in scientific notation and multiply/divide in that form.
> - Name a polynomial's terms, coefficients, degree, and leading coefficient; write it in standard form; and add or subtract polynomials by combining like terms.
> - Multiply a monomial by a polynomial and a binomial by a binomial using the **area model**, getting the middle term right.
> - See that **multiplying out is the forward direction** that Unit 11 (factoring) will run in reverse.

## Teaching this unit (orientation for the tutor)

This unit opens the back third of the course: the chain **distribute → multiply binomials → factor (Unit 11) → solve by factoring (Unit 12)**. Everything here is "moving forward" (building expressions up); Unit 11 reverses it. Say that out loud at 10.4 so factoring later feels like *undoing* something familiar, not a brand-new trick.

The arc: **10.1** establishes the exponent rules — and treats \(x^0\) and \(x^{-a}\) not as decrees to memorize but as *consequences* of the quotient rule (this is the conceptual heart of the lesson). **10.2** is a high-payoff application of those rules — scientific notation is just "the exponent rules, applied to powers of ten." **10.3** introduces polynomial vocabulary and add/subtract, which is *exactly* Unit 2's combining-like-terms with the §3 sign trap front and center on subtraction. **10.4** multiplies polynomials with the area model from visuals.md and metaphors.md — the single most error-prone step is the **middle term** (misconceptions.md §7).

**Biggest traps, in order of how often they bite:**
- **Adding vs. multiplying exponents:** \(x^2\cdot x^3 = x^6\) (wrong — it's \(x^5\)). Multiplying like bases *adds* exponents; raising a power *multiplies* them. Lesson 10.1. This confusion is the spine of the whole lesson.
- **The missing middle term:** \((x+2)(x+3)=x^2+6\) (misconceptions.md §7). Lesson 10.4 — repair with the area-model box, which makes the two cross-terms visible.
- **Sign error subtracting a polynomial:** \((2x^2+3x)-(x^2-x+2)\) where the \(-x\) and \(+2\) don't get their signs flipped (misconceptions.md §3). Lesson 10.3 — this is Unit 2's "distribute the negative to *every* term" wearing new clothes.
- **\(-3^2\) vs. \((-3)^2\)** resurfacing (misconceptions.md §3) whenever a base is negative.

**Pacing:** Don't rush 10.1's *why* — a student who can re-derive \(x^0=1\) from \(x^3/x^3\) owns the rules instead of renting them. 10.2 is light and fun; let it reinforce 10.1. Slow down on 10.3 subtraction and on 10.4's middle term. Interleave Unit 2's distributive property continuously — 10.4 *is* the distributive property applied twice (metaphors.md → Multiplying binomials B).

**Threading function language:** where natural, note that \(P(x)=x^2+5x+6\) names a polynomial *function* — "multiplying \((x+2)(x+3)\) builds the rule \(P\); in Unit 11 we'll be handed \(P\) and asked to find the pieces." This connects back to Unit 4's \(f(x)\) notation and forward to the quadratics capstone.

---

## Lesson 10.1: Exponent rules (including zero & negative exponents)

**Goal:** Simplify expressions with the product, quotient, power, and power-of-a-product rules, and *derive* the zero- and negative-exponent rules from the quotient rule.

**Why it matters:** These rules are the grammar of every expression to come — scientific notation (10.2), polynomial multiplication (10.4), and all of Units 11–12 lean on them. A student who memorizes them backwards will multiply exponents that should add for the rest of the course.

**New terms:**
- **Base** and **exponent:** in \(x^5\), \(x\) is the base, \(5\) is the exponent; \(x^5\) means \(x\) multiplied by itself 5 times.
- **Zero exponent:** \(x^0=1\) (for \(x\neq 0\)).
- **Negative exponent:** \(x^{-a}=\dfrac{1}{x^a}\) — a negative exponent means "reciprocal," *not* a negative number.

**Teaching arc (concrete → pictorial → symbolic):**
- *Concrete — count the factors.* Don't lead with the rule; lead with expansion. \(x^2\cdot x^3 = (x\cdot x)(x\cdot x\cdot x)\) — line up the \(x\)'s and *count*: five of them, so \(x^5\). The student should **see** that multiplying like bases just pools the factors, so the exponents **add**. This single picture inoculates against the \(x^2\cdot x^3=x^6\) trap.
- *Quotient the same way.* \(\dfrac{x^5}{x^2}=\dfrac{x\cdot x\cdot x\cdot x\cdot x}{x\cdot x}\) — two factors on top pair off with two on the bottom and **go to one** (avoid "cancel," per misconceptions.md §1), leaving \(x^3\). Subtracting exponents is just "how many factors are left over."
- *Power of a power.* \((x^2)^3=x^2\cdot x^2\cdot x^2\) — three copies of \(x^2\), so \(2+2+2=6\): exponents **multiply**. Contrast deliberately with the product rule so the student feels *when* you add and *when* you multiply.
- *Symbolic — the five rules:*
$$x^a\cdot x^b=x^{a+b}\quad\frac{x^a}{x^b}=x^{a-b}\quad (x^a)^b=x^{ab}\quad (xy)^a=x^a y^a\quad x^0=1$$

**Deriving the surprising two (this is the lesson's core — don't skip):**
- *Why \(x^0=1\):* Apply the quotient rule to \(\dfrac{x^3}{x^3}\). By the rule it's \(x^{3-3}=x^0\). But anything over itself is \(1\). So \(x^0=1\) — *forced*, not invented.
$$\frac{x^3}{x^3}=x^{3-3}=x^0 \quad\text{and}\quad \frac{x^3}{x^3}=1 \;\Rightarrow\; x^0=1$$
- *Why \(x^{-a}=\tfrac{1}{x^a}\):* Apply the quotient rule to \(\dfrac{x^2}{x^5}\). By the rule it's \(x^{2-5}=x^{-3}\). By counting factors, two on top pair off and three are left *on the bottom*: \(\dfrac{1}{x^3}\). Both describe the same quantity, so \(x^{-3}=\dfrac{1}{x^3}\).
$$\frac{x^2}{x^5}=x^{2-5}=x^{-3}\quad\text{and}\quad\frac{x^2}{x^5}=\frac{1}{x^3}\;\Rightarrow\;x^{-3}=\frac{1}{x^3}$$

**Worked examples** (each names the rule):

*Product rule — add the exponents:*
$$x^4\cdot x^3 = x^{4+3}=x^7$$

*The trap, done right — add, don't multiply:*
$$x^2\cdot x^3 = x^{2+3}=x^5 \quad(\text{not }x^6;\ \text{count: }(xx)(xxx)=xxxxx)$$

*Quotient rule — subtract:*
$$\frac{x^7}{x^2}=x^{7-2}=x^5$$

*Power of a power — multiply:*
$$(x^2)^3 = x^{2\cdot 3}=x^6$$

*Power of a product — exponent reaches the coefficient too:*
$$(2x)^3 = 2^3 x^3 = 8x^3$$

*Zero & negative:*
$$x^0 = 1 \qquad\qquad x^{-2}=\frac{1}{x^2}$$

*Quotient landing negative (ties the two ideas together):*
$$\frac{x^3}{x^5}=x^{3-5}=x^{-2}=\frac{1}{x^2}$$

**Watch for:**
- **Multiplying exponents that should add** (and vice versa): \(x^2\cdot x^3=x^6\), or \((x^2)^3=x^5\). Tell: the student applied the wrong rule. Repair: go back to *counting factors* — write the \(x\)'s out. Hinge: "Is \(x^2\cdot x^3\) the same as \((x^2)^3\)? Count the \(x\)'s in each." (\(x^5\) vs. \(x^6\).) (misconceptions.md §7 — structure over memorized tricks.)
- **Power not reaching the coefficient:** \((2x)^3=2x^3\) (forgot to cube the 2). Repair: the exponent greets *every* factor inside, the 2 included — \(2^3x^3\).
- **Negative exponent read as a negative number:** thinking \(x^{-2}\) is negative or equals \(-x^2\). Repair: re-derive from \(x^2/x^4\) — it's a *reciprocal*, always positive for positive \(x\).
- **\(x^0=0\)** instead of \(1\). Repair: the \(x^3/x^3\) derivation — anything over itself is 1.

**Visuals to offer:** none needed — the "write out the factors and count" expansion *is* the visual; do it in line.

**Check for understanding (transfer):**
1. "Why does \(x^2\cdot x^3\) add the exponents but \((x^2)^3\) multiplies them? Convince me by counting \(x\)'s."
2. "Use the quotient rule on \(x^4/x^4\) two different ways to explain why \(x^0=1\)."
3. "A student says \(x^{-3}\) is a negative number. What would you show them to fix that?"

**Practice problems:**

*Product rule:*
1. \(x^4\cdot x^3\)  2. \(x^2\cdot x^3\)  3. \(y^5\cdot y\)  4. \(a^3\cdot a^4\cdot a^2\)

*Quotient rule:*
5. \(\dfrac{x^7}{x^2}\)  6. \(\dfrac{y^6}{y^4}\)  7. \(\dfrac{a^5}{a}\)

*Power rules:*
8. \((x^2)^3\)  9. \((y^3)^4\)  10. \((xy)^3\)  11. \((2x)^3\)

*Zero & negative exponents:*
12. \(x^0\)  13. \(5x^0\)  14. \(x^{-2}\)  15. \(\dfrac{x^3}{x^5}\)

*Mixed (combine rules):*
16. \(\dfrac{x^2\cdot x^4}{x^3}\)  17. \((3x^2)(4x^5)\)

**Answer key (all verified):**
1) \(x^7\)  2) \(x^5\)  3) \(y^6\)  4) \(a^9\)  5) \(x^5\)  6) \(y^2\)  7) \(a^4\)  8) \(x^6\)  9) \(y^{12}\)  10) \(x^3y^3\)  11) \(8x^3\)  12) \(1\)  13) \(5\)  14) \(\dfrac{1}{x^2}\)  15) \(\dfrac{1}{x^2}\)  16) \(x^3\)  17) \(12x^7\)

---

## Lesson 10.2: Scientific notation

**Goal:** Write large and small numbers as \(a\times 10^n\) with \(1\le a<10\), convert to and from standard form, and multiply/divide in scientific notation.

**Why it matters:** It's how science and engineering write the very big (distances, populations) and the very small (atom sizes), and it's a clean, motivating use of 10.1's exponent rules — multiplying powers of ten *adds* the exponents.

**New terms:**
- **Scientific notation:** a number written as \(a\times 10^n\), where \(a\) (the **coefficient**) satisfies \(1\le a<10\) and \(n\) is an integer.
- **Standard form** (here): the ordinary way to write the number, e.g. \(5300\).

**Teaching arc (concrete → pictorial → symbolic):**
- *Concrete — the decimal slides.* Multiplying by \(10\) moves the decimal point one place right; dividing by \(10\) moves it one place left. So \(10^n\) just records *how many places* the point moved. For \(5300\): start at \(5.3\), the point must slide **3 places right** to rebuild \(5300\), so \(5300=5.3\times 10^3\).
- *Small numbers → negative exponent (callback to 10.1).* For \(0.00042\): get to \(4.2\) by sliding the point **4 places right**, which means the original was \(4.2\) divided by \(10^4\) — a *negative* exponent: \(0.00042=4.2\times 10^{-4}\). The negative exponent is exactly the \(x^{-a}=\tfrac{1}{x^a}\) idea from 10.1.
- *Symbolic — multiply/divide.* Treat \(a\) and the power of ten separately: multiply (or divide) the \(a\)'s, and **add** (or **subtract**) the exponents — the product and quotient rules from 10.1 applied to base 10. Then, if needed, renormalize so \(1\le a<10\).

**Worked examples:**

*Large number → scientific notation:*
$$5300 = 5.3\times 10^3 \qquad(\text{check: } 5.3\times 1000 = 5300)$$

*Small number → scientific notation (negative exponent):*
$$0.00042 = 4.2\times 10^{-4} \qquad(\text{check: } 4.2\div 10^{4}=0.00042)$$

*Multiply — multiply the \(a\)'s, add the exponents:*
$$(3\times 10^4)(2\times 10^3) = (3\cdot 2)\times 10^{4+3} = 6\times 10^7$$

*Divide — divide the \(a\)'s, subtract the exponents:*
$$\frac{8\times 10^5}{2\times 10^2} = \frac{8}{2}\times 10^{5-2} = 4\times 10^3$$

*Mixed signs in the exponent (callback to 10.1):*
$$(4\times 10^6)(2\times 10^{-2}) = 8\times 10^{6+(-2)} = 8\times 10^4$$

**Watch for:**
- **Coefficient out of range:** writing \(53\times 10^2\) or \(0.53\times 10^4\) for \(5300\). Repair: "\(a\) must be at least 1 and under 10 — exactly one nonzero digit before the decimal." (Both are *equal* to 5300 but not in scientific notation.)
- **Wrong sign on the exponent for small numbers:** \(0.00042=4.2\times 10^{4}\). Repair: "Is this number bigger or smaller than 1? Smaller → the exponent is negative." Tie to 10.1's negative-exponent meaning.
- **Adding the coefficients instead of multiplying**, or multiplying the exponents instead of adding. Repair: separate the two jobs out loud — "the \(a\)'s multiply; the tens follow the *product rule* and add."
- **Off-by-one place counting.** Repair: write the number and count the slides deliberately; verify by sliding back.

**Visuals to offer:** none needed; an ASCII note of the decimal sliding (\(5.3\to 53.\to 530.\to 5300.\)) can anchor a stuck student.

**Check for understanding (transfer):**
1. "Is \(42\times 10^3\) in proper scientific notation? If not, fix it and explain the rule." (No → \(4.2\times 10^4\).)
2. "Without computing the full number, what's \((2\times 10^5)(4\times 10^3)\)? Which exponent rule did you just use?"
3. "Why does a number *smaller* than 1 get a *negative* power of ten?"

**Practice problems:**

*Convert to standard form (write the full number):*
1. \(5.3\times 10^3\)  2. \(6.7\times 10^4\)  3. \(4.2\times 10^{-4}\)  4. \(9.1\times 10^{-3}\)

*Convert to scientific notation:*
5. \(720{,}000\)  6. \(0.0305\)

*Multiply or divide (leave in scientific notation):*
7. \((3\times 10^4)(2\times 10^3)\)  8. \(\dfrac{8\times 10^5}{2\times 10^2}\)  9. \((4\times 10^6)(2\times 10^{-2})\)  10. \(\dfrac{9\times 10^8}{3\times 10^5}\)

**Answer key (all verified):**
1) \(5300\)  2) \(67{,}000\)  3) \(0.00042\)  4) \(0.0091\)  5) \(7.2\times 10^5\)  6) \(3.05\times 10^{-2}\)  7) \(6\times 10^7\)  8) \(4\times 10^3\)  9) \(8\times 10^4\)  10) \(3\times 10^3\)

---

## Lesson 10.3: Polynomials — terms, degree, standard form; add & subtract

**Goal:** Identify a polynomial's terms, coefficients, degree, leading coefficient, and type; write it in standard form; and add or subtract polynomials by combining like terms — distributing the negative to *every* term when subtracting.

**Why it matters:** "Polynomial" is the noun the next three units are about. Adding and subtracting them is Unit 2's combining-like-terms with new vocabulary — and subtraction is where the §3 sign trap returns in force.

**New terms:**
- **Polynomial:** a sum of terms, each a number times a whole-number power of a variable (e.g. \(3x^2+2x-1\)).
- **Term / coefficient:** a single piece separated by \(+\) or \(-\); the coefficient is its number part (in \(3x^2\), the coefficient is \(3\)).
- **Monomial / binomial / trinomial:** a polynomial with 1 / 2 / 3 terms.
- **Degree:** the highest exponent in the polynomial (\(3x^2+2x-1\) has degree 2). The degree of a single term is its exponent.
- **Standard form:** terms written in **descending** order of degree (highest power first).
- **Leading coefficient:** the coefficient of the highest-degree term (once in standard form).

**Teaching arc (concrete → pictorial → symbolic):**
- *Vocabulary first, on one example.* Take \(5x^2-3x+2\): three terms → **trinomial**; highest power 2 → **degree 2**; leading coefficient \(5\); already in standard form. Have the student name the parts of a fresh one before any arithmetic.
- *Add — combine like terms (mystery-box picture, metaphors.md → Variables).* Like terms must match the variable *and* its power: \(3x^2\) and \(x^2\) are like (both "\(x^2\)-boxes"); \(3x^2\) and \(3x\) are **not**. Add the coefficients of each kind, stack by degree:
$$(3x^2+2x-1)+(x^2-5x+4) = (3+1)x^2+(2-5)x+(-1+4) = 4x^2-3x+3$$
- *Subtract — the sign trap (misconceptions.md §3, the Unit 2 §3 callback).* Subtracting a whole polynomial means a \(-1\) shakes hands with **every** term inside the second parentheses — *every* sign flips:
$$(2x^2+3x)-(x^2-x+2) = 2x^2+3x \;\underbrace{-x^2+x-2}_{\text{every sign flipped}} = x^2+4x-2$$
Note the \(-x\) became \(+x\) and the \(+2\) became \(-2\). Verify by substituting \(x=1\): original \((2+3)-(1-1+2)=5-2=3\); result \(1+4-2=3\).

**Worked examples:**

*Naming (no arithmetic):* \(3x^2-7\) → binomial, degree 2, leading coefficient \(3\).

*Standard form:*
$$2+5x^2-3x \;\Rightarrow\; 5x^2-3x+2$$

*Add:*
$$(3x^2+2x-1)+(x^2-5x+4) = 4x^2-3x+3$$

*Add (a term cancels to zero):*
$$(x^2+6x+2)+(3x^2-6x-7) = 4x^2+0x-5 = 4x^2-5$$

*Subtract — distribute the negative (the #1 trap here):*
$$(2x^2+3x)-(x^2-x+2) = x^2+4x-2 \qquad\text{Check at }x=1:\; 5-2=3 \;\text{ and }\; 1+4-2=3$$

*Subtract — three terms each:*
$$(5x^2-2x+1)-(2x^2+3x-4) = 3x^2-5x+5$$

**Watch for:**
- **Sign not distributed across the subtraction:** \((2x^2+3x)-(x^2-x+2)=x^2+2x+2\) or \(\dots+? \) — the \(-x\) or the \(+2\) keeps its old sign. Tell: only the first subtracted term got flipped. Repair: "The minus is a \(-1\) greeting *everyone* in the second parentheses — what does it do to the \(-x\)? to the \(+2\)?" Then substitution-check at \(x=1\) (misconceptions.md §3).
- **Combining unlike terms:** \(3x^2+2x=5x^2\) or \(=5x^3\). Tell: different powers fused. Repair: \(x^2\)-boxes and \(x\)-boxes are different objects (misconceptions.md §7) — only same-power terms combine.
- **Standard form scrambled:** leaving \(2-3x+5x^2\) or calling \(-3\) the leading coefficient. Repair: descending powers first; the leading coefficient is whatever rides the *highest* power.

**Visuals to offer:** none needed; vertical alignment by degree (line up the \(x^2\) terms, the \(x\) terms, the constants) is the helpful "picture" — show it for a stuck student.

**Check for understanding (transfer):**
1. "Name the type, degree, and leading coefficient of \(4x^3-x+9\), then put \(7-2x^2\) in standard form."
2. "Subtract \((x^2-4x+5)-(2x^2-4x-1)\) and prove the signs are right by testing \(x=1\)."
3. "Why can't \(3x^2\) and \(3x\) be combined, even though both have a 3 and an \(x\)?"

**Practice problems:**

*Name the type, degree, and leading coefficient:*
1. \(3x-7\)  2. \(x^2-4x+1\)  3. \(7x^5\)

*Write in standard form:*
4. \(2+5x^2-3x\)  5. \(4x-1+x^3\)

*Add:*
6. \((3x^2+2x-1)+(x^2-5x+4)\)  7. \((2x^2+3x)+(4x^2-x+5)\)  8. \((x^2+6x+2)+(3x^2-6x-7)\)

*Subtract (distribute the negative to every term):*
9. \((2x^2+3x)-(x^2-x+2)\)  10. \((5x^2-2x+1)-(2x^2+3x-4)\)  11. \((4x^2+x)-(x^2+x-6)\)  12. \((x^3+2x-3)-(x^3-x+5)\)

**Answer key (all verified):**
1) binomial, degree 1, leading coefficient 3.  2) trinomial, degree 2, leading coefficient 1.  3) monomial, degree 5, leading coefficient 7.  4) \(5x^2-3x+2\)  5) \(x^3+4x-1\)  6) \(4x^2-3x+3\)  7) \(6x^2+2x+5\)  8) \(4x^2-5\)  9) \(x^2+4x-2\)  10) \(3x^2-5x+5\)  11) \(3x^2+6\)  12) \(3x-8\)

*Substitution spot-checks:* #9 at \(x=1\): \(5-2=3\), \(1+4-2=3\). #12 at \(x=1\): \((1+2-3)-(1-1+5)=0-5=-5\), and \(3(1)-8=-5\) (the \(x^3\)'s subtract to zero).

---

## Lesson 10.4: Multiplying polynomials

**Goal:** Multiply a monomial by a polynomial (distribute) and a binomial by a binomial using the **area-model box**, reliably producing the middle term.

**Why it matters:** This is the **forward direction** of the course's spine: \((x+2)(x+3)\to x^2+5x+6\). Unit 11 hands you \(x^2+5x+6\) and asks for the pieces — factoring is *this lesson run backward*. Owning the area model now means factoring later is "fill in the same box."

**New terms:** none new — this is the distributive property (Unit 2) applied once (monomial × polynomial) or twice (binomial × binomial).

**Teaching arc (concrete → pictorial → symbolic):**
- *Monomial × polynomial — distribute (flyers, metaphors.md → Distributive A).* The outside factor hands a flyer to *everyone* inside: \(3x(x+4)=3x\cdot x+3x\cdot 4=3x^2+12x\). Exponents follow 10.1's product rule (\(x\cdot x=x^2\)).
- *Binomial × binomial — the area box (visuals.md → area-model; metaphors.md → Multiplying binomials A).* \((x+2)(x+3)\) is a rectangle with sides \(x+2\) and \(x+3\). Split into four cells — each cell is one product:
$$\begin{array}{c|c|c}
 & x & 3 \\ \hline
x & x^2 & 3x \\ \hline
2 & 2x & 6
\end{array}\qquad\Rightarrow\qquad x^2 + \underbrace{3x+2x}_{=\,5x} + 6 = x^2+5x+6$$
The two **middle cells** (\(3x\) and \(2x\)) are exactly what people forget. Prefer this box over the **FOIL** acronym: FOIL is just the four cells in a fixed order and stops working past two terms, while the box generalizes and *shows why the middle term exists* (misconceptions.md §7).
- *Symbolic — two rounds of distributing (metaphors.md → Multiplying binomials B).* The same result without the grid: \(x\) greets both terms, then \(2\) greets both: \(x(x+3)+2(x+3)=x^2+3x+2x+6=x^2+5x+6\).

**Worked examples:**

*Monomial × binomial — distribute:*
$$3x(x+4)=3x^2+12x$$

*Binomial × binomial — the area box:*
$$(x+2)(x+3)=x^2+5x+6 \quad(\text{middle term }3x+2x=5x)$$

*A negative in one binomial (watch signs):*
$$(x-3)(x-4)=x^2-4x-3x+12=x^2-7x+12$$

*Difference of squares — middle term vanishes (preview of Unit 11 special pattern):*
$$(x-4)(x+4)=x^2+4x-4x-16=x^2-16$$
The \(+4x\) and \(-4x\) cancel — that's *why* \((a-b)(a+b)=a^2-b^2\). Flag it: Unit 11.3 will run this backward.

*Squaring a binomial — the middle term is doubled (preview of perfect-square trinomials):*
$$(x+3)^2=(x+3)(x+3)=x^2+3x+3x+9=x^2+6x+9$$
Stress: \((x+3)^2\neq x^2+9\). The middle \(6x\) is the whole point (misconceptions.md §7).

**Watch for:**
- **The missing middle term:** \((x+2)(x+3)=x^2+6\), or \((x+3)^2=x^2+9\). Tell: only the first-and-last products survived. Repair: the area-model box — "every part of the width meets every part of the height; that's *four* cells, not two. Where did the two middle ones go?" (misconceptions.md §7).
- **Sign errors in the cross terms:** \((x-3)(x-4)\) giving a \(+7x\) or a \(-12\). Repair: fill each cell with its signed product (\(x\cdot-4=-4x\), \(2\cdot-? \) etc.), then add; substitution-check at \(x=1\).
- **Coefficient × exponent confusion:** in \((2x+1)(x+3)\), writing \(2x\cdot x=2x\) instead of \(2x^2\). Repair: 10.1 product rule — the \(x\)'s combine to \(x^2\), the coefficient \(2\) rides along.
- **\((x+3)^2\) mis-expanded as \(x^2+9\)** (squaring each term). Repair: write it as \((x+3)(x+3)\) and run the box — the \(2\cdot 3x\) middle term appears.

**Visuals to offer:** the LaTeX `array` area-model box (visuals.md → area-model) for any binomial × binomial — show all four cells, then collect the two middle ones into the single middle term. This is *the* visual to make automatic, because it's the same box Unit 11 fills in reverse.

**Check for understanding (transfer):**
1. "Expand \((x+2)(x+5)\) with the area box, and point to where the middle term \(7x\) comes from."
2. "Why does \((x-5)(x+5)\) have *no* middle term, but \((x-5)(x-5)\) does?"
3. "A student writes \((x+4)^2=x^2+16\). Show them — with the box — exactly what they dropped." (the \(8x\))

**Practice problems:**

*Monomial × polynomial (distribute):*
1. \(3x(x+4)\)  2. \(2x(3x-5)\)  3. \(-4x(x^2-2x+1)\)

*Binomial × binomial (use the area box):*
4. \((x+2)(x+3)\)  5. \((x+5)(x+1)\)  6. \((x-2)(x+7)\)  7. \((x-3)(x-4)\)

*With a leading coefficient:*
8. \((2x+1)(x+3)\)  9. \((3x-2)(x+5)\)

*Special patterns (preview of Unit 11):*
10. \((x-4)(x+4)\)  11. \((x+3)^2\)  12. \((x-5)^2\)

**Answer key (all verified):**
1) \(3x^2+12x\)  2) \(6x^2-10x\)  3) \(-4x^3+8x^2-4x\)  4) \(x^2+5x+6\)  5) \(x^2+6x+5\)  6) \(x^2+5x-14\)  7) \(x^2-7x+12\)  8) \(2x^2+7x+3\)  9) \(3x^2+13x-10\)  10) \(x^2-16\)  11) \(x^2+6x+9\)  12) \(x^2-10x+25\)

*Substitution spot-checks at \(x=1\):* #6: \((-1)(8)=-8\), and \(1+5-14=-8\). #9: \((1)(6)=6\), and \(3+13-10=6\). #11: \((4)^2=16\), and \(1+6+9=16\).

---

## Wrap-up & interleaving

**Consolidate:** The student should leave able to (1) simplify with the exponent rules and *explain* the zero/negative cases from the quotient rule, (2) move fluidly between standard and scientific notation, (3) add/subtract polynomials with the subtraction sign-trap handled, and (4) multiply binomials with the area model, always producing the middle term. The throughline: **multiplying builds expressions up; Unit 11 will take them apart.**

**Mix back in (interleaving, pedagogy.md):**
- Keep re-running the **distribute-the-negative** trap (10.3 subtraction) — it's the same Unit 2 §3 error and the one most likely to relapse; pair it with a quick substitution check every time.
- Revisit the **add-vs-multiply exponents** distinction (10.1) inside 10.4 problems (\(2x\cdot x=2x^2\)) so it stays sharp.
- Whenever a base is negative, re-surface \(-3^2\) vs. \((-3)^2\) (Unit 1, misconceptions.md §3).
- Foreshadow Unit 11 explicitly at every \((x+2)(x+3)=x^2+5x+6\): "remember this pair — next unit we start from the right side and hunt for the left."
- Where natural, name a result as a **function**: \(P(x)=x^2+5x+6\) is the rule we just built (callback to Unit 4's \(f(x)\)).

**Progress Card should note:**
- Which lessons are solid (e.g. "10.1–10.2 fluent; exponent rules explained, not just memorized").
- Whether the student can **re-derive** \(x^0=1\) and \(x^{-a}=\tfrac{1}{x^a}\) or is leaning on memory.
- Whether the **subtraction sign-trap** (10.3) and the **middle term** (10.4) are reliable yet.
- Any lingering **add-vs-multiply exponent** confusion.
- Tone/detail preference.

Example:
```
ALGEBRA PROGRESS CARD
Unit/Lesson: 10.4 — Multiplying polynomials
Mastered: 10.1–10.3; derives x^0 and x^-a from the quotient rule
Watch for: occasionally drops the middle term on (x+a)^2 — area box fixes it
Last problem: (x+2)(x+3) → x^2 + 5x + 6
Next up: finish 10.4, then Unit 11 (factoring = this, run backward)
Tone preference: medium detail
```
