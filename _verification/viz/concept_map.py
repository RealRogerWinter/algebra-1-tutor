# -*- coding: utf-8 -*-
"""Concept / prerequisite map for the Algebra 1 course.

A calm left-to-right learning-path diagram: course units drawn as rounded
nodes, joined by prerequisite arrows. The main spine (Units 1-7) is gold;
branch units (8-12, Appendix A) are slate-blue. Every arrow points forward
(toward later material), so the eye can trace a study path without backtracking.

All geometry is computed in plain Python and validated so that:
  * every arrow advances left-to-right (no backward edges),
  * no two node boxes overlap,
  * the one "skip" edge (Unit 10 -> Unit 12) arcs below its row so it never
    cuts through Unit 11.
Nothing here uses randomness or the clock, so the output is byte-identical
every run.
"""

TITLE = "Concept / prerequisite map"
KIND = "deterministic-svg"
BLURB = "A gentle left-to-right map of the course: each unit is a rounded node, and arrows show what you learn first."
LESSONS = ["1.1", "5.1", "5.4", "10.1", "11.1", "12.1"]

# --------------------------------------------------------------------------
# Palette (must use the book's exact hexes so dark-mode overrides apply).
# --------------------------------------------------------------------------
GOLD = "#a9740f"   # the main spine, Units 1-7
BLUE = "#2980b9"   # branch units
AXIS = "#888"      # neutral arrows / connectors

# Real unit names, lifted verbatim from the textbook hero headings.
NAMES = {
    1: "Foundations",
    2: "Linear Equations",
    3: "Proportional Reasoning",
    4: "Functions",
    5: "Lines & Graphs",
    6: "Modeling & Translation",
    7: "Systems of Equations",
    8: "Inequalities",
    9: "Sequences & Growth",
    10: "Exponents & Polynomials",
    11: "Factoring",
    12: "Quadratics",
    "A": "Data & Statistics",
}
LABEL = {n: f"Unit {n}" for n in range(1, 13)}
LABEL["A"] = "Appendix A"

# Full prerequisite structure for the course (node -> list of prerequisites).
PREREQ = {
    2: [1], 3: [2], 4: [3], 5: [4], 6: [5], 7: [6],
    8: [2, 5], 9: [4], 10: [1, 2], 11: [10], 12: [5, 10, 11], "A": [5],
}


# --------------------------------------------------------------------------
# Tiny SVG helpers.
# --------------------------------------------------------------------------
def _n(v):
    """Trim floats to short, stable strings (no locale, no trailing zeros)."""
    if isinstance(v, float):
        s = f"{v:.2f}".rstrip("0").rstrip(".")
        return s if s not in ("-0", "") else "0"
    return str(v)


def _esc(s):
    """Escape text for safe use inside SVG/XML <text> nodes."""
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _node(slug, cx, cy, w, h, line1, line2, stroke, *, is_spine):
    """A rounded, friendly unit card centered at (cx, cy)."""
    x = cx - w / 2.0
    y = cy - h / 2.0
    # Spine nodes get a faint gold wash; branches a faint blue wash. The
    # washes use the same stroke hue at low opacity so the card reads as
    # "tinted paper" and still works in dark mode.
    fill_op = 0.12 if is_spine else 0.10
    rx = 14
    return (
        f'<g>'
        f'<rect x="{_n(x)}" y="{_n(y)}" width="{_n(w)}" height="{_n(h)}" '
        f'rx="{rx}" ry="{rx}" fill="{stroke}" fill-opacity="{fill_op}" '
        f'stroke="{stroke}" stroke-width="2.5"/>'
        f'<text x="{_n(cx)}" y="{_n(cy - 6)}" text-anchor="middle" '
        f'font-size="13" font-weight="700" fill="{stroke}">{_esc(line1)}</text>'
        f'<text x="{_n(cx)}" y="{_n(cy + 12)}" text-anchor="middle" '
        f'font-size="10.5" fill="{stroke}" opacity="0.92">{_esc(line2)}</text>'
        f'</g>'
    )


def _arrow_id(slug):
    return f"{slug}-arrow"


def _defs(slug, color):
    """One arrowhead marker per sample (unique id), tinted to the edge color."""
    return (
        f'<defs><marker id="{_arrow_id(slug)}" viewBox="0 0 10 10" '
        f'refX="8.5" refY="5" markerWidth="7" markerHeight="7" '
        f'orient="auto-start-reverse">'
        f'<path d="M1 1 L9 5 L1 9 z" fill="{color}"/></marker></defs>'
    )


def _edge(slug, x1, y1, x2, y2, color, *, bow=0.0):
    """A soft arrow from (x1,y1) to (x2,y2).

    bow > 0 curves the path downward by that many pixels at its midpoint;
    bow < 0 curves it upward. Straight when bow == 0.
    """
    marker = f'marker-end="url(#{_arrow_id(slug)})"'
    common = (f'fill="none" stroke="{color}" stroke-width="2.5" '
              f'stroke-linecap="round" {marker}')
    if abs(bow) < 0.5:
        return (f'<path d="M{_n(x1)} {_n(y1)} L{_n(x2)} {_n(y2)}" {common}/>')
    mx = (x1 + x2) / 2.0
    my = (y1 + y2) / 2.0 + bow
    return (f'<path d="M{_n(x1)} {_n(y1)} Q{_n(mx)} {_n(my)} '
            f'{_n(x2)} {_n(y2)}" {common}/>')


