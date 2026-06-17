"""Generate the GitHub Pages landing page (docs/index.html) that links the three generated sites
(textbook, student guide, tutor guide). Build tooling; shares the textbook's chrome (left rail into
the textbook, a hero) and CSS so the front door reads as one work.

  python _verification/build_landing.py            # (re)generate docs/index.html + docs/textbook.css
  python _verification/build_landing.py --check    # verify the committed landing is current
"""
import argparse, glob, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
OUT_DIR = os.path.join(REPO_ROOT, "docs")

TOP = [("how-to-use.html", "How to use this book"), ("index.html", "All units")]


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
    lede = (f"A complete, self-paced Algebra 1 course for an adult who knows arithmetic: a friendly "
            f"textbook to read and a one-on-one tutor to learn with, plus extra practice when you want "
            f"it. {u} units and {l} lessons in all, from foundations to a quadratics capstone plus a "
            f"core unit on data and statistics, each quotable by a short code.")
    body = f"""<ul class="units">
<li><a href="student-guide/index.html"><b>Student guide</b></a><br><span class="u">Start here: how the course works and how to learn with the tutor.</span></li>
<li><a href="textbook/index.html"><b>Textbook</b></a><br><span class="u">The lessons in full — worked examples, practice, and {f} computed figures, each with a reference code you can deep-link or quote.</span></li>
<li><a href="tutor-guide/index.html"><b>Tutor guide</b></a><br><span class="u">{c} extra parallel-form problems with full worked solutions, plus a mixed-review set per unit.</span></li>
</ul>
<p>The tutor is a <b>Claude skill</b>: download <a href="https://github.com/RealRogerWinter/algebra-1-tutor/raw/main/algebra-1-tutor.zip"><code>algebra-1-tutor.zip</code></a> and upload it in the Claude app or on claude.ai, and Claude becomes a patient one-on-one teacher with this whole course in front of it. New to that? <a href="textbook/how-to-use.html">See how to set it up and learn with it</a> — it works on the free plan.</p>
<blockquote><p>See a code like <code>12.5.w2</code> beside a worked example? Quote it to the tutor — "explain 12.5.w2" — and it pulls up that exact item, re-checks the math, and walks you through it.</p></blockquote>
<p class="u">Math is rendered with KaTeX. The whole course is generated from one source of truth and held correct by sympy and a CI gate.</p>
"""
    page = bt._lesson_page("Algebra 1", body, bt._ssot_model(ssot), "", None, None, subtitle=lede,
                           hero="assets/landing-hero.jpg", kicker="A complete course",
                           sidebar_prefix="textbook/", sidebar_top=TOP, brand_prefix="")
    return {"index.html": page, "textbook.css": bt.CSS}


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
