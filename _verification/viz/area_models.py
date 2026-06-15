# -*- coding: utf-8 -*-
"""Area models & algebra tiles -- deterministic labeled SVG figures.

Every figure shows the REAL terms of an area model. The cell areas in each
grid sum to the stated product; each identity below is verified with sympy in
the module's __main__ self-check (run `python area_models.py`).

Verified identities (sympy):
  (1) 2(x+4)            = 2x + 8                       [cells 2x, 8]
  (2) (x+2)(x+3)        = x^2 + 5x + 6                 [cells x^2, 3x, 2x, 6]
  (3) x^2 + 5x + 6      = (x+2)(x+3)                   [factoring, sides recovered]
  (4) 2x + 3x           = 5x   ;  2x + 3 stays 2x + 3  [like vs unlike terms]
  (5) x^2 + 6x          = (x+3)^2 - 9                  [completing the square]
"""

TITLE = "Area models & algebra tiles"
KIND = "deterministic-svg"
BLURB = "Rectangles split into labeled cells so a product, a factoring, or a completed square becomes something you can see and add up."
LESSONS = ["2.3", "10.4", "11.2", "12.4"]

# --- palette (exact hex so the book's dark-mode overrides apply) ------------
BLUE = "#2980b9"      # the x-dimension / x^2 region
VIOLET = "#8e44ad"    # the constant dimension / mixed cells
RED = "#c0392b"       # the constant*constant cell / "what's missing"
GREEN = "#27ae60"     # totals, "now they match" outcomes
AXIS = "#888"         # neutral guide lines & dimension ticks
GOLD = "#a9740f"      # the added corner in completing the square

# Soft transparent fills keep the figure calm and let stroke colors carry the
# meaning; transparency means the paper/dark background shows through cleanly.
FILL_OP = "0.13"


def _svg(slug, view_w, view_h, body):
    """Wrap an SVG body. Transparent background; rounded caps; roomy padding."""
    return (
        f'<figure class="fig" style="margin:0">'
        f'<svg viewBox="0 0 {view_w} {view_h}" xmlns="http://www.w3.org/2000/svg" '
        f'font-family="sans-serif" role="img" '
        f'stroke-linecap="round" stroke-linejoin="round" '
        f'style="max-width:{view_w}px;width:100%;height:auto;display:block;margin:0 auto">'
        f'{body}</svg></figure>'
    )


def _cell(x, y, w, h, stroke, fill=True, sw="2.5"):
    f = f' fill="{stroke}" fill-opacity="{FILL_OP}"' if fill else ' fill="none"'
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" '
        f'stroke="{stroke}" stroke-width="{sw}"{f}/>'
    )


def _label(x, y, txt, fill, size="17", weight="600", anchor="middle"):
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" '
        f'fill="{fill}" text-anchor="{anchor}" '
        f'dominant-baseline="middle">{txt}</text>'
    )


def _dim(x, y, txt, fill, size="14", anchor="middle"):
    """A dimension (side-length) label -- lighter, italic-feeling guide text."""
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" font-weight="500" '
        f'fill="{fill}" text-anchor="{anchor}" '
        f'dominant-baseline="middle">{txt}</text>'
    )


def _brace_top(x1, x2, y, fill):
    """A simple flat dimension line with end ticks, sitting above a width."""
    t = 5
    return (
        f'<path d="M{x1} {y+t} V{y} H{x2} V{y+t}" fill="none" '
        f'stroke="{fill}" stroke-width="1.6" opacity="0.75"/>'
    )


def _brace_left(y1, y2, x, fill):
    t = 5
    return (
        f'<path d="M{x+t} {y1} H{x} V{y2} H{x+t}" fill="none" '
        f'stroke="{fill}" stroke-width="1.6" opacity="0.75"/>'
    )


