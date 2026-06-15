"""Fraction diagrams (bars, number line, area model) for the Algebra 1 textbook.

A gallery / textbook builder imports this module and renders samples() into a page that
already loads the textbook stylesheet and KaTeX. Each diagram is a deterministic inline SVG
(transparent background, rounded shapes, stroke-width ~2.5) with every part labeled by its
REAL value; the equation underneath is typeset by KaTeX via $$ ... $$.

These support Lesson 2.5 (the expanded fraction refresher). They complement, and do not
duplicate, the labelled fraction *anatomy* diagram (viz anatomy#1) already in 2.5: those
name the numerator/denominator; these SHOW the quantity as shaded area and as a point on a
line, then rename, reduce, add, multiply, and flip it.

All arithmetic is checked at import time by _verify() so a wrong pixel cannot teach a
falsehood:
  (0) 3/4  -> 3 of 4 equal parts; point at 0.75
  (1) 3/4 == 6/8                         (equivalent: split each piece in two)
  (2) 6/8 == 3/4, gcd(6, 8) == 2         (reduce: divide top and bottom by the GCD)
  (3) 3/4 == 9/12 and 1/6 == 2/12        (common denominator: rename to twelfths)
  (4) (1/2) * (2/3) == 1/3               (multiply: overlap is 2 of 6 cells)
  (5) (2/3) * (3/2) == 1                 (reciprocal: a number times its flip is 1)
"""
from math import gcd

# NOTE: this module is named fractions.py, so we must NOT `from fractions import Fraction`
# (that would import this module itself). Fraction equality is checked with plain integers:
# a/b == c/d  <=>  a*d == b*c.  The central gate (viz_figures --check) independently re-verifies
# the same numbers via sympy `facts`, so the SVG cannot teach a falsehood.
def _eq(a, b, c, d):
    """True iff a/b == c/d for integers (cross-multiply)."""
    return a * d == b * c


TITLE = "Fraction diagrams"
KIND = "deterministic-svg"
BLURB = "Bars, a number line, and an area model that show what a fraction is and how to rename, reduce, add, multiply, and flip it."
LESSONS = ["2.5"]

# --- palette (book hexes; dark-mode overrides key off these) ------------------------------------
BLUE = "#2980b9"
VIOLET = "#8e44ad"
RED = "#c0392b"
GREEN = "#27ae60"
GOLD = "#a9740f"
AXIS = "#888"

# Shaded cells use the cell's own color at a low fill-opacity so the count reads clearly against
# the cream page; unshaded cells are left empty (page shows through). The stroke carries the color.
_SHADE_OP = 0.30

# --- layout constants -----------------------------------------------------------------------------
VB_W = 540          # viewBox width (units == px at 1:1); extra right margin holds the value label
BAR_X0 = 24         # left edge of every bar
BAR_W = 432         # bar width -> BAR_X0 + BAR_W = 456, leaving room for the "n/d" label on the right
BAR_H = 52          # bar height
RX = 8              # corner radius for the bar's outer frame


def _svg_open(h):
    return (f'<svg viewBox="0 0 {VB_W} {h}" xmlns="http://www.w3.org/2000/svg" '
            f'width="100%" font-family="inherit" '
            f'stroke-linecap="round" stroke-linejoin="round">')


def _bar(x0, y, w, n, k, color, h=BAR_H, label=None, fs=16):
    """A bar of n equal cells with the first k shaded in `color`; thin dividers between cells."""
    cw = w / n
    out = []
    for i in range(n):
        x = x0 + i * cw
        shade = (f'fill="{color}" fill-opacity="{_SHADE_OP}"' if i < k else 'fill="none"')
        out.append(
            f'<rect x="{round(x,2)}" y="{y}" width="{round(cw,2)}" height="{h}" '
            f'{shade} stroke="{color}" stroke-width="1.5"/>'
        )
    # outer frame on top, rounded, heavier
    out.append(
        f'<rect x="{round(x0,2)}" y="{y}" width="{round(w,2)}" height="{h}" rx="{RX}" ry="{RX}" '
        f'fill="none" stroke="{color}" stroke-width="2.5"/>'
    )
    if label is not None:
        out.append(
            f'<text x="{round(x0 + w + 10,2)}" y="{round(y + h/2,2)}" font-size="{fs}" '
            f'font-weight="600" fill="{color}" dominant-baseline="central">{label}</text>'
        )
    return "".join(out)


