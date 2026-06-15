"""Regenerate every generated material (textbook, student guide, tutor guide, landing) and gate them
together — the design lives in build_textbook.CSS/_page, shared by all four, so they move in lockstep.

  python _verification/build_all.py            # regenerate all four
  python _verification/build_all.py --check    # verify all four are current + smoke aligned
"""
import argparse, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_textbook, build_student_guide, build_tutor_guide, build_landing, smoke_test  # noqa: E402

_MODS = (build_textbook, build_student_guide, build_tutor_guide, build_landing)


def generate():
    return sum(m.generate() for m in _MODS)


def check():
    issues = []
    for m in _MODS:
        issues += m.check()
    issues += smoke_test.check()
    return issues


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if a.check:
        iss = check()
        if iss:
            print("FAIL:\n  " + "\n  ".join(iss)); return 1
        print("all materials current and aligned."); return 0
    n = generate(); print(f"regenerated {n} files across all materials."); return 0


if __name__ == "__main__":
    sys.exit(main())
