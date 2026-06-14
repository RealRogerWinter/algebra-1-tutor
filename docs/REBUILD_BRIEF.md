# Rebuild Brief — living requirements & decisions

> Purpose: a running log of user-stated requirements and confirmed decisions for the
> **college-quality rebuild** of the Algebra 1 course. The research + red-team **handoff
> deliverable** (in progress) and the later **implementation plan** consume this brief.
> Started 2026-06-13, during the `algebra-redteam-research` workflow run.

## Confirmed scope
1. Elevate the existing (already strong, sympy-verified) course content to **college-level
   quality** — the rigor/precision/production quality of a respected college text
   (OpenStax Elementary/Intermediate Algebra, Lial, Blitzer), **without scope-creep into
   precalculus/college-algebra** topics that don't belong in Algebra 1.
2. Produce a **full-length digital textbook in rich HTML** with a **reference-code system**
   for every example/problem/explanation, so a student can quote a code to the tutor skill
   for an explanation or extra context.
3. Compile a **vetted, fetchable, authoritative reference list** with a reputable source
   for every concept (and thus every example).
4. **Unify the four materials** so they align: the skill (`SKILL.md` + `references/`), the
   HTML textbook, the **student guide** (`algebra-1-student-guide.html`), and the **tutor
   guide** (`algebra-1-lesson-plan.html`).
5. Deliver as a **multi-stage, multi-PR plan** that can run autonomously.

## Requirements log
### R1 — Tutor guide complementary problem sets  · added 2026-06-13
The **tutor guide** must include a **problem-set page** whose problems are **complementary
to, and not identical to**, the textbook's problems.
- **Why:** supports the skill's "hand them a *fresh* similar problem" (hint-ladder rung 5)
  and transfer-check patterns — the tutor needs problems the student hasn't already worked
  in the textbook.
- **Implications for the plan:**
  - New, original problems (parallel forms: same skill/concept, different numbers/contexts) —
    authored, not reused from the unit files' practice sets.
  - Each needs a **sympy-verified answer key** (extend `_verification/`), same rigor as today.
  - Addressed in the unified **code system but in a separate namespace** so codes never
    collide with textbook problems (e.g. a "T"/tutor tier).
  - Tutor-facing → include **full worked solutions**, not just answers.
