"""Assemble a review gallery of candidate visual elements (build tooling, NOT a CI gate, NOT shipped).

Imports every self-contained module in _verification/viz/*.py (each exposes TITLE/KIND/BLURB/LESSONS
and a samples() -> [{"caption","html"}]) and writes a single review page at docs/preview/index.html,
reusing the textbook stylesheet + KaTeX + dark toggle. Defensive: a broken module is reported inline
rather than failing the whole page.

  python _verification/build_gallery.py
"""
import glob, html as _html, importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
VIZ_DIR = os.path.join(HERE, "viz")
OUT_DIR = os.path.join(REPO_ROOT, "docs", "preview")
KATEX = "0.16.11"

# Logical display order (deterministic SVG, then HTML/CSS, then interactive); unknowns appended.
ORDER = ["area_models", "anatomy", "example_graphs", "bar_models", "double_number_lines",
         "stats_charts", "flowcharts", "concept_map", "annotated_examples", "reference_cards",
         "interactive_graph", "interactive_equation"]


def _esc(s):
    return _html.escape(str(s), quote=False)


def _load():
    mods = {}
    for fp in sorted(glob.glob(os.path.join(VIZ_DIR, "*.py"))):
        name = os.path.splitext(os.path.basename(fp))[0]
        if name.startswith("_"):
            continue
        try:
            spec = importlib.util.spec_from_file_location("viz_" + name, fp)
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            mods[name] = m
        except Exception as e:  # noqa: BLE001
            mods[name] = e
    return mods


def _ordered(names):
    return [n for n in ORDER if n in names] + sorted(n for n in names if n not in ORDER)


def _section(name, m):
    if isinstance(m, Exception):
        return f'<section id="{name}"><h2>{_esc(name)}</h2><p class="gx-err">module failed to import: {_esc(m)}</p></section>'
    title = getattr(m, "TITLE", name)
    kind = getattr(m, "KIND", "")
    blurb = getattr(m, "BLURB", "")
    lessons = getattr(m, "LESSONS", []) or []
    try:
        samples = list(m.samples())
    except Exception as e:  # noqa: BLE001
        return f'<section id="{name}"><h2>{_esc(title)}</h2><p class="gx-err">samples() failed: {_esc(e)}</p></section>'
    cards = []
    for i, s in enumerate(samples):
        cap = _esc(s.get("caption", ""))
        cards.append(f'<figure class="gx"><div class="gx-art">{s.get("html", "")}</div>'
                     f'<figcaption>{cap}</figcaption></figure>')
    meta = (f'<p class="gx-meta"><span class="gx-kind">{_esc(kind)}</span>'
            + (f' &middot; serves {_esc(", ".join(map(str, lessons)))}' if lessons else "") + "</p>")
    return (f'<section id="{name}"><h2>{_esc(title)}</h2>{meta}'
            f'<p class="gx-blurb">{_esc(blurb)}</p><div class="gx-grid">{"".join(cards)}</div></section>')


GALLERY_CSS = """
.gx-wrap{display:grid; grid-template-columns:15rem minmax(0,1fr); align-items:start; gap:0}
.gx-nav{position:sticky; top:3.2rem; align-self:start; max-height:calc(100vh - 3.4rem); overflow:auto;
  padding:1.1rem .8rem 3rem; border-right:1px solid var(--rule); font-size:var(--step--1)}
.gx-nav a{display:block; color:var(--ink-soft); text-decoration:none; padding:.3rem .5rem; border-radius:8px; line-height:1.3}
.gx-nav a:hover{background:var(--card-2); color:var(--ink)}
.gx-main{min-width:0; max-width:64rem; margin:0 auto; padding:1.2rem 1.6rem 5rem}
.gx-main > section{margin:0 0 var(--s7); padding-top:var(--s5); border-top:1px solid var(--rule)}
.gx-main > section:first-of-type{border-top:0}
.gx-meta{margin:.2rem 0 .3rem; font-size:var(--step--1); color:var(--ink-soft)}
.gx-kind{font:600 .8em "IBM Plex Mono",monospace; background:var(--tint-blue); color:var(--link);
  border:1px solid var(--rule); border-radius:999px; padding:.1em .6em}
.gx-blurb{color:var(--ink-soft); margin:0 0 var(--s4); max-width:62ch}
.gx-grid{display:grid; gap:1.2rem; grid-template-columns:repeat(auto-fill,minmax(min(100%,22rem),1fr))}
.gx{margin:0; background:var(--card); border:1px solid var(--rule); border-radius:var(--radius);
  padding:1rem 1rem .7rem; box-shadow:var(--shadow); overflow:hidden}
.gx-art{display:flex; align-items:center; justify-content:center; min-height:8rem; overflow:auto}
.gx-art svg{max-width:100%; height:auto}
.gx figcaption{margin-top:.6rem; font-size:var(--step--1); color:var(--ink-soft); text-align:center}
.gx-err{color:var(--rose); font:600 .9em "IBM Plex Mono",monospace}
.gx input[type=range]{width:100%}
@media (max-width:60rem){ .gx-wrap{grid-template-columns:1fr} .gx-nav{display:none} }
"""


