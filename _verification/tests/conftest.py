import os, sys
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VERIF = os.path.join(REPO_ROOT, "_verification")
sys.path.insert(0, VERIF)  # so tests can `import generate, check_alignment, check_notation`

@pytest.fixture
def repo_root():
    return REPO_ROOT
