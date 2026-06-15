# -*- coding: utf-8 -*-
"""Worked-example-exact graphs.

Each graph is annotated to match a specific worked example. Every plotted
point, root, vertex, and intersection is verified with sympy at build time
(see _verify below) so a wrong pixel can never teach a falsehood.
"""

import sympy as _sp

TITLE = "Worked-example-exact graphs"
KIND = "deterministic-svg"
BLURB = "Graphs annotated to match a worked example, with every point checked by sympy."
LESSONS = ["5.3", "12.3", "7.1"]

# ---------------------------------------------------------------------------
# Palette (must match the book's dark-mode overrides exactly)
_BLUE = "#2980b9"
_VIOLET = "#8e44ad"
_RED = "#c0392b"
_GREEN = "#27ae60"
_AXIS = "#888"
_GOLD = "#a9740f"

# A shared world->pixel mapping keeps every sample on the same calm grid.
# World x in [XMIN, XMAX], y in [YMIN, YMAX] -> pixel box inside the padding.
_PAD_L, _PAD_R, _PAD_T, _PAD_B = 26, 18, 18, 26


class _Frame:
    """Maps math coordinates to SVG pixels for one fixed window."""

    def __init__(self, xmin, xmax, ymin, ymax, w=300, h=300):
        self.xmin, self.xmax = xmin, xmax
        self.ymin, self.ymax = ymin, ymax
        self.w, self.h = w, h
        self._ix0, self._ix1 = _PAD_L, w - _PAD_R
        self._iy0, self._iy1 = _PAD_T, h - _PAD_B  # iy0=top, iy1=bottom

    def px(self, x):
        t = (x - self.xmin) / (self.xmax - self.xmin)
        return self._ix0 + t * (self._ix1 - self._ix0)

    def py(self, y):
        t = (y - self.ymin) / (self.ymax - self.ymin)
        return self._iy1 - t * (self._iy1 - self._iy0)  # invert: +y is up

    # ---- reusable pieces ------------------------------------------------
    def grid_and_axes(self, slug, xstep=1, ystep=1):
        """Light grid lines on integers, plus bold x- and y-axes."""
        parts = []
        # vertical grid
        gx = _sp.ceiling(self.xmin / xstep) * xstep
        x = int(gx)
        while x <= self.xmax + 1e-9:
            X = round(self.px(x), 2)
            parts.append(
                f'<line x1="{X}" y1="{self._iy0}" x2="{X}" y2="{self._iy1}" '
                f'stroke="{_AXIS}" stroke-width="0.6" opacity="0.30"/>'
            )
            x += xstep
        # horizontal grid
        gy = _sp.ceiling(self.ymin / ystep) * ystep
        y = int(gy)
        while y <= self.ymax + 1e-9:
            Y = round(self.py(y), 2)
            parts.append(
                f'<line x1="{self._ix0}" y1="{Y}" x2="{self._ix1}" y2="{Y}" '
                f'stroke="{_AXIS}" stroke-width="0.6" opacity="0.30"/>'
            )
            y += ystep
        # axes (only if 0 is inside the window)
        if self.xmin <= 0 <= self.xmax:
            X0 = round(self.px(0), 2)
            parts.append(
                f'<line x1="{X0}" y1="{self._iy0}" x2="{X0}" y2="{self._iy1}" '
                f'stroke="{_AXIS}" stroke-width="1.4" stroke-linecap="round"/>'
            )
        if self.ymin <= 0 <= self.ymax:
            Y0 = round(self.py(0), 2)
            parts.append(
                f'<line x1="{self._ix0}" y1="{Y0}" x2="{self._ix1}" y2="{Y0}" '
                f'stroke="{_AXIS}" stroke-width="1.4" stroke-linecap="round"/>'
            )
        return "".join(parts)

    def point(self, x, y, color, r=4.5):
        cx, cy = round(self.px(x), 2), round(self.py(y), 2)
        # White halo first so dots read clearly where they cross a line.
        return (
            f'<circle cx="{cx}" cy="{cy}" r="{r + 2}" fill="var(--card)"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>'
        )

    def label(self, x, y, text, color, dx=0, dy=0, anchor="start", size=12.5):
        tx, ty = round(self.px(x) + dx, 2), round(self.py(y) + dy, 2)
        return (
            f'<text x="{tx}" y="{ty}" fill="{color}" font-size="{size}" '
            f'font-weight="600" text-anchor="{anchor}" '
            f'paint-order="stroke" stroke="var(--card)" stroke-width="3.2" '
            f'stroke-linejoin="round">{text}</text>'
        )


def _open(slug, w=300, h=300):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'font-family="ui-sans-serif, system-ui, sans-serif" '
        f'role="img" aria-labelledby="{slug}-t">'
    )


