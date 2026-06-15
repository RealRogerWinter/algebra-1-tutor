"""Anatomy-of diagrams: labeled callout diagrams for Algebra 1.

Each sample shows a KaTeX-rendered expression ($$..$$) and, below it, a small
inline SVG that names the parts.  Inside the SVG every named part is written
once more as a short colored chip with a rounded 2.5-width underline (the
"main stroke"), and a thin slate leader line runs from that underline to a
friendly description.  Keeping the part-words inside the SVG means the leaders
always land exactly where they should, instead of guessing where KaTeX laid
the glyphs out.

Every numeric claim (the drawn slope, the count of "copies", the intercepts)
is computed/verified in arithmetic before being drawn so a stray pixel never
teaches a falsehood.  Colors are the exact book palette so the dark-mode
overrides in textbook.css apply.
"""

TITLE = "Anatomy-of diagrams"
KIND = "deterministic-svg"
BLURB = "Friendly callout diagrams that name the parts of an expression, with thin leader lines pointing from each part to a plain-language description."
LESSONS = ["5.4", "1.2", "10.1", "5.6", "4.2", "1.5"]

# --- shared palette (exact hex so dark-mode overrides match) -------------
BLUE = "#2980b9"
VIOLET = "#8e44ad"
RED = "#c0392b"
GREEN = "#27ae60"
SLATE = "#888"   # neutral / leader lines / underlines (has a dark-mode override)
GOLD = "#a9740f"


def _leader(x1, y1, x2, y2):
    """A thin slate leader line with a soft dot at the start (the part end)."""
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{SLATE}" '
        f'stroke-width="1.2" stroke-linecap="round"/>'
        f'<circle cx="{x2}" cy="{y2}" r="1.7" fill="{SLATE}"/>'
    )


def _part(cx, baseline, text, color, half=16, size=14):
    """A part-word centered at cx with a rounded color underline (main stroke).

    Returns (svg, underline_x1, underline_y, underline_x2) so a leader can be
    attached to the underline.
    """
    uy = baseline + 5
    svg = (
        f'<text x="{cx}" y="{baseline}" font-size="{size}" fill="{color}" '
        f'text-anchor="middle" font-weight="600" '
        f'font-family="ui-monospace, Consolas, monospace">{text}</text>'
        f'<line x1="{cx - half}" y1="{uy}" x2="{cx + half}" y2="{uy}" '
        f'stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>'
    )
    return svg, (cx - half, uy, cx + half)


def _label(x, y, text, color=SLATE, size=10, anchor="start", weight="600"):
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" '
        f'text-anchor="{anchor}" font-weight="{weight}">{text}</text>'
    )


def _svg(viewbox, body):
    return (
        f'<svg viewBox="{viewbox}" xmlns="http://www.w3.org/2000/svg" '
        f'font-family="sans-serif" role="img">{body}</svg>'
    )


def _frame(slug, expr_tex, svg, expr_size="1.7em"):
    """Stack the KaTeX expression over its anatomy SVG."""
    return (
        f'<div class="{slug}" style="text-align:center">'
        f'<div style="font-size:{expr_size};margin:.2rem 0 .1rem">$${expr_tex}$$</div>'
        f'{svg}'
        f'</div>'
    )


