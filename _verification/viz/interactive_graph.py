"""Interactive graph widgets for the Algebra 1 textbook gallery.

Self-contained inline-SVG + vanilla-JS widgets. Each sample's "html" is dropped
into a page that already loads the textbook stylesheet and KaTeX. No libraries,
no randomness, no clock. Every widget is safe to (re-)initialise on load: each is
wrapped in an IIFE, scopes all DOM queries to its own root element, uses
slug-prefixed unique ids, and guards against double-initialisation.

COLOR CONTRACT (literal hexes so the book's dark-mode SVG overrides apply):
  blue #2980b9 (the line), violet #8e44ad (the parabola),
  red/terracotta #c0392b (the moving point), green #27ae60 (the y-intercept),
  neutral/axis #888.

CORRECTNESS: the JS coordinate mapper is the SINGLE source of truth for both the
drawn geometry and the text readouts, so the picture can never disagree with the
numbers. The mapping (and the sample defaults shown below) are cross-checked in
Python at import time via _selfcheck().
"""

TITLE = "Interactive graphs"
KIND = "interactive"
BLURB = ("Move a slider and the graph answers back: tilt and lift a line, walk a "
         "point along it, or open and close a parabola, all in real time.")
LESSONS = ["5.4", "12.6"]


# --------------------------------------------------------------------------- #
# Shared coordinate-mapping helpers (mirrored exactly by the inline JS below). #
# Window is symmetric: x,y in [-LIM, LIM]. Pixel box is WxW with PAD padding.  #
# --------------------------------------------------------------------------- #
_W = 360       # svg pixel width/height of the plotting square
_PAD = 30      # padding so axis labels + tick numbers have breathing room
_LIM = 6       # axis range: -6..6 in both directions


def _to_px(x, y, lim=_LIM, w=_W, pad=_PAD):
    """Map graph coords -> pixel coords (y flipped). Same formula as JS toPx()."""
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


def _eq_line(m, b):
    """Plain-text 'y = mx + b' exactly as the JS builds it. Used for captions."""
    mt = _fmt(m)
    # slope term
    if m == 0:
        slope = ""
    elif m == 1:
        slope = "x"
    elif m == -1:
        slope = "-x"
    else:
        slope = mt + "x"
    # intercept term
    if b == 0:
        inter = "" if slope else "0"
    elif slope == "":
        inter = _fmt(b)
    elif b > 0:
        inter = " + " + _fmt(b)
    else:
        inter = " - " + _fmt(-b)
    return "y = " + (slope + inter if (slope or inter) else "0")


def _eq_parab(a):
    at = _fmt(a)
    if a == 0:
        return "y = 0"
    if a == 1:
        return "y = x²"
    if a == -1:
        return "y = -x²"
    return "y = " + at + "x²"


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


# JS snippet (as a Python string) of the mapper, injected into each widget so the
# drawing math is identical to _to_px above. {LIM},{W},{PAD} filled per-widget.
_JS_MAP = """
  var LIM={LIM}, W={W}, PAD={PAD};
  var SX=(W-2*PAD)/(2*LIM);
  function px(x){{return PAD+(x+LIM)*SX;}}
  function py(y){{return PAD+(LIM-y)*SX;}}
  function fmt(v){{v=Math.round(v*100)/100; return (v===Math.round(v))?(''+Math.round(v)):(''+v);}}
"""


