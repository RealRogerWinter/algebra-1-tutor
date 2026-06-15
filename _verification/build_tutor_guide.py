"""Generate the tutor-guide complementary-problem site from the verified T-tier datastore (build
tooling). Same chrome and CSS as the textbook — a left unit rail, a hero, and prev/next nav — so the
guide reads as part of the same book. Each unit is a page of fresh, parallel-form problems with
collapsible worked solutions; there is a How-to-use intro and a catalog index. Data from
_verification/complementary/*.json (REBUILD_BRIEF R1).

  python _verification/build_tutor_guide.py            # (re)generate docs/tutor-guide/
  python _verification/build_tutor_guide.py --check    # verify committed pages are current
"""
import argparse, html as _html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
COMP_DIR = os.path.join(HERE, "complementary")
OUT_DIR = os.path.join(REPO_ROOT, "docs", "tutor-guide")

TOP = [("how-to-use.html", "How to use this guide"), ("index.html", "All units")]

# --- new prose (course house voice; copyedited) --------------------------------------------------
INDEX_LEDE = ("Extra practice for every unit: fresh problems built in the same shapes as the "
              "textbook's, each with a full worked solution you open once you've tried it yourself. "
              "Every unit also closes with a mixed-review set for keeping earlier skills sharp.")

UNIT_SUBTITLE = ("Fresh, parallel-form problems with full worked solutions — more reps for the "
                 "skills in this unit, kept separate from the textbook's own problems.")

HOWTO_BODY = """<p>This guide is a bank of extra practice. For the lessons in the course, it has fresh problems built in the same shape as the ones in the textbook, so you can keep working a skill until it feels steady. Each problem comes with a full worked solution behind a reveal: try the problem first, then open the solution to check your reasoning, not just your final answer.</p>
<p>The quickest way to use it is with the tutor. Ask Claude for a few problems like the ones in Lesson 5.4, or quote a problem's code, and it will work through it with you and check the math. You can also read a unit's page here and work straight down it on paper.</p>
<p>Every problem carries a short code, like <code>5.4.T1</code>. The <code>T</code> marks it as a tutor-guide problem, kept separate from the textbook's own numbering so the two never collide. Quote a code to the tutor to point at one exact problem.</p>
<p>Each unit ends with a <b>mixed-review set</b>, with codes like <code>5.R.T1</code>. These mix skills from across the unit on purpose, so two problems in a row rarely call for the same first move. That kind of mixed, spaced practice feels harder than a page of look-alikes, and it's what makes a skill last to next week. Reach for a review set when a unit feels solid, or to warm up after a few days away.</p>
<p>The matching lessons, worked examples, and figures live in the <a href="../textbook/index.html">textbook</a>, and the <a href="../student-guide/index.html">student guide</a> lays out the whole path through the course.</p>"""


def _bt():
    sys.path.insert(0, HERE)
    import build_textbook
    return build_textbook


def _ssot():
    sys.path.insert(0, HERE)
    import generate
    return generate.load_ssot()


def _ufname(uid):
    return "appendix.html" if str(uid) == "A" else f"unit-{int(uid):02d}.html"


def _comp_file(uid):
    name = "appendix.json" if uid == "A" else f"unit-{int(uid):02d}.json"
    p = os.path.join(COMP_DIR, name)
    return json.load(open(p, encoding="utf-8"))["problems"] if os.path.exists(p) else []


def _render_text(s):
    """Plain prompt/solution text -> HTML: escape (so <,&,> in $$ survive to KaTeX), keep $$ blocks,
    paragraph-break on blank lines, <br> on single newlines."""
    s = _html.escape(s, quote=False)
    paras = re.split(r"\n\s*\n", s.strip())
    return "\n".join(f"<p>{p.replace(chr(10), '<br>')}</p>" for p in paras if p.strip())


def _problem_html(p):
    code = _html.escape(str(p.get("id", "")))
    prompt = _render_text(str(p.get("prompt", "")))
    sol = _render_text(str(p.get("solution", "")))
    ans = _html.escape(str(p.get("answer", "")))
    return (f'<div class="tproblem" id="{code}">\n'
            f'<a class="refcode" href="#{code}">{code}</a>\n{prompt}\n'
            f'<details class="answers"><summary><span class="tw"></span>'
            f'<span class="eyebrow">Worked solution</span>'
            f'<span class="hint">Try it first, then open.</span></summary>\n'
            f'<div class="ak-body">\n{sol}\n<p class="ans"><b>Answer:</b> {ans}</p></div></details>\n</div>')


