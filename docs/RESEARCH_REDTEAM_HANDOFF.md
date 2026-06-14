# Algebra 1 Course — Research & Red-Team Handoff

> **Purpose:** the deliverable that hands off to planning mode. It consolidates the
> multi-agent red-team of every unit/example/explanation, the deep research benchmarking
> the course against authoritative college-level sources, the platform-feasibility findings,
> the vetted reference list, and a scoped multi-PR plan outline.
> **Status:** research complete (2026-06-13). Not yet a plan — planning is the next phase.
> **Companion files:** requirements in [`REBUILD_BRIEF.md`](REBUILD_BRIEF.md); full detail in
> `research-output/00-overview.md`, `01-findings-confirmed.md`, `02-crosscutting.md`,
> `03-sources.md` (158 vetted sources).
> **How it was produced:** a 64-agent workflow (15 red-team + 15 adversarial-verify + 7
> cross-cutting research + source vetting) plus a dedicated image-feasibility probe. Every
> claimed math error was re-checked with sympy; every finding was adjudicated by an
> independent skeptic.

---

## 1. Executive summary

**The course is fundamentally sound. This is an *elevation + new-artifacts + unification*
job, not a repair.** Across 15 reviewed parts (12 units + stats appendix + the
misconceptions/metaphors bank + the pedagogy/visuals/curriculum bank):

- Every part rated **strong** or **excellent**. **Zero critical findings. Zero answer-key
  math errors** — all 543 auto-checked answers re-verified clean under sympy (twice).
- 162 confirmed findings: **33 major, 75 minor, 54 enhancement**. Only **2** red-team findings
  were rejected by the adversarial verifiers; the verifiers also caught **~24** issues the
  red-team missed.
- The 4 findings tagged "math-error" are all **minor and in prose/annotations, not the keys**
  (one real coordinate typo at 5.3; three imprecise/over-general explanatory claims at
  7.3, 9.2, 11.2). Confirmed by independent sympy checks.
- **One verification-tooling defect** (not a content error): the `_verification` entry for
  problem **5.5.6** encodes a self-consistent but *wrong* equation, so it passes the sweep
  while testing the wrong thing — the "0 failures / 765" claim has exactly one mis-specified
  check. Fix it and add a lint.

**The dominant finding pattern:** precision-of-definition, coverage-completeness, and
cross-material consistency gaps — all closeable **within Algebra 1 scope**, lifting an
already-strong course to college-text rigor.

**Five strategic questions the research resolved:**
1. *Can the skill fetch figures/sources from GitHub at runtime?* **No** (CSP blocks remote
   images in artifacts; sandbox egress excludes `raw.githubusercontent.com`; no image-output
   channel). → **Bundle reviewed SVGs + a citation pack into the skill**; the GitHub repo is
   the source of truth and feeds the HTML textbook.
2. *Is "college-level" a scope expansion?* **No.** Hold Algebra-1 scope; raise rigor/precision.
   Exactly **one** scope-creep item exists today (absolute-value *solving*, 8.3).
3. *Is there a usable code system already?* **Yes** — the JSON dotted IDs (`12.5.w2`, `12.3.7`)
   are the seed; a backward-compatible grammar extends them to definitions/figures/etc.
4. *How do the four materials stay unified?* **One `curriculum.yaml` source of truth generates
   the skeletons; the HTML textbook is generated from the unit `.md` prose.**
5. *Can the tutor read photos of student work?* **Yes** (image input is fully supported) — R3 is
   safe to build.

---

## 2. Red-team findings — the content assessment

### 2.1 Per-part quality and finding counts

| Part | Quality | Confirmed | Verifier-added | Rejected |
|---|---|---|---|---|
| 1 Foundations | strong | 9 | 1 | 0 |
| 2 Linear Equations | strong | 10 | 2 | 0 |
| 3 Proportional Reasoning | strong | 9 | 2 | 0 |
| 4 Functions | strong | 9 | 2 | 0 |
| 5 Linear Functions & Graphs | strong | 11 | 2 | 0 |
| 6 Modeling & Translation | strong | 7 | 2 | 0 |
| 7 Systems | strong | 9 | 0 | 0 |
| 8 Inequalities | strong | 9 | 2 | 0 |
| 9 Sequences & Exponentials | strong | 9 | 2 | 0 |
| 10 Exponents & Polynomials | **excellent** | 7 | 1 | 0 |
| 11 Factoring | strong | 8 | 1 | 0 |
| 12 Quadratics | strong | 10 | 2 | 0 |
| A Statistics | strong | 10 | 1 | 0 |
| misconceptions+metaphors | strong | 12 | 2 | 0 |
| pedagogy+visuals+curriculum | strong | 9 | 2 | 2 |

