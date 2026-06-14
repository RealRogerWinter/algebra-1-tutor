import glob, os
import build_textbook as bt


def _read(name):
    return open(os.path.join(bt.OUT_DIR, name), encoding="utf-8").read()


def test_check_clean():
    assert bt.check() == []          # committed site matches a fresh build


def test_deeplink_ids_present():
    s = _read("unit-12.html")
    for cid in ['id="12.6.f1"', 'id="12.5.w1"', 'id="12.1.1"']:
        assert cid in s, cid


def test_definition_and_check_anchors():
    s = _read("unit-01.html")
    assert 'id="1.1.d1"' in s and 'id="1.1.c1"' in s


def test_figure_svg_embedded():
    s = _read("unit-12.html")
    assert '<figure class="fig"' in s and "<svg" in s


def test_math_escaped_in_arrays():
    s = _read("unit-11.html")
    i = s.find("begin{array}")
    assert i != -1 and "&amp;" in s[i:i + 200]


def test_one_h1_per_page():
    for p in glob.glob(os.path.join(bt.OUT_DIR, "*.html")):
        assert open(p, encoding="utf-8").read().count("<h1>") == 1, p