def _unit_body(u):
    probs = _comp_file(u.id)
    by_lesson, review = {}, []
    for p in probs:
        pid = str(p.get("id", ".."))
        mid = pid.split(".")[1] if "." in pid else ""
        (review if mid == "R" else by_lesson.setdefault(f"{u.id}.{mid}", [])).append(p)
    label = "Appendix" if u.id == "A" else f"Unit {u.id}"
    out = [f'<p class="tset"><a class="xref" href="../textbook/{_ufname(u.id)}">Read {label} in the textbook &rarr;</a></p>']
    for l in u.lessons:
        items = by_lesson.get(l.id, [])
        if not items:
            continue
        out.append(f'<section class="tset"><h2>Lesson {l.id}: {_html.escape(l.title)}</h2>\n'
                   + "\n".join(_problem_html(p) for p in items) + "</section>")
    if review:
        out.append('<section class="tset"><h2>Mixed review</h2>\n'
                   '<p class="subtitle">Problems that mix skills from across the unit — good for spacing earlier work back in.</p>\n'
                   + "\n".join(_problem_html(p) for p in review) + "</section>")
    return "\n".join(out) if len(out) > 1 else "<p>(No complementary problems yet.)</p>"


def build_site(ssot):
    bt = _bt()
    order = ssot.units
    model = [{"id": str(u.id), "title": u.title, "overview": _ufname(u.id), "lessons": []} for u in order]

    seq = [("how-to-use.html", "How to use this guide"), ("index.html", "All units")]
    seq += [(_ufname(u.id), "Appendix" if u.id == "A" else f"Unit {u.id}") for u in order]
    posn = {fn: k for k, (fn, _l) in enumerate(seq)}

    def around(fn):
        k = posn[fn]
        return (seq[k - 1] if k > 0 else None), (seq[k + 1] if k + 1 < len(seq) else None)

    def page(title, body, cur, *, subtitle="", hero=None, kicker=""):
        pl, nl = around(cur)
        return bt._lesson_page(title, body, model, cur, pl, nl, subtitle=subtitle, surface="tutor",
                               hero=hero, kicker=kicker, sidebar_top=TOP, home_href="../index.html")

    files = {"textbook.css": bt.CSS}
    files["how-to-use.html"] = page("How to use the tutor guide", HOWTO_BODY, "how-to-use.html",
                                    kicker="Start here")

    items = []
    for u in order:
        n = len(_comp_file(u.id))
        label = "Appendix" if u.id == "A" else f"Unit {u.id}"
        items.append(f'<li><a href="{_ufname(u.id)}"><b>{label}</b> · {_html.escape(u.title)}</a>'
                     f'<br><span class="u">{n} problems</span></li>')
    idx_body = '<ul class="units">' + "\n".join(items) + "</ul>"
    files["index.html"] = page("Extra practice", idx_body, "index.html", subtitle=INDEX_LEDE,
                               hero="../assets/steps.jpg", kicker="Tutor guide")

    for u in order:
        kicker = "Tutor guide · " + ("Appendix" if u.id == "A" else f"Unit {u.id}")
        hero = f"../assets/{bt._UNIT_HERO.get(str(u.id), 'lines')}.jpg"
        files[_ufname(u.id)] = page(u.title, _unit_body(u), _ufname(u.id), subtitle=UNIT_SUBTITLE,
                                    hero=hero, kicker=kicker)
    return files


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
            issues.append(f"{name}: missing (run build_tutor_guide.py)")
        elif open(p, encoding="utf-8").read() != content:
            issues.append(f"{name}: stale (run build_tutor_guide.py)")
    return issues


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if a.check:
        iss = check()
        if iss:
            print("FAIL:\n  " + "\n  ".join(iss)); return 1
        print(f"tutor-guide: {len(build_site(_ssot()))} files current."); return 0
    n = generate(); print(f"generated {n} tutor-guide files -> {os.path.relpath(OUT_DIR, REPO_ROOT)}/"); return 0


if __name__ == "__main__":
    sys.exit(main())
