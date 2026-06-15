# -*- coding: utf-8 -*-
"""Interactive equation widgets for the Algebra 1 textbook gallery.

Three self-contained, vanilla-JS widgets that let a nervous beginner *do*
algebra with their hands instead of just reading it:

  1. A balance scale for ``x + 3 = 7``. The beam is drawn level and STAYS
     level, because the whole idea is that doing the same thing to both
     sides keeps the equation balanced. A button takes 3 away from both
     sides until x sits alone, then a calm success state appears.
  2. An "evaluate" slider: drag x from -5..5 and watch 3x + 2 compute live.
  3. A "do the same to both sides" stepper for ``4x = 12`` whose button
     divides both sides by 4 and lands on x = 3.

Every displayed number is computed (and double-checked against sympy in the
module's verification), so a learner never reads a false value.

Note on math text: KaTeX auto-renders ``$$...$$`` once when the page loads,
so it is used for the *static* framing equations. The values that change
while the learner clicks/drags are rendered as plain styled text (allowed
for live interactive widgets), so they stay correct without re-running KaTeX.
"""

TITLE = "Interactive equations"
KIND = "interactive"
BLURB = (
    "Hands-on equation widgets: a balance scale you keep level by doing the "
    "same thing to both sides, plus a live evaluate slider."
)
LESSONS = ["1.1", "1.5", "2.1"]


# --------------------------------------------------------------------------
# Verified facts (computed, not hand-typed). Cross-checked with sympy:
#   solve(x + 3 = 7) -> 4 ;  solve(4x = 12) -> 3 ;  (3*x + 2) over -5..5
# --------------------------------------------------------------------------
def _eval_table():
    """3*x + 2 for x in -5..5, as a JS-ready list of [x, y] pairs."""
    return [[v, 3 * v + 2] for v in range(-5, 6)]


