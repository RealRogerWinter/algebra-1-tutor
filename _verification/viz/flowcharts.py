"""Decision flowcharts -- calm, rounded flow diagrams for an Algebra 1 textbook.

A gallery builder imports this module and renders each sample's "html" into a page that
already loads the textbook stylesheet and KaTeX. Everything here is deterministic SVG
(boxes, arrows, short text labels) with KaTeX $$...$$ for any real math, computed/verified
with sympy so a label never asserts a falsehood.

Module contract: TITLE, KIND, BLURB, LESSONS, samples().
"""

import sympy as sp

TITLE = "Decision flowcharts"
KIND = "deterministic-svg"
BLURB = "Calm rounded boxes and arrows that walk a beginner through a procedure or a choose-your-method decision."
LESSONS = ["1.3", "2.1", "12.5"]

# --- SVG palette (matches figures.py / dark-mode overrides) --------------------------------------
BLUE = "#2980b9"
VIOLET = "#8e44ad"
RED = "#c0392b"
GREEN = "#27ae60"
NEUTRAL = "#888"
GOLD = "#a9740f"


def _esc(s):
    """Escape plain node text for safe inline SVG <text> (these are short labels, not markup)."""
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _svg(slug, w, h, body):
    """Wrap body in a transparent, responsive SVG with a per-sample arrowhead marker."""
    mid = f"{slug}-arrow"
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'font-family="sans-serif" style="width:100%;max-width:{w}px;height:auto" '
        f'role="img" aria-label="{TITLE}">\n'
        f'  <defs>\n'
        f'    <marker id="{mid}" viewBox="0 0 10 10" refX="8.5" refY="5" '
        f'markerWidth="7" markerHeight="7" orient="auto-start-reverse">\n'
        f'      <path d="M1,1 L9,5 L1,9" fill="none" stroke="{NEUTRAL}" '
        f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>\n'
        f'    </marker>\n'
        f'  </defs>\n'
        f'  {body}\n'
        f'</svg>'
    )


def _box(x, y, w, h, lines, color, slug, idx, fill_opacity=0.10, accent=True):
    """A soft rounded box, left-accent bar, centered short text label(s).

    `lines` is a list of plain strings (flowchart node text -- short labels are allowed).
    Returns (svg, anchors) where anchors gives connection points on each side.
    """
    rx = 14
    parts = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" ry="{rx}" '
        f'fill="{color}" fill-opacity="{fill_opacity}" stroke="{color}" '
        f'stroke-width="2.5" stroke-linejoin="round"/>'
    ]
    if accent:
        # short rounded accent bar near the left edge
        bx = x + 11
        by = y + 11
        bh = h - 22
        parts.append(
            f'<line x1="{bx}" y1="{by}" x2="{bx}" y2="{by + bh}" stroke="{color}" '
            f'stroke-width="3.5" stroke-linecap="round"/>'
        )
    # vertically center the block of lines
    cx = x + w / 2 + (5 if accent else 0)
    line_h = 17
    total = line_h * len(lines)
    start = y + h / 2 - total / 2 + 12
    for i, ln in enumerate(lines):
        weight = "600" if i == 0 else "400"
        col = color if i == 0 else "#555"
        size = 13 if i == 0 else 11.5
        parts.append(
            f'<text x="{round(cx, 1)}" y="{round(start + i * line_h, 1)}" '
            f'text-anchor="middle" font-size="{size}" font-weight="{weight}" '
            f'fill="{col}">{_esc(ln)}</text>'
        )
    anchors = {
        "top": (x + w / 2, y),
        "bottom": (x + w / 2, y + h),
        "left": (x, y + h / 2),
        "right": (x + w, y + h / 2),
        "cx": x + w / 2,
        "cy": y + h / 2,
        "x": x, "y": y, "w": w, "h": h,
    }
    return "\n  ".join(parts), anchors


def _arrow(x1, y1, x2, y2, slug, color=NEUTRAL, label=None, lx=None, ly=None,
           label_color=None, dash=False):
    """A straight arrow from (x1,y1) to (x2,y2) with the marker arrowhead; optional label."""
    mid = f"{slug}-arrow"
    da = ' stroke-dasharray="2 5"' if dash else ""
    out = [
        f'<line x1="{round(x1, 1)}" y1="{round(y1, 1)}" x2="{round(x2, 1)}" '
        f'y2="{round(y2, 1)}" stroke="{color}" stroke-width="2.5" '
        f'stroke-linecap="round"{da} marker-end="url(#{mid})"/>'
    ]
    if label:
        lc = label_color or NEUTRAL
        out.append(
            f'<text x="{round(lx, 1)}" y="{round(ly, 1)}" text-anchor="middle" '
            f'font-size="11" font-weight="600" fill="{lc}">{_esc(label)}</text>'
        )
    return "\n  ".join(out)


