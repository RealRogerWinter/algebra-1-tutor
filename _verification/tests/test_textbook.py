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


# --- per-question answer reveal ----------------------------------------------------------------
def test_md_inline_strips_paragraph_and_keeps_formatting():
    assert bt._md_inline("x+5=12") == "x+5=12"
    assert bt._md_inline("**prime**") == "<strong>prime</strong>"
    assert bt._md_inline('<a class="refcode">2.1.1</a> x=1') == '<a class="refcode">2.1.1</a> x=1'
    assert 'markdown="1"' not in bt._md_inline("**a**")


def test_answers_for_basic_and_robust():
    assert bt._answers_for("1) 7  2) 5  3) 0", [1, 2, 3]) == {1: "7", 2: "5", 3: "0"}
    # stray '+1)' inside a parenthetical note must not be read as marker 1
    m = bt._answers_for("11) 2×10¹² (from 20×10¹¹ — slide left, exponent +1)  12) 5.6×10⁶", [11, 12])
    assert m[11] == "2×10¹² (from 20×10¹¹ — slide left, exponent +1)"
    assert m[12] == "5.6×10⁶"
    # multi-line, prose answer, '.'-delimited with a leading italic note
    m2 = bt._answers_for("1) 4  2) 5\n13) x=4  14) identity — all real numbers", [1, 2, 13, 14])
    assert m2[2] == "5" and m2[13] == "x=4" and m2[14] == "identity — all real numbers"
    assert bt._answers_for("*(note)* 13. -4 14. 4", [13, 14]) == {13: "-4", 14: "4"}
    # non-contiguous numbering (unit-08 'core' set) pairs fine
    assert bt._answers_for("1) a  4) b  8) c", [1, 4, 8]) == {1: "a", 4: "b", 8: "c"}
    # a missing answer -> cannot pair -> None (drives graceful fallback)
    assert bt._answers_for("1) 7  2) 5", [1, 2, 3]) is None


def test_answers_for_handles_parens_in_values():
    # ordered pairs (unit-07) and factorisations (unit-11): the ')'/' )' inside values is ignored
    assert bt._answers_for("1) (2, 3)  2) (1, -1)  3) (0, 4)", [1, 2, 3]) == {
        1: "(2, 3)", 2: "(1, -1)", 3: "(0, 4)"}
    assert bt._answers_for("1) 2(x+3)  2) 5(x+3)  3) 3(2x-3)", [1, 2, 3]) == {
        1: "2(x+3)", 2: "5(x+3)", 3: "3(2x-3)"}


def test_key_numbers_residual_not_claimed():
    assert bt._key_numbers("1) 7  2) 5  3) 0", {1, 2, 3, 4}) == {1, 2, 3}
    assert bt._key_numbers("13. -4 14. 4", {1, 2, 3}) == set()   # residual key keeps its box


def test_split_practice_block_packed_and_subheads():
    body = ("*Add (undo by subtracting):*\n"
            "1. x+5=12  2. x+9=14  3. x+7=7\n"
            "*Subtract (undo by adding):*\n"
            "6. x-4=10  7. x-6=1")
    items = bt._split_practice_block(body)
    assert items[0] == ("sub", "Add (undo by subtracting):")
    assert items[1] == ("prob", 1, "x+5=12")
    assert items[3] == ("prob", 3, "x+7=7")
    assert items[4] == ("sub", "Subtract (undo by adding):")
    assert items[5] == ("prob", 6, "x-4=10")


def test_split_practice_block_carries_badge_and_multiline():
    body = ('1. <a class="refcode" id="2.1.1">2.1.1</a> Two trains leave at\n'
            'the same time. How far?\n2. Short one')
    items = bt._split_practice_block(body)
    assert items[0][0] == "prob" and items[0][1] == 1
    assert '<a class="refcode" id="2.1.1">2.1.1</a>' in items[0][2]
    assert "Two trains leave at the same time. How far?" in items[0][2]
    assert items[1] == ("prob", 2, "Short one")


LESSON_OK = (
    "## Lesson 9.9: Demo\n\n"
    "**Practice problems:**\n\n"
    "*Group one:*\n"
    "1. x+5=12  2. x+9=14  3. x+7=7\n\n"
    "**Answer key:**\n"
    "1) 7  2) 5  3) 0\n\n"
    "---\n")


def test_pair_converts_and_drops_key():
    html = bt.md_to_body(LESSON_OK)
    assert html.count('class="prow"') == 3
    assert html.count('class="qcheck"') == 3
    assert 'class="practice-sub"' in html
    assert '>7<' in html and 'Reveal answer' in html
    assert 'class="answers"' not in html
    assert 'to problem 1' in html


def test_pair_falls_back_when_answer_missing():
    bad = LESSON_OK.replace("1) 7  2) 5  3) 0", "1) 7  2) 5")
    html = bt.md_to_body(bad)
    assert 'class="qcheck"' not in html
    assert 'class="answers"' in html


def test_qcheck_css_present_and_answers_untouched():
    css = bt.CSS
    assert ".prow{" in css and ".qcheck" in css and ".practice-sub" in css and ".vh{" in css
    assert ".answers > summary{cursor:pointer" in css


def test_tutor_guide_answers_unchanged():
    import build_tutor_guide as tg
    files = tg.build_site(tg._ssot())
    unit = next(v for k, v in files.items() if k.startswith("unit-"))
    assert 'details class="answers"' in unit
    assert 'class="qcheck"' not in unit


def test_pair_build_is_deterministic():
    out1 = bt.md_to_body(LESSON_OK)
    out2 = bt.md_to_body(LESSON_OK)
    assert out1 == out2
    assert 'markdown="1"' not in out1


def test_pair_converts_parenthetical_header_with_caption():
    lesson = (
        "## Lesson 8.9: Demo\n\n"
        "**Practice problems** (solve; then describe the graph):\n\n"
        "1. x - 2 < 3\n2. 3x > 12\n3. x/2 ≥ 4\n\n"
        "**Answer key:**\n"
        "1. x < 5 — open circle at 5, shade left.\n"
        "2. x > 4 — open circle at 4, shade right.\n"
        "3. x ≥ 8 — filled circle at 8, shade right.\n\n"
        "---\n")
    html = bt.md_to_body(lesson)
    assert html.count('class="qcheck"') == 3                 # broad header now detected + converted
    assert 'class="practice-intro"' in html                  # instructional parenthetical preserved
    assert "solve; then describe the graph" in html
    assert 'class="answers"' not in html
    assert "open circle at 5, shade left." in html           # prose '.'-delimited answer paired in
