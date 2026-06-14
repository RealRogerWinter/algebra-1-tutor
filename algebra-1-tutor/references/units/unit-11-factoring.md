# Unit 11: Factoring

> **Prerequisites:** Unit 10 (multiplying polynomials — the area box and distribution), the distributive property and combining like terms (Unit 2.3), and comfort with negatives (Unit 1.4 / misconceptions.md §3).
> **By the end, the student can:**
> - Factor out the greatest common factor (GCF) — numbers *and* variables — from any polynomial, e.g. \(15x^3-10x^2=5x^2(3x-2)\).
> - Factor a trinomial \(x^2+bx+c\) by finding two numbers that multiply to \(c\) and add to \(b\), reasoning correctly about signs.
> - Recognize and factor the two special patterns: difference of squares \(a^2-b^2=(a+b)(a-b)\) and perfect-square trinomials \(a^2\pm 2ab+b^2=(a\pm b)^2\).
> - **Check every factorization by multiplying it back out** — the central habit of the unit.

## Teaching this unit (orientation for the tutor)

The single framing that makes this whole unit click: **factoring is multiplying run backward.** In Unit 10 the student took factors and built a product (the area box, filled in); here they're handed the finished product and must rebuild the factors (the same area box, but deducing the edges). Keep the **reverse-distributing / area-box** picture (metaphors.md → Factoring A) live the entire time, and lean on the **"common item in every bag"** picture for GCF (metaphors.md → Factoring B).

Because factoring is multiplying backward, it comes with a *free, built-in answer key*: **multiply the factors back out and you must land on what you started with.** Model this check on *every* example, no exceptions — it ties straight back to Unit 10, it catches the slips a language model (and a student) will make, and it's the verification habit this course threads through everything (see Unit 2's substitution-check ritual; same spirit). A factorization that doesn't multiply back is simply wrong — say so out loud and re-do it.

The arc: **11.1** pulls a common factor out front (the inverse of single-term distribution); **11.2** reverses the area box for trinomials — *this is the load-bearing lesson*, because it's the skill that unlocks solving quadratics by factoring in Unit 12; **11.3** teaches the eye to *recognize* two patterns so they can be factored on sight.

**Biggest traps, in order of how often they bite:**
- **Not pulling the *greatest* common factor** — e.g. \(12x+18=2(6x+9)\), stopping early instead of \(6(2x+3)\). Tell: a common factor still lurks inside the parentheses. (11.1)
- **Sign reasoning in trinomials** (misconceptions.md §3 negatives, §7 structure). The two numbers' signs are *determined* by the signs of \(b\) and \(c\); getting them backward is the #1 trinomial error. (11.2)
- **Forgetting the middle-term check on perfect squares** — calling \(x^2+9\) or \(x^2+6x+9\) something it isn't. Difference of squares needs a *minus*; \(a^2+b^2\) does **not** factor over the reals. (11.3)
- **Combining-unlike-terms relapse** when checking by multiplying back (misconceptions.md §7) — watch the expansion step itself.

**Pacing:** 11.1 is usually quick — use it to cement the "multiply-back" check. Slow down at 11.2 and give it the most time; cover *all four sign cases* deliberately. 11.3 is pattern-recognition drill — fast once the eye is trained. Interleave Unit 10 throughout: every check *is* a Unit 10 expansion, so the two units reinforce each other (pedagogy.md → interleaving). Where natural, narrate in function language: "factoring \(x^2+5x+6\) finds where the function \(f(x)=x^2+5x+6\) will equal zero — that's Unit 12, and it starts here."

---

## Lesson 11.1: Greatest common factor (GCF)

**Goal:** Find the largest factor (numbers *and* variables) shared by **every** term and pull it out front, leaving the rest in parentheses.

**Why it matters:** GCF is the *first* thing to try on any factoring problem — pulling it out often shrinks a scary expression into something simple, and it's the inverse of the single-term distribution from Unit 2/10. It also sets up the multiply-back check the rest of the unit depends on.

