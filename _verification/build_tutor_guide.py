"""Generate the tutor-guide complementary-problem pages from the verified T-tier datastore
(build tooling). Look/CSS shared with the textbook. Data from _verification/complementary/*.json
(REBUILD_BRIEF R1). Each problem shows its reference code, the prompt, and a collapsible full
worked solution.

  python _verification/build_tutor_guide.py            # (re)generate docs/tutor-guide/
  python _verification/build_tutor_guide.py --check    # verify committed pages are current
"""
import argparse, glob, html as _html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
COMP_DIR = os.path.join(HERE, "complementary")
OUT_DIR = os.path.join(REPO_ROOT, "docs", "tutor-guide")


def _bt():
    sys.path.insert(0, HERE)
    import build_textbook
    return build_textbook


def _ssot():
    sys.path.insert(0, HERE)
    import generate
    return generate.load_ssot()


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
            f'<span class="eyebrow">Worked solution</span></summary>\n'
            f'<div class="ak-body">\n{sol}\n<p class="ans"><b>Answer:</b> {ans}</p></div></details>\n</div>')


def _unit_page(bt, u, prev_link, next_link):
    probs = _comp_file(u.id)
    by_lesson, review = {}, []
    for p in probs:
        mid = str(p.get("id", "..")).split(".")[1] if "." in str(p.get("id", "")) else ""
        (review if mid == "R" else by_lesson.setdefault(f"{u.id}.{mid}", [])).append(p)
    sections = []
    for l in u.lessons:
        items = by_lesson.get(l.id, [])
        if not items:
            continue
        sections.append(f'<section><h2>Lesson {l.id}: {_html.escape(l.title)}</h2>\n'
                        + "\n".join(_problem_html(p) for p in items) + "</section>")
    if review:
        sections.append('<section><h2>Mixed review (interleaving)</h2>\n'
                        '<p class="subtitle">Problems that mix skills from across the unit.</p>\n'
                        + "\n".join(_problem_html(p) for p in review) + "</section>")
    body = "\n".join(sections) or "<p>(No complementary problems yet.)</p>"
    return bt._page(f"Unit {u.id}: {u.title} — Complementary problems", body, prev_link, next_link,
                    "Tutor guide: fresh, parallel problems with full worked solutions.", surface="tutor")


def build_site(ssot):
    bt = _bt()
    files = {"textbook.css": bt.CSS}
    order = ssot.units
    # index
    items = []
    for u in order:
        href = "appendix.html" if u.id == "A" else f"unit-{int(u.id):02d}.html"
        n = len(_comp_file(u.id))
        items.append(f'<li><a href="{href}"><b>Unit {u.id}</b> · {_html.escape(u.title)}</a> '
                     f'<span class="u">({n} problems)</span></li>')
    idx_body = ('<p class="subtitle">Complementary problem sets for the tutor — original parallel-form '
                'problems (separate from the textbook) with full worked solutions, plus a mixed-review '
                'set per unit for interleaving.</p><ul class="units">' + "\n".join(items) + "</ul>")
    files["index.html"] = bt._page("Algebra 1 — Tutor Guide (Complementary Problems)", idx_body, None, None, surface="tutor")
    for i, u in enumerate(order):
        fname = "appendix.html" if u.id == "A" else f"unit-{int(u.id):02d}.html"
        prev_u = order[i - 1] if i > 0 else None
        next_u = order[i + 1] if i + 1 < len(order) else None
        pl = (("appendix.html" if prev_u.id == "A" else f"unit-{int(prev_u.id):02d}.html"),
              f"Unit {prev_u.id}") if prev_u else None
        nl = (("appendix.html" if next_u.id == "A" else f"unit-{int(next_u.id):02d}.html"),
              f"Unit {next_u.id}") if next_u else None
        files[fname] = _unit_page(_bt(), u, pl, nl)
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
