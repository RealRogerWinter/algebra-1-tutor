"""Statistics charts -- candidate visual-element type for the Algebra 1 textbook.

Three deterministic SVG charts, each computed from a small fixed dataset with plain
Python arithmetic and drawn to scale:
  (1) box-and-whisker plot  (min, Q1, median, Q3, max)
  (2) histogram             (5 equal-width bins; bar heights = counts)
  (3) two-way table 2x2     (row/col totals; one cell highlighted for an association)

Every asserted number (a quartile position, a bar height, a percentage) is computed,
re-checked by _selftest() at import time, and labelled with the real value. KaTeX
renders the math written as $$ ... $$. Colours are the book's fixed hexes so dark-mode
overrides apply; SVG backgrounds stay transparent.
"""

from fractions import Fraction as F

TITLE = "Statistics charts"
KIND = "deterministic-svg"
BLURB = "Box-and-whisker plots, histograms, and two-way tables drawn to scale from a small dataset, every quartile and count computed exactly."
LESSONS = ["A.1", "A.3"]

# ---- palette (book's fixed hexes; dark-mode overrides key off these) ---------------------------
BLUE = "#2980b9"
VIOLET = "#8e44ad"
RED = "#c0392b"
GREEN = "#27ae60"
GOLD = "#a9740f"
AXIS = "#888"


# ================================================================================================
# shared helpers
# ================================================================================================
def _svg(view_w, view_h, body, slug):
    """Wrap body in a transparent, responsive inline SVG."""
    return (
        f'<svg viewBox="0 0 {view_w} {view_h}" xmlns="http://www.w3.org/2000/svg" '
        f'role="img" font-family="sans-serif" '
        f'style="width:100%;max-width:{view_w}px;height:auto;display:block;margin:0 auto" '
        f'data-slug="{slug}">\n{body}\n</svg>'
    )


def _r2(x):
    """Round to 2 dp, dropping a trailing .0 so coordinates stay tidy."""
    v = round(float(x), 2)
    return int(v) if v == int(v) else v


