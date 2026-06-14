"""Generate the GitHub Pages landing page (docs/index.html) that links the three generated sites
(textbook, student guide, tutor guide). Build tooling; CSS shared with the textbook.

  python _verification/build_landing.py            # (re)generate docs/index.html + docs/textbook.css
  python _verification/build_landing.py --check    # verify the committed landing is current
"""
import argparse, glob, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
OUT_DIR = os.path.join(REPO_ROOT, "docs")


def _bt():
    sys.path.insert(0, HERE)
    import build_textbook
    return build_textbook


def _ssot():
    sys.path.insert(0, HERE)
    import generate
    return generate.load_ssot()


def _counts(ssot):
    sys.path.insert(0, HERE)
    import figures
    units = len(ssot.units)
    lessons = sum(len(u.lessons) for u in ssot.units)
    figs = len(figures.FIGURES)
    comp = sum(len(json.load(open(p, encoding="utf-8"))["problems"])
               for p in glob.glob(os.path.join(HERE, "complementary", "*.json")))
    return units, lessons, figs, comp


def build_site(ssot):
    bt = _bt()
    u, l, f, c = _counts(ssot)
    body = f"""<p class="subtitle">A complete, self-paced Algebra 1 course for an adult learner who knows arithmetic — {u} units, {l} lessons. Every worked example, definition, and figure has a reference code you can quote to the tutor.</p>
<ul class="units">
<li><a href="student-guide/index.html"><b>Student guide</b></a><br><span class="u">Start here: how the course works, the roadmap, and how to use the tutor.</span></li>
<li><a href="textbook/index.html"><b>Textbook</b></a><br><span class="u">The lessons in full — worked examples, practice, and {f} computed figures, with reference-code deep links.</span></li>
<li><a href="tutor-guide/index.html"><b>Tutor guide</b></a><br><span class="u">{c} extra parallel-form problems with full worked solutions, plus a mixed-review set per unit.</span></li>
</ul>
<p class="u">Math is rendered with KaTeX. The course is generated from a single source of truth and held correct by sympy and a CI gate. Sources and licenses are listed in the textbook's reference pack.</p>
"""
    return {"index.html": bt._page("Algebra 1 — A Complete Course", body, None, None),
            "textbook.css": bt.CSS}


def generate():
    files = build_site(_ssot())
    for name, content in files.items():
        open(os.path.join(OUT_DIR, name), "w", encoding="utf-8", newline="\n").write(content)
    return len(files)


def check():
    files = build_site(_ssot())
    issues = []
    for name, content in files.items():
        p = os.path.join(OUT_DIR, name)
        if not os.path.exists(p):
            issues.append(f"docs/{name}: missing (run build_landing.py)")
        elif open(p, encoding="utf-8").read() != content:
            issues.append(f"docs/{name}: stale (run build_landing.py)")
    return issues


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if a.check:
        iss = check()
        if iss:
            print("FAIL:\n  " + "\n  ".join(iss)); return 1
        print("landing: docs/index.html current."); return 0
    n = generate(); print(f"generated landing page ({n} files) -> docs/"); return 0


if __name__ == "__main__":
    sys.exit(main())
