"""Generate the HTML textbook from the unit .md prose + SSOT + bundled figures (build tooling).

The textbook is a *generated presentation layer* over the unit `.md` files (the prose source of
truth) — never a hand-maintained copy — so the tutor and the textbook can never teach different math
(REBUILD_PLAN "Architecture spine", handoff §9). Math renders via KaTeX (the textbook is a normal
website, so a pinned CDN is fine — the no-fetch rule is only for the skill sandbox). Reference codes
become deep-link targets; bundled figure SVGs are embedded inline.

CLI:
  python _verification/build_textbook.py            # (re)generate docs/textbook/
  python _verification/build_textbook.py --check    # verify the committed site is current
"""
import argparse, glob, html as _html, os, re, sys
import markdown as mdlib

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
UNIT_MD = os.path.join(REPO_ROOT, "algebra-1-tutor", "references", "units")
FIG_DIR = os.path.join(REPO_ROOT, "algebra-1-tutor", "figures")
OUT_DIR = os.path.join(REPO_ROOT, "docs", "textbook")
KATEX = "0.16.11"
ANCHOR_RE = re.compile(r"\{#([^}\s]+)\}")
FCODE_RE = re.compile(r"^(?:[1-9]|1[0-2]|A)\.\d+\.f\d+[a-z]?$")


def _ssot():
    sys.path.insert(0, HERE)
    import generate
    return generate.load_ssot()


def _md_path(uid):
    if uid == "A":
        return os.path.join(UNIT_MD, "appendix-statistics.md")
    return glob.glob(os.path.join(UNIT_MD, f"unit-{int(uid):02d}-*.md"))[0]


# --- preprocessing (operates on the raw markdown before conversion) ------------------------------
def _protect_math(text):
    blocks = []
    def repl(m):
        blocks.append(m.group(0))
        return f"\x00M{len(blocks)-1}\x00"
    return re.sub(r"\$\$.*?\$\$", repl, text, flags=re.DOTALL), blocks


def _restore_math(htmltext, blocks):
    for i, b in enumerate(blocks):
        # KaTeX auto-render reads textContent; HTML-escape so '<', '&' in LaTeX survive to the text node
        htmltext = htmltext.replace(f"\x00M{i}\x00", _html.escape(b, quote=False))
    return htmltext


def _id_worked_practice(text):
    """Insert {#code} markers after each Worked-example and Practice-problem number, lesson-aware,
    so they become deep-link targets like the explicit anchors. (In-memory only; not the source.)"""
    lines = text.split("\n")
    spans = [(i, m.group(1)) for i, ln in enumerate(lines)
             for m in [re.match(r"^## Lesson ([0-9A]+\.\d+):", ln)] if m]
    for li, (lstart, lid) in enumerate(spans):
        lend = spans[li + 1][0] if li + 1 < len(spans) else len(lines)
        block, wk, pk, infence = None, 0, 0, False
        for j in range(lstart, lend):
            ln = lines[j]
            if ln.lstrip().startswith("```"):
                infence = not infence; continue
            if infence:
                continue
            if ln.startswith("**Worked example"):
                block = "w"; continue
            if ln.startswith("**Practice problem"):
                block = "p"; continue
            if ln.startswith("**") or ln.startswith("## "):
                block = None; continue
            if block and re.match(r"^\d+\. ", ln):
                if block == "w":
                    wk += 1; code = f"{lid}.w{wk}"
                else:
                    pk += 1; code = f"{lid}.{pk}"
                lines[j] = re.sub(r"^(\d+)\. ", r"\g<0>{#%s} " % code, ln, count=1)
    return "\n".join(lines)


def _convert_anchors(text):
    """Turn {#code} into a visible, linkable refcode badge; embed the bundled SVG for f-codes."""
    out = []
    for ln in text.split("\n"):
        fcodes = [c for c in ANCHOR_RE.findall(ln)
                  if FCODE_RE.match(c) and os.path.exists(os.path.join(FIG_DIR, c + ".svg"))]
        ln = ANCHOR_RE.sub(
            lambda m: f'<a class="refcode" id="{m.group(1)}" href="#{m.group(1)}">{m.group(1)}</a>', ln)
        out.append(ln)
        for c in fcodes:
            svg = open(os.path.join(FIG_DIR, c + ".svg"), encoding="utf-8").read().strip()
            out += ["", f'<figure class="fig" id="fig-{c}">{svg}<figcaption><b>Figure {c}</b></figcaption></figure>', ""]
    return "\n".join(out)


_LIST_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s")
_BQ_LIST_RE = re.compile(r"^>\s*(?:[-*+]|\d+\.)\s")


