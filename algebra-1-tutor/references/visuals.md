# Visuals: Making Correct, Labeled Graphs as Artifacts

The student needs to *see* number lines, coordinate planes, lines, and parabolas. Two hard constraints shape how:

1. **No image generator exists**, and **raw SVG pasted into a chat message does not render** — it shows as code. To make a graphic the student actually sees, emit it as an **Artifact** (an SVG document, or a small self-contained HTML/React document). Artifacts render in a side panel.
2. **An LLM that eyeballs coordinates draws wrong curves.** A misshapen parabola or a line through the wrong intercept teaches a false picture — worse than no picture. So **always compute the coordinates** (plug x-values into the equation, ideally with the code tool) and build the artifact from those numbers.

Three rules that never change:
- **Compute, don't guess** the points. (And note: the numbers baked into the templates below are *examples for one specific equation*. When you graph a different equation, recompute every point for it — never copy a template's coordinates and hope they fit.)
- **Label** axes, scale, and key points (intercepts, vertex, slope).
- **Pair every visual with words** — a sentence or a small table of points — so it still helps if the panel doesn't open, and so it's accessible.

---

## When to use what

| Situation | Best medium |
|-----------|-------------|
| A single point or interval on a number line; an inequality solution like x>2 | **ASCII/Unicode in chat** (fast, friendly, no panel needed) |
| A clean labeled number line you want to look polished | **SVG artifact** |
| A coordinate plane with plotted points | **SVG artifact** |
| A graphed line y = mx+b | **SVG artifact** (two computed endpoints) |
| A parabola or any curve | **SVG artifact** (many computed sample points) |
| A 2-D inequality region (shading) | **SVG artifact** (boundary line + semi-transparent fill) |
| Something the student should *drag/tweak* to build intuition | **HTML/React artifact** with a slider (only when interactivity truly helps) |

Default to **SVG artifacts** for graphs and **ASCII** for simple number lines. Reach for HTML/React only when interaction is the point.

---

## ASCII / Unicode sketches (in-chat, always render)

Number line with a point at 3:
```
──┼────┼────┼────┼────●────┼────┼──
 -1    0    1    2    3    4    5
```
Inequality x > 2 (open circle = "not equal to 2", ray to the right):
```
──┼────┼────○━━━━━━━━━━━━▶
  0    1    2    3    4
```
Inequality x ≤ -1 (filled circle = "or equal to", ray left):
```
◀━━━━━━━●────┼────┼────┼──
       -1    0    1    2
```
A tiny slope intuition (rise over run):
```
y
│        ╱
│      ╱     up 2, right 1  →  slope 2
│    ╱
└────────── x
```
Always say in words what the picture shows ("filled circle means -1 is included").

### Balance scale (for "do the same to both sides")

The balance-scale picture is how Units 1–2 make the equals sign *mean* something: the two pans hold equal weight, so whatever you do to one pan you must do to the other or the scale tips. Sketch it in chat as Unicode; it always renders. (The metaphor itself lives in metaphors.md — Equations A, the balance scale; this is just the drawing recipe.)

A balanced equation x + 3 = 5 — equal pans, fulcrum (△) underneath:
```
   x + 3   │   5
  ┌─────┐  │  ┌─────┐
  │ x ◯◯◯│ = │◯◯◯◯◯│
  └──┬──┘  │  └──┬──┘
─────┴──────────┴─────
          △
```
"Do the same to both sides" = take the same off (or put the same on) **both** pans so it stays level. Subtract 3 from each pan:
```
   x       │   2
  ┌─────┐  │  ┌─────┐
  │ x   │ = │ ◯◯  │     (took 3 ◯ off EACH pan; still balanced → x = 2)
  └──┬──┘  │  └──┬──┘
─────┴──────────┴─────
          △
```
Always pair it with the symbolic step (x + 3 = 5 → x = 2) and say in words what kept it balanced ("3 off the left, so 3 off the right"). Tips to flag: removing from only one side tips the scale (the classic "did it to one side only" error), and multiplying both sides by a *negative* has no clean weight picture — switch metaphors there (see misconceptions.md §6 for the inequality-flip demonstration).

---

## The coordinate-mapping rule (use for every SVG graph)

Pick a viewBox and an origin, then map math coordinates to screen coordinates. SVG's y-axis points **down**, so y is *subtracted*.

For a plane showing roughly -5 to 5 on both axes at 20 px per unit, origin at screen (110, 110):

```
screenX = 110 + x * 20
screenY = 110 - y * 20      (note the minus: up on the page = larger y)
```

Compute each point with this, then drop the numbers into the templates below. **Use the code tool to generate the point list** for anything with a curve.

---

## Template 1 — Number line with a marked point (SVG artifact)

Maps value v to x = 60 + v·30. Filled dot = included; for an open endpoint use `fill="white" stroke="#c0392b" stroke-width="2"`. For an interval/ray, add a thick colored segment.

```svg
<svg viewBox="0 0 320 60" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
  <line x1="20" y1="30" x2="300" y2="30" stroke="#333" stroke-width="2"/>
  <g stroke="#333" stroke-width="1">
    <line x1="60"  y1="25" x2="60"  y2="35"/>
    <line x1="90"  y1="25" x2="90"  y2="35"/>
    <line x1="120" y1="25" x2="120" y2="35"/>
    <line x1="150" y1="25" x2="150" y2="35"/>
    <line x1="180" y1="25" x2="180" y2="35"/>
    <line x1="210" y1="25" x2="210" y2="35"/>
  </g>
  <g text-anchor="middle">
    <text x="60"  y="50">0</text><text x="90"  y="50">1</text>
    <text x="120" y="50">2</text><text x="150" y="50">3</text>
    <text x="180" y="50">4</text><text x="210" y="50">5</text>
  </g>
  <!-- point at x = 3  →  60 + 3*30 = 150 -->
  <circle cx="150" cy="30" r="5" fill="#c0392b"/>
  <text x="150" y="18" text-anchor="middle" fill="#c0392b">x = 3</text>
</svg>
```

