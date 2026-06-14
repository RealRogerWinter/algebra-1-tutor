# _verification/tests/test_notation.py
import os, tempfile, textwrap
import check_notation

def test_clean_tree_has_no_issues():
    issues = check_notation.check()
    assert issues == [], f"unexpected notation leaks: {issues}"

def test_flags_stray_inline_latex(tmp_path):
    d = tmp_path / "algebra-1-tutor" / "references"
    d.mkdir(parents=True)
    (d / "bad.md").write_text("This has inline \\(x+1\\) latex.\n", encoding="utf-8")
    issues = check_notation.check(root=str(tmp_path / "algebra-1-tutor"))
    assert any("bad.md" in str(i) for i in issues)

def test_skill_md_is_excluded(tmp_path):
    d = tmp_path / "algebra-1-tutor"
    d.mkdir(parents=True)
    (d / "SKILL.md").write_text("Documents the \\( ... \\) forbidden form.\n", encoding="utf-8")
    issues = check_notation.check(root=str(d))
    assert issues == []
