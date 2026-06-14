"""SSOT generator + checker for the algebra-1-tutor curriculum (build tooling, not shipped).

Generates the marker-bounded data tables in curriculum-map.md and docs/CURRICULUM.md from
curriculum.yaml, and CHECKS the unit .md titles / lesson ids / counts / outline / JSON ids
against the SSOT. `--check` writes nothing and exits non-zero on any drift or staleness.
"""
import argparse, glob, json, os, re, sys
from dataclasses import dataclass, field
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
SSOT_PATH = os.path.join(REPO_ROOT, "curriculum.yaml")
MAP_MD = os.path.join(REPO_ROOT, "algebra-1-tutor", "references", "curriculum-map.md")
CURRIC_MD = os.path.join(REPO_ROOT, "docs", "CURRICULUM.md")
UNIT_MD = os.path.join(REPO_ROOT, "algebra-1-tutor", "references", "units")

@dataclass
class Lesson:
    id: str
    title: str

@dataclass
class Unit:
    id: str
    slug: str
    title: str
    short_title: str
    description: str
    prerequisites: str
    optional: bool
    lessons: list = field(default_factory=list)

@dataclass
class Ssot:
    course: str
    units: list

def load_ssot(path=SSOT_PATH):
    raw = yaml.safe_load(open(path, encoding="utf-8"))
    units = []
    for u in raw["units"]:
        lessons = [Lesson(str(l["id"]), l["title"]) for l in u["lessons"]]
        units.append(Unit(str(u["id"]), u["slug"], u["title"], u["short_title"],
                          u["description"], u["prerequisites"], bool(u["optional"]), lessons))
    return Ssot(raw["course"], units)


def _opt(u, kind):
    if not u.optional:
        return ""
    return " *(optional, off the main path)*" if kind == "map" else " (optional)"

def render_map_table(ssot):
    rows = [f"| {u.id} | **{u.title}**{_opt(u,'map')} | {u.description} | {u.prerequisites} |"
            for u in ssot.units]
    return "\n".join(rows)

def render_curric_table(ssot):
    rows = [f"| {u.id} | {u.title}{_opt(u,'cur')} | {u.description} |"
            for u in ssot.units]
    return "\n".join(rows)

def write_region(path, region_id, body):
    text = open(path, encoding="utf-8").read()
    begin = f"<!-- BEGIN GENERATED: {region_id} -->"
    end = f"<!-- END GENERATED: {region_id} -->"
    pat = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.DOTALL)
    if not pat.search(text):
        raise ValueError(f"missing marker pair for region '{region_id}' in {path}")
    new = pat.sub(lambda _m: begin + "\n" + body + "\n" + end, text)  # function repl: body stays literal
    if new != text:
        open(path, "w", encoding="utf-8", newline="\n").write(new)

def generate():
    ssot = load_ssot()
    write_region(MAP_MD, "units-at-a-glance", render_map_table(ssot))
    write_region(CURRIC_MD, "units-table", render_curric_table(ssot))


H1_RE = re.compile(r"^#\s+(?:Unit\s+(\d+)|Appendix\s+([A-Z])):\s+(.*?)\s*$", re.M)
LESSON_RE = re.compile(r"^##\s+Lesson\s+([0-9A]+\.\d+):\s+(.*?)\s*$", re.M)

def _unit_md_path(uid):
    if uid == "A":
        return os.path.join(UNIT_MD, "appendix-statistics.md")
    hits = glob.glob(os.path.join(UNIT_MD, f"unit-{int(uid):02d}-*.md"))
    return hits[0] if hits else None

def _outline_lesson_ids(text):
    m = re.search(r"^##\s+Lesson-level outline\s*$", text, re.M)
    if not m:
        return set()
    rest = text[m.end():]
    end = re.search(r"^##\s", rest, re.M)
    region = rest[: end.start() if end else len(rest)]
    return set(re.findall(r"^-\s+([0-9A]+\.\d+)\b", region, re.M))

def _region_body(path, region_id):
    text = open(path, encoding="utf-8").read()
    m = re.search(re.escape(f"<!-- BEGIN GENERATED: {region_id} -->") + r"\n(.*?)\n"
                  + re.escape(f"<!-- END GENERATED: {region_id} -->"), text, re.DOTALL)
    return m.group(1) if m else None

def run_checks():
    ssot = load_ssot()
    issues = []
    ssot_lessons = {(u.id, l.id, l.title) for u in ssot.units for l in u.lessons}
    ssot_ids = {l.id for u in ssot.units for l in u.lessons}
    # 1-3: unit .md H1 + lesson headers + counts
    for u in ssot.units:
        path = _unit_md_path(u.id)
        if not path:
            issues.append(f"unit {u.id}: no .md file found"); continue
        text = open(path, encoding="utf-8").read()
        h1 = H1_RE.search(text)
        title = h1.group(3) if h1 else None
        if title != u.title:
            issues.append(f"unit {u.id}: .md H1 title {title!r} != SSOT {u.title!r}")
        md_lessons = LESSON_RE.findall(text)
        if len(md_lessons) != len(u.lessons):
            issues.append(f"unit {u.id}: .md lesson count {len(md_lessons)} != SSOT {len(u.lessons)}")
        for lid, ltitle in md_lessons:
            if (u.id, lid, ltitle) not in ssot_lessons:
                issues.append(f"unit {u.id}: .md lesson {lid} {ltitle!r} not in SSOT")
    # 4: outline ids
    map_text = open(MAP_MD, encoding="utf-8").read()
    outline_ids = _outline_lesson_ids(map_text)
    if outline_ids != ssot_ids:
        issues.append(f"curriculum-map outline ids mismatch: "
                      f"missing={sorted(ssot_ids - outline_ids)} extra={sorted(outline_ids - ssot_ids)}")
    # 5: JSON ids belong to a known lesson
    for fp in (sorted(glob.glob(os.path.join(HERE, "unit-*.json")))
               + sorted(glob.glob(os.path.join(HERE, "appendix*.json")))):
        for prob in json.load(open(fp, encoding="utf-8"))["problems"]:
            pid = str(prob.get("id", ""))
            if pid.startswith("ref"):
                continue                                   # refresher items live under a lesson 2.5
            mm = re.match(r"^([0-9A]+\.\d+)\.", pid)
            if mm and mm.group(1) not in ssot_ids:
                issues.append(f"{os.path.basename(fp)}: id {pid} -> unknown lesson {mm.group(1)}")
    # 6: staleness
    if _region_body(MAP_MD, "units-at-a-glance") != render_map_table(ssot):
        issues.append("curriculum-map.md units-at-a-glance region is stale (run generate.py)")
    if _region_body(CURRIC_MD, "units-table") != render_curric_table(ssot):
        issues.append("docs/CURRICULUM.md units-table region is stale (run generate.py)")
    return issues

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="verify only; write nothing")
    args = ap.parse_args(argv)
    if args.check:
        issues = run_checks()
        if issues:
            print("\n".join(issues)); return 1
        print("alignment: SSOT <-> tables/.md/outline/JSON all consistent."); return 0
    generate()
    print("generated: curriculum-map.md + docs/CURRICULUM.md regions.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
