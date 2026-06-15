# -*- coding: utf-8 -*-
"""Annotated worked examples — an HTML/CSS treatment that makes the moves visible.

Each solution is a vertical stack of step rows. Every step shows its equation as
KaTeX ($$..$$), with the x-terms tinted blue and the constants tinted gold so the
eye can follow what travels and what stays. Between consecutive steps a small
centered connector names the single operation performed on both sides.

All arithmetic verified with sympy:
    2x + 3 = 11        -> x = 4
    2(x + 4) = 18      -> x = 5   (distribute, then solve)
    x/2 + x/3 = 5      -> x = 6   (clear the fractions, LCD = 6)
"""

TITLE = "Annotated worked examples"
KIND = "html-css"
BLURB = "A worked solution laid out step by step, with each move named between the lines."
LESSONS = ["2.2", "2.3", "2.6"]

# Colors: the x-terms read blue, the constants read gold. We use the spec's SVG
# hex values directly so the math stays legible on both the light paper and the
# dark surface (KaTeX inline \textcolor isn't touched by the book's dark-mode
# variable swaps, so a fixed mid-tone hex is the safe, readable choice).
_XCOL = "#2980b9"   # blue   — terms with the variable
_KCOL = "#a9740f"   # gold   — plain numbers / constants


def _x(tex):
    """Wrap a fragment as a blue x-term."""
    return r"\textcolor{%s}{%s}" % (_XCOL, tex)


def _k(tex):
    """Wrap a fragment as a gold constant."""
    return r"\textcolor{%s}{%s}" % (_KCOL, tex)


_STYLE = """
<style>
.awe{
  --awe-x:%(xcol)s; --awe-k:%(kcol)s;
  max-width:30rem; margin:0 auto;
  background:var(--card); border:1px solid var(--rule);
  border-left:4px solid var(--blue);
  border-radius:var(--radius); box-shadow:var(--shadow);
  padding:1.15rem 1.35rem 1.3rem;
}
.awe-head{
  font-weight:600; color:var(--blue);
  font-size:.82rem; letter-spacing:.04em; text-transform:uppercase;
  margin:0 0 .15rem;
}
.awe-prompt{
  color:var(--ink-soft); font-size:.95rem; margin:0 0 .35rem;
}
.awe-step{
  background:var(--paper);
  border:1px solid var(--rule); border-radius:var(--radius-sm,11px);
  padding:.5rem .85rem; text-align:center;
}
.awe-step .katex{ font-size:1.18em; }
.awe-step.is-answer{
  border-color:var(--leaf);
  box-shadow:inset 0 0 0 1px var(--leaf);
}
.awe-conn{
  display:flex; align-items:center; justify-content:center; gap:.6rem;
  margin:.32rem auto; color:var(--ink-soft);
  font-size:.86rem; line-height:1.3;
}
.awe-conn::before,.awe-conn::after{
  content:""; height:1px; flex:1 1 1.4rem; max-width:2.4rem;
  background:var(--rule);
}
.awe-conn .op{
  display:inline-block; padding:.12rem .6rem;
  background:var(--card); border:1px solid var(--rule);
  border-radius:999px; white-space:nowrap;
}
.awe-conn .arr{ color:var(--blue); font-weight:600; }
.awe-legend{
  display:flex; flex-wrap:wrap; gap:.4rem 1.1rem;
  margin:.85rem 0 0; padding-top:.7rem;
  border-top:1px solid var(--rule);
  color:var(--ink-soft); font-size:.82rem;
}
.awe-legend b{ font-weight:600; }
.awe-legend .sw{
  display:inline-block; width:.7rem; height:.7rem; border-radius:3px;
  vertical-align:-1px; margin-right:.32rem;
}
.awe-legend .sw-x{ background:var(--awe-x); }
.awe-legend .sw-k{ background:var(--awe-k); }
</style>
""" % {"xcol": _XCOL, "kcol": _KCOL}