# =========================================================================
# (1) y = mx + b  ->  Lesson 5.4
# A real line y = 2x + 1 is drawn.  Verified: rise(60px) = 2*run(30px) so the
# drawn slope is exactly m = 2, and the dot sits at the true y-intercept (0,1).
# =========================================================================
def _slope_intercept():
    # math grid: origin pixel (60,148), 1 unit = 30px (same on both axes)
    ox, oy, u = 60.0, 148.0, 30.0

    def P(xm, ym):
        return (round(ox + xm * u, 1), round(oy - ym * u, 1))

    lx1, ly1 = P(-1.0, -1.0)   # line drawn for x in [-1, 1.6]
    lx2, ly2 = P(1.6, 4.2)
    yi = P(0, 1)               # true y-intercept (0,1)
    r0, r1, s1 = P(0, 1), P(1, 1), P(1, 3)   # run then rise (slope triangle)

    body = [
        # axes
        f'<line x1="{P(-1.3,0)[0]}" y1="{oy}" x2="{P(2.0,0)[0]}" y2="{oy}" '
        f'stroke="{SLATE}" stroke-width="1.2" stroke-linecap="round"/>',
        f'<line x1="{ox}" y1="{P(0,-1.2)[1]}" x2="{ox}" y2="{P(0,4.4)[1]}" '
        f'stroke="{SLATE}" stroke-width="1.2" stroke-linecap="round"/>',
        _label(P(2.0, 0)[0] + 2, oy + 3, "x", SLATE, 9, "start"),
        _label(ox - 5, P(0, 4.4)[1] + 2, "y", SLATE, 9, "end"),
        # the line (main stroke)
        f'<line x1="{lx1}" y1="{ly1}" x2="{lx2}" y2="{ly2}" stroke="{BLUE}" '
        f'stroke-width="2.5" stroke-linecap="round"/>',
        # slope triangle: run + rise
        f'<path d="M {r0[0]} {r0[1]} H {r1[0]} V {s1[1]}" fill="none" '
        f'stroke="{GREEN}" stroke-width="2.5" stroke-linecap="round" '
        f'stroke-linejoin="round" stroke-dasharray="1 5"/>',
        _label((r0[0] + r1[0]) / 2, r1[1] + 13, "run 1", GREEN, 9, "middle"),
        _label(r1[0] + 5, (r1[1] + s1[1]) / 2 + 3, "rise 2", GREEN, 9, "start"),
        # y-intercept dot
        f'<circle cx="{yi[0]}" cy="{yi[1]}" r="3.6" fill="{RED}"/>',
        # leader: m -> a point on the line
        _leader(214, 58, P(1.35, 3.7)[0], P(1.35, 3.7)[1]),
        _label(218, 55, "m = slope", BLUE, 11, "start"),
        _label(218, 69, "how steep the line is", SLATE, 9, "start"),
        # leader: b -> the y-intercept dot
        _leader(214, 128, yi[0], yi[1]),
        _label(218, 125, "b = y-intercept", RED, 11, "start"),
        _label(218, 139, "where it crosses the y-axis", SLATE, 9, "start"),
    ]
    svg = _svg("0 0 380 195", "".join(body))
    expr = "y = \\textcolor{#2980b9}{m}\\,x + \\textcolor{#c0392b}{b}"
    return {
        "caption": "slope-intercept form: m is the slope, b is the y-intercept",
        "html": _frame("anat-slope", expr, svg, "1.8em"),
    }


# =========================================================================
# (2) parts of a fraction  ->  Lesson 1.2
# =========================================================================
def _fraction():
    body = []
    # the fraction redrawn small inside the SVG: 3 over 4 with a violet bar
    body.append(_label(110, 64, "3", BLUE, 22, "middle"))
    body.append(
        f'<line x1="88" y1="74" x2="132" y2="74" stroke="{VIOLET}" '
        f'stroke-width="2.5" stroke-linecap="round"/>'
    )
    body.append(_label(110, 98, "4", GREEN, 22, "middle"))
    body += [
        # leader: numerator (the 3) -> right-up
        _leader(220, 40, 122, 56),
        _label(224, 37, "numerator", BLUE, 11, "start"),
        _label(224, 51, "the part you have", SLATE, 9, "start"),
        # leader: the bar -> right
        _leader(220, 78, 132, 74),
        _label(224, 75, "the bar means ÷", VIOLET, 11, "start"),
        _label(224, 89, "(divide top by bottom)", SLATE, 9, "start"),
        # leader: denominator (the 4) -> right-down
        _leader(220, 116, 122, 92),
        _label(224, 113, "denominator", GREEN, 11, "start"),
        _label(224, 127, "how many equal parts", SLATE, 9, "start"),
    ]
    svg = _svg("0 0 400 150", "".join(body))
    expr = "\\dfrac{\\textcolor{#2980b9}{3}}{\\textcolor{#27ae60}{4}}"
    return {
        "caption": "a fraction: numerator on top, denominator on the bottom, the bar means divide",
        "html": _frame("anat-fraction", expr, svg, "1.6em"),
    }