def _numline(x0, y, w, n, mark_k, color):
    """A 0..1 number line with n equal ticks; a labeled dot at tick mark_k (= mark_k/n)."""
    out = [f'<line x1="{x0}" y1="{y}" x2="{round(x0+w,2)}" y2="{y}" stroke="{AXIS}" stroke-width="2"/>']
    cw = w / n
    for i in range(n + 1):
        x = x0 + i * cw
        out.append(f'<line x1="{round(x,2)}" y1="{y-6}" x2="{round(x,2)}" y2="{y+6}" '
                   f'stroke="{AXIS}" stroke-width="2"/>')
    out.append(f'<text x="{x0}" y="{y+24}" font-size="13" fill="{AXIS}" text-anchor="middle">0</text>')
    out.append(f'<text x="{round(x0+w,2)}" y="{y+24}" font-size="13" fill="{AXIS}" text-anchor="middle">1</text>')
    dx = x0 + mark_k * cw
    out.append(f'<circle cx="{round(dx,2)}" cy="{y}" r="6" fill="{color}"/>')
    out.append(f'<text x="{round(dx,2)}" y="{y-14}" font-size="14" font-weight="600" fill="{color}" '
               f'text-anchor="middle">{mark_k}/{n}</text>')
    return "".join(out)


def _brace_below(x1, x2, y, color, label, fs=14):
    """A calm curly brace under [x1,x2] at top-y=y, label centered below."""
    x1 = round(x1, 2); x2 = round(x2, 2)
    mid = round((x1 + x2) / 2, 2)
    ty = y + 10
    d = (f'M {x1} {y} Q {x1} {ty} {round((x1+mid)/2,2)} {ty} T {mid} {ty+5} '
         f'M {x2} {y} Q {x2} {ty} {round((x2+mid)/2,2)} {ty} T {mid} {ty+5}')
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2"/>'
            f'<text x="{mid}" y="{ty + 22}" font-size="{fs}" fill="{color}" text-anchor="middle">{label}</text>')


def _figcap(svg, html_caption, plain_caption):
    html = ('<figure style="margin:0">' + svg +
            '<figcaption style="margin-top:.4rem;color:var(--ink-soft)">' + html_caption +
            '</figcaption></figure>')
    return {"caption": plain_caption, "html": html}


# =================================================================================================
# (0) What a fraction is: 3/4 as a shaded bar AND as a point on the number line
# =================================================================================================
def _what_is():
    n, k = 4, 3
    assert (k, n) == (3, 4)
    y = 16
    body = [
        _bar(BAR_X0, y, BAR_W, n, k, BLUE, label="3/4"),
        _numline(BAR_X0, y + BAR_H + 40, BAR_W, n, k, BLUE),
    ]
    h = y + BAR_H + 40 + 40
    svg = _svg_open(h) + "".join(body) + "</svg>"
    cap = ('The same 3/4 shown two ways: three of four equal pieces shaded, and a single point '
           'three-quarters of the way from 0 to 1. The number line is home base — it shows a fraction '
           'is one number with one location, not two numbers stacked.')
    return _figcap(svg, cap, "3/4 as a shaded bar and as one point on a number line")


# =================================================================================================
# (1) Equivalent fractions: 3/4 = 6/8 (cut each piece in two; shaded length is unchanged)
# =================================================================================================
def _equivalent():
    assert _eq(3, 4, 6, 8)
    y = 16
    gap = 30
    body = [
        _bar(BAR_X0, y, BAR_W, 4, 3, BLUE, label="3/4"),
        _bar(BAR_X0, y + BAR_H + gap, BAR_W, 8, 6, BLUE, label="6/8"),
    ]
    h = y + 2 * BAR_H + gap + 16
    svg = _svg_open(h) + "".join(body) + "</svg>"
    cap = ('Cut every piece in two: twice as many pieces, twice as many shaded, and the shaded length '
           'never moves. Same amount, new name: '
           '$$\\frac34 = \\frac{3\\times 2}{4\\times 2} = \\frac68.$$')
    return _figcap(svg, cap, "Equivalent fractions: 3/4 = 6/8")