# ---------------------------------------------------------------------------
# (1) Distributive:  2(x+4) = 2x + 8
# ---------------------------------------------------------------------------
def _distributive():
    # Layout: height 2 (fixed), widths x (wide) and 4 (narrower).
    x0, y0 = 70, 56
    h = 96            # the "2" side
    wx = 168          # visual width for x
    w4 = 96           # visual width for 4
    body = []
    # cell 2x
    body.append(_cell(x0, y0, wx, h, BLUE))
    body.append(_label(x0 + wx / 2, y0 + h / 2, "2x", BLUE, size="22"))
    # cell 8
    body.append(_cell(x0 + wx, y0, w4, h, VIOLET))
    body.append(_label(x0 + wx + w4 / 2, y0 + h / 2, "8", VIOLET, size="22"))
    # left dimension "2"
    body.append(_brace_left(y0, y0 + h, x0 - 12, AXIS))
    body.append(_dim(x0 - 26, y0 + h / 2, "2", AXIS, size="16"))
    # top dimensions x and 4
    body.append(_brace_top(x0, x0 + wx, y0 - 12, AXIS))
    body.append(_dim(x0 + wx / 2, y0 - 26, "x", AXIS, size="16"))
    body.append(_brace_top(x0 + wx, x0 + wx + w4, y0 - 12, AXIS))
    body.append(_dim(x0 + wx + w4 / 2, y0 - 26, "4", AXIS, size="16"))
    svg = _svg("dist", 360, 184, "".join(body))
    return (
        '<div style="display:flex;flex-direction:column;gap:.5rem;align-items:center">'
        + svg
        + '<div>$$2(x+4)=\\underbrace{2x}_{\\text{width }x}+\\underbrace{8}_{\\text{width }4}$$</div>'
        + "</div>"
    )


# ---------------------------------------------------------------------------
# (2) FOIL:  (x+2)(x+3) = x^2 + 5x + 6
# ---------------------------------------------------------------------------
def _foil():
    # Columns: x (wide), 3 (narrow).  Rows: x (tall), 2 (short).
    x0, y0 = 86, 60
    wx, w3 = 150, 78        # column widths for x and 3
    hx, h2 = 150, 70        # row heights for x and 2
    body = []
    # top-left x*x = x^2
    body.append(_cell(x0, y0, wx, hx, BLUE))
    body.append(_label(x0 + wx / 2, y0 + hx / 2, "x²", BLUE, size="24"))
    # top-right 3*x = 3x
    body.append(_cell(x0 + wx, y0, w3, hx, VIOLET))
    body.append(_label(x0 + wx + w3 / 2, y0 + hx / 2, "3x", VIOLET, size="20"))
    # bottom-left x*2 = 2x
    body.append(_cell(x0, y0 + hx, wx, h2, VIOLET))
    body.append(_label(x0 + wx / 2, y0 + hx + h2 / 2, "2x", VIOLET, size="20"))
    # bottom-right 3*2 = 6
    body.append(_cell(x0 + wx, y0 + hx, w3, h2, RED))
    body.append(_label(x0 + wx + w3 / 2, y0 + hx + h2 / 2, "6", RED, size="20"))
    # top dimensions: x , 3
    body.append(_brace_top(x0, x0 + wx, y0 - 12, AXIS))
    body.append(_dim(x0 + wx / 2, y0 - 26, "x", AXIS, size="16"))
    body.append(_brace_top(x0 + wx, x0 + wx + w3, y0 - 12, AXIS))
    body.append(_dim(x0 + wx + w3 / 2, y0 - 26, "3", AXIS, size="16"))
    # left dimensions: x , 2
    body.append(_brace_left(y0, y0 + hx, x0 - 12, AXIS))
    body.append(_dim(x0 - 26, y0 + hx / 2, "x", AXIS, size="16"))
    body.append(_brace_left(y0 + hx, y0 + hx + h2, x0 - 12, AXIS))
    body.append(_dim(x0 - 26, y0 + hx + h2 / 2, "2", AXIS, size="16"))
    svg = _svg("foil", 360, 320, "".join(body))
    return (
        '<div style="display:flex;flex-direction:column;gap:.5rem;align-items:center">'
        + svg
        + '<div>$$(x+2)(x+3)=x^2+\\underbrace{3x+2x}_{5x}+6=x^2+5x+6$$</div>'
        + "</div>"
    )


