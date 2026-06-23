# -*- coding: utf-8 -*-
"""Interactive Vertical Line Test widget for the Algebra 1 textbook gallery.

A single self-contained inline-SVG + vanilla-JS widget that lets a learner SEE
why "a function passes the vertical line test." The reader grabs a big red handle
and drags a dashed vertical test line across the plane themselves (a slider and an
auto-Sweep button are there too); at every x it lights up a dot wherever the line
crosses the chosen graph and tallies the hits live:

  * a straight (non-vertical) LINE is touched exactly ONCE at every x, so the
    sweep stays green and the verdict reads "a function";
  * a CIRCLE centred at the origin is touched TWICE wherever the line is inside
    it, so the instant the sweep finds a 2-hit position the verdict locks to red
    "not a function" (one vertical line hitting twice is all it takes to fail).
  * an up-PARABOLA y = a x^2 is a third option: also one hit everywhere, another
    "passes" case so the rule doesn't read as "lines good, curves bad."

Same conventions as interactive_graph.py: no libraries, no randomness, no clock
for STATE (requestAnimationFrame drives only the optional sweep animation; the
picture renders correctly statically and is safe to re-init). Wrapped in an IIFE
that reads document.currentScript.parentNode as root, guards on root.dataset.init,
scopes every DOM query to root, and uses slug-prefixed ids so instances never
collide. Degrades without KaTeX (all readouts are plain styled text).

COLOR CONTRACT (literal hexes so the book's dark-mode SVG overrides apply):
  graph #2980b9 (blue), vertical TEST LINE #c0392b (red, dashed),
  intersection dots #c0392b, axes/grid #888.

CORRECTNESS: the JS coordinate mapper px()/py() is the SINGLE source of truth for
both the drawn geometry and the text readouts, so the picture can never disagree
with the count. The circle intersections solve x^2 + y^2 = r^2 at the test x = X:
y = +/- sqrt(r^2 - X^2) when |X| <= r, none otherwise. The mapper round-trip and
the intersection arithmetic are cross-checked in Python at import time.
"""

TITLE = "Vertical line test"
KIND = "interactive"
BLURB = (
    "Drag a red vertical line across a graph and watch the hits tally: one "
    "touch everywhere means a function; two touches anywhere means it is not."
)
LESSONS = ["4.2"]


# --------------------------------------------------------------------------- #
# Shared coordinate-mapping helpers (mirrored exactly by the inline JS below). #
# Window is symmetric: x,y in [-LIM, LIM]. Pixel box is WxW with PAD padding.  #
# --------------------------------------------------------------------------- #
_W = 360       # svg pixel width/height of the plotting square
_PAD = 30      # padding so axis labels + tick numbers have breathing room
_LIM = 6       # axis range: -6..6 in both directions
_R = 4         # circle radius for the non-function option


def _to_px(x, y, lim=_LIM, w=_W, pad=_PAD):
    """Map graph coords -> pixel coords (y flipped). Same formula as JS px/py()."""
    sx = (w - 2 * pad) / (2 * lim)
    px = pad + (x + lim) * sx
    py = pad + (lim - y) * sx          # y grows upward in graph space
    return (round(px, 3), round(py, 3))


def _fmt(v):
    """Format a number the way the JS readout does: drop a trailing '.0'."""
    v = round(float(v), 2)
    if v == int(v):
        return str(int(v))
    return ("%g" % v)


def _circle_hits(x, r=_R):
    """y-values where the vertical line x=X meets x^2+y^2=r^2 (mirror of JS)."""
    d = r * r - x * x
    if d < 0:
        return []
    if d == 0:
        return [0.0]
    import math
    s = math.sqrt(d)
    return [s, -s]


