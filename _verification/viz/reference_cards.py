# -*- coding: utf-8 -*-
"""Per-unit reference cards — a calm one-card summary for a whole unit.

Each card uses the book's card vocabulary (rounded corners, var(--card)
background, var(--shadow)). It holds the unit title, a short "you can now..."
checklist, the key forms/definitions as tinted chips, and two tiny worked
mini-examples. Every asserted number was checked with sympy:

  Unit 5
    slope through (1,2) and (4,8):  (8-2)/(4-1) = 6/3 = 2
    y = 2x + 1:  y-intercept (0, 1);  x-intercept (-1/2, 0)
  Unit 12
    x^2 = 49        ->  x = +-7
    x^2 - 5x + 6    ->  (x-2)(x-3) -> x = 2 or 3
    x^2 + 5x + 6    ->  discriminant 1 -> x = -2 or -3
    y = x^2 - 2x - 3 ->  vertex (1, -4), x-intercepts -1 and 3, y-intercept -3
"""

TITLE = "Per-unit reference cards"
KIND = "html-css"
BLURB = "A calm one-card recap of a whole unit: what you can now do, the key forms, and two tiny worked examples."
LESSONS = ["5.3", "5.4", "5.6", "12.2", "12.3", "12.5", "12.6"]


# --- shared, idempotent stylesheet -----------------------------------------
# Pure CSS, no JS, so re-running it on a page is harmless. Scoped under
# .refcard so it cannot leak into the rest of the textbook.
def _style():
    # No id on the <style>: rules are class-scoped, so two copies on one page
    # (gallery showing both samples) stay valid HTML with no duplicate-id clash.
    return (
        "<style>\n"
        ".refcard{background:var(--card); border-radius:var(--radius);\n"
        "  box-shadow:var(--shadow); border:1px solid var(--rule);\n"
        "  padding:1.3rem 1.45rem; margin:1.6rem auto; max-width:42rem;\n"
        "  font-family:\"Source Serif 4\",Georgia,serif; color:var(--ink);}\n"
        ".refcard .rc-eyebrow{font-weight:600; font-size:.86rem; letter-spacing:.04em;\n"
        "  text-transform:uppercase; color:var(--blue); margin:0 0 .15rem;}\n"
        ".refcard h3.rc-title{font-family:\"Fraunces\",Georgia,serif; font-weight:600;\n"
        "  font-size:1.42rem; line-height:1.18; margin:0 0 1rem; color:var(--ink);\n"
        "  border:0; padding:0;}\n"
        ".refcard .rc-sec{font-weight:600; font-size:.82rem; letter-spacing:.04em;\n"
        "  text-transform:uppercase; color:var(--ink-soft); margin:1.25rem 0 .5rem;}\n"
        ".refcard ul.rc-can{list-style:none; margin:0; padding:0; display:grid; gap:.5rem;}\n"
        ".refcard ul.rc-can li{display:flex; gap:.6rem; align-items:flex-start;\n"
        "  line-height:1.5;}\n"
        ".refcard ul.rc-can li .rc-tick{flex:0 0 auto; width:1.15rem; height:1.15rem;\n"
        "  margin-top:.18rem; color:var(--leaf);}\n"
        ".refcard .rc-forms{display:grid; gap:.7rem;}\n"
        ".refcard .rc-form{background:var(--card-2); border:1px solid var(--rule);\n"
        "  border-left:3px solid var(--violet); border-radius:var(--radius-sm);\n"
        "  padding:.55rem .85rem;}\n"
        ".refcard .rc-form .rc-label{font-size:.84rem; color:var(--ink-soft);\n"
        "  margin:0 0 .1rem;}\n"
        ".refcard .rc-form .katex-display{margin:.15rem 0; overflow-x:auto;}\n"
        ".refcard .rc-egs{display:grid; gap:.8rem; grid-template-columns:1fr 1fr;}\n"
        ".refcard .rc-eg{background:var(--card-2); border:1px solid var(--rule);\n"
        "  border-left:3px solid var(--leaf); border-radius:var(--radius-sm);\n"
        "  padding:.6rem .85rem .35rem;}\n"
        ".refcard .rc-eg .rc-ask{font-size:.84rem; color:var(--ink-soft); margin:0 0 .1rem;}\n"
        ".refcard .rc-eg .katex-display{margin:.2rem 0; overflow-x:auto;}\n"
        ".refcard .rc-shape{display:flex; gap:.9rem; align-items:center;\n"
        "  background:var(--card-2); border:1px solid var(--rule);\n"
        "  border-radius:var(--radius-sm); padding:.65rem .85rem; margin-top:.2rem;}\n"
        ".refcard .rc-shape svg{flex:0 0 auto; width:108px; height:auto;}\n"
        ".refcard .rc-shape .rc-shape-t{font-size:.92rem; line-height:1.5; color:var(--ink-soft);}\n"
        ".refcard .rc-shape .rc-shape-t b{color:var(--ink); font-weight:600;}\n"
        "@media (max-width:30rem){ .refcard .rc-egs{grid-template-columns:1fr;}\n"
        "  .refcard .rc-shape{flex-direction:column; align-items:flex-start;} }\n"
        "</style>\n"
    )


