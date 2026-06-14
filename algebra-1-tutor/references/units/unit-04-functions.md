# Unit 4: Introducing Functions

> **Prerequisites:** Unit 2 (solving and evaluating expressions). Helped by Unit 3 — the *unit rate* idea returns here as a function's constant rate of change.
> **By the end, the student can:**
> - Decide whether a rule, a table, a set of pairs, or a graph is a function (one input → exactly one output; the vertical line test).
> - Read and use f(x) notation; evaluate a function at a number and at a simple expression; explain why f(x) is *not* multiplication.
> - State the domain and range from a small table or list, and for a line.
> - Move the *same* relationship between table, graph, equation, and words, and tell linear from nonlinear from any of those.

## Teaching this unit (orientation for the tutor)

Functions are the backbone of everything after this unit — once a student owns them, every later topic (lines, systems, sequences, quadratics) gets *narrated in function language*. So the goal here is fluency and comfort, not speed. From this unit on, when a line or rule shows up, name it as a function: "this line *is* a function; f(x)=2x+1 just names it."

The arc is: (4.1) build the *one-output-per-input* idea with the **vending-machine** picture and the vertical line test; (4.2) name the rule with **f(x)** notation using the **recipe** picture, then pin down domain and range; (4.3) show that table ↔ graph ↔ equation ↔ words are four faces of *one* relationship, and split linear from nonlinear (constant rate of change → the seed of slope, forward to Unit 5).

**The three biggest traps:**
1. **"Two outputs is fine."** Students often think *any* repetition breaks a function. The exact rule: two inputs *may* share an output (fine); one input may *not* have two outputs (broken). Drill the asymmetry directly.
2. **f(x) read as multiplication** — "f times x." This is the single most important fix in 4.2. Name it early, every time. (Ties to the variable misconception, `misconceptions.md` §2 — letter as object/operation.)
3. **Sign slips when evaluating at negatives**, e.g. f(-2) with a squared or doubled term. Lean on the substitution habit and `misconceptions.md` §3 (negatives).

**Pacing:** an adult who already evaluates expressions can move briskly through 4.1–4.2; spend the saved time on 4.3's representation-translation, which is where durable understanding lives. Use the **backward-faded** evaluation scripts from `pedagogy.md` if notation feels shaky. Interleave: every evaluation is also an order-of-operations and a negatives rep — call that out as a free callback to Units 1–2.

---

## Lesson 4.1: What is a function

**Goal:** Decide whether a rule, table, set of pairs, or graph is a function — using "each input gives exactly one output."

**Why it matters:** "Function" is the word the rest of the course is built on. Lines, sequences, and parabolas are all functions; getting the defining rule clean now pays off in every later unit.

**New terms:**
- **Function** — a rule that assigns to each *input* exactly **one** *output*.
- **Input / output** — what you feed the rule, and what comes back. (Later called the variable and its value; in pairs (input, output).)
- **Vertical line test** — a graph is a function exactly when **no vertical line** crosses it more than once.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete (vending machine — `metaphors.md` Functions A):** "Press a button (input), get exactly one snack (output). Press B4 today and tomorrow — same snack both times. That reliability *is* what makes it a function." Then the key asymmetry: "Two different buttons can both give pretzels — two inputs, one output, totally fine. But one button can *not* sometimes give pretzels and sometimes give a soda — that machine is broken. One input, two outputs = not a function."
- **Pictorial (input → output table / arrow map):** draw inputs on the left, outputs on the right, arrows between. It's a function if **every input has exactly one arrow leaving it**. Repeated *outputs* (two arrows landing on the same right-hand value) are fine; a *split input* (two arrows leaving one left-hand value) breaks it.
- **Symbolic / graphical (vertical line test):** on a graph, an input is an x-value; a vertical line is "all the points with that one x." If a vertical line hits the graph twice, that input has two outputs → not a function. Walk a finger left-to-right as an imaginary vertical line.