Full per-finding detail (locator, severity, recommendation, verifier verdict, citation) is in
`research-output/01-findings-confirmed.md`.

### 2.2 The major findings, grouped by theme (33 total; some down-scoped by verifiers)

**A. Number-system completeness (Unit 1)**
- **1.2** introduces natural/whole/integer/rational but **never names irrational or real
  numbers** — yet asserts "algebra uses the whole line." Add a light irrational/real layer
  (π, √2; "real = every point on the line"). *Core Algebra 1, not scope-creep.*
- **1.4** **never introduces absolute value** (|a| = distance from 0). Add it to sharpen
  ordering of negatives and the different-signs rule. (Note: this is the *graphing/distance*
  sense — distinct from the 8.3 *solving* scope-creep item; see §3.)

**B. Equation theory (Unit 2)**
- **No-solution (contradiction) and infinitely-many (identity) outcomes are never taught** — a
  standard Algebra-1 endpoint that follows directly from variables-on-both-sides. Add the
  three-outcome framing (conditional / identity / contradiction).
- Down-scoped to minor by verifiers: consolidate an explicit general solving strategy; tighten
  the "term" definition so the sign travels with the term.

**C. Function rigor (Unit 4)**
- **4.1** defines a function as a **"rule"**, but the unit's own examples are pair-sets/tables
  with no rule → use **"correspondence/pairing"** (or relation → function). Reserve "rule" for
  the 4.2 formula.
- **4.2** jumps from finite-set domains to "all real numbers" without naming **discrete vs
  continuous domain** — add it (no interval notation needed).

**D. Linear functions (Unit 5)**
- **Verification defect 5.5.6** (see §1) — fix the harness entry + add a "point-lies-on-line"
  lint.
- **x-intercept, graph-by-intercepts, and standard form `Ax+By=C` are missing** — standard
  Algebra-1 content; add a short sub-lesson.
- Interpret **slope and intercept in context** (story meaning) in each worked example.
- Down-scoped: state the **constant-rate-of-change** defining property explicitly.

**E. Sequences & exponentials (Unit 9)**
- Make the exponential object well-defined: **a≠0, b>0, b≠1** with one-sentence reasons.
- Name the **discrete domain** (counting numbers) and that a **geometric sequence is an
  exponential restricted to those inputs**.
- Add **recursive *and* explicit formulas** for arithmetic/geometric (meets CCSS F-BF.A.2).

**F. Polynomials & factoring (Units 10–11)**
- **10.2** add a scientific-notation worked example where the **coefficient product exceeds 10**
  (the renormalization slide, e.g. 30×10⁷ → 3×10⁸).
- **11** introduce **prime/irreducible trinomials** (not everything factors) with a stopping
  rule, and scope the unit to **factoring over the integers** (reframe the `a²+b²` note).

**G. Quadratics (Unit 12)**
- Promote the **square-root property to a named conditional rule** ("if x²=k with k≥0 then
  x=±√k; if k<0 no real solution").
- Down-scoped/optional: connect the **discriminant to rational vs irrational roots**.

**H. Statistics (Appendix)**
- Teach **checking the cloud is roughly linear before fitting** a line, and name **outliers**.
- Make a **two-way table show association** (tweak numbers so conditional rates differ).
- Standing scope question: stats is currently optional (see §3).

**I. Cross-cutting banks**
- **misconceptions.md** add a **Slope misconception entry** (steepness vs direction; |slope|).
- **visuals.md / SKILL.md:125** — SKILL.md claims balance-scale and algebra-tile templates
  exist, but **they don't** in visuals.md. Add the templates or fix the claim. (This was the
  source of the 2 rejected findings region too — the verifiers tightened the pedagogy bundle.)

