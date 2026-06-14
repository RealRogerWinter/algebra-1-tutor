"""Generate the student guide from the SSOT (build tooling). A learner-facing roadmap (a motivating
map, not a textbook) that links into the generated textbook and explains how to use the tutor + the
reference-code system. Look/CSS shared with the textbook.

  python _verification/build_student_guide.py            # (re)generate docs/student-guide/
  python _verification/build_student_guide.py --check    # verify the committed page is current
"""
import argparse, html as _html, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
OUT_DIR = os.path.join(REPO_ROOT, "docs", "student-guide")


def _bt():
    sys.path.insert(0, HERE)
    import build_textbook
    return build_textbook


def _ssot():
    sys.path.insert(0, HERE)
    import generate
    return generate.load_ssot()


def _roadmap(ssot):
    rows = []
    for u in ssot.units:
        href = "../textbook/" + ("appendix.html" if u.id == "A" else f"unit-{int(u.id):02d}.html")
        opt = ' <span class="u">(optional)</span>' if u.optional else ""
        lessons = " · ".join(f"{l.id} {_html.escape(l.title)}" for l in u.lessons)
        rows.append(
            f'<section class="ug"><h3><a href="{href}">Unit {u.id}: {_html.escape(u.title)}</a>{opt}</h3>'
            f'<p>{_html.escape(u.description)}</p>'
            f'<p class="u"><b>Builds on:</b> {_html.escape(u.prerequisites)}</p>'
            f'<p class="u"><b>Lessons:</b> {lessons}</p></section>')
    return "\n".join(rows)


def build_site(ssot):
    bt = _bt()
    body = f"""<p class="subtitle">A self-paced path through Algebra 1 for an adult learner who knows arithmetic.
Work with the tutor, read the textbook, and practice — in order, or jump to what you need.</p>

<h2>How to use this course</h2>
<ul>
<li><b>The tutor</b> teaches one-on-one: it asks before it tells, checks every answer, and never rushes you. Ask it to start at the beginning, jump to a topic, or place you with a few quick questions.</li>
<li><b>The textbook</b> (linked per unit below) has the worked examples, practice, and figures to read alongside.</li>
<li><b>The Progress Card</b> is how you pick up where you left off: paste last session's card at the start of the next, and keep the <b>Due for review</b> line so old skills get mixed back in.</li>
<li><b>Photos welcome:</b> snap your handwritten work and upload it — the tutor reads it back to confirm, then helps.</li>
</ul>

<h2>Reference codes</h2>
<p>Every worked example, practice problem, definition, and figure has a short code like <code>12.5.w2</code> (worked example 2 of lesson 12.5), <code>1.1.d3</code> (a definition), or <code>12.6.f1</code> (a figure). Quote one to the tutor — "explain 12.5.w2" — and it will pull that exact item up, re-check the math, and walk you through it.</p>

<h2>The roadmap</h2>
{_roadmap(ssot)}
"""
    return {"index.html": bt._page("Algebra 1 — Student Guide", body, None, None),
            "textbook.css": bt.CSS}


def generate():
    os.makedirs(OUT_DIR, exist_ok=True)
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
            issues.append(f"{name}: missing (run build_student_guide.py)")
        elif open(p, encoding="utf-8").read() != content:
            issues.append(f"{name}: stale (run build_student_guide.py)")
    return issues


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if a.check:
        iss = check()
        if iss:
            print("FAIL:\n  " + "\n  ".join(iss)); return 1
        print("student-guide: current."); return 0
    n = generate(); print(f"generated {n} student-guide files -> {os.path.relpath(OUT_DIR, REPO_ROOT)}/"); return 0


if __name__ == "__main__":
    sys.exit(main())
