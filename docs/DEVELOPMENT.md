# Development

How to edit the course, re-verify the math, regenerate the site, and repackage the skill. For the why behind the structure, see [ARCHITECTURE.md](ARCHITECTURE.md); for the full contributor workflow and the house voice, see [CONTRIBUTING.md](../CONTRIBUTING.md).

## Prerequisites

- Python 3.11+ (CI uses 3.11).
- `pip install -r requirements.txt` (sympy, PyYAML, pytest, markdown).

## The loop

One source of truth (`curriculum.yaml`) plus lesson prose generate everything else, and a CI gate rebuilds and byte-compares the outputs. So the working loop is: **edit a source → update its answer JSON → verify → regenerate → check.**

## Editing lesson content

Each lesson exists as two synced files: the tutor copy (`algebra-1-tutor/references/units/unit-NN-*.md`) and the student copy (`textbook-src/unit-NN-*.md`). Keep the math, answers, and reference codes identical; the prose differs by design. The unit-file structure is specified in [`_verification/AUTHOR_GUIDE.md`](../_verification/AUTHOR_GUIDE.md).

When you change a practice problem or an answer, **also update the matching entry** in that unit's `_verification/unit-NN.json`. Problem kinds:

| kind | meaning | checked by |
|------|---------|-----------|
| `solve` | `eq: "lhs=rhs"`, `var`, `answer` (comma-separated for multiple roots) | `sympy.solve`, set equality |
| `eval` | a pure-number expression equals `answer` | algebraic equality |
| `simplify` / `expand` | `expr` is algebraically equal to `answer` | `simplify(expr − answer) == 0` |
| `factor_check` | `answer` multiplies back to `expr` | `expand(answer) == expand(expr)` |
| `manual` | conceptual / not auto-checkable | skipped (human answer only) |

Expressions use Python syntax: `*` multiply, `**` power, `/` divide, explicit parentheses, single-letter variables.

> **The `.md` math is only as safe as your eyes.** CI re-checks the JSON against itself with sympy, but it does *not* cross-check your lesson `.md` numbers against the JSON (except a narrow line-intercept lint). If you reword `4x = 20` to `4x = 21` in a lesson without updating the JSON, the build stays green and you've shipped wrong math. Change the lesson, the JSON, and the student copy together.

## Verify the math

```bash
python _verification/verify_answers.py
python _verification/verify_complementary.py
```

Both must end with `Failures: 0`. The headline totals (currently 909 and 269 problems) grow as content is added; the invariant is zero failures. A non-zero exit lists each failing problem with got-versus-expected.

## Regenerate the site and skill

```bash
python _verification/build_all.py     # textbook, student guide, tutor guide, landing
python _verification/build_skill.py   # repackage algebra-1-tutor/ → algebra-1-tutor.zip
```

Don't hand-edit anything under `docs/textbook/`, `docs/student-guide/`, `docs/tutor-guide/`, or `docs/index.html` — they are generated. Edit the source and regenerate.

**Byte-determinism.** CI rebuilds and byte-compares on `cimg/python:3.11`, and the generated HTML must be byte-identical across Python patch versions. If a regenerate produces an unexpected local diff, reproduce CI's interpreter before committing:

```bash
docker run --rm -v "$PWD":/work -w /work cimg/python:3.11 \
  bash -lc "pip install -q -r requirements.txt && python _verification/build_all.py --check"
```

`build_skill.py` writes the `.zip` deterministically (it's the committed, installable package). Re-upload it on Claude.ai or the Claude app (**Customize → Skills → +**, then **Create Skill → Upload a skill**) to replace the previous version. Keep `SKILL.md` lean (push detail into reference files), the `description` under 1024 characters, and the `name` lowercase-hyphen with no "claude" or "anthropic".

## Run the full gate locally

The CI gate ([`.circleci/config.yml`](../.circleci/config.yml)) runs, in order:

```bash
python _verification/verify_answers.py
python _verification/verify_complementary.py
python _verification/generate.py --check
python _verification/check_alignment.py
python _verification/figures.py --check
python _verification/build_textbook.py --check
python _verification/build_tutor_guide.py --check
python _verification/build_skill.py --check
python _verification/build_student_guide.py --check
python _verification/build_landing.py --check
python _verification/smoke_test.py
python -m pytest _verification/tests
```

A `--check` that reports "stale" means you changed a source but didn't regenerate — run the matching `build_*.py`.

## Smoke-testing tutor behavior

There is no automated test of tutoring *quality* — validate it by running realistic prompts through the skill and reading the transcripts: a brand-new learner; a topic jump ("just help me with slope"); a wrong answer that reveals a known misconception (for example computing 6 / −2 as 3); a photo of handwritten work; a reference-code lookup ("explain 12.5.w2"); and a graph request (expect a correctly computed, labeled artifact with a companion table).