# ---------------------------------------------------------------------------
# (3) Factoring:  x^2 + 5x + 6 = (x+2)(x+3)  (same grid, read backwards)
# ---------------------------------------------------------------------------
def _factoring():
    x0, y0 = 92, 64
    wx, w3 = 150, 78
    hx, h2 = 150, 70
    body = []
    # Inside cells: GIVEN polynomial (greyed-as-known), the puzzle pieces.
    body.append(_cell(x0, y0, wx, hx, BLUE))
    body.append(_label(x0 + wx / 2, y0 + hx / 2, "x²", BLUE, size="24"))
    body.append(_cell(x0 + wx, y0, w3, hx, VIOLET))
    body.append(_label(x0 + wx + w3 / 2, y0 + hx / 2, "3x", VIOLET, size="20"))
    body.append(_cell(x0, y0 + hx, wx, h2, VIOLET))
    body.append(_label(x0 + wx / 2, y0 + hx + h2 / 2, "2x", VIOLET, size="20"))
    body.append(_cell(x0 + wx, y0 + hx, w3, h2, RED))
    body.append(_label(x0 + wx + w3 / 2, y0 + hx + h2 / 2, "6", RED, size="20"))
    # RECOVERED sides drawn in green with a small "?-solved" feel.
    # top: x , 3
    body.append(_brace_top(x0, x0 + wx, y0 - 12, GREEN))
    body.append(_dim(x0 + wx / 2, y0 - 27, "x", GREEN, size="17"))
    body.append(_brace_top(x0 + wx, x0 + wx + w3, y0 - 12, GREEN))
    body.append(_dim(x0 + wx + w3 / 2, y0 - 27, "3", GREEN, size="17"))
    # left: x , 2
    body.append(_brace_left(y0, y0 + hx, x0 - 12, GREEN))
    body.append(_dim(x0 - 28, y0 + hx / 2, "x", GREEN, size="17"))
    body.append(_brace_left(y0 + hx, y0 + hx + h2, x0 - 12, GREEN))
    body.append(_dim(x0 - 28, y0 + hx + h2 / 2, "2", GREEN, size="17"))
    svg = _svg("fact", 360, 320, "".join(body))
    return (
        '<div style="display:flex;flex-direction:column;gap:.5rem;align-items:center">'
        + '<div style="color:var(--ink-soft);font-size:.95em">Fill the grid, then read the sides you needed:</div>'
        + svg
        + '<div>$$x^2+5x+6=(x+2)(x+3)$$</div>'
        + "</div>"
    )


# ---------------------------------------------------------------------------
# (4) Algebra tiles:  2x + 3x = 5x   (and 2x + 3 will NOT combine)
# ---------------------------------------------------------------------------
def _tile_x(x, y, fill):
    """A long unit-x tile: tall, thin -- length x, width 1."""
    w, h = 26, 92
    return _cell(x, y, w, h, fill, sw="2.5") + _label(
        x + w / 2, y + h / 2, "x", fill, size="15"
    ), w


def _tile_one(x, y, fill):
    """A small unit tile: 1 by 1."""
    s = 26
    return _cell(x, y, s, s, fill, sw="2.5") + _label(
        x + s / 2, y + s / 2, "1", fill, size="13"
    ), s