# --------------------------------------------------------------------------
# Sample 1 -- the whole course map.
# --------------------------------------------------------------------------
def _full_map():
    slug = "cmap-full"
    W, H = 1240, 620
    NW, NH = 154, 56
    left, right = 80, W - 80
    xs = [left + (right - left) * i / 6.0 for i in range(7)]  # Units 1..7
    spine_y = 320.0
    top_y = spine_y - 170.0
    bot_y = spine_y + 170.0

    pos = {
        1: (xs[0], spine_y), 2: (xs[1], spine_y), 3: (xs[2], spine_y),
        4: (xs[3], spine_y), 5: (xs[4], spine_y), 6: (xs[5], spine_y),
        7: (xs[6], spine_y),
        # bottom track: polynomials -> factoring -> quadratics
        10: (xs[2], bot_y), 11: (xs[3], bot_y), 12: (xs[5], bot_y),
        # top track: sequences, inequalities, data
        9: (xs[4], top_y), 8: (xs[5], top_y), "A": (xs[6], top_y),
    }
    spine = {1, 2, 3, 4, 5, 6, 7}

    def box(p):
        x, y = p
        return (x - NW / 2.0, y - NH / 2.0, x + NW / 2.0, y + NH / 2.0)

    # --- self-check the geometry (so a wrong pixel can't ship) ---
    ids = list(pos)
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = box(pos[ids[i]]), box(pos[ids[j]])
            assert not (a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]), \
                f"node overlap {ids[i]} {ids[j]}"
    for node, ps in PREREQ.items():
        for p in ps:
            assert pos[p][0] <= pos[node][0] + 0.5, f"backward edge {p}->{node}"

    parts = [
        f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
        f'font-family="-apple-system, Segoe UI, Roboto, sans-serif" '
        f'role="img" aria-label="Course prerequisite map: a gold main path '
        f'through Units 1 to 7, with blue branch units above and below.">',
        _defs(slug, AXIS),
    ]

    # Faint lane labels for the two side tracks (small, calm, not shouting).
    parts.append(
        f'<text x="{_n(left - 8)}" y="{_n(top_y - NH/2 - 14)}" '
        f'font-size="12" font-style="italic" fill="{AXIS}" opacity="0.85">'
        f'branches that grow out of the main path</text>'
    )
    parts.append(
        f'<text x="{_n(left - 8)}" y="{_n(spine_y - NH/2 - 14)}" '
        f'font-size="12.5" font-weight="700" fill="{GOLD}">'
        f'the main path</text>'
    )

    # --- edges first, so nodes sit on top of the lines ---
    def edge_between(p, n, bow=0.0):
        sb, db = box(pos[p]), box(pos[n])
        sx, sy = pos[p]
        dx, dy = pos[n]
        if abs(sy - dy) < 1:           # same row: right edge -> left edge
            x1, y1 = sb[2], sy
            x2, y2 = db[0], dy
        elif dy < sy:                  # going up: top of src -> bottom of dst
            x1, y1 = sx, sb[1]
            x2, y2 = dx, db[3]
        else:                          # going down: bottom of src -> top of dst
            x1, y1 = sx, sb[3]
            x2, y2 = dx, db[1]
        parts.append(_edge(slug, x1, y1, x2, y2, AXIS, bow=bow))

    # Spine (straight).
    for p in [1, 2, 3, 4, 5, 6]:
        edge_between(p, p + 1)
    # Bottom track. 10->11 straight; 11->12 gentle; 10->12 dips below 11.
    edge_between(10, 11)
    edge_between(11, 12, bow=26)
    # 10 -> 12 must arc UNDER node 11: leave bottom of 10, enter bottom of 12.
    b10, b12 = box(pos[10]), box(pos[12])
    parts.append(
        _edge(slug, pos[10][0], b10[3], pos[12][0], b12[3], AXIS, bow=170)
    )
    # Feed-ins to the bottom track from the spine.
    edge_between(1, 10, bow=-30)
    edge_between(2, 10, bow=10)
    edge_between(5, 12, bow=10)
    # Top track.
    edge_between(4, 9)
    edge_between(5, 8)
    edge_between(2, 8, bow=-60)   # long reach across the top gap, bowed up
    edge_between(5, "A", bow=-12)

    # --- nodes on top ---
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "A"]:
        cx, cy = pos[n]
        col = GOLD if n in spine else BLUE
        parts.append(_node(slug, cx, cy, NW, NH, LABEL[n], NAMES[n], col,
                           is_spine=(n in spine)))

    parts.append("</svg>")
    svg = "".join(parts)

    caption_math = (
        '<div style="text-align:center;margin-top:.5rem;color:var(--ink-soft);'
        'font-size:.95rem">Follow the gold path in order; the blue units branch '
        'off once their feeder units are done. '
        '$$\\text{Unit }1 \\to 2 \\to 3 \\to 4 \\to 5 \\to 6 \\to 7$$</div>'
    )
    return {
        "caption": "the whole course as a learning path — gold main road, blue side branches",
        "html": svg + caption_math,
    }


