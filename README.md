# Algebra 1 Tutor

A complete, self-paced **Algebra 1 course** for an adult who knows arithmetic and is meeting the rest of algebra for the first time. It comes in two forms that share one machine-verified source:

1. **A textbook you read in your browser** — free, no account, no install.
2. **An interactive tutor you install into Claude** — a patient one-on-one teacher that works problems with you, diagnoses *why* a wrong answer went wrong, and draws the graphs.

**Read the textbook online: <https://realrogerwinter.github.io/algebra-1-tutor/>**

Every answer in the course is checked with `sympy`, and the whole thing is generated from a single source of truth, so the textbook, the tutor, and the practice sets always agree.

---

## Two ways to use it

### 1. Read the textbook (no account needed)

The full course is a website: **<https://realrogerwinter.github.io/algebra-1-tutor/>**. Worked examples to study, practice with per-question answers you can reveal, computed graphs, and a short reference code beside each item so you can point a tutor at one exact thing. It also includes a **student guide** (how to learn with the course) and a **tutor guide** (extra parallel-form practice).

### 2. Install the interactive tutor in Claude

The tutor is an uploadable [Agent Skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) for **Claude.ai** and the **Claude desktop and mobile apps**.

1. Download **`algebra-1-tutor.zip`** from this repo.
2. In Claude: **Settings → Capabilities** and turn on code execution (recommended), then **Settings → Features** and upload the `.zip` under Skills.
3. Start a chat — for example:
   - *"I'd like to learn algebra from the beginning."*
   - *"Help me with slope and y = mx + b, I have a test Friday."*
   - *"Solve 8 − 2x = 14 with me."*
   - Paste a **Progress Card** to resume a previous session.

**It works on the free plan.** The skill runs on the free tier of Claude (today backed by Sonnet 4.6). Larger models such as Opus tend to tutor better — sharper diagnosis, clearer explanation — but they are not required. Code execution is a recommended enhancement, not a hard requirement: when it is available the tutor runs `sympy` to check answers and compute graphs; when it is not, `SKILL.md` tells the tutor to verify by careful, written-out substitution instead, so it degrades gracefully.

The skill triggers on algebra topics even when you don't say "algebra" (for example "solve for x", "factor this", "what's a function").

---

## What it teaches

13 units and 52 lessons, from foundations to a quadratics capstone, plus a core unit on data and statistics. Full map in [docs/CURRICULUM.md](docs/CURRICULUM.md).

- **Go in order or jump anywhere.** Every unit declares its prerequisites, so jumping to "slope" is safe — the tutor patches gaps instead of forcing a restart.
- **Diagnoses misconceptions.** It reads the *specific* wrong answer (inverting rise over run, dropping a negative, reading `=` as "compute") and repairs it with a targeted question and a fresh representation, rather than just marking it wrong.
- **Verifies before asserting.** It checks every answer before calling it right or wrong, and assumes *you* may be the one who's right on a disagreement. No confidently mis-graded correct answers.
- **Shows the math.** Notation in `$$…$$` LaTeX plus plain Unicode (x², √12, ½) inline, and graphs as computed, labeled artifacts with a companion table.
- **Remembers across sessions** through a copy-paste **Progress Card**, since Claude chats are otherwise stateless.

## How it teaches (design in brief)

- **Concrete → pictorial → symbolic** — a balance scale for equations, money and debt for negatives, an input-output machine for functions, then the symbols.
- **Ask before telling**, with a graduated hint ladder that still honors "just tell me."
- **Backward-faded worked examples** — show one fully, then hand back more of the work as you get fluent.
- **Check understanding by transfer**, not "does that make sense?"
- **Encouragement decoupled from correctness** — acknowledge effort plainly; never praise a wrong result.

Full rationale and file layout: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

---

## How it's built and verified

The course is generated from one source of truth and held correct by a CI gate, so the four surfaces (textbook, tutor skill, student guide, tutor guide) can't silently drift apart.

- `curriculum.yaml` is the structural source of truth (units, lessons, prerequisites).
- Lesson prose lives in two synced copies: tutor-facing (`algebra-1-tutor/references/units/`) and student-facing (`textbook-src/`).
- Every computational answer is stored as machine-readable data and re-derived with `sympy`:

```bash
python _verification/verify_answers.py
# Files checked: 13 | Total problems: 909 | auto-checked: 614 | manual (skipped): 295 | Failures: 0
python _verification/verify_complementary.py
# Complementary files: 13 | problems: 269 | auto-checked: 214 | manual: 55 | failures: 0
```