## Template 2 — Coordinate plane + a line y = mx + b (SVG artifact)

Compute two convenient points from the equation, map them, draw a line between. Mark the y-intercept. Example shown: y = 2x - 1 (points (-2,-5) and (3,5) → screen (70,210) and (170,10)).

```svg
<svg viewBox="0 0 220 220" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11">
  <line x1="10" y1="110" x2="210" y2="110" stroke="#888"/>   <!-- x-axis -->
  <line x1="110" y1="10" x2="110" y2="210" stroke="#888"/>   <!-- y-axis -->
  <text x="203" y="124" fill="#888">x</text>
  <text x="116" y="18" fill="#888">y</text>
  <!-- gridline ticks every unit could be added; keep it clean -->
  <line x1="70" y1="210" x2="170" y2="10" stroke="#2980b9" stroke-width="2.5"/>
  <circle cx="110" cy="130" r="3.5" fill="#2980b9"/>          <!-- y-intercept (0,-1) -->
  <text x="116" y="142" fill="#2980b9">(0, -1)</text>
  <text x="150" y="40" fill="#2980b9">y = 2x - 1</text>
</svg>
```
General recipe: choose two x-values that keep both points on-screen, compute y=mx+b for each, map with `screenX=110+x*20`, `screenY=110-y*20`, draw the `<line>`, and dot the intercept.

## Template 3 — Parabola y = ax² + bx + c (SVG artifact)

Sample x in unit steps, compute y for each (use the code tool), map each point, and join with a `<polyline>`. Mark roots and the vertex. Example: y = x² - 4, points (-3,5)(-2,0)(-1,-3)(0,-4)(1,-3)(2,0)(3,5); origin (110,150), 20 px/unit (widen the viewBox height so the vertex shows).

```svg
<svg viewBox="0 0 220 240" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11">
  <line x1="10" y1="150" x2="210" y2="150" stroke="#888"/>   <!-- x-axis (y=0) -->
  <line x1="110" y1="10" x2="110" y2="230" stroke="#888"/>   <!-- y-axis -->
  <polyline fill="none" stroke="#8e44ad" stroke-width="2.5"
    points="50,50 70,150 90,210 110,230 130,210 150,150 170,50"/>
  <circle cx="70"  cy="150" r="3.5" fill="#8e44ad"/>          <!-- root x = -2 -->
  <circle cx="150" cy="150" r="3.5" fill="#8e44ad"/>          <!-- root x = 2  -->
  <circle cx="110" cy="230" r="3.5" fill="#c0392b"/>          <!-- vertex (0,-4) -->
  <text x="60"  y="145" fill="#8e44ad">-2</text>
  <text x="156" y="145" fill="#8e44ad">2</text>
  <text x="120" y="228" fill="#c0392b">vertex (0, -4)</text>
</svg>
```

## Template 4 — Inequality region (2-D shading)

Draw the boundary line (dashed if `<` or `>`, solid if `≤` or `≥`), then fill the satisfying side with a semi-transparent `<polygon>` or a `rect` with `fill-opacity="0.2"`. Always test one point (e.g. the origin) to decide which side to shade, and say so in words.

---

## Area-model boxes / algebra tiles (no artifact needed — use a `$$` display block)

These labeled boxes are the **area model**, also called **algebra tiles** — the same partition-into-rectangles picture, whether you call the cells "area-model boxes" or "tiles." Use them for distribution, multiplying binomials, and factoring.

Notation convention: write **inline** math as Unicode plain text (x², 1/2, ≤, ±, √, →) — inline `\( \)` does not render reliably. Reserve `$$ ... $$` **display** blocks for things that genuinely need them, like the `array` boxes below. (SKILL.md holds the authoritative rule.)

For distribution and factoring, a `$$` `array` renders a clean labeled box (an area-model / algebra-tile grid) right in chat:

Distribution 3(x+4):
```latex
$$\begin{array}{c|c|c}
 & x & 4 \\ \hline
3 & 3x & 12
\end{array}\qquad\Rightarrow\qquad 3x + 12$$
```

Multiplying / factoring (x+4)(x+3):
```latex
$$\begin{array}{c|c|c}
 & x & 3 \\ \hline
x & x^2 & 3x \\ \hline
4 & 4x & 12
\end{array}\qquad\Rightarrow\qquad x^2 + 7x + 12$$
```
(If a particular surface doesn't draw the `\hline` rules, the grid of cells still reads fine.)

---

## HTML / React interactive (only when interaction is the point)

When a student would benefit from *dragging* (e.g. watching how changing m tilts a line, or how a widens a parabola), make a small self-contained HTML artifact with a `<input type="range">` slider that recomputes and redraws an SVG on change. Keep it tiny and label everything. Don't reach for this for a static graph — an SVG artifact is simpler and less likely to break.

---

## Final checklist before sending any visual

- [ ] Points **computed** (ideally via the code tool), not eyeballed.
- [ ] Axes, scale, and key points **labeled**.
- [ ] A **sentence or table** accompanies it in the chat.
- [ ] It's an **artifact** (for SVG/curves) or clean **ASCII** (for a simple number line) — never raw SVG loose in a message.