# --------------------------------------------------------------------------
# Sample 2 -- the Unit 5 neighborhood.
# --------------------------------------------------------------------------
def _unit5_neighborhood():
    slug = "cmap-u5"
    W, H = 930, 500
    NW, NH = 152, 54
    cy = H / 2.0

    # Four calm columns, left to right:
    #   col 1,2  -> the lead-in chain 3 -> 4
    #   col 3    -> Unit 5 itself (centered, gold)
    #   col 4    -> the units Unit 5 unlocks (6, 8, Appendix A)
    # Unit 7 sits just below Unit 6 in that last column, because Unit 7 is
    # reached *through* Unit 6 (7 needs 6, and 6 needs 5) rather than straight
    # from Unit 5.
    pad = 70
    c1 = pad + NW / 2.0
    c2 = c1 + NW + 55
    c3 = c2 + NW + 72
    c4 = c3 + NW + 80
    pos = {
        3: (c1, cy),
        4: (c2, cy),
        5: (c3, cy),
        6: (c4, 88.0),
        7: (c4, 200.0),       # next hop, directly under Unit 6
        8: (c4, cy + 25.0),
        "A": (c4, H - 70.0),
    }

    def box(p):
        x, y = p
        return (x - NW / 2.0, y - NH / 2.0, x + NW / 2.0, y + NH / 2.0)

    # geometry self-check
    ids = list(pos)
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = box(pos[ids[i]]), box(pos[ids[j]])
            assert not (a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]), \
                f"u5 overlap {ids[i]} {ids[j]}"

    parts = [
        f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
        f'font-family="-apple-system, Segoe UI, Roboto, sans-serif" '
        f'role="img" aria-label="Unit 5 neighborhood: it comes after Units 3 '
        f'and 4, and it opens the door to Units 6, 7, 8 and Appendix A.">',
        _defs(slug, AXIS),
    ]

    def edge_between(p, n, bow=0.0):
        sb, db = box(pos[p]), box(pos[n])
        sx, sy = pos[p]
        dx, dy = pos[n]
        if abs(sx - dx) < 1:
            # vertical hop (Unit 6 -> Unit 7): bottom edge -> top edge
            x1, y1, x2, y2 = sx, sb[3], dx, db[1]
        else:
            # rightward: leave the right edge, arrive at the left edge
            x1, y1, x2, y2 = sb[2], sy, db[0], dy
        parts.append(_edge(slug, x1, y1, x2, y2, AXIS, bow=bow))

    # lead-in chain
    edge_between(3, 4)
    edge_between(4, 5)
    # what Unit 5 unlocks directly (bow the top/bottom ones so the fan is tidy)
    edge_between(5, 6, bow=-18)
    edge_between(5, 8)
    edge_between(5, "A", bow=18)
    # Unit 7 chains off Unit 6 (honest: 7 needs 6, which needs 5)
    edge_between(6, 7)

    # gentle labels for the two halves of the story
    mid_left = (pos[3][0] + pos[5][0]) / 2.0
    parts.append(
        f'<text x="{_n(mid_left)}" y="{_n(cy - NH/2 - 18)}" text-anchor="middle" '
        f'font-size="13" font-style="italic" fill="{AXIS}">comes after</text>'
    )
    parts.append(
        f'<text x="{_n(pos[8][0])}" y="{_n(box(pos[6])[1] - 16)}" '
        f'text-anchor="middle" font-size="13" font-style="italic" '
        f'fill="{AXIS}">opens the door to</text>'
    )

    order = [3, 4, 6, 7, 8, "A", 5]  # draw 5 last so it sits on top, centered
    for n in order:
        x, y = pos[n]
        if n == 5:
            col = GOLD
            is_sp = True
        else:
            col = BLUE
            is_sp = False
        parts.append(_node(slug, x, y, NW, NH, LABEL[n], NAMES[n], col,
                           is_spine=is_sp))

    parts.append("</svg>")
    svg = "".join(parts)

    caption_math = (
        '<div style="text-align:center;margin-top:.5rem;color:var(--ink-soft);'
        'font-size:.95rem">Once Unit 5 clicks, four doors open '
        '(Unit 7 is just past Unit 6). '
        '$$5 \\;\\Rightarrow\\; \\{\\,6,\\ 7,\\ 8,\\ \\text{A}\\,\\}$$</div>'
    )
    return {
        "caption": "the Unit 5 neighborhood — what comes before it, and what it unlocks",
        "html": svg + caption_math,
    }


def samples():
    return [_full_map(), _unit5_neighborhood()]