The "manual" problems are conceptual (classify a number, function-or-not, word-problem setups): answered in the lessons but not auto-checkable. Totals grow as content is added; the invariant that matters is **0 failures**, enforced on every push by [CircleCI](.circleci/config.yml) along with alignment, notation, figure-accuracy, byte-identical-build, and packaging checks plus a pytest suite.

See [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) to edit, re-verify, and repackage, and [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow.

---

## Repository layout

```
.
├── curriculum.yaml             # Source of truth: units, lessons, prerequisites
├── algebra-1-tutor/            # The skill that gets packaged & uploaded (CC BY-NC)
│   ├── SKILL.md                #   Operating manual: persona, pedagogy, verification, notation
│   ├── references/             #   curriculum-map, misconceptions, metaphors, visuals, pedagogy, sources
│   │   └── units/              #   One file per unit (12 numbered + Unit A statistics = 13)
│   └── figures/                #   22 computed, sympy-checked SVG figures (bundled in the skill)
├── textbook-src/               # Student-facing prose for the textbook (same math as the tutor)
├── _verification/              # Build & verification tooling (MIT; not shipped in the skill)
│   ├── build_all.py            #   Regenerate the textbook, student guide, tutor guide, and landing
│   ├── build_skill.py          #   Package algebra-1-tutor/ → algebra-1-tutor.zip
│   ├── verify_answers.py       #   sympy re-check of every answer key
│   ├── verify_complementary.py #   sympy re-check of the tutor-guide practice sets
│   ├── check_alignment.py      #   SSOT / notation / figure / reference-code guards
│   ├── figures.py              #   Computed, accuracy-checked SVG figure library
│   ├── unit-*.json             #   Machine-checkable answers; complementary/ holds the tutor sets
│   ├── AUTHOR_GUIDE.md         #   Unit-file authoring spec
│   └── tests/                  #   pytest suite
├── docs/                       # Generated GitHub Pages site (CC BY-NC) + project docs
│   ├── index.html              #   Landing page
│   ├── textbook/ student-guide/ tutor-guide/   # the generated reader sites
│   ├── assets/                 #   Hero & illustration images (CC0; see assets/README.md)
│   └── ARCHITECTURE.md  DEVELOPMENT.md  CURRICULUM.md
├── algebra-1-tutor.zip         # Built, installable skill package
├── LICENSE  LICENSE-CONTENT    # MIT (code) + CC BY-NC 4.0 (content)
└── README.md
```

---

## Why the skill is built this way (platform constraints)

The design works around verified constraints of the Claude.ai / app surface:

- **No native image generation**, and raw SVG in a chat message doesn't render → graphs are emitted as **Artifacts** with computed coordinates.
- **Only `$$…$$` LaTeX renders dependably** on Claude.ai; inline `\(…\)` and `$…$` often show as raw text → real notation goes in `$$…$$` blocks, inline math is plain Unicode.
- **Conversations are stateless** across chats → the **Progress Card** carries progress.
- **A 13-unit course can't live in one file** → a lean `SKILL.md` plus per-unit reference files loaded on demand.

---

## Contributing

Issues and pull requests are welcome — a wrong answer, a clearer explanation, a better figure. The math is machine-checked and the four surfaces are kept in sync by CI, so start with [CONTRIBUTING.md](CONTRIBUTING.md), which walks the edit-and-verify loop.

## License

Two licenses, by directory:

- **Code and build tooling** — MIT. Covers `_verification/`, `curriculum.yaml`, `requirements.txt`, `.circleci/`. See [LICENSE](LICENSE).
- **Course content** — Creative Commons **CC BY-NC 4.0** (free to share and adapt for non-commercial use, with attribution). Covers `algebra-1-tutor/`, `textbook-src/`, and the `docs/` site. See [LICENSE-CONTENT](LICENSE-CONTENT).
- **AI-generated images** in `docs/assets/` are CC0. See [docs/assets/README.md](docs/assets/README.md).

The course content is original; OpenStax and other sources are cited as further reading, not reproduced.

## Status

Functional, deployed, and verified. The tutoring behavior was validated through simulated student sessions; the real proof is live use on Claude.ai. Feedback and fixes welcome.

> Built with the [skill-creator](https://github.com/anthropics/skills) workflow.
