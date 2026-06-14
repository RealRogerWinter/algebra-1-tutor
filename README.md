# Algebra 1 Tutor — a Claude Agent Skill

An interactive, one-on-one **Algebra 1 tutor** that runs inside **Claude.ai** and the **Claude desktop & mobile apps** as an uploadable [Agent Skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview). It teaches the full Algebra 1 course to an adult learner who is comfortable with arithmetic but meeting algebra for the first time.

It is patient and plain-spoken (not gushing), works Socratically (asks before telling), diagnoses the *specific* misconception behind a wrong answer, renders math in LaTeX, draws graphs as computed artifacts, and carries progress across sessions with a copy‑paste **Progress Card**.

> Built with the [skill-creator](https://github.com/anthropics/skills) workflow. Every answer key is machine‑verified with `sympy`.

---

## Install (Claude.ai / Claude app)

1. Download **`algebra-1-tutor.zip`** from this repo.
2. In Claude.ai: **Settings → Capabilities** → turn on **code execution**, then **Settings → Features** → **upload the `.zip`** under Skills.
   - Requires a paid plan (Pro / Max / Team / Enterprise) with code execution enabled. Custom skills are per‑user.
3. Open a chat and start, e.g.:
   - *"I'd like to learn algebra from the beginning."*
   - *"Help me with slope and y = mx + b, I have a test Friday."*
   - *"Solve 8 − 2x = 14 with me."*
   - Paste a **Progress Card** to resume a previous session.

The skill triggers on algebra topics even when the word "algebra" isn't used (e.g. "solve for x", "factor this", "what's a function").

---

## What it does

- **Teaches the whole course** — 12 units from foundations to a quadratics capstone, plus an optional statistics appendix (see [docs/CURRICULUM.md](docs/CURRICULUM.md)).
- **Go in order or jump anywhere** — every unit declares its prerequisites, so jumping to "slope" is safe; the tutor patches gaps instead of forcing a restart.
- **Diagnoses misconceptions** — reads the *specific* wrong answer (e.g. inverting rise/run, dropping a negative, reading `=` as "compute") and repairs it with a targeted question and a fresh representation, rather than just marking it wrong.
- **Verifies before asserting** — checks every answer by substitution or the code sandbox before calling it right or wrong, and assumes the *student* may be right on a disagreement. No confidently mis-graded correct answers.
- **Shows the math** — LaTeX notation (`$$…$$` / `\(…\)`) and graphs (number lines, lines, parabolas, inequality regions) as **computed SVG/HTML artifacts** with labeled axes and a companion table.
- **Remembers across sessions** — emits a Progress Card you paste back next time, since Claude conversations are otherwise stateless.

---

## How it teaches (design in brief)

- **Concrete → pictorial → symbolic** — a balance scale for equations, money/debt and a number line for negatives, an input‑output machine for functions, then the symbols.
- **Ask before telling**, with a graduated hint ladder that still honors "just tell me."
- **Backward‑faded worked examples** — show one fully, then hand back more of the work as the student gets fluent.
- **Check understanding by transfer**, not "does that make sense?"
- **Encouragement decoupled from correctness** — acknowledge effort plainly; never praise a wrong result.

Full rationale and file layout: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

---

## Repository layout

```
.
├── algebra-1-tutor/            # The skill itself (this is what gets packaged/uploaded)
│   ├── SKILL.md                #   Operating manual: persona, pedagogy, verification, notation, navigation
│   └── references/
│       ├── curriculum-map.md   #   Unit list, prerequisite graph, placement check
│       ├── misconceptions.md   #   Diagnostic bank (tells, hinge questions, repairs)
│       ├── metaphors.md        #   ≥2 explanations per hard concept
│       ├── visuals.md          #   Artifact recipes + coordinate rules for graphs
│       ├── pedagogy.md         #   Concreteness-fading & faded-example scripts
│       └── units/              #   One file per unit (12 units + optional stats appendix)
├── docs/                       # Project documentation
│   ├── CURRICULUM.md
│   ├── ARCHITECTURE.md
│   └── DEVELOPMENT.md
├── _verification/              # Build tooling (NOT shipped in the skill)
│   ├── verify_answers.py       #   sympy re-check of every answer key
│   ├── unit-*.json             #   Machine-checkable problem/answer data per unit
│   ├── AUTHOR_GUIDE.md         #   Template/spec the unit files follow
│   └── ...
├── algebra-1-tutor.zip         # Built, installable skill package
└── README.md
```

---

## Built and verified

Every computational practice problem and worked‑example result is stored in machine‑readable form (`_verification/unit-*.json`) and checked with `sympy`:

```bash
python _verification/verify_answers.py
# Total problems: 765 | auto-checked: 543 | manual (skipped): 222
# Failures: 0
```

The "manual" problems are conceptual (classify-a-number, function-or-not, word‑problem setups) and are answered in the lesson files but not auto-checkable.

See [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) for how to edit content, re‑verify, and repackage.

---

## Why it's built this way (platform constraints)

The design works around verified constraints of the Claude.ai / app surface:

- **No native image generation**, and raw SVG in a chat message doesn't render → graphs are emitted as **Artifacts** with computed coordinates.
- **LaTeX renders** with `$$…$$` and `\(…\)` (avoid lone `$…$`; escape currency `\$`).
- **Conversations are stateless** across chats → the **Progress Card** carries progress.
- **A 12-unit course can't live in one file** → a lean `SKILL.md` plus per‑unit reference files loaded on demand (progressive disclosure).

---

## Status

Functional and verified. The tutoring behavior was validated through simulated student sessions; the real proof is live use on Claude.ai. Feedback and adjustments welcome.