# ---------------------------------------------------------------------------
# (1) y = 2x - 1 with a slope triangle from (0,-1) to (1,1)
def _line_slope():
    slug = "wex-line"
    x = _sp.Symbol("x")
    f = 2 * x - 1
    # Endpoints of the visible segment + the slope-triangle corners.
    fr = _Frame(-3, 3, -4, 4)

    # Draw the line across the whole window.
    xL, xR = -3, 3
    yL, yR = float(f.subs(x, xL)), float(f.subs(x, xR))
    line = (
        f'<line x1="{round(fr.px(xL),2)}" y1="{round(fr.py(yL),2)}" '
        f'x2="{round(fr.px(xR),2)}" y2="{round(fr.py(yR),2)}" '
        f'stroke="{_BLUE}" stroke-width="2.5" stroke-linecap="round"/>'
    )

    # Slope triangle: (0,-1) -> (1,-1) [run] -> (1,1) [rise].
    p0 = (0, -1)
    pr = (1, -1)
    p1 = (1, 1)
    tri = (
        f'<path d="M {round(fr.px(*[p0[0]]),2)} {round(fr.py(p0[1]),2)} '
        f'L {round(fr.px(pr[0]),2)} {round(fr.py(pr[1]),2)} '
        f'L {round(fr.px(p1[0]),2)} {round(fr.py(p1[1]),2)}" '
        f'fill="none" stroke="{_RED}" stroke-width="2.5" '
        f'stroke-linecap="round" stroke-linejoin="round" '
        f'stroke-dasharray="1 5"/>'
    )

    # run label below the horizontal leg; rise label right of the vertical leg.
    run_lab = fr.label(0.5, -1, "run 1", _RED, dy=15, anchor="middle", size=12)
    rise_lab = fr.label(1, 0, "rise 2", _RED, dx=8, dy=4, anchor="start", size=12)

    pts = fr.point(*p0, _BLUE) + fr.point(*p1, _BLUE)
    lab0 = fr.label(0, -1, "(0, -1)", _BLUE, dx=-8, dy=16, anchor="end", size=11.5)
    lab1 = fr.label(1, 1, "(1, 1)", _BLUE, dx=8, dy=-7, anchor="start", size=11.5)

    svg = (
        _open(slug)
        + f'<title id="{slug}-t">The line y = 2x minus 1 with a slope triangle '
        f'showing rise 2 over run 1.</title>'
        + fr.grid_and_axes(slug)
        + line
        + tri
        + pts
        + run_lab + rise_lab + lab0 + lab1
        + "</svg>"
    )
    html = (
        '<div style="text-align:center">'
        + svg
        + '<div style="margin-top:.3rem">$$y = 2x - 1 '
        r'\quad\Rightarrow\quad \text{slope}=\dfrac{\text{rise}}{\text{run}}'
        r'=\dfrac{2}{1}=2$$</div>'
        + "</div>"
    )
    return html


# ---------------------------------------------------------------------------
# (2) y = x^2 - x - 6 with roots, vertex, factored caption
def _parabola():
    slug = "wex-parab"
    x = _sp.Symbol("x")
    f = x**2 - 5 * x + 6
    fr = _Frame(-1, 6, -2, 8)

    # Smooth polyline of the curve (deterministic sampling, fine step).
    pts_path = []
    n = 90
    for i in range(n + 1):
        xv = -1 + (6 - (-1)) * i / n
        yv = float(f.subs(x, xv))
        # clamp drawing to the window so it does not spill past the frame
        yv = max(min(yv, 8.0), -2.0)
        pts_path.append(f"{round(fr.px(xv),2)},{round(fr.py(yv),2)}")
    curve = (
        f'<polyline points="{" ".join(pts_path)}" fill="none" '
        f'stroke="{_VIOLET}" stroke-width="2.5" '
        f'stroke-linecap="round" stroke-linejoin="round"/>'
    )

    # Roots and vertex (sympy-exact values converted to float for pixels).
    roots = _sp.solve(f, x)            # [2, 3]
    vx = _sp.Rational(5, 2)
    vy = f.subs(x, vx)                 # -1/4 = -0.25

    rmark = "".join(fr.point(float(r), 0, _RED) for r in roots)
    vmark = fr.point(float(vx), float(vy), _GREEN)

    rlab1 = fr.label(2, 0, "(2, 0)", _RED, dx=-6, dy=-9, anchor="end", size=11.5)
    rlab2 = fr.label(3, 0, "(3, 0)", _RED, dx=6, dy=-9, anchor="start", size=11.5)
    vlab = fr.label(
        float(vx), float(vy), "vertex (2.5, -0.25)", _GREEN,
        dx=0, dy=18, anchor="middle", size=11.5,
    )

    svg = (
        _open(slug)
        + f'<title id="{slug}-t">The parabola y = x squared minus 5 x plus 6, '
        f'with roots at 2 and 3 and a vertex at 2.5, minus 0.25.</title>'
        + fr.grid_and_axes(slug)
        + curve
        + rmark + vmark
        + rlab1 + rlab2 + vlab
        + "</svg>"
    )
    html = (
        '<div style="text-align:center">'
        + svg
        + '<div style="margin-top:.3rem">$$x^2 - 5x + 6 = (x-2)(x-3)$$</div>'
        + "</div>"
    )
    return html


