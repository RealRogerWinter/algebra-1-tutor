# Reference-code → tutor launcher (hover prompt + click-to-copy)

- **Date:** 2026-06-14
- **Status:** Design approved; spec under review
- **Worktree / branch:** `.claude/worktrees/refcode-tutor-launcher` / `worktree-refcode-tutor-launcher` (off `main` @ `1811ecd`)

## Summary

Turn every reference-code badge in the **student-facing HTML textbook** (`docs/textbook/`) into a one-click launcher into the Algebra 1 tutor. On hover or keyboard focus a badge shows a small dropdown containing a ready-to-paste prompt; clicking the badge copies that prompt to the clipboard and shows a confirmation toast. The tutor skill is taught to recognize such a pasted prompt: it silently resolves the code for its own grounding, then asks how the student wants to work the item (have it explained, worked together, or a specific question answered) before teaching.

## Goal & success criteria

A reader of any lesson page can point at, say, `12.5.w2`, see exactly what will be sent to Claude, copy it with one click, paste it into Claude, and immediately be in a focused tutoring session on that exact item — with the tutor having pulled the item up for its own reference and asking how to proceed.

Done when:
- Hovering/focusing any `.refcode` badge in `docs/textbook/` shows a dropdown with the prompt; clicking copies it and shows a toast.
- The prompt is self-describing (plain-words label + code), generated deterministically from the code alone.
- `SKILL.md` documents the launcher behavior (triage + silent resolution); the skill `.zip` is rebuilt.
- All work is on the worktree above; the full CI gate is green; the generated `docs/` is byte-deterministic in CI's Python image.
- Other surfaces (student guide, tutor guide, landing) are visually and behaviorally unchanged.

## Decisions (settled with the user)