Always restate the rule as a one-liner the student can repeat: *"Each input, exactly one output. Repeats are only a problem on the input side."*

**Worked examples:**

*Example 1 — a set of pairs.* Is {(1,2),(2,4),(3,6),(4,8)} a function?
Inputs are 1,2,3,4 — all different, each appears once, so each has exactly one output. **Yes, a function.**

*Example 2 — a repeated output (still fine).* Is {(1,5),(2,5),(3,5)} a function?
The output 5 repeats, but look at the *inputs*: 1,2,3, each appears once with one output. Repeated outputs are allowed. **Yes, a function.** (This is the "two buttons, same snack" case.)

*Example 3 — a split input (broken).* Is {(1,2),(1,3),(2,4)} a function?
Input 1 is paired with both 2 *and* 3 — one input, two outputs. **No, not a function.**

*Example 4 — a table.*

| input x | 0 | 1 | 2 | 0 |
|---|---|---|---|---|
| output | 4 | 5 | 6 | 9 |

Input 0 appears twice, giving 4 once and 9 once — two outputs for one input. **No, not a function.**

*Example 5 — a graph (vertical line test).* A straight line such as y=2x+1: sweep a vertical line across it — it touches exactly once everywhere. **Function.** A circle or a sideways "U" (parabola opening rightward): a vertical line through the middle hits it **twice**. **Not a function.**

**Watch for:**
- **"Any repeat means it's not a function."** Tell: student rejects {(1,5),(2,5)}. Repair: back to the vending machine — "two buttons, same snack: is the machine broken? No." Then point only at the *input* column. (Root: same asymmetry as `misconceptions.md` §2 — read what the structure actually says, not a memorized "no repeats" rule.)
- **Vertical vs. horizontal line confusion.** Tell: student sweeps a *horizontal* line. Repair: "an input is an x; the line that gathers one x's points is *vertical*."

**Visuals to offer:** A clean arrow-map (inputs→outputs) reads fine as plain text or a small table — no artifact needed. For the vertical line test, offer an **SVG artifact** of a line vs. a sideways parabola with a dashed vertical test line (`visuals.md` Template 2 for the line; compute points, label the double-hit). Pair any picture with the one-line rule.

**Check for understanding (transfer):**
1. "Make me a set of three pairs that is *not* a function, and tell me which input breaks it."
2. "Here's a table where the output 7 shows up three times — can it still be a function? What would I have to check?"
3. "Why does the *vertical* line test, and not a horizontal one, decide it?"

**Practice problems:**

*A. Sets of pairs — function or not? (give the reason)*
1. {(0,1),(1,2),(2,3)}
2. {(2,4),(3,4),(5,4)}
3. {(1,1),(1,2),(3,4)}
4. {(-1,0),(0,1),(1,0)}
5. {(5,5),(5,6)}

*B. Tables — function or not?*
6. inputs 1,2,3,4 → outputs 2,2,2,2
7. inputs 3,4,3 → outputs 1,2,8
8. inputs -2,-1,0,1 → outputs 4,1,0,1

*C. Descriptions / graphs — function or not?*
9. "Each person is matched to their birth year." (input = person)
10. "Each birth year is matched to a person born then." (input = year)
11. The graph of a single straight line.
12. The graph of a circle.

**Answer key:**
1. **Function** — inputs 0,1,2 all distinct.
2. **Function** — output 4 repeats, but inputs 2,3,5 are distinct (two buttons, same snack).
3. **Not a function** — input 1 gives both 1 and 2.
4. **Function** — output 0 repeats, but inputs -1,0,1 are distinct.
5. **Not a function** — input 5 gives both 5 and 6.
6. **Function** — inputs all distinct; identical outputs are allowed.
7. **Not a function** — input 3 appears twice with outputs 1 and 8.
8. **Function** — inputs -2,-1,0,1 distinct; repeated output 1 is fine.
9. **Function** — each person has exactly one birth year.
10. **Not a function** — a year can match many people (one input → many outputs).
11. **Function** — passes the vertical line test.
12. **Not a function** — a vertical line through it hits twice.

