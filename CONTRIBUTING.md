# Contributing

Thanks for helping improve this Algebra 1 course. Useful contributions include fixing a wrong answer or a typo, making an explanation clearer, improving a figure, or strengthening the tooling. The math is machine-checked and the four published surfaces are kept in sync by CI, so this guide is mostly about working *with* that machinery.

By contributing you agree to the [Code of Conduct](CODE_OF_CONDUCT.md). Content changes are licensed CC BY-NC 4.0 and code changes MIT (see [LICENSE](LICENSE)).

## Setup

```bash
git clone https://github.com/RealRogerWinter/algebra-1-tutor.git
cd algebra-1-tutor
pip install -r requirements.txt
python -m pytest _verification/tests        # confirm a clean checkout is green
```

Python 3.11 is what CI uses.

## How the project fits together

One structural source of truth, two prose copies, generated outputs, and a CI gate that keeps them aligned. The full picture (with a data-flow diagram) is in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md). The short version:

- `curriculum.yaml` defines units, lessons, and prerequisites.
- Each lesson has a **tutor copy** (`algebra-1-tutor/references/units/`) the skill reads, and a **student copy** (`textbook-src/`) the textbook is built from.
- Answers live as machine-checkable data in `_verification/unit-*.json` (and `complementary/*.json` for the tutor guide).
- The `build_*.py` scripts generate the skill `.zip` and the website under `docs/`.

### The dual-source rule (important)

The tutor copy and the student copy are different prose for different readers — the tutor file is guidance for the AI; the textbook file is warm writing for a person. But they must agree on **the math, the answers, the lesson and section structure, and every reference code.** `check_textbook_src.py` guards that they match and that tutor-only notes don't leak into the textbook.

One sharp edge: **CI does not cross-check your lesson `.md` numbers against the answer JSON** (apart from a narrow line-intercept lint). If you change a problem in a lesson without updating the JSON — or change one copy and not the other — the build can stay green while the math is wrong. Change the tutor copy, the student copy, and the JSON together, and read your own math carefully.

## Editing or adding a lesson

1. Edit the **tutor** unit file (`algebra-1-tutor/references/units/unit-NN-*.md`) following [`_verification/AUTHOR_GUIDE.md`](_verification/AUTHOR_GUIDE.md).
2. Mirror the change in the **student** copy (`textbook-src/unit-NN-*.md`) in the house voice (below), keeping the math, answers, and reference codes identical.
3. Update `_verification/unit-NN.json` for any computational problem you changed or added.
4. **Structural change?** (new or renamed lesson, and so on) Update `curriculum.yaml` and the `.md` headers, run `python _verification/generate.py` to refresh the tables, and fix any hardcoded count in `_verification/tests/test_generate.py`.
5. Verify and regenerate (the two sections below).

## Reference codes

Every referenceable item has a short, stable code. The grammar:

- **Lesson items:** `scope.lesson.tag+index`, where scope is `1`–`12` or `A`. A bare trailing number is a practice problem (`5.5.6`); a letter tag marks the type — `w` worked example, `ex` inline example, `d` definition, `c` transfer check, `h` how-to, `f` figure. Examples: `12.1.w1`, `1.1.d3`, `1.2.f1`, `5.4.c2`.
- **Refreshers:** `refA.4`, `refB.10`.
- **Global banks:** `mis.N` (misconception), `vis.tN` (visual template), `met.<slug>` (metaphor).
- **Tutor practice tier:** `scope.lesson.T<n>` and `scope.R.T<n>` (unit mixed review).

Rules:

- **Append-only.** A code is a permanent reference. Assign the next free index in document order; never renumber an existing one.
- **Worked-example and practice codes are assigned by document position** at build time. Reordering, inserting, or dropping a numbered item silently shifts every code after it.
- Anchors are written `{#code}` (plain text, no backslash). Never anchor a `# Unit` or `## Lesson` header — the generator parses those lines.
- `md_anchor_lint` (in `check_alignment.py`) enforces the grammar, global uniqueness, and dense per-group indices.

## House voice (student-facing prose)

The textbook is written for one reader: a motivated adult, comfortable with arithmetic, meeting algebra for the first time, often anxious about math. Write to *them*.

- Warm, plain, and direct — a knowledgeable person sitting beside the reader. Honest over nice. Lead with the idea, not with how important it is.
- Write to "you," and use contractions. (This is a deliberate override of the usual "no second person" copy rule — it's instructional writing.)
- Teach **concrete → pictorial → symbolic**. Reuse the established metaphors (the balance scale, money and debt, the function machine, the area-model box); don't invent new ones. Every metaphor leaks, so name where it stops being exact.
- Worked examples are reasoning narrated, with the check shown every time.
- Put a "common mix-up" note *after* one clean success, framed as a sensible misreading. Call an *error* common; never rank the *reader*.

Run an anti-AI-tell pass on anything you write:

- No filler or hype words (delve, leverage, robust, seamless, crucial, vital, comprehensive-as-filler, and the like).
- No "it's not X, it's Y" fake-insight flips. (A genuine misconception correction — "= doesn't mean *compute*; it means the two sides balance" — is fine and encouraged.)
- At most one rule-of-three per page; sparing em-dashes; no throat-clearing openers.
- No emoji and no check/cross marks. Write "Correct" or show the substitution.

Notation: display math in `$$ … $$`; inline math in plain Unicode (x², √12, ½); never `\(…\)`, `\[…\]`, or single-`$`; ASCII inside table cells; a bare `$` for currency, away from any `$$` block. `check_notation.py` enforces this for shipped files.

## Figures and images

- **Math-bearing pictures are deterministic.** A graph, number line, or parabola is a spec in `figures.py`, rendered to an accuracy-checked SVG under `algebra-1-tutor/figures/`. To add one: add the spec, regenerate (`python _verification/figures.py`), and place a `{#…fK}` anchor in **both** the tutor and student copies. `figure_lint` requires every anchor to have an SVG and every SVG an anchor.
- **Decorative art is generated.** Hero and concept illustrations are AI-generated JPEGs under `docs/assets/` (CC0), wired in by filename. `gen_illustration.py` produces them; it is intentionally outside CI and reads a Google Gemini key only from a local, git-ignored location. **Never commit a key** (`*.key` and `_imgwork/` are git-ignored).

## Verify, regenerate, and check

```bash
# verify the math
python _verification/verify_answers.py
python _verification/verify_complementary.py

# regenerate outputs you affected
python _verification/build_all.py        # the four sites
python _verification/build_skill.py      # the skill .zip (if you touched algebra-1-tutor/)

# run the guards
python _verification/check_alignment.py
python -m pytest _verification/tests
```

[docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) lists every CI step and the byte-determinism note. A `--check` that reports "stale" means you changed a source but didn't regenerate.

## Pull requests

- Branch off `main`, and keep each PR focused.
- Fill in the checklist in the PR template.
- Make sure the gate is green locally first.
