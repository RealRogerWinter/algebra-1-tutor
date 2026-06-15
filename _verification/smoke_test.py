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

    # 2. every bundled figure is embedded in its textbook LESSON page (figure render)
    for s in figmod.FIGURES:
        p = os.path.join(tb.OUT_DIR, tb._lesson_fname(s["lesson"]))
        if os.path.exists(p) and f'id="fig-{s["code"]}"' not in open(p, encoding="utf-8").read():
            issues.append(f'figure {s["code"]} not embedded in {os.path.basename(p)}')

    # 2b. every viz figure resolves to a bundled .html artifact AND is embedded in its lesson page
    vfmod = _imp("viz_figures")
    for e in vfmod.VIZ_FIGURES:
        code = e["code"]
        if not os.path.exists(os.path.join(REPO_ROOT, "algebra-1-tutor", "figures", code + ".html")):
            issues.append(f"viz figure {code} has no bundled .html artifact")
        lesson = code.rsplit(".f", 1)[0]            # "3.2.f1" -> "3.2"; "5.0.f1" -> "5.0"
        p = os.path.join(tb.OUT_DIR, tb._lesson_fname(lesson))
        if os.path.exists(p) and f'id="fig-{code}"' not in open(p, encoding="utf-8").read():
            issues.append(f"viz figure {code} not embedded in {os.path.basename(p)}")

    # 3. reference-code resolution spot-checks across materials (code lookup)
    spot = [
        (_has(os.path.join(tb.OUT_DIR, tb._lesson_fname("1.1")), 'id="1.1.d1"'), "definition 1.1.d1 -> textbook lesson 1.1"),
        (_has(os.path.join(tb.OUT_DIR, tb._lesson_fname("12.6")), 'id="12.6.w1"'), "worked-ex 12.6.w1 -> textbook lesson 12.6"),
        (_has(os.path.join(tb.OUT_DIR, tb._lesson_fname("12.6")), 'id="fig-12.6.f1"'), "figure 12.6.f1 -> textbook lesson 12.6"),
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