---

## Lesson 4.2: Function notation f(x), domain & range

**Goal:** Read and use f(x); evaluate at numbers and simple expressions; state domain and range.

**Why it matters:** f(x) is the standard language for "the output of this rule at this input." Every later unit writes lines, systems, and curves this way, so comfort here removes friction everywhere after.

**New terms:**
- **Function notation f(x)** — a *name* for a rule (f) together with what you fed it (x). Read "f of x." It is **not** "f times x."
- **Evaluate** — substitute a value for the input and compute. f(2) means "run 2 through the rule f."
- **Domain** — the set of allowed inputs.
- **Range** — the set of outputs you actually get.

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete (recipe — `metaphors.md` Functions B):** "f(x)=3x-1 is the recipe *triple it, then subtract one*. The name of the recipe is f. The thing in the parentheses is what you drop into the bowl. f(2) = 'run 2 through the recipe': 3(2)-1=5." Say plainly: "The parentheses here mean *feed this in*, not *multiply*."
- **Pictorial (the machine with a readout):** input goes in the top, the rule runs, the output f(2)=5 appears on the display. Domain = every input the machine accepts; range = every output that can light up.
- **Symbolic:** f(2)=3(2)-1=6-1=5. Show the substitution explicitly with parentheses *around* the input — that's the habit that survives negatives. Then evaluate at an *expression*: f(a+1)=3(a+1)-1=3a+3-1=3a+2 — "feed a+1 wherever x was."

For domain and range, stay concrete: from a *table or list*, the domain is just the input column and the range is the (de-duplicated) output column. For a *line* like f(x)=3x-1, any real number is an allowed input and any real number can come out, so domain and range are both **all real numbers**.

**Worked examples:**

*Example 1 — f(x)=3x-1 at several inputs.*
$$f(2)=3(2)-1=5,\quad f(0)=3(0)-1=-1,\quad f(-2)=3(-2)-1=-6-1=-7.$$
Note the parentheses around -2: they keep the sign honest (`misconceptions.md` §3).

*Example 2 — "not multiplication."* If a student writes f(2)=f·2: there is no number f; f is the *name of the rule*. f(2) is "the rule's output at 2." Re-evaluate together: 3(2)-1=5.

*Example 3 — g(x)=x²+1.*
$$g(3)=3^2+1=9+1=10,\quad g(0)=0+1=1,\quad g(-2)=(-2)^2+1=4+1=5.$$
Stress (-2)²=4, not -4 — square the *whole* input (`misconceptions.md` §3, the -3² vs (-3)² tell).

*Example 4 — evaluate at an expression.* With f(x)=3x-1:
$$f(2a)=3(2a)-1=6a-1.$$
"Whatever sits in the parentheses goes everywhere x was."

*Example 5 — domain & range from a table.* For

| x | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| f(x) | 5 | 5 | 7 | 9 |

**Domain** = {1,2,3,4}; **Range** = {5,7,9} (list each output once).

**Watch for:**
- **f(x) as multiplication** — the headline misconception of this lesson. Tell: "f(2)=2f" or treating f as a number. Repair: name it — "f is the recipe's *name*; the parentheses say *what we fed it*." Re-read it aloud as "f of 2."
- **Sign loss at negatives** (`misconceptions.md` §3). Tell: g(-2)=-3 (computed -2²+1). Repair: "substitute with parentheses: (-2)². What is a negative squared?"
- **Listing the range with duplicates.** Range is a *set* — list 5 once even if it appears twice.

**Visuals to offer:** none needed for evaluation. For domain/range of a *line*, a small **SVG line graph** (`visuals.md` Template 2) with a sentence — "the line runs left-to-right forever and up-down forever, so domain and range are all real numbers" — helps the "all reals" idea land.