**New terms:**
- **Factor (noun):** something multiplied. In \(6=2\cdot 3\), both \(2\) and \(3\) are factors of \(6\). In \(3(2x+3)\), the factors are \(3\) and \((2x+3)\).
- **Greatest common factor (GCF):** the *largest* factor — biggest number times the most variables — that divides evenly into **every** term.
- **Factor (verb):** to rewrite a sum as a product, i.e. to *undo* distributing.

**Teaching arc (concrete → pictorial → symbolic):**
- *Concrete (common item in every bag, metaphors.md → Factoring B):* Each term is a gift bag. If *every* bag contains a chocolate, you can take one chocolate out of each and set them in a single pile out front. \(6x+9\): both terms are divisible by \(3\), so \(3\) comes out front and what's left of each bag goes inside: \(3(2x+3)\).
- *Pictorial (reverse the area box, visuals.md → area-model):* GCF undoes a one-row box. \(4x^2+8x\) is the *inside* of a box whose left edge is \(4x\):
$$\begin{array}{c|c|c}
 & x & 2 \\ \hline
4x & 4x^2 & 8x
\end{array}\qquad\Rightarrow\qquad 4x^2+8x = 4x(x+2)$$
- *Symbolic — find the GCF in two parts:*
  1. **Numbers:** the biggest number dividing every coefficient (for \(4\) and \(8\), that's \(4\)).
  2. **Variables:** the *lowest* power of any variable present in every term (for \(x^2\) and \(x^1\), that's \(x^1\)).
  Multiply them: GCF \(=4x\). Then divide each term by the GCF to get the inside.

Lead Socratically (SKILL.md): "What's the biggest number that divides *both* \(15\) and \(10\)? ... And what's the most \(x\)'s that *every* term has?" Then **always** close with the check: "Multiply \(5x^2(3x-2)\) back out — do we get \(15x^3-10x^2\)? Then it's right."

**Naming the move honestly:** dividing \(8x\) by \(4x\) leaves \(2\), not \(0\) — the term doesn't disappear, it gets *smaller* by the factor we removed. (Heads off the "things vanish by magic" idea, misconceptions.md §1.)

**Worked examples** (each pulls the GCF, then checks by multiplying back):

*Numbers only:*
$$6x+9 \;=\; 3(2x+3) \qquad \text{Check: } 3\cdot 2x + 3\cdot 3 = 6x+9$$

*Number and a variable:*
$$4x^2+8x \;=\; 4x(x+2) \qquad \text{Check: } 4x\cdot x + 4x\cdot 2 = 4x^2+8x$$

*Higher powers — take the lowest power of \(x\):*
$$15x^3-10x^2 \;=\; 5x^2(3x-2) \qquad \text{Check: } 5x^2\cdot 3x - 5x^2\cdot 2 = 15x^3-10x^2$$
"Both terms have at least \(x^2\), so \(x^2\) comes out; \(\gcd(15,10)=5\), so \(5\) comes out — GCF \(=5x^2\)."

*The "stopped too early" trap, done right:*
$$12x+18 \;=\; 6(2x+3) \qquad \text{Check: } 6\cdot 2x + 6\cdot 3 = 12x+18$$
Note: \(2(6x+9)\) and \(3(4x+6)\) are common factors but **not the greatest** — the inside still shares a factor. Only \(6\) leaves an inside (\(2x+3\)) with nothing left to pull.

*Variable factor with a negative inside:*
$$10x^2-25x \;=\; 5x(2x-5) \qquad \text{Check: } 5x\cdot 2x - 5x\cdot 5 = 10x^2-25x$$

**Watch for:**
- **Not pulling the *greatest* factor** — \(12x+18=2(6x+9)\) and stopping. Tell: the parentheses still share a factor. Repair: "Look inside — do \(6x\) and \(9\) *still* have something in common? Then we didn't take it all." (misconceptions.md §7)
- **Forgetting the variable part** — \(4x^2+8x=4(x^2+2x)\), leaving an \(x\) behind. Repair: "Does *every* bag have at least one \(x\)? Then the \(x\) comes out too."
- **Taking too high a power** — \(15x^3-10x^2=5x^3(\dots)\). Repair: "The second term only has \(x^2\); you can't pull an \(x^3\) out of it. Take the *lowest* power present."
- **Sign slip on the inside** when a term is subtracted — \(10x^2-25x=5x(2x+5)\). The multiply-back check catches it instantly.

**Visuals to offer:** the one-row LaTeX `array` area-model box above (visuals.md → area-model) — show the GCF as the left edge and the inside as the top labels. No artifact needed.

**Check for understanding (transfer):**
1. "Factor \(8x^2+12x\), then prove it's right without me." (listen for the multiply-back check)
2. "A student writes \(6x+9=3(2x+9)\). Multiply it back — where did it go wrong?" (\(3\cdot 3=9\), so the \(9\) inside should be \(3\))
3. "Why can't you pull \(x^2\) out of \(15x^3-10x^2\) as \(x^2\) *and* also leave an \(x\) in the second term?" (the second term *is* the \(x^2\); nothing's left of it but the coefficient)

**Practice problems:**

*Numbers only:*
1. \(2x+6\)  2. \(5x+15\)  3. \(6x+9\)  4. \(4x-12\)  5. \(8x+20\)  6. \(9x-6\)

*With a variable:*
7. \(x^2+7x\)  8. \(3x^2+6x\)  9. \(10x^2-15x\)  10. \(4x^2+8x\)

*Higher powers (take the lowest power):*
11. \(6x^3-9x^2\)  12. \(14x^2+21x\)  13. \(12x^3+8x^2\)  14. \(18x^2-12x\)

**Answer key (all verified — multiply each back to confirm):**
1) \(2(x+3)\)  2) \(5(x+3)\)  3) \(3(2x+3)\)  4) \(4(x-3)\)  5) \(4(2x+5)\)  6) \(3(3x-2)\)  7) \(x(x+7)\)  8) \(3x(x+2)\)  9) \(5x(2x-3)\)  10) \(4x(x+2)\)  11) \(3x^2(2x-3)\)  12) \(7x(2x+3)\)  13) \(4x^2(3x+2)\)  14) \(6x(3x-2)\)

