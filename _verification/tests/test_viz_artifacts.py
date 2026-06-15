import build_viz_artifacts as bva
import viz_figures as vf


def test_page_is_self_contained_and_keyed():
    code = "3.2.f1"
    html = bva.render_page(code)
    assert html.lstrip().lower().startswith("<!doctype html>")
    assert f'id="fig-{code}"' in html
    assert "<style>" in html                      # CSS inlined, not linked to a local file
    assert "var(--ink)" in html                   # the textbook CSS variables are present
    assert "cdnjs.cloudflare.com/ajax/libs/KaTeX/" + bva.KATEX in html
    assert "renderMathInElement" in html


def test_math_body_pulls_katex():
    # 3.2.f1 body contains TeX; the page must load KaTeX css + js from cdnjs
    html = bva.render_page("3.2.f1")
    assert "katex.min.css" in html and "katex.min.js" in html and "auto-render.min.js" in html


def test_interactive_js_preserved():
    # 5.2.f2 is an interactive slider widget; its inline <script> must survive verbatim
    html = bva.render_page("5.2.f2")
    assert "<script" in html
    body = bva.figure_body("5.2.f2")
    assert "addEventListener" in body or "oninput" in body


def test_check_passes_after_build():
    bva.build()
    assert bva.check() == []


def test_check_detects_stale():
    import os
    bva.build()
    target = os.path.join(bva.FIG_DIR, "3.2.f1.html")
    original = open(target, encoding="utf-8").read()
    try:
        open(target, "w", encoding="utf-8").write(original + "<!--drift-->")
        issues = bva.check()
        assert any("3.2.f1.html" in i for i in issues)
    finally:
        open(target, "w", encoding="utf-8", newline="\n").write(original.replace("\r\n", "\n"))


def test_one_to_one_with_registry():
    import glob, os
    bva.build()
    on_disk = {os.path.splitext(os.path.basename(p))[0]
               for p in glob.glob(os.path.join(bva.FIG_DIR, "*.html"))}
    assert on_disk == set(bva.codes())
