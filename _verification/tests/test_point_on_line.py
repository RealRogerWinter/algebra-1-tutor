# _verification/tests/test_point_on_line.py
import check_alignment as ca

OLD_556 = {"id": "5.5.6", "kind": "solve", "eq": "3*1+b=5", "var": "b", "answer": "2",
           "on_line": [[0, -2], [3, 7]]}
NEW_556 = {"id": "5.5.6", "kind": "solve", "eq": "3*3+b=7", "var": "b", "answer": "-2",
           "on_line": [[0, -2], [3, 7]]}
ONE_PT  = {"id": "5.5.1", "kind": "solve", "eq": "2*3+b=1", "var": "b", "answer": "-5",
           "on_line": [[3, 1]], "slope": 2}

def test_corrected_entry_passes_geometric():
    assert ca.point_on_line_geometric(NEW_556) == []

def test_old_entry_rejected_geometric():
    # class regression: self-consistent eq but wrong line -> points are NOT on it
    assert ca.point_on_line_geometric(OLD_556) != []

def test_one_point_slope_entry_passes():
    assert ca.point_on_line_geometric(ONE_PT) == []

def test_two_point_noncollinear_rejected():
    bad = dict(NEW_556, on_line=[[0, -2], [3, 99]])
    assert ca.point_on_line_geometric(bad) != []


def test_md_crosscheck_passes_for_real_556():
    prob = {"id": "5.5.6", "kind": "solve", "eq": "3*3+b=7", "var": "b", "answer": "-2",
            "on_line": [[0, -2], [3, 7]]}
    assert ca.point_on_line_md(prob) == []

def test_md_crosscheck_rejects_wrong_line():
    # JSON encodes y=3x+2 but .md answer key #6 says y=3x-2
    prob = {"id": "5.5.6", "kind": "solve", "eq": "3*1+b=5", "var": "b", "answer": "2",
            "on_line": [[0, -2], [3, 7]]}
    assert ca.point_on_line_md(prob) != []

def test_full_lint_green_on_repo():
    # both witnesses, every line-intercept entry across all units
    assert ca.point_on_line_lint() == []

def test_md_crosscheck_passes_real_worked_examples():
    # the two real worked-example line entries parse from the multi-line $$ blocks
    for prob in (
        {"id": "5.5.w1", "kind": "solve", "eq": "4*2+b=3", "var": "b", "answer": "-5",
         "on_line": [[2, 3]], "slope": 4},
        {"id": "5.5.w2", "kind": "solve", "eq": "3*1+b=2", "var": "b", "answer": "-1",
         "on_line": [[1, 2], [3, 8]]},
    ):
        assert ca.point_on_line_md(prob) == [], prob["id"]

def test_md_crosscheck_rejects_wrong_worked_example():
    # fabricated worked example encoding a totally wrong line; .md WE #2 is y=3x-1.
    # the geometric witness can't catch this (self-consistent) -> the .md witness must.
    bad = {"id": "5.5.w2", "kind": "solve", "eq": "7*0+b=100", "var": "b", "answer": "100",
           "on_line": [[0, 100], [1, 107]]}
    assert ca.point_on_line_geometric(bad) == []   # internally consistent -> geometric passes
    assert ca.point_on_line_md(bad) != []          # .md cross-check rejects it

def test_md_crosscheck_no_crash_on_one_point_no_slope():
    # malformed (one point, no slope) -> a readable issue, never a ValueError/traceback
    bad = {"id": "5.5.4", "kind": "solve", "eq": "3*2+b=5", "var": "b", "answer": "-1",
           "on_line": [[2, 5]]}
    out = ca.point_on_line_md(bad)
    assert out and "slope" in out[0].lower()

def test_full_lint_flags_missing_annotation(monkeypatch):
    import json, os
    real = json.load(open(os.path.join(ca.HERE, "unit-05.json"), encoding="utf-8"))
    stripped = {"unit": 5, "problems": [
        {k: v for k, v in p.items() if k != "on_line"} if p.get("id") == "5.5.1" else p
        for p in real["problems"]]}
    monkeypatch.setattr(ca, "_load_problems", lambda fp: stripped
                        if fp.endswith("unit-05.json") else json.load(open(fp, encoding="utf-8")))
    assert any("5.5.1" in str(i) for i in ca.point_on_line_lint())
