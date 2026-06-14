"""End-to-end integration smoke test across the four materials (build tooling).

Structural analog of the live smoke tests (new-learner / topic-jump / wrong-answer / photo / code
lookup / figure render): confirms the SSOT, skill references, HTML textbook, tutor guide, and student
guide are aligned, and that reference codes resolve ACROSS materials. The behavioral runtime tests
(actually talking to the skill on Claude.ai) require a live session and are out of scope here.

  python _verification/smoke_test.py
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)


def _imp(name):
    sys.path.insert(0, HERE)
    return __import__(name)


def _page(d, uid):
    return os.path.join(d, "appendix.html" if uid == "A" else f"unit-{int(uid):02d}.html")


def _has(path, needle):
    return os.path.exists(path) and needle in open(path, encoding="utf-8").read()


def check():
    gen = _imp("generate"); ssot = gen.load_ssot()
    tb = _imp("build_textbook"); tg = _imp("build_tutor_guide")
    sg = _imp("build_student_guide"); figmod = _imp("figures")
    issues = []

    # 1. every unit is present across textbook, tutor guide, and the complementary datastore
    for u in ssot.units:
        if not os.path.exists(_page(tb.OUT_DIR, u.id)):
            issues.append(f"textbook page missing for unit {u.id}")
        if not os.path.exists(_page(tg.OUT_DIR, u.id)):
            issues.append(f"tutor-guide page missing for unit {u.id}")
        cf = os.path.join(HERE, "complementary",
                          "appendix.json" if u.id == "A" else f"unit-{int(u.id):02d}.json")
        if not os.path.exists(cf):
            issues.append(f"complementary set missing for unit {u.id}")

    # 2. every bundled figure is embedded in its textbook unit page (figure render)
    for s in figmod.FIGURES:
        p = _page(tb.OUT_DIR, s["lesson"].split(".")[0])
        if os.path.exists(p) and f'id="fig-{s["code"]}"' not in open(p, encoding="utf-8").read():
            issues.append(f'figure {s["code"]} not embedded in {os.path.basename(p)}')

    # 3. reference-code resolution spot-checks across materials (code lookup)
    spot = [
        (_has(_page(tb.OUT_DIR, "1"), 'id="1.1.d1"'), "definition 1.1.d1 -> textbook unit-01"),
        (_has(_page(tb.OUT_DIR, "12"), 'id="12.6.w1"'), "worked-ex 12.6.w1 -> textbook unit-12"),
        (_has(_page(tb.OUT_DIR, "12"), 'id="fig-12.6.f1"'), "figure 12.6.f1 -> textbook unit-12"),
        (_has(_page(tg.OUT_DIR, "5"), 'id="5.4.T1"'), "complementary 5.4.T1 -> tutor-guide unit-05"),
        (_has(os.path.join(REPO_ROOT, "algebra-1-tutor", "references", "misconceptions.md"),
              "{#mis.3}"), "mis.3 -> misconceptions.md anchor"),
        (_has(os.path.join(REPO_ROOT, "algebra-1-tutor", "figures", "12.6.f1.svg"), "<svg"),
         "figure 12.6.f1 -> bundled SVG"),
    ]
    for ok, desc in spot:
        if not ok:
            issues.append(f"code resolution failed: {desc}")

    # 4. student guide exists and links into the textbook (topic jump)
    sgi = os.path.join(sg.OUT_DIR, "index.html")
    if not os.path.exists(sgi):
        issues.append("student-guide index missing")
    elif "../textbook/" not in open(sgi, encoding="utf-8").read():
        issues.append("student-guide does not link the textbook")

    return issues


def main():
    issues = check()
    if issues:
        print("SMOKE TEST FAIL:")
        for i in issues:
            print("  " + i)
        return 1
    print("smoke test: SSOT <-> skill <-> textbook <-> tutor-guide <-> student-guide aligned; "
          "reference codes resolve across materials. [OK]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
