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

def test_full_lint_flags_missing_annotation(monkeypatch):
    import json, os
    real = json.load(open(os.path.join(ca.HERE, "unit-05.json"), encoding="utf-8"))
    stripped = {"unit": 5, "problems": [
        {k: v for k, v in p.items() if k != "on_line"} if p.get("id") == "5.5.1" else p
        for p in real["problems"]]}
    monkeypatch.setattr(ca, "_load_problems", lambda fp: stripped
                        if fp.endswith("unit-05.json") else json.load(open(fp, encoding="utf-8")))
    assert any("5.5.1" in str(i) for i in ca.point_on_line_lint())
