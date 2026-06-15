"""Double number lines for ratio and proportional reasoning.

Two parallel number lines whose ticks line up vertically. A value on the
top line sits directly above its partner on the bottom line, so the
straight connector dropping between them *is* the proof of the ratio.

Every tick position is computed from the ratio itself (a fixed
pixels-per-unit on each line), so equal ratios always land in the same
column. The numbers printed are verified with plain arithmetic:

  (1) 60 mi : 1 hr   ->  60/1 = 120/2 = 180/3 = 60 mi per hr
  (2) 3 apples : 2 dollars -> 3/2 = 6/4 = 9/6 = 1.5 apples per dollar
  (3) percent        ->  10/40 = 25%, 20/40 = 50%, 40/40 = 100%
"""

TITLE = "Double number lines"
KIND = "deterministic-svg"
BLURB = "Two aligned number lines whose ticks line up to show a ratio holding steady."
LESSONS = ["3.1", "3.2", "3.3"]

# ---------------------------------------------------------------------------
# Palette (book colors; dark-mode overrides key on these exact hexes)
# ---------------------------------------------------------------------------
BLUE = "#2980b9"
VIOLET = "#8e44ad"
GREEN = "#27ae60"
GOLD = "#a9740f"
AXIS = "#888"

# Shared geometry for all three diagrams.
VB_W = 360.0          # viewBox width
X0 = 46.0             # x of the "0" tick (left padding)
X1 = 320.0           # x of the right-most tick (right padding)
SPAN = X1 - X0        # usable pixel span

TOP_Y = 56.0          # baseline y of the top line
BOT_Y = 132.0         # baseline y of the bottom line
TICK = 9.0            # half-height of a tick mark


def _x(value, vmax):
    """Pixel x for ``value`` on a line that runs 0..vmax across SPAN.

    Identical ``value/vmax`` ratios return identical x, which is exactly
    what makes corresponding ticks share a column.
    """
    return X0 + SPAN * (float(value) / float(vmax))


def _fmt(n):
    """Trim a float that is really an int ('2.0' -> '2')."""
    f = float(n)
    return str(int(f)) if f == int(f) else ("%g" % f)


def _line(y, color):
    """The horizontal rule for one number line."""
    return (
        f'<line x1="{X0:.1f}" y1="{y:.1f}" x2="{X1:.1f}" y2="{y:.1f}" '
        f'stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>'
        # soft arrow hint at the right end
        f'<path d="M {X1 - 7:.1f} {y - 4:.1f} L {X1 + 1:.1f} {y:.1f} '
        f'L {X1 - 7:.1f} {y + 4:.1f}" fill="none" stroke="{color}" '
        f'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
    )


def _tick(x, y, color, up=True):
    """A single tick mark; ``up`` puts it above the baseline."""
    y2 = y - TICK if up else y + TICK
    return (
        f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x:.1f}" y2="{y2:.1f}" '
        f'stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>'
    )


def _num(x, y, text, color, dy):
    """A small numeric tick label (numbers only, never an equation)."""
    return (
        f'<text x="{x:.1f}" y="{y + dy:.1f}" fill="{color}" font-size="13" '
        f'font-family="sans-serif" text-anchor="middle">{text}</text>'
    )


def _connector(x):
    """Dashed vertical line proving a top value pairs with a bottom value."""
    return (
        f'<line x1="{x:.1f}" y1="{TOP_Y:.1f}" x2="{x:.1f}" y2="{BOT_Y:.1f}" '
        f'stroke="{AXIS}" stroke-width="1.5" stroke-linecap="round" '
        f'stroke-dasharray="2 5" opacity="0.75"/>'
    )


def _svg(body, title):
    """Wrap drawing ``body`` in a padded, transparent svg."""
    return (
        f'<svg viewBox="0 0 {VB_W:.0f} 176" xmlns="http://www.w3.org/2000/svg" '
        f'font-family="sans-serif" role="img" aria-label="{title}" '
        f'style="max-width:480px;width:100%;height:auto">'
        f'{body}</svg>'
    )