---

## Lesson 11.2: Factoring trinomials \(x^2+bx+c\)

**Goal:** Factor \(x^2+bx+c\) into \((x+m)(x+n)\) by finding two numbers that **multiply to \(c\)** and **add to \(b\)** — with the signs reasoned, not guessed.

**Why it matters:** This is the lesson the whole unit builds toward. It's the reverse of the binomial multiplication from Unit 10, and it's the key that unlocks **solving quadratics by factoring** in Unit 12 — once \(x^2+5x+6=(x+2)(x+3)\), setting it to zero is one short step away. Invest the most time here.

**New terms:**
- **Trinomial:** a polynomial with three terms, here \(x^2+bx+c\) (a squared term, an \(x\) term, and a constant).

**Teaching arc (concrete → pictorial → symbolic):**
- *Pictorial (reverse the area box, metaphors.md → Factoring A; visuals.md → area-model):* In Unit 10, \((x+2)(x+3)\) filled a box: corners \(x^2\) and \(6\), middle cells \(2x\) and \(3x\) that add to \(5x\). Factoring runs it **backward** — you're handed the inside and must find the edges:
$$\begin{array}{c|c|c}
 & x & \,? \\ \hline
x & x^2 & ?x \\ \hline
? & ?x & 6
\end{array}$$
The two unknown edges must **multiply to \(6\)** (the corner) and their \(x\)-terms must **add to \(5x\)** (the middle). That's exactly the question: *"What two numbers multiply to \(c\) and add to \(b\)?"*
- *Symbolic — the two-number search:* List factor pairs of \(c\); pick the pair that adds to \(b\). For \(x^2+5x+6\): pairs of \(6\) are \(1\cdot 6\) and \(2\cdot 3\); only \(2+3=5\). So \((x+2)(x+3)\).
- **Sign reasoning (the heart of the lesson)** — read the signs of \(c\) and \(b\):
  - **\(c>0\):** the two numbers have the **same sign** (their product is positive). Then \(b\) tells you which: \(b>0 \Rightarrow\) both **positive**; \(b<0 \Rightarrow\) both **negative**.
  - **\(c<0\):** the two numbers have **opposite signs** (their product is negative). The one with the larger absolute value carries the sign of \(b\).