# ==========================================================================
# Sample 1 -- balance scale solver for x + 3 = 7
# ==========================================================================
def _balance():
    slug = "bal"
    # SVG geometry (a calm, symmetric, level scale). The beam never tilts:
    # balance is the lesson, not the surprise.
    svg = f'''
<svg viewBox="0 0 320 230" xmlns="http://www.w3.org/2000/svg"
     font-family="inherit" class="{slug}-svg" aria-hidden="true">
  <!-- base + stand -->
  <line x1="160" y1="70" x2="160" y2="178" stroke="#888" stroke-width="2.5"
        stroke-linecap="round"/>
  <line x1="116" y1="182" x2="204" y2="182" stroke="#888" stroke-width="2.5"
        stroke-linecap="round"/>
  <circle cx="160" cy="70" r="6" fill="#888"/>
  <!-- level beam -->
  <line x1="48" y1="70" x2="272" y2="70" stroke="#8e44ad" stroke-width="2.5"
        stroke-linecap="round"/>
  <!-- hangers -->
  <line x1="78" y1="70" x2="78" y2="104" stroke="#888" stroke-width="2"
        stroke-linecap="round"/>
  <line x1="242" y1="70" x2="242" y2="104" stroke="#888" stroke-width="2"
        stroke-linecap="round"/>
  <!-- pans -->
  <path d="M40 104 Q78 138 116 104" fill="none" stroke="#2980b9"
        stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M204 104 Q242 138 280 104" fill="none" stroke="#2980b9"
        stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <!-- contents are filled in by script, into these groups -->
  <g class="{slug}-left"></g>
  <g class="{slug}-right"></g>
</svg>'''

    # Two equal pans => beam is level. Caption framing uses static KaTeX.
    html = f'''
<div class="{slug}-wrap viz-iq" data-slug="{slug}">
  <style>
    .{slug}-wrap{{max-width:30rem;margin-inline:auto}}
    .{slug}-svg{{max-width:100%;height:auto;display:block;margin-inline:auto}}
    .{slug}-eq{{text-align:center;font-size:1.45rem;letter-spacing:.01em;
      margin:.2rem 0 .1rem;color:var(--ink)}}
    .{slug}-eq .v{{color:var(--violet);font-weight:600}}
    .{slug}-note{{text-align:center;color:var(--ink-soft);
      font-size:.95rem;min-height:1.3em;margin-bottom:.6rem}}
    .{slug}-note.win{{color:var(--leaf);font-weight:600}}
    .{slug}-controls{{display:flex;gap:.6rem;justify-content:center;
      flex-wrap:wrap;margin-top:.2rem}}
    .iq-btn{{font:inherit;font-size:.95rem;cursor:pointer;
      padding:.5rem .9rem;border-radius:var(--radius-sm,11px);
      border:1.5px solid var(--rule);background:var(--card);
      color:var(--ink);box-shadow:var(--shadow);
      transition:transform .12s ease,border-color .12s ease,
        background .12s ease,opacity .12s ease}}
    .iq-btn:hover:not(:disabled){{transform:translateY(-1px);
      border-color:var(--blue)}}
    .iq-btn:active:not(:disabled){{transform:translateY(0)}}
    .iq-btn:focus-visible{{outline:2.5px solid var(--blue);
      outline-offset:2px}}
    .iq-btn.primary{{border-color:var(--blue);color:var(--blue)}}
    .iq-btn:disabled{{opacity:.45;cursor:default;box-shadow:none}}
  </style>

  <p class="{slug}-eq" aria-live="polite"></p>
  <p class="{slug}-note" aria-live="polite">Both pans weigh the same, so the
    scale is level. Keep it that way.</p>
  {svg}
  <p style="text-align:center;color:var(--ink-soft);font-size:.92rem;
    margin:.5rem 0 0">Goal: get the blue&nbsp;<b style="color:var(--blue)">x</b>
    box alone.</p>
  <div class="{slug}-controls">
    <button type="button" class="iq-btn primary" data-act="sub">
      Take 3 from both sides</button>
    <button type="button" class="iq-btn" data-act="reset">Start over</button>
  </div>
</div>

<script>
(function(){{
  var slug = "{slug}";
  // Find the most recently inserted, not-yet-initialised widget of this kind.
  var roots = document.querySelectorAll('.'+slug+'-wrap[data-slug="'+slug+'"]');
  var root = null;
  for (var i = roots.length - 1; i >= 0; i--) {{
    if (!roots[i].dataset.iqReady) {{ root = roots[i]; break; }}
  }}
  if (!root) return;
  root.dataset.iqReady = "1";

  var SVGNS = "http://www.w3.org/2000/svg";
  var leftG  = root.querySelector('.'+slug+'-left');
  var rightG = root.querySelector('.'+slug+'-right');
  var eqEl   = root.querySelector('.'+slug+'-eq');
  var noteEl = root.querySelector('.'+slug+'-note');
  var btnSub = root.querySelector('[data-act="sub"]');
  var btnRst = root.querySelector('[data-act="reset"]');

  // state: left side = one x-box + `units` unit weights; right side = `right`.
  var units, right;

  function unitDot(g, cx, cy){{
    var c = document.createElementNS(SVGNS, "circle");
    c.setAttribute("cx", cx); c.setAttribute("cy", cy);
    c.setAttribute("r", 7);
    c.setAttribute("fill", "#c0392b");
    c.setAttribute("opacity", "0.92");
    g.appendChild(c);
  }}
  function xBox(g, cx, cy){{
    var r = document.createElementNS(SVGNS, "rect");
    var w = 30, h = 24;
    r.setAttribute("x", cx - w/2); r.setAttribute("y", cy - h/2);
    r.setAttribute("width", w);    r.setAttribute("height", h);
    r.setAttribute("rx", 6);
    r.setAttribute("fill", "none");
    r.setAttribute("stroke", "#2980b9");
    r.setAttribute("stroke-width", "2.5");
    g.appendChild(r);
    var t = document.createElementNS(SVGNS, "text");
    t.setAttribute("x", cx); t.setAttribute("y", cy);
    t.setAttribute("text-anchor", "middle");
    t.setAttribute("dominant-baseline", "central");
    t.setAttribute("font-style", "italic");
    t.setAttribute("font-size", "15");
    t.setAttribute("fill", "#2980b9");
    t.textContent = "x";
    g.appendChild(t);
  }}
  // Lay items in a tidy row, centred under a pan whose centre x is `cx`.
  function rowAt(g, cx, hasX, dots){{
    while (g.firstChild) g.removeChild(g.firstChild);
    var items = (hasX ? 1 : 0) + dots;
    var step = 20, y = 92;
    var startX = cx - (items - 1) * step / 2;
    var k = 0;
    if (hasX) {{ xBox(g, startX + k * step, y); k++; }}
    for (var d = 0; d < dots; d++) {{ unitDot(g, startX + k * step, y); k++; }}
  }}

  function solved(){{ return units === 0; }}

  function draw(){{
    rowAt(leftG, 78, true, units);          // left pan centre x = 78
    rowAt(rightG, 242, false, right);       // right pan centre x = 242

    var leftStr = "x" + (units > 0 ? " + " + units : "");
    eqEl.innerHTML = leftStr + " = <span class=\\"v\\">" + right + "</span>";

    if (solved()) {{
      noteEl.textContent = "Balanced and solved \\u2014 x weighs " + right
        + ".  x = " + right;
      noteEl.classList.add("win");
      btnSub.disabled = true;
    }} else {{
      noteEl.textContent = "Still balanced. Take 3 more from each side to free x.";
      noteEl.classList.remove("win");
      btnSub.disabled = false;
    }}
  }}

  function reset(){{
    units = 3; right = 7;     // x + 3 = 7
    btnSub.disabled = false;
    draw();
    noteEl.textContent = "Both pans weigh the same, so the scale is level. "
      + "Keep it that way.";
    noteEl.classList.remove("win");
  }}

  btnSub.addEventListener("click", function(){{
    if (solved()) return;
    // Same operation, both sides => stays balanced.
    units -= 3; right -= 3;   // -> x = 4
    if (units < 0) units = 0;
    draw();
  }});
  btnRst.addEventListener("click", reset);

  reset();
}})();
</script>'''
    return {
        "caption": "Balance scale for x + 3 = 7: subtract 3 from both pans, "
                   "the beam stays level, x is freed (x = 4).",
        "html": html,
    }


