"""Verify the complementary (tutor-guide) problem sets — the 'T' tier (build tooling, not shipped).

These are NEW, original problems (parallel forms of the textbook skills, different numbers/contexts)
authored for the tutor guide so the tutor can hand a student a *fresh* similar problem. They live in
their own namespace so codes never collide with textbook codes (REBUILD_BRIEF R1, handoff §5):
  per-lesson : scope.lesson.T<n>   e.g. 5.4.T1, 12.3.T7
  unit review: scope.R.T<n>        e.g. 5.R.T1   (the unit-level mixed-review / interleaving set)

Reuses verify_answers' sympy CHECKERS so every answer is re-derived independently. Each problem also
carries a `prompt` (the statement) and a `solution` (full worked solution) for the tutor guide.

  python _verification/verify_complementary.py            # verify all complementary/*.json
"""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
COMP_DIR = os.path.join(HERE, "complementary")
TID_RE = re.compile(r"^(?:[1-9]|1[0-2]|A)\.(?:\d+|R)\.T\d+$")


def main():
    sys.path.insert(0, HERE)
    import verify_answers as va
    import generate
    units = {u.id: u for u in generate.load_ssot().units}
    lesson_ids = {l.id for u in units.values() for l in u.lessons}
    files = sorted(glob.glob(os.path.join(COMP_DIR, "*.json")))
    total = auto = manual = failed = 0
    issues, seen = [], set()
    for fp in files:
        fn = os.path.basename(fp)
        data = json.load(open(fp, encoding="utf-8"))
        for prob in data["problems"]:
            total += 1
            pid = str(prob.get("id", ""))
            if not TID_RE.match(pid):
                issues.append(f"{fn}: malformed T-id {pid!r}"); continue
            if pid in seen:
                issues.append(f"{fn}: duplicate id {pid}")
            seen.add(pid)
            scope, mid, _ = pid.split(".")
            if mid == "R":
                if scope not in units:
                    issues.append(f"{pid}: unknown unit {scope}")
            elif f"{scope}.{mid}" not in lesson_ids:
                issues.append(f"{pid}: unknown lesson {scope}.{mid}")
            if not str(prob.get("prompt", "")).strip():
                issues.append(f"{pid}: missing prompt")
            if not str(prob.get("solution", "")).strip():
                issues.append(f"{pid}: missing solution")
            kind = prob.get("kind")
            if kind == "manual":
                manual += 1; continue
            auto += 1
            checker = va.CHECKERS.get(kind)
            if checker is None:
                failed += 1; issues.append(f"{pid}: unknown kind {kind!r}"); continue
            try:
                ok, desc = checker(prob)
                if not ok:
                    failed += 1; issues.append(f"{pid}: {desc}")
            except Exception as e:  # noqa
                failed += 1; issues.append(f"{pid}: ERROR {type(e).__name__}: {e}")
    print(f"Complementary files: {len(files)} | problems: {total} | "
          f"auto-checked: {auto} | manual: {manual} | failures: {failed}")
    if issues:
        print("--- ISSUES ---")
        for i in issues[:80]:
            print("  " + i)
        return 1
    print("All complementary problems verified + well-formed. [OK]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