| signs | \(c\) | \(b\) | the two numbers | example |
|---|---|---|---|---|
| both \(+\) | \(+\) | \(+\) | both positive | \(x^2+5x+6=(x+2)(x+3)\) |
| both \(-\) | \(+\) | \(-\) | both negative | \(x^2-5x+6=(x-2)(x-3)\) |
| opposite, sum \(+\) | \(-\) | \(+\) | bigger one positive | \(x^2+x-6=(x+3)(x-2)\) |
| opposite, sum \(-\) | \(-\) | \(-\) | bigger one negative | \(x^2-x-6=(x-3)(x+2)\) |

Lead Socratically: "We need two numbers. Their product is \(c=6\) — same sign or opposite? Their sum is \(b=5\). Which pair fits?" Then **check by multiplying back** every time (this is also a Unit 10 rep).

**Worked examples** (covering all sign cases; each checked by expanding back):

*Both positive (\(c>0,\ b>0\)):*
$$x^2+5x+6=(x+2)(x+3) \qquad \text{Check: } x^2+3x+2x+6 = x^2+5x+6$$
(\(2\cdot 3=6\), \(2+3=5\).)

*Both negative (\(c>0,\ b<0\)):*
$$x^2-5x+6=(x-2)(x-3) \qquad \text{Check: } x^2-3x-2x+6 = x^2-5x+6$$
(\(c\) positive ⇒ same sign; \(b\) negative ⇒ both negative. \((-2)(-3)=6\), \((-2)+(-3)=-5\).)

*Opposite signs, sum positive (\(c<0,\ b>0\)):*
$$x^2+x-6=(x+3)(x-2) \qquad \text{Check: } x^2-2x+3x-6 = x^2+x-6$$
(\(c\) negative ⇒ opposite signs; need product \(-6\), sum \(+1\): \(+3\) and \(-2\).)

*Opposite signs, sum negative (\(c<0,\ b<0\)):*
$$x^2-x-6=(x-3)(x+2) \qquad \text{Check: } x^2+2x-3x-6 = x^2-x-6$$
(Opposite signs; product \(-6\), sum \(-1\): the bigger number \(3\) is negative.)

*A bigger both-positive one:*
$$x^2+7x+12=(x+3)(x+4) \qquad \text{Check: } x^2+4x+3x+12 = x^2+7x+12$$
(Pairs of \(12\): \(1\cdot12,\ 2\cdot6,\ 3\cdot4\); only \(3+4=7\).)

*Opposite signs, larger gap:*
$$x^2-2x-15=(x-5)(x+3) \qquad \text{Check: } x^2+3x-5x-15 = x^2-2x-15$$
(Product \(-15\), sum \(-2\): \(-5\) and \(+3\); the bigger, \(5\), is negative because \(b<0\).)

**Watch for:**
- **Sign reasoning backward** (misconceptions.md §3) — e.g. writing \(x^2-5x+6=(x+2)(x+3)\) (forgot both must be negative) or \(x^2+x-6=(x-3)(x+2)\) (put the sign on the wrong number). Tell: the multiply-back gives the wrong middle term. Repair: "Is \(c\) positive or negative? Same sign or opposite? Now which sign does \(b\) force?"
- **Product/sum swapped** — finding numbers that *add* to \(c\) and *multiply* to \(b\). Repair: "Which one is the constant on its own — that's the product target."
- **Skipping the GCF first** — if every term shares a factor (e.g. \(2x^2+10x+12\)), pull it out *before* hunting the pair. (Out of scope for the practice below, which is monic, but mention it.)
- **No middle-term check** — accepting \((x+2)(x+3)\) for \(x^2+6x+6\) without expanding. Repair: always multiply back; the middle term is where errors surface (misconceptions.md §7).