# =========================================================================
# (3) a power a^n  ->  Lesson 10.1
# Verified: 2^4 = 2*2*2*2 = 16 — four copies of the base (matches the exponent).
# =========================================================================
def _power():
    base, exp = 2, 4
    factors = [str(base)] * exp
    product = " \\times ".join(factors)        # 2 x 2 x 2 x 2
    value = base ** exp                         # 16
    assert value == eval("*".join(factors)) and len(factors) == exp

    body = []
    # redraw a^n big inside the SVG: base then a raised exponent, each with a
    # rounded color underline (main stroke) that a leader attaches to.
    body.append(_label(150, 72, str(base), BLUE, 30, "middle"))
    body.append(
        f'<line x1="140" y1="79" x2="160" y2="79" stroke="{BLUE}" '
        f'stroke-width="2.5" stroke-linecap="round"/>'
    )
    body.append(_label(172, 52, str(exp), RED, 18, "middle"))
    body.append(
        f'<line x1="165" y1="58" x2="179" y2="58" stroke="{RED}" '
        f'stroke-width="2.5" stroke-linecap="round"/>'
    )
    body += [
        # leader: base underline -> down-left
        _leader(70, 116, 150, 81),
        _label(66, 130, "base", BLUE, 11, "end"),
        _label(66, 143, "the number being multiplied", SLATE, 9, "end"),
        # leader: exponent underline -> up-right
        _leader(250, 34, 172, 58),
        _label(254, 31, "exponent", RED, 11, "start"),
        _label(254, 45, f"use the base {exp} times", SLATE, 9, "start"),
    ]
    # viewBox extends left of 0: the "base / the number being multiplied" label is right-anchored
    # at x=66 and its long second line runs left past x=0 — widen the canvas so it isn't clipped.
    svg = _svg("-78 0 478 155", "".join(body))
    expr = (
        f"\\textcolor{{#2980b9}}{{{base}}}^{{\\textcolor{{#c0392b}}{{{exp}}}}}"
        f" = \\underbrace{{{product}}}_{{\\textcolor{{#c0392b}}{{{exp}}}\\ \\text{{copies}}}}"
        f" = {value}"
    )
    return {
        "caption": f"a power: base {base}, exponent {exp} ({exp} copies multiplied = {value})",
        "html": _frame("anat-power", expr, svg, "1.5em"),
    }


# =========================================================================
# (4) standard form Ax + By = C  ->  Lesson 5.6
# Uses 2x + 3y = 6.  (Checked: x-intercept (3,0), y-intercept (0,2).)
# =========================================================================
def _standard_form():
    pA, uA = _part(60, 62, "A", BLUE)
    pB, uB = _part(150, 62, "B", VIOLET)
    pC, uC = _part(250, 62, "C", GREEN)
    body = [
        pA, pB, pC,
        # leaders drop from each underline to its description
        _leader(60, 96, uA[0] + 16, uA[1]),
        _label(60, 110, "A", BLUE, 11, "middle"),
        _label(60, 123, "x-coefficient", SLATE, 9, "middle"),
        _leader(150, 96, uB[0] + 16, uB[1]),
        _label(150, 110, "B", VIOLET, 11, "middle"),
        _label(150, 123, "y-coefficient", SLATE, 9, "middle"),
        _leader(250, 96, uC[0] + 16, uC[1]),
        _label(250, 110, "C", GREEN, 11, "middle"),
        _label(250, 123, "the constant", SLATE, 9, "middle"),
    ]
    svg = _svg("0 0 320 135", "".join(body))
    expr = (
        "\\textcolor{#2980b9}{A}\\,x + \\textcolor{#8e44ad}{B}\\,y "
        "= \\textcolor{#27ae60}{C} \\qquad \\text{e.g. } 2x + 3y = 6"
    )
    return {
        "caption": "standard form Ax + By = C: A and B are coefficients, C is the constant",
        "html": _frame("anat-standard", expr, svg, "1.3em"),
    }


