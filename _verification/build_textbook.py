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
            lambda m: f'<a class="refcode" id="{m.group(1)}" href="#{m.group(1)}">#{m.group(1)}</a>', ln)
        out.append(ln)
        for c in fcodes:
            svg = open(os.path.join(FIG_DIR, c + ".svg"), encoding="utf-8").read().strip()
            out += ["", f'<figure class="fig" id="fig-{c}">{svg}<figcaption>Figure {c}</figcaption></figure>', ""]
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


def md_to_body(text):
    text, math = _protect_math(text)
    text = _id_worked_practice(text)
    text = _convert_anchors(text)
    text = _ensure_list_blank_lines(text)
    body = mdlib.markdown(text, extensions=["extra", "sane_lists", "toc"], output_format="html5")
    return _restore_math(body, math)


# --- HTML template ------------------------------------------------------------------------------
def _page(title, body, prev_link, next_link, subtitle=""):
    nav = ['<a href="index.html">Contents</a>']
    if prev_link:
        nav.append(f'<a href="{prev_link[0]}">&larr; {prev_link[1]}</a>')
    if next_link:
        nav.append(f'<a href="{next_link[0]}">{next_link[1]} &rarr;</a>')
    navhtml = " &nbsp;·&nbsp; ".join(nav)
    sub = f'<p class="subtitle">{subtitle}</p>' if subtitle else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{_html.escape(title)} — Algebra 1</title>
<link rel="stylesheet" href="textbook.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@{KATEX}/dist/katex.min.css" crossorigin="anonymous">
</head>
<body>
<header class="topbar">
  <nav>{navhtml}</nav>
  <button id="theme" type="button" aria-label="Toggle dark mode">◐</button>
</header>
<main>
<h1>{_html.escape(title)}</h1>
{sub}
{body}
</main>
<footer><p>Generated from the unit source by <code>_verification/build_textbook.py</code>. Math by KaTeX.</p></footer>
<script defer src="https://cdn.jsdelivr.net/npm/katex@{KATEX}/dist/katex.min.js" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@{KATEX}/dist/contrib/auto-render.min.js" crossorigin="anonymous"></script>
<script>
document.addEventListener("DOMContentLoaded", function () {{
  renderMathInElement(document.body, {{delimiters: [{{left: "$$", right: "$$", display: true}}], throwOnError: false}});
  var t = document.getElementById("theme"), root = document.documentElement;
  if (localStorage.getItem("a1-theme") === "dark") root.classList.add("dark");
  t.addEventListener("click", function () {{
    root.classList.toggle("dark");
    localStorage.setItem("a1-theme", root.classList.contains("dark") ? "dark" : "light");
  }});
}});
</script>
</body>
</html>
"""


CSS = """:root{--bg:#fff;--fg:#1a1a1a;--muted:#666;--accent:#2563eb;--code:#f3f4f6;--rule:#e5e7eb;--figbg:#fafafa}
html.dark{--bg:#14171c;--fg:#e6e6e6;--muted:#9aa4b2;--accent:#6ea8fe;--code:#1f242c;--rule:#2a313b;--figbg:#1b2027}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.65 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}
main{max-width:48rem;margin:0 auto;padding:1.5rem 1.2rem 4rem}
.topbar{position:sticky;top:0;display:flex;justify-content:space-between;align-items:center;gap:1rem;
  padding:.6rem 1.2rem;background:var(--bg);border-bottom:1px solid var(--rule);font-size:.9rem}
.topbar a{color:var(--accent);text-decoration:none}.topbar a:hover{text-decoration:underline}
#theme{background:none;border:1px solid var(--rule);border-radius:6px;color:var(--fg);cursor:pointer;font-size:1rem;padding:.2rem .5rem}
h1{font-size:1.9rem;line-height:1.2}h2{font-size:1.4rem;margin-top:2.2rem;border-top:1px solid var(--rule);padding-top:1.2rem}
h3{font-size:1.15rem;margin-top:1.6rem}.subtitle{color:var(--muted);margin-top:-.4rem}
a{color:var(--accent)}code{background:var(--code);padding:.1em .35em;border-radius:4px;font-size:.9em}
pre{background:var(--code);padding:.8rem 1rem;border-radius:8px;overflow:auto}pre code{background:none;padding:0}
blockquote{margin:1rem 0;padding:.4rem 1rem;border-left:3px solid var(--accent);background:var(--figbg);color:var(--muted)}
table{border-collapse:collapse;width:100%;margin:1rem 0;font-size:.95em}th,td{border:1px solid var(--rule);padding:.4rem .6rem;text-align:left}
th{background:var(--figbg)}
.refcode{display:inline-block;font:600 .72em ui-monospace,Consolas,monospace;background:var(--code);color:var(--muted);
  border:1px solid var(--rule);border-radius:5px;padding:.05em .4em;margin-right:.3em;text-decoration:none;vertical-align:.08em}
.refcode:hover{color:var(--accent);border-color:var(--accent)}
.refcode:target,*:target>.refcode{outline:2px solid var(--accent)}
:target{scroll-margin-top:4rem}
figure.fig{margin:1.2rem 0;padding:1rem;background:var(--figbg);border:1px solid var(--rule);border-radius:8px;text-align:center}
figure.fig svg{max-width:100%;height:auto}figcaption{color:var(--muted);font-size:.85rem;margin-top:.5rem}
.katex-display{overflow-x:auto;overflow-y:hidden;padding:.2rem 0}
footer{max-width:48rem;margin:0 auto;padding:1.2rem;color:var(--muted);font-size:.85rem;border-top:1px solid var(--rule)}
.toc{background:var(--figbg);border:1px solid var(--rule);border-radius:8px;padding:.6rem 1rem}
ul.units{list-style:none;padding:0}ul.units li{margin:.4rem 0}ul.units .u{color:var(--muted);font-size:.85em}
@media print{.topbar{position:static}#theme{display:none}a{color:inherit;text-decoration:none}figure.fig{break-inside:avoid}}
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
        pages[fname] = _page(f"Unit {u.id}: {u.title}", body, pl, nl, u.description)
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