def _tiles():
    body = []
    gap = 8
    top = 30
    # --- like terms: 2 x-tiles + 3 x-tiles -> 5 x-tiles
    x = 24
    for _ in range(2):
        s, w = _tile_x(x, top, BLUE)
        body.append(s)
        x += w + gap
    body.append(_label(x + 6, top + 46, "+", AXIS, size="20"))
    x += 22
    for _ in range(3):
        s, w = _tile_x(x, top, VIOLET)
        body.append(s)
        x += w + gap
    body.append(_label(x + 8, top + 46, "=", GREEN, size="22"))
    x += 30
    # the combined 5 tiles, drawn in green to say "now they're one group"
    for _ in range(5):
        s, w = _tile_x(x, top, GREEN)
        body.append(s)
        x += w + gap
    width1 = x + 8
    svg_like = _svg("tilesA", width1, 150, "".join(body))

    # --- unlike terms: 2 x-tiles + 3 unit-tiles -> stays as-is
    body2 = []
    top2 = 30
    x = 24
    for _ in range(2):
        s, w = _tile_x(x, top2, BLUE)
        body2.append(s)
        x += w + gap
    body2.append(_label(x + 6, top2 + 46, "+", AXIS, size="20"))
    x += 22
    # three unit tiles share the bottom line (different shape => can't merge)
    base = top2 + 92 - 26
    for _ in range(3):
        s, w = _tile_one(x, base, RED)
        body2.append(s)
        x += w + gap
    body2.append(
        _label(x + 30, top2 + 46, "stays 2x + 3", RED, size="16", anchor="middle")
    )
    width2 = x + 90
    svg_unlike = _svg("tilesB", width2, 150, "".join(body2))

    return (
        '<div style="display:flex;flex-direction:column;gap:1rem;align-items:center">'
        + '<div style="color:var(--ink-soft);font-size:.95em">Same shape (same size) tiles combine:</div>'
        + svg_like
        + "<div>$$2x+3x=5x$$</div>"
        + '<div style="color:var(--ink-soft);font-size:.95em;margin-top:.3rem">Different shapes can’t merge into one number:</div>'
        + svg_unlike
        + '<div>$$2x+3\\ \\text{is already simplest}$$</div>'
        + "</div>"
    )


# ---------------------------------------------------------------------------
# (5) Completing the square:  x^2 + 6x = (x+3)^2 - 9
# ---------------------------------------------------------------------------
def _complete_square():
    x0, y0 = 80, 62
    sq = 150          # the x-by-x square side
    strip = 64        # the "3" strip thickness (visual)
    body = []
    # big x^2 square (top-left)
    body.append(_cell(x0, y0, sq, sq, BLUE))
    body.append(_label(x0 + sq / 2, y0 + sq / 2, "x²", BLUE, size="26"))
    # right strip: x tall, 3 wide -> 3x   (split 6x as 3x + 3x)
    body.append(_cell(x0 + sq, y0, strip, sq, VIOLET))
    body.append(_label(x0 + sq + strip / 2, y0 + sq / 2, "3x", VIOLET, size="18"))
    # bottom strip: 3 tall, x wide -> 3x
    body.append(_cell(x0, y0 + sq, sq, strip, VIOLET))
    body.append(_label(x0 + sq / 2, y0 + sq + strip / 2, "3x", VIOLET, size="18"))
    # the MISSING corner 3x3 = 9 (dashed, "add this")
    body.append(
        f'<rect x="{x0 + sq}" y="{y0 + sq}" width="{strip}" height="{strip}" rx="6" '
        f'fill="{GOLD}" fill-opacity="0.16" stroke="{GOLD}" stroke-width="2.5" '
        f'stroke-dasharray="6 5"/>'
    )
    body.append(_label(x0 + sq + strip / 2, y0 + sq + strip / 2 - 8, "9", GOLD, size="20"))
    body.append(
        _dim(x0 + sq + strip / 2, y0 + sq + strip / 2 + 12, "add", GOLD, size="12")
    )
    # dimensions on top: x , 3   and left: x , 3  -> the completed side is (x+3)
    body.append(_brace_top(x0, x0 + sq, y0 - 12, AXIS))
    body.append(_dim(x0 + sq / 2, y0 - 26, "x", AXIS, size="16"))
    body.append(_brace_top(x0 + sq, x0 + sq + strip, y0 - 12, GOLD))
    body.append(_dim(x0 + sq + strip / 2, y0 - 26, "3", GOLD, size="16"))
    body.append(_brace_left(y0, y0 + sq, x0 - 12, AXIS))
    body.append(_dim(x0 - 26, y0 + sq / 2, "x", AXIS, size="16"))
    body.append(_brace_left(y0 + sq, y0 + sq + strip, x0 - 12, GOLD))
    body.append(_dim(x0 - 26, y0 + sq + strip / 2, "3", GOLD, size="16"))
    svg = _svg("cmpsq", 320, 320, "".join(body))
    return (
        '<div style="display:flex;flex-direction:column;gap:.5rem;align-items:center">'
        + '<div style="color:var(--ink-soft);font-size:.95em">Split 6x into two 3-wide strips; the dashed corner is what completes the big square:</div>'
        + svg
        + '<div>$$x^2+6x=(x+3)^2-9$$</div>'
        + '<div style="color:var(--ink-soft);font-size:.9em">filled square is $(x+3)^2$; we added $9$, so we subtract it back.</div>'
        + "</div>"
    )