**Visuals to offer:** the 2×2 LaTeX `array` area-model box (visuals.md → area-model), filled in *backward* — write the known corners (\(x^2\) and \(c\)) and let the student deduce the edges. Especially useful for a stuck student.

**Check for understanding (transfer):**
1. "Factor \(x^2+8x+15\), and tell me *why* both numbers are positive." (because \(c>0\) and \(b>0\))
2. "What changes between \(x^2+2x-8\) and \(x^2-2x-8\)? Factor both." (the sign of \(b\) flips which number is negative)
3. "A student says \(x^2-7x+12=(x+3)(x+4)\). Multiply it back — what's wrong, and what's the fix?" (gives \(+7x\); both factors should be negative: \((x-3)(x-4)\))

**Practice problems:**

*Both positive (\(c>0,\ b>0\)):*
1. \(x^2+5x+6\)  2. \(x^2+7x+10\)  3. \(x^2+8x+15\)  4. \(x^2+9x+20\)

*Both negative (\(c>0,\ b<0\)):*
5. \(x^2-5x+6\)  6. \(x^2-7x+12\)  7. \(x^2-8x+15\)  8. \(x^2-6x+8\)

*Opposite signs, sum positive (\(c<0,\ b>0\)):*
9. \(x^2+x-6\)  10. \(x^2+2x-8\)  11. \(x^2+3x-10\)

*Opposite signs, sum negative (\(c<0,\ b<0\)):*
12. \(x^2-x-6\)  13. \(x^2-2x-15\)  14. \(x^2-4x-12\)

**Answer key (all verified — multiply each back; watch the middle term):**
1) \((x+2)(x+3)\)  2) \((x+2)(x+5)\)  3) \((x+3)(x+5)\)  4) \((x+4)(x+5)\)  5) \((x-2)(x-3)\)  6) \((x-3)(x-4)\)  7) \((x-3)(x-5)\)  8) \((x-2)(x-4)\)  9) \((x+3)(x-2)\)  10) \((x+4)(x-2)\)  11) \((x+5)(x-2)\)  12) \((x-3)(x+2)\)  13) \((x-5)(x+3)\)  14) \((x-6)(x+2)\)

*Sign spot-checks:* #5: \((-2)(-3)=6\), \((-2)+(-3)=-5\). #11: \((+5)(-2)=-10\), \(5+(-2)=+3\). #14: \((-6)(+2)=-12\), \(-6+2=-4\).

---

## Lesson 11.3: Special patterns

**Goal:** Recognize two patterns on sight and factor them instantly: **difference of squares** \(a^2-b^2=(a+b)(a-b)\) and **perfect-square trinomials** \(a^2\pm 2ab+b^2=(a\pm b)^2\).

**Why it matters:** These show up constantly (and again in Unit 12). Spotting them saves the whole two-number search — and knowing \(a^2+b^2\) does **not** factor over the reals keeps the student from chasing impossible factorizations.

**New terms:**
- **Perfect square:** a quantity that is something squared. \(9=3^2\), \(x^2=(x)^2\), \(4x^2=(2x)^2\) are perfect squares; \(7\) and \(x\) are not.
- **Difference of squares:** one perfect square *minus* another, \(a^2-b^2\).
- **Perfect-square trinomial:** a trinomial that is exactly \((a\pm b)^2\) multiplied out.

**Teaching arc (concrete → pictorial → symbolic):**

*Difference of squares* — derive it, don't just state it. Multiply \((a+b)(a-b)\) with the area box (Unit 10): the middle terms \(+ab\) and \(-ab\) **add to zero**, leaving \(a^2-b^2\):
$$\begin{array}{c|c|c}
 & a & -b \\ \hline
