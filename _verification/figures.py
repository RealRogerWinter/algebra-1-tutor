"""Programmatic figure library for the algebra-1-tutor skill (build tooling, NOT shipped as code;
the *generated SVGs* are shipped/bundled).

Every figure is computed SVG from coordinate data backed by a reproducible spec, then sympy-accuracy
-checked, then written to algebra-1-tutor/figures/<code>.svg and bundled into the skill. The tutor
reads the local SVG and re-emits it as an Artifact (no runtime fetch; math exact). This supersedes
the runtime "compute coordinates and eyeball" approach.

CLI:
  python _verification/figures.py            # (re)generate all SVGs
  python _verification/figures.py --check    # verify accuracy + staleness; write nothing
"""
import argparse, math, os, sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
FIG_DIR = os.path.join(REPO_ROOT, "algebra-1-tutor", "figures")

# --- coordinate mapping -------------------------------------------------------------------------
SIZE, PAD = 240, 18

def _mapper(xmin, xmax, ymin, ymax, size=SIZE, pad=PAD):
    sx = (size - 2 * pad) / (xmax - xmin)
    sy = (size - 2 * pad) / (ymax - ymin)
    def M(x, y):
        return (round(pad + (float(x) - xmin) * sx, 2), round(size - pad - (float(y) - ymin) * sy, 2))
    return M

GRID_STROKE = "#e8e8e8"   # light unit-grid lines (dark-mode override lives in build_textbook CSS)

def _grid(M, xmin, xmax, ymin, ymax):
    """Light gridlines at every integer, drawn with the SAME mapper as the axes and the plotted
    points, so a point always lands exactly on a grid crossing. The x=0 / y=0 lines are left to
    the bolder axes drawn on top."""
    parts = []
    x = math.ceil(xmin)
    while x <= xmax:
        if x != 0:
            gx, gy1 = M(x, ymax); _, gy2 = M(x, ymin)
            parts.append(f'<line x1="{gx}" y1="{gy1}" x2="{gx}" y2="{gy2}" stroke="{GRID_STROKE}" stroke-width="1"/>')
        x += 1
    y = math.ceil(ymin)
    while y <= ymax:
        if y != 0:
            gx1, gy = M(xmin, y); gx2, _ = M(xmax, y)
            parts.append(f'<line x1="{gx1}" y1="{gy}" x2="{gx2}" y2="{gy}" stroke="{GRID_STROKE}" stroke-width="1"/>')
        y += 1
    return "\n  ".join(parts)

def _axes(M, xmin, xmax, ymin, ymax):
    parts = [_grid(M, xmin, xmax, ymin, ymax)]
    if ymin <= 0 <= ymax:                          # x-axis
        x1, y0 = M(xmin, 0); x2, _ = M(xmax, 0)
        parts.append(f'<line x1="{x1}" y1="{y0}" x2="{x2}" y2="{y0}" stroke="#888"/>')
        parts.append(f'<text x="{x2-6}" y="{y0-4}" font-size="10" fill="#888">x</text>')
    if xmin <= 0 <= xmax:                           # y-axis
        x0, yy1 = M(0, ymax); _, yy2 = M(0, ymin)
        parts.append(f'<line x1="{x0}" y1="{yy1}" x2="{x0}" y2="{yy2}" stroke="#888"/>')
        parts.append(f'<text x="{x0+4}" y="{yy1+8}" font-size="10" fill="#888">y</text>')
    return "\n  ".join(p for p in parts if p)

def _svg(body, size=SIZE):
    return (f'<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg" '
            f'font-family="sans-serif">\n  {body}\n</svg>\n')

def _dot(M, x, y, color="#c0392b", r=3.5):
    sx, sy = M(x, y)
    return f'<circle cx="{sx}" cy="{sy}" r="{r}" fill="{color}"/>'

def _label(M, x, y, text, color="#c0392b", dx=5, dy=-6):
    sx, sy = M(x, y)
    return f'<text x="{sx+dx}" y="{sy+dy}" font-size="10" fill="{color}">{text}</text>'

# --- renderers ----------------------------------------------------------------------------------
def _r_line(s):
    m, b = sp.Rational(str(s["m"])), sp.Rational(str(s["b"]))
    xmin, xmax = s["xwindow"]; ymin, ymax = s["ywindow"]
    M = _mapper(xmin, xmax, ymin, ymax)
    y1 = float(m * xmin + b); y2 = float(m * xmax + b)
    (px1, py1), (px2, py2) = M(xmin, y1), M(xmax, y2)
    out = [_axes(M, xmin, xmax, ymin, ymax),
           f'<line x1="{px1}" y1="{py1}" x2="{px2}" y2="{py2}" stroke="#2980b9" stroke-width="2.5"/>']
    for (x, y, lab) in s.get("marks", []):
        out.append(_dot(M, x, y)); out.append(_label(M, x, y, lab))
    out.append(_label(M, *s.get("eqpos", (xmax * 0.4, m * (xmax * 0.4) + b)), s["caption"], "#2980b9", 4, -4))
    return _svg("\n  ".join(out))

