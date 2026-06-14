import smoke_test as st
import build_student_guide as sg
import build_landing as bl


def test_smoke_passes():
    assert st.check() == []          # all four materials aligned; codes resolve across them


def test_student_guide_current():
    assert sg.check() == []


def test_landing_current():
    assert bl.check() == []