def _diagram(top_label, bottom_label, top_color, bottom_color,
             top_max, bottom_max, pairs, title):
    """Build one double-number-line svg.

    ``pairs`` is a list of (top_value, bottom_value). Both values are
    placed by their own line's scale; when the ratio is consistent they
    resolve to the same x, and a connector is drawn once for the column.
    """
    parts = []

    # caption strips for each line, set just outside the drawing
    parts.append(
        f'<text x="{X0 - 8:.1f}" y="{TOP_Y - 22:.1f}" fill="{top_color}" '
        f'font-size="12.5" font-family="sans-serif" text-anchor="start" '
        f'font-weight="600">{top_label}</text>'
    )
    parts.append(
        f'<text x="{X0 - 8:.1f}" y="{BOT_Y + 34:.1f}" fill="{bottom_color}" '
        f'font-size="12.5" font-family="sans-serif" text-anchor="start" '
        f'font-weight="600">{bottom_label}</text>'
    )

    # connectors first so the lines/ticks sit on top of them
    for tv, bv in pairs:
        xt = _x(tv, top_max)
        xb = _x(bv, bottom_max)
        # When the ratio holds, xt == xb. Guard against float dust.
        assert abs(xt - xb) < 1e-6, (
            f"tick mismatch: {tv}/{top_max} vs {bv}/{bottom_max}"
        )
        parts.append(_connector(xt))

    # the two baselines
    parts.append(_line(TOP_Y, top_color))
    parts.append(_line(BOT_Y, bottom_color))

    # always include the 0 tick on each line
    parts.append(_tick(X0, TOP_Y, top_color, up=True))
    parts.append(_num(X0, TOP_Y, "0", top_color, -TICK - 4))
    parts.append(_tick(X0, BOT_Y, bottom_color, up=False))
    parts.append(_num(X0, BOT_Y, "0", bottom_color, TICK + 14))

    # value ticks + labels
    for tv, bv in pairs:
        x = _x(tv, top_max)
        parts.append(_tick(x, TOP_Y, top_color, up=True))
        parts.append(_num(x, TOP_Y, _fmt(tv), top_color, -TICK - 4))
        parts.append(_tick(x, BOT_Y, bottom_color, up=False))
        parts.append(_num(x, BOT_Y, _fmt(bv), bottom_color, TICK + 14))

    return _svg("".join(parts), title)


# ---------------------------------------------------------------------------
# Sample 1 — unit rate 60 miles : 1 hour
# ---------------------------------------------------------------------------
def _miles_hours():
    # verify the rate is the same at every tick
    pairs = [(60, 1), (120, 2), (180, 3)]
    assert len({(m / h) for m, h in pairs}) == 1, "speed not constant"
    assert all((m / h) == 60 for m, h in pairs)

    svg = _diagram(
        top_label="miles",
        bottom_label="hours",
        top_color=BLUE,
        bottom_color=VIOLET,
        top_max=180,      # right edge = 180 miles
        bottom_max=3,     # right edge = 3 hours  (180/3 = 60 = rate)
        pairs=pairs,
        title="Double number line: 60 miles per hour",
    )
    math = r"$$\frac{60\text{ mi}}{1\text{ hr}}=\frac{120\text{ mi}}{2\text{ hr}}=\frac{180\text{ mi}}{3\text{ hr}}=60\ \tfrac{\text{mi}}{\text{hr}}$$"
    return svg + math


# ---------------------------------------------------------------------------
# Sample 2 — ratio 3 apples : 2 dollars, scaled to 6:4 and 9:6
# ---------------------------------------------------------------------------
def _apples_dollars():
    pairs = [(3, 2), (6, 4), (9, 6)]
    from fractions import Fraction as F
    rates = {F(a, d) for a, d in pairs}
    assert rates == {F(3, 2)}, "ratio not constant"

    svg = _diagram(
        top_label="apples",
        bottom_label="dollars",
        top_color=GREEN,
        bottom_color=GOLD,
        top_max=9,        # right edge = 9 apples
        bottom_max=6,     # right edge = 6 dollars (9/6 = 3/2)
        pairs=pairs,
        title="Double number line: 3 apples for 2 dollars",
    )
    math = r"$$\frac{3\text{ apples}}{2\text{ dollars}}=\frac{6\text{ apples}}{4\text{ dollars}}=\frac{9\text{ apples}}{6\text{ dollars}}=\tfrac{3}{2}$$"
    return svg + math


# ---------------------------------------------------------------------------
# Sample 3 — percent: 0..40 aligned to 0%..100%
# ---------------------------------------------------------------------------
def _percent():
    # top values with the percent they represent of 40
    pairs = [(10, 25), (20, 50), (30, 75), (40, 100)]
    for v, p in pairs:
        assert v / 40 * 100 == p, f"{v} of 40 is not {p}%"

    svg = _diagram(
        top_label="amount",
        bottom_label="percent",
        top_color=BLUE,
        bottom_color=VIOLET,
        top_max=40,       # right edge = 40
        bottom_max=100,   # right edge = 100%  (40 over 40 = 100%)
        pairs=pairs,
        title="Double number line: amount lined up with percent",
    )
    # render the % labels nicely under the diagram via KaTeX
    math = r"$$10=25\%\quad 20=50\%\quad 40=100\%\ \text{ of }40$$"
    return svg + math


def samples():
    return [
        {
            "caption": "60 miles every 1 hour: the rate holds at each aligned tick",
            "html": _miles_hours(),
        },
        {
            "caption": "3 apples for 2 dollars, scaled up to 6 : 4 and 9 : 6",
            "html": _apples_dollars(),
        },
        {
            "caption": "amount over 40 aligned to percent: 10 sits under 25%, 20 under 50%",
            "html": _percent(),
        },
    ]


if __name__ == "__main__":
    items = samples()
    print(TITLE, len(items))
    for it in items:
        print("-", it["caption"])