def _r_parabola(s):
    a, b, c = (sp.Rational(str(s[k])) for k in "abc")
    xmin, xmax = s["xwindow"]; ymin, ymax = s["ywindow"]
    M = _mapper(xmin, xmax, ymin, ymax)
    pts, x = [], xmin
    while x <= xmax + 1e-9:
        y = float(a * x * x + b * x + c)
        if ymin - 1 <= y <= ymax + 1:
            sx, sy = M(x, y); pts.append(f"{sx},{sy}")
        x += (xmax - xmin) / 80.0
    out = [_axes(M, xmin, xmax, ymin, ymax),
           f'<polyline fill="none" stroke="#8e44ad" stroke-width="2.5" points="{" ".join(pts)}"/>']
    for (x, y, lab) in s.get("marks", []):
        out.append(_dot(M, x, y)); out.append(_label(M, x, y, lab))
    return _svg("\n  ".join(out))

def _r_vgraph(s):
    sh = sp.Rational(str(s.get("shift", 0)))
    xmin, xmax = s["xwindow"]; ymin, ymax = s["ywindow"]
    M = _mapper(xmin, xmax, ymin, ymax)
    pts = [M(x, abs(x) + float(sh)) for x in (xmin, 0, xmax)]
    poly = " ".join(f"{p[0]},{p[1]}" for p in pts)
    out = [_axes(M, xmin, xmax, ymin, ymax),
           f'<polyline fill="none" stroke="#8e44ad" stroke-width="2.5" points="{poly}"/>']
    for (x, y, lab) in s.get("marks", []):
        out.append(_dot(M, x, y)); out.append(_label(M, x, y, lab))
    return _svg("\n  ".join(out))

def _r_inequality(s):
    m, b = sp.Rational(str(s["m"])), sp.Rational(str(s["b"]))
    op = s["op"]; xmin, xmax = s["xwindow"]; ymin, ymax = s["ywindow"]
    M = _mapper(xmin, xmax, ymin, ymax)
    y1 = float(m * xmin + b); y2 = float(m * xmax + b)
    dash = "" if op in (">=", "<=") else ' stroke-dasharray="5 3"'
    # shade toward +inf or -inf in y depending on op
    up = op in (">", ">=")
    yfill = ymax if up else ymin
    (ax1, ay1), (ax2, ay2) = M(xmin, y1), M(xmax, y2)
    (cx1, cyf), (cx2, _) = M(xmin, yfill), M(xmax, yfill)
    poly = f"{ax1},{ay1} {ax2},{ay2} {cx2},{cyf} {cx1},{cyf}"
    out = [f'<polygon points="{poly}" fill="#2980b9" fill-opacity="0.15"/>',
           _axes(M, xmin, xmax, ymin, ymax),
           f'<line x1="{ax1}" y1="{ay1}" x2="{ax2}" y2="{ay2}" stroke="#2980b9" stroke-width="2.5"{dash}/>']
    tp = s.get("test_point")
    if tp:
        out.append(_dot(M, tp[0], tp[1], "#27ae60"))
        out.append(_label(M, tp[0], tp[1], f"test {tuple(tp)}", "#27ae60"))
    return _svg("\n  ".join(out))

def _r_scatter(s):
    pts = s["points"]; fm, fb = sp.Rational(str(s["fit"]["m"])), sp.Rational(str(s["fit"]["b"]))
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    xmin, xmax = min(xs + [0]), max(xs); ymin, ymax = min(ys + [0]), max(ys)
    xmin, xmax = xmin - 1, xmax + 1; ymin, ymax = ymin - 1, ymax + 1
    M = _mapper(xmin, xmax, ymin, ymax)
    out = [_axes(M, xmin, xmax, ymin, ymax)]
    y1 = float(fm * xmin + fb); y2 = float(fm * xmax + fb)
    (lx1, ly1), (lx2, ly2) = M(xmin, y1), M(xmax, y2)
    out.append(f'<line x1="{lx1}" y1="{ly1}" x2="{lx2}" y2="{ly2}" stroke="#c0392b" stroke-width="2"/>')
    for (x, y) in pts:
        out.append(_dot(M, x, y, "#2980b9", 3))
    return _svg("\n  ".join(out))