# ---------------------------------------------------------------------------
# (3) y = x + 1 and y = -x + 5 meeting at (2,3)
def _two_lines():
    slug = "wex-sys"
    x = _sp.Symbol("x")
    g1 = x + 1
    g2 = -x + 5
    fr = _Frame(-1, 6, -1, 7)

    def seg(expr, color, slugid):
        xL, xR = -1, 6
        yL, yR = float(expr.subs(x, xL)), float(expr.subs(x, xR))
        return (
            f'<line x1="{round(fr.px(xL),2)}" y1="{round(fr.py(yL),2)}" '
            f'x2="{round(fr.px(xR),2)}" y2="{round(fr.py(yR),2)}" '
            f'stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>'
        )

    sol = _sp.solve(_sp.Eq(g1, g2), x)[0]   # 2
    sy = g1.subs(x, sol)                     # 3

    line1 = seg(g1, _BLUE, slug)
    line2 = seg(g2, _VIOLET, slug)

    # Label each line near its right end, just above the stroke.
    l1lab = fr.label(6, float(g1.subs(x, 6)), "y = x + 1", _BLUE,
                     dx=-4, dy=-6, anchor="end", size=11.5)
    l2lab = fr.label(6, float(g2.subs(x, 6)), "y = -x + 5", _VIOLET,
                     dx=-4, dy=16, anchor="end", size=11.5)

    inter = fr.point(float(sol), float(sy), _GREEN, r=5)
    ilab = fr.label(float(sol), float(sy), "solution (2, 3)", _GREEN,
                    dx=9, dy=-7, anchor="start", size=12)

    svg = (
        _open(slug)
        + f'<title id="{slug}-t">Two lines, y = x + 1 and y = minus x + 5, '
        f'crossing at the solution point 2, 3.</title>'
        + fr.grid_and_axes(slug)
        + line1 + line2
        + inter
        + l1lab + l2lab + ilab
        + "</svg>"
    )
    html = (
        '<div style="text-align:center">'
        + svg
        + '<div style="margin-top:.3rem">'
        r'$$\begin{cases} y = x + 1 \\ y = -x + 5 \end{cases}'
        r'\;\Rightarrow\; (x, y) = (2, 3)$$</div>'
        + "</div>"
    )
    return html


# ---------------------------------------------------------------------------
def _verify():
    """Recompute every asserted coordinate; raise on any mismatch."""
    x = _sp.Symbol("x")
    # (1) line + slope triangle
    f1 = 2 * x - 1
    assert f1.subs(x, 0) == -1, "line through (0,-1)"
    assert f1.subs(x, 1) == 1, "line through (1,1)"
    assert (f1.subs(x, 1) - f1.subs(x, 0)) == 2, "rise == 2"
    # (2) parabola
    f2 = x**2 - 5 * x + 6
    assert sorted(_sp.solve(f2, x)) == [2, 3], "roots are 2, 3"
    assert _sp.factor(f2) == (x - 2) * (x - 3), "factors to (x-2)(x-3)"
    assert _sp.expand((x - 2) * (x - 3)) == f2, "expansion matches"
    vy = f2.subs(x, _sp.Rational(5, 2))
    assert vy == _sp.Rational(-1, 4), "vertex y == -0.25"
    assert float(vy) == -0.25
    # (3) intersection
    s = _sp.solve(_sp.Eq(x + 1, -x + 5), x)[0]
    assert s == 2 and (x + 1).subs(x, s) == 3 and (-x + 5).subs(x, s) == 3
    return True


_verify()  # fail loudly at import time if any math is wrong


def samples():
    return [
        {
            "caption": "y = 2x - 1 with a slope triangle: rise 2 over run 1",
            "html": _line_slope(),
        },
        {
            "caption": "y = x^2 - 5x + 6: roots (2,0) and (3,0), vertex (2.5, -0.25)",
            "html": _parabola(),
        },
        {
            "caption": "y = x + 1 and y = -x + 5 meet at the solution (2, 3)",
            "html": _two_lines(),
        },
    ]