def _ensure_list_blank_lines(text):
    """python-markdown needs a blank line before a list. The unit sources glue lists directly under
    a label (e.g. '**New terms:**' then '- ...'), so insert a blank before the first item of each
    list group. Fence-aware (never edits inside ``` blocks); handles blockquote lists with a '>' line."""
    out, prev, infence = [], "", False
    for ln in text.split("\n"):
        if ln.lstrip().startswith("```"):
            infence = not infence
            out.append(ln); prev = ln; continue
        if not infence:
            if _BQ_LIST_RE.match(ln):
                if prev.startswith(">") and prev.strip() != ">" and not _BQ_LIST_RE.match(prev):
                    out.append(">")
            elif _LIST_RE.match(ln) and not ln.startswith(">"):
                if prev.strip() != "" and not _LIST_RE.match(prev):
                    out.append("")
        out.append(ln); prev = ln
    return "\n".join(out)


# --- component blockify: wrap each "**Label:**" lesson part in a semantic, scannable block -------
_LABELS = [
    (re.compile(r'^\*\*Goal:\*\*\s*(.*)$'), "goal", "What you'll learn"),
    (re.compile(r'^\*\*Why it matters:\*\*\s*(.*)$'), "why", ""),
    (re.compile(r'^\*\*New terms:\*\*\s*(.*)$'), "terms", "New words"),
    (re.compile(r'^\*\*Worked examples?:?\*\*\s*(.*)$'), "worked", "Worked example"),
    (re.compile(r'^\*\*Watch for:\*\*\s*(.*)$'), "watch", "A common mix-up"),
    (re.compile(r'^\*\*Check for understanding[^*]*:\*\*\s*(.*)$'), "check", "Check yourself"),
    (re.compile(r'^\*\*Practice problems?:\*\*\s*(.*)$'), "practice", "Practice"),
    (re.compile(r'^\*\*Answer key[^*]*:\*\*\s*(.*)$'), "answers", "Answers"),
    (re.compile(r'^\*\*Teaching arc[^*]*:\*\*\s*(.*)$'), "note", "How this builds"),
    (re.compile(r'^\*\*Visuals to offer:\*\*\s*(.*)$'), "note", "Figures to use"),
    (re.compile(r'^\*\*Consolidate:\*\*\s*(.*)$'), "wrap", "Putting it together"),
    (re.compile(r'^\*\*Mix back in[^*]*:\*\*\s*(.*)$'), "note", "Mix back in"),
    (re.compile(r'^\*\*Looking ahead:\*\*\s*(.*)$'), "note", "Looking ahead"),
    (re.compile(r'^\*\*Threading forward[^*]*:\*\*\s*(.*)$'), "note", "Looking ahead"),
    (re.compile(r'^\*\*Progress Card[^*]*:\*\*\s*(.*)$'), "note", "Progress card"),
]
_KIND_WRAP = {"goal": ("div", "cl-goal"), "why": ("div", "cl-why"), "terms": ("div", "cl-terms"),
              "worked": ("section", "worked"), "watch": ("div", "cl-watch"), "check": ("div", "cl-check"),
              "practice": ("section", "practice"), "wrap": ("div", "cl-wrap"), "note": ("div", "cl-note")}
_STOP_RE = re.compile(r'^(#{1,6}\s|-{3,}\s*$|\*{3,}\s*$)')