**The three minor "math-error" prose fixes** (all confirmed, none in the keys): 5.3 coordinate
typo `(2,5)→(150,10)` not `(150,50)`; 7.3 "adding two equations gives a line through the
crossing point" is false for inconsistent/dependent systems; 9.2 "tied at x=2" should be
"tied at x=1 *and* x=2, dips below between."

---

## 3. Scope calibration (the Algebra-1 boundary)

Triangulated from **CCSS Algebra I (Appendix A)** and **OpenStax Elementary/Intermediate/College
Algebra**.

- **Confirmed IN-scope** (keep, no rescoping): completing the square, the quadratic formula,
  point-slope form, scientific notation (as Grade-8 fluency maintenance), sequences &
  exponential functions, radicals in service of quadratics, functions/f(x)/domain-range.
- **The ONE scope-creep item: Unit 8.3 absolute-value equations & inequalities** — both
  frameworks place algebraic `|ax+b|=c` / `|ax+b|<c` solving in **Intermediate/College
  Algebra**. **Recommendation:** keep the Algebra-1-legitimate piece (the **V-shape graph** and
  **|x|=k "distance from zero"**), and either drop the full two-case/interval-notation solving
  or mark it an explicit optional "reach beyond Algebra 1" lesson. Reconciles with finding **1.4**:
  introduce |a| as distance early; graph the V; don't do full algebraic solving.
- **Hard ceiling — keep OUT:** logarithms; complex/imaginary numbers (hold the *real*-solutions
  ceiling on the discriminant); rational & radical *functions*, asymptotes, partial fractions;
  polynomial division and degree>2 as a strand; conics beyond the quadratic parabola; matrices;
  series/summation/binomial theorem; trigonometry; function composition & general inverses.
- **Three intentional departures to *document*, not "fix"** (so reviewers read them as choices):
  (a) statistics demoted to optional appendix is **narrower** than CCSS (which makes it a full
  required unit); (b) rational expressions omitted is **narrower** than traditional OpenStax;
  (c) proportional reasoning (Unit 3) is **below** the Algebra-1 line (Grade 6–7) — keep it as a
  labeled "bridge/review" unit.

---

## 4. State-of-the-art pedagogy (learning-science research)

**Already strong & evidence-aligned — keep and foreground:** worked examples + backward fading
(meta-analytic g≈0.48), concrete→pictorial→symbolic (Bruner), ask-before-tell hint ladder that
honors "just tell me" (human tutoring ≈0.79 SD; step-level ≈0.76), transfer checks over "make
sense?", diagnose-the-misconception-then-reframe.

**Highest-leverage gaps to add (priority order):**
1. **Strategy choice (IES Rec 3 — the highest-rated recommendation and the clearest gap):** for
   high-frequency problem types (multi-step equations, factoring, substitution vs elimination,
   slope two ways), show **two valid methods side-by-side** and ask which/why and when each wins.
2. **Interleaving (d≈0.83 — the single biggest lever, currently weakest):** build **mixed,
   cumulative problem sets** where consecutive problems need different strategies, and a
   **spaced-review schedule** persisted across sessions. *This directly motivates R1's
   complementary problem sets + the unit-level mixed-review sets.*
3. **"Spot-the-error" study items (IES Rec 1 full form):** pair a **correct and an incorrect**
   worked solution (drawn from `misconceptions.md`) and have the student find/explain the error
   *before* solving — use the misconception bank **proactively**, not only reactively.
4. **Delayed retrieval warm-ups:** 2–4 mixed recall problems at session start ("hard on purpose").
5. **Self-regulated-learning scaffolds** for the adult learner: prompt goal-setting, planning,
   self-monitoring; gradually hand ownership of the Progress Card + review schedule to the student.
6. **Temper the concrete ceremony** for fluent adults (state as evidence-based, not just
   pragmatic) and **make "explain back" targeted** (reflexive "why?" at every step can hurt).
7. **Bidirectional representation translation** (NCTM): context ↔ table ↔ equation ↔ graph, both
   directions, as an explicit checked skill.

---

## 5. The reference-code system (design resolved)

