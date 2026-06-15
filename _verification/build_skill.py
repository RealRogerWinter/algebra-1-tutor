"""Package the shipped skill folder into algebra-1-tutor.skill + .zip (build tooling).

The .zip is the installable artifact (committed); the .skill is a gitignored duplicate. Bundles
everything under algebra-1-tutor/ (SKILL.md, references/, the Phase-3 figures/, the reference pack).
`--check` confirms the committed .zip matches the source folder file-for-file (content comparison,
not zip-container bytes, so it's stable across OS/zlib).

  python _verification/build_skill.py            # rebuild .skill + .zip from algebra-1-tutor/
  python _verification/build_skill.py --check    # verify committed .zip is current
"""
import argparse, glob, os, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
SKILL_DIR = os.path.join(REPO_ROOT, "algebra-1-tutor")
SKILL_FILE = os.path.join(REPO_ROOT, "algebra-1-tutor.skill")
ZIP_FILE = os.path.join(REPO_ROOT, "algebra-1-tutor.zip")
EXCLUDE = ("__pycache__", ".DS_Store", "Thumbs.db")
_TEXT_EXT = (".md", ".svg", ".txt", ".html")


def _files():
    out = []
    for p in glob.glob(os.path.join(SKILL_DIR, "**", "*"), recursive=True):
        if os.path.isfile(p) and not p.endswith(".pyc") and not any(x in p for x in EXCLUDE):
            rel = "algebra-1-tutor/" + os.path.relpath(p, SKILL_DIR).replace("\\", "/")
            out.append((rel, p))
    return sorted(out)


def _read_norm(p):
    """Read bytes; normalize text files to LF so the package is deterministic regardless of the
    working-tree's line endings (Windows autocrlf vs LF)."""
    b = open(p, "rb").read()
    return b.replace(b"\r\n", b"\n") if p.endswith(_TEXT_EXT) else b


def build():
    files = _files()
    for target in (SKILL_FILE, ZIP_FILE):
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
            for rel, p in files:
                zi = zipfile.ZipInfo(rel, date_time=(1980, 1, 1, 0, 0, 0))
                zi.compress_type = zipfile.ZIP_DEFLATED
                zi.external_attr = 0o644 << 16
                z.writestr(zi, _read_norm(p))
    return len(files)


def check():
    if not os.path.exists(ZIP_FILE):
        return ["algebra-1-tutor.zip missing (run build_skill.py)"]
    issues = []
    z = zipfile.ZipFile(ZIP_FILE)
    if z.testzip() is not None:
        issues.append("zip is corrupt")
    names = {n.replace("\\", "/") for n in z.namelist()}
    if "algebra-1-tutor/SKILL.md" not in names:
        issues.append("SKILL.md missing from zip")
    files = _files()
    src = {rel for rel, _ in files}
    for rel, p in files:
        if rel not in names:
            issues.append(f"{rel}: in source dir but not in zip (run build_skill.py)")
        elif z.read(rel) != _read_norm(p):
            issues.append(f"{rel}: content differs from source (run build_skill.py)")
    for n in sorted(names - src):
        issues.append(f"{n}: in zip but not in source dir (run build_skill.py)")
    return issues


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if a.check:
        iss = check()
        if iss:
            print("FAIL:\n  " + "\n  ".join(iss)); return 1
        print(f"skill package: algebra-1-tutor.zip current ({len(_files())} files)."); return 0
    n = build(); print(f"built algebra-1-tutor.skill + .zip ({n} files)."); return 0


if __name__ == "__main__":
    sys.exit(main())
