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
        'font-size:.95rem">Follow the gold path in order &mdash; Unit 1 &rarr; '
        '2 &rarr; 3 &rarr; 4 &rarr; 5 &rarr; 6 &rarr; 7 &mdash; and the blue '
        'units branch off once their feeder units are done.</div>'
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
    cx = W / 2.0
    cy = H / 2.0

    # A "hub" picture: Unit 5 sits in the dead center (gold). Its
    # prerequisites (Units 3 and 4) stack on the LEFT with arrows pointing IN;
    # the units it unlocks (6, 7, 8, Appendix A) fan out on the RIGHT with
    # arrows pointing OUT. No set-notation text -- the geometry tells the story.
    left_x = NW / 2.0 + 60          # column for the "comes before" nodes
    right_x = W - NW / 2.0 - 60     # column for the "unlocks" nodes
    # vertical slots so the side cards never collide with the centered hub
    pre_ys = [cy - 95.0, cy + 95.0]            # Units 3, 4
    post_ys = [86.0, cy - 36.0, cy + 36.0, H - 86.0]  # Units 6, 7, 8, A

    pos = {
        5: (cx, cy),
        3: (left_x, pre_ys[0]),
        4: (left_x, pre_ys[1]),
        6: (right_x, post_ys[0]),
        7: (right_x, post_ys[1]),
        8: (right_x, post_ys[2]),
        "A": (right_x, post_ys[3]),
    }

    def box(p):
        x, y = p
        return (x - NW / 2.0, y - NH / 2.0, x + NW / 2.0, y + NH / 2.0)

    # geometry self-check: no two cards overlap
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

    hub = box(pos[5])

    def edge_in(p):
        """Arrow from a prerequisite (left) pointing IN to the hub's left edge."""
        sb = box(pos[p])
        sx, sy = pos[p]
        x1, y1 = sb[2], sy                 # leave the right edge of the prereq
        x2, y2 = hub[0], cy                # arrive at the hub's left edge
        parts.append(_edge(slug, x1, y1, x2, y2, AXIS))

    def edge_out(n):
        """Arrow from the hub's right edge pointing OUT to an unlocked unit."""
        db = box(pos[n])
        dx, dy = pos[n]
        x1, y1 = hub[2], cy                # leave the hub's right edge
        x2, y2 = db[0], dy                 # arrive at the left edge of the unit
        parts.append(_edge(slug, x1, y1, x2, y2, AXIS))

    # prerequisites point IN; unlocks point OUT
    for p in (3, 4):
        edge_in(p)
    for n in (6, 7, 8, "A"):
        edge_out(n)

    # gentle labels for the two halves of the story
    parts.append(
        f'<text x="{_n(left_x)}" y="{_n(box(pos[3])[1] - 16)}" '
        f'text-anchor="middle" font-size="13" font-style="italic" '
        f'fill="{AXIS}">comes after</text>'
    )
    parts.append(
        f'<text x="{_n(right_x)}" y="{_n(box(pos[6])[1] - 16)}" '
        f'text-anchor="middle" font-size="13" font-style="italic" '
        f'fill="{AXIS}">opens the door to</text>'
    )

    order = [3, 4, 6, 7, 8, "A", 5]  # draw 5 last so the hub sits on top
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

    caption = (
        '<div style="text-align:center;margin-top:.5rem;color:var(--ink-soft);'
        'font-size:.95rem">Units 3 and 4 lead into Unit 5; once it clicks, four '
        'more doors open &mdash; Units 6, 7, 8 and Appendix A.</div>'
    )
    return {
        "caption": "the Unit 5 neighborhood — what comes before it, and what it unlocks",
        "html": svg + caption,
    }


def samples():
    return [_full_map(), _unit5_neighborhood()]