def _r_number_line(s):
    lo, hi = s["min"], s["max"]
    M = lambda v: round(20 + (v - lo) * (280.0 / (hi - lo)), 2)
    out = ['<line x1="14" y1="30" x2="306" y2="30" stroke="#333" stroke-width="2"/>']
    for t in s["ticks"]:
        x = M(t)
        out.append(f'<line x1="{x}" y1="25" x2="{x}" y2="35" stroke="#333"/>')
        out.append(f'<text x="{x}" y="50" font-size="10" text-anchor="middle">{t}</text>')
    for seg in s.get("segments", []):
        x1, x2 = M(seg["from"]), M(seg["to"])
        out.append(f'<line x1="{x1}" y1="30" x2="{x2}" y2="30" stroke="#c0392b" stroke-width="4"/>')
    for p in s.get("points", []):
        x = M(p["x"]); fill = "#c0392b" if p.get("filled", True) else "white"
        out.append(f'<circle cx="{x}" cy="30" r="5" fill="{fill}" stroke="#c0392b" stroke-width="2"/>')
        if p.get("label"):
            out.append(f'<text x="{x}" y="18" font-size="10" text-anchor="middle" fill="#c0392b">{p["label"]}</text>')
    return f'<svg viewBox="0 0 320 60" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">\n  ' + "\n  ".join(out) + "\n</svg>\n"

def _r_plane(s):
    """Four-quadrant coordinate plane with quadrant sign labels and a plotted point (dashed guides
    to each axis). 5.1: the plane itself is the lesson."""
    xmin, xmax = s["xwindow"]; ymin, ymax = s["ywindow"]
    M = _mapper(xmin, xmax, ymin, ymax)
    out = [_axes(M, xmin, xmax, ymin, ymax)]
    for (qx, qy, lab) in s.get("quadrants", []):
        sx, sy = M(qx, qy)
        out.append(f'<text x="{sx}" y="{sy}" font-size="9" fill="#888" text-anchor="middle">{lab}</text>')
    for (x, y, lab) in s.get("marks", []):
        px, py = M(x, y); ax0, _ = M(0, y); _, ay0 = M(x, 0)
        out.append(f'<line x1="{ax0}" y1="{py}" x2="{px}" y2="{py}" stroke="#c0392b" stroke-width="1" stroke-dasharray="3 3"/>')
        out.append(f'<line x1="{px}" y1="{ay0}" x2="{px}" y2="{py}" stroke="#c0392b" stroke-width="1" stroke-dasharray="3 3"/>')
        out.append(_dot(M, x, y)); out.append(_label(M, x, y, lab))
    return _svg("\n  ".join(out))

def _r_lines2(s):
    """Two lines on one axis, with their intersection (the solution of the system) marked. 7.1."""
    xmin, xmax = s["xwindow"]; ymin, ymax = s["ywindow"]
    M = _mapper(xmin, xmax, ymin, ymax)
    out = [_axes(M, xmin, xmax, ymin, ymax)]
    cols = ["#2980b9", "#8e44ad"]
    for i, ln in enumerate(s["lines"]):
        m, b = sp.Rational(str(ln["m"])), sp.Rational(str(ln["b"]))
        (x1, y1), (x2, y2) = M(xmin, float(m * xmin + b)), M(xmax, float(m * xmax + b))
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{cols[i % len(cols)]}" stroke-width="2.5"/>')
    ix, iy = s["intersect"]
    out.append(_dot(M, ix, iy)); out.append(_label(M, ix, iy, f"({ix}, {iy})"))
    return _svg("\n  ".join(out))

def _r_growth(s):
    """A straight line vs a bending exponential curve on one axis (same start). 9.2: linear vs
    exponential is the unit's punchline; 'straight vs bending' must be seen."""
    xmin, xmax = s["xwindow"]; ymin, ymax = s["ywindow"]
    M = _mapper(xmin, xmax, ymin, ymax)
    out = [_axes(M, xmin, xmax, ymin, ymax)]
    m, b = sp.Rational(str(s["line"]["m"])), sp.Rational(str(s["line"]["b"]))
    (lx1, ly1), (lx2, ly2) = M(xmin, float(m * xmin + b)), M(xmax, float(m * xmax + b))
    out.append(f'<line x1="{lx1}" y1="{ly1}" x2="{lx2}" y2="{ly2}" stroke="#2980b9" stroke-width="2.5"/>')
    base = float(sp.Rational(str(s["exp"]["base"])))
    pts, x = [], xmin
    while x <= xmax + 1e-9:
        y = base ** x
        if ymin - 1 <= y <= ymax + 1:
            sx, sy = M(x, y); pts.append(f"{sx},{sy}")
        x += (xmax - xmin) / 80.0
    out.append(f'<polyline fill="none" stroke="#8e44ad" stroke-width="2.5" points="{" ".join(pts)}"/>')
    for (x, y, lab) in s.get("marks", []):
        out.append(_dot(M, x, y)); out.append(_label(M, x, y, lab))
    return _svg("\n  ".join(out))

