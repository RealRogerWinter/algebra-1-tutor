import check_textbook_src as cts


def test_textbook_src_no_drift():
    """The student textbook source (textbook-src/) keeps every SSOT-verified item — reference codes,
    lessons, and answer-key values — identical to the tutor lesson source, with no tutor-meta
    leakage or render-breaking notation. This is the only backstop for the .md math in the student
    copy (verify_answers re-checks the JSON, not the .md), so it runs in CI."""
    issues = cts.check()
    assert issues == [], "textbook-src drift from the verified tutor source:\n  " + "\n  ".join(issues)
