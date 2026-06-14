import glob, os

ROOT = r"C:\Users\18084\algebra\algebra-1-tutor\references"
# ordered replacements: clear in-math thin-space marks, then prose marks, then any stragglers
REPL = [
    ("\\ ✓", ""), ("\\ ✗", ""),   # backslash thin-space + mark (inside math)
    (" ✓)", ")"), (" ✗)", ")"),   # mark before a close paren
    (". ✓", "."), (". ✗", "."),    # period space mark
    (" ✓", ""), (" ✗", ""),        # space + mark
    ("✓", ""), ("✗", ""),          # bare mark
]

total = 0
for fp in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
    s = open(fp, encoding="utf-8").read()
    n = s.count("✓") + s.count("✗")
    if n == 0:
        continue
    for a, b in REPL:
        s = s.replace(a, b)
    # tidy any doubled spaces left mid-line (not at line start)
    s = "\n".join(" ".join(part for part in line.split(" ")) if "  " in line else line for line in s.split("\n"))
    open(fp, "w", encoding="utf-8").write(s)
    total += n
    print(f"{os.path.relpath(fp, ROOT)}: removed {n}")

print(f"\nTotal marks removed: {total}")
# confirm none remain
left = sum(open(fp, encoding="utf-8").read().count("✓") + open(fp, encoding="utf-8").read().count("✗")
           for fp in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True))
print("Remaining marks:", left)