- **Proposed defaults (confirm at plan review):** per-lesson sets **plus** a unit-level
  **mixed-review/interleaving** set (per `pedagogy.md`); difficulty parallel-equivalent to
  the textbook **plus a light stretch tier**; ~5–8 per lesson (a reservoir, leaner than the
  textbook's 8–15).

### R2 — Pre-generated, reviewed figure library in a public GitHub repo · added 2026-06-13
Every example with **graphing or other visual elements beyond equations** references an
**exact, pre-generated image** stored in a **public GitHub repo**; the skill **grabs** the
image at runtime from any session. The model must **not** generate images on the fly. Every
image is generated, **reviewed, and QA'd**: mathematically accurate, represents the concept
cleanly, clearly legible, no other issues.
- **Why:** removes the runtime "LLM eyeballs a curve → wrong picture" risk that `visuals.md`
  itself warns against; gives textbook + skill one vetted, consistent figure set.
- **Generation method (a correctness requirement, not a preference):** figures are generated
  **programmatically / computed** — Python (matplotlib) or deterministic SVG built from
  coordinate data — **never** with a generative/diffusion image model (which cannot draw
  accurate math). Each figure is backed by a reproducible **spec** (equation, window, sample
  points, labels) so it can be regenerated and machine-verified.
- **Pipeline (treat like the answer-key verification — nothing ships unreviewed):**
  spec → render → **accuracy check** (intercepts/vertex/points verified, e.g. sympy) →
  **visual review** (legibility, labels, cleanliness) → store, **versioned**.
- **Code system:** every figure gets a code (e.g. `FIG-12.6.1`) in the unified scheme;
  referenced from the textbook, the skill, and (separate namespace) the tutor-guide problems.
- **Hosting (resolved):** public repo is the **source of truth**; serve the web/textbook via
  **jsDelivr pinned to a tag/commit SHA** (immutable, correct MIME, CORS `*`) or GitHub Pages
  relative paths; **avoid `raw.githubusercontent.com`** (serves `text/plain`, no CORS,
  throttled, and not on the sandbox allowlist).
- **FEASIBILITY — RESOLVED (research probe, 2026-06-13):** the skill **cannot fetch + display a
  remote GitHub image inline** on Claude.ai. Confirmed blockers: artifacts enforce CSP
  `img-src 'self' blob: data: https://www.claudeusercontent.com`, so a remote `<img>` (raw
  GitHub, Pages, jsDelivr) is blocked; chat messages don't render raw HTML/SVG and don't
  reliably render markdown `![](url)`; the code-sandbox network is an allowlist that **excludes
  `raw.githubusercontent.com`** and isn't guaranteed on Pro/Max; Claude has **no image-output
  channel**. **Adopted design (HYBRID):** the public repo's reviewed SVGs are the source of
  truth and feed the HTML textbook; a **build step syncs those SVGs into the skill package**
  (Level-3 refs — tiny, well under the 30 MB limit), and at runtime the skill **reads the local
  SVG and emits it as an Artifact** (inline source → renders in-chat, no network, math stays
  exact). "Available from any session" is met because figures **travel with the per-user skill
  install**, not by runtime fetch. (See memory `claude-ai-skill-constraints`.)
- This **supersedes** the current `visuals.md` "compute coordinates and emit an artifact at
  runtime" approach (shift to *reference a reviewed asset*, possibly via the hybrid above).

### R3 — Multimodal: read & evaluate photos of the student's work · added 2026-06-13
The tutor (skill) must expect the user to **occasionally upload photos** of their handwritten
or printed work, and use **multimodal vision** to scan, interpret, and evaluate it.
- **Protocol (an extension of the core "verify before asserting" rule):**
  1. Read the photo; **detect the relevant equations / steps** (the problem and, if shown,
     the student's attempted work).
  2. **Render what was read** back in the skill's notation (`$$...$$` display blocks) and
     **confirm with the user** — "Here's what I see; is this what you wrote?" — **before**
     offering any feedback or advice. Misreading a photo and then grading it would be exactly
     the "confidently mis-grade a correct student" failure the skill exists to prevent.
  3. Only after confirmation: diagnose/teach as usual. A photo of their *steps* is prime input
     for **misconception diagnosis** — read the actual written work and find the tell.
- **Encourage it:** the tutor occasionally reminds the student they can do this, and that a
  **photo is the preferred way to upload large problem sets / lots of work** (less friction
  than typing it all).
- **Edge cases the instruction should cover:** illegible/ambiguous handwriting (ask for a
  clearer shot or to type just the unclear part); multiple problems per photo (enumerate &
  confirm each); rotated/cropped images; telling the *printed problem* from the *student's
  handwriting*.
- **Feasibility:** user→model **image input is a supported Claude.ai consumer capability**
  (Claude is multimodal). Note the asymmetry: this *input* direction is solid, whereas R2's
  model→user remote-image *display* is unverified — so photo-input is a dependable channel
  regardless of how R2 resolves.
- **Lands in:** primarily `SKILL.md` (a new "Reading the student's work from a photo" section,
  threaded into the teaching loop, the verify-first rule, and misconception diagnosis); a
  friendly mention in the student guide; a note in the tutor guide. Slated for the
  skill-revision PR (apply coherently + repackage the `.zip`).

### R4 — All generated course copy passes `/copyedit`; the skill obeys the house voice · added 2026-06-13
- **Process gate:** every piece of **course-material copy** generated in the rebuild (textbook
  prose, student-/tutor-guide prose, lesson explanations, word-problem wording, figure captions)
  is run through the **`/copyedit` skill** before it ships — a required QA step in each content
  PR. "Copy" = prose only (not math, answer keys, code, or these planning docs, which are
  **exempt**).
- **Product:** the tutor **skill obeys the same house voice at runtime** — extend `SKILL.md`'s
  persona/voice section with the copyedit rules: no AI-tell clichés (delve, leverage, robust,
  seamless), no "it's not X it's Y", no forced rule-of-threes, no throat-clearing, no em-dash
  overuse, no fake enthusiasm/emoji. (The current persona — "plain, no gushing, lead with the
  math, no decorative marks" — is already strongly aligned; this formalizes + extends it.)
- **Register caveat:** a tutor legitimately uses **direct second-person address ("you")** —
  the correct instructional register, not an AI tell. Run `/copyedit` on course copy with an
  **instructional-tutor voice target**, not generic prose, so it doesn't strip natural address.
- **Consider:** a short shared **house-style sheet** in the repo that both the `/copyedit` runs
  and `SKILL.md` reference, so voice stays consistent across all four materials.
- **Lands in:** a `/copyedit` QA step in every content PR; a voice-rules addition to `SKILL.md`
  (skill-revision PR).

## Working assumptions (surfaced in the deliverable; correct me if wrong)
- "College-level quality" = production rigor of a respected college **Algebra/developmental**
  text, applied to Algebra-1-level content — **not** an expansion of topic scope.
- The reference list maps **concepts/lessons → authoritative sources**; since every example
  belongs to a lesson, every example inherits a vetted source. Example-specific sources are
  added only where a particular technique has a canonical reference.
- The HTML **textbook is a new, richer artifact** (the current student guide is a
  motivational *map*, not a textbook with worked examples/practice).

## Open decisions for plan review
- Complementary-set granularity (per-lesson vs +unit mixed-review vs cumulative).
- Complementary-set difficulty band and count per lesson.
- Single-source-of-truth strategy: is the textbook **generated from** the unit `.md` files
  (+ a problems datastore), or authored alongside them? (Affects how all four stay aligned.)
- Figure **format** — resolved: **SVG canonical** (renders in both the textbook and the in-chat
  inline-SVG-artifact path); PNG only as an optional download/fallback. In-chat strategy
  resolved to **bundle-SVG-into-skill + emit-as-Artifact** (see R2, FEASIBILITY — RESOLVED).
- R3 scope: confirm-before-evaluating is a hard default; decide whether to also accept photos
  of *figures/graphs* the student points to, not just equations/steps.