**Grammar (backward-compatible with every existing JSON ID):**
`scope . lesson . [type-tag]index[part]`
- **scope** = unit `1`–`12` | `A` (appendix) | `refA`/`refB` (fraction refreshers).
- **type-tag** (omitted = practice problem): `w` worked example, `d` definition/new-term,
  `f` figure, `m` misconception, `p` metaphor, `c` transfer-check, `h` how-to/procedure.
- Examples: `12.5.7` (practice 7), `12.5.w2` (worked ex 2), `12.1.d3` (definition 3),
  `12.6.f1` (figure 1), `8.2.5b` (part b). Globals: `mis.3`, `vis.t3`, `met.balance-scale`.
- **Collision-free** by construction (numeric vs letter-prefixed scope; type-tag = letter-then-digit
  vs digit-only practice). Add a **regex linter** to the build; IDs are **append-only**; authors
  assign d/f/c tags in document order.
- **R1 tutor-guide complementary problems** get a **separate namespace** (a tutor tier, e.g.
  `12.3.T7`) so they never collide with textbook codes.

**Resolution at runtime:** student types `#12.5.w2` (case-insensitive; spoken fallback "worked
example 2 of lesson 12.5"). Tutor parses → loads the unit `.md` (or global bank) → finds the
labeled item → **re-verifies any computation against the bundled JSON and live** before showing →
echoes the canonical code back. Requires a "Reference codes" section in `SKILL.md` and explicit
inline anchors in the unit files.

---

## 6. Figures system (R2 — resolved)

- **Generation is programmatic, not generative-AI:** figures are computed (Python/matplotlib or
  deterministic SVG from coordinate data), each backed by a reproducible **spec** (equation,
  window, points, labels). A diffusion image model would draw wrong math — forbidden.
- **Pipeline (treat like answer-key verification):** spec → render → **accuracy check** (sympy)
  → **visual review** (legibility, labels, cleanliness) → store, versioned. Each figure gets a
  `FIG`/`f` code.
- **Source of truth = public GitHub repo.** It feeds the **HTML textbook** (which embeds SVGs
  natively; serve via **jsDelivr pinned to a tag/SHA** or GitHub Pages relative paths — **never
  `raw.githubusercontent.com`**: wrong MIME, no CORS, throttled).
- **In-chat (the hard part): the skill cannot fetch+display remote images.** Artifacts enforce
  CSP `img-src 'self' blob: data: claudeusercontent.com`. **Adopted HYBRID:** a build step
  **syncs the reviewed SVGs into the skill package**; at runtime the skill **reads the local SVG
  and emits it as an Artifact** (inline source → renders in-chat, no network, math exact). This
  **supersedes** the current "compute coordinates and eyeball an artifact at runtime" approach.

---

## 7. Multimodal photo input (R3 — confirmed supported)

Image input is officially supported (**≤20 images/msg, ≤10 MB each, JPEG/PNG/GIF/WebP**).
Protocol (an extension of "verify before asserting"): **detect → render in `$$…$$` → confirm
"is this what you wrote?" → only then advise.** A photo of the student's *steps* is prime
misconception-diagnosis input. The tutor encourages it and notes it's the **preferred way to
upload large problem sets**. Edge cases: illegible handwriting, multiple problems per photo,
rotation, separating printed problem from handwriting.

---

## 8. House voice / copyedit (R4)

Every generated **course-material copy** (prose) passes the **`/copyedit`** skill before shipping
(planning docs exempt). The tutor **skill obeys the same house voice at runtime** — extend
`SKILL.md`'s persona with the copyedit rules (no AI-tell clichés, no "it's not X it's Y", no
forced rule-of-threes, no em-dash overuse, no fake enthusiasm). **Register caveat:** run
`/copyedit` with an **instructional-tutor** target so it keeps natural second-person "you".
Recommend a shared **house-style sheet** both the copyedit runs and `SKILL.md` reference.

---

## 9. Unification architecture (the alignment audit → the spine of the plan)

