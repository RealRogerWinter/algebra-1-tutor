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