**Check for understanding (transfer):**
1. "With h(x)=2x+1, find h(-3), and tell me each step out loud."
2. "Someone reads f(5) as 'f times 5'. In one sentence, what's wrong?"
3. "Give me the domain and range of {(0,2),(1,2),(2,8)} — and explain why 2 is written once in the range."

**Practice problems:**

*A. Evaluate f(x)=3x-1.*
1. f(2)
2. f(0)
3. f(-2)
4. f(5)
5. f(-1)

*B. Evaluate g(x)=x²+1.*
6. g(3)
7. g(0)
8. g(-2)
9. g(1)

*C. Evaluate (mixed rules).*
10. q(x)=5-2x: find q(4)
11. r(x)=x²-3: find r(-3)
12. p(x)=4x+2: find p(-1)

*D. Domain & range (from the explicit data).*
13. State domain and range of {(1,3),(2,6),(3,9)}.
14. State domain and range of {(-2,4),(-1,1),(0,0),(1,1)}.
15. State the domain and range of the line f(x)=3x-1.

**Answer key:**
1. f(2)=5  2. f(0)=-1  3. f(-2)=-7  4. f(5)=14  5. f(-1)=-4
6. g(3)=10  7. g(0)=1  8. g(-2)=5  9. g(1)=2
10. q(4)=5-8=-3  11. r(-3)=9-3=6  12. p(-1)=-4+2=-2
13. Domain {1,2,3}, Range {3,6,9}.
14. Domain {-2,-1,0,1}, Range {0,1,4} (output 1 listed once).
15. Domain: all real numbers; Range: all real numbers.

---

## Lesson 4.3: Multiple representations; linear vs. nonlinear

**Goal:** Move one relationship between table, graph, equation, and words; tell linear from nonlinear.

**Why it matters:** A function rarely arrives in your preferred form. Reading the *same* relationship as a table, a picture, an equation, or a sentence — and spotting when it's a straight line — is exactly the fluency Unit 5 (graphing, slope) and Unit 9 (linear vs. exponential) build on.

**New terms:**
- **Linear function** — constant rate of change; its graph is a straight line; its equation has the form y=mx+b (equivalently f(x)=mx+b).
- **Constant rate of change** — equal steps in x always produce equal steps in the output. (This *is* the unit rate from Unit 3, and it becomes **slope** in Unit 5.)
- **Nonlinear function** — rate of change is *not* constant; the graph curves (e.g. y=x²).

**Teaching arc (concrete → pictorial → symbolic):**
- **Concrete / words:** "*Start with $1, add $2 every step*" is the same relationship as the rule f(x)=2x+1, as a table, and as a straight-line graph. Build the table together to see the words become numbers.
- **Pictorial (table → graph):** plot the table's pairs; equal x-steps with equal output-steps make the dots fall in a straight line. The **constant difference** in the output column is what your eye sees as a straight line, and what Unit 5 will call slope.
- **Symbolic (spot linear from a table):** "Equal steps in x give equal steps in y" ⇒ linear. If the differences themselves change, it's nonlinear (it curves). Connect to Unit 3: the constant step is the *unit rate*; forward to Unit 5: it's the slope m in y=mx+b.

**Worked examples:**

*Example 1 — build a table from f(x)=2x+1; note the constant step.*

| x | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| f(x)=2x+1 | 1 | 3 | 5 | 7 |

Output differences: 3-1=2, 5-3=2, 7-5=2 — **constant +2** for each +1 in x. **Linear.** That constant +2 is the rate of change (the future slope).

*Example 2 — contrast with y=x².*

| x | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| y=x^2 | 0 | 1 | 4 | 9 |

Differences: 1-0=1, 4-1=3, 9-4=5 — 1,3,5, **not constant**. **Nonlinear** (this curve is a parabola — preview of Unit 12).

*Example 3 — linear-or-not from a table (no equation given).*

| x | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| y | 1 | 4 | 7 | 10 |

Equal x-steps of +1; output steps 3,3,3 — constant. **Linear.** (Rule: y=3x-2.)

