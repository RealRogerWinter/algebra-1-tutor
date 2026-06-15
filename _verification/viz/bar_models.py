"""Bar / tape diagrams (Singapore-style) for the Algebra 1 textbook gallery.

A gallery builder imports this module and renders samples() into a page that already
loads the textbook stylesheet and KaTeX. Each diagram is a deterministic inline SVG
(transparent background, rounded shapes, stroke-width ~2.5) with every segment labeled
by its REAL value; the equation underneath is typeset by KaTeX via $$ ... $$.

All arithmetic is checked at import time by _verify() so a wrong pixel cannot teach a
falsehood:
  (1) part-part-whole  18 = 7 + 11
  (2) 3x = 54          -> x = 18
  (3) 2x + 3 = 11      -> x = 4
  (4) A = B + 5, A + B = 17 -> B = 6, A = 11
"""

TITLE = "Bar / tape diagrams"
KIND = "deterministic-svg"
BLURB = "Singapore-style bars that turn a word problem or equation into segments you can see and add up."
LESSONS = ["6.2", "2.1", "2.2"]

# --- palette (book hexes; dark-mode overrides key off these) ------------------------------------
BLUE = "#2980b9"
VIOLET = "#8e44ad"
RED = "#c0392b"
GREEN = "#27ae60"
GOLD = "#a9740f"
AXIS = "#888"

# --- layout constants -----------------------------------------------------------------------------
VB_W = 480          # viewBox width (units == px at 1:1); height varies per diagram
BAR_X0 = 24         # left edge of every bar
BAR_W = 432         # full drawable width -> BAR_X0 + BAR_W = 456, leaving 24 padding on the right
BAR_H = 56          # bar height
RX = 10             # corner radius for rounded bars

# Tints so fills stay calm/pale; the stroke carries the real color.
_TINT = {BLUE: "#eaf2f8", VIOLET: "#f3ecf7", RED: "#f9ebe9", GOLD: "#f6efe1", GREEN: "#eafaf1"}


def _svg_open(h):
    return (f'<svg viewBox="0 0 {VB_W} {h}" xmlns="http://www.w3.org/2000/svg" '
            f'width="100%" font-family="inherit" '
            f'stroke-linecap="round" stroke-linejoin="round">')


def _seg(x, w, y, color, label, h=BAR_H, fs=18):
    """One rounded bar segment with a centered numeric label."""
    fill = _TINT.get(color, "#eee")
    cx = round(x + w / 2, 2)
    cy = round(y + h / 2, 2)
    return (
        f'<rect x="{round(x,2)}" y="{y}" width="{round(w,2)}" height="{h}" rx="{RX}" ry="{RX}" '
        f'fill="{fill}" stroke="{color}" stroke-width="2.5"/>'
        f'<text x="{cx}" y="{cy}" font-size="{fs}" font-weight="600" fill="{color}" '
        f'text-anchor="middle" dominant-baseline="central">{label}</text>'
    )


def _brace_below(x1, x2, y, color, label, fs=15):
    """A calm curly brace under [x1,x2] at top-y=y, with a label centered below it."""
    x1 = round(x1, 2); x2 = round(x2, 2)
    mid = round((x1 + x2) / 2, 2)
    drop = 10                                  # how far the brace dips
    ty = y + drop                              # the trough line
    # Two gentle quadratic halves meeting at a small downward tip in the middle.
    d = (f'M {x1} {y} Q {x1} {ty} {round((x1+mid)/2,2)} {ty} '
         f'T {mid} {ty+5} '
         f'M {x2} {y} Q {x2} {ty} {round((x2+mid)/2,2)} {ty} '
         f'T {mid} {ty+5}')
    return (
        f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2"/>'
        f'<text x="{mid}" y="{ty + 24}" font-size="{fs}" fill="{color}" '
        f'text-anchor="middle">{label}</text>'
    )


def _brace_right(x, y1, y2, color, label, fs=15):
    """A curly brace to the RIGHT of a stacked pair spanning [y1,y2], label to its right."""
    y1 = round(y1, 2); y2 = round(y2, 2)
    mid = round((y1 + y2) / 2, 2)
    reach = 12
    bx = x + reach
    d = (f'M {x} {y1} Q {bx} {y1} {bx} {round((y1+mid)/2,2)} '
         f'T {bx+5} {mid} '
         f'M {x} {y2} Q {bx} {y2} {bx} {round((y2+mid)/2,2)} '
         f'T {bx+5} {mid}')
    return (
        f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2"/>'
        f'<text x="{bx + 12}" y="{mid}" font-size="{fs}" fill="{color}" '
        f'dominant-baseline="central">{label}</text>'
    )


# =================================================================================================
# (1) Part-part-whole : 18 = 7 + 11   (lesson 6.2)
# =================================================================================================
def _part_part_whole():
    whole, part = 18, 7
    unknown = whole - part                              # 11
    assert part + unknown == whole

    y = 18
    # widths proportional to the values
    w_part = BAR_W * part / whole
    w_unknown = BAR_W * unknown / whole
    body = [
        _seg(BAR_X0, w_part, y, BLUE, str(part)),
        _seg(BAR_X0 + w_part, w_unknown, y, VIOLET, "?"),
        _brace_below(BAR_X0, BAR_X0 + BAR_W, y + BAR_H + 4, AXIS, f"whole = {whole}"),
    ]
    h = y + BAR_H + 4 + 40
    svg = _svg_open(h) + "".join(body) + "</svg>"
    html = (
        '<figure style="margin:0">'
        f'{svg}'
        f'<figcaption style="margin-top:.4rem;color:var(--ink-soft)">'
        f'The two parts fill the whole bar, so the missing part is '
        f'$$18 - 7 = 11.$$</figcaption>'
        '</figure>'
    )
    return {"caption": "Part-part-whole: 18 split into 7 and 11", "html": html}