a & a^2 & -ab \\ \hline
b & ab & -b^2
\end{array}\qquad\Rightarrow\qquad a^2 - ab + ab - b^2 = a^2-b^2$$
Run it **backward** to factor. *Recognizing it:* two perfect squares with a **minus** between them. Then \(a=\sqrt{\text{first}}\), \(b=\sqrt{\text{last}}\), and it splits into \((a+b)(a-b)\).
$$x^2-9=(x)^2-(3)^2=(x+3)(x-3)$$
*Crucial:* \(x^2+9\) (a **plus**) does **not** factor over the reals — there are no two real numbers multiplying to \(+9\) and adding to \(0\). Difference of squares needs the minus.

*Perfect-square trinomials* — these are \((x+k)^2\) expanded: \((x+3)^2=x^2+6x+9\). *Recognizing one:* the **first and last terms are perfect squares**, and the **middle term equals \(2\cdot\sqrt{\text{first}}\cdot\sqrt{\text{last}}\)**. For \(x^2+6x+9\): \(\sqrt{x^2}=x\), \(\sqrt{9}=3\), and \(2\cdot x\cdot 3=6x\) — matches, so it's \((x+3)^2\). The middle sign becomes the sign inside: \(x^2-10x+25=(x-5)^2\).

These are really *special cases* of Lesson 11.2 (the two numbers are equal for a perfect square; opposite for difference of squares), so the multiply-back check is identical — and still mandatory.

Lead Socratically: "Are both ends perfect squares? Is there a minus between them, or a middle term? ... If a middle term, does it equal twice the roots multiplied?" Then **check by expanding**.

**Worked examples** (each checked by multiplying back):

*Difference of squares — basic:*
$$x^2-9=(x+3)(x-3) \qquad \text{Check: } x^2-3x+3x-9 = x^2-9$$

*Difference of squares — larger:*
$$x^2-25=(x+5)(x-5) \qquad \text{Check: } x^2-5x+5x-25 = x^2-25$$

*Difference of squares with a coefficient (\(4x^2=(2x)^2\)):*
$$4x^2-1=(2x+1)(2x-1) \qquad \text{Check: } 4x^2-2x+2x-1 = 4x^2-1$$

*Perfect-square trinomial (plus):*
$$x^2+6x+9=(x+3)^2 \qquad \text{Check: } (x+3)(x+3)=x^2+3x+3x+9 = x^2+6x+9$$
(\(\sqrt{x^2}=x\), \(\sqrt9=3\), \(2\cdot x\cdot 3=6x\).)

*Perfect-square trinomial (minus):*
$$x^2-10x+25=(x-5)^2 \qquad \text{Check: } (x-5)(x-5)=x^2-5x-5x+25 = x^2-10x+25$$
(\(\sqrt{x^2}=x\), \(\sqrt{25}=5\), \(2\cdot x\cdot 5=10x\); minus ⇒ \((x-5)^2\).)

**Watch for:**
- **Trying to factor \(a^2+b^2\)** — e.g. "\(x^2+9=(x+3)(x-3)\)?" No: that multiplies back to \(x^2-9\). Sum of squares doesn't factor over the reals. Repair: "Multiply your answer back — do you get a plus or a minus?"
- **Mistaking a near-miss for a perfect square** — \(x^2+5x+9\) has square ends but \(2\cdot x\cdot 3=6x\neq 5x\), so it is **not** \((x+3)^2\). Repair: "Check the middle: does it equal twice the roots multiplied? If not, it's a regular 11.2 trinomial (or doesn't factor nicely)."
- **Dropping the coefficient's square root** — \(4x^2-1=(4x+1)(4x-1)\). Repair: "\(\sqrt{4x^2}\) is \(2x\), not \(4x\) — multiply back to see." (misconceptions.md §3/§7)
- **Sign of the middle ignored** in a perfect square — calling \(x^2-10x+25\) a \((x+5)^2\). The middle sign carries inside.