*Example 4 — same relationship, four faces.*
- **Words:** "start at $1, add $2 each step."
- **Equation:** f(x)=2x+1.
- **Table:** the table from Example 1.
- **Graph:** a straight line through (0,1) rising 2 for every 1 right.

All four describe one function. Translating among them is the whole skill.

**Watch for:**
- **Checking y-differences without checking x-steps.** The "constant difference ⇒ linear" shortcut only works when the x-values step *evenly*. Tell: a student calls a table linear when x jumps 1,2,4,8. Repair: "Are the inputs evenly spaced first? Then check the outputs."
- **"Curved means broken/not a function."** Nonlinear is still a function (callback to 4.1's vertical line test) — it just isn't a straight line.
- **Sign slips filling x² at negatives** (`misconceptions.md` §3) if you extend the parabola table leftward.

**Visuals to offer:** **SVG artifacts** — Template 2 for the straight line from Example 1, Template 3 for the y=x² parabola from Example 2 (compute the points, label them). Showing the two side by side makes "straight vs. curved" unmistakable. Pair each with its difference row in words.

**Check for understanding (transfer):**
1. "Here's a table with x = 0,1,2,3 and y = 2,2,2,2. Linear or not? What's its rate of change?"
2. "Turn the words *'start at 10 and lose 1 each step'* into an equation and a four-row table."
3. "A table's outputs go 2, 6, 12, 20 for x=1,2,3,4. Linear or nonlinear — and how can you tell without graphing?"

**Practice problems:**

*A. Fill the table from the rule.*
1. f(x)=3x: find outputs at x=0,1,2,3,4.
2. k(x)=10-x: find outputs at x=0,1,2,3.
3. f(x)=2x+1: find outputs at x=-2,-1,0,1.

*B. Linear or nonlinear? (equal x-steps; check the output differences)*
4. x:0,1,2,3 → y:1,4,7,10
5. x:0,1,2,3 → y:0,1,4,9
6. x:1,2,3,4 → y:5,5,5,5
7. x:0,1,2,3 → y:1,2,4,8

*C. Match the representation.*
8. Which equation matches the words *"start at $1 and add $2 each step"*: (a) f(x)=x+2, (b) f(x)=2x+1, (c) f(x)=2x?

**Answer key:**
1. 0,3,6,9,12 — constant +3, linear.
2. 10,9,8,7 — constant -1, linear.
3. -3,-1,1,3 — constant +2, linear.
4. **Linear** — output steps 3,3,3.
5. **Nonlinear** — steps 1,3,5 (this is y=x²).
6. **Linear** — steps 0,0,0 (a constant/horizontal function; rate of change 0).
7. **Nonlinear** — steps 1,2,4 (doubling; previews exponential, Unit 9).
8. **(b)** f(x)=2x+1 — start 1 at x=0, add 2 per step.

---

## Wrap-up & interleaving

**Consolidate:** the one-output-per-input rule and the vertical line test (4.1); f(x) as a *named rule you feed a value* — never multiplication — plus domain/range from explicit data (4.2); and the table ↔ graph ↔ equation ↔ words quartet with the linear/nonlinear split (4.3).

**Mix back in:** every evaluation is also an order-of-operations and a negatives drill (Units 1–2) — call that out. The constant rate of change in 4.3 *is* Unit 3's unit rate, and it becomes **slope** in Unit 5 — name that bridge explicitly. A good warm-up before Unit 5 is "build a table from f(x)=mx+b and read off its constant step."

**Thread function language forward:** from here on, narrate lines, systems, and curves as functions — "this line *is* a function; f(x)=2x+1 just names it." Unit 5 graphs them, Unit 9 contrasts linear vs. exponential functions, Unit 12 graphs quadratic functions.

**Progress Card should note:** Can the student state the function rule cleanly? Do they read f(x) correctly (not as multiplication)? Are they fluent evaluating at negatives without sign slips? Can they classify linear vs. nonlinear from a table? Flag any lingering "any repeat breaks it" or "f(x) = times" tells for a quick callback next session.