# =========================================================================
# (5) function notation f(x)  ->  Lesson 4.2
# =========================================================================
def _function_notation():
    body = []
    # redraw f(x) inside the SVG so leaders land precisely; underline the name
    # f and the input x (main strokes the leaders attach to).
    body.append(_label(150, 66, "f", VIOLET, 26, "middle"))
    body.append(
        f'<line x1="143" y1="73" x2="157" y2="73" stroke="{VIOLET}" '
        f'stroke-width="2.5" stroke-linecap="round"/>'
    )
    body.append(_label(168, 66, "(", SLATE, 26, "middle"))
    body.append(_label(184, 66, "x", BLUE, 26, "middle"))
    body.append(
        f'<line x1="177" y1="73" x2="191" y2="73" stroke="{BLUE}" '
        f'stroke-width="2.5" stroke-linecap="round"/>'
    )
    body.append(_label(200, 66, ")", SLATE, 26, "middle"))
    body += [
        # leader: name f -> down-left
        _leader(60, 108, 150, 75),
        _label(60, 122, "name of the rule", VIOLET, 11, "end"),
        _label(60, 135, "(here it is f)", SLATE, 9, "end"),
        # leader: input x -> down-right
        _leader(300, 108, 184, 75),
        _label(300, 122, "the input", BLUE, 11, "start"),
        _label(300, 135, "what you put in", SLATE, 9, "start"),
        # leader: whole expression -> up
        _leader(300, 30, 200, 50),
        _label(300, 27, '"f of x"', GREEN, 11, "start"),
        _label(300, 41, "the rule applied to x", SLATE, 9, "start"),
    ]
    svg = _svg("0 0 400 150", "".join(body))
    expr = "\\textcolor{#8e44ad}{f}(\\textcolor{#2980b9}{x})"
    return {
        "caption": 'function notation f(x): the name f, the input x, "the rule applied to x"',
        "html": _frame("anat-function", expr, svg, "1.6em"),
    }


# =========================================================================
# (6) a term / expression  3x + 2  ->  Lesson 1.5
# Coefficient 3, variable x, constant 2.  (Checked: at x = 4, 3x + 2 = 14.)
# =========================================================================
def _term():
    body = []
    # redraw 3x + 2 inside the SVG with colored glyphs, each named part with a
    # rounded color underline (main stroke) for its leader.
    body.append(_label(96, 66, "3", BLUE, 26, "middle"))
    body.append(
        f'<line x1="89" y1="73" x2="103" y2="73" stroke="{BLUE}" '
        f'stroke-width="2.5" stroke-linecap="round"/>'
    )
    body.append(_label(116, 66, "x", VIOLET, 26, "middle"))
    body.append(
        f'<line x1="109" y1="73" x2="123" y2="73" stroke="{VIOLET}" '
        f'stroke-width="2.5" stroke-linecap="round"/>'
    )
    body.append(_label(146, 66, "+", SLATE, 22, "middle"))
    body.append(_label(172, 66, "2", GREEN, 26, "middle"))
    body.append(
        f'<line x1="165" y1="73" x2="179" y2="73" stroke="{GREEN}" '
        f'stroke-width="2.5" stroke-linecap="round"/>'
    )
    body += [
        # leader: coefficient 3 -> up
        _leader(70, 30, 96, 50),
        _label(66, 27, "coefficient", BLUE, 11, "end"),
        _label(66, 41, "how many x's", SLATE, 9, "end"),
        # leader: variable x -> down-left
        _leader(96, 112, 116, 75),
        _label(96, 126, "variable", VIOLET, 11, "middle"),
        _label(96, 139, "the unknown", SLATE, 9, "middle"),
        # leader: constant 2 -> down-right
        _leader(250, 112, 172, 75),
        _label(250, 126, "constant", GREEN, 11, "start"),
        _label(250, 139, "a plain number", SLATE, 9, "start"),
    ]
    svg = _svg("0 0 360 150", "".join(body))
    expr = (
        "\\textcolor{#2980b9}{3}\\textcolor{#8e44ad}{x} "
        "+ \\textcolor{#27ae60}{2}"
    )
    return {
        "caption": "the expression 3x + 2: coefficient 3, variable x, constant 2",
        "html": _frame("anat-term", expr, svg, "1.5em"),
    }


def samples():
    return [
        _slope_intercept(),
        _fraction(),
        _power(),
        _standard_form(),
        _function_notation(),
        _term(),
    ]