- **Prompt wording:** self-describing — plain-words label + `(reference CODE)` + explicit skill invocation + the triage instruction.
- **Scope:** the textbook only (`docs/textbook/`). Not the student guide or tutor guide.
- **Interaction:** dropdown on hover/focus; **click the code itself = copy** (per the user's explicit request).
- **Worktree:** all changes (including this spec) live on the new worktree.

## Context (what already exists)

- **SSOT reference codes** render as badges in `_verification/build_textbook.py:_convert_anchors`:
  ```python
  ANCHOR_RE.sub(lambda m: f'<a class="refcode" id="{m.group(1)}" href="#{m.group(1)}">{m.group(1)}</a>', ln)
  ```
  This covers worked examples (`w`), practice problems (bare number, optionally with a letter part like `5b`), definitions (`d`), checks (`c`), and figures (`f`); worked/practice numbers are auto-coded upstream by `_id_worked_practice`. The badge is both a deep-link target (`id`) and a self-link (`href="#self"`).
- **The textbook is generated, never hand-edited.** `build_textbook.py` is the sole writer of `docs/textbook/`; output is compared byte-for-byte by `build_textbook.py --check` and must be identical across CPython **3.11.9** (local) and **3.11.15** (CI `cimg/python:3.11`). A past bug came from `md_in_html` leaving a `markdown="1"` residue on one version — the build already strips it.
- **Shared design assets.** `build_textbook.CSS` and `build_textbook._page` are imported and reused by `build_student_guide.py`, `build_tutor_guide.py`, and `build_landing.py` (`build_all.py:2`: "the design lives in `build_textbook.CSS`/`_page`, shared by all four, so they move in lockstep"). Each surface writes `bt.CSS` to its own `textbook.css`. **Consequence:** anything added to the `CSS` constant appears on every surface and must be scoped.
- **The textbook's page template is `_lesson_page`** (left index rail + inline `<script>` for KaTeX/theme/menu). It is used *only* by the textbook. Guides/landing use `_page`. So injecting markup and JS in `_lesson_page` is automatically textbook-scoped.
- **`md_to_body`/`_convert_anchors` are called only by `build_textbook`'s own page builders** (`_intro_page`, overview intro, lesson body). The guides build their badges separately. So a flag on `md_to_body` cleanly confines the new badge attributes to the textbook.
- **The tutor skill** (`algebra-1-tutor/SKILL.md`) already has a "Reference codes" section with a resolution recipe (open file → find item → re-verify → show) and an "ask before you tell" pedagogy. It is packaged into `algebra-1-tutor.zip`/`.skill` by `build_skill.py`, whose `--check` is a CI gate; the skill runs on Claude.ai (uploaded `.zip`), not Claude Code.

## Approach

**Chosen: a single JS-positioned shared tooltip + click-to-copy, emitted statically by the builder.** Each badge gains a `data-prompt` attribute and an `aria-label`. One `position:fixed` tooltip element and one toast element exist once per page; one delegated script shows the tooltip on hover/focus and copies on click.

**Rejected — CSS-only `:hover` popover:** `.worked` and `.answers` cards use `overflow:hidden` (for a decorative watermark), so a popover on a worked-example badge would be clipped. Also bloats every badge.

**Rejected — native `popover`/`<details>`:** `<details>` is click-to-toggle (collides with click-to-copy); the `popover`/CSS-anchor APIs aren't uniformly supported. Overkill for a tooltip.

A `position:fixed` tooltip escapes all `overflow:hidden` clipping, adds almost no per-badge markup, is keyboard/screen-reader accessible, and keeps the generated files static and byte-deterministic.

## Detailed design

### 1. Prompt generation — new pure functions in `build_textbook.py`

`_label_for(code)` derives a plain-words label from the code string alone (no SSOT lookup → deterministic). A code is `scope.lesson.item` (three dot-parts); two-part codes (`mis.3`, `vis.t1`, `met.balance-scale`) take the fallback.

| Item pattern (after `scope.lesson.`) | Label |
|---|---|
| `w{n}` or `ex{n}` (opt. letter part) | `worked example {n}` (+ `, part {p}`) |
| `{n}` bare (opt. letter part) | `practice problem {n}` (+ `, part {p}`) |
| `d{n}` | `a key term` |
| `c{n}` | `a check-for-understanding question` |
| `f{n}` (opt. letter part) | `the figure` |
| `h{n}` | `a how-to` |
| anything else / 2-part bank code | `reference {code}` (no lesson clause) |

For three-part codes the lesson clause ` in Lesson {scope}.{lesson}` is appended (e.g. `… in Lesson 12.5`, `… in Lesson A.2`).

`_prompt_for(code)` returns:

> `Use the Algebra 1 tutor skill to help me with {label} (reference {code}). Pull it up, then ask whether I'd like you to explain it, work through it together, or answer a specific question.`

Example (`12.5.w2`):

> Use the Algebra 1 tutor skill to help me with worked example 2 in Lesson 12.5 (reference 12.5.w2). Pull it up, then ask whether I'd like you to explain it, work through it together, or answer a specific question.

### 2. Badge markup — `_convert_anchors(text, launcher=False)`, threaded from `md_to_body(text, launcher=False)`

`build_textbook`'s three `md_to_body` calls (intro page, unit-overview intro, lesson body) pass `launcher=True`. All other callers (and the default) get today's plain badge unchanged.

When `launcher=True`, the badge becomes (still a single inline line, so markdown treats it as inline HTML exactly as today):

```html
<a class="refcode" id="12.5.w2" href="#12.5.w2" data-prompt="{escaped prompt}" aria-label="Copy a tutor prompt for worked example 2 in Lesson 12.5">12.5.w2</a>
```

- `id` and `href="#self"` are preserved — deep-link targets keep working; without JS, clicking still jumps to the anchor (graceful degradation).
- `data-prompt` is escaped with `html.escape(prompt, quote=True)`; the `aria-label` likewise. Codes are grammar-constrained, so injection is impossible, but escaping keeps output well-formed and deterministic.
- No wrapper element is added, so existing selectors (`.practice li > .refcode`, etc.) are unaffected.

### 3. Interaction, accessibility, and the shared elements

`_lesson_page` injects, once per page (before `</body>`, outside the markdown body so no markdown processing):

```html
<div id="rc-tip" role="tooltip" aria-hidden="true"></div>
<div id="rc-toast" role="status" aria-live="polite" aria-hidden="true"></div>
```

The existing inline `<script>` in `_lesson_page` is extended (inside the same `DOMContentLoaded` handler) with a delegated refcode controller:

- **Show (hover/focus):** on `pointerover`/`focusin` where `target.closest('.refcode')`, set `#rc-tip` content to a header (`Tutor prompt (click the code to copy):`) plus the badge's `data-prompt`; position it with `getBoundingClientRect` — above the badge if there's room, else below; clamp within the viewport. Reveal via a `.show` class.
- **Hide:** on `pointerout` (leaving the badge), `focusout`, `scroll`, `resize`, or `Escape`.
- **Copy (click / Enter):** on `click` of a `.refcode`, `preventDefault()` and copy `data-prompt`. Prefer `navigator.clipboard.writeText`; on rejection or absence, fall back to a temporary off-screen `<textarea>` + `document.execCommand('copy')`. On success show `#rc-toast` ("Copied. Paste it into Claude to start.") for ~2.5 s; if both copy paths fail, leave the tooltip open so the text can be selected manually.
- **Accessibility:** screen-reader users get the `aria-label` on every badge (purpose is clear without the visual tooltip); keyboard users get a focus-triggered tooltip and Enter-to-copy; `Escape` dismisses; the toast is an `aria-live` status. `.refcode` gets `cursor:copy` (textbook only).
- **Behavior change to note:** clicking a code no longer writes `#code` to the URL. Deep-linking is unaffected (the `id` targets remain), so existing links and the sidebar still jump correctly.

### 4. CSS (added to the shared `CSS` constant, **all scoped under `body[data-surface="textbook"]`**)

- `body[data-surface="textbook"] .refcode{cursor:copy}`
- `#rc-tip`: `position:fixed; z-index:80;` hidden by default (`opacity:0; visibility:hidden`), `.show` reveals; themed from existing tokens (`--card`, `--rule`, `--ink`, `--shadow`, `--radius-sm`); `max-width:min(92vw,30rem)`; header in the `.eyebrow` style, prompt body in the reading font.
- `#rc-toast`: `position:fixed; left:50%; bottom:1.4rem; transform:translateX(-50%);` hidden by default, `.show` reveals; themed (accent `--leaf`/`--blue`).
- Transitions only inside `@media (prefers-reduced-motion:no-preference)`.

`#rc-tip`/`#rc-toast` rules are inert on other surfaces (the elements exist only on textbook pages), and the `cursor` rule is scoped, so the shared stylesheet stays safe for the guides.

### 5. Skill behavior — `algebra-1-tutor/SKILL.md`

Add a short subsection under "Reference codes" (house voice; no clichés or em-dash pile-ups), in substance:

> **Arriving from the textbook (the copy-paste launcher).** The HTML textbook lets a student copy a prompt like "Use the Algebra 1 tutor skill to help me with worked example 2 in Lesson 12.5 (reference 12.5.w2). Pull it up, then ask…". When you receive one:
> 1. **Resolve it silently for your own reference first.** Open the file, find the item, and re-verify the math (the recipe above). Ground yourself before responding; do not dump the full solution yet.
> 2. **Ask how they want to work it** — have you explain it, work through it together, or answer a specific question they have. If their message already says which, skip the ask and go.
> 3. **Proceed via the hint ladder** for the mode they chose, verifying before asserting as always.

Then rebuild the package: `python _verification/build_skill.py` regenerates `algebra-1-tutor.zip` and `.skill`; commit them so `build_skill.py --check` stays green. **The user must re-upload the `.zip` on Claude.ai** for the new behavior to take effect (the website feature works as soon as `docs/` deploys).

### 6. Determinism & scoping guards (summary)

- All markup/CSS/JS is emitted statically by the builder; no `Date`/random; the script and shared elements are byte-identical on every page.
- Badge attributes flow through markdown exactly like today's inline `<a>` (single line), so no new `md_in_html` drift.
- The `launcher` flag confines new badge attributes to the textbook; CSS scoping confines visual/cursor changes to the textbook.
- Verify byte-determinism in CI's image before committing `docs/`:
  `docker run --rm -v <worktree>:/work -w /work cimg/python:3.11 bash -lc "pip install -q markdown==3.7 pyyaml && python _verification/build_all.py && git status"` → clean.

## Testing

- **Update** `_verification/tests/test_textbook.py` refcode assertions: badges now carry `data-prompt` + `aria-label`; `id`/`href` intact.
- **Add** unit tests for `_label_for`/`_prompt_for`: `w`, `ex`, bare practice, lettered part (`8.2.5b`), `d`, `c`, `f`, `h`, `A`-scope lesson clause, two-part bank fallback, and HTML-escaping of the attribute (quotes/`&`).
- **Add** page-level tests: each generated lesson/overview/index/how-to page contains exactly one `#rc-tip` and one `#rc-toast` and the refcode controller script; a known badge’s `data-prompt` matches `_prompt_for(code)`.
- **Add** a guard test: `md_to_body(text)` with the default (`launcher=False`) produces today’s plain badge (no `data-prompt`).
- **Gate:** the full 12-gate must stay green — `build_textbook.py --check`, `build_all.py --check`, `build_skill.py --check`, `smoke_test.py`, and pytest — plus the CI-image determinism check above.

## Out of scope (YAGNI)

- No separate per-mode (explain vs work) buttons — the skill runs the triage.
- No "copy shareable link" action.
- No changes to the student guide, tutor guide, or landing.
- No new figures/illustrations.

## Risks & mitigations

- **Shared CSS bleed →** scope every new rule under `body[data-surface="textbook"]`.
- **Clipboard API unavailable (insecure context) →** `execCommand` fallback, then manual-select fallback. (GitHub Pages is HTTPS.)
- **Tooltip clipped by `overflow:hidden` →** `position:fixed` tooltip.
- **CI-only byte drift →** reproduce `cimg/python:3.11` before committing `docs/`.
- **Skill behavior needs redeploy →** call out the `.zip` re-upload explicitly.

## Acceptance checklist

- [ ] `_label_for`/`_prompt_for` implemented + unit-tested (all kinds, parts, `A`, fallback, escaping).
- [ ] Badges carry `data-prompt`/`aria-label` (textbook only); `id`/`href` preserved.
- [ ] Tooltip + toast + delegated controller in `_lesson_page`; hover/focus shows prompt; click/Enter copies + toast; Escape dismisses.
- [ ] New CSS scoped to `body[data-surface="textbook"]`.
- [ ] `SKILL.md` launcher subsection added; `.zip`/`.skill` rebuilt.
- [ ] `docs/` regenerated; full gate green; determinism verified in CI image.
- [ ] Guides/landing unchanged; all work on the worktree.
