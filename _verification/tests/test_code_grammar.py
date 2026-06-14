# _verification/tests/test_code_grammar.py
import check_alignment as ca

def test_all_real_ids_pass():
    bad = ca.code_grammar_lint()
    assert bad == [], f"ids violating grammar: {bad}"

def test_accepts_known_shapes():
    for good in ["5.5.6", "12.1.w1", "A.2.3", "refA.4", "refB.10", "8.2.5b"]:
        assert ca.ID_RE.match(good), good

def test_rejects_malformed():
    for bad in ["5.5.", "13.1.1", "x.y.z", "5..6", "ref.4", "5.5.w"]:
        assert not ca.ID_RE.match(bad), bad


def test_accepts_new_shapes():
    for good in ["1.1.d1", "1.1.c1", "2.2.h1", "1.2.f1",
                 "mis.3", "vis.t1", "met.balance-scale", "met.two-round-flyers",
                 "5.5.6", "12.1.w1", "A.2.3", "refA.4", "8.2.5b", "6.2.ex1"]:
        assert ca.ID_RE.match(good), good


def test_rejects_malformed_new():
    for bad in ["1.1.d", "mis.", "vis.3", "vis.tx", "met.Bad_Slug", "met.",
                "met.-x", "met.x-", "5.5.", "13.1.1", "x.y.z", "5..6", "ref.4", "5.5.w"]:
        assert not ca.ID_RE.match(bad), bad


# --- md_anchor_lint logic (pure, fixture-driven) ---
SSOT = {"1.1", "1.2", "2.2"}  # minimal lesson set for pure-logic tests


def test_anchor_clean():
    anchors = [("1.1.d1", "u.md"), ("1.1.d2", "u.md"), ("1.1.c1", "u.md"),
               ("mis.1", "m.md"), ("vis.t1", "v.md"), ("met.balance-scale", "x.md")]
    assert ca._lint_anchor_list(anchors, SSOT) == []


def test_anchor_grammar_failure():
    issues = ca._lint_anchor_list([("1.1.zz", "u.md")], SSOT)
    assert any("grammar" in i for i in issues)


def test_anchor_collision():
    issues = ca._lint_anchor_list([("1.1.d1", "a.md"), ("1.1.d1", "b.md")], SSOT)
    assert any("duplicate" in i.lower() for i in issues)


def test_anchor_density_gap():
    issues = ca._lint_anchor_list([("1.1.d1", "u.md"), ("1.1.d3", "u.md")], SSOT)
    assert any("dense" in i for i in issues)


def test_anchor_unknown_lesson():
    issues = ca._lint_anchor_list([("9.9.d1", "u.md")], SSOT)
    assert any("unknown lesson" in i for i in issues)


def test_md_anchor_lint_real_tree_clean():
    assert ca.md_anchor_lint() == []   # holds once banks (PR1) / units (PR2) are tagged