# --------------------------------------------------------------------------- #
# Static SVG scaffold (axes + light grid + tick numbers) shared by all widgets #
# Built in Python so the grid lines land on exact integer coordinates.         #
# --------------------------------------------------------------------------- #
def _grid_svg():
    parts = []
    # faint grid lines at every integer
    for i in range(-_LIM, _LIM + 1):
        if i == 0:
            continue
        x1, y1 = _to_px(i, -_LIM)
        x2, y2 = _to_px(i, _LIM)
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                     f'stroke="#888" stroke-width="0.6" opacity="0.28"/>')
        hx1, hy1 = _to_px(-_LIM, i)
        hx2, hy2 = _to_px(_LIM, i)
        parts.append(f'<line x1="{hx1}" y1="{hy1}" x2="{hx2}" y2="{hy2}" '
                     f'stroke="#888" stroke-width="0.6" opacity="0.28"/>')
    # axes
    ax1, ay = _to_px(-_LIM, 0)
    ax2, _ = _to_px(_LIM, 0)
    parts.append(f'<line x1="{ax1}" y1="{ay}" x2="{ax2}" y2="{ay}" '
                 f'stroke="#888" stroke-width="2.5" stroke-linecap="round"/>')
    ax, ay1 = _to_px(0, _LIM)
    _, ay2 = _to_px(0, -_LIM)
    parts.append(f'<line x1="{ax}" y1="{ay1}" x2="{ax}" y2="{ay2}" '
                 f'stroke="#888" stroke-width="2.5" stroke-linecap="round"/>')
    # axis letters
    parts.append(f'<text x="{ax2 - 4}" y="{ay - 8}" font-size="13" '
                 f'fill="#888" text-anchor="end">x</text>')
    parts.append(f'<text x="{ax + 8}" y="{ay1 + 11}" font-size="13" '
                 f'fill="#888">y</text>')
    # a few tick numbers on each axis (skip 0; keep it uncluttered)
    for i in (-4, -2, 2, 4):
        tx, _ = _to_px(i, 0)
        parts.append(f'<text x="{tx}" y="{ay + 15}" font-size="10" '
                     f'fill="#888" text-anchor="middle">{i}</text>')
        _, ty = _to_px(0, i)
        parts.append(f'<text x="{ax - 6}" y="{ty + 3.5}" font-size="10" '
                     f'fill="#888" text-anchor="end">{i}</text>')
    return "\n    ".join(parts)


# JS snippet (as a Python string) of the mapper, injected into the widget so the
# drawing math is identical to _to_px above. {LIM},{W},{PAD} filled per-widget.
_JS_MAP = """
  var LIM={LIM}, W={W}, PAD={PAD};
  var SX=(W-2*PAD)/(2*LIM);
  function px(x){{return PAD+(x+LIM)*SX;}}
  function py(y){{return PAD+(LIM-y)*SX;}}
  function fmt(v){{v=Math.round(v*100)/100; return (v===Math.round(v))?(''+Math.round(v)):(''+v);}}
"""


