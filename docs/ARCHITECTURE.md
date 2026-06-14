# Architecture

## Progressive disclosure

A full 12‑unit Algebra 1 course is far too large to inline into a single `SKILL.md`. The skill uses the three‑level loading model that Agent Skills are designed for:

1. **Metadata** (`name` + `description`) — always in context; this is what makes Claude decide to use the skill.
2. **`SKILL.md` body** — loaded when the skill triggers. It is the **operating manual** only: persona, the teaching loop, the verification rule, notation/visual rules, the Progress Card, and how to navigate the course. Kept lean (~200 lines).
3. **Reference files** — loaded on demand. The tutor reads only the unit it's teaching plus whichever cross‑cutting reference it needs, so the whole course never sits in context at once.

```
algebra-1-tutor/
├── SKILL.md                      # operating manual (always-on once triggered)
└── references/
    ├── curriculum-map.md         # read at session start / on a topic jump
    ├── misconceptions.md         # read when diagnosing a wrong answer
    ├── metaphors.md              # read when a first explanation didn't land
    ├── visuals.md                # read before generating any graph
    ├── pedagogy.md               # read for a ready-made teaching sequence
    └── units/unit-NN-*.md        # read the one being taught
```

## The five behavioral pillars (in `SKILL.md`)

1. **Never teach wrong math.** Verify every nontrivial result by substitution or the code sandbox *before* asserting it's right or wrong; on a disagreement, re‑derive and assume the student may be right. This is the highest‑priority rule — a confidently mis‑graded correct answer is the worst failure for a tutor a beginner can't double‑check.
2. **Ask before telling**, via a graduated hint ladder (diagnose → targeted hint → parallel worked example → co‑solve → full solution + fresh practice) that still honors an explicit "just tell me."
3. **Diagnose the misconception**, don't just mark the answer wrong; switch representation rather than repeating the same explanation.
4. **Concrete → pictorial → symbolic** introductions with backward‑faded worked examples; check understanding by transfer.
5. **Plain, honest tone** — patient and never harsh, but matter‑of‑fact, no gushing, no emoji or decorative marks.

## Notation and visuals (platform‑shaped)

- **LaTeX** with `$$…$$` (display) and `\(…\)` (inline). Lone `$…$` is avoided; currency is escaped `\$`. Inline math **must** use backslash‑parens — plain `( … )` is not a math delimiter and renders the raw LaTeX as literal text.
- **Graphs are Artifacts.** There is no image generator on Claude.ai, and raw SVG in a chat message doesn't render. Graphs are emitted as SVG/HTML artifacts with **computed** coordinates (never freehanded — an eyeballed curve is wrong), labeled axes/intercepts/vertex, and a companion point table. Simple number lines may use ASCII/Unicode in‑chat. Recipes and the coordinate‑mapping rule live in `visuals.md`.

## Statelessness → the Progress Card

Claude conversations don't share memory by default, so a linear course needs a resume mechanism. At the end of a session the tutor emits a short, human‑readable **Progress Card** (current lesson, what's mastered, what to watch, last problem, next step, tone preference). The student pastes it back next time. The skill itself holds no per‑student state.

## Correctness pipeline

Lesson content is paired with machine‑readable answer data under `_verification/unit-*.json`. `verify_answers.py` re‑checks every computational answer with `sympy` (solve / eval / simplify / expand / factor_check). The tutor is *also* told to re‑derive and re‑verify live, and to trust live verification over any stored value if they ever disagree — defense in depth against both stored and live errors.

## What ships vs. what doesn't

- **Ships** (packaged into the `.zip`): everything under `algebra-1-tutor/`.
- **Does not ship**: `_verification/` (build tooling — the sympy checker, the per‑unit JSON answer data, the author guide, packaging helpers) and `docs/`.
