import os
import verify_complementary as vc
import build_tutor_guide as tg


def test_complementary_verifies():
    assert vc.main() == 0          # sympy re-checks all answers + grammar/uniqueness/SSOT


def test_tutor_guide_current():
    assert tg.check() == []        # committed pages match a fresh build


def test_every_unit_has_a_set():
    # all 13 units (12 + appendix) have a complementary file with problems
    n = 0
    for name in (["appendix.json"] + [f"unit-{i:02d}.json" for i in range(1, 13)]):
        p = os.path.join(vc.COMP_DIR, name)
        assert os.path.exists(p), name
        n += 1
    assert n == 13


def test_tutor_guide_renders_problem_and_solution():
    s = open(os.path.join(tg.OUT_DIR, "unit-05.html"), encoding="utf-8").read()
    assert 'class="tproblem"' in s and '<span class="eyebrow">Worked solution</span>' in s
    assert 'id="5.4.T1"' in s          # a per-lesson T code is a deep-link target