def _r_factor_array(s):
    """Each factor pair of a number drawn as a rectangle of unit squares (rows x cols), so the
    rectangle's area IS the number and its two side lengths are a factor pair. 1.4: 'factor' at the
    word's first use. Integer coordinates only, so the SVG is byte-deterministic."""
    num = int(s["num"])
    pairs = [(int(r), int(c)) for (r, c) in s["pairs"]]
    cell, pitch, padx, top, gap_lbl, blockgap = 12, 15, 12, 18, 7, 14
    out, y = [], top
    for (rows, cols) in pairs:
        out.append(f'<text x="{padx}" y="{y}" font-size="12" fill="#2980b9">{rows} × {cols} = {num}</text>')
        gy = y + gap_lbl
        for r in range(rows):
            for c in range(cols):
                out.append(f'<rect x="{padx + c * pitch}" y="{gy + r * pitch}" width="{cell}" '
                           f'height="{cell}" rx="2" fill="#d6eaf8" stroke="#2980b9" stroke-width="1.5"/>')
        y = gy + rows * pitch + blockgap
    return (f'<svg viewBox="0 0 240 {y}" xmlns="http://www.w3.org/2000/svg" '
            f'font-family="sans-serif">\n  ' + "\n  ".join(out) + "\n</svg>\n")

def _r_vlt(s):
    """Vertical-line-test figure: a graph (line / uparabola / rparabola / circle / vline) with a
    dashed red vertical 'test line' at x = s['test_x'], and the intersection(s) marked. One hit ->
    a function; two hits -> not. Circle uses a square window so it renders round."""
    xmin, xmax = s["xwindow"]; ymin, ymax = s["ywindow"]
    M = _mapper(xmin, xmax, ymin, ymax)
    out = [_axes(M, xmin, xmax, ymin, ymax)]
    shape = s["shape"]; col = "#2980b9"
    if shape == "line":
        m, b = sp.Rational(str(s["m"])), sp.Rational(str(s["b"]))
        (x1, y1), (x2, y2) = M(xmin, float(m * xmin + b)), M(xmax, float(m * xmax + b))
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="2.5"/>')
    elif shape == "uparabola":
        a, b, c = (sp.Rational(str(s[k])) for k in "abc")
        pts, x = [], xmin
        while x <= xmax + 1e-9:
            y = float(a * x * x + b * x + c)
            if ymin - 1 <= y <= ymax + 1:
                px, py = M(x, y); pts.append(f"{px},{py}")
            x += (xmax - xmin) / 80.0
        out.append(f'<polyline fill="none" stroke="{col}" stroke-width="2.5" points="{" ".join(pts)}"/>')
    elif shape == "rparabola":
        a = sp.Rational(str(s["a"]))
        pts, y = [], ymin
        while y <= ymax + 1e-9:
            x = float(a * y * y)
            if xmin - 1 <= x <= xmax + 1:
                px, py = M(x, y); pts.append(f"{px},{py}")
            y += (ymax - ymin) / 80.0
        out.append(f'<polyline fill="none" stroke="{col}" stroke-width="2.5" points="{" ".join(pts)}"/>')
    elif shape == "circle":
        r = float(sp.Rational(str(s["r"]))); cx, cy = s.get("cx", 0), s.get("cy", 0)
        mcx, mcy = M(cx, cy)
        rpx = round(r * (SIZE - 2 * PAD) / (xmax - xmin), 2)
        out.append(f'<circle cx="{mcx}" cy="{mcy}" r="{rpx}" fill="none" stroke="{col}" stroke-width="2.5"/>')
    elif shape == "vline":
        vx, vy1 = M(s["k"], ymax); _, vy2 = M(s["k"], ymin)
        out.append(f'<line x1="{vx}" y1="{vy1}" x2="{vx}" y2="{vy2}" stroke="{col}" stroke-width="2.5"/>')
    if shape != "vline":
        px, ty1 = M(s["test_x"], ymax); _, ty2 = M(s["test_x"], ymin)
        out.append(f'<line x1="{px}" y1="{ty1}" x2="{px}" y2="{ty2}" stroke="#c0392b" stroke-width="1.5" stroke-dasharray="5 3"/>')
    for (mx, my, lab) in s.get("marks", []):
        out.append(_dot(M, mx, my))
        if lab:
            out.append(_label(M, mx, my, lab))
    return _svg("\n  ".join(out))

RENDERERS = {"line": _r_line, "parabola": _r_parabola, "vgraph": _r_vgraph,
             "inequality_region": _r_inequality, "scatter": _r_scatter, "number_line": _r_number_line,
             "plane": _r_plane, "lines2": _r_lines2, "growth": _r_growth, "factor_array": _r_factor_array,
             "vlt": _r_vlt}

def render(spec):
    return RENDERERS[spec["type"]](spec)