**Visuals to offer:** the difference-of-squares area box above (visuals.md → area-model) — the cancelling middle cells make the pattern visible. No artifact needed.

**Check for understanding (transfer):**
1. "Is \(x^2-16\) a difference of squares? Factor it, then multiply back to prove it." (\((x+4)(x-4)\))
2. "Can \(x^2+16\) be factored the same way? Why or why not?" (no — sum of squares; no real factorization)
3. "How do you tell \(x^2+6x+9\) (a perfect square) from \(x^2+6x+8\) (not one)? Factor each." (\((x+3)^2\) vs. \((x+2)(x+4)\) — check the middle against twice the roots)

**Practice problems:**

*Difference of squares:*
1. \(x^2-9\)  2. \(x^2-16\)  3. \(x^2-25\)  4. \(x^2-49\)  5. \(x^2-1\)  6. \(4x^2-9\)  7. \(9x^2-1\)

*Perfect-square trinomials:*
8. \(x^2+6x+9\)  9. \(x^2-10x+25\)  10. \(x^2+8x+16\)  11. \(x^2-4x+4\)  12. \(x^2+2x+1\)

**Answer key (all verified — multiply each back):**
1) \((x+3)(x-3)\)  2) \((x+4)(x-4)\)  3) \((x+5)(x-5)\)  4) \((x+7)(x-7)\)  5) \((x+1)(x-1)\)  6) \((2x+3)(2x-3)\)  7) \((3x+1)(3x-1)\)  8) \((x+3)^2\)  9) \((x-5)^2\)  10) \((x+4)^2\)  11) \((x-2)^2\)  12) \((x+1)^2\)

*Spot-checks:* #6: \((2x+3)(2x-3)=4x^2-9\). #10: \(2\cdot x\cdot 4=8x\), so \((x+4)^2\). #11: middle \(-4x=2\cdot x\cdot(-2)\), so \((x-2)^2\).

---

## Wrap-up & interleaving

**Consolidate:** The student should leave with a reliable order of attack for any factoring problem:
1. **GCF first** — always check whether a common factor pulls out (11.1).
2. **Count the terms.** Two terms → look for **difference of squares** (11.3). Three terms → check for a **perfect square**, else do the **two-number search** \(c\) and \(b\) (11.2/11.3).
3. **Multiply back to check — every time.** A factorization that doesn't expand to the original is wrong.

The unifying idea: *factoring is multiplying backward,* so Unit 10 *is* the answer key. That makes the check feel natural, not like extra work.

**Mix back in (interleaving, pedagogy.md):**
- Every multiply-back check is a **Unit 10 expansion** — keep both skills sharp by alternating "factor this" with "now expand it back."
- Re-run the **sign-reasoning** of 11.2 inside 11.3 problems (it's the same logic specialized).
- Warm up sessions with a quick GCF pull or a one-line trinomial before new material.
- **Function-language bridge to Unit 12:** "We just factored \(x^2+5x+6\) into \((x+2)(x+3)\). Next unit, setting \(f(x)=0\) and reading off \(x=-2,\,-3\) is one step away — you've already done the hard part."

**Progress Card should note:**
- Which lessons are mastered (e.g. "11.1–11.2 solid").
- Whether the **multiply-back check** is automatic yet.
- Any lingering **sign trap** in trinomials, **stopping short of the greatest** common factor, or **mis-recognizing** a special pattern (especially attempting \(a^2+b^2\)).
- Tone/detail preference.

Example:
```
ALGEBRA PROGRESS CARD
Unit/Lesson: 11.2 — Factoring trinomials
Mastered: 11.1 (GCF); multiply-back check is automatic
Watch for: sign reasoning when c < 0 (which number gets the minus)
Last problem: x^2 - 2x - 15  →  (x-5)(x+3)
Next up: finish 11.2, then 11.3 (special patterns) — sets up Unit 12
Tone preference: medium detail
```