def _page(nav, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Visual elements — candidates for review</title>
<script>try{{if(localStorage.getItem("a1-theme")==="dark")document.documentElement.classList.add("dark");}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..40,500..600&family=Source+Serif+4:ital,wght@0,400;0,600;1,400&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../textbook/textbook.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@{KATEX}/dist/katex.min.css" crossorigin="anonymous">
<style>{GALLERY_CSS}</style>
</head>
<body data-surface="textbook">
<header class="topbar">
  <a class="home" href="#">Algebra 1 — visual elements</a>
  <span class="sp"></span>
  <button id="theme" type="button" aria-label="Toggle light or dark theme">◐&nbsp;Theme</button>
</header>
<div class="gx-wrap">
<nav class="gx-nav" aria-label="Sections"><strong>Candidates</strong>{nav}</nav>
<main class="gx-main">
<p class="subtitle">Each candidate visual element with sample renderings. Toggle the theme to check dark mode; interactive widgets are live. Nothing here is wired into the textbook yet — this page is for deciding what goes in.</p>
{body}
</main>
</div>
<script defer src="https://cdn.jsdelivr.net/npm/katex@{KATEX}/dist/katex.min.js" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@{KATEX}/dist/contrib/auto-render.min.js" crossorigin="anonymous"></script>
<script>
document.addEventListener("DOMContentLoaded", function () {{
  if (window.renderMathInElement) renderMathInElement(document.body, {{delimiters:[{{left:"$$",right:"$$",display:true}}], throwOnError:false}});
  var _sec=(location.hash||"").slice(1);
  if(_sec){{ setTimeout(function(){{ var el=document.getElementById(_sec); if(el) el.scrollIntoView({{block:"start"}}); }}, 350); }}
  var root=document.documentElement, t=document.getElementById("theme");
  t.addEventListener("click", function(){{ root.classList.toggle("dark"); try{{localStorage.setItem("a1-theme", root.classList.contains("dark")?"dark":"light");}}catch(e){{}} }});
}});
</script>
</body>
</html>
"""


def build():
    mods = _load()
    names = _ordered(list(mods))
    nav = "".join(
        f'<a href="#{n}">{_esc(getattr(mods[n], "TITLE", n) if not isinstance(mods[n], Exception) else n)}</a>'
        for n in names)
    body = "".join(_section(n, mods[n]) for n in names)
    os.makedirs(OUT_DIR, exist_ok=True)
    open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8", newline="\n").write(_page(nav, body))
    # one standalone page per section (same dir, so the ../textbook/textbook.css path holds) — used
    # to screenshot each candidate cleanly from the top of the viewport.
    for n in names:
        open(os.path.join(OUT_DIR, f"_sec_{n}.html"), "w", encoding="utf-8", newline="\n").write(
            _page(nav, _section(n, mods[n])))
    bad = [n for n in names if isinstance(mods[n], Exception)]
    return names, bad


def main():
    names, bad = build()
    print(f"gallery: {len(names)} modules -> docs/preview/index.html"
          + (f"  (FAILED import: {', '.join(bad)})" if bad else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
