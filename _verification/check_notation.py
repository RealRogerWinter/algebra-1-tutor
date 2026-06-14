"""Check that no inline LaTeX leaked outside $$...$$ display blocks in the shipped skill.

For each markdown file under algebra-1-tutor/ (excluding SKILL.md, which intentionally
documents the \\( \\) forms as 'do not use'), strip $$...$$ blocks and fenced code blocks,
then flag any remaining inline-LaTeX delimiters or backslash macros.
"""
import glob, os, re

ROOT = r"C:\Users\18084\algebra\algebra-1-tutor"
issues = 0
files = sorted(glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True))

DELIMS = ["\\(", "\\)", "\\[", "\\]"]
MACRO = re.compile(r"\\[a-zA-Z]+")

for fp in files:
    base = os.path.basename(fp)
    if base == "SKILL.md":
        continue
    s = open(fp, encoding="utf-8").read()
    # remove $$...$$ display blocks (DOTALL) and fenced code blocks ```...```
    stripped = re.sub(r"\$\$.*?\$\$", " ", s, flags=re.DOTALL)
    stripped = re.sub(r"```.*?```", " ", stripped, flags=re.DOTALL)

    found = []
    for d in DELIMS:
        if d in stripped:
            found.append(d)
    macros = set(MACRO.findall(stripped))
    if found or macros:
        issues += 1
        rel = os.path.relpath(fp, ROOT)
        if found:
            print(f"{rel}: inline delimiters present: {found}")
        if macros:
            print(f"{rel}: leftover inline macros: {sorted(macros)}")

if issues == 0:
    print("Clean: no inline LaTeX leaks outside $$ blocks in any shipped reference/unit file.")
else:
    print(f"\n{issues} file(s) with inline-LaTeX leaks.")