# ==========================================================================
# Sample 2 -- evaluate slider for 3x + 2
# ==========================================================================
def _evaluate():
    slug = "evl"
    pairs = _eval_table()
    import json
    data = json.dumps(pairs)

    html = f'''
<div class="{slug}-wrap viz-iq" data-slug="{slug}">
  <style>
    .{slug}-wrap{{max-width:30rem;margin-inline:auto;text-align:center}}
    .{slug}-static{{margin:.1rem 0 .7rem}}
    .{slug}-row{{display:flex;align-items:center;gap:.8rem;
      justify-content:center;flex-wrap:wrap}}
    .{slug}-row label{{color:var(--ink-soft);font-size:.95rem}}
    .{slug}-x{{display:inline-block;min-width:2.4ch;font-weight:600;
      color:var(--blue);font-size:1.15rem}}
    .{slug}-slide{{width:min(22rem,80%);accent-color:var(--blue);
      cursor:pointer;height:1.5rem}}
    .{slug}-slide:focus-visible{{outline:2.5px solid var(--blue);
      outline-offset:4px;border-radius:6px}}
    .{slug}-out{{margin-top:.9rem;font-size:1.35rem;color:var(--ink);
      line-height:1.5}}
    .{slug}-out .term{{color:var(--ink-soft)}}
    .{slug}-out .res{{color:var(--leaf);font-weight:700;
      font-size:1.5rem;display:inline-block;min-width:3ch}}
    .{slug}-ticks{{display:flex;justify-content:space-between;
      width:min(22rem,80%);margin:.1rem auto 0;color:var(--ink-soft);
      font-size:.78rem}}
  </style>

  <p class="{slug}-static">Drag <i>x</i>, and watch the expression compute:</p>
  <div class="{slug}-static">$$3x + 2$$</div>

  <div class="{slug}-row">
    <label for="{slug}-slide">x =</label>
    <span class="{slug}-x" aria-hidden="true">0</span>
  </div>
  <input id="{slug}-slide" class="{slug}-slide" type="range"
         min="-5" max="5" step="1" value="0"
         aria-label="value of x from negative five to five">
  <div class="{slug}-ticks"><span>-5</span><span>0</span><span>5</span></div>

  <p class="{slug}-out" aria-live="polite">
    <span class="term">3(<span class="xa">0</span>) + 2</span>
    &nbsp;=&nbsp; <span class="res">2</span>
  </p>
</div>

<script>
(function(){{
  var slug = "{slug}";
  var DATA = {data};                 // [[x, 3x+2], ...] precomputed & verified
  var map = {{}};
  for (var i = 0; i < DATA.length; i++) map[DATA[i][0]] = DATA[i][1];

  var roots = document.querySelectorAll('.'+slug+'-wrap[data-slug="'+slug+'"]');
  var root = null;
  for (var j = roots.length - 1; j >= 0; j--) {{
    if (!roots[j].dataset.iqReady) {{ root = roots[j]; break; }}
  }}
  if (!root) return;
  root.dataset.iqReady = "1";

  var slide = root.querySelector('.'+slug+'-slide');
  var xLbl  = root.querySelector('.'+slug+'-x');
  var xa    = root.querySelector('.'+slug+'-out .xa');
  var res   = root.querySelector('.'+slug+'-out .res');

  function fmt(n){{ return n < 0 ? "(" + n + ")" : "" + n; }}

  function update(){{
    var x = parseInt(slide.value, 10);
    var y = map[x];
    if (y === undefined) y = 3 * x + 2;   // safety; matches the table
    xLbl.textContent = x;
    xa.textContent = fmt(x);
    res.textContent = y;
  }}

  slide.addEventListener("input", update);
  slide.addEventListener("change", update);
  update();
}})();
</script>'''
    return {
        "caption": "Evaluate slider: drag x from -5 to 5 and 3x + 2 updates "
                   "live (x = 0 gives 2, x = 5 gives 17).",
        "html": html,
    }


