# Development

How to edit the skill, re‑verify the math, and repackage for upload.

## Prerequisites

- Python 3.11+ with `sympy` (`pip install sympy`).

## Editing lesson content

Each unit is a single file under `algebra-1-tutor/references/units/`. The structure every unit follows (goal, why, new terms, concrete→pictorial→symbolic arc, worked examples, "watch for" misconceptions, visuals, transfer checks, practice, answer key) is specified in
[`_verification/AUTHOR_GUIDE.md`](../_verification/AUTHOR_GUIDE.md).

When you change a practice problem or an answer, **also update the matching entry** in that unit's
`_verification/unit-NN.json` so the verifier stays in sync. Problem kinds:

| kind | meaning | checked by |
|------|---------|-----------|
| `solve` | `eq: "lhs=rhs"`, `var`, `answer` (comma‑sep for multiple roots) | `sympy.solve`, set equality |
| `eval` | a pure‑number expression equals `answer` | algebraic equality |
| `simplify` / `expand` | `expr` is algebraically equal to `answer` | `simplify(expr − answer) == 0` |
| `factor_check` | `answer` multiplies back to `expr` | `expand(answer) == expand(expr)` |
| `manual` | conceptual / not auto‑checkable | skipped (human answer only) |

Expressions use Python syntax: `*` multiply, `**` power, `/` divide, explicit parentheses, single‑letter variables.

## Verify the math

```bash
python _verification/verify_answers.py
```

Expected tail:

```
Total problems: 765 | auto-checked: 543 | manual (skipped): 222
Failures: 0
```

A non‑zero exit lists each failing problem with what it got vs. expected. Fix the lesson file and/or the JSON until it's clean.

## Editing the tutor's behavior

The persona, teaching loop, hint ladder, verification rule, notation rules, visual rules, and Progress Card all live in `algebra-1-tutor/SKILL.md`. The cross‑cutting reference banks (`misconceptions.md`, `metaphors.md`, `visuals.md`, `pedagogy.md`) are read on demand — edit those to change *how* a concept is diagnosed or explained without touching unit content.

Keep `SKILL.md` lean; push detail into reference files. Keep the `description` under 1024 characters and the `name` lowercase‑hyphen (no "claude"/"anthropic").

## Repackage for upload

The packaging helper is from the skill‑creator plugin. On Windows, force UTF‑8 so its console output doesn't choke:

```bash
PYTHONUTF8=1 python -m scripts.package_skill /path/to/algebra-1-tutor /output/dir
```

This validates the skill and writes `algebra-1-tutor.skill` (a zip with the skill folder at root). Claude.ai's uploader expects a `.zip`; the two are byte‑identical, so copying the `.skill` to `.zip` works:

```bash
cp algebra-1-tutor.skill algebra-1-tutor.zip
```

Then re‑upload via **Settings → Features** on Claude.ai to replace the previous version.

## Smoke‑testing behavior

There's no automated test of tutoring *quality* — it's validated by running realistic student prompts through the skill and reading the transcripts. Useful scenarios: a brand‑new learner; a topic jump ("just help me with slope"); a student giving a wrong answer that reveals a known misconception (e.g. dividing `6/−2` and getting `3`); and a graph request (to confirm a correctly‑computed, labeled artifact with a companion table).
