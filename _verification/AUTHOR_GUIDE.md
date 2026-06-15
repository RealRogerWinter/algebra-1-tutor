# Unit-File Author Guide (build tooling — NOT shipped in the skill)

You are authoring ONE unit file for an **Algebra 1 tutoring skill that runs on Claude.ai**. Read this entire guide, then author your assigned unit.

## Audience of the file you're writing
The unit file is **read by the tutor (an AI), not shown directly to students**. Write it as clear teaching *guidance + content the tutor draws from* — not as student-facing prose, and not as a worksheet. The persona, teaching methods, hint ladder, verification habit, LaTeX rules, and visual rules are ALREADY defined in sibling files (`SKILL.md`, `references/misconceptions.md`, `references/metaphors.md`, `references/visuals.md`, `references/pedagogy.md`). **Do not duplicate them — reference them by name** where relevant.

## Write TWO files

Paths are relative to the repo root.

1. **Unit content:** `algebra-1-tutor/references/units/unit-NN-slug.md` (two-digit NN and a short slug, e.g. `unit-02-linear-equations.md`).
2. **Verification data:** `_verification/unit-NN.json`.

> This guide covers the **tutor-facing** unit file. The course also ships a warm **student-facing** rewrite under `textbook-src/` that must keep the same math, answers, and reference codes. See [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the dual-source workflow, the house voice, and the full edit-and-verify loop.

## Conventions
- Display math in **`$$...$$`** blocks. **Inline math is plain Unicode** (x², √12, ½, ±, ≤, →) — **never** `\(...\)` or lone `$...$` (they show as raw text on Claude.ai). Escape literal currency as `\$`.
- Treat every concept beyond arithmetic as a **first introduction**; define each new term plainly the first time it appears.
- Keep it concise and tutor-usable. Warm in spirit but this is guidance, not a lecture.
- Reference the right misconception section (e.g. "see misconceptions.md §3 negatives") and the right visual template (e.g. "visuals.md Template 3 — parabola") rather than re-explaining them.
- If your unit introduces or uses functions, thread **function language** (e.g. "this line *is* a function; f(x)=2x+1 names it") per the course design.

## Notation reference (inline math → Unicode)

Display math goes in `$$ … $$` blocks (LaTeX is fine inside). **Inline** math is plain Unicode — never `\(…\)`, `\[…\]`, or single-`$…$`, and no `\macro` outside a `$$` block (`check_notation.py` flags these). Common conversions:

- Exponents → superscripts: `x^2` → x², `x^3` → x³, `^{-2}` → ⁻², `^n` → ⁿ (digits ⁰¹²³⁴⁵⁶⁷⁸⁹, plus ⁻ ⁿ).
- Fractions → slash form; parenthesize when multiplied by a variable: `2/3`, `(2/3)x`, `x/3`.
- Roots and symbols: √12, ±, ∓, ≤, ≥, ≠, ×, ·, ÷, →, ⇒, ≈, ∞, π, θ, °.
- Inside markdown **table cells**, use ASCII (`x^2`, `-3`, `1/2`) — Unicode superscripts and fraction glyphs can drop out in some table renderers.
- Currency is a bare `$` in prose, kept well clear of any `$$` block.
- No emoji and no ✓/✗ marks; confirm correctness by writing "Correct" or showing the substitution.

Promote anything too tangled for clean inline Unicode (stacked fractions, big radicals, the quadratic formula) into its own `$$ … $$` block rather than forcing ugly inline text.

## Reference-code anchors

Referenceable items carry an inline **reference code** so a student (and the HTML textbook) can point to one exact thing (see `SKILL.md` → "Reference codes"; full grammar in [`CONTRIBUTING.md`](../CONTRIBUTING.md) → "Reference codes"). Add anchors as you author, in document order.

- **Syntax:** `{#code}`. Trailing on a heading (`## Template 1 — … {#vis.t1}`); leading on a list item or bold-led paragraph, right after the marker (`- {#1.1.d1} **Variable:** …`). Plain text, no backslashes, so `check_notation.py` stays clean. **Never** anchor the `# Unit N:` H1 or a `## Lesson N.M:` header — `generate.py` parses those lines.
- **Tags:** `scope.lesson.tag+index`. `d` definition (new term), `c` transfer-check, `h` how-to/procedure, `f` figure (reserve the anchor where a figure will live — do not draw it; figures are Phase 3). `w` worked example and bare-number practice already exist as JSON ids.
- **What to anchor:** every **New terms** definition (`d1`, `d2`, … in order) and every **Check for understanding** prompt (`c1`, `c2`, …). Add an `h` only where the lesson states an explicit, reusable, multi-step method; add an `f` only where **Visuals to offer** names a real figure.
- **What needs no anchor:** worked examples (`wK`) and practice problems (`K`) are found by their visible number — leave them un-anchored.
- **Append-only:** a code is a stable reference. Assign the next free index in document order; never renumber an existing one. `md_anchor_lint` (in `check_alignment.py`) enforces grammar, global uniqueness, and dense per-group indices.

## Required structure of the unit `.md`

```
# Unit N: Title

> **Prerequisites:** ...
> **By the end, the student can:** ... (a few bullet outcomes)

## Teaching this unit (orientation for the tutor)
A short paragraph: the arc of the unit, the biggest misconception traps, pacing advice, and any threading (e.g. function language, callbacks to earlier units).

## Lesson N.1: Title
**Goal:** one sentence.
**Why it matters:** 1–2 sentences (motivation / where it's used later).
**New terms:** bulleted plain-language definitions (only genuinely new ones).
**Teaching arc (concrete → pictorial → symbolic):** a short script the tutor can follow; name the metaphor/visual to use (reference metaphors.md / visuals.md).
**Worked examples:** 3–5, fully worked in LaTeX, each VERIFIED correct.
**Watch for:** the specific misconception(s) live in this lesson + the tell; point to the misconceptions.md section.
**Visuals to offer:** which visuals.md template applies (or "none needed").
**Check for understanding (transfer):** 2–3 transfer prompts (never yes/no).
**Practice problems:** grouped by type, ~8–15 total, increasing difficulty, numbered.
**Answer key:** human-readable, ALL VERIFIED.

## Lesson N.2: ... (repeat) ...

## Wrap-up & interleaving
What to consolidate; which earlier skills to mix back in; what the Progress Card should note when the student finishes this unit.
```

For lessons that are conceptual (e.g. "what is a function", "the coordinate plane"), practice can be a mix of short-answer/conceptual and computational — that's fine; mark the conceptual ones "manual" in the JSON.

## Depth
Match the depth of a well-built lesson: 3–5 worked examples and 8–15 practice problems per lesson. For units given only as a sketch in your assignment, **author full content** to this depth. Keep numbers clean and pedagogically chosen (e.g. introduce negatives only after the procedure is solid, as the source curriculum does).

## VERIFICATION (critical — do this before writing)
Every numeric/algebraic answer MUST be correct. A wrong answer key becomes wrong teaching. Use **Python + sympy** (run via Bash, e.g. `python -c "import sympy as s; ..."`) to verify each computational answer. Then record every computational problem in the JSON so it can be re-checked centrally.

### JSON schema for `unit-NN.json`
```json
{
  "unit": 2,
  "problems": [
    {"id": "2.2.1",  "kind": "solve",        "eq": "2*x+1=9",      "var": "x", "answer": "4"},
    {"id": "2.1.16", "kind": "solve",        "eq": "x/2=6",        "var": "x", "answer": "12"},
    {"id": "1.3.5",  "kind": "eval",         "expr": "3+4**2",                 "answer": "19"},
    {"id": "refA.4", "kind": "simplify",     "expr": "2/3+1/4",                "answer": "11/12"},
    {"id": "2.3.2",  "kind": "simplify",     "expr": "3*x+2*x",                "answer": "5*x"},
    {"id": "10.4.1", "kind": "expand",       "expr": "(x+2)*(x+3)",            "answer": "x**2+5*x+6"},
    {"id": "11.2.1", "kind": "factor_check", "expr": "x**2+5*x+6",             "answer": "(x+2)*(x+3)"},
    {"id": "1.2.1",  "kind": "manual",                                         "answer": "integer, rational"}
  ]
}
```
Rules:
- **Python syntax** in all expressions: `*` multiply, `**` power, `/` divide, explicit parentheses; single-letter variables.
- `solve`: `eq` is `"lhs=rhs"`; `var` the variable; `answer` the solution. Multiple solutions → comma-separated, e.g. `"3,-3"`.
- Line-equation `solve` problems (find the intercept `b`, template `m*x0+b=y0`) MUST also carry
  `on_line`: the given point(s) as `[[x,y],...]`, plus `slope` for one-point (point+slope)
  problems. The point-on-line lint rebuilds the line and cross-checks it against the .md answer key.
- `eval`: pure-number expression; `answer` is the value (a fraction like `"3/4"` is fine).
- `simplify` / `expand`: `answer` is an equivalent expression; the checker tests algebraic equality.
- `factor_check`: `answer` multiplies back to `expr`; checker tests `expand(answer) == expand(expr)`.
- `manual`: for classify-the-number, ratios written as `a:b`, conceptual, or word problems not auto-checkable — still give the human answer; the auto-checker skips these.
- Include **every computational practice problem** (and any worked-example result worth checking). Put conceptual ones as `manual`.
- The `id` should match the problem's number in the `.md` (e.g. lesson 2.2 problem 1 → `"2.2.1"`; fraction refresher A problem 4 → `"refA.4"`).

### Self-check before writing
Write a quick Python snippet that loads your JSON, and for each non-`manual` problem confirms the answer checks out (solve/eval/simplify/expand/factor_check as above). Fix any mismatch — if the source's answer is wrong, correct it and note it. Only then write the two files.

## Return
A 2–3 line summary: the two file paths, the lesson count, and the problem count (auto-checked / manual), plus any source answer-key errors you corrected.
