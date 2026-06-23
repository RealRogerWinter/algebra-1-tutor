import zipfile
import build_skill as bs


def test_skill_zip_current():
    assert bs.check() == []          # committed .zip matches the source folder file-for-file


def test_zip_has_key_content():
    z = zipfile.ZipFile(bs.ZIP_FILE)
    names = {n.replace("\\", "/") for n in z.namelist()}
    assert "algebra-1-tutor/SKILL.md" in names
    assert "algebra-1-tutor/references/sources.md" in names      # bundled reference pack
    figs = [n for n in names if "/figures/" in n]
    assert sum(1 for n in figs if n.endswith(".svg")) == 31       # deterministic SVGs
    assert sum(1 for n in figs if n.endswith(".html")) == 41      # viz-figure artifacts
    assert z.testzip() is None