# --- accuracy (sympy): labeled features must satisfy the equation -------------------------------
def accuracy_issues(spec):
    t = spec["type"]; code = spec["code"]; iss = []
    x = sp.Symbol("x")
    if t == "line":
        m, b = sp.Rational(str(spec["m"])), sp.Rational(str(spec["b"]))
        for (mx, my, lab) in spec.get("marks", []):
            if sp.nsimplify(my) != m * sp.nsimplify(mx) + b:
                iss.append(f"{code}: mark ({mx},{my}) '{lab}' not on y={m}x+{b}")
    elif t == "parabola":
        a, b, c = (sp.Rational(str(spec[k])) for k in "abc")
        vx, vy = -b / (2 * a), c - b * b / (4 * a)
        for (mx, my, lab) in spec.get("marks", []):
            mxs, mys = sp.nsimplify(mx), sp.nsimplify(my)
            on_curve = (mys == a * mxs * mxs + b * mxs + c)
            is_vertex = "vertex" in lab.lower() and (mxs, mys) == (vx, vy)
            if not (on_curve or is_vertex):
                iss.append(f"{code}: mark ({mx},{my}) '{lab}' not on y={a}x^2+{b}x+{c} (vertex={vx},{vy})")
        for r in spec.get("roots", []):
            if sp.nsimplify(a * sp.nsimplify(r) ** 2 + b * sp.nsimplify(r) + c) != 0:
                iss.append(f"{code}: stated root {r} does not satisfy the equation")
    elif t == "vgraph":
        sh = sp.Rational(str(spec.get("shift", 0)))
        for (mx, my, lab) in spec.get("marks", []):
            if sp.nsimplify(my) != abs(sp.nsimplify(mx)) + sh:
                iss.append(f"{code}: mark ({mx},{my}) '{lab}' not on y=|x|+{sh}")
    elif t == "inequality_region":
        m, b = sp.Rational(str(spec["m"])), sp.Rational(str(spec["b"]))
        op = spec["op"]; tp = spec.get("test_point")
        if tp:
            lhs, rhs = sp.nsimplify(tp[1]), m * sp.nsimplify(tp[0]) + b
            sat = (lhs > rhs) if op == ">" else (lhs >= rhs) if op == ">=" else (lhs < rhs) if op == "<" else (lhs <= rhs)
            # the renderer shades the satisfying side by construction (up iff op in >,>=); the
            # marked test point must lie in that shaded/satisfying region, or the figure misleads.
            if not bool(sat):
                iss.append(f"{code}: test point {tp} not in the shaded (satisfying) region for y {op} {m}x+{b}")
    elif t == "scatter":
        pts = spec["points"]
        if len(pts) < 3:
            iss.append(f"{code}: scatter needs >=3 points")
        else:
            # the stated best-fit line must roughly match the least-squares fit of the points,
            # so an absurd fit (wrong sign / far-off slope or intercept) is caught.
            fm, fb = sp.Rational(str(spec["fit"]["m"])), sp.Rational(str(spec["fit"]["b"]))
            n = len(pts)
            xs = [sp.Rational(str(p[0])) for p in pts]; ys = [sp.Rational(str(p[1])) for p in pts]
            xbar, ybar = sum(xs) / n, sum(ys) / n
            sxx = sum((x - xbar) ** 2 for x in xs)
            sxy = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))
            if sxx == 0:
                iss.append(f"{code}: scatter x-values are all equal (no fit)")
            else:
                ms = sxy / sxx; bs = ybar - ms * xbar
                if ms != 0 and (fm == 0 or fm * ms < 0 or not (abs(ms) / 2 <= abs(fm) <= 2 * abs(ms))):
                    iss.append(f"{code}: fit slope {fm} far from least-squares {ms}")
                if abs(fb - bs) > sp.Rational(3, 2):
                    iss.append(f"{code}: fit intercept {fb} far from least-squares {bs}")
    elif t == "number_line":
        for p in spec.get("points", []):
            if not (spec["min"] <= p["x"] <= spec["max"]):
                iss.append(f"{code}: point {p['x']} out of range [{spec['min']},{spec['max']}]")
    elif t == "plane":
        xw, yw = spec["xwindow"], spec["ywindow"]
        for (mx, my, lab) in spec.get("marks", []):
            if not (xw[0] <= mx <= xw[1] and yw[0] <= my <= yw[1]):
                iss.append(f"{code}: plotted point ({mx},{my}) outside the window")
    elif t == "lines2":
        ix, iy = sp.nsimplify(spec["intersect"][0]), sp.nsimplify(spec["intersect"][1])
        for ln in spec["lines"]:
            m, b = sp.Rational(str(ln["m"])), sp.Rational(str(ln["b"]))
            if iy != m * ix + b:
                iss.append(f"{code}: stated intersection {spec['intersect']} not on y={m}x+{b}")
    elif t == "growth":
        m, b = sp.Rational(str(spec["line"]["m"])), sp.Rational(str(spec["line"]["b"]))
        base = sp.Rational(str(spec["exp"]["base"]))
        for (mx, my, lab) in spec.get("marks", []):
            mxs, mys = sp.nsimplify(mx), sp.nsimplify(my)
            if not (mys == m * mxs + b or mys == base ** mxs):
                iss.append(f"{code}: mark ({mx},{my}) '{lab}' on neither y={m}x+{b} nor y={base}^x")
    elif t == "factor_array":
        num = spec["num"]
        pairs = [(int(a), int(b)) for (a, b) in spec["pairs"]]
        for (a, b) in pairs:
            if a * b != num:
                iss.append(f"{code}: pair {a}x{b} does not multiply to {num}")
        # the drawn pairs must be EXACTLY the complete set of unordered factor pairs, so the
        # figure can never imply a number has fewer (or wrong) factors than it does.
        complete = sorted({(d, num // d) for d in range(1, num + 1) if num % d == 0 and d <= num // d})
        given = sorted((min(a, b), max(a, b)) for (a, b) in pairs)
        if given != complete:
            iss.append(f"{code}: pairs {given} are not the complete factor pairs {complete} of {num}")
    elif t == "vlt":
        shape = spec["shape"]
        for (mx, my, lab) in spec.get("marks", []):
            mxs, mys = sp.nsimplify(mx), sp.nsimplify(my)
            if shape == "line":
                on = mys == sp.Rational(str(spec["m"])) * mxs + sp.Rational(str(spec["b"]))
            elif shape == "uparabola":
                a, b, c = (sp.Rational(str(spec[k])) for k in "abc"); on = mys == a * mxs * mxs + b * mxs + c
            elif shape == "rparabola":
                on = mxs == sp.Rational(str(spec["a"])) * mys * mys
            elif shape == "circle":
                r = sp.Rational(str(spec["r"]))
                cx, cy = sp.nsimplify(spec.get("cx", 0)), sp.nsimplify(spec.get("cy", 0))
                on = (mxs - cx) ** 2 + (mys - cy) ** 2 == r ** 2
            elif shape == "vline":
                on = mxs == sp.nsimplify(spec["k"])
            else:
                on = False
            if not on:
                iss.append(f"{code}: VLT mark ({mx},{my}) '{lab}' not on the {shape}")
            if shape != "vline" and mxs != sp.nsimplify(spec["test_x"]):
                iss.append(f"{code}: VLT mark ({mx},{my}) not on the test line x={spec['test_x']}")
    return iss

# --- registry -----------------------------------------------------------------------------------
# Each spec: code (= f-anchor in the unit), lesson, type, params, caption. Math drawn from the
# lesson's worked example; labeled features are sympy-verified by accuracy_issues().
FIGURES = [
    # Unit 1 — number system / distance
    {"code": "1.2.f1", "lesson": "1.2", "type": "number_line", "min": -3, "max": 5,
     "ticks": [-3, -2, -1, 0, 1, 2, 3, 4, 5],
     "points": [{"x": 0.75, "label": "3/4"}, {"x": -2.5, "label": "-2.5"}],
     "caption": "number line"},
    # Unit 4 — multiple representations: a line and a parabola
    {"code": "4.4.f1", "lesson": "4.4", "type": "line", "m": 2, "b": 1,
     "xwindow": [-3, 3], "ywindow": [-5, 7], "marks": [(0, 1, "(0,1)")], "caption": "y = 2x + 1"},
    {"code": "4.4.f2", "lesson": "4.4", "type": "parabola", "a": 1, "b": 0, "c": 0,
     "xwindow": [-3, 3], "ywindow": [-1, 9], "marks": [(0, 0, "vertex (0,0)"), (2, 4, "(2,4)")],
     "roots": [0], "caption": "y = x^2"},
    # Unit 5 — linear functions & graphs
    {"code": "5.2.f1", "lesson": "5.2", "type": "line", "m": 2, "b": -1,
     "xwindow": [-3, 4], "ywindow": [-7, 7], "marks": [(0, -1, "(0,-1)"), (3, 5, "(3,5)")],
     "caption": "y = 2x - 1"},
    {"code": "5.3.f1", "lesson": "5.3", "type": "line", "m": sp.Rational(2, 3), "b": 1,
     "xwindow": [-3, 6], "ywindow": [-2, 6], "marks": [(0, 1, "(0,1)"), (3, 3, "(3,3)")],
     "caption": "slope 2/3"},
    {"code": "5.4.f1", "lesson": "5.4", "type": "line", "m": 3, "b": -2,
     "xwindow": [-2, 4], "ywindow": [-8, 8], "marks": [(0, -2, "y-int (0,-2)")], "caption": "y = 3x - 2"},
    {"code": "5.6.f1", "lesson": "5.6", "type": "line", "m": -2, "b": 4,
     "xwindow": [-1, 4], "ywindow": [-2, 6], "marks": [(0, 4, "(0,4)"), (2, 0, "x-int (2,0)")],
     "caption": "2x + y = 4"},
    # Unit 8 — inequalities: a number line, the V-graph, a 2-D region
    {"code": "8.1.f1", "lesson": "8.1", "type": "number_line", "min": -1, "max": 5,
     "ticks": [-1, 0, 1, 2, 3, 4, 5], "points": [{"x": 2, "label": "x > 2", "filled": False}],
     "segments": [{"from": 2, "to": 5}], "caption": "x > 2"},
    {"code": "8.3.f1", "lesson": "8.3", "type": "vgraph", "shift": 0, "xwindow": [-4, 4],
     "ywindow": [-1, 5], "marks": [(0, 0, "vertex (0,0)"), (3, 3, "(3,3)")], "caption": "y = |x|"},
    {"code": "8.4.f1", "lesson": "8.4", "type": "inequality_region", "m": 1, "b": 1, "op": ">",
     "xwindow": [-3, 3], "ywindow": [-3, 5], "test_point": [0, 3], "caption": "y > x + 1"},
    # Unit 12 — quadratics: the capstone parabola
    {"code": "12.6.f1", "lesson": "12.6", "type": "parabola", "a": 1, "b": 0, "c": -4,
     "xwindow": [-3, 3], "ywindow": [-5, 6], "marks": [(-2, 0, "(-2,0)"), (2, 0, "(2,0)"),
     (0, -4, "vertex (0,-4)")], "roots": [-2, 2], "caption": "y = x^2 - 4"},
    # Appendix A — scatter + line of best fit
    {"code": "A.2.f1", "lesson": "A.2", "type": "scatter",
     "points": [(1, 2), (2, 3), (3, 3), (4, 5), (5, 6)], "fit": {"m": 1, "b": 1},
     "caption": "scatter + best fit y = x + 1"},

    # --- Additional deterministic figures: math-bearing, reuse/extend existing renderers ----------
    # Unit 1 — negatives as distance on the line
    # Unit 1 — negatives as distance on the line (Lesson 1.5 after the factors lesson was inserted at 1.4)
    {"code": "1.5.f1", "lesson": "1.5", "type": "number_line", "min": -6, "max": 6,
     "ticks": [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6],
     "points": [{"x": -5, "label": "-5"}, {"x": -2, "label": "-2"}],
     "caption": "-5 sits farther left (a bigger debt) than -2"},
    # Unit 1 — factors: 12 as its rectangles (1x12, 2x6, 3x4); side lengths are the factor pairs
    {"code": "1.4.f1", "lesson": "1.4", "type": "factor_array", "num": 12,
     "pairs": [[1, 12], [2, 6], [3, 4]], "caption": "the factors of 12 as rectangles: 1x12, 2x6, 3x4"},
    # Unit 4 — the coordinate plane intro; the two worked points plotted (no quadrant labels yet)
    {"code": "4.1.f1", "lesson": "4.1", "type": "plane", "xwindow": [-5, 5], "ywindow": [-5, 5],
     "marks": [(3, 2, "(3, 2)")], "caption": "the address (3, 2): three across, two up from the origin"},
    {"code": "4.1.f2", "lesson": "4.1", "type": "plane", "xwindow": [-5, 5], "ywindow": [-5, 5],
     "marks": [(3, 2, "(3, 2)")], "caption": "Example 1: plotting (3, 2)"},
    {"code": "4.1.f3", "lesson": "4.1", "type": "plane", "xwindow": [-5, 5], "ywindow": [-5, 5],
     "marks": [(-2, -1, "(-2, -1)")], "caption": "Example 2: plotting (-2, -1)"},
    {"code": "4.1.f4", "lesson": "4.1", "type": "plane", "xwindow": [-5, 5], "ywindow": [-5, 5],
     "marks": [(-1, 3, "(-1, 3)")], "caption": "Example 3: the dot read back as (-1, 3)"},
    {"code": "4.1.f5", "lesson": "4.1", "type": "plane", "xwindow": [-1, 7], "ywindow": [-1, 7],
     "marks": [(1, 2, "(1, 2)"), (2, 4, "(2, 4)"), (3, 6, "(3, 6)")], "caption": "Example 4: (1, 2), (2, 4), (3, 6) fall in a row"},
    # Unit 4 — the vertical line test (4.2): a graph + a sweeping vertical test line, hits marked
    {"code": "4.2.f1", "lesson": "4.2", "type": "vlt", "shape": "uparabola", "a": 1, "b": 0, "c": 0,
     "xwindow": [-3, 3], "ywindow": [-1, 9], "test_x": 1, "marks": [(1, 1, "")],
     "caption": "a function: the vertical line meets the graph in just one place"},
    {"code": "4.2.f2", "lesson": "4.2", "type": "vlt", "shape": "line", "m": 2, "b": 1,
     "xwindow": [-3, 3], "ywindow": [-5, 7], "test_x": 1, "marks": [(1, 3, "")],
     "caption": "y = 2x + 1: the vertical line hits once — a function"},
    {"code": "4.2.f3", "lesson": "4.2", "type": "vlt", "shape": "circle", "r": 5,
     "xwindow": [-6, 6], "ywindow": [-6, 6], "test_x": 3, "marks": [(3, 4, ""), (3, -4, "")],
     "caption": "a circle: the vertical line hits twice — not a function"},
    {"code": "4.2.f4", "lesson": "4.2", "type": "vlt", "shape": "vline", "k": 3,
     "xwindow": [-1, 5], "ywindow": [-4, 4], "marks": [(3, -2, ""), (3, 1, ""), (3, 3, "")],
     "caption": "x = 3: one input, many outputs — not a function"},
    # Unit 5 — the coordinate plane; writing a line from a point + slope
    {"code": "5.1.f1", "lesson": "5.1", "type": "plane", "xwindow": [-5, 5], "ywindow": [-5, 5],
     "quadrants": [(2.7, 2.7, "(+, +)"), (-2.7, 2.7, "(-, +)"), (-2.7, -2.7, "(-, -)"), (2.7, -2.7, "(+, -)")],
     "marks": [(3, 2, "(3, 2)")], "caption": "the coordinate plane: plotting (3, 2)"},
    {"code": "5.5.f1", "lesson": "5.5", "type": "line", "m": 4, "b": -5,
     "xwindow": [-1, 4], "ywindow": [-9, 11], "marks": [(0, -5, "(0, -5)"), (2, 3, "(2, 3)")],
     "caption": "y = 4x - 5 through (2, 3)"},
    # Unit 6 — scatter + best fit (a distinct cloud from A.2)
    {"code": "6.3.f1", "lesson": "6.3", "type": "scatter",
     "points": [(1, 3), (2, 2), (3, 4), (4, 5), (5, 4), (6, 6)], "fit": {"m": 0.6, "b": 2},
     "caption": "a scatter plot with its line of best fit"},
    # Unit 7 — a system solved by graphing: two lines meet at the solution
    {"code": "7.1.f1", "lesson": "7.1", "type": "lines2",
     "lines": [{"m": 1, "b": 1}, {"m": -1, "b": 5}], "intersect": [2, 3],
     "xwindow": [-1, 5], "ywindow": [-1, 7], "caption": "two lines meet at the solution (2, 3)"},
    # Unit 8 — a compound 'and' inequality on the line
    {"code": "8.2.f1", "lesson": "8.2", "type": "number_line", "min": -4, "max": 5,
     "ticks": [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
     "points": [{"x": -1, "label": "-1", "filled": True}, {"x": 3, "label": "3", "filled": False}],
     "segments": [{"from": -1, "to": 3}], "caption": "-1 <= x < 3 (a compound 'and')"},
    # Unit 9 — linear vs exponential
    {"code": "9.2.f1", "lesson": "9.2", "type": "growth", "line": {"m": 2, "b": 0}, "exp": {"base": 2},
     "xwindow": [0, 4], "ywindow": [0, 16], "marks": [(1, 2, "(1, 2)"), (3, 8, "(3, 8)")],
     "caption": "straight line y = 2x vs bending curve y = 2^x"},
    # Unit 12 — quadratics: two solutions, factoring roots, formula roots
    {"code": "12.2.f1", "lesson": "12.2", "type": "number_line", "min": -5, "max": 5,
     "ticks": [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
     "points": [{"x": -3, "label": "-3"}, {"x": 3, "label": "3"}],
     "caption": "x^2 = 9 has two solutions, x = -3 and x = 3"},
    {"code": "12.3.f1", "lesson": "12.3", "type": "parabola", "a": 1, "b": -1, "c": -6,
     "xwindow": [-4, 5], "ywindow": [-7, 8],
     "marks": [(-2, 0, "(-2, 0)"), (3, 0, "(3, 0)"), (0.5, -6.25, "vertex")],
     "roots": [-2, 3], "caption": "y = x^2 - x - 6 = (x-3)(x+2)"},
    {"code": "12.5.f1", "lesson": "12.5", "type": "parabola", "a": 1, "b": -4, "c": 3,
     "xwindow": [-1, 5], "ywindow": [-3, 6],
     "marks": [(1, 0, "(1, 0)"), (3, 0, "(3, 0)"), (2, -1, "vertex")],
     "roots": [1, 3], "caption": "y = x^2 - 4x + 3: discriminant 4 > 0, two roots"},
]

def _svg_path(code):
    return os.path.join(FIG_DIR, code + ".svg")

def generate():
    os.makedirs(FIG_DIR, exist_ok=True)
    for s in FIGURES:
        open(_svg_path(s["code"]), "w", encoding="utf-8", newline="\n").write(render(s))
    return len(FIGURES)

def check():
    issues = []
    codes = set()
    for s in FIGURES:
        if s["code"] in codes:
            issues.append(f"duplicate figure code {s['code']}")
        codes.add(s["code"])
        issues += accuracy_issues(s)
        p = _svg_path(s["code"])
        if not os.path.exists(p):
            issues.append(f"{s['code']}: SVG missing (run figures.py)")
        elif open(p, encoding="utf-8").read() != render(s):
            issues.append(f"{s['code']}: SVG stale (run figures.py)")
    return issues

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if a.check:
        iss = check()
        if iss:
            print("FAIL:\n  " + "\n  ".join(iss)); return 1
        print(f"figures: {len(FIGURES)} specs accurate + SVGs current."); return 0
    n = generate(); print(f"generated {n} figure SVGs -> {os.path.relpath(FIG_DIR, REPO_ROOT)}/"); return 0

if __name__ == "__main__":
    sys.exit(main())