**Current state:** the spine is **fully aligned** (12 units + Appendix A; identical numbers,
titles, lesson counts = 47 core + 3 optional = 50 lessons) and the teaching framing is consistent
across SKILL.md, the lesson-plan HTML, and the unit files. But:
- **No single source of truth:** the unit/lesson list is hand-maintained in **6+ places**
  (curriculum-map.md, docs/CURRICULUM.md, lesson-plan HTML, student-guide HTML, unit `.md`
  headers, the JSON) — they agree today, nothing enforces it → silent desync risk.
- **Stale docs:** `AUTHOR_GUIDE.md:13` and `SKILL.md:115` say unit files use `\(...\)` inline,
  but a conversion pass (`NOTATION_CONVERSION.md`) made the shipped files **plain-Unicode**.
  Only `ARCHITECTURE.md:33` matches reality. Fix the two stale descriptions.
- **Cosmetic title drift** (8.3, 8.4, 6.3 differ across materials) and `curriculum-map.md` mixes
  `x^2` and `x²`.

**Target architecture (the recommendation):**
- **One canonical data file — `curriculum.yaml`** (per unit/lesson: number, slug, canonical
  `title`, learner-facing `short_title`, prerequisites, dependency-chain tags, one-line
  description, ordered lessons). **Generate** from it: curriculum-map.md, docs/CURRICULUM.md, the
  lesson-plan & student-guide HTML skeletons, and the unit `.md` front-matter.