def _elbow(x1, y1, x2, y2, slug, color=NEUTRAL):
    """An L-shaped connector (down then across, with rounded corner) ending in an arrowhead.

    Goes straight down from (x1,y1) to the level y2, then horizontally to just before x2.
    """
    mid = f"{slug}-arrow"
    r = 10
    if x2 >= x1:
        corner = f"L{x1},{y2 - r} Q{x1},{y2} {x1 + r},{y2} L{x2},{y2}"
    else:
        corner = f"L{x1},{y2 - r} Q{x1},{y2} {x1 - r},{y2} L{x2},{y2}"
    d = f"M{round(x1, 1)},{round(y1, 1)} {corner}"
    return (
        f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.5" '
        f'stroke-linecap="round" stroke-linejoin="round" marker-end="url(#{mid})"/>'
    )


# ================================================================================================
# Sample 1 -- Order of operations (4-step vertical flow). Lesson 1.3.
# ================================================================================================
def _order_of_operations():
    slug = "ooo"
    W, H = 360, 432
    bx, bw, bh = 50, 260, 70
    gap = 90  # top-to-top spacing
    tops = [24, 24 + gap, 24 + 2 * gap, 24 + 3 * gap]

    steps = [
        (["1. Grouping", "parentheses, brackets, fraction bars"], VIOLET),
        (["2. Exponents", "powers and roots"], BLUE),
        (["3. Multiply & divide", "as they come, left to right"], GREEN),
        (["4. Add & subtract", "as they come, left to right"], GOLD),
    ]

    parts = []
    anchors = []
    for (lines, color), top in zip(steps, tops):
        svg, a = _box(bx, top, bw, bh, lines, color, slug, len(anchors))
        parts.append(svg)
        anchors.append(a)

    # connecting arrows between consecutive boxes
    for i in range(len(anchors) - 1):
        x = anchors[i]["cx"]
        y1 = anchors[i]["bottom"][1] + 2
        y2 = anchors[i + 1]["top"][1] - 3
        parts.append(_arrow(x, y1, x, y2, slug))

    body = "\n  ".join(parts)
    svg = _svg(slug, W, H, body)
    # Caption carries the mnemonic via KaTeX-safe plain text + a math reminder.
    html = (
        '<figure style="margin:0;text-align:center">'
        + svg
        + '<figcaption style="margin-top:.6rem;font-size:.95em;color:#555">'
        'Work top to bottom. Multiply / divide share a step (left to right), '
        'and so do add / subtract &mdash; e.g. '
        '$$8 - 2\\cdot 3 + 4 = 8 - 6 + 4 = 6.$$'
        '</figcaption></figure>'
    )
    return html


# ================================================================================================
# Sample 2 -- Solve a linear equation (5-step vertical flow). Lesson 2.1.
# ================================================================================================
def _solve_linear():
    slug = "sle"
    W, H = 380, 520
    bx, bw, bh = 36, 308, 66
    gap = 88
    tops = [22 + i * gap for i in range(5)]

    steps = [
        (["1. Simplify each side", "distribute, combine like terms"], VIOLET),
        (["2. Collect the variables", "move them to one side"], BLUE),
        (["3. Undo + and −", "add / subtract from both sides"], GREEN),
        (["4. Undo × and ÷", "multiply / divide both sides"], GOLD),
        (["5. Check", "substitute back in"], RED),
    ]

    parts, anchors = [], []
    for (lines, color), top in zip(steps, tops):
        svg, a = _box(bx, top, bw, bh, lines, color, slug, len(anchors))
        parts.append(svg)
        anchors.append(a)

    for i in range(len(anchors) - 1):
        x = anchors[i]["cx"]
        y1 = anchors[i]["bottom"][1] + 2
        y2 = anchors[i + 1]["top"][1] - 3
        parts.append(_arrow(x, y1, x, y2, slug))

    body = "\n  ".join(parts)
    svg = _svg(slug, W, H, body)
    # A real worked example, sympy-verified below, rendered with KaTeX.
    html = (
        '<figure style="margin:0;text-align:center">'
        + svg
        + '<figcaption style="margin-top:.6rem;font-size:.95em;color:#555">'
        'Same path every time. For example $$3(x+2) = x + 10$$ becomes '
        '$$3x + 6 = x + 10,\\ \\ 2x = 4,\\ \\ x = 2.$$'
        '</figcaption></figure>'
    )
    return html