def _svg(inner):
    return ('<svg class="cl-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + inner + '</svg>')


# small line-icon glyph per callout kind (currentColor -> inherits the eyebrow colour, theme-aware)
_ICONS = {
    "goal": _svg('<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r="1" fill="currentColor" stroke="none"/>'),
    "terms": _svg('<path d="M12 6.5C9.5 5 6 5 3.5 6.5V18C6 16.5 9.5 16.5 12 18C14.5 16.5 18 16.5 20.5 18V6.5C18 5 14.5 5 12 6.5Z"/><path d="M12 6.5V18"/>'),
    "watch": _svg('<path d="M6 9H17"/><path d="M14.5 6.5 17 9 14.5 11.5"/><path d="M18 15H7"/><path d="M9.5 12.5 7 15 9.5 17.5"/>'),
    "worked": _svg('<path d="M5 19.5V15L15.5 4.5 19.5 8.5 9 19Z"/><path d="M13.5 6.5 17.5 10.5"/>'),
    "practice": _svg('<rect x="4" y="4.5" width="15.5" height="15.5" rx="2.5"/><path d="M7.5 10 9 11.5 12 8.5"/><path d="M14 10H16.5"/><path d="M7.5 15H16.5"/>'),
    "check": _svg('<circle cx="12" cy="12" r="8.5"/><path d="M9.6 9.6a2.6 2.6 0 1 1 3.3 2.5c-.9.3-1.4.9-1.4 1.8"/><circle cx="11.5" cy="16.6" r=".9" fill="currentColor" stroke="none"/>'),
    "note": _svg('<circle cx="12" cy="12" r="8.5"/><path d="M12 11V16"/><circle cx="12" cy="8" r=".9" fill="currentColor" stroke="none"/>'),
    "wrap": _svg('<path d="M12 3.5 3.5 8 12 12.5 20.5 8Z"/><path d="M5.5 11.5 12 15 18.5 11.5"/>'),
}


def _match_label(line):
    for pat, kind, eyebrow in _LABELS:
        m = pat.match(line)
        if m:
            return kind, eyebrow, m.group(1)
    return None


def _blockify(text):
    """Wrap each labelled lesson part in a semantic block so the page reads as scannable cards,
    not a wall of text. Fence-aware; math is already protected to sentinels upstream. Inner
    markdown is processed by the md_in_html extension (markdown="1")."""
    lines = text.split("\n")
    out, i, n, infence = [], 0, len(lines), False
    while i < n:
        ln = lines[i]
        if ln.lstrip().startswith("```"):
            infence = not infence; out.append(ln); i += 1; continue
        if infence:
            out.append(ln); i += 1; continue
        lab = _match_label(ln)
        if not lab:
            out.append(ln); i += 1; continue
        kind, eyebrow, remainder = lab
        body, j, f2 = ([remainder] if remainder.strip() else []), i + 1, False
        while j < n:
            l2 = lines[j]
            if l2.lstrip().startswith("```"):
                f2 = not f2; body.append(l2); j += 1; continue
            if not f2 and (_match_label(l2) or _STOP_RE.match(l2)):
                break
            body.append(l2); j += 1
        while body and body[-1].strip() == "":
            body.pop()
        inner = "\n".join(body).strip("\n")
        if kind == "answers":
            wrapped = ('<details class="answers" markdown="1">\n'
                       '<summary><span class="tw"></span><span class="eyebrow">Answers</span>'
                       '<span class="hint">Try each one yourself first, then open to check.</span></summary>\n'
                       f'<div class="ak-body" markdown="1">\n\n{inner}\n\n</div>\n</details>')
        else:
            tag, cls = _KIND_WRAP[kind]
            eb = f'<span class="eyebrow">{_ICONS.get(kind, "")}{eyebrow}</span>\n\n' if eyebrow else ""
            wrapped = f'<{tag} class="{cls}" markdown="1">\n\n{eb}{inner}\n\n</{tag}>'
        out += ["", wrapped, ""]
        i = j
    return "\n".join(out)


_SUBHEAD_RE = re.compile(r'^\*[^*][^\n]*:\*\s*$')


def _space_subheads(text):
    """Detach an italic group sub-heading (e.g. *Plot & locate:*) from a preceding list item with a
    blank line, so it renders as its own group head instead of being glued into the last problem
    (the 'swallowed subheading' bug). Fence-aware."""
    out, infence = [], False
    for ln in text.split("\n"):
        if ln.lstrip().startswith("```"):
            infence = not infence; out.append(ln); continue
        if not infence and _SUBHEAD_RE.match(ln.strip()) and out and out[-1].strip() != "":
            out.append("")
        out.append(ln)
    return "\n".join(out)


_DIVIDER = ('<div class="ldiv" aria-hidden="true"><i></i>'
            '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.6">'
            '<path d="M12 3.5 20.5 12 12 20.5 3.5 12Z"/></svg><i></i></div>')


def md_to_body(text):
    text, math = _protect_math(text)
    text = _id_worked_practice(text)
    text = _convert_anchors(text)
    text = _space_subheads(text)
    text = _blockify(text)
    text = _ensure_list_blank_lines(text)
    body = mdlib.markdown(text, extensions=["extra", "sane_lists", "toc", "md_in_html"], output_format="html5")
    body = body.replace("<hr />", _DIVIDER).replace("<hr>", _DIVIDER)  # decorative lesson dividers
    return _restore_math(body, math)


# --- HTML template ------------------------------------------------------------------------------
def _page(title, body, prev_link, next_link, subtitle="", *, surface="textbook", hero=None, kicker=""):
    nav = ['<a class="home" href="index.html">Algebra&nbsp;1</a>']
    if prev_link:
        nav.append(f'<a href="{prev_link[0]}">&larr;&nbsp;{prev_link[1]}</a>')
    if next_link:
        nav.append(f'<a href="{next_link[0]}">{next_link[1]}&nbsp;&rarr;</a>')
    navhtml = " &nbsp;·&nbsp; ".join(nav)
    if hero:
        kick = f'<div class="kicker">{_html.escape(kicker)}</div>' if kicker else ""
        lede = f'<p class="lede">{_html.escape(subtitle)}</p>' if subtitle else ""
        head_block = (f'<div class="hero"><div class="hero-text">{kick}'
                      f'<h1>{_html.escape(title)}</h1>{lede}</div>'
                      f'<img class="hero-art" src="{hero}" alt=""></div>')
    else:
        sub = f'<p class="subtitle">{subtitle}</p>' if subtitle else ""
        head_block = f'<h1>{_html.escape(title)}</h1>\n{sub}'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{_html.escape(title)} — Algebra 1</title>
<script>try{{if(localStorage.getItem("a1-theme")==="dark")document.documentElement.classList.add("dark");}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..40,500..600&family=Source+Serif+4:ital,wght@0,400;0,600;1,400&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="textbook.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@{KATEX}/dist/katex.min.css" crossorigin="anonymous">
</head>
<body data-surface="{surface}">
<header class="topbar">
  <nav>{navhtml}</nav>
  <span class="sp"></span>
  <button id="theme" type="button" aria-label="Toggle light or dark theme">◐ Theme</button>
</header>
<main>
{head_block}
{body}
</main>
<footer><p>Generated from the unit source by <code>_verification/build_textbook.py</code>. Math by KaTeX.</p></footer>
<script defer src="https://cdn.jsdelivr.net/npm/katex@{KATEX}/dist/katex.min.js" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@{KATEX}/dist/contrib/auto-render.min.js" crossorigin="anonymous"></script>
<script>
document.addEventListener("DOMContentLoaded", function () {{
  renderMathInElement(document.body, {{delimiters: [{{left: "$$", right: "$$", display: true}}], throwOnError: false}});
  var t = document.getElementById("theme"), root = document.documentElement;
  t.addEventListener("click", function () {{
    root.classList.toggle("dark");
    localStorage.setItem("a1-theme", root.classList.contains("dark") ? "dark" : "light");
  }});
}});
</script>
</body>
</html>
"""


CSS = """/* ============================================================================
   Algebra 1 — visual design language (warm, friendly, calm; for a true beginner).
   One stylesheet shared by the textbook, student guide, tutor guide, and landing.
   Light is the default theme; a refined slate-ink dark is the alternate.
   ============================================================================ */
:root{
  --step--1:.86rem; --step-0:1rem; --step-1:1.18rem; --step-2:1.42rem; --step-3:1.7rem; --step-4:2.05rem; --step-5:2.45rem;
  --lh:1.68; --lh-tight:1.18;
  --measure:64ch; --wide:46rem;
  --serif-math:"STIX Two Text","Cambria Math";
  --radius:16px; --radius-sm:11px;
  --s2:.5rem; --s3:.8rem; --s4:1.15rem; --s5:1.9rem; --s6:2.8rem; --s7:4.2rem;
  /* LIGHT — warm cream (default) */
  --paper:#f8f4ea; --card:#fffdf6; --card-2:#fbf6ec;
  --ink:#2c2820; --ink-soft:#6c6457; --rule:#ece2d0;
  --blue:#2f74b0; --link:#1f6391; --violet:#7d5aa6; --rose:#bb5b4a; --leaf:#3f8f5e; --honey:#a9740f;
  --tint-blue:#eef3f7; --tint-honey:#f6efe0; --tint-rose:#f7ede9; --tint-leaf:#eef4ee;
  --shadow:0 1px 2px rgba(60,48,28,.05), 0 6px 22px -12px rgba(60,48,28,.18);
}
html.dark{
  /* DARK — refined slate ink */
  --paper:#191c20; --card:#22262c; --card-2:#1d2127;
  --ink:#e9e8e3; --ink-soft:#9aa1a9; --rule:#2e333a;
  --blue:#6fb0e8; --link:#8cc2ef; --violet:#c3a4e6; --rose:#ef9b8e; --leaf:#69cf97; --honey:#e0bd76;
  --tint-blue:#1d2530; --tint-honey:#272318; --tint-rose:#2a1f1c; --tint-leaf:#1c2722;
  --shadow:0 1px 2px rgba(0,0,0,.3), 0 10px 28px -16px rgba(0,0,0,.65);
}
/* per-surface paper tint (student guide cooler, tutor guide buff) */
body[data-surface="guide"]{--paper:#eef2f4; --card:#fdfefe; --card-2:#f5f9fb; --rule:#dde7ec; --tint-blue:#e9f1f6;}
body[data-surface="tutor"]{--paper:#f4efe3; --card:#fffdf6; --card-2:#faf4e7; --rule:#e7ddca;}
html.dark body[data-surface="guide"]{--paper:#141a20; --card:#1c232b; --card-2:#18202a;}
html.dark body[data-surface="tutor"]{--paper:#1b1a16; --card:#24221c; --card-2:#1f1d18;}

*{box-sizing:border-box}
html{font-size:112.5%}
body{margin:0; background:var(--paper); color:var(--ink);
  font:var(--step-0)/var(--lh) "Source Serif 4",var(--serif-math),Georgia,serif;
  -webkit-font-smoothing:antialiased; text-rendering:optimizeLegibility; text-wrap:pretty;}
h1,h2,h3{font-family:"Fraunces",var(--serif-math),Georgia,serif; font-weight:600; line-height:var(--lh-tight);
  font-optical-sizing:auto; text-wrap:balance; color:var(--ink);}
h1{font-size:var(--step-4); margin:.2rem 0 .5rem}
h2{font-size:var(--step-2); margin:var(--s7) 0 var(--s4); padding-top:var(--s5); border-top:1px solid var(--rule)}
h3{font-size:var(--step-1); margin:var(--s6) 0 var(--s3)}
p{margin:0 0 var(--s4)}
a{color:var(--link)} a:hover{text-decoration-thickness:2px}
strong,b{font-weight:600; color:var(--ink)}
.imath{font-family:var(--serif-math),"Source Serif 4",serif}
code{font:500 .9em "IBM Plex Mono",ui-monospace,Consolas,monospace; background:var(--card-2); padding:.06em .35em; border-radius:5px}
pre{background:var(--card-2); padding:.85rem 1rem; border-radius:var(--radius-sm); overflow:auto; border:1px solid var(--rule)}
pre code{background:none; padding:0}
hr{border:0; border-top:1px solid var(--rule); margin:var(--s6) 0}
.ldiv{display:flex; align-items:center; gap:1rem; margin:var(--s6) auto}
.ldiv i{height:1px; flex:1; background:var(--rule)}
.ldiv svg{color:var(--honey); opacity:.7; flex:none}
.eyebrow{font-weight:600; font-size:var(--step--1); letter-spacing:.01em; color:var(--ink-soft); display:flex; align-items:center; gap:.42rem; margin-bottom:.4rem}
.cl-ic{width:1.15em; height:1.15em; flex:none}

/* ---- top bar ---- */
.topbar{position:sticky; top:0; z-index:9; display:flex; align-items:center; gap:1.1rem;
  padding:.6rem max(1.2rem,calc((100% - var(--wide))/2)); border-bottom:1px solid var(--rule);
  background:color-mix(in srgb,var(--paper) 86%,transparent); font-size:var(--step--1);}
@supports not (background:color-mix(in srgb,red,blue)){ .topbar{background:var(--paper)} }
.topbar nav{display:flex; gap:.9rem; flex-wrap:wrap; align-items:baseline}
.topbar a{color:var(--link); text-decoration:none} .topbar a:hover{text-decoration:underline}
.topbar .home{font-family:"Fraunces",serif; font-weight:600; font-size:var(--step-0); color:var(--ink)}
.topbar .sp{margin-left:auto}
#theme{background:none; border:1px solid var(--rule); border-radius:999px; color:var(--ink-soft);
  cursor:pointer; padding:.3rem .7rem; font:inherit; font-size:var(--step--1)} #theme:hover{color:var(--ink); border-color:var(--blue)}
@supports ((backdrop-filter:blur(1px)) or (-webkit-backdrop-filter:blur(1px))){
  .topbar{-webkit-backdrop-filter:blur(8px); backdrop-filter:blur(8px)} }

/* ---- layout: calm centered column; special blocks a touch wider ---- */
main{max-width:var(--wide); margin:0 auto; padding:0 1.2rem 5rem}
main > *{max-width:var(--measure); margin-inline:auto}
main > figure.fig, main > .worked, main > .practice, main > .answers, main > .hero,
main > table, main > .katex-display, main > .unit-grid{max-width:var(--wide)}
footer{max-width:var(--measure); margin:var(--s7) auto 0; padding:1.1rem 1.2rem; color:var(--ink-soft);
  font-size:var(--step--1); border-top:1px solid var(--rule)}

/* ---- unit hero ---- */
.hero{margin:var(--s6) auto var(--s5); display:grid; grid-template-columns:1.05fr .95fr; gap:1.6rem; align-items:center}
.hero .kicker{color:var(--blue); font-weight:600; font-size:var(--step--1); letter-spacing:.04em}
.hero h1{margin:.3rem 0 .5rem}
.hero .lede{font-size:var(--step-1); color:var(--ink-soft); margin:0}
.hero-art{width:100%; height:auto; border-radius:var(--radius); box-shadow:var(--shadow); display:block; aspect-ratio:16/9; object-fit:cover}
html.dark .hero-art{filter:brightness(.9) saturate(.92)}
.subtitle{color:var(--ink-soft); font-size:var(--step-1); margin:.2rem auto var(--s5)}
@media (max-width:46rem){ .hero{grid-template-columns:1fr; gap:1rem} .hero-art{order:-1} }

/* ---- reference code: one quiet, friendly identifier ---- */
.refcode{font:500 .8em "IBM Plex Mono",ui-monospace,monospace; color:var(--ink-soft); text-decoration:none;
  background:var(--card-2); border:1px solid var(--rule); border-radius:999px; padding:.08em .55em; white-space:nowrap}
.refcode:hover,.refcode:focus-visible{color:var(--link); border-color:var(--blue)}
:target{scroll-margin-top:5rem}

/* ---- callout family (plain-language labels) ---- */
.cl-goal,.cl-terms,.cl-watch,.cl-note,.cl-check,.cl-wrap{background:var(--card); border-radius:var(--radius);
  padding:1rem 1.25rem; margin:var(--s5) auto; box-shadow:var(--shadow)}
.cl-goal{background:none; box-shadow:none; border-left:3px solid var(--blue); border-radius:0; padding:.3rem 0 .3rem 1.1rem}
.cl-goal .eyebrow{color:var(--blue)} .cl-goal p:last-child{margin-bottom:0} .cl-goal p{font-size:var(--step-1)}
.cl-why{font-size:var(--step-1); color:var(--ink-soft); line-height:1.55; margin:var(--s4) auto var(--s5);
  padding-left:1.1rem; border-left:2px solid var(--rule)}
.cl-terms{border-left:3px solid var(--violet)} .cl-terms .eyebrow{color:var(--violet)}
.cl-watch{background:var(--tint-honey); box-shadow:none; border:1px solid var(--rule)} .cl-watch .eyebrow{color:var(--honey)}
.cl-check .eyebrow{color:var(--leaf)} .cl-note{background:var(--card-2); box-shadow:none; color:var(--ink-soft)}
.cl-wrap{border-left:3px solid var(--leaf)} .cl-wrap .eyebrow{color:var(--leaf)}
.cl-goal p:last-child,.cl-terms :last-child,.cl-watch :last-child,.cl-note :last-child,.cl-check :last-child,.cl-wrap :last-child{margin-bottom:0}
.cl-terms ul,.cl-check ol,.cl-watch ul{margin:0; padding-left:0; list-style:none; display:grid; gap:.6rem}
.cl-terms li,.cl-check li,.cl-watch li{padding-left:0; min-width:0}
.cl-check ol{counter-reset:c}

/* ---- worked example ---- */
.worked{background:var(--card); border-radius:var(--radius); padding:1.1rem 1.35rem; margin:var(--s5) auto;
  box-shadow:var(--shadow); border-left:4px solid var(--blue)}
.worked .eyebrow{color:var(--blue)}
.worked ol,.worked ul{list-style:none; padding-left:0; margin:.4rem 0; display:grid; gap:1rem}
.worked li{padding-top:1rem; border-top:1px solid var(--rule); min-width:0} .worked li:first-child{padding-top:0; border-top:0}
.worked .katex-display{overflow-x:auto; padding:.3rem 0; margin:.5rem 0}
.worked :last-child{margin-bottom:0}
.worked,.answers{position:relative; overflow:hidden}
.worked::after,.answers::after{content:""; position:absolute; right:-22px; bottom:-22px; width:128px; height:128px; pointer-events:none; background:var(--blue); opacity:.05;
  --wm:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><circle cx='12' cy='12' r='10' fill='none' stroke='%23000' stroke-width='1.4'/><circle cx='12' cy='12' r='5.5' fill='none' stroke='%23000' stroke-width='1.4'/></svg>");
  -webkit-mask:var(--wm) center/contain no-repeat; mask:var(--wm) center/contain no-repeat}
.answers::after{background:var(--leaf)}

/* ---- practice / problem set ---- */
.practice{margin:var(--s5) auto}
.practice .eyebrow{color:var(--ink-soft)}
.practice p em{font-style:normal; font-weight:600; font-size:var(--step--1); color:var(--ink-soft)}
.practice > p{margin:1.2rem 0 .5rem}
.practice ol{list-style:none; padding-left:0; margin:0; display:grid; gap:.55rem;
  grid-template-columns:repeat(auto-fill,minmax(min(100%,18rem),1fr))}
.practice li{display:flex; gap:.6rem; align-items:baseline; background:var(--card); border:1px solid var(--rule);
  border-left:2px solid var(--rule); border-radius:var(--radius-sm); padding:.55rem .8rem; box-shadow:var(--shadow); min-width:0}
.practice li:hover{border-color:var(--blue); border-left-width:4px}
.practice li:target{border-color:var(--blue); border-left-width:4px; background:var(--tint-blue)}
.practice li > .refcode{flex:0 0 auto}
.practice li.long{grid-column:1/-1}

/* ---- answer key reveal ---- */
.answers{background:var(--card); border-radius:var(--radius); margin:var(--s5) auto; box-shadow:var(--shadow); overflow:hidden; border:1px solid var(--rule)}
.answers > summary{cursor:pointer; list-style:none; display:flex; align-items:center; gap:.6rem; padding:.9rem 1.25rem}
.answers > summary::-webkit-details-marker{display:none}
.answers .tw{width:.7rem; height:.7rem; border:2px solid var(--leaf); border-top:0; border-right:0;
  transform:rotate(-45deg); transition:transform .2s; flex:0 0 auto; margin-bottom:.12rem}
.answers[open] .tw{transform:rotate(45deg) translate(-1px,-1px)}
.answers summary .eyebrow{color:var(--leaf); margin:0}
.answers .hint{color:var(--ink-soft); font-size:var(--step--1)} .answers[open] .hint{display:none}
.answers .ak-body{padding:.1rem 1.4rem 1.1rem} .answers .ak-body > :last-child{margin-bottom:0}

/* ---- tutor-guide problem card (cross-site consistency) ---- */
.tproblem{background:var(--card); border:1px solid var(--rule); border-radius:var(--radius); padding:1rem 1.25rem; margin:var(--s4) auto; box-shadow:var(--shadow)}
.tproblem > .refcode{display:inline-block; margin-bottom:.5rem}
.tproblem > p{margin:.2rem 0 .6rem}
.tproblem .answers{margin:.5rem 0 0; box-shadow:none}
.tproblem .ans{margin:.7rem 0 0}

/* ---- figure (graph paper belongs here) ---- */
figure.fig{margin:var(--s5) auto; background:var(--card); border-radius:var(--radius); padding:1.1rem 1.1rem .7rem;
  box-shadow:var(--shadow); text-align:center; border:1px solid var(--rule);
  background-image:linear-gradient(var(--rule) 1px,transparent 1px),linear-gradient(90deg,var(--rule) 1px,transparent 1px);
  background-size:22px 22px}
figure.fig svg{max-width:100%; max-height:360px; height:auto; display:block; margin-inline:auto}
figcaption{color:var(--ink-soft); font-size:var(--step--1); margin-top:.6rem; text-align:left}
figcaption b,figcaption strong{color:var(--blue); font-weight:600}
html.dark figure.fig [stroke="#888"]{stroke:#7c8590} html.dark figure.fig text[fill="#888"]{fill:#9aa3b0}
html.dark figure.fig text[fill="#c0392b"],html.dark figure.fig [fill="#c0392b"]{fill:#ef9b8e}
html.dark figure.fig text[fill="#2980b9"],html.dark figure.fig [fill="#2980b9"]:not(line){fill:#6fb0e8}
html.dark figure.fig text[fill="#27ae60"]{fill:#69cf97} html.dark figure.fig text[fill="#8e44ad"]{fill:#c3a4e6}
html.dark figure.fig line[stroke="#2980b9"]{stroke:#6fb0e8} html.dark figure.fig line[stroke="#8e44ad"]{stroke:#c3a4e6}

/* ---- objectives blockquote & tables ---- */
blockquote{margin:var(--s5) auto; padding:1rem 1.25rem; background:var(--tint-blue); border:1px solid var(--rule);
  border-left:3px solid var(--blue); border-radius:var(--radius); color:var(--ink)}
blockquote :last-child{margin-bottom:0}
table{border-collapse:collapse; width:100%; margin:var(--s4) auto; font-size:.95em; background:var(--card); border-radius:var(--radius-sm); overflow:hidden}
th,td{border:1px solid var(--rule); padding:.45rem .65rem; text-align:left} th{background:var(--card-2); font-family:"IBM Plex Mono",monospace; font-size:.85em; font-weight:600}
.katex-display{overflow-x:auto; overflow-y:hidden; padding:.2rem 0; max-width:100%}

/* ---- landing / index catalogs ---- */
ul.units{list-style:none; padding:0; margin:var(--s5) auto; display:grid; gap:.9rem;
  grid-template-columns:repeat(auto-fill,minmax(min(100%,20rem),1fr))}
ul.units li{margin:0; background:var(--card); border:1px solid var(--rule); border-radius:var(--radius); padding:1rem 1.15rem; box-shadow:var(--shadow)}
ul.units a{text-decoration:none; font-size:var(--step-1)} ul.units a b{font-family:"Fraunces",serif}
.u{color:var(--ink-soft); font-size:.92em}
section.ug{margin:var(--s4) auto; background:var(--card); border:1px solid var(--rule); border-radius:var(--radius); padding:1rem 1.25rem; box-shadow:var(--shadow)}
section.ug h3{margin:.1rem 0 .4rem} section.ug :last-child{margin-bottom:0}
.toc{background:var(--card); border:1px solid var(--rule); border-radius:var(--radius); padding:.8rem 1.15rem}

/* ---- motion (reduced-motion safe) ---- */
@media (prefers-reduced-motion:no-preference){
  .practice li,.worked,figure.fig,#theme,ul.units li,.refcode{transition:border-color .15s ease, box-shadow .15s ease, color .15s ease, transform .15s ease}
  ul.units li:hover{transform:translateY(-1px)}
  :target{animation:flash 1.4s ease-out 1} @keyframes flash{0%{background:var(--tint-honey)}100%{background:transparent}}
}

/* ---- print (courtesy) ---- */
@media print{
  .topbar{position:static} #theme{display:none} a{color:inherit; text-decoration:none}
  body,figure.fig{background-image:none}
  .answers[open] .ak-body, details > *{display:revert} details{display:block} .answers summary{display:none}
  .worked,.practice li,figure.fig,blockquote,ul.units li{break-inside:avoid; box-shadow:none}
}
"""


def _index_html(ssot):
    items = []
    for u in ssot.units:
        href = ("appendix.html" if u.id == "A" else f"unit-{int(u.id):02d}.html")
        opt = " (optional)" if u.optional else ""
        items.append(f'<li><a href="{href}"><b>Unit {u.id}</b> · {_html.escape(u.title)}</a>{opt}'
                     f'<br><span class="u">{_html.escape(u.description)}</span></li>')
    body = ('<p class="subtitle">A full Algebra 1 textbook, generated from the tutor\'s lesson source. '
            'Every worked example, definition, and figure has a reference code you can quote to the tutor.</p>'
            '<ul class="units">' + "\n".join(items) + "</ul>")
    return _page("Algebra 1 — Contents", body, None, None)


_UNIT_HERO = {"1": "numberline", "2": "balance", "3": "steps", "4": "machine", "5": "lines",
              "6": "modeling", "7": "systems", "8": "inequality", "9": "exponential", "10": "areamodel",
              "11": "factoring", "12": "arch", "A": "dots"}


def _unit_pages(ssot):
    order = ssot.units
    pages = {}
    for i, u in enumerate(order):
        fname = ("appendix.html" if u.id == "A" else f"unit-{int(u.id):02d}.html")
        body = md_to_body(open(_md_path(u.id), encoding="utf-8").read())
        # strip the leading <h1> (the template adds its own) and use the SSOT title
        body = re.sub(r"^\s*<h1[^>]*>.*?</h1>", "", body, count=1, flags=re.DOTALL)
        prev_u = order[i - 1] if i > 0 else None
        next_u = order[i + 1] if i + 1 < len(order) else None
        pl = ((("appendix.html" if prev_u.id == "A" else f"unit-{int(prev_u.id):02d}.html"),
               f"Unit {prev_u.id}") if prev_u else None)
        nl = ((("appendix.html" if next_u.id == "A" else f"unit-{int(next_u.id):02d}.html"),
               f"Unit {next_u.id}") if next_u else None)
        kicker = "Appendix" if str(u.id) == "A" else f"Unit {u.id}"
        hero = f"../assets/{_UNIT_HERO.get(str(u.id), 'lines')}.jpg"
        pages[fname] = _page(u.title, body, pl, nl, u.description, hero=hero, kicker=kicker)
    return pages


def build_site(ssot):
    files = {"index.html": _index_html(ssot), "textbook.css": CSS}
    files.update(_unit_pages(ssot))
    return files


def generate():
    os.makedirs(OUT_DIR, exist_ok=True)
    files = build_site(_ssot())
    for name, content in files.items():
        open(os.path.join(OUT_DIR, name), "w", encoding="utf-8", newline="\n").write(content)
    return len(files)


def check():
    files = build_site(_ssot())
    issues = []
    for name, content in files.items():
        p = os.path.join(OUT_DIR, name)
        if not os.path.exists(p):
            issues.append(f"{name}: missing (run build_textbook.py)")
        elif open(p, encoding="utf-8").read() != content:
            issues.append(f"{name}: stale (run build_textbook.py)")
    return issues


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if a.check:
        iss = check()
        if iss:
            print("FAIL:\n  " + "\n  ".join(iss)); return 1
        print(f"textbook: {len(build_site(_ssot()))} files current."); return 0
    n = generate(); print(f"generated {n} textbook files -> {os.path.relpath(OUT_DIR, REPO_ROOT)}/"); return 0


if __name__ == "__main__":
    sys.exit(main())