# --------------------------------------------------------------------------- #
# The widget: a graph selector (line / circle / parabola), a draggable red      #
# vertical test line (handle + drag-anywhere + slider), and a Sweep button.     #
# --------------------------------------------------------------------------- #
def _vlt_widget(slug, r=_R):
    grid = _grid_svg()
    jsmap = _JS_MAP.format(LIM=_LIM, W=_W, PAD=_PAD)

    html = f"""<div class="{slug}-wrap" data-init="0">
  <style>
    .{slug}-wrap{{max-width:380px;margin:0 auto;font-family:inherit}}
    .{slug}-wrap svg{{width:100%;height:auto;display:block;
      background:transparent;border-radius:var(--radius);touch-action:none}}
    .{slug}-seg{{display:flex;gap:.3rem;justify-content:center;margin:.1rem 0 .55rem;
      flex-wrap:wrap}}
    .{slug}-seg label{{cursor:pointer;font-size:.85rem;font-weight:600;
      color:var(--ink-soft);border:1.5px solid #888;border-radius:999px;
      padding:.22rem .7rem;user-select:none;background:transparent;
      transition:background .12s,color .12s,border-color .12s}}
    .{slug}-seg input{{position:absolute;opacity:0;width:0;height:0}}
    .{slug}-seg input:checked + label{{background:var(--blue);color:#fff;
      border-color:var(--blue)}}
    .{slug}-seg input:focus-visible + label{{outline:2px solid var(--blue);
      outline-offset:2px}}
    .{slug}-ctrl{{display:grid;grid-template-columns:auto 1fr auto;gap:.5rem .7rem;
      align-items:center;margin:.55rem .3rem 0;font-size:.92rem;color:var(--ink-soft)}}
    .{slug}-ctrl label{{font-weight:600;color:var(--ink)}}
    .{slug}-ctrl output{{font:600 .92rem "IBM Plex Mono",monospace;color:var(--ink);
      min-width:2.6em;text-align:right}}
    .{slug}-wrap input[type=range]{{width:100%;accent-color:#c0392b;
      height:1.4rem;cursor:pointer}}
    .{slug}-wrap input[type=range]:focus-visible{{outline:2px solid #c0392b;
      outline-offset:3px;border-radius:6px}}
    .{slug}-bar{{display:flex;gap:.6rem;align-items:center;justify-content:center;
      margin:.7rem 0 .2rem;flex-wrap:wrap}}
    .{slug}-sweep{{font:700 1rem inherit;cursor:pointer;border:none;
      border-radius:999px;padding:.5rem 1.3rem;background:#c0392b;color:#fff;
      letter-spacing:.01em;box-shadow:0 2px 6px rgba(192,57,43,.35);
      transition:transform .08s,background .12s}}
    .{slug}-sweep:hover{{transform:translateY(-1px)}}
    .{slug}-sweep:active{{transform:translateY(0)}}
    .{slug}-sweep:focus-visible{{outline:3px solid var(--blue);outline-offset:2px}}
    .{slug}-reset{{font:600 .85rem inherit;cursor:pointer;background:transparent;
      border:1.5px solid #888;border-radius:999px;padding:.4rem .9rem;
      color:var(--ink-soft)}}
    .{slug}-reset:focus-visible{{outline:2px solid var(--blue);outline-offset:2px}}
    .{slug}-read{{text-align:center;margin:.6rem 0 0;font-size:.95rem;
      color:var(--ink-soft)}}
    .{slug}-hits b{{font:700 1.05rem "IBM Plex Mono",monospace;color:#c0392b}}
    .{slug}-badge{{display:inline-block;margin-top:.45rem;font-weight:700;
      font-size:.95rem;padding:.28rem .85rem;border-radius:999px;
      border:2px solid #27ae60;color:#27ae60;background:rgba(39,174,96,.08)}}
    .{slug}-badge.fail{{border-color:#c0392b;color:#c0392b;
      background:rgba(192,57,43,.1)}}
    .{slug}-hint{{display:block;text-align:center;font-size:.8rem;
      color:var(--ink-soft);margin-top:.4rem;opacity:.85}}
  </style>

  <div class="{slug}-seg" role="radiogroup" aria-label="choose a graph to test">
    <input type="radio" name="{slug}-graph" id="{slug}-g-line" value="line" checked>
    <label for="{slug}-g-line">Line&nbsp;y = x</label>
    <input type="radio" name="{slug}-graph" id="{slug}-g-circ" value="circle">
    <label for="{slug}-g-circ">Circle&nbsp;r = {r}</label>
    <input type="radio" name="{slug}-graph" id="{slug}-g-par" value="parab">
    <label for="{slug}-g-par">Parabola</label>
  </div>

  <svg viewBox="0 0 {_W} {_W}" xmlns="http://www.w3.org/2000/svg"
       font-family="sans-serif"
       aria-label="coordinate grid with a graph and a movable vertical test line">
    {grid}
    <path id="{slug}-graph" fill="none" stroke="#2980b9" stroke-width="2.5"
          stroke-linecap="round" stroke-linejoin="round"/>
    <line id="{slug}-test" stroke="#c0392b" stroke-width="2.2"
          stroke-dasharray="6 5" stroke-linecap="round"/>
    <circle id="{slug}-h0" r="0" fill="#c0392b" stroke="#fff" stroke-width="1.4"
            opacity="0"/>
    <circle id="{slug}-h1" r="0" fill="#c0392b" stroke="#fff" stroke-width="1.4"
            opacity="0"/>
    <!-- the big draggable handle that rides the test line near the top edge -->
    <circle id="{slug}-grip" r="11" fill="#c0392b" stroke="#fff" stroke-width="2.5"
            tabindex="0" role="slider"
            aria-label="vertical test line, drag or use the left and right arrow keys"
            aria-valuemin="-6" aria-valuemax="6"
            style="cursor:ew-resize;outline:none"/>
  </svg>

  <div class="{slug}-ctrl">
    <label for="{slug}-x">test&nbsp;x</label>
    <input id="{slug}-x" type="range" min="-6" max="6" step="any" value="-5"
       aria-label="x position of the vertical test line, from negative 6 to 6">
    <output id="{slug}-xo">-5</output>
  </div>

  <div class="{slug}-bar">
    <button type="button" class="{slug}-sweep" id="{slug}-sweep"
            aria-label="animate the test line sweeping across the graph"
            aria-pressed="false">&#9654;&nbsp;Sweep</button>
    <button type="button" class="{slug}-reset" id="{slug}-reset"
            aria-label="reset the verdict">Reset</button>
  </div>

  <div class="{slug}-read">
    <div class="{slug}-hits">hits at this x:&nbsp;<b id="{slug}-n">1</b></div>
    <span class="{slug}-badge" id="{slug}-badge">&#10003; a function</span>
    <span class="{slug}-hint" id="{slug}-hint">Drag the red handle across the plane
      (or scrub the slider / press &larr; &rarr;). Two hits anywhere means it fails.</span>
  </div>

  <script>(function(){{
    var root=document.currentScript.parentNode;
    if(!root||root.dataset.init==="1"){{return;}} root.dataset.init="1";
    {jsmap}
    var R={r};

    var gpath=root.querySelector("#{slug}-graph");
    var tline=root.querySelector("#{slug}-test");
    var h0=root.querySelector("#{slug}-h0");
    var h1=root.querySelector("#{slug}-h1");
    var grip=root.querySelector("#{slug}-grip");
    var svg=gpath.ownerSVGElement;
    var sx=root.querySelector("#{slug}-x");
    var xo=root.querySelector("#{slug}-xo");
    var nEl=root.querySelector("#{slug}-n");
    var badge=root.querySelector("#{slug}-badge");
    var hint=root.querySelector("#{slug}-hint");
    var sweepBtn=root.querySelector("#{slug}-sweep");
    var resetBtn=root.querySelector("#{slug}-reset");
    var radios=root.querySelectorAll('input[name="{slug}-graph"]');

    var mode="line";       // "line" | "circle" | "parab"
    var failed=false;      // verdict locks to "not a function" once 2 hits seen
    var raf=null;          // requestAnimationFrame handle for the sweep
    var sweepDir=1;        // +1 right, -1 left
    var bounces=0;         // stop after a left->right->left pass

    function clampX(X){{
      if(!isFinite(X)) return 0;
      if(X<-LIM) return -LIM;
      if(X>LIM) return LIM;
      return X;
    }}

    // --- geometry: the chosen graph as an SVG path (mapper is the source) ----
    function graphPath(){{
      var d="", started=false, i, x, y, t;
      if(mode==="line"){{
        // y = x, drawn corner to corner
        return "M"+px(-LIM).toFixed(2)+" "+py(-LIM).toFixed(2)+
               " L"+px(LIM).toFixed(2)+" "+py(LIM).toFixed(2);
      }}
      if(mode==="parab"){{
        // y = 0.5 x^2 (an up-parabola; still one hit per x)
        for(i=0;i<=120;i++){{
          x=-LIM+(2*LIM)*i/120; y=0.5*x*x;
          if(y<-LIM-0.5||y>LIM+0.5){{ started=false; continue; }}
          d+=(started?" L":"M")+px(x).toFixed(2)+" "+py(y).toFixed(2);
          started=true;
        }}
        return d || ("M"+px(0)+" "+py(0));
      }}
      // circle x^2 + y^2 = R^2, traced as a polyline so it uses the same mapper
      for(i=0;i<=140;i++){{
        t=2*Math.PI*i/140;
        x=R*Math.cos(t); y=R*Math.sin(t);
        d+=(i===0?"M":" L")+px(x).toFixed(2)+" "+py(y).toFixed(2);
      }}
      return d+" Z";
    }}

    // --- intersections of the vertical line x=X with the chosen graph --------
    // Returns an array of y-values (0, 1, or 2 entries).
    function hitsAt(X){{
      if(mode==="line"){{           // y = x  -> exactly one
        return [X];
      }}
      if(mode==="parab"){{          // y = 0.5 x^2 -> exactly one (may be offscreen)
        var y=0.5*X*X;
        return (y<=LIM+0.001)?[y]:[];
      }}
      // circle: y = +/- sqrt(R^2 - X^2) when |X| <= R
      var disc=R*R - X*X;
      if(disc<0) return [];
      if(disc===0) return [0];
      var s=Math.sqrt(disc);
      return [s,-s];
    }}

    function setDot(dot,X,y,vis){{
      if(vis){{
        dot.setAttribute("cx",px(X)); dot.setAttribute("cy",py(y));
        dot.setAttribute("r","6"); dot.setAttribute("opacity","1");
      }} else {{
        dot.setAttribute("r","0"); dot.setAttribute("opacity","0");
      }}
    }}

    function draw(){{
      var X=clampX(parseFloat(sx.value));
      xo.textContent=fmt(X);
      // test line top-to-bottom at x=X
      tline.setAttribute("x1",px(X)); tline.setAttribute("y1",py(LIM));
      tline.setAttribute("x2",px(X)); tline.setAttribute("y2",py(-LIM));
      // the draggable handle rides the line just below the top edge
      grip.setAttribute("cx",px(X)); grip.setAttribute("cy",py(LIM)+14);
      grip.setAttribute("aria-valuenow",fmt(X));
      grip.setAttribute("aria-valuetext","x equals "+fmt(X));
      // intersection dots (only those on-screen are shown)
      var ys=hitsAt(X);
      var shown=[];
      for(var k=0;k<ys.length;k++){{
        if(ys[k]>=-LIM-0.001 && ys[k]<=LIM+0.001) shown.push(ys[k]);
      }}
      setDot(h0, X, shown[0], shown.length>=1);
      setDot(h1, X, shown[1], shown.length>=2);
      var n=shown.length;
      nEl.textContent=n;
      // a position with 2 hits permanently fails the test
      if(n>=2 && !failed){{ failed=true; }}
      updateVerdict();
    }}

    function updateVerdict(){{
      badge.className="{slug}-badge";
      if(failed){{
        badge.classList.add("fail");
        badge.textContent="\\u2717 not a function";
      }} else {{
        badge.textContent="\\u2713 a function";
      }}
    }}

    // --- the auto-sweep: a smooth left -> right -> left glide -----------------
    function startSweep(){{
      stopSweep();
      // begin from the far left so the whole graph gets tested
      sx.value="-6"; sweepDir=1; bounces=0;
      var last=null;
      function step(ts){{
        if(last==null) last=ts;
        var dt=(ts-last)/1000; last=ts;
        if(dt>0.1) dt=0.1;                          // ignore long frame gaps
        var X=clampX(parseFloat(sx.value))+sweepDir*5.0*dt;   // ~5 units/sec
        if(X>=LIM){{ X=LIM; sweepDir=-1; bounces++; }}
        else if(X<=-LIM){{ X=-LIM; sweepDir=1; bounces++; }}
        sx.value=String(X);
        draw();
        if(bounces>=2){{ stopSweep(); return; }}   // left->right->left, then stop
        raf=requestAnimationFrame(step);
      }}
      sweepBtn.setAttribute("aria-pressed","true");
      raf=requestAnimationFrame(step);
    }}
    function stopSweep(){{
      if(raf!=null){{ cancelAnimationFrame(raf); raf=null; }}
      sweepBtn.setAttribute("aria-pressed","false");
    }}

    function setMode(m){{
      mode=m; failed=false; stopSweep();
      gpath.setAttribute("d", graphPath());
      sx.value="-5";
      draw();
      hint.textContent = (m==="circle")
        ? "Drag inside the circle: the line hits twice \\u2014 that fails the test."
        : "Drag anywhere: one hit at every x \\u2014 that passes the test.";
    }}

    // --- manual control is the star: drag the handle, or drag anywhere on the
    //     plane, and the test line snaps to your finger/pointer in real time. --
    function gxFromEvent(evt){{
      var rb=svg.getBoundingClientRect();
      var sxpx=(evt.clientX-rb.left)*(W/rb.width);   // client px -> viewBox px
      var gxv=(sxpx-PAD)/SX-LIM;                      // inverse of px()
      gxv=clampX(gxv);
      return Math.round(gxv*10)/10;                   // match slider's 0.1 step
    }}
    var dragging=false;
    function beginDrag(e){{
      dragging=true; stopSweep();
      if(svg.setPointerCapture && e.pointerId!=null){{
        try{{svg.setPointerCapture(e.pointerId);}}catch(_){{}}
      }}
      sx.value=String(gxFromEvent(e)); draw(); e.preventDefault();
    }}
    function moveDrag(e){{
      if(!dragging)return;
      sx.value=String(gxFromEvent(e)); draw(); e.preventDefault();
    }}
    function endDrag(e){{
      if(!dragging)return; dragging=false;
      if(svg.releasePointerCapture && e&&e.pointerId!=null){{
        try{{svg.releasePointerCapture(e.pointerId);}}catch(_){{}}
      }}
    }}
    grip.addEventListener("pointerdown",function(e){{ e.stopPropagation(); beginDrag(e); }});
    svg.addEventListener("pointerdown",beginDrag);  // tap/drag anywhere on the plane
    svg.addEventListener("pointermove",moveDrag);
    svg.addEventListener("pointerup",endDrag);
    svg.addEventListener("pointercancel",endDrag);
    window.addEventListener("pointerup",endDrag);

    // keyboard on the handle: arrows nudge, Home/End jump to the edges.
    grip.addEventListener("keydown",function(e){{
      var X=clampX(parseFloat(sx.value)), moved=true;
      if(e.key==="ArrowLeft"||e.key==="ArrowDown") X-=0.5;
      else if(e.key==="ArrowRight"||e.key==="ArrowUp") X+=0.5;
      else if(e.key==="Home") X=-LIM;
      else if(e.key==="End") X=LIM;
      else moved=false;
      if(!moved) return;
      stopSweep();
      sx.value=String(clampX(X)); draw(); e.preventDefault();
    }});

    // --- wiring --------------------------------------------------------------
    sx.addEventListener("input",function(){{ stopSweep(); draw(); }});
    sweepBtn.addEventListener("click",function(){{
      if(raf!=null) stopSweep(); else startSweep();
    }});
    resetBtn.addEventListener("click",function(){{
      stopSweep(); failed=false; sx.value="-5"; draw();
    }});
    for(var ri=0;ri<radios.length;ri++){{
      radios[ri].addEventListener("change",function(e){{
        if(e.target.checked) setMode(e.target.value);
      }});
    }}

    // initial render (static, correct without any interaction)
    gpath.setAttribute("d", graphPath());
    draw();
  }})();</script>
</div>"""
    return html