def samples():
    return [
        {
            "caption": "Distributive law: 2(x+4) is one rectangle, two cells (2x and 8).",
            "html": _distributive(),
        },
        {
            "caption": "FOIL as area: (x+2)(x+3) fills a 2×2 grid that adds to x²+5x+6.",
            "html": _foil(),
        },
        {
            "caption": "Factoring backwards: fill x²+5x+6 into the grid to recover the sides (x+2)(x+3).",
            "html": _factoring(),
        },
        {
            "caption": "Algebra tiles: like x-tiles combine (2x+3x=5x); an x-tile and unit tiles cannot.",
            "html": _tiles(),
        },
        {
            "caption": "Completing the square: x²+6x plus the missing 3×3 corner makes (x+3)² − 9.",
            "html": _complete_square(),
        },
    ]


if __name__ == "__main__":
    # Self-check: prove every asserted identity before trusting the pixels.
    import sympy as sp

    x = sp.Symbol("x")
    checks = [
        ("2(x+4) == 2x+8", sp.expand(2 * (x + 4)) == sp.expand(2 * x + 8)),
        (
            "(x+2)(x+3) == x^2+5x+6",
            sp.expand((x + 2) * (x + 3)) == sp.expand(x**2 + 5 * x + 6),
        ),
        (
            "cells x^2+3x+2x+6 == x^2+5x+6",
            sp.expand(x**2 + 3 * x + 2 * x + 6) == sp.expand(x**2 + 5 * x + 6),
        ),
        ("factor(x^2+5x+6) == (x+2)(x+3)", sp.factor(x**2 + 5 * x + 6) == (x + 2) * (x + 3)),
        ("2x+3x == 5x", sp.simplify(2 * x + 3 * x) == 5 * x),
        ("2x+3 stays 2x+3", sp.simplify(2 * x + 3) == 2 * x + 3),
        ("x^2+6x == (x+3)^2-9", sp.expand(x**2 + 6 * x) == sp.expand((x + 3) ** 2 - 9)),
        ("strips 3x+3x == 6x", sp.expand(3 * x + 3 * x) == sp.expand(6 * x)),
        ("corner 3*3 == 9", 3 * 3 == 9),
        ("filled square x^2+6x+9 == (x+3)^2", sp.factor(x**2 + 6 * x + 9) == (x + 3) ** 2),
    ]
    ok = all(v for _, v in checks)
    for name, v in checks:
        print(("PASS" if v else "FAIL"), name)
    print(TITLE, "|", len(samples()), "samples |", "ALL OK" if ok else "*** FAILURE ***")
    assert ok
