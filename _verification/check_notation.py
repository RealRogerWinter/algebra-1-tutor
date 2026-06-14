"""Check that no inline LaTeX leaked outside $$...$$ display blocks in the shipped skill.

For each markdown file under algebra-1-tutor/ (excluding SKILL.md, which intentionally
documents the \\( \\) forms as 'do not use'), strip $$...$$ blocks and fenced code blocks,
then flag any remaining inline-LaTeX delimiters or backslash macros.

Importable: call check(root=None) -> list[str] of issue messages (empty == clean).
"""
import glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ROOT = os.path.join(os.path.dirname(HERE), "algebra-1-tutor")

DELIMS = ["\\(", "\\)", "\\[", "\\]"]
MACRO = re.compile(r"\\[a-zA-Z]+")


def check(root=None):
    """Return a list of issue strings (empty list == clean)."""
    root = root or DEFAULT_ROOT
    issues = []
    files = sorted(glob.glob(os.path.join(root, "**", "*.md"), recursive=True))
    for fp in files:
        if os.path.basename(fp) == "SKILL.md":
            continue
        s = open(fp, encoding="utf-8").read()
        stripped = re.sub(r"\$\$.*?\$\$", " ", s, flags=re.DOTALL)
        stripped = re.sub(r"```.*?```", " ", stripped, flags=re.DOTALL)
        stripped = re.sub(r"`[^`\n]*`", " ", stripped)  # inline code spans render literally
        found = [d for d in DELIMS if d in stripped]
        macros = sorted(set(MACRO.findall(stripped)))
        rel = os.path.relpath(fp, root)
        if found:
            issues.append(f"{rel}: inline delimiters present: {found}")
        if macros:
            issues.append(f"{rel}: leftover inline macros: {macros}")
    return issues


def main():
    issues = check()
    if not issues:
        print("Clean: no inline LaTeX leaks outside $$ blocks in any shipped reference/unit file.")
        return 0
    for i in issues:
        print(i)
    print(f"\n{len(issues)} issue(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
