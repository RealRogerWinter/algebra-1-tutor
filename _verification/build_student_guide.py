"""Generate the student guide (build tooling): one warm front page for the course that shares the
textbook's chrome — the same left unit rail (pointed into ../textbook/), a hero, and the shared CSS.
A motivating map, not a second textbook: it explains how to learn with the tutor and the
reference-code system, then lays out the roadmap as cards that link straight into the textbook.

  python _verification/build_student_guide.py            # (re)generate docs/student-guide/
  python _verification/build_student_guide.py --check    # verify the committed page is current
"""
import argparse, html as _html, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
OUT_DIR = os.path.join(REPO_ROOT, "docs", "student-guide")

TOP = [("how-to-use.html", "How to use this book"), ("index.html", "All units")]

HERO_LEDE = ("A self-paced path through Algebra 1, written for an adult who knows arithmetic and is "
             "meeting the rest of it for the first time. Read the textbook, work with the tutor, and "
             "practice — in order, or jump to whatever you need.")


def _bt():
    sys.path.insert(0, HERE)
    import build_textbook
    return build_textbook


def _ssot():
    sys.path.insert(0, HERE)
    import generate
    return generate.load_ssot()


def _roadmap(ssot):
    items = []
    for u in ssot.units:
        href = "../textbook/" + ("appendix.html" if u.id == "A" else f"unit-{int(u.id):02d}.html")
        opt = ' <span class="u">(optional)</span>' if u.optional else ""
        label = "Appendix" if u.id == "A" else f"Unit {u.id}"
        items.append(f'<li><a href="{href}"><b>{label}</b> · {_html.escape(u.title)}</a>{opt}'
                     f'<br><span class="u">{_html.escape(u.description)}</span></li>')
    return '<ul class="units">' + "\n".join(items) + "</ul>"


def build_site(ssot):
    bt = _bt()
    body = f"""<h2>Start here</h2>
<p>This course is built to be read on your own, at whatever pace suits you. Open the <a href="../textbook/how-to-use.html">textbook</a> and start with Lesson 1.1, or jump to the topic you need — each lesson explains itself, with worked examples to study and practice to try. There's no clock and nothing to keep up with.</p>
<p>When you want a hand, ask Claude, your tutor. It has the whole book in front of it, so you can lean on it the way you'd lean on a patient person sitting beside you. Asking for help is part of how this works, not a sign you're behind.</p>

<h2>How the tutor helps</h2>
<p>The tutor teaches one-on-one. A few things it's good for:</p>
<ul>
<li><b>Working a problem with you, one line at a time</b>, so you're doing the thinking instead of watching.</li>
<li><b>Checking every answer</b> before it calls anything right or wrong — and assuming you might be the one who's right.</li>
<li><b>Explaining a different way</b> when the first explanation doesn't land. A second picture often does it.</li>
<li><b>Reading a photo of your handwritten work.</b> Snap a picture of what you wrote on paper; the tutor reads your steps back to confirm, then shows you where a line went sideways, if one did.</li>
<li><b>Giving you more practice</b> when a skill is almost solid and you want a few more to lock it in.</li>
</ul>

<h2>Keeping your place: the Progress Card</h2>
<p>Each conversation with the tutor starts fresh, so you carry your progress between sessions yourself. At a good stopping point, ask for a <b>Progress Card</b> — a short, readable note of where you are and what's next. Paste it back at the start of your next session and the tutor picks up right where you left off. Keep the <b>Due for review</b> line, too: it names a skill or two to mix back in, which is what keeps earlier work from fading.</p>

<h2>Reference codes</h2>
<p>Every worked example, practice problem, definition, and figure has a short code. A code reads as place-then-item: <code>12.5.w2</code> is worked example 2 in Lesson 12.5, <code>5.3.4</code> is practice problem 4 in Lesson 5.3, <code>1.2.f1</code> is a figure, and <code>1.1.d3</code> is a definition. You'll see them beside items in the textbook, where they double as deep links you can bookmark.</p>
<p>Their real use is pointing. Say "explain 12.5.w2" or "walk me through 5.3.4," and the tutor pulls that exact item up and works through it with you, re-checking the math as it goes. The <a href="../tutor-guide/index.html">tutor guide</a>'s extra problems use codes too, with a <code>T</code> in them, like <code>5.4.T1</code>.</p>

<h2>The roadmap</h2>
<p class="subtitle">Twelve units and a statistics appendix, in a sensible order. Each card opens it in the textbook — start at the top, or jump to what you need.</p>
{_roadmap(ssot)}
"""
    page = bt._lesson_page("Your path through Algebra 1", body, bt._ssot_model(ssot), "", None, None,
                           subtitle=HERO_LEDE, surface="guide", hero="../assets/lines.jpg",
                           kicker="Student guide", home_href="../index.html",
                           sidebar_prefix="../textbook/", sidebar_top=TOP)
    return {"index.html": page, "textbook.css": bt.CSS}


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