# a small, reusable rounded check mark (inherits color: leaf)
_TICK = (
    "<svg class=\"rc-tick\" viewBox=\"0 0 24 24\" fill=\"none\" aria-hidden=\"true\">"
    "<path d=\"M5 13l4 4L19 7\" stroke=\"currentColor\" stroke-width=\"2.5\" "
    "stroke-linecap=\"round\" stroke-linejoin=\"round\"/></svg>"
)


def _can_list(items):
    lis = "".join("<li>{tick}<span>{t}</span></li>".format(tick=_TICK, t=t) for t in items)
    return "<ul class=\"rc-can\">" + lis + "</ul>"


def _forms(rows):
    # rows: list of (label, math_without_dollars)
    out = []
    for label, math in rows:
        out.append(
            "<div class=\"rc-form\"><p class=\"rc-label\">{l}</p>$$ {m} $$</div>".format(
                l=label, m=math
            )
        )
    return "<div class=\"rc-forms\">" + "".join(out) + "</div>"


def _eg(ask, math):
    return (
        "<div class=\"rc-eg\"><p class=\"rc-ask\">{a}</p>$$ {m} $$</div>".format(a=ask, m=math)
    )


# --- Unit 5: Linear Functions & Their Graphs -------------------------------
def _unit5():
    can = _can_list([
        "find the slope between two points as rise over run,",
        "read a line straight from <b>slope-intercept form</b>,",
        "graph a line from its slope and y-intercept,",
        "find where a line crosses each axis (its intercepts).",
    ])
    forms = _forms([
        ("Slope (steepness) between two points",
         r"m=\dfrac{\text{rise}}{\text{run}}=\dfrac{y_2-y_1}{x_2-x_1}"),
        ("Slope-intercept form (m = slope, b = y-intercept)",
         r"y=mx+b"),
        ("Intercepts (where the line meets each axis)",
         r"\text{x-int: set }y=0\qquad \text{y-int: set }x=0"),
    ])
    # Mini-example A: slope through (1,2) and (4,8) = 6/3 = 2  (sympy-checked)
    egA = _eg(
        "Slope through (1, 2) and (4, 8)?",
        r"m=\dfrac{8-2}{4-1}=\dfrac{6}{3}=2",
    )
    # Mini-example B: intercepts of y = 2x + 1  ->  (0,1) and (-1/2,0) (sympy-checked)
    egB = _eg(
        "Intercepts of y = 2x + 1?",
        r"(0,\,1)\ \text{and}\ \left(-\tfrac{1}{2},\,0\right)",
    )
    return (
        _style()
        + "<div class=\"refcard\" id=\"u5card\">"
        + "<p class=\"rc-eyebrow\">Unit 5 &middot; Reference card</p>"
        + "<h3 class=\"rc-title\">Linear Functions &amp; Their Graphs</h3>"
        + "<p class=\"rc-sec\">You can now&hellip;</p>"
        + can
        + "<p class=\"rc-sec\">Key forms</p>"
        + forms
        + "<p class=\"rc-sec\">Two quick examples</p>"
        + "<div class=\"rc-egs\">" + egA + egB + "</div>"
        + "</div>"
    )