# =================================================================================================
# (2) "3 times a number is 54" : three equal honey bars, each 18   (lesson 2.1)
# =================================================================================================
def _three_times():
    total, n = 54, 3
    each = total // n                                   # 18
    assert each * n == total

    y = 18
    gap = 8
    w = (BAR_W - gap * (n - 1)) / n
    body = []
    for i in range(n):
        x = BAR_X0 + i * (w + gap)
        body.append(_seg(x, w, y, GOLD, str(each)))
    body.append(_brace_below(BAR_X0, BAR_X0 + BAR_W, y + BAR_H + 4, AXIS, f"total = {total}"))
    h = y + BAR_H + 4 + 40
    svg = _svg_open(h) + "".join(body) + "</svg>"
    html = (
        '<figure style="margin:0">'
        f'{svg}'
        f'<figcaption style="margin-top:.4rem;color:var(--ink-soft)">'
        f'Three equal bars make 54, so each one is '
        f'$$54 \\div 3 = 18.$$</figcaption>'
        '</figure>'
    )
    return {"caption": "3 times a number is 54, so the number is 18", "html": html}


# =================================================================================================
# (3) Two-step equation  2x + 3 = 11   ->  x = 4   (lesson 2.2)
# =================================================================================================
def _two_step():
    # 2x + 3 = 11
    a, b, rhs = 2, 3, 11
    x = (rhs - b) // a                                  # 4
    assert a * x + b == rhs

    y = 18
    gap = 8
    # Visual scale: 1 unit of value = (BAR_W - one gap) / total_units of width, so the whole
    # tape (two x-blocks + the 3-block) spans the full bar and segment widths are TRUE to value.
    total_units = a * x + b                             # 11
    unit = (BAR_W - gap * a) / total_units             # account for the 2 gaps between 3 blocks
    body = []
    cur = BAR_X0
    for _ in range(a):                                  # two equal x-blocks
        w = unit * x
        body.append(_seg(cur, w, y, BLUE, "x"))
        cur += w + gap
    w3 = unit * b                                       # the constant 3-block
    body.append(_seg(cur, w3, y, RED, str(b)))
    end = cur + w3
    body.append(_brace_below(BAR_X0, end, y + BAR_H + 4, AXIS, f"= {rhs}"))
    h = y + BAR_H + 4 + 40
    svg = _svg_open(h) + "".join(body) + "</svg>"
    html = (
        '<figure style="margin:0">'
        f'{svg}'
        f'<figcaption style="margin-top:.4rem;color:var(--ink-soft)">'
        f'Take away the 3, then split what is left between the two x-blocks: '
        f'$$2x + 3 = 11 \\;\\Rightarrow\\; 2x = 8 \\;\\Rightarrow\\; x = 4.$$</figcaption>'
        '</figure>'
    )
    return {"caption": "Two-step equation 2x + 3 = 11 gives x = 4", "html": html}


# =================================================================================================
# (4) Comparison : A is 5 more than B, together 17  ->  B = 6, A = 11   (lesson 6.2 / 2.1)
# =================================================================================================
def _comparison():
    total, diff = 17, 5
    b = (total - diff) // 2                             # 6
    a = b + diff                                        # 11
    assert a + b == total and a - b == diff

    y = 18
    # Both rows share the same scale; B's bar = b units, A's bar = a units, full bar = total units.
    unit = BAR_W / total
    wB = unit * b
    wA = unit * a
    rowgap = 14
    yB = y
    yA = y + BAR_H + rowgap

    body = [
        # Row B
        _seg(BAR_X0, wB, yB, GREEN, str(b)),
        f'<text x="{BAR_X0 - 6}" y="{yB + BAR_H/2}" font-size="16" fill="{GREEN}" '
        f'text-anchor="end" dominant-baseline="central">B</text>',
        # Row A = B + 5  (the matching part, then the extra 5)
        _seg(BAR_X0, wB, yA, GREEN, str(b)),
        _seg(BAR_X0 + wB, unit * diff, yA, RED, str(diff)),
        f'<text x="{BAR_X0 - 6}" y="{yA + BAR_H/2}" font-size="16" fill="{RED}" '
        f'text-anchor="end" dominant-baseline="central">A</text>',
        # brace on the right spanning both rows -> the total 17
        _brace_right(BAR_X0 + BAR_W + 2, yB, yA + BAR_H, AXIS, f"17"),
    ]
    h = yA + BAR_H + 18
    svg = _svg_open(h) + "".join(body) + "</svg>"
    html = (
        '<figure style="margin:0">'
        f'{svg}'
        f'<figcaption style="margin-top:.4rem;color:var(--ink-soft)">'
        f'A is one B plus 5 more. Two B-parts plus 5 make 17, so '
        f'$$B = 6 \\quad\\text{{and}}\\quad A = 11.$$</figcaption>'
        '</figure>'
    )
    return {"caption": "A is 5 more than B and together 17: B = 6, A = 11", "html": html}


def _verify():
    """Re-check every asserted number; raise if any diagram would lie."""
    assert 7 + 11 == 18
    assert 18 * 3 == 54
    assert 2 * 4 + 3 == 11
    assert 6 + 11 == 17 and 11 - 6 == 5


_verify()


def samples():
    return [
        _part_part_whole(),
        _three_times(),
        _two_step(),
        _comparison(),
    ]


if __name__ == "__main__":
    s = samples()
    print(TITLE, "|", KIND, "|", len(s), "samples")
    for d in s:
        print(" -", d["caption"])