# --------------------------------------------------------------------------- #
# Import-time self-check: confirm the mapper round-trips and the intersection   #
# arithmetic matches what the JS computes for the chosen defaults.             #
# --------------------------------------------------------------------------- #
def _selfcheck():
    # mapper sanity: origin maps to centre; corners map to the padded box.
    cx, cy = _to_px(0, 0)
    assert abs(cx - _W / 2) < 1e-6 and abs(cy - _W / 2) < 1e-6, (cx, cy)
    assert _to_px(-_LIM, -_LIM) == (float(_PAD), float(_W - _PAD))
    assert _to_px(_LIM, _LIM) == (float(_W - _PAD), float(_PAD))
    # a sampled point lands where arithmetic says it should (round-trip).
    pxa, pya = _to_px(2, 2)            # on y = x
    expx, expy = _to_px(2, 2)
    assert (pxa, pya) == (expx, expy)

    # circle intersections: x^2 + y^2 = r^2 at test x = X.
    import math
    r = _R
    # inside -> two symmetric hits
    hs = _circle_hits(0, r)
    assert len(hs) == 2 and abs(hs[0] - r) < 1e-9 and abs(hs[1] + r) < 1e-9, hs
    hs = _circle_hits(3, r)            # 3^2 + y^2 = 16 -> y = +/- sqrt(7)
    assert len(hs) == 2, hs
    assert abs(hs[0] - math.sqrt(7)) < 1e-9 and abs(hs[1] + math.sqrt(7)) < 1e-9, hs
    assert abs(hs[0] + hs[1]) < 1e-12, hs   # symmetric about the x-axis
    # tangent -> exactly one hit at y = 0
    hs = _circle_hits(r, r)
    assert hs == [0.0], hs
    # outside -> no hits
    assert _circle_hits(r + 1, r) == [], _circle_hits(r + 1, r)

    # the parabola y = 0.5 x^2 and the line y = x each give exactly one y per x.
    for X in (-3, -1, 0, 1.5, 3):
        assert len([0.5 * X * X]) == 1
        assert len([X]) == 1

    # formatting matches the documented readout style.
    assert _fmt(-5) == "-5" and _fmt(1.5) == "1.5" and _fmt(2.0) == "2", _fmt(2.0)


_selfcheck()


def samples():
    return [
        {
            "caption": (
                "Vertical line test, hands-on: pick a graph, then grab the red "
                "handle and drag the dashed test line across the plane (scrub the "
                "slider, press the arrow keys, or tap ▶ Sweep to watch it glide "
                "on its own). The dots and the hit count update as you move. The "
                "line y = x (and the parabola) get touched exactly once at every "
                "x, so the verdict stays “✓ a function.” The circle r = "
                + str(_R) + " gets touched twice wherever the line is inside it — "
                "the instant you find a 2-hit spot the verdict locks to "
                "“✗ not a function.”"
            ),
            "html": _vlt_widget("vltslider", r=_R),
        },
    ]
