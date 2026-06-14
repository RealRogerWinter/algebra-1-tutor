# _verification/tests/test_check_alignment.py
import subprocess, sys, os
import check_alignment as ca

def test_main_green_on_repo():
    assert ca.main() == 0

def test_cli_exit_zero():
    r = subprocess.run([sys.executable,
                        os.path.join(ca.HERE, "check_alignment.py")])
    assert r.returncode == 0