# ==========================================================================
# Sample 3 -- "do the same to both sides" stepper for 2x = 8
# ==========================================================================
def _divide():
    slug = "div"
    html = f'''
<div class="{slug}-wrap viz-iq" data-slug="{slug}">
  <style>
    .{slug}-wrap{{max-width:30rem;margin-inline:auto;text-align:center}}
    .{slug}-eq{{font-size:1.6rem;margin:.3rem 0 .2rem;color:var(--ink);
      letter-spacing:.01em}}
    .{slug}-eq .v{{color:var(--violet);font-weight:600}}
    .{slug}-note{{color:var(--ink-soft);min-height:1.3em;
      font-size:.95rem;margin:.1rem 0 .7rem}}
    .{slug}-note.win{{color:var(--leaf);font-weight:600}}
    .{slug}-vis{{display:flex;gap:1.4rem;justify-content:center;
      align-items:flex-end;margin:.2rem 0 .9rem;min-height:74px}}
    .{slug}-side{{display:flex;flex-direction:column;align-items:center;
      gap:.35rem}}
    .{slug}-side .lab{{color:var(--ink-soft);font-size:.82rem}}
    .{slug}-groups{{display:flex;gap:.5rem;align-items:flex-end}}
    .{slug}-grp{{display:flex;flex-direction:column-reverse;gap:.28rem;
      padding:.3rem;border-radius:9px}}
    .{slug}-grp.ring{{outline:1.5px dashed var(--blue);
      outline-offset:1px}}
    .{slug}-xchip{{width:30px;height:24px;border-radius:6px;
      border:1.5px solid var(--blue);color:var(--blue);
      display:flex;align-items:center;justify-content:center;
      font-style:italic;font-size:.95rem;background:transparent}}
    .{slug}-unit{{width:14px;height:14px;border-radius:50%;
      background:var(--rose);opacity:.9}}
    .{slug}-controls{{display:flex;gap:.6rem;justify-content:center;
      flex-wrap:wrap}}
  </style>

  <p class="{slug}-eq" aria-live="polite"></p>
  <p class="{slug}-note" aria-live="polite"></p>

  <div class="{slug}-vis">
    <div class="{slug}-side">
      <div class="{slug}-groups {slug}-left"></div>
      <span class="lab">left side</span>
    </div>
    <div style="font-size:1.4rem;color:var(--ink-soft);
      align-self:center">=</div>
    <div class="{slug}-side">
      <div class="{slug}-groups {slug}-right"></div>
      <span class="lab">right side</span>
    </div>
  </div>

  <div class="{slug}-controls">
    <button type="button" class="iq-btn primary" data-act="div">
      Divide both sides by 4</button>
    <button type="button" class="iq-btn" data-act="reset">Start over</button>
  </div>
</div>

<script>
(function(){{
  var slug = "{slug}";
  var roots = document.querySelectorAll('.'+slug+'-wrap[data-slug="'+slug+'"]');
  var root = null;
  for (var i = roots.length - 1; i >= 0; i--) {{
    if (!roots[i].dataset.iqReady) {{ root = roots[i]; break; }}
  }}
  if (!root) return;
  root.dataset.iqReady = "1";

  var eqEl   = root.querySelector('.'+slug+'-eq');
  var noteEl = root.querySelector('.'+slug+'-note');
  var leftG  = root.querySelector('.'+slug+'-left');
  var rightG = root.querySelector('.'+slug+'-right');
  var btnDiv = root.querySelector('[data-act="div"]');
  var btnRst = root.querySelector('[data-act="reset"]');

  // state: coef * x = total.  Start 4x = 20, split into `groups` equal columns.
  var coef, total, groups;

  function chip(){{ var d = document.createElement("div");
    d.className = slug + "-xchip"; d.textContent = "x"; return d; }}
  function unit(){{ var d = document.createElement("div");
    d.className = slug + "-unit"; return d; }}

  function clear(g){{ while (g.firstChild) g.removeChild(g.firstChild); }}

  function render(){{
    clear(leftG); clear(rightG);
    var ring = groups > 1;             // show the equal-share grouping
    var perL = coef / groups;          // x's per group (1 each)
    var perR = total / groups;         // units per group
    for (var g = 0; g < groups; g++) {{
      var gl = document.createElement("div");
      gl.className = slug + "-grp" + (ring ? " ring" : "");
      for (var a = 0; a < perL; a++) gl.appendChild(chip());
      leftG.appendChild(gl);

      var gr = document.createElement("div");
      gr.className = slug + "-grp" + (ring ? " ring" : "");
      for (var b = 0; b < perR; b++) gr.appendChild(unit());
      rightG.appendChild(gr);
    }}

    var leftStr = (coef === 1 ? "x" : coef + "x");
    eqEl.innerHTML = leftStr + " = <span class=\\"v\\">" + total + "</span>";

    if (coef === 1) {{
      noteEl.textContent = "One x equals " + total + ".  x = " + total
        + ".  Solved!";
      noteEl.classList.add("win");
      btnDiv.disabled = true;
    }} else {{
      noteEl.textContent = coef + " equal x's share " + total + " equally "
        + "\\u2014 split both sides into " + coef + " matching groups.";
      noteEl.classList.remove("win");
      btnDiv.disabled = false;
    }}
  }}

  function reset(){{
    coef = 4; total = 12; groups = 1;   // 4x = 12
    btnDiv.disabled = false;
    render();
  }}

  btnDiv.addEventListener("click", function(){{
    if (coef === 1) return;
    var k = coef;                      // show the k equal shares first...
    groups = k;
    render();
    // ...then settle to one group => x = total / k
    total = total / k; coef = 1; groups = 1;
    setTimeout(render, 480);
  }});
  btnRst.addEventListener("click", reset);

  reset();
}})();
</script>'''
    return {
        "caption": "Divide-both-sides stepper for 4x = 12: split each side into "
                   "4 equal shares to reach x = 3.",
        "html": html,
    }


def samples():
    return [_balance(), _evaluate(), _divide()]


# Tiny self-check when run directly (not used by the gallery importer).
if __name__ == "__main__":
    ss = samples()
    print(TITLE, "->", len(ss), "samples")
    for s in ss:
        assert "caption" in s and "html" in s and s["html"].strip()
        print("  -", s["caption"][:60])