# ================================================================================================
# Sample 3 -- Which method solves this quadratic? (decision tree). Lesson 12.5.
# ================================================================================================
def _quadratic_method():
    slug = "qmd"
    W, H = 460, 430

    parts = []

    # Start box (top center)
    start_svg, start = _box(150, 18, 160, 56, ["Solve a quadratic"], BLUE, slug, 0, accent=False)
    parts.append(start_svg)

    # Decision 1
    d1_svg, d1 = _box(140, 110, 180, 60, ["Is it just", "x² = k  ?"], VIOLET, slug, 1, accent=False)
    parts.append(d1_svg)
    # Decision 2
    d2_svg, d2 = _box(140, 222, 180, 60, ["Does it factor", "easily?"], VIOLET, slug, 2, accent=False)
    parts.append(d2_svg)

    # Outcome boxes on the right (yes branches) and bottom (no -> formula)
    o1_svg, o1 = _box(340, 112, 108, 56, ["Square root", "both sides"], GREEN, slug, 3, accent=False)
    parts.append(o1_svg)
    o2_svg, o2 = _box(340, 224, 108, 56, ["Factor", "(zero product)"], GREEN, slug, 4, accent=False)
    parts.append(o2_svg)
    o3_svg, o3 = _box(140, 338, 180, 60, ["Quadratic", "formula"], GOLD, slug, 5, accent=False)
    parts.append(o3_svg)

    # Arrows: start -> d1 -> d2 -> o3 (the "no, no" spine)
    parts.append(_arrow(start["cx"], start["bottom"][1] + 2, d1["cx"], d1["top"][1] - 3, slug))
    parts.append(_arrow(d1["cx"], d1["bottom"][1] + 2, d2["cx"], d2["top"][1] - 3,
                        slug, label="no", lx=d1["cx"] - 16, ly=(d1["bottom"][1] + d2["top"][1]) / 2 + 4,
                        label_color=RED))
    parts.append(_arrow(d2["cx"], d2["bottom"][1] + 2, o3["cx"], o3["top"][1] - 3,
                        slug, label="no", lx=d2["cx"] - 16, ly=(d2["bottom"][1] + o3["top"][1]) / 2 + 4,
                        label_color=RED))

    # "yes" branches to the right
    parts.append(_arrow(d1["right"][0] + 2, d1["right"][1], o1["left"][0] - 3, o1["left"][1],
                        slug, color=GREEN, label="yes", lx=(d1["right"][0] + o1["left"][0]) / 2,
                        ly=d1["right"][1] - 8, label_color=GREEN))
    parts.append(_arrow(d2["right"][0] + 2, d2["right"][1], o2["left"][0] - 3, o2["left"][1],
                        slug, color=GREEN, label="yes", lx=(d2["right"][0] + o2["left"][0]) / 2,
                        ly=d2["right"][1] - 8, label_color=GREEN))

    body = "\n  ".join(parts)
    svg = _svg(slug, W, H, body)
    html = (
        '<figure style="margin:0;text-align:center">'
        + svg
        + '<figcaption style="margin-top:.6rem;font-size:.95em;color:#555">'
        'Three doors, in order. If stuck, the formula always works: '
        '$$x = \\dfrac{-b \\pm \\sqrt{b^{2} - 4ac}}{2a}.$$'
        '</figcaption></figure>'
    )
    return html


# --- correctness check (runs at import; raises if any asserted math is wrong) --------------------
def _verify_math():
    x = sp.Symbol("x")

    # Sample 1: 8 - 2*3 + 4 == 6, evaluated by true order of operations.
    assert sp.sympify("8 - 2*3 + 4") == 6, "order-of-operations example wrong"

    # Sample 2: 3(x+2) = x+10  ->  x = 2, and each printed step is an equivalent equation.
    eq = sp.Eq(3 * (x + 2), x + 10)
    sol = sp.solve(eq, x)
    assert sol == [2], f"linear solution wrong: {sol}"
    # printed intermediate forms must be equivalent to the original equation
    assert sp.simplify((3 * (x + 2)) - (x + 10)) == sp.simplify((3 * x + 6) - (x + 10))
    assert sp.simplify((3 * x + 6 - (x + 10)) - (2 * x - 4)) == 0
    # final value satisfies the equation
    assert eq.subs(x, 2)

    # Sample 3: the quadratic formula is the genuine root formula for a*x^2+b*x+c=0.
    a, b, c = sp.symbols("a b c")
    roots = sp.solve(sp.Eq(a * x**2 + b * x + c, 0), x)
    formula = [(-b - sp.sqrt(b**2 - 4 * a * c)) / (2 * a),
               (-b + sp.sqrt(b**2 - 4 * a * c)) / (2 * a)]
    assert set(sp.simplify(r) for r in roots) == set(sp.simplify(f) for f in formula), \
        "quadratic formula mismatch"
    # and the x^2 = k branch: solving x^2 = k gives +/- sqrt(k)
    k = sp.Symbol("k")
    assert set(sp.solve(sp.Eq(x**2, k), x)) == {sp.sqrt(k), -sp.sqrt(k)}


_verify_math()


def samples():
    return [
        {
            "caption": "Order of operations as a 4-step vertical flow (lesson 1.3)",
            "html": _order_of_operations(),
        },
        {
            "caption": "Solve a linear equation: the same five steps every time (lesson 2.1)",
            "html": _solve_linear(),
        },
        {
            "caption": "Which method solves this quadratic? A small decision tree (lesson 12.5)",
            "html": _quadratic_method(),
        },
    ]


if __name__ == "__main__":
    print(TITLE, len(samples()))