- **The HTML textbook is a *generated presentation layer* from the unit `.md` prose** (tagged
  with reference codes) — **not** a fifth hand-maintained source. This guarantees the tutor and
  the textbook can never teach different math. The unit `.md` files remain the prose source of
  truth (they're what the skill loads).
- **CI alignment guard** next to `verify_answers.py`: lesson IDs match across `.md`/JSON;
  per-unit counts match across all materials; no `\(...\)` survives in shipped files; code-grammar
  lints; every `solve` entry's point lies on its line.

---

## 10. Platform constraints the plan must respect (consumer Claude.ai)

- **No runtime web fetch / web search / URL retrieval.** Sandbox egress is an allowlist
  (package managers + github.com + Anthropic; **not** raw.githubusercontent.com; Pro/Max can't
  add domains); web_search/web_fetch are API-only. → **Bundle the reference pack; never ship a
  fetchable URL list.**
- **Only `$$…$$` renders in chat** → inline math stays plain Unicode (x², √12, ½, ±, ≤). The
  **HTML textbook** uses KaTeX/MathJax (different surface, different rule).
- **No image output; remote images blocked in artifacts** → figures as **bundled inline-SVG
  artifacts** (§6). **Image input works** (§7).
- **Stateless** across chats → Progress Card (extend it with a "due for review" list for spacing).
- **Skill files ≤30 MB**, per-user upload; `name` lowercase-hyphen (no "claude"/"anthropic"),
  `description` ≤1024 chars. SVGs + citation pack fit easily.
- **Licensing:** OpenStax & Khan are **CC BY-NC-SA** (not CC BY); OpenStax prohibits LLM-training
  use; Paul's Notes & NCTM are all-rights-reserved (**link-only**); Lumen & IM-2019 are **CC BY**
  (most reusable). → **Author original copy; link/cite sources; excerpt only from CC BY sources**
  in the bundled pack, each with attribution + license + verified-date.

---

## 11. The vetted reference list

158 sources vetted (79 gold, 27 strong, 39 acceptable, 13 rejected). Gold tier is dominated by
**OpenStax** (Elementary/Intermediate/College Algebra, Prealgebra, Contemporary Math), **CCSS**,
**IES/WWC practice guides**, **W3C/WCAG**, **MathJax/KaTeX docs**, plus peer-reviewed pedagogy
(Fyfe concreteness-fading, Barbieri worked-examples, Rohrer interleaving, VanLehn tutoring).
Strong tier adds **Khan, Illustrative Mathematics, Paul's Online Math Notes, Lumen, Desmos,
LibreTexts**. Full list with per-source coverage + license + accessibility:
`research-output/03-sources.md`.

**Delivery:** the list ships **bundled into the skill** as a Level-3 reference (concept → source,
with a short verified excerpt + attribution + license + retrieved-date), mapped so **every
lesson — and thus every example — has a reputable backing source.** Plain clickable links are
printed for the human to open; the model never fetches them.

---

## 12. Proposed multi-PR plan (outline for planning mode)

A multi-stage program; **each stage gets its own planning + design pass** before implementation.
Dependencies noted; per-unit work parallelizes.

- **Stage 0 — Foundations & single source of truth.** Create `curriculum.yaml`; build the
  generator; add the CI alignment guard; **fix the 5.5.6 harness defect + point-on-line lint**;
  fix the stale notation docs (SKILL.md:115, AUTHOR_GUIDE:13). *Unblocks everything; low risk.*
- **Stage 1 — Content elevation (≈13 per-unit PRs).** Apply confirmed findings (majors first);
  rescope 8.3; add no-solution/identity (U2), irrational/real + |a| (U1), correspondence +
  discrete/continuous (U4), intercepts/standard form (U5), exponential/sequence precision (U9),
  prime trinomials (U11), square-root property (U12), stats fixes (Appendix). Add the SOTA
  elements (strategy-choice, spot-the-error, interpret-in-context). Each PR: **/copyedit** new
  prose, **re-verify with sympy + update JSON**, alignment CI green.
- **Stage 2 — Reference-code system.** Implement the grammar repo-wide; tag unit `.md` items
  (d/f/c/…); linter; `SKILL.md` "Reference codes" section + resolution recipe.
- **Stage 3 — Figures pipeline.** Figure specs → programmatic render → accuracy + visual review →
  versioned repo; bundle SVGs into the skill; `FIG` codes; replace runtime-eyeballed artifacts.
- **Stage 4 — HTML textbook.** Generated from unit `.md`: KaTeX pre-render + MathML, one file per
  unit, WCAG 2.2 AA (reflow/contrast/resize), deep-linking by reference code, embedded SVGs,
  offline/self-hosted assets, search (Pagefind), dark mode + print. Uses **frontend-design**.
- **Stage 5 — Tutor guide + complementary problems (R1).** Author complementary sets (separate
  namespace, sympy-verified, full worked solutions), per-lesson + unit mixed-review (interleaving);
  add the problem-set pages to the tutor-guide HTML.
- **Stage 6 — Skill behavior (skill-creator).** `SKILL.md`: multimodal photo protocol (R3),
  reference-code resolution, house-voice rules (R4), strategy-choice/spot-the-error/SRL pedagogy,
  figure-artifact emission, bundled reference pack. Repackage + re-verify the `.zip`.
- **Stage 7 — Student-guide refresh + final alignment.** Regenerate the student guide from the
  SSOT; full alignment CI green; end-to-end smoke tests (new learner, topic jump, wrong-answer
  diagnosis, photo upload, code lookup, figure render).

---

## 13. Open decisions for planning (recommendations in **bold**; proceeding on these unless redirected)

1. **Statistics:** keep as **optional appendix** (matches the adult-self-learner design) and
   *document* the CCSS departure — vs. promote to a core unit.
2. **Absolute value 8.3:** **rescope** to the V-shape graph + |x|=k distance, defer full
   two-case/interval solving (or mark it optional "reach") — vs. keep as-is.
3. **Commercial intent / licensing:** default to **author-original + link/cite only**, which is
   license-safe regardless; if monetization is ever intended, additionally avoid excerpting
   OpenStax/Khan text and prefer CC BY (Lumen, IM-2019).
4. **SSOT format:** **`curriculum.yaml`** (human-diffable) — vs JSON.
5. **Figure format:** **SVG canonical**, PNG only as optional download (resolved by research).
6. **Textbook packaging:** **one HTML file per unit** (performance, deep-linking) — vs monolith.
7. **Complementary-set shape (R1):** **per-lesson + a unit mixed-review set; ~5–8 each; parallel
   difficulty + light stretch tier.**

---

## 14. Corrections to earlier statements in this effort
- The shipped unit `.md` files are **plain-Unicode inline**, not `\(...\)` LaTeX — a conversion
  pass removed the `\(...\)`. Earlier in this effort I repeated `SKILL.md`'s (now stale)
  description that they use `\(...\)`. The stale descriptions in `SKILL.md:115` and
  `AUTHOR_GUIDE.md:13` should be corrected in Stage 0.