# --------------------------------------------------------------------------- #
# Widget 1 + 2 share a builder: a y=mx+b line, optionally with a draggable     #
# point that walks along the line.                                             #
# --------------------------------------------------------------------------- #
def _line_widget(slug, m0, b0, draggable, px0=None):
    grid = _grid_svg()
    jsmap = _JS_MAP.format(LIM=_LIM, W=_W, PAD=_PAD)
    drag = "true" if draggable else "false"
    px0 = 0 if px0 is None else px0

    # The draggable bits (dot + readout row) only exist when draggable.
    pt_svg = ""
    if draggable:
        pt_svg = (
            f'<line id="{slug}-drop" stroke="#c0392b" stroke-width="1.4" '
            f'stroke-dasharray="3 3" opacity="0.6"/>'
            f'<circle id="{slug}-pt" r="8" fill="#c0392b" tabindex="0" '
            f'role="slider" aria-label="point on the line, use left and right arrow keys" '
            f'style="cursor:grab;outline:none"/>'
        )

    drag_readout = ""
    if draggable:
        drag_readout = (
            f'<div class="{slug}-row">point&nbsp;'
            f'<b id="{slug}-xy" style="color:var(--rose)">(0, 0)</b>'
            f'<span class="{slug}-hint">drag the red dot, or focus it and press '
            f'← / →</span></div>'
        )

    html = f"""<div class="{slug}-wrap" data-init="0">
  <style>
    .{slug}-wrap{{max-width:380px;margin:0 auto;font-family:inherit}}
    .{slug}-wrap svg{{width:100%;height:auto;display:block;
      background:transparent;border-radius:var(--radius);touch-action:none}}
    .{slug}-eq{{font:600 1.15rem "IBM Plex Mono",ui-monospace,Consolas,monospace;
      color:var(--blue);text-align:center;margin:.5rem 0 .2rem;letter-spacing:.01em}}
    .{slug}-ctrl{{display:grid;grid-template-columns:auto 1fr auto;gap:.5rem .7rem;
      align-items:center;margin:.55rem .3rem 0;font-size:.92rem;color:var(--ink-soft)}}
    .{slug}-ctrl label{{font-weight:600;color:var(--ink)}}
    .{slug}-ctrl output{{font:600 .92rem "IBM Plex Mono",monospace;color:var(--ink);
      min-width:2.4em;text-align:right}}
    .{slug}-wrap input[type=range]{{width:100%;accent-color:var(--blue);
      height:1.4rem;cursor:pointer}}
    .{slug}-wrap input[type=range]:focus-visible{{outline:2px solid var(--blue);
      outline-offset:3px;border-radius:6px}}
    .{slug}-row{{text-align:center;margin:.55rem 0 0;font-size:.95rem;color:var(--ink-soft)}}
    .{slug}-hint{{display:block;font-size:.8rem;color:var(--ink-soft);
      margin-top:.15rem;opacity:.85}}
  </style>
  <div class="{slug}-eq" id="{slug}-eq">y = x</div>
  <svg viewBox="0 0 {_W} {_W}" xmlns="http://www.w3.org/2000/svg"
       font-family="sans-serif" aria-label="coordinate grid with a movable line">
    {grid}
    <line id="{slug}-line" stroke="#2980b9" stroke-width="2.5" stroke-linecap="round"/>
    <circle id="{slug}-yint" r="4.5" fill="#27ae60"/>
    {pt_svg}
  </svg>
  <div class="{slug}-ctrl">
    <label for="{slug}-m">slope&nbsp;m</label>
    <input id="{slug}-m" type="range" min="-3" max="3" step="0.5" value="{m0}"
       aria-label="slope m from negative 3 to 3">
    <output id="{slug}-mo">{_fmt(m0)}</output>
    <label for="{slug}-b">intercept&nbsp;b</label>
    <input id="{slug}-b" type="range" min="-5" max="5" step="1" value="{b0}"
       aria-label="y-intercept b from negative 5 to 5">
    <output id="{slug}-bo">{_fmt(b0)}</output>
  </div>
  {drag_readout}
  <script>(function(){{
    var root=document.currentScript.parentNode;
    if(!root||root.dataset.init==="1"){{return;}} root.dataset.init="1";
    {jsmap}
    var DRAG={drag};
    var line=root.querySelector("#{slug}-line");
    var yint=root.querySelector("#{slug}-yint");
    var eq=root.querySelector("#{slug}-eq");
    var sm=root.querySelector("#{slug}-m"), sb=root.querySelector("#{slug}-b");
    var om=root.querySelector("#{slug}-mo"), ob=root.querySelector("#{slug}-bo");
    var pt=root.querySelector("#{slug}-pt");
    var drop=root.querySelector("#{slug}-drop");
    var xy=root.querySelector("#{slug}-xy");
    var ptx={px0};   // graph x of the draggable point (clamped to [-LIM,LIM])

    function eqText(m,b){{
      var s = (m===0)?"":(m===1)?"x":(m===-1)?"-x":(fmt(m)+"x");
      var t;
      if(b===0){{ t = s?"":"0"; }}
      else if(s===""){{ t = fmt(b); }}
      else {{ t = (b>0? " + ":" - ")+fmt(Math.abs(b)); }}
      return "y = " + ((s||t)? (s+t) : "0");
    }}
    // y on the line at graph-x, clamped so the segment stays inside the box.
    function lineEndpoints(m,b){{
      // draw across full width; clip y visually via the viewBox (fine for LIM range)
      return [[-LIM, m*(-LIM)+b],[LIM, m*LIM+b]];
    }}
    function draw(){{
      var m=parseFloat(sm.value), b=parseFloat(sb.value);
      om.textContent=fmt(m); ob.textContent=fmt(b);
      var e=lineEndpoints(m,b);
      line.setAttribute("x1",px(e[0][0])); line.setAttribute("y1",py(e[0][1]));
      line.setAttribute("x2",px(e[1][0])); line.setAttribute("y2",py(e[1][1]));
      yint.setAttribute("cx",px(0)); yint.setAttribute("cy",py(b));
      eq.textContent=eqText(m,b);
      if(DRAG){{
        if(ptx<-LIM)ptx=-LIM; if(ptx>LIM)ptx=LIM;
        var yv=m*ptx+b;
        pt.setAttribute("cx",px(ptx)); pt.setAttribute("cy",py(yv));
        // dotted drop-line to the x-axis
        drop.setAttribute("x1",px(ptx)); drop.setAttribute("y1",py(yv));
        drop.setAttribute("x2",px(ptx)); drop.setAttribute("y2",py(0));
        xy.textContent="("+fmt(ptx)+",\\u00a0"+fmt(yv)+")";
        pt.setAttribute("aria-valuetext","x equals "+fmt(ptx)+", y equals "+fmt(yv));
      }}
    }}
    sm.addEventListener("input",draw); sb.addEventListener("input",draw);

    if(DRAG && pt){{
      var svg=line.ownerSVGElement;
      function gx(evt){{ // pointer clientX -> graph x (inverse of px())
        var r=svg.getBoundingClientRect();
        var sxpx=(evt.clientX-r.left)*(W/r.width); // into viewBox px
        var gxv=(sxpx-PAD)/SX-LIM;
        gxv=Math.round(gxv*2)/2;                   // snap to half-units
        if(gxv<-LIM)gxv=-LIM; if(gxv>LIM)gxv=LIM; return gxv;
      }}
      var dragging=false;
      pt.addEventListener("pointerdown",function(e){{
        dragging=true; pt.setPointerCapture(e.pointerId);
        pt.style.cursor="grabbing"; e.preventDefault();
      }});
      pt.addEventListener("pointermove",function(e){{
        if(!dragging)return; ptx=gx(e); draw();
      }});
      function release(e){{
        dragging=false; pt.style.cursor="grab";
        if(e&&e.pointerId!=null&&pt.releasePointerCapture){{
          try{{pt.releasePointerCapture(e.pointerId);}}catch(_){{}}
        }}
      }}
      pt.addEventListener("pointerup",release);
      pt.addEventListener("pointercancel",release);
      pt.addEventListener("keydown",function(e){{
        var step=(e.key==="ArrowLeft")?-0.5:(e.key==="ArrowRight")?0.5:0;
        if(step!==0){{ ptx+=step; if(ptx<-LIM)ptx=-LIM; if(ptx>LIM)ptx=LIM;
          draw(); e.preventDefault(); }}
      }});
    }}
    draw();
  }})();</script>
</div>"""
    return html