def _render(slug, head, prompt, steps, ops):
    """Build one annotated solution.

    steps : list of LaTeX strings (no surrounding $$); last one is the answer.
    ops   : list of operation phrases, one fewer than steps (the connectors).
    """
    assert len(ops) == len(steps) - 1, "need one connector between each pair of steps"
    parts = ['<div class="awe" id="%s">' % slug]
    parts.append('<p class="awe-head">Worked example</p>')
    parts.append('<p class="awe-prompt">%s</p>' % prompt)
    for i, tex in enumerate(steps):
        is_ans = (i == len(steps) - 1)
        cls = "awe-step is-answer" if is_ans else "awe-step"
        parts.append('<div class="%s">$$%s$$</div>' % (cls, tex))
        if i < len(ops):
            parts.append(
                '<div class="awe-conn"><span class="arr">&#8595;</span>'
                '<span class="op">%s</span></div>' % ops[i]
            )
    parts.append(
        '<div class="awe-legend">'
        '<span><span class="sw sw-x"></span><b>x&#8209;terms</b></span>'
        '<span><span class="sw sw-k"></span><b>constants</b></span>'
        "</div>"
    )
    parts.append("</div>")
    # The <style> is identical every time and id-scoped by class, so re-dropping
    # it on a page is harmless.
    return _STYLE + "".join(parts)


def _one_step():
    # 2x + 3 = 11  ->  x = 4
    steps = [
        "%s + %s = %s" % (_x("2x"), _k("3"), _k("11")),
        "%s = %s" % (_x("2x"), _k("8")),                 # 11 - 3 = 8
        "%s = %s" % (_x("x"), _k("4")),                  # 8 / 2 = 4
    ]
    ops = [
        "subtract&nbsp;3 from both sides",
        "divide both sides by&nbsp;2",
    ]
    return _render(
        "awe-twostep",
        "two-step equation",
        "Solve for x:  2x + 3 = 11.",
        steps, ops,
    )


def _distribute():
    # 2(x + 4) = 18  ->  distribute  ->  2x + 8 = 18  ->  x = 5
    steps = [
        "%s = %s" % (_x("2(x + 4)"), _k("18")),
        "%s + %s = %s" % (_x("2x"), _k("8"), _k("18")),  # distribute: 2*4 = 8
        "%s = %s" % (_x("2x"), _k("10")),                # 18 - 8 = 10
        "%s = %s" % (_x("x"), _k("5")),                  # 10 / 2 = 5
    ]
    ops = [
        "distribute the&nbsp;2",
        "subtract&nbsp;8 from both sides",
        "divide both sides by&nbsp;2",
    ]
    return _render(
        "awe-distrib",
        "distribute, then solve",
        "Solve for x:  2(x + 4) = 18.",
        steps, ops,
    )


def _clear_fractions():
    # x/2 + x/3 = 5  ->  *6  ->  3x + 2x = 30  ->  5x = 30  ->  x = 6
    steps = [
        r"%s + %s = %s" % (_x(r"\dfrac{x}{2}"), _x(r"\dfrac{x}{3}"), _k("5")),
        "%s + %s = %s" % (_x("3x"), _x("2x"), _k("30")),  # 6*(x/2)=3x, 6*(x/3)=2x, 6*5=30
        "%s = %s" % (_x("5x"), _k("30")),                 # 3x + 2x = 5x
        "%s = %s" % (_x("x"), _k("6")),                   # 30 / 5 = 6
    ]
    ops = [
        "multiply every term by&nbsp;6 (the LCD)",
        "combine the x&#8209;terms",
        "divide both sides by&nbsp;5",
    ]
    return _render(
        "awe-fractions",
        "clear the fractions",
        "Solve for x:  x/2 + x/3 = 5.",
        steps, ops,
    )


def samples():
    return [
        {"caption": "Two-step equation: 2x + 3 = 11", "html": _one_step()},
        {"caption": "Distribute, then solve: 2(x + 4) = 18", "html": _distribute()},
        {"caption": "Clear the fractions: x/2 + x/3 = 5", "html": _clear_fractions()},
    ]
