import glob, os, re
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


def test_answers_for_delim_detection_dot_key_ignores_paren_coords():
    # unit-07 7.3: a DOT-delimited key whose value '(9, 3)' contains ', 3)'. Searching the key's own
    # '.' delimiter must skip the ')' coordinate and find the real '3.' on the next line.
    key = "1. (5, 3) — a\n2. (9, 3) — b\n3. (4, 1) — c"
    assert bt._answers_for(key, [1, 2, 3]) == {1: "(5, 3) — a", 2: "(9, 3) — b", 3: "(4, 1) — c"}
    # unit-01 1.1: value 'open (... is 4)' (paren) inside a DOT key must keep its trailing ')'
    k2 = "1. true 2. false 3. open (true when the blank is 4) 4. 7 5. 7"
    assert bt._answers_for(k2, [1, 2, 3, 4, 5])[3] == "open (true when the blank is 4)"
    assert bt._answers_for(k2, [1, 2, 3, 4, 5])[4] == "7"


def test_answers_for_strips_middot_separator():
    # unit-12: ' · '-separated key, with a middot also inside a value '√(4·2)'
    m = bt._answers_for("1. 4 · 2. 7 · 3. √(4·2)=2√2", [1, 2, 3])
    assert m == {1: "4", 2: "7", 3: "√(4·2)=2√2"}


def test_answers_for_bails_on_swallowed_marker():
    # unit-04: an answer ending in the next problem's number ('... and 6.') would swallow marker 6;
    # detect the value that becomes a stray '6. ...' and bail so the lesson falls back safely.
    assert bt._answers_for("5. Not a function — gives both 5 and 6.  6. Function.", [5, 6]) is None


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
    # continuation line is captured (joined with a newline, which _md_inline later renders as a space)
    assert "Two trains leave at" in items[0][2] and "the same time. How far?" in items[0][2]
    assert items[1] == ("prob", 2, "Short one")


def test_split_practice_block_ignores_sentence_ending_number():
    # a number ending problem prose ('... sum to 47.') must NOT become a phantom problem (unit-06 bug)
    body = ("1. Two consecutive integers sum to 47. Find them.\n"
            "2. Two consecutive odd integers sum to 56. Find them.")
    nums = [it[1] for it in bt._split_practice_block(body) if it[0] == "prob"]
    assert nums == [1, 2]


def test_md_inline_unwraps_stray_list():
    # a fragment that begins with an enumerator must not leave a block <ol>/<li> inside a <span>
    assert bt._md_inline("6. Function — inputs all distinct.") == "Function — inputs all distinct."
    assert "<ol" not in bt._md_inline("2. Through (-1,4), slope -3.")


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


def test_pair_does_not_swallow_trailing_note():
    # a paragraph after the answer key (e.g. '*Substitution spot-checks:*') must render on its own,
    # not get glued into the last problem's reveal (unit-01/02/10/11/12 bug).
    lesson = ("## Lesson 9.8: Demo\n\n"
              "**Practice problems:**\n\n"
              "1. x+5=12  2. x+9=14  3. x+7=7\n\n"
              "**Answer key:**\n1) 7  2) 5  3) 0\n\n"
              "*Spot-checks:* check #3 by substituting.\n\n---\n")
    html = bt.md_to_body(lesson)
    assert html.count('class="qcheck"') == 3
    qa3 = html.split('to problem 3</span></summary><span class="qa">')[1][:40]
    assert qa3.startswith("0<")                       # problem 3's reveal is just '0'
    assert "Spot-checks" not in html.split('class="qa">0<')[0].rsplit("prow", 1)[-1]
    assert "Spot-checks" in html                      # the note still renders somewhere on the page


def test_pair_does_not_append_later_key_to_last_answer():
    # a 1-3 set followed by a SEPARATE key for problems 4-6 (e.g. unit-01 1.5): problem 3's reveal
    # must be just its answer, never the following key's content.
    lesson = ("## Lesson 9.6: Demo\n\n"
              "**Practice problems:**\n\n"
              "1. a  2. b  3. c\n\n"
              "**Answer key:**\n1) A  2) B  3) C\n\n"
              "More text here.\n\n"
              "**Answer key:**\n4) D  5) E  6) F\n\n---\n")
    html = bt.md_to_body(lesson)
    m = re.search(r'to problem 3</span></summary><span class="qa">(.*?)</span>', html, re.S)
    assert m and m.group(1) == "C"                    # not 'C ... 4) D ...'
    assert "4) D" in html                             # the 4-6 key still renders (its own box)


def test_pair_falls_back_on_preamble_table():
    # a shared $$ table/array before problem 1 (appendix A.3) can't live in per-problem rows, so the
    # lesson must fall back (keeping the table), not silently drop it.
    lesson = ("## Lesson 9.4: Demo\n\n"
              "**Practice problems**. Use this table:\n\n"
              "$$\\begin{array}{c|c} a & b \\\\ 1 & 2 \\end{array}$$\n\n"
              "1. Find a.\n2. Find b.\n\n"
              "**Answer key:**\n1. one  2. two\n\n---\n")
    html = bt.md_to_body(lesson)
    assert 'class="qcheck"' not in html               # fell back
    assert "begin{array}" in html                     # the table survives


def test_pair_keeps_unused_strand_key():
    # a second strand with its OWN re-numbered key (unit-12 6) must not be deleted just because its
    # numbers overlap the converted set's numbers — only keys actually used in a conversion are dropped.
    lesson = ("## Lesson 9.3: Demo\n\n"
              "**Practice problems:**\n\n"
              "1. p  2. q  3. r\n\n"
              "**Answer key:**\n1) P  2) Q  3) R\n\n"
              "A short strand follows.\n\n"
              "**Answer key:**\n1) strandone  2) strandtwo\n\n---\n")
    html = bt.md_to_body(lesson)
    assert html.count('class="qcheck"') == 3          # main set converted
    assert "strandone" in html and "strandtwo" in html  # strand key NOT dropped


def test_pair_falls_back_on_nonmonotonic_numbering():
    # unit-08 8.3 'core' set lists problems out of order (… 9 then 8); that must fall back, not drop 8.
    lesson = ("## Lesson 9.7: Demo\n\n"
              "**Practice problems:**\n\n"
              "1. a\n4. b\n9. c\n8. d\n10. e\n\n"
              "**Answer key:**\n1. A\n4. B\n9. C\n8. D\n10. E\n\n---\n")
    html = bt.md_to_body(lesson)
    assert 'class="qcheck"' not in html               # not converted (out-of-order)
    assert 'class="answers"' in html                  # safe single box instead


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