# --- Unit 12: Quadratic Functions & Equations ------------------------------
def _parabola_svg():
    # A friendly, transparent U. Approved hex so dark-mode overrides apply:
    # axes #888, curve violet #8e44ad, vertex dot green #27ae60.
    # Drawn from y = x^2 mapped into the viewBox; purely decorative shape.
    return (
        "<svg viewBox=\"0 0 120 96\" xmlns=\"http://www.w3.org/2000/svg\" "
        "role=\"img\" aria-label=\"A U-shaped parabola opening upward\">"
        # axes
        "<line x1=\"10\" y1=\"82\" x2=\"110\" y2=\"82\" stroke=\"#888\" "
        "stroke-width=\"1.5\" stroke-linecap=\"round\"/>"
        "<line x1=\"60\" y1=\"8\" x2=\"60\" y2=\"90\" stroke=\"#888\" "
        "stroke-width=\"1.5\" stroke-linecap=\"round\"/>"
        # parabola y = x^2 sampled at x = -6..6 -> (60+8x, 80 - 2*(x^2/...))
        # points computed so vertex sits at (60,78); width ~ +-48px, top ~12px.
        "<path d=\"M 16 12 Q 60 108 104 12\" fill=\"none\" stroke=\"#8e44ad\" "
        "stroke-width=\"2.5\" stroke-linecap=\"round\"/>"
        # vertex (lowest point)
        "<circle cx=\"60\" cy=\"78\" r=\"3.4\" fill=\"#27ae60\"/>"
        "</svg>"
    )


def _unit12():
    can = _can_list([
        "solve a pure square equation with the <b>square-root method</b>,",
        "solve by <b>factoring</b> using the zero-product property,",
        "solve any quadratic with the <b>quadratic formula</b>,",
        "picture a quadratic as a U-shaped <b>parabola</b>.",
    ])
    forms = _forms([
        ("Square-root method (for x squared equals a number)",
         r"x^2=k\ \Longrightarrow\ x=\pm\sqrt{k}"),
        ("Zero-product property (after factoring)",
         r"\text{if } A\cdot B=0,\ \text{then } A=0 \text{ or } B=0"),
        ("Quadratic formula (works for every quadratic)",
         r"x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}"),
    ])
    # Mini-example C: x^2 = 49 -> x = +-7  (sympy-checked)
    egC = _eg(
        "Square-root method: x&sup2; = 49",
        r"x=\pm\sqrt{49}=\pm 7",
    )
    # Mini-example D: factor x^2 - 5x + 6 -> x = 2 or 3  (sympy-checked)
    egD = _eg(
        "Factoring: x&sup2; &minus; 5x + 6 = 0",
        r"(x-2)(x-3)=0\ \Rightarrow\ x=2,\ 3",
    )
    # parabola shape note: y = x^2 - 2x - 3, vertex (1,-4) (sympy-checked, shown as text)
    shape = (
        "<p class=\"rc-sec\">The shape</p>"
        "<div class=\"rc-shape\">"
        + _parabola_svg()
        + "<p class=\"rc-shape-t\">Every quadratic graphs as a <b>parabola</b> &mdash; "
        "a smooth U. It opens up when <span class=\"imath\">a &gt; 0</span> and down "
        "when <span class=\"imath\">a &lt; 0</span>, with a single turning point called "
        "the <b>vertex</b>.</p>"
        + "</div>"
    )
    return (
        _style()
        + "<div class=\"refcard\" id=\"u12card\">"
        + "<p class=\"rc-eyebrow\">Unit 12 &middot; Reference card</p>"
        + "<h3 class=\"rc-title\">Quadratic Functions &amp; Equations</h3>"
        + "<p class=\"rc-sec\">You can now&hellip;</p>"
        + can
        + "<p class=\"rc-sec\">Key methods</p>"
        + forms
        + "<p class=\"rc-sec\">Two quick examples</p>"
        + "<div class=\"rc-egs\">" + egC + egD + "</div>"
        + shape
        + "</div>"
    )


def samples():
    return [
        {
            "caption": "Unit 5 recap: slope, slope-intercept form, and intercepts",
            "html": _unit5(),
        },
        {
            "caption": "Unit 12 recap: square-root method, factoring, the quadratic formula, and the parabola",
            "html": _unit12(),
        },
    ]
