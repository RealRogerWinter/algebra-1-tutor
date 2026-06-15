import glob, os
import smoke_test as st
import build_student_guide as sg
import build_tutor_guide as tg
import build_landing as bl


def test_smoke_passes():
    assert st.check() == []          # all four materials aligned; codes resolve across them


def test_one_h1_per_guide_page():
    # the guides + landing render through the textbook template, so each must have exactly one h1
    pages = glob.glob(os.path.join(sg.OUT_DIR, "*.html")) + glob.glob(os.path.join(tg.OUT_DIR, "*.html"))
    pages.append(os.path.join(bl.OUT_DIR, "index.html"))
    for p in pages:
        assert open(p, encoding="utf-8").read().count("<h1>") == 1, p


def test_student_guide_current():
    assert sg.check() == []


def test_landing_current():
    assert bl.check() == []
