import xml.dom.minidom as minidom
import figures as F


def test_registry_accuracy_clean():
    for s in F.FIGURES:
        assert F.accuracy_issues(s) == [], (s["code"], F.accuracy_issues(s))


def test_catches_off_line_mark():
    bad = {"code": "x", "type": "line", "m": 2, "b": -1, "xwindow": [-3, 3], "ywindow": [-7, 7],
           "marks": [(0, 5, "wrong")], "caption": "y=2x-1"}
    assert F.accuracy_issues(bad)


def test_catches_wrong_vertex():
    bad = {"code": "x", "type": "parabola", "a": 1, "b": 0, "c": -4, "xwindow": [-3, 3],
           "ywindow": [-5, 6], "marks": [(0, 0, "vertex wrong")], "roots": [-2, 2], "caption": "y=x^2-4"}
    assert F.accuracy_issues(bad)


def test_catches_wrong_root():
    bad = {"code": "x", "type": "parabola", "a": 1, "b": 0, "c": -4, "xwindow": [-3, 3],
           "ywindow": [-5, 6], "marks": [], "roots": [1, 2], "caption": "y=x^2-4"}
    assert F.accuracy_issues(bad)


def test_catches_inequality_shading_flip():
    bad = {"code": "x", "type": "inequality_region", "m": 1, "b": 1, "op": "<", "xwindow": [-3, 3],
           "ywindow": [-3, 5], "test_point": [0, 3], "caption": "y<x+1"}  # (0,3) is ABOVE, op is <
    assert F.accuracy_issues(bad)


def test_catches_absurd_scatter_fit():
    bad = {"code": "x", "type": "scatter", "points": [(1, 2), (2, 3), (3, 3), (4, 5), (5, 6)],
           "fit": {"m": -10, "b": 50}, "caption": "absurd"}   # upward points, wrong-sign steep fit
    assert F.accuracy_issues(bad)


def test_render_valid_xml():
    for s in F.FIGURES:
        minidom.parseString(F.render(s))   # raises if not well-formed


def test_figure_lint_clean():
    import check_alignment as ca
    assert ca.figure_lint() == []          # anchors <-> SVGs <-> accurate registry all aligned