# =================================================================================================
# (2) Reducing with the GCD: 6/8 -> 3/4 (group the 8 cells into pairs; divide top and bottom by 2)
# =================================================================================================
def _reduce_gcd():
    g = gcd(6, 8)
    assert g == 2 and _eq(6, 8, 3, 4)
    y = 16
    n, k = 8, 6
    body = [_bar(BAR_X0, y, BAR_W, n, k, GREEN, label="6/8")]
    # braces grouping the 8 cells into 4 pairs (divide by the GCD, 2)
    cw = BAR_W / n
    for j in range(n // g):
        x1 = BAR_X0 + j * g * cw
        x2 = x1 + g * cw
        body.append(_brace_below(x1, x2, y + BAR_H + 4, AXIS, ""))
    body.append(f'<text x="{round(BAR_X0 + BAR_W/2,2)}" y="{y + BAR_H + 44}" font-size="13" '
                f'fill="{AXIS}" text-anchor="middle">4 groups of 2 — 3 groups shaded</text>')
    h = y + BAR_H + 4 + 56
    svg = _svg_open(h) + "".join(body) + "</svg>"
    cap = ('The biggest number that divides both 6 and 8 is the GCD, 2. Group the eight pieces into pairs '
           'and divide top and bottom by 2 to reach lowest terms: '
           '$$\\frac68 = \\frac{6\\div 2}{8\\div 2} = \\frac34.$$')
    return _figcap(svg, cap, "Reducing 6/8 to 3/4 with the GCD (2)")


# =================================================================================================
# (3) Common denominator: 3/4 and 1/6 both renamed to twelfths (9/12 and 2/12)
# =================================================================================================
def _common_denominator():
    assert _eq(3, 4, 9, 12) and _eq(1, 6, 2, 12)
    y = 16
    gap = 30
    body = [
        _bar(BAR_X0, y, BAR_W, 12, 9, BLUE, label="9/12"),
        _bar(BAR_X0, y + BAR_H + gap, BAR_W, 12, 2, RED, label="2/12"),
    ]
    h = y + 2 * BAR_H + gap + 16
    svg = _svg_open(h) + "".join(body) + "</svg>"
    cap = ('Twelfths are a size that both fourths and sixths fit into evenly (the LCM of 4 and 6 is 12). '
           'Renamed to the same-size pieces, the two fractions are finally ready to add: '
           '$$\\frac34 = \\frac{9}{12}, \\qquad \\frac16 = \\frac{2}{12}.$$')
    return _figcap(svg, cap, "Common denominator: 3/4 and 1/6 renamed to twelfths")


# =================================================================================================
# (4) Multiplying as area: 1/2 across and 2/3 down; the overlap is 2 of 6 cells = 1/3
# =================================================================================================
def _multiply_area():
    assert _eq(1 * 2, 2 * 3, 1, 3)   # (1/2)*(2/3) = 2/6 = 1/3
    side = 200
    x0, y0 = 150, 16
    cols, rows = 2, 3            # 1/2 -> 2 columns (1 shaded); 2/3 -> 3 rows (2 shaded)
    cw, ch = side / cols, side / rows
    body = []
    for r in range(rows):
        for c in range(cols):
            x = x0 + c * cw
            yy = y0 + r * ch
            in_half = c < 1            # left 1 of 2 columns
            in_two_thirds = r < 2      # top 2 of 3 rows
            if in_half and in_two_thirds:
                shade = f'fill="{VIOLET}" fill-opacity="0.34"'   # overlap = the product
            elif in_half or in_two_thirds:
                shade = f'fill="{AXIS}" fill-opacity="0.12"'
            else:
                shade = 'fill="none"'
            body.append(f'<rect x="{round(x,2)}" y="{round(yy,2)}" width="{round(cw,2)}" '
                        f'height="{round(ch,2)}" {shade} stroke="{AXIS}" stroke-width="1.5"/>')
    body.append(f'<rect x="{x0}" y="{y0}" width="{side}" height="{side}" fill="none" '
                f'stroke="{AXIS}" stroke-width="2.5"/>')
    # edge labels
    body.append(f'<text x="{round(x0 + side/2,2)}" y="{y0 - 4}" font-size="14" fill="{BLUE}" '
                f'text-anchor="middle">1/2 across</text>')
    body.append(f'<text x="{x0 - 10}" y="{round(y0 + side/2,2)}" font-size="14" fill="{RED}" '
                f'text-anchor="end" dominant-baseline="central">2/3 down</text>')
    h = y0 + side + 16
    svg = _svg_open(h) + "".join(body) + "</svg>"
    cap = ('Shade 1/2 across and 2/3 down one whole square. Where the two shadings overlap is the product: '
           '2 of the 6 equal cells, which is 1/3. Multiply straight across, then reduce: '
           '$$\\frac12 \\times \\frac23 = \\frac{2}{6} = \\frac13.$$')
    return _figcap(svg, cap, "Multiplying 1/2 x 2/3 as overlapping area = 1/3")


# =================================================================================================
# (5) Reciprocal: flip top and bottom; a number times its reciprocal is 1
# =================================================================================================
def _reciprocal():
    assert _eq(2 * 3, 3 * 2, 1, 1)   # (2/3)*(3/2) = 6/6 = 1
    y = 44
    cx1, cx2 = 180, 360
    body = [
        # 2/3 card
        f'<text x="{cx1}" y="{y}" font-size="34" font-weight="700" fill="{BLUE}" text-anchor="middle">2</text>',
        f'<line x1="{cx1-26}" y1="{y+10}" x2="{cx1+26}" y2="{y+10}" stroke="{BLUE}" stroke-width="2.5"/>',
        f'<text x="{cx1}" y="{y+46}" font-size="34" font-weight="700" fill="{BLUE}" text-anchor="middle">3</text>',
        # flip arrow
        f'<path d="M {cx1+50} {y+5} C {cx1+95} {y-20}, {cx2-95} {y-20}, {cx2-50} {y+5}" '
        f'fill="none" stroke="{GOLD}" stroke-width="2.5" marker-end="url(#fr-arrow)"/>',
        f'<text x="{round((cx1+cx2)/2,2)}" y="{y-22}" font-size="14" fill="{GOLD}" text-anchor="middle">flip</text>',
        # 3/2 card
        f'<text x="{cx2}" y="{y}" font-size="34" font-weight="700" fill="{VIOLET}" text-anchor="middle">3</text>',
        f'<line x1="{cx2-26}" y1="{y+10}" x2="{cx2+26}" y2="{y+10}" stroke="{VIOLET}" stroke-width="2.5"/>',
        f'<text x="{cx2}" y="{y+46}" font-size="34" font-weight="700" fill="{VIOLET}" text-anchor="middle">2</text>',
    ]
    defs = (f'<defs><marker id="fr-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" '
            f'markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" '
            f'fill="{GOLD}"/></marker></defs>')
    h = y + 70
    svg = _svg_open(h) + defs + "".join(body) + "</svg>"
    cap = ('The reciprocal flips top and bottom. A number times its reciprocal always goes to one, which '
           'is exactly what undoes a fraction that multiplies x: '
           '$$\\frac23 \\times \\frac32 = \\frac{6}{6} = 1.$$')
    return _figcap(svg, cap, "Reciprocal: 2/3 flips to 3/2 and their product is 1")


def _verify():
    """Re-check every asserted number; raise if any diagram would lie."""
    assert _eq(3, 4, 6, 8)                       # 3/4 = 6/8
    assert gcd(6, 8) == 2 and _eq(6, 8, 3, 4)    # reduce 6/8 -> 3/4
    assert _eq(3, 4, 9, 12) and _eq(1, 6, 2, 12) # twelfths
    assert _eq(1 * 2, 2 * 3, 1, 3)               # (1/2)(2/3) = 1/3
    assert _eq(2 * 3, 3 * 2, 1, 1)               # (2/3)(3/2) = 1


_verify()


def samples():
    return [
        _what_is(),            # 0  -> 2.5.f2
        _equivalent(),         # 1  -> 2.5.f3
        _reduce_gcd(),         # 2  -> 2.5.f4
        _common_denominator(), # 3  -> 2.5.f5
        _multiply_area(),      # 4  -> 2.5.f6
        _reciprocal(),         # 5  -> 2.5.f7
    ]


if __name__ == "__main__":
    s = samples()
    print(TITLE, "|", KIND, "|", len(s), "samples")
    for d in s:
        print(" -", d["caption"])
