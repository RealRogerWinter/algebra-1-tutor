# _verification/tests/test_generate.py
import subprocess, sys, os, shutil
import generate


def test_load_ssot_shape():
    ssot = generate.load_ssot()
    assert len(ssot.units) == 13                       # 12 units + appendix A
    total = sum(len(u.lessons) for u in ssot.units)
    assert total == 50                                  # 47 core + 3 appendix
    u5 = next(u for u in ssot.units if u.id == "5")
    assert u5.title == "Linear Functions & Their Graphs"
    assert [l.id for l in u5.lessons][0] == "5.1"
    appA = next(u for u in ssot.units if u.id == "A")
    assert appA.optional is True


def test_unit_ids_normalized_to_str():
    ssot = generate.load_ssot()
    assert {u.id for u in ssot.units} == {str(n) for n in range(1, 13)} | {"A"}


def test_render_units_table_normalizes(tmp_path):
    ssot = generate.load_ssot()
    body = generate.render_map_table(ssot)
    assert "x²" in body and "x^2" not in body
    assert "**Proportional Reasoning (the bridge to linearity)**" in body
    assert "*(optional, off the main path)*" in body          # appendix row


def test_marker_rewrite_is_idempotent(tmp_path):
    f = tmp_path / "doc.md"
    f.write_text("pre\n<!-- BEGIN GENERATED: x -->\nOLD\n<!-- END GENERATED: x -->\npost\n",
                 encoding="utf-8")
    generate.write_region(str(f), "x", "NEW\nLINES")
    once = f.read_text(encoding="utf-8")
    generate.write_region(str(f), "x", "NEW\nLINES")
    assert f.read_text(encoding="utf-8") == once
    assert "NEW\nLINES" in once and "OLD" not in once


def test_missing_marker_raises(tmp_path):
    f = tmp_path / "doc.md"
    f.write_text("no markers here\n", encoding="utf-8")
    try:
        generate.write_region(str(f), "x", "NEW")
        assert False, "expected error"
    except ValueError as e:
        assert "marker" in str(e).lower()


def test_generate_then_check_is_clean():
    generate.generate()                                        # write regions
    r = subprocess.run([sys.executable, os.path.join(generate.HERE, "generate.py"), "--check"])
    assert r.returncode == 0


def test_run_checks_clean_on_repo():
    assert generate.run_checks() == []


def test_check_detects_md_title_drift(monkeypatch):
    ssot = generate.load_ssot()
    next(u for u in ssot.units if u.id == "5").title = "WRONG TITLE"
    monkeypatch.setattr(generate, "load_ssot", lambda *a, **k: ssot)
    assert any("WRONG TITLE" in i or "Unit 5" in i for i in generate.run_checks())


def test_check_detects_stale_region(tmp_path, monkeypatch):
    # corrupt a generated region, then --check must fail
    import shutil
    bak = MAP_MD = generate.MAP_MD
    original = open(generate.MAP_MD, encoding="utf-8").read()
    try:
        corrupt = original.replace("<!-- END GENERATED: units-at-a-glance -->",
                                   "| 99 | **BOGUS** | x | y |\n<!-- END GENERATED: units-at-a-glance -->")
        open(generate.MAP_MD, "w", encoding="utf-8", newline="\n").write(corrupt)
        assert any("stale" in i.lower() or "units-at-a-glance" in i for i in generate.run_checks())
    finally:
        open(generate.MAP_MD, "w", encoding="utf-8", newline="\n").write(original)
