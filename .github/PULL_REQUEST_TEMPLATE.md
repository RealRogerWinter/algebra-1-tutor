## What this changes

<!-- One or two plain sentences. -->

## Checklist

- [ ] If I changed a problem or answer, I updated the matching `_verification/unit-NN.json` entry.
- [ ] If I changed a lesson, I kept the tutor source (`algebra-1-tutor/references/units/`) and the student source (`textbook-src/`) in sync — same math, answers, and reference codes.
- [ ] I ran the answer verifiers with 0 failures: `python _verification/verify_answers.py` and `python _verification/verify_complementary.py`.
- [ ] I ran the guards: `python _verification/check_alignment.py` and `python -m pytest _verification/tests`.
- [ ] If I changed generated output, I regenerated it: `python _verification/build_all.py` (and `python _verification/build_skill.py` if I touched `algebra-1-tutor/`).
- [ ] Prose follows the house voice in `CONTRIBUTING.md`.

See [CONTRIBUTING.md](../CONTRIBUTING.md) for the full workflow.
