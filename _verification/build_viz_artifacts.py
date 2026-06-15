"""Generate a self-contained .html artifact per viz figure, bundled into the skill (build tooling).

The student textbook embeds ~40 "viz" figures (viz_figures.VIZ_FIGURES) as HTML/SVG + inline JS
via build_textbook; unlike the deterministic figures.py SVGs they were never bundled into the
skill, so the tutor could not emit them. This writes algebra-1-tutor/figures/<code>.html for every
viz code: each sample's html wrapped in a standalone page that inlines build_textbook.CSS (reused
wholesale so it cannot drift) and loads KaTeX from cdnjs (the CDN Claude.ai artifacts may use).
Codes are disjoint from the .svg codes, so <code>.svg and <code>.html never coexist.

  python _verification/build_viz_artifacts.py            # (re)write the .html artifacts
  python _verification/build_viz_artifacts.py --check     # verify committed artifacts are current
"""
import argparse, glob, html as _html, importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
VIZ_DIR = os.path.join(HERE, "viz")
FIG_DIR = os.path.join(REPO_ROOT, "algebra-1-tutor", "figures")

sys.path.insert(0, HERE)
import viz_figures as _vf
import build_textbook as _bt

KATEX = _bt.KATEX
_CDNJS = "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/" + KATEX

# Assembled by .replace (NOT .format): build_textbook.CSS and the viz bodies contain literal { } and $$.
_HEAD = (
    "<!doctype html>\n<html lang=\"en\">\n<head>\n"
    "<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
    "<title>Figure __CODE__</title>\n"
    "<link rel=\"stylesheet\" href=\"" + _CDNJS + "/katex.min.css\">\n"
    "<style>\n__CSS__\n"
    ".fig-standalone{max-width:760px;margin:1.4rem auto;padding:0 1rem}\n"
    "</style>\n"
    "<script>try{if(window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches)"
    "document.documentElement.classList.add('dark');}catch(e){}</script>\n"
    "</head>\n<body data-surface=\"textbook\">\n<main class=\"fig-standalone\">\n"
)
_TAIL = (
    "\n</main>\n"
    "<script defer src=\"" + _CDNJS + "/katex.min.js\"></script>\n"
    "<script defer src=\"" + _CDNJS + "/contrib/auto-render.min.js\"></script>\n"
    "<script>\ndocument.addEventListener('DOMContentLoaded', function () {\n"
    "  if (typeof renderMathInElement === 'function') {\n"
    "    renderMathInElement(document.body, {delimiters: ["
    "{left: '$$', right: '$$', display: true}, {left: '\\\\(', right: '\\\\)', display: false}],"
    " throwOnError: false});\n  }\n});\n</script>\n</body>\n</html>\n"
)

_MOD_CACHE = {}


def _module(name):
    if name not in _MOD_CACHE:
        fp = os.path.join(VIZ_DIR, name + ".py")
        spec = importlib.util.spec_from_file_location("bva_" + name, fp)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        _MOD_CACHE[name] = m
    return _MOD_CACHE[name]


def _entry(code):
    for e in _vf.VIZ_FIGURES:
        if e["code"] == code:
            return e
    raise KeyError("no viz figure with code " + code)


def figure_body(code):
    """The raw sample html for a viz code (the inline SVG/HTML/JS, before wrapping)."""
    e = _entry(code)
    return _module(e["module"]).samples()[int(e["index"])]["html"]


def _caption(code):
    e = _entry(code)
    cap = _module(e["module"]).samples()[int(e["index"])].get("caption", "")
    return (" &mdash; " + _html.escape(cap)) if cap else ""


def render_page(code):
    """Full standalone HTML document for a viz code."""
    fig = ('<figure class="fig viz" id="fig-' + code + '">' + figure_body(code)
           + '<figcaption><b>Figure ' + code + '</b>' + _caption(code) + '</figcaption></figure>')
    head = _HEAD.replace("__CODE__", code).replace("__CSS__", _bt.CSS)
    return head + fig + _TAIL


def codes():
    return [e["code"] for e in _vf.VIZ_FIGURES]


def build():
    """Write algebra-1-tutor/figures/<code>.html for every viz code. Returns the count."""
    os.makedirs(FIG_DIR, exist_ok=True)
    for code in codes():
        with open(os.path.join(FIG_DIR, code + ".html"), "w", encoding="utf-8", newline="\n") as f:
            f.write(render_page(code))
    return len(codes())


def check():
    """Verify every committed <code>.html matches a fresh render and there are no orphans."""
    issues = []
    want = set(codes())
    for code in sorted(want):
        p = os.path.join(FIG_DIR, code + ".html")
        if not os.path.exists(p):
            issues.append(code + ".html: missing (run build_viz_artifacts.py)")
            continue
        on_disk = open(p, encoding="utf-8").read().replace("\r\n", "\n")
        if on_disk != render_page(code):
            issues.append(code + ".html: content differs from source (run build_viz_artifacts.py)")
    have = {os.path.splitext(os.path.basename(p))[0]
            for p in glob.glob(os.path.join(FIG_DIR, "*.html"))}
    for orphan in sorted(have - want):
        issues.append(orphan + ".html: bundled but has no viz_figures entry")
    return issues


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if a.check:
        iss = check()
        if iss:
            print("FAIL:\n  " + "\n  ".join(iss)); return 1
        print("viz artifacts: " + str(len(codes())) + " figures bundled as .html; current."); return 0
    n = build(); print("built " + str(n) + " viz-figure .html artifacts in algebra-1-tutor/figures/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