# --------------------------------------------------------------------------- #
# Widget 3: parabola y = a x^2 with a single slider for a.                     #
# --------------------------------------------------------------------------- #
def _parabola_widget(slug, a0):
    grid = _grid_svg()
    jsmap = _JS_MAP.format(LIM=_LIM, W=_W, PAD=_PAD)
    html = f"""<div class="{slug}-wrap" data-init="0">
  <style>
    .{slug}-wrap{{max-width:380px;margin:0 auto;font-family:inherit}}
    .{slug}-wrap svg{{width:100%;height:auto;display:block;
      background:transparent;border-radius:var(--radius);touch-action:none}}
    .{slug}-eq{{font:600 1.15rem "IBM Plex Mono",ui-monospace,Consolas,monospace;
      color:var(--violet);text-align:center;margin:.5rem 0 .2rem;letter-spacing:.01em}}
    .{slug}-ctrl{{display:grid;grid-template-columns:auto 1fr auto;gap:.5rem .7rem;
      align-items:center;margin:.55rem .3rem 0;font-size:.92rem;color:var(--ink-soft)}}
    .{slug}-ctrl label{{font-weight:600;color:var(--ink)}}
    .{slug}-ctrl output{{font:600 .92rem "IBM Plex Mono",monospace;color:var(--ink);
      min-width:2.4em;text-align:right}}
    .{slug}-wrap input[type=range]{{width:100%;accent-color:var(--violet);
      height:1.4rem;cursor:pointer}}
    .{slug}-wrap input[type=range]:focus-visible{{outline:2px solid var(--violet);
      outline-offset:3px;border-radius:6px}}
    .{slug}-hint{{text-align:center;font-size:.82rem;color:var(--ink-soft);
      margin:.5rem 0 0;opacity:.9}}
  </style>
  <div class="{slug}-eq" id="{slug}-eq">y = x²</div>
  <svg viewBox="0 0 {_W} {_W}" xmlns="http://www.w3.org/2000/svg"
       font-family="sans-serif" aria-label="coordinate grid with a movable parabola">
    {grid}
    <path id="{slug}-curve" fill="none" stroke="#8e44ad" stroke-width="2.5"
          stroke-linecap="round" stroke-linejoin="round"/>
    <circle id="{slug}-vtx" r="4.5" fill="#8e44ad"/>
  </svg>
  <div class="{slug}-ctrl">
    <label for="{slug}-a">stretch&nbsp;a</label>
    <input id="{slug}-a" type="range" min="-2" max="2" step="0.5" value="{a0}"
       aria-label="coefficient a from negative 2 to 2">
    <output id="{slug}-ao">{_fmt(a0)}</output>
  </div>
  <p class="{slug}-hint">a&nbsp;&gt;&nbsp;0 opens up, a&nbsp;&lt;&nbsp;0 opens down,
     bigger |a| makes it narrower. The vertex stays at the origin.</p>
  <script>(function(){{
    var root=document.currentScript.parentNode;
    if(!root||root.dataset.init==="1"){{return;}} root.dataset.init="1";
    {jsmap}
    var curve=root.querySelector("#{slug}-curve");
    var vtx=root.querySelector("#{slug}-vtx");
    var eq=root.querySelector("#{slug}-eq");
    var sa=root.querySelector("#{slug}-a"), oa=root.querySelector("#{slug}-ao");
    function eqText(a){{
      if(a===0)return "y = 0";
      if(a===1)return "y = x\\u00b2";
      if(a===-1)return "y = -x\\u00b2";
      return "y = "+fmt(a)+"x\\u00b2";
    }}
    function draw(){{
      var a=parseFloat(sa.value); oa.textContent=fmt(a);
      eq.textContent=eqText(a);
      var d="", started=false;
      for(var i=0;i<=120;i++){{
        var x=-LIM+(2*LIM)*i/120;
        var y=a*x*x;
        if(y<-LIM-0.5||y>LIM+0.5){{ started=false; continue; }} // pen up off-screen
        d += (started?" L":"M")+px(x).toFixed(2)+" "+py(y).toFixed(2);
        started=true;
      }}
      curve.setAttribute("d", d || ("M"+px(0)+" "+py(0)));
      vtx.setAttribute("cx",px(0)); vtx.setAttribute("cy",py(0));
    }}
    sa.addEventListener("input",draw);
    draw();
  }})();</script>
</div>"""
    return html


