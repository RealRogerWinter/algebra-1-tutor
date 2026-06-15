import glob, os
import build_textbook as bt


def _read(name):
    return open(os.path.join(bt.OUT_DIR, name), encoding="utf-8").read()


def test_check_clean():
    assert bt.check() == []          # committed site matches a fresh build


def test_deeplink_ids_present():
    for fn, cid in [("unit-12-6.html", 'id="12.6.f1"'),
                    ("unit-12-5.html", 'id="12.5.w1"'),
                    ("unit-12-1.html", 'id="12.1.1"')]:
        assert cid in _read(fn), (fn, cid)


def test_definition_and_check_anchors():
    s = _read("unit-01-1.html")
    assert 'id="1.1.d1"' in s and 'id="1.1.c1"' in s


def test_figure_svg_embedded():
    s = _read("unit-12-6.html")
    assert '<figure class="fig"' in s and "<svg" in s


def test_math_escaped_in_arrays():
    for p in glob.glob(os.path.join(bt.OUT_DIR, "*.html")):
        s = open(p, encoding="utf-8").read()
        i = s.find("begin{array}")
        if i != -1:
            assert "&amp;" in s[i:i + 200], p
            return
    raise AssertionError("no begin{array} found in any textbook page")


def test_one_h1_per_page():
    for p in glob.glob(os.path.join(bt.OUT_DIR, "*.html")):
        assert open(p, encoding="utf-8").read().count("<h1>") == 1, p


# --- reference-code tutor launcher -------------------------------------------------------------
def _built():
    return bt.build_site(bt._ssot())


def test_label_for_kinds():
    assert bt._label_for("12.5.w2") == "worked example 2 in Lesson 12.5"
    assert bt._label_for("6.2.ex1") == "worked example 1 in Lesson 6.2"   # 'ex' form; really shipped (e.g. {#6.2.ex1})
    assert bt._label_for("12.5.7") == "practice problem 7 in Lesson 12.5"
    assert bt._label_for("1.1.d1") == "a key term in Lesson 1.1"
    assert bt._label_for("1.1.c1") == "a check-for-understanding question in Lesson 1.1"
    assert bt._label_for("12.6.f1") == "the figure in Lesson 12.6"
    assert bt._label_for("3.1.h1") == "a how-to in Lesson 3.1"            # h branch
    assert bt._label_for("12.5.x9") == "reference 12.5.x9 in Lesson 12.5"  # 3-part unknown kind -> fallback WITH lesson clause
    assert bt._label_for("mis.3") == "reference mis.3"                    # 2-part bank code -> bare fallback
    assert bt._label_for("vis.t1") == "reference vis.t1"
    # Pure-function coverage of the ", part" / A-scope branches. The current generator never emits a
    # lettered part (_id_worked_practice writes f"{lid}.{pk}") nor an A.* f-code, so these inputs are
    # defensive, not drawn from shipping output:
    assert bt._label_for("8.2.5b") == "practice problem 5, part b in Lesson 8.2"
    assert bt._label_for("A.2.f1") == "the figure in Lesson A.2"


def test_attr_escaping():
    assert bt._attr('a & "b"') == 'a &amp; &quot;b&quot;'   # & and double-quote escaped for the attribute
    assert bt._attr("I'd") == "I'd"                         # apostrophe stays literal (no entity)


def test_prompt_for_shape():
    assert bt._prompt_for("12.5.w2") == (
        "Use the Algebra 1 tutor skill to help me with worked example 2 in Lesson 12.5 "
        "(reference 12.5.w2). Pull it up, then ask whether I'd like you to explain it, "
        "work through it together, or answer a specific question.")


def test_badge_launcher_attrs():
    html = bt.md_to_body("See {#12.5.w2} here.", launcher=True)
    assert 'class="refcode" id="12.5.w2" href="#12.5.w2"' in html
    assert ('data-prompt="' + bt._attr(bt._prompt_for("12.5.w2")) + '"') in html   # full prompt, exact
    assert 'aria-label="Copy a tutor prompt for worked example 2 in Lesson 12.5"' in html
    assert "whether I'd like you" in html          # apostrophe stays literal (no entity)


def test_badge_plain_by_default():
    html = bt.md_to_body("See {#12.5.w2} here.")    # launcher defaults False
    assert 'class="refcode" id="12.5.w2" href="#12.5.w2">12.5.w2</a>' in html
    assert "data-prompt" not in html and "aria-label" not in html


def test_shared_elements_once_per_textbook_page():
    files = _built()
    page = files["unit-12-5.html"]
    assert page.count('id="rc-tip"') == 1 and page.count('id="rc-toast"') == 1
    # a real badge's data-prompt equals _prompt_for(code) (12.5.w1 is a known badge on this page)
    code = "12.5.w1"
    assert ('id="' + code + '" href="#' + code + '" data-prompt="' + bt._attr(bt._prompt_for(code)) + '"') in page
    assert files["index.html"].count('id="rc-toast"') == 1   # index also routes through _lesson_page


def test_refcode_controller_present():
    page = _built()["unit-12-5.html"]
    assert "navigator.clipboard" in page and 'closest(".refcode")' in page


def test_launcher_css_scoped():
    css = _built()["textbook.css"]
    assert 'body[data-surface="textbook"] .refcode{cursor:copy}' in css
    assert "#rc-tip" in css and "#rc-toast" in css


def test_guides_have_no_launcher_attrs():
    # md_to_body without the flag (the path guides reuse) must stay plain
    assert "data-prompt" not in bt.md_to_body("See {#1.1.d1} here.")