def _med(xs):
    """Median of a list as an exact Fraction."""
    xs = sorted(xs)
    m = len(xs)
    if m % 2:
        return F(xs[m // 2])
    return F(xs[m // 2 - 1] + xs[m // 2], 2)


def _num(fr):
    """Render a Fraction as a tidy number string (12, 5.5, or 7/2 if non-terminating-ish)."""
    if fr.denominator == 1:
        return str(fr.numerator)
    dec = fr.numerator / fr.denominator
    # show one or two decimals when they terminate cleanly; else fall back to a fraction
    if abs(dec * 2 - round(dec * 2)) < 1e-9:
        s = f"{dec:.1f}"
    elif abs(dec * 100 - round(dec * 100)) < 1e-9:
        s = f"{dec:.2f}"
    else:
        return f"{fr.numerator}/{fr.denominator}"
    return s


# ================================================================================================
# (1) BOX-AND-WHISKER PLOT
# ================================================================================================
# Nine quiz scores (already sorted). n = 9 is odd, so the median is the 5th value; the lower and
# upper halves (4 values each) exclude the median -- the common school "exclusive" method.
_BOX_DATA = [6, 7, 7, 8, 9, 9, 10, 10, 12]


def _box_stats(data):
    s = sorted(data)
    n = len(s)
    half = n // 2
    return {
        "min": F(s[0]),
        "q1": _med(s[:half]),
        "med": _med([s[half]]) if n % 2 else _med(s),
        "q3": _med(s[half + 1:] if n % 2 else s[half:]),
        "max": F(s[-1]),
    }


def _box_plot():
    st = _box_stats(_BOX_DATA)
    lo = float(st["min"])
    q1 = float(st["q1"])
    me = float(st["med"])
    q3 = float(st["q3"])
    hi = float(st["max"])

    # axis runs a touch below min and above max so whiskers have breathing room
    a_lo, a_hi = 4, 14          # tick range chosen to bracket the data with even ticks
    W, H = 360, 150
    left, right = 30, 330
    y_axis = 118               # baseline for the number line
    y_box = 56                 # vertical centre of the box
    box_h = 36
    y_top = y_box - box_h / 2
    y_bot = y_box + box_h / 2

    def X(v):
        return left + (v - a_lo) * (right - left) / (a_hi - a_lo)

    parts = []

    # --- number-line axis with integer ticks ---
    parts.append(
        f'<line x1="{left}" y1="{y_axis}" x2="{right}" y2="{y_axis}" '
        f'stroke="{AXIS}" stroke-width="2.5" stroke-linecap="round"/>'
    )
    for v in range(a_lo, a_hi + 1, 2):
        tx = _r2(X(v))
        parts.append(
            f'<line x1="{tx}" y1="{y_axis}" x2="{tx}" y2="{y_axis + 6}" '
            f'stroke="{AXIS}" stroke-width="1.5" stroke-linecap="round"/>'
        )
        parts.append(
            f'<text x="{tx}" y="{y_axis + 20}" font-size="11" fill="{AXIS}" '
            f'text-anchor="middle">{v}</text>'
        )

    # --- whiskers (min -> Q1, Q3 -> max) with end caps ---
    xlo, xq1, xme, xq3, xhi = (_r2(X(v)) for v in (lo, q1, me, q3, hi))
    parts.append(
        f'<line x1="{xlo}" y1="{y_box}" x2="{xq1}" y2="{y_box}" '
        f'stroke="{BLUE}" stroke-width="2.5" stroke-linecap="round"/>'
    )
    parts.append(
        f'<line x1="{xq3}" y1="{y_box}" x2="{xhi}" y2="{y_box}" '
        f'stroke="{BLUE}" stroke-width="2.5" stroke-linecap="round"/>'
    )
    for xc in (xlo, xhi):
        parts.append(
            f'<line x1="{xc}" y1="{_r2(y_box - 9)}" x2="{xc}" y2="{_r2(y_box + 9)}" '
            f'stroke="{BLUE}" stroke-width="2.5" stroke-linecap="round"/>'
        )

    # --- the box (Q1 -> Q3), softly tinted, with the median line in red ---
    parts.append(
        f'<rect x="{xq1}" y="{_r2(y_top)}" width="{_r2(xq3 - xq1)}" height="{_r2(box_h)}" '
        f'rx="4" fill="{BLUE}" fill-opacity="0.12" stroke="{BLUE}" stroke-width="2.5"/>'
    )
    parts.append(
        f'<line x1="{xme}" y1="{_r2(y_top)}" x2="{xme}" y2="{_r2(y_bot)}" '
        f'stroke="{RED}" stroke-width="2.5" stroke-linecap="round"/>'
    )

    # --- value labels above each marker (real computed numbers) ---
    labels = [
        (xlo, _num(st["min"]), AXIS),
        (xq1, _num(st["q1"]), BLUE),
        (xme, _num(st["med"]), RED),
        (xq3, _num(st["q3"]), BLUE),
        (xhi, _num(st["max"]), AXIS),
    ]
    # min & max sit a little higher so they don't collide with the box edges
    for xc, txt, col in labels:
        yy = _r2(y_top - 8)
        parts.append(
            f'<text x="{xc}" y="{yy}" font-size="11" fill="{col}" '
            f'text-anchor="middle" font-weight="600">{txt}</text>'
        )

    return _svg(W, H, "  " + "\n  ".join(parts), "box")


# ================================================================================================
# (2) HISTOGRAM
# ================================================================================================
# Minutes a class spent studying. Five equal-width bins of width 10 over [40, 90); the top bin is
# inclusive of 90. Bar height = count in the bin; counts sum to n.
_HIST_DATA = [42, 51, 53, 58, 61, 64, 66, 67, 72, 74, 78, 83]
_HIST_EDGES = [40, 50, 60, 70, 80, 90]


def _hist_counts(data, edges):
    counts = []
    for i in range(len(edges) - 1):
        lo, hi = edges[i], edges[i + 1]
        last = i == len(edges) - 2
        if last:
            counts.append(sum(1 for v in data if lo <= v <= hi))
        else:
            counts.append(sum(1 for v in data if lo <= v < hi))
    return counts


def _histogram():
    counts = _hist_counts(_HIST_DATA, _HIST_EDGES)
    nbins = len(counts)
    top = max(counts)            # tallest bar -> top gridline count

    W, H = 360, 200
    left, right = 38, 338
    base = 158                   # y of the horizontal axis
    plot_top = 26                # y reserved for the tallest bar's top
    plot_h = base - plot_top
    plot_w = right - left
    gap = 6                      # px gap between adjacent bars
    bw = (plot_w - gap * (nbins - 1)) / nbins

    def Y(count):
        return base - (count / top) * plot_h

    parts = []

    # --- faint horizontal gridlines + count ticks (0..top) on the left ---
    for c in range(top + 1):
        gy = _r2(Y(c))
        if c > 0:
            parts.append(
                f'<line x1="{left}" y1="{gy}" x2="{right}" y2="{gy}" '
                f'stroke="{AXIS}" stroke-width="1" stroke-opacity="0.25"/>'
            )
        parts.append(
            f'<text x="{left - 8}" y="{gy + 4}" font-size="10" fill="{AXIS}" '
            f'text-anchor="end">{c}</text>'
        )

    # --- bars (height = count), tinted with a solid top edge ---
    for i, c in enumerate(counts):
        x = left + i * (bw + gap)
        h = base - Y(c)
        parts.append(
            f'<rect x="{_r2(x)}" y="{_r2(Y(c))}" width="{_r2(bw)}" height="{_r2(h)}" '
            f'rx="3" fill="{VIOLET}" fill-opacity="0.18" '
            f'stroke="{VIOLET}" stroke-width="2.5"/>'
        )
        # count printed just above each bar
        parts.append(
            f'<text x="{_r2(x + bw / 2)}" y="{_r2(Y(c) - 6)}" font-size="11" '
            f'fill="{VIOLET}" text-anchor="middle" font-weight="600">{c}</text>'
        )
        # bin edge label centred under the bar (e.g. 40-50)
        parts.append(
            f'<text x="{_r2(x + bw / 2)}" y="{base + 16}" font-size="10" '
            f'fill="{AXIS}" text-anchor="middle">{_HIST_EDGES[i]}–{_HIST_EDGES[i + 1]}</text>'
        )

    # --- axis line on top of the bars' baseline ---
    parts.append(
        f'<line x1="{left}" y1="{base}" x2="{right}" y2="{base}" '
        f'stroke="{AXIS}" stroke-width="2.5" stroke-linecap="round"/>'
    )

    return _svg(W, H, "  " + "\n  ".join(parts), "hist")


# ================================================================================================
# (3) TWO-WAY TABLE (2x2 with totals + highlighted cell)
# ================================================================================================
# Matches the Lesson A.3 worked-example table exactly (n = 50): rows = owns a pet (Yes / No),
# columns = where they live (Apartment / House). Comparing DOWN the columns, the apartment
# pet-rate is 6/20 = 30% and the house pet-rate is 24/30 = 80% -> a real association. The
# high-rate cell (pet & house) is highlighted as the "busy corner".
_TW = {
    "pet_apt": 6, "pet_house": 24,
    "no_apt": 14, "no_house": 6,
}


def _two_way():
    pet_apt = _TW["pet_apt"]
    pet_house = _TW["pet_house"]
    no_apt = _TW["no_apt"]
    no_house = _TW["no_house"]
    row_pet = pet_apt + pet_house
    row_no = no_apt + no_house
    col_apt = pet_apt + no_apt
    col_house = pet_house + no_house
    grand = row_pet + row_no

    apt_rate = F(pet_apt, col_apt)        # of apartment dwellers, the share with a pet
    house_rate = F(pet_house, col_house)  # of house dwellers, the share with a pet

    hi = (f"background:rgba(169,116,15,0.16);"
          f"outline:2px solid {GOLD};outline-offset:-2px;font-weight:700;color:{GOLD}")
    cap = "color:var(--ink-soft);font-size:.85em;text-align:left;padding-bottom:.3rem"

    # Plain HTML table styled to lean on the book's own table CSS + variables.
    return f"""<div style="max-width:440px;margin:0 auto">
  <table style="border-collapse:collapse;width:100%;background:var(--card);border-radius:var(--radius-sm);overflow:hidden;font-size:.95em">
    <caption style="{cap}">Owning a pet vs. where people live (n = {grand})</caption>
    <thead>
      <tr>
        <th style="border:1px solid var(--rule);padding:.45rem .6rem;background:var(--card-2)"></th>
        <th style="border:1px solid var(--rule);padding:.45rem .6rem;background:var(--card-2);text-align:center">Apartment</th>
        <th style="border:1px solid var(--rule);padding:.45rem .6rem;background:var(--card-2);text-align:center">House</th>
        <th style="border:1px solid var(--rule);padding:.45rem .6rem;background:var(--card-2);text-align:center">Total</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th style="border:1px solid var(--rule);padding:.45rem .6rem;background:var(--card-2);text-align:left">Pet: Yes</th>
        <td style="border:1px solid var(--rule);padding:.45rem .6rem;text-align:center">{pet_apt}</td>
        <td style="border:1px solid var(--rule);padding:.45rem .6rem;text-align:center;{hi}">{pet_house}</td>
        <td style="border:1px solid var(--rule);padding:.45rem .6rem;text-align:center;color:var(--ink-soft)">{row_pet}</td>
      </tr>
      <tr>
        <th style="border:1px solid var(--rule);padding:.45rem .6rem;background:var(--card-2);text-align:left">Pet: No</th>
        <td style="border:1px solid var(--rule);padding:.45rem .6rem;text-align:center">{no_apt}</td>
        <td style="border:1px solid var(--rule);padding:.45rem .6rem;text-align:center">{no_house}</td>
        <td style="border:1px solid var(--rule);padding:.45rem .6rem;text-align:center;color:var(--ink-soft)">{row_no}</td>
      </tr>
      <tr>
        <th style="border:1px solid var(--rule);padding:.45rem .6rem;background:var(--card-2);text-align:left">Total</th>
        <td style="border:1px solid var(--rule);padding:.45rem .6rem;text-align:center;color:var(--ink-soft)">{col_apt}</td>
        <td style="border:1px solid var(--rule);padding:.45rem .6rem;text-align:center;color:var(--ink-soft)">{col_house}</td>
        <td style="border:1px solid var(--rule);padding:.45rem .6rem;text-align:center;color:var(--ink-soft);font-weight:700">{grand}</td>
      </tr>
    </tbody>
  </table>
  <p style="margin:.7rem 0 0;color:var(--ink-soft);font-size:.92em;line-height:1.5">
    The gold cell is the busy corner. Comparing down the columns (within each place):
  </p>
  $$\\text{{apartment}}:\\ \\frac{{{pet_apt}}}{{{col_apt}}}={_num(apt_rate)}={_pct(apt_rate)}\\%
     \\qquad \\text{{house}}:\\ \\frac{{{pet_house}}}{{{col_house}}}={_num(house_rate)}={_pct(house_rate)}\\%$$
  <p style="margin:.4rem 0 0;color:var(--ink-soft);font-size:.92em;line-height:1.5">
    {_pct(house_rate)}% of house-dwellers have a pet versus {_pct(apt_rate)}% in apartments,
    so where you live and owning a pet are <strong style="color:var(--ink)">associated</strong>.
  </p>
</div>"""


def _pct(fr):
    """Fraction -> integer-or-tidy percent string (no % sign)."""
    p = fr * 100
    if p.denominator == 1:
        return str(p.numerator)
    return _num(p)


# ================================================================================================
# self-check (runs at import; a wrong pixel must not teach a falsehood)
# ================================================================================================
def _selftest():
    # (1) box plot
    st = _box_stats(_BOX_DATA)
    assert (st["min"], st["q1"], st["med"], st["q3"], st["max"]) == (
        F(6), F(7), F(9), F(10), F(12)
    ), st
    assert st["min"] <= st["q1"] <= st["med"] <= st["q3"] <= st["max"]

    # (2) histogram: counts must sum to n, none negative
    counts = _hist_counts(_HIST_DATA, _HIST_EDGES)
    assert counts == [1, 3, 4, 3, 1], counts
    assert sum(counts) == len(_HIST_DATA)

    # (3) two-way table: margins are internally consistent; the association is real
    pet_apt, pet_house = _TW["pet_apt"], _TW["pet_house"]
    no_apt, no_house = _TW["no_apt"], _TW["no_house"]
    grand = pet_apt + pet_house + no_apt + no_house
    assert (pet_apt + no_apt) + (pet_house + no_house) == grand
    assert F(pet_apt, pet_apt + no_apt) == F(3, 10)        # apartment: 6/20 = 30%
    assert F(pet_house, pet_house + no_house) == F(4, 5)   # house: 24/30 = 80%
    assert F(pet_apt + pet_house, grand) == F(3, 5)        # overall pet rate 30/50 = 60%
    return True


_selftest()


# ================================================================================================
# public API
# ================================================================================================
def samples():
    return [
        {
            "caption": (
                "Box-and-whisker plot of nine quiz scores: the box spans Q1 to Q3, "
                "the red line is the median, the whiskers reach the min and max."
            ),
            "html": _box_plot()
            + '\n<div style="text-align:center;color:var(--ink-soft);font-size:.9em;'
              'margin-top:.4rem">$$\\min=6,\\ Q_1=7,\\ \\text{median}=9,'
              '\\ Q_3=10,\\ \\max=12$$</div>',
        },
        {
            "caption": (
                "Histogram of study minutes sorted into five equal-width bins; "
                "each bar's height is the count in that bin."
            ),
            "html": _histogram()
            + '\n<div style="text-align:center;color:var(--ink-soft);font-size:.9em;'
              'margin-top:.3rem">minutes spent studying</div>',
        },
        {
            "caption": (
                "Two-way table (pets vs. housing, n = 50) with row and column totals; the "
                "highlighted cell and the two column percentages reveal an association."
            ),
            "html": _two_way(),
        },
    ]


if __name__ == "__main__":
    print(TITLE, "|", KIND)
    print("self-check:", _selftest())
    for s in samples():
        print("-", s["caption"][:70])