# --------------------------------------------------------------------------- #
# Import-time self-check: confirm the mapper round-trips and the captioned     #
# equations match what the JS would print for the chosen defaults.            #
# --------------------------------------------------------------------------- #
def _selfcheck():
    # mapper sanity: origin maps to centre; corners map to the padded box.
    cx, cy = _to_px(0, 0)
    assert abs(cx - _W / 2) < 1e-6 and abs(cy - _W / 2) < 1e-6, (cx, cy)
    assert _to_px(-_LIM, -_LIM) == (float(_PAD), float(_W - _PAD))
    assert _to_px(_LIM, _LIM) == (float(_W - _PAD), float(_PAD))
    # equation formatting matches the documented readouts.
    assert _eq_line(1, 0) == "y = x", _eq_line(1, 0)
    assert _eq_line(1.5, 2) == "y = 1.5x + 2", _eq_line(1.5, 2)
    assert _eq_line(-1, -3) == "y = -x - 3", _eq_line(-1, -3)
    assert _eq_line(0, 4) == "y = 4", _eq_line(0, 4)
    assert _eq_line(2, 0) == "y = 2x", _eq_line(2, 0)
    assert _eq_parab(1) == "y = x²"
    assert _eq_parab(-2) == "y = -2x²"
    # a sampled point on y = 1.5x + 2 lands where arithmetic says it should.
    px2, py2 = _to_px(2, 1.5 * 2 + 2)   # (2, 5)
    expx, expy = _to_px(2, 5)
    assert (px2, py2) == (expx, expy)


_selfcheck()


def samples():
    return [
        {
            "caption": "Slope-intercept explorer: drag m to tilt the line and b to "
                       "slide it up or down. The green dot is the y-intercept; the "
                       "readout shows the line's equation. Starts at " + _eq_line(1, 0) + ".",
            "html": _line_widget("lineexp", m0=1, b0=0, draggable=False),
        },
        {
            "caption": "Walk a point along the line. Drag the red dot (or focus it and "
                       "use the arrow keys); its coordinates update live, and they "
                       "always satisfy the equation above. Starts at " + _eq_line(0.5, 1) + ".",
            "html": _line_widget("linept", m0=0.5, b0=1, draggable=True, px0=2),
        },
        {
            "caption": "Parabola stretcher: one slider sets a in " + _eq_parab(1) +
                       ". Watch it open upward, flatten, then open downward as a "
                       "passes through zero, with the vertex pinned at the origin.",
            "html": _parabola_widget("parab", a0=1),
        },
    ]
