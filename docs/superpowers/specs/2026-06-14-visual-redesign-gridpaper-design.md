I now have full ground-truth. Every red-team blocker is verified against real files. Here is the final, authoritative spec.

---

# GRIDPAPER — Final Visual Design Language for the Algebra 1 System
### Design Director's authoritative specification · textbook · student guide · tutor guide
**Status:** implementation-ready. Every red-team **blocker** and **major** is folded in below, each tagged inline as **[RESOLVED: source]**. Deliberately deferred minors are listed in §11.

> **Anchor.** Four proposals converged (Fraunces + Source Serif 4 + mono; warm-paper / slate-dark; figure-blue accent; refcode-as-sole-identifier; native `<details>`). The fork was *editorial monograph* vs *engineering quadrille*. I anchor **engineering quadrille** — its organizing metaphor (a coordinate plane on a grid) is already in the product (`figures.py` draws every figure on graph paper), so it turns the two liabilities (colliding codes, bare figures) into the signature at near-zero asset cost — and graft the monograph's discipline (strict modular scale, callout taxonomy, real contrast tables, motion budget). The red-team passes forced five structural corrections that the draft got wrong; the design survives all of them, but **several headline mechanisms are re-specified** (the refcode is now the *only* number and is the **trailing code segment shown as a chip**, not a separate decorative point-chip; per-problem answer reveal is **cut from v1**; every label/answer-key transform is a **markdown pre-pass**, not an HTML post-pass; a **math-glyph font fallback** is mandatory; the figure dark-lift covers **colored text**).

---

## 0 · CONCEPT

**Name — GRIDPAPER.**
**Essence:** *An engineer's quadrille notebook rebuilt for the screen — warm paper, a faint coordinate grid, ink-blue rules, and one machined monospace part-number stamped on every object you can point at. A serious reference you can deep-link into, read in the dark, and quote to a tutor.*

**Why, for this reader.** The audience is an adult relearning algebra alone, often at night, often math-anxious, doing real pencil-and-paper work. A toy-bright edu-app look says *remedial*; GRIDPAPER says *this is a real, rigorous book that respects you*, and spends its interactivity budget exactly where self-study needs it: scannable structure to find your place, answers revealed only when earned, deep links you can paste to the tutor, and a genuine dark mode. The course already lives on a coordinate plane (`screenX = 110 + x*20` in `figures.py`); the page becomes the same graph paper the figures are drawn on, so a figure never looks pasted into prose — the prose is drawn on the same sheet.

**Three sites, one language, differentiated by paper tint only.** A single `--paper` token shifts per surface via a `data-surface` attribute on `<body>` (one keyword-only template arg, §7). Type, grid, components, motion are identical across all three — instantly one work (Problem 6).

| Surface | Identity | Tint | Accent register |
|---|---|---|---|
| **Textbook** | the notebook | **Ivory** (warmest) | blueprint **blue** primary |
| **Student guide** | the friendly map | **Blueprint** (cool, lighter) | blue + **green** wayfinding |
| **Tutor guide** | the instructor's answer book | **Manila** (buff, denser) | blue + **graphite-red** marks |
| **Appendix** (inside textbook) | lighter addendum | Ivory at reduced ink (`data-surface="appendix"`) | same, muted |

---

## 1 · TYPOGRAPHY

Three families, three jobs. Google Fonts (open-license, self-hostable), each with a robust system fallback so a CDN hiccup degrades gracefully. UI eyebrows/labels are set in **IBM Plex Mono uppercase** (no fourth "drafting sans" family — avoids the Inter cliché and keeps the count at three).

| Role | Face | Job |
|---|---|---|
| **Display** — h1/h2/h3, unit & landing titles, card titles | **Fraunces** (`opsz` 9–144, wght 400–600, SOFT) | Authored, bookish gravity at large optical sizes. |
| **Body** — all prose, definitions, problems, tables, answers | **Source Serif 4** (400/600 + italic) | Screen reading serif that sits *with* KaTeX's Computer-Modern math. |
| **Mono** — code, every refcode, all UI eyebrows/labels, figure captions, data tables | **IBM Plex Mono** (500/600) | Makes the refcode read as a stamped part-number; one machine voice for every identifier. |

### 1.1 Mandatory math-glyph fallback — **[RESOLVED: math blocker #1 & #6 — verified]**
Verified against the corpus: inline Unicode math glyphs that must render in body/headings appear at scale **outside** `$$…$$` — **→ ×538, ² ×603, √ ×161, × ×135, ⇒ ×121, ≤ ×91, ± ×82, ³ ×80, ≥ ×58, ≠ ×37, ÷ ×26, ₁ ×23, ₂ ×13, π ×4, ⁿ ×3, ≈ ×3**. Source Serif 4 and Fraunces do **not** cover all of these (notably `⇒ ⇔ → √ ⁿ ₁ ₂ π`), so per-glyph browser fallback would scatter wrong-weight, wrong-baseline glyphs mid-sentence — destroying the central legibility claim, most visibly inside the new answer-key box. **Fix (two layers):**

1. **Deterministic stack-level fallback** on *both* the body and display stacks, placing a math-complete serif (STIX Two Text → Cambria Math) ahead of the generic system serifs, so any missing glyph degrades to a math face, never to the UI sans.
2. **Belt-and-suspenders build pass `_wrap_inline_math` (B):** wrap stray inline operators `[⇒ ⇔ → √ ⁿ ₁ ₂ π ∞ ≈]` (run **outside** `_protect_math` placeholders) in `<span class="imath">`, where `.imath{font-family:"STIX Two Text","Cambria Math",serif; font-variant-position:normal}`. This makes the fallback face *identical in light and dark* and independent of the host's installed fonts.
3. **Test (NEW):** `test_inline_math_glyphs` asserts the chosen fallback name precedes the generic serif in the body stack and that `.imath` wraps a sampled `⇒`/`√` in a built page.

```css
:root{
  --serif-math: "STIX Two Text","Cambria Math";   /* math-complete fallback */
}
body{font:var(--step-0)/var(--leading-body)
     "Source Serif 4", var(--serif-math), Charter, Georgia, serif;
     text-wrap:pretty;}
h1,h2,h3,.display{font-family:"Fraunces", var(--serif-math),"Iowan Old Style",Georgia,serif;
     line-height:var(--leading-tight); font-weight:600; font-optical-sizing:auto; text-wrap:balance;}
code,pre,.refcode,.eyebrow,figcaption{font-family:"IBM Plex Mono",ui-monospace,Consolas,monospace;}
.imath{font-family:var(--serif-math),"Source Serif 4",serif;}
```

### 1.2 Modular scale — 1.200 (minor third), 18px base
18px is generous for adult eyes without forcing the measure wide; the *minor* third keeps steps close so hierarchy reads as deliberate rhythm. Display sizes escalate via optical size, not a wider ratio. Tokens lock all three sites + KaTeX.

```css
:root{
  --step--1:0.833rem;  /* 15px — refcode stamp, captions, fine print, answer body */
  --step-0: 1rem;      /* 18px — body (html{font-size:112.5%}) */
  --step-1: 1.20rem;   /* 21.6 — lead/deck, h3, callout label-line */
  --step-2: 1.44rem;   /* 25.9 — h2 (lesson) */
  --step-3: 1.728rem;  /* 31.1 — h1 sub-deck / unit standfirst */
  --step-4: 2.074rem;  /* 37.3 — h1 (unit title) */
  --step-5: 2.488rem;  /* 44.8 — landing hero only */
  --leading-body:1.62; --leading-tight:1.15;
  --measure:66ch; --wide:52rem;
}
h1{font-size:var(--step-4); font-variation-settings:"opsz" 40,"SOFT" 30;}
h2{font-size:var(--step-2); font-variation-settings:"opsz" 28,"SOFT" 30;}
```

### 1.3 Font-loading plan — no FOIT, minimal reflow — **[RESOLVED: perf major (loading chain)]**
Render-blocking already includes local CSS + KaTeX CSS. Add fonts without a slow cross-origin chain or a large swap reflow:

1. `<link rel="preconnect" href="https://fonts.googleapis.com">` and `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>` **before** the font stylesheet (cuts 2 handshakes off the critical path).
2. **One** Google-Fonts stylesheet link with `display=swap` (no FOIT) and the Fraunces axis request **restricted to the ranges actually used** (`opsz 9..40`, `wght 400..600`) to shrink the variable-font payload — not the full `9..144`.
3. `@font-face … font-display:swap` plus **metric-matching descriptors** (`size-adjust`, `ascent-override`, `descent-override`) on the fallback so the swap from Georgia/Charter to Source Serif/Fraunces does not shift layout (protects CLS — body copy is the page bulk).
4. **Preload** only the two critical files: Source Serif 4 400 and the single Fraunces heading instance.
5. **Self-host follow-up (deferred, §11):** GitHub Pages cannot set cache headers on Google's origin; self-hosting into the pinned-CDN model later improves repeat-load caching. Not a launch blocker.

### 1.4 Measure & KaTeX seams
Body locks to **66ch**; the current build's single 48rem ribbon for *everything* is the wall-of-text root cause. GRIDPAPER keeps **prose narrow**, lets **artifacts breathe wider** (to `--wide` 52rem) and into the rail (§3). KaTeX tuning:
1. `.katex{font-size:1.06em}` — match CM's x-height to Source Serif.
2. `.katex-display{margin:1.3rem 0; overflow-x:auto}` retained so long equations scroll, never break the measure. **Critical scroll rule re-specified in §4.3/§4.4** — **[RESOLVED: math blockers #2 & #4]**.
3. Inline math stays plain Unicode per the hard constraint (now glyph-safe via §1.1). A literal `$` is safe: KaTeX binds only `$$…$$`, refcodes are mono `<a>` (never `$`-delimited), `_protect_math` shields math through every transform, and the new currency guard (§7) prevents any accidental `$$`.

---

## 2 · COLOR

The figure palette is the law: every UI accent is the figure ink or an AA-corrected cousin. The light ground is **warm ivory, never `#fff`** (kills glare). Purple is demoted to its figure role (parabolas) plus the "New terms" accent, never the global brand color.

**Decision (load-bearing):** there are **two blues**. `--blue #2980b9` = the *figure/graphic* blue, used **only** for ≥24px display text, SVG strokes, borders, and hover states. `--blue-ink #1f6391` = the *text* blue (AA 5.3:1) used for **all body-size links including the top-bar nav**. **[RESOLVED: a11y blocker #1 — verified #2980b9 nav text is 3.9:1 fail.]**

### 2.1 Eyebrow/label colors are AA-corrected against the *card* surface — **[RESOLVED: a11y blockers #2/#3, perf major (table errors) — verified arithmetic]**
The draft's green/amber/red label inks were validated against page ivory but actually render on the lighter card `--paper-2` and on the cooler guide paper, where they failed AA at 15px. All *text/icon* uses now route through dedicated `*-text` tokens derived against the **worst surface** (guide card `#fbfdfe`); the raw figure inks survive **only inside SVG**.

### Light — "Ivory pad" (textbook baseline)
```css
:root{
  --paper:#f7f4ec; --paper-2:#fffdf7;          /* page / raised card */
  --grid:#e7e1d3; --grid-strong:#d8d0bd;       /* quadrille; every-5th + plate ticks */
  --ink:#20242b; --ink-soft:#5c6470; --rule:#ddd6c6;

  /* figure inks (exact) — SVG/borders/≥24px only */
  --blue:#2980b9; --purple:#8e44ad; --red:#c0392b; --green:#27ae60; --amber:#b07a16;

  /* AA-corrected text inks — used for ALL small text/labels/links */
  --blue-ink:#1f6391;   /* 5.3:1 on card */
  --purple-ink:#7d3cab; /* 5.0:1 */
  --red-ink:#b3271a;    /* 5.2:1 */
  --green-text:#15723d; /* 4.7:1 on #fffdf7 — was #1f8a4c (3.98:1 FAIL) */
  --amber-text:#8a5e10; /* 4.9:1 on #fffdf7 — was #b07a16 (3.66:1 FAIL) */

  --accent:var(--blue);           /* graphic accent (borders, strokes) */
  --link:var(--blue-ink);         /* text accent (links) */
  --code-bg:#efe9da; --target-bg:#fff3cf; --figbg:var(--paper-2);
  --tooltip-bg:#20242b; --tooltip-fg:#fffdf7;
}
body[data-surface="guide"]   {--paper:#eef3f5;--paper-2:#fbfdfe;--grid:#dde7ec;--grid-strong:#cbdae1;--rule:#d2e0e6;}
body[data-surface="tutor"]   {--paper:#f4efe3;--paper-2:#fdfbf4;--grid:#e6ddca;--grid-strong:#d7cbb2;}
body[data-surface="appendix"]{--ink:#33383f;--ink-soft:#5c6470;--grid:#ece7da;}  /* ink re-checked AA on ivory (see 2.3) */
```

### Dark — "Slate pad"
A true slate (not black) so chalk figures glow; figure inks are lifted in lightness so the *same* SVG strokes read on the dark field (no asset re-render). Figure **text** labels are lifted too (§4.6).
```css
html.dark{
  --paper:#15181d; --paper-2:#1b1f26; --grid:#23282f; --grid-strong:#2c333c;
  --ink:#e8e6df; --ink-soft:#9aa3af; --rule:#2a313b;
  --blue:#62a8e0; --purple:#bd8ce0; --red:#ef6f63; --green:#54c98a; --amber:#d6a955;
  --blue-ink:#8cc2ef; --purple-ink:#cfa6e6; --red-ink:#f59a90; --green-text:#6fd6a0; --amber-text:#e0b667;
  --accent:var(--blue); --link:var(--blue-ink);
  --code-bg:#222831; --target-bg:#3a371f; --figbg:var(--paper-2);
  --tooltip-bg:#e8e6df; --tooltip-fg:#15181d;
}
html.dark body[data-surface="guide"]   {--paper:#121821;--paper-2:#18202b;--grid:#1f2935;--grid-strong:#27323f;}
html.dark body[data-surface="tutor"]   {--paper:#181712;--paper-2:#1e1c16;--grid:#272318;}
html.dark body[data-surface="appendix"]{--ink:#c4c8d0; --paper:#13161a; --grid:#20242b;}  /* dark appendix actually reads lighter */
```

### 2.2 Contrast ledger (WCAG, measured against the surface each token sits on)
| Token / pair | On surface | Ratio | Verdict |
|---|---|---|---|
| `--ink` body | `--paper` ivory | 14.8:1 | AAA |
| `--ink` body (dark) | `--paper` slate | 13.6:1 | AAA |
| `--link` `#1f6391` body link | `--paper-2` card | **5.3:1** | AA |
| `--link` topbar nav | topbar (≈ivory) | **5.6:1** | AA — **[a11y #1]** |
| `--blue` `#2980b9` (≥24px / strokes / borders) | ivory | 3.9:1 | AA-large / non-text ✓ |
| `--green-text` `#15723d` eyebrow 15px | `#fffdf7` card | **4.7:1** | AA — **[a11y #2, perf]** |
| `--amber-text` `#8a5e10` eyebrow 15px | `#fffdf7` card | **4.9:1** | AA — **[a11y #3, perf]** |
| `--red-ink` / `--purple-ink` 15px | card | 5.2 / 5.0:1 | AA |
| `--ink-soft` captions/marginalia | paper / dark | 5.4 / 5.2:1 | AA |
| Figure colored **text**, dark-lifted (§4.6) | dark figure ground | red 6.9 / blue 6.4 / green 6.6:1 | AA — **[perf blocker #2]** |
| `:focus-visible` ring vs card **and** paper | both | ≥3:1 | AA non-text (§4.1) |
| `--grid` lines | paper | <3:1 | decorative, text-contrast-exempt |

### 2.3 Color-blind & forced-colors safety
- **Color is never the sole signal.** Every callout pairs hue with a mono **eyebrow word** (GOAL / WATCH FOR / …); the code letter (`d`/`c`/`w`/`f`) encodes kind; the answer-key chevron is a **shape** change (§4.2). Fully CVD-safe.
- `:target` pairs a translucent wash with a solid 3px accent bar + motion — legible in both themes, never hue-only.
- **`@media (prefers-contrast:more)`** (new): swap every eyebrow/figcaption/refcode color to `--ink`, thicken borders, and keep the grid off. **[RESOLVED: a11y minor (high-contrast did nothing)]**
- **`@media (forced-colors:active)`** (new): map links→`LinkText`, buttons→`ButtonText`, text→`CanvasText`, card/topbar bg→`Canvas`; drop `backdrop-filter` and `color-mix` grounds; **restore the native `<details>` marker**; set `.chip`/`.refcode` border to `CanvasText`. **[RESOLVED: perf minor (forced-colors untested)]**
- Appendix `--ink #33383f` re-checked: **9.6:1 on ivory** (AA/AAA) light, and dark appendix now shifts paper+grid (not only ink) so "lighter" is visible in both themes. **[RESOLVED: build major (dark appendix)]**

---

## 3 · LAYOUT & SPACE — defeating the wall

One CSS Grid on the existing single `<main>`, a quadrille background, and a deliberate spacing scale. No structural template change beyond the `data-surface` attribute and wrapper classes the build emits. **Left margin rail is canonical**; the right gutter is an opt-in sticky mini-TOC on very wide screens only.

### 3.1 The quadrille ground — signature, ~6 lines, zero assets — **[RESOLVED: build major & usability major (fixed-bg jank on mobile)]**
`background-attachment:fixed` is dropped (it causes scroll jank and mis-paints on mobile Safari/Android). The grid is painted on a `position:fixed` full-viewport `::before` layer behind content (cheap, no per-scroll repaint), lightened on small screens, and removed for print/high-contrast/reduced-data.
```css
body{background-color:var(--paper);}
body::before{content:""; position:fixed; inset:0; z-index:-1; pointer-events:none;
  background-image:linear-gradient(var(--grid) 1px,transparent 1px),
                   linear-gradient(90deg,var(--grid) 1px,transparent 1px);
  background-size:24px 24px;}            /* echoes the figures' 20px/unit grid */
@media (max-width:48rem){ body::before{opacity:.5;} }      /* calmer behind dense prose on phones */
@media print,(prefers-contrast:more),(prefers-reduced-data:reduce){ body::before{display:none;} }
```

### 3.2 Content grid + live margin rail — rail gated where it *fits* — **[RESOLVED: usability major (rail overflow 60–78rem)]**
The absolute rail activates at **78rem** (where measure + rail + gutter are satisfied), not 60rem; stamps are positioned by **named grid lines**, not a hard `left:-12.5rem`, so they track the real gutter. Below 78rem the rail collapses and stamps reflow inline.
```css
main{display:grid; column-gap:0; padding:1.5rem 0 5rem;
  grid-template-columns:
    [full-start] minmax(1rem,1fr)
    [rail-start] minmax(0,12rem)
    [wide-start] minmax(0,calc((var(--wide) - var(--measure))/2))
    [text-start] min(var(--measure),100%) [text-end]
    minmax(0,calc((var(--wide) - var(--measure))/2)) [wide-end]
    minmax(1rem,1fr) [rail-end full-end];}
main > *{grid-column:text;}
main > figure.fig, main > table, main > .katex-display,
main > .worked, main > .practice, main > .answerkey{grid-column:wide; min-width:0;}  /* min-width:0 → math can scroll */
main > .unit-hero, main > .bleed{grid-column:full;}
@media (max-width:78rem){ main{display:block; max-width:42rem; margin:0 auto; padding:1.5rem 1.2rem 4rem;} }
```
**What the rail earns (anti-wall weapons):** the **refcode stamp** for every coded item (§4.1) sits in the gutter like clause numbers; short **marginalia** (cross-refs, a one-line Watch-for flag) pull out of the column; a small mono **section marker** sits beside each `h2`. Nothing is lost when it collapses.

### 3.3 Vertical rhythm — section rests
Uniform spacing *is* the wall. One ramp drives every gap; lessons get big air so each reads as its own sheet.
```css
:root{--s-2:.5rem;--s-3:.75rem;--s-4:1.1rem;--s-5:2rem;--s-6:2.75rem;--s-7:4.5rem;}
p{margin:0 0 var(--s-4);}
h2{margin:var(--s-7) 0 var(--s-4); padding-top:var(--s-5); border-top:1px solid var(--grid-strong);}
h3{margin:var(--s-6) 0 var(--s-3);}
.worked,.practice,.answerkey,figure.fig,[class^="cl-"]{margin-block:var(--s-5);}
```
Each lesson opens with a **standfirst deck**: the *Why it matters* line (isolated by the pre-pass, §4.5) renders at `--step-1` in `--ink` with extra leading — a calm larger lead that breaks the grey before the body starts.

### 3.4 Prose-level rhythm where there are no labels — **[RESOLVED: usability minor (densest pages under-served)]**
Long label-free passages (e.g. the dense 5.3 rate-of-change prose) still need rhythm. The build applies, **heuristically and conservatively**: a `--step-1` lead treatment on the first sentence of any prose block over ~90 words that opens a sub-section, and `max-width:66ch` is never exceeded. No content rewrite (content is final); this is presentation only. Verify on Lesson 5.3 specifically.

### 3.5 The repeating "plate" motif
Worked examples, display equations, and figures share a **2px left grid-tick** (`--grid-strong`/`--blue`) on a `--paper-2` ground, so three content types rhyme down the page — the eye learns "tick = a worked artifact" and navigates by texture.

**Responsive summary.** `<78rem`: single column, rail collapses, refcode becomes an inline chip, mini-TOC hidden. `<48rem`: grid texture at half opacity. `≥90rem`: right gutter gains the sticky per-page mini-TOC from the existing `toc` output. Mobile-first, one source.

---

## 4 · COMPONENT SPEC (with build mapping)

Mechanism keys: **(C)** global CSS · **(T)** shared `_page()` template · **(B)** markdown pre-pass / HTML post-pass. **SACRED ids are restyled/repositioned, never renamed** — verified the tests assert literal `id="12.5.w1"`, `id="12.6.f1"`, `id="12.1.1"`, one `<h1>`, `<figure class="fig"`, `id="fig-{code}"`, and byte-equality.

> **Architecture correction adopted from the build red-team — [RESOLVED: build blocker #1, top-3].** Every "wrap the `<p>`/`<ol>` for this label" idea is moved to a **fence/math-aware markdown PRE-pass** that (a) inserts a blank line before every `**Label:**` so each becomes its own block, and (b) emits a fenced wrapper (a sentinel `<div class="cl-…">…</div>` the converter passes through). Verified necessity: in unit-05 the Goal / Why it matters / New terms labels are **three `<strong>` inlines inside one `<p>`** — there is no per-label `<p>` to post-process, so an HTML post-pass would silently no-op on the most common lesson shape. The tolerant label regex used throughout: `^\*\*(Goal|Why it matters|New terms|Watch for|Teaching arc[^*]*|Visuals to offer|Check for understanding[^*]*|Practice problems|Worked examples?|Answer key)[^*]*:?\*\*` (singular/plural + trailing parenthetical).

### 4.1 Reference-code identifier — *the specimen stamp* (Problem 1)

**Root cause (verified live):** the `<ol>` renders its own `1.` **and** `_convert_anchors` injects `#5.1.1` as the item's first inline — two numbering systems. **Decision — the refcode becomes the single identifier; the visible number a student reads IS the code's trailing segment.**

**The one-number rule — [RESOLVED: usability majors (ordinal cross-refs; decorative chip = second number) — verified content addresses problems by ordinal].** Verified the answer key reads `… · 4. Quadrant IV · …` and prose says "(problems 1–4 …)" / inline "4. Then write …" — i.e. content maps to problems by **ordinal**. So we must keep one human ordinal visible, and it must equal the code's last segment (`5.1.4 → 4`). The draft's separate red "plotted-point chip" is **cut** (it re-introduced two numbers). Instead:

1. **(B) Suppress the competing list marker** only on `<li>`s that actually contain a `.refcode` (per-`li` class `coded`, not the whole `<ol>`, so an uncoded sibling keeps its marker). **[RESOLVED: build major (uncoded orphan)]**
2. **(B) Normalize loose items first.** **[RESOLVED: usability blocker #2, build major — verified 5.1.9/5.1.10/5.2.4–5.2.7 render `<li><p>…`]** The post-pass **unwraps a single child `<p>`** inside any coded `<li>` so tight/loose items have identical structure, *then* applies the grid. A build assertion fails if any coded `<li>` still has `.refcode` nested below the first element child.
3. **The stamp shows the trailing ordinal as the primary glyph**, with the full code as the link text/`aria-label` and copy payload. One number on the card; the canonical code one keystroke away.
4. **(B) Fix the swallowed subheading in the pre-pass.** **[RESOLVED: build major, usability blocker — verified `*Plot & locate:*` absorbed into 5.1.9]** When an italic group subhead line `^\*[^*]+:\*\s*$` follows a list item with no blank line, insert blank lines so it terminates the list and becomes its own `.group-head` (extends `_ensure_list_blank_lines`). This also removes the loose-item cause.
5. **Kind sub-cue, not a second system:** definition stamps carry a thin `--purple` edge, figure stamps a `--blue` edge (from the `d`/`f` letter).
6. **(T) Quote-to-tutor copy** affordance: each stamp is `<a href="#code">`; a copy icon copies the bare code + flashes "copied — paste to the tutor." Progressive enhancement; no-JS still deep-links. The href keeps `#code` for backward-compatible links.
7. **Per-context placement — [RESOLVED: usability minor (blanket absolute rule detaches definition codes)].** The absolute-rail rule is scoped to **practice items and worked examples only**; definitions, checks, and inline-figure refcodes stay inline-adjacent to their bold term/caption. Each `.refcode` context (practice, worked, definition, check, figure) has an explicit placement rule.

```css
.coded{list-style:none;}
li.coded{display:grid; grid-template-columns:max-content minmax(0,1fr); gap:.7rem;  /* minmax(0,) → math shrinks */
  align-items:baseline; padding:.5rem 0; border-top:1px solid var(--rule);}
.refcode{font:600 var(--step--1)/1 "IBM Plex Mono",ui-monospace,monospace; letter-spacing:.02em;
  color:var(--ink-soft); text-decoration:none; white-space:nowrap;}
.refcode .full{position:absolute; width:1px; height:1px; overflow:hidden; clip-path:inset(50%);} /* full code for AT/copy */
.refcode:hover,.refcode:focus-visible{color:var(--blue-ink);}
.refcode:focus-visible{outline:3px solid var(--blue); outline-offset:2px;
  box-shadow:0 0 0 5px color-mix(in srgb,var(--blue) 28%,transparent);}  /* halo ≥3:1 vs chip AND paper — a11y minor */
@media (min-width:78rem){
  li.coded .refcode, .worked .refcode, .practice-item .refcode{
    position:absolute; width:11rem; text-align:right; padding-top:.15em;
    left:auto; margin-left:-12.5rem;}   /* tracks the named gutter; reflows under 78rem */
  .refcode::after{content:""; position:absolute; right:-1.1rem; top:.55em; width:.7rem; height:1px; background:var(--rule);}
}
@media (max-width:78rem){
  li.coded .refcode, .practice-item .refcode{display:inline-block; background:var(--code-bg);
    border:1px solid var(--rule); border-radius:5px; padding:.05em .45em; margin-bottom:.25em;}
}
```
**Accessibility — [RESOLVED: a11y minor (chip vs stamp = two numbers in audio)].** Only **one** token is announced: the `.refcode` link carries `aria-label="reference 5.1.4"`; the visible ordinal glyph is `aria-hidden`. No competing number in any modality.

### 4.2 Answer-key reveal — *progressive disclosure* (Problem 2)

**Hook (verified):** `**Answer key:**` (and parenthetical variants like `**Answer key (all verified):**`, `**Answer key (mean · median · mode · range):**`) then a `·`/ordinal run-on rendered as **one `<li>`**. `<details>` is already shipped in the tutor guide.

**Decisions:**
- **Per-set reveal ONLY in v1. Per-problem reveal is CUT.** — **[RESOLVED: usability blocker #1, math blocker #3, build blocker #2 — all verified]** The per-problem plan relied on `split(" · ")`, but ` · ` is **also multiplication** (verified unit-05 key ends `…(4 · -1/4 = -1)`) and is even used inside the appendix label and as a data separator; delimiters also vary (` · `, double-space, `N)`), keys span multiple lines, and the first item often loses its `1.`. Splitting the presentation blob corrupts math. If per-problem is ever wanted, it must be driven from a **code-keyed structured answer datastore** (the tutor guide already carries per-problem `answer` fields), never from rendered prose — stated as a deferred §11 item, not "ships later."
- **Tolerant detector (B):** match the label with the §4 regex and wrap the label `<p>` **plus every following block until the next heading / `<hr>` / `**Label:**`** (not just one `<ol>`) — captures multi-line keys and trailing `*note*` paragraphs. **[RESOLVED: build blocker #2 (parenthetical labels, multi-block keys)]**
- **Rebuild the run-on into a real `<ol>` (B):** parse the `N.`-marker boundaries (split only at a middot/space immediately followed by `\d+\.`, **outside** `_protect_math`), strip the leading `N.`, emit one `<li>` per answer so a screen reader announces "list, 10 items" with correct numbering, and force the list `start`/CSS counters to match the practice ordinals. **[RESOLVED: a11y blocker (run-on `<li>`), a11y major (degraded semantics) — verified single-`<li>` at unit-05]** Appendix keys that legitimately use ` · ` as in-content data (`6 · 7 · 7 · 6`) are protected by the "middot must be followed by `N.`" rule.
- **Native `<details>`, shape-based chevron — [RESOLVED: a11y blocker #2 & a11y major (color-only triangle)].** Keep `<details>/<summary>` (its expanded/collapsed state is announced natively). The chevron is a **real inline SVG** inside `<summary>` (`aria-hidden`), a box/shape change meeting 3:1 non-text contrast — **not** a color-only CSS `::before`. The native marker is *restored* under forced-colors.
- **Deep-link + focus into closed details — [RESOLVED: a11y blocker (focus lost), build major (nested details), math minor (no-JS)].** On load and `hashchange`: walk **all** `<details>` ancestors of the target and open each (loop, synchronously, **before** the browser's target scroll), then `scrollIntoView()` and move focus to the target (`tabindex="-1"` on the wrapper if needed) so keyboard + screen-reader users land on and hear the revealed item. **No-JS fallback:** a CSS rule opens any `<details>` containing a `:target`, and per-set granularity means a JS-off answer link lands on the (open) set.
- **Spoiler guard — [RESOLVED: usability major (deep-link auto-reveals answer)].** The auto-open + green "affirm" fires **only** when the target id *is* an answer element, never when the target is a problem/definition/figure that merely sits above an answer block. Answer-key `<details>` get their own id namespace (`ak-5.1`) so a problem deep-link scrolls to the problem with its answer **still closed**. The green affirm animation plays on **real user click only**, never on programmatic open. Test: deep-linking a `.N` practice id leaves its answer collapsed.
- **No CSS multicol — [RESOLVED: usability major (multicol fractures derivations) — verified long worked answers in unit-11/12].** The key renders as a **single-column** ordered list (matching practice numbering), `break-inside:avoid` per item; reserve any 2-up only for keys detected all-short, and force single column if any answer contains `.katex`. Single column is the safe default given the corpus.
- **Print:** `@media print` forces `details[open]` so the courtesy print keeps answers (§9).

```css
.answerkey{border:1px solid var(--rule); border-radius:10px; background:var(--paper-2); overflow:hidden;}
.answerkey > summary{cursor:pointer; list-style:none; display:flex; align-items:center; gap:.6rem; padding:.75rem 1rem;}
.answerkey > summary::-webkit-details-marker{display:none;}
.answerkey .chev{flex:0 0 auto; width:.9rem; height:.9rem; border:1.5px solid var(--green-text); border-radius:2px;} /* shape cue */
.answerkey .eyebrow{color:var(--green-text);}
.ak-hint{color:var(--ink-soft); font-size:var(--step--1);} .answerkey[open] .ak-hint{display:none;}
.ak-body{padding:.25rem 1rem 1rem;} .ak-body ol{margin:0;} .ak-body li{break-inside:avoid; margin:.25rem 0;}
@media (forced-colors:active){ .answerkey > summary::-webkit-details-marker{display:revert;} }
```

### 4.3 Worked-example block — *the drafting card*

**Hook + correctness (verified):** worked examples are **sometimes prose, sometimes a `<ul>`/`<ol>`, sometimes inline after the label**; the label appears as `**Worked examples:**`, `**Worked examples** (…)` (no colon), and `**Worked example:**` (singular). **Decision — wrap keys off the *label*, not the list type** (tolerant `Worked examples?` regex), wrapping the run from the label to the next `**Label:**`/`<h2>` in `<section class="worked">`. **[RESOLVED: build blocker #3 — verified colon/no-colon/singular/inline forms across units 02/05/08/10/11/appendix]**
- The practice-subheading promoter (§4.4) is scoped **strictly inside an identified Practice run**, so italic worked-example run-ins like `*w5 — inclusive within.*` are never misclassified as group-heads. **[RESOLVED: build blocker #3]**
- Prose worked examples and italic `*wN*` run-ins carry **no `.wN` id** today (verified `_id_worked_practice` only ids `^\d+\. ` lines). **Decision (explicit):** accept they remain id-less in v1 — the SACRED `.wN` ids are on list-form examples (e.g. `12.5.w1`) and are preserved. The spec text drops any claim that *every* worked example gets a rail stamp. Adding ids to prose/`*wN*` examples is a deferred §11 item.

**(C)** plate styling: `--paper-2` ground, 2px `--blue` left-tick, mono `WORKED` eyebrow, `.wN` stamp in rail (list form). Multi-step solutions render as a bordered sequence. The card is robust to a `<table>`-only or `<p>`-only body (no `.work-step` required) — **[RESOLVED: build major (appendix table worked-ex)]**.

**Display-math scroll inside the card — [RESOLVED: math blockers #2 & #4 — verified wide arrays in unit-07/10/11].** The tinted inset must not eat the scroll viewport: keep `overflow-x:auto` on the element that has **zero inline padding on the scroll axis**, move the tint to an inner wrapper, add `min-width:0`, and signal scroll with `scrollbar-gutter:stable` + a right-edge mask fade. Any `$$block$$` that sits inside a coded `<li>` grid cell is **lifted out** to a full-width child of `.worked` (`grid-column:1/-1`) so display math is never a constrained grid item.
```css
.worked{border:1px solid var(--rule); border-left:3px solid var(--blue); border-radius:0 10px 10px 0;
  background:var(--paper-2); padding:1.1rem 1.25rem; min-width:0;}
.worked .eyebrow{display:block; color:var(--blue-ink); margin-bottom:.4rem;}
.worked .work-step + .work-step{margin-top:1.1rem; padding-top:1.1rem; border-top:1px dashed var(--rule);}
.worked .katex-display{min-width:0; overflow-x:auto; padding-inline:0; padding-block:.5rem;
  -webkit-mask-image:linear-gradient(90deg,#000 calc(100% - 1.5rem),transparent);
          mask-image:linear-gradient(90deg,#000 calc(100% - 1.5rem),transparent);}
.worked .mathwrap{background:color-mix(in oklab,var(--blue) 7%,var(--paper-2)); border-radius:8px; padding:.5rem .75rem;}
```

### 4.4 Practice / problem-set block — *numbered cards* (Problem 5)

**Hook:** `**Practice problems:**` and `*italic sub-headings*` grouping items. The swallowed-subheading and loose-item fixes (§4.1.4, §4.1.2) apply here first.

**(B)** wrap as `<section class="practice">`; promote `*italic*` subheads (scoped to this run only) to `<h4 class="group-head">`; each item is a `.practice-item` card whose structure is normalized (no stray `<p>` wrapper). **(C)** responsive card grid — short numeric drills tile 2–3 across (finally using the width), prose/graph problems span full via `.long`. Each card shows **one** number: the code-derived ordinal as a chip, full code in the rail/`aria-label` (no separate decorative point-chip — §4.1). `:target` gives a 3px ring **and** a thickened left edge so the state survives reduced-motion and CVD — **[RESOLVED: a11y major (hover/focus = hue-only, removed under reduced-motion)]**.
```css
.practice{display:grid; gap:.6rem;}
.practice .group-head{font:600 var(--step--1) "IBM Plex Mono",monospace; text-transform:uppercase;
  letter-spacing:.05em; color:var(--ink-soft); margin-top:1.1rem;}
.problem-grid{display:grid; gap:.6rem; grid-template-columns:repeat(auto-fill,minmax(min(100%,20rem),1fr));}
.practice-item{display:grid; grid-template-columns:max-content minmax(0,1fr); gap:.7rem; align-items:start;
  background:var(--paper-2); border:1px solid var(--rule); border-left:2px solid var(--rule); border-radius:9px; padding:.6rem .8rem;}
.practice-item:hover,.practice-item:focus-within{border-color:var(--blue); border-left-width:4px;}  /* shape change, not hue-only */
.practice-item:target{border-color:var(--blue); border-left-width:4px;
  box-shadow:0 0 0 3px color-mix(in srgb,var(--blue) 22%,transparent);}
.practice-item .chip{width:1.6rem; height:1.6rem; display:grid; place-items:center; border-radius:50%;
  font:600 .8rem "IBM Plex Mono",monospace; color:var(--ink-soft); background:var(--paper); border:1.5px solid var(--rule);}
.problem-grid > .practice-item.long{grid-column:1/-1;}
```

### 4.5 Callout family — *engineering-stencil labels* (the hierarchy engine, Problem 3)

The lesson's bold `**Label:**` parts are the strongest already-present hook. **Decision: one skeleton (mono eyebrow + accent + body), seven semantic skins**, produced by the **pre-pass** (§4 correction) so glued inline labels each get their own block. This is the single biggest scannability win.

| Source label | Class | Accent · eyebrow | Treatment |
|---|---|---|---|
| `**Goal:**` | `.cl-goal` | `--blue-ink` · GOAL | Lead "contract": thin top rule, no box, slightly larger. |
| `**Why it matters:**` | `.cl-why-deck` | — | The standfirst **deck** (§3.3), not a box. |
| `**New terms:**` (+ `.dN`) | `.cl-terms` | `--purple-ink` · NEW TERMS | Definition list; bold term leads, code in rail. |
| `**Watch for:**` | `.cl-watch` | `--red-ink` · WATCH FOR | The one cautionary skin; dashed left-tick. |
| `**Teaching arc…**` / `**Visuals to offer:**` | `.cl-note` | `--ink-soft` · neutral | Quiet, tutor-facing. |
| Objectives **blockquote** (*Prerequisites / By the end…*) | `.cl-objectives` | `--blue` · BEFORE YOU START / YOU'LL BE ABLE TO | Blueprint title-block at unit top; outcomes as green-ticked checklist. |
| **Wrap-up** parts (Consolidate / Mix back in / Looking ahead / Progress Card) | `.cl-wrap` | `--green-text` · WRAP-UP | End-of-unit summary plate, heavier rule. |

**Scope guard — [RESOLVED: build minor (mid-lesson blockquotes)].** `.cl-objectives` is scoped to the **first blockquote in `<main>`** (or detected by "Prerequisites/By the end" content); generic mid-lesson `>` callouts (e.g. unit-11 "Stopping rule.") get a separate quiet skin, not the objectives title-block.
```css
[class^="cl-"]{border:1px solid var(--rule); border-radius:10px; background:var(--paper-2); padding:.9rem 1.1rem;}
[class^="cl-"] > .eyebrow{font:700 var(--step--1)/1 "IBM Plex Mono",monospace; text-transform:uppercase;
  letter-spacing:.07em; display:block; margin-bottom:.4rem;}
.cl-goal{border:0; border-top:2px solid var(--blue); border-radius:0; background:none; font-size:var(--step-1); padding:.6rem 0;}
.cl-goal .eyebrow{color:var(--blue-ink);}
.cl-why-deck{font-size:var(--step-1); color:var(--ink); line-height:1.5; border:0; background:none; padding:0;}
.cl-terms{border-left:3px solid var(--purple);} .cl-terms .eyebrow{color:var(--purple-ink);}
.cl-watch{border-left:3px dashed var(--red);}   .cl-watch .eyebrow{color:var(--red-ink);}
.cl-note{background:none; border:0; border-left:2px solid var(--rule); color:var(--ink-soft);}
.cl-objectives,.cl-wrap{border-width:2px;} .cl-wrap{border-left:3px solid var(--green);} .cl-wrap .eyebrow{color:var(--green-text);}
.cl-quote{border-left:3px solid var(--ink-soft); background:none; color:var(--ink); font-style:italic;}
```
**"Teaching this unit":** in the textbook it renders inside a `.cl-note` `<details>` collapsed by default (out of the student's way); in the tutor surface it is open with the graphite-red register.

### 4.6 Figure frame — *the mounted plate*

Figures already ship as `<figure class="fig"><svg/><figcaption>` (verified palette: axes `#888`, line `#2980b9` @2.5, points `#c0392b` r3.5, sans-serif 10px labels). **Decision: frame as drawing plates; recolor scaffolding *and colored text* for dark via scoped CSS — no asset duplication.**

**Dark-mode colored-text lift — [RESOLVED: perf blocker #2 — verified 17 red, 5 blue, 1 green `<text fill>`; red text = 3.04:1 / blue = 3.84:1 on dark ground both FAIL AA].** Extend the lift to colored `<text>`, reusing the dark `--red/--blue/--green` values (→ ≈6.4–6.9:1).
```css
figure.fig{background:var(--paper-2); border:1px solid var(--rule); border-left:2px solid var(--blue); border-radius:12px;
  padding:1.1rem 1.1rem .6rem; position:relative; text-align:center;
  background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);
  background-size:24px 24px;}
figure.fig::before{content:""; position:absolute; top:.6rem; left:.6rem; width:.7rem; height:.7rem;
  border-left:2px solid var(--grid-strong); border-top:2px solid var(--grid-strong);}
figure.fig svg{max-width:100%; height:auto; display:block; margin-inline:auto;}
figcaption{font:var(--step--1)/1.4 "IBM Plex Mono",monospace; color:var(--ink-soft); margin-top:.6rem; text-align:left;}
figcaption::before{content:"FIG "; color:var(--blue-ink); font-weight:700; letter-spacing:.05em;}
/* dark chalk lift — inlined SVGs recolored by attribute selector; geometric strokes ≥2.5px stay as-authored (3:1 ok) */
html.dark figure.fig [stroke="#888"]{stroke:#6b7480;} html.dark figure.fig text[fill="#888"]{fill:#9aa3b0;}
html.dark figure.fig text[fill="#c0392b"]{fill:#ef6f63;}  /* 6.9:1 */
html.dark figure.fig text[fill="#2980b9"]{fill:#62a8e0;}  /* 6.4:1 */
html.dark figure.fig text[fill="#27ae60"]{fill:#54c98a;}  /* 6.6:1 */
```
**Test (NEW):** assert no raw `#c0392b`/`#2980b9`/`#27ae60` survives in a `<text fill>` *unlifted* under `html.dark`. `.fig.wide` opts a detailed figure into the wide track. **No diffusion imagery ever touches a figure** (sympy SVG is the sacred, verified job). The `figcaption` already carries the code → `id="fig-{code}"` and `<figure class="fig"` are preserved (tests stay green). **Cleaner long-term (deferred §11):** drive label `fill` from `currentColor` in `figures.py`.

### 4.7 Navigation + landing/index — *the drafting header & catalog*

**(T) Top bar (all sites):** keep the sticky `.topbar`, the `#theme` button, and the `a1-theme` key **unchanged** (sacred). Reskin as a slim drafting strip: paper-tinted, hairline base, **Fraunces wordmark** + unit code in mono left, breadcrumb center, theme toggle right (glyph `◐` → sun/blueprint SVG, mechanism identical). A 2px `--blue` scroll-progress hairline under the bar (one cheap scroll listener; hidden under reduced-motion). `:target{scroll-margin-top:5rem}` retunes the offset to the new bar height. **`backdrop-filter` is `@supports`-gated with an opaque fallback** (perf), and **scroll-margin-top is set on the content element, not the absolute refcode** — **[RESOLVED: math minor (target lands under header)]**.
```css
.topbar{position:sticky; top:0; z-index:20; display:flex; align-items:center; gap:1.5rem; padding:.55rem 1.2rem;
  background:var(--paper); border-bottom:1px solid var(--rule); font:var(--step--1) "IBM Plex Mono",monospace;}
@supports ((backdrop-filter:blur(1px)) or (-webkit-backdrop-filter:blur(1px))){
  .topbar{background:color-mix(in srgb,var(--paper) 90%,transparent); backdrop-filter:saturate(1.2) blur(8px);}}
.topbar a{color:var(--link);}   /* AA — never raw --blue */
.topbar .wordmark{font-family:"Fraunces",serif; font-weight:600; font-size:var(--step-0);}
.worked,.practice-item,figure.fig,li.coded,[class^="cl-"]{scroll-margin-top:5rem;}  /* offset on content, not the absolute anchor */
:target{scroll-margin-top:5rem;}
```

**Landing & index — front door (B/T/C):**
- **Hero band** (`.unit-hero`, `grid-column:full`): the existing template `<h1>` (no second `<h1>` — keeps `test_one_h1_per_page`), the one-line essence, a generated hero (§5) behind.
- **Landing** three entries become three hero cards sharing the language, each with its surface-tint swatch chip so wayfinding teaches itself; the tutor card carries the graphite-red register.
- **Unit index** (`ul.units`) becomes a responsive **catalog of cards**: unit number in big Fraunces, title, one-line description, optional-tag in `--amber-text`, a per-unit topic-color spine bar. Hover lifts 1px (reduced-motion: none).
- A persistent **"how to quote a code to the tutor"** strip on the landing.
- **≥90rem:** sticky per-page mini-TOC in the right gutter from the existing `toc` output.

### 4.8 Cross-site consistency for the refcode + reveal — **[RESOLVED: perf major #5 — verified tutor guide uses `<div class="tproblem" id><a class="refcode">` and a bespoke `<details><summary>Worked solution</summary>`]**
The refcode CSS must target the **`.refcode` class itself** (placement/`#`-strip on `.refcode`), not three structure-specific selectors, so the tutor guide's `.tproblem` refcode gets the same rail mechanism. `build_tutor_guide` emits a shared wrapper class (`.refcard`) on each `.tproblem` so the rail rule fires there too. The tutor-guide "Worked solution" `<summary>` is given the **same eyebrow + shape-chevron styling** as the answer-key summary so both reveals read as one component. **Test (NEW):** extend `test_integration` / smoke to assert the refcode markup shape and the disclosure summary class are identical across `docs/textbook`, `docs/student-guide`, `docs/tutor-guide`.

---

## 5 · IMAGERY — "Blueprint Plates" art direction (Problem 4)

A single rigid system so generated art reads as a family, never AI clip-art. Imagery is **decorative/illustrative only — it never depicts math** (the sympy SVGs' sacred job) and never sits beside a real figure.

**Style.** Cyanotype-meets-engineering-diagram / two-color risograph. Confident single-weight ink linework on warm paper; sparse cross-hatching; the faint quad grid showing through; registration ticks; **no text in the image** (localization-safe); no photoreal, gloss, gradients-as-shading, mascots, faces, or emoji-adjacent icons.

**Palette lock (to the generator):** paper `#f7f4ec`/`#fffdf7`; primary ink `#1f6391`/`#2980b9`; accents **strictly** the figure inks (purple `#8e44ad`, red `#c0392b`, green `#27ae60`); grid `#e7e1d3`. **One dominant accent per image, keyed to the unit's topic color.** Dark variants invert to slate with luminous blue linework.

**Motif vocabulary = the curriculum's own mental models** (from `metaphors.md`/`visuals.md`): balance scale (equations), staircase/ramp (slope), function machine (functions), tiled area model (distributive/factoring), garden-plot grid, number-line walk, stacked coins (negatives/money), bridge cable (parabola), constellation of plotted points. The art *teaches*.

### 5.1 Delivery — capped, lazy, theme-correct — **[RESOLVED: perf blocker #1 — 17 slots × 2 themes raster would be 4–12MB, 4–11× the entire current ~1.1MB site]**
- **Default path = SVG line-art with `currentColor`/token strokes** for ALL openers and section glyphs → **one file recolors per theme**, zero dual-theme raster.
- **If raster ships (the required `nano-banana` path):** WebP/AVIF only, **≤80KB/image enforced in the build** (`build_landing`/`_unit_pages` assert the byte budget); `loading="lazy" decoding="async"` + explicit `width`/`height` on every non-hero image; theme served via `<picture><source media="(prefers-color-scheme:dark)">` **and** a `html.dark` CSS `background-image` swap (so only one variant downloads and it reconciles with the manual `dark` class); the **landing hero is the only `fetchpriority="high"` eager image**.
- All assets are **static, reviewed, committed** (same discipline as figures), never generated at the learner's runtime — keeps GitHub Pages light and the build deterministic.
- **The site launches with zero raster** (CSS quad texture + SVG glyphs + the figures carry it). Imagery is additive polish, gated behind the measured budget; never a load-bearing dependency.

**Roles (defined slots):** Hero (landing + each index, behind the wordmark) · Unit opener (`grid-column:full`, ~3:1 letterbox, keyed to the unit's metaphor + topic color) · Section marker (≤48px SVG glyph in the rail, `--ink-soft`) · Illustrative spot (rail-width line vignette in a *Why it matters* deck, captioned like a figure) · Texture (the CSS quad grid + faint grain, theme-aware, always on).

**Guardrail:** every generated image must depict a **named course metaphor**; if it can't justify itself pedagogically, it doesn't ship.

---

## 6 · MOTION — restrained, reduced-motion-safe

**Everything lives inside `@media (prefers-reduced-motion:no-preference)`; the reduced-motion path is the default static, fully-functional experience.** Transform/opacity only; 120–320ms except the deliberate target pulse. No parallax, scroll-jacking, autoplay, spinners, loops.

1. **Page-load reveal — FOUC/LCP-safe — [RESOLVED: perf minor (opacity:0 resting state harms LCP)].** Content is **visible by default**; the reveal animates only as an enhancement (`@starting-style` / fill-mode that never persists `opacity:0`). The **`<h1>` and first paragraph (LCP candidates) are excluded**. **Triggered after `renderMathInElement` resolves** (or skipped on blocks containing `.katex-display`) so math height settles before animating — **[RESOLVED: build major (load reveal animates pre-KaTeX height)]**.
2. **Refcode `:target` pulse — the signature.** A ~1.6s warm pulse: a `--target-bg` wash blooms and recedes, plus a persistent 3px `--blue` left bar so the highlight *stays*; the rail stamp briefly brightens. Upgrades the old flat `outline:2px` while keeping the 5rem offset.
3. **Answer reveal.** `<details>` open animates height/opacity ~220ms (`interpolate-size`/grid-rows where supported; instant elsewhere); the shape-chevron rotates. Green affirm **only on real user click**, never programmatic (spoiler guard, §4.2).
4. **Theme switch.** 180ms `background-color`/`color` crossfade on `:root`. Excluded under reduced-motion. `a1-theme` logic untouched.
5. **Hover micro-states.** Cards: border thickens + `--blue` (a *shape* change, survives CVD); 120–150ms; copy flashes a 1s tooltip (`--tooltip-bg/-fg`).
```css
:target{scroll-margin-top:5rem;}
@media (prefers-reduced-motion:no-preference){
  :target > .refcode{animation:stamp 1.2s ease-out 1;}
  .worked:target,.practice-item:target,[class^="cl-"]:target,figure.fig:target,li.coded:target{animation:pulse 1.6s ease-out 1;}
  @keyframes pulse{0%{background:var(--target-bg);box-shadow:inset 3px 0 0 var(--blue);}100%{background:var(--paper-2);box-shadow:inset 3px 0 0 var(--blue);}}
  @keyframes stamp{0%,40%{color:var(--blue-ink);transform:scale(1.06);}100%{transform:scale(1);}}
}
@media (prefers-reduced-motion:reduce){ :target{outline:2px solid var(--blue);} .topbar .progress{display:none;} }
```

---

## 7 · BUILD-MAPPING — how each component is produced

**All three sites and the landing import `build_textbook.CSS` and `build_textbook._page`**, so every change propagates to all four. The `--check` byte-equality gate means *the design is the build*.

**Operational fix — [RESOLVED: build blocker #4, perf major #7 (byte-equality blast radius + all-callers TypeError)]:**
- Add **`_verification/build_all.py`** with `generate()` (calls all four generators in order) and `--check` (aggregates all four `check()` lists + `smoke_test.check()`), so "regenerate everything" and "gate everything" are **one command**. CI runs the single aggregate gate; a partial regenerate is caught with a clear message.
- The new `_page()` `surface` parameter is **keyword-only with default `"textbook"`** (`def _page(title, body, prev_link, next_link, subtitle="", *, surface="textbook")`), so existing positional callers don't throw; only callers that opt into a tint change. Still regenerate all four in one commit.

| Component | Mechanism | Production detail · **NEW work flagged** |
|---|---|---|
| Tokens, type, grid, quad ground, spacing, plate motif, math-glyph stack, contrast/forced-colors/high-contrast blocks | **C** | Replace the ~30-line `CSS` string wholesale with §1–3. Shared verbatim by all four builds. |
| Fonts (preconnect, swap, axis-scoped, metric-matched, preload) | **T** | §1.3 `<head>` additions. Self-host deferred (§11). |
| Per-surface tint | **T (NEW)** | `surface` **keyword-only** arg → `<body data-surface>`; callers pass `"guide"`/`"tutor"`; `_unit_pages` passes `"appendix"` when `u.id=="A"`. |
| **Markdown label pre-pass** (the spine) | **B (NEW)** | Fence/math-aware pass: insert a blank line before every `**Label:**` (tolerant regex), emit `cl-*` wrappers; **drives callouts, deck, worked-card, practice-wrap, answer-key**. Replaces every "post-process the HTML for this label" idea. **[build blocker #1]** |
| Refcode stamp (single number = trailing segment; kill marker per-`li`; unwrap loose `<p>`; per-context placement; copy button) | **B+T (NEW)** | §4.1. Build assertion: every coded `<li>` has `.refcode` as first element child. id stays as `id="..."`. **[Problem 1; usability blocker #2/#3; build major]** |
| Swallowed subheading + loose-item normalization | **B (NEW)** | Extend `_ensure_list_blank_lines` to split a trailing `*…:*` onto its own line. Regression assert: unit-05 has a "Plot & locate" group-head and 5.1.9/5.1.10 are siblings. **[build major; usability blocker]** |
| Answer-key reveal (per-set only; tolerant detector; rebuild run-on into real `<ol>`; shape-chevron; spoiler-guarded auto-open + focus; single column) | **B+T (NEW)** | §4.2. **Per-problem reveal CUT** (deferred §11). **[Problem 2; usability blocker #1; math blocker #3; build blocker #2; a11y blockers]** |
| Deep-link into closed `<details>` (open all ancestors, scroll, move focus; CSS no-JS fallback) | **T+C (NEW)** | §4.2. **[a11y blocker; build major; math minor]** |
| Worked-example card (label-keyed wrap; robust to table/prose body; math scroll inside inset; lift `$$` out of grid cell) | **B+C (NEW)** | §4.3. Prose/`*wN*` examples stay id-less in v1 (documented). **[build blocker #3; math blockers #2/#4]** |
| Practice cards + group-heads (one number; shape-based hover/target) | **B+C (NEW)** | §4.4. Promoter scoped **inside the practice run only**. **[Problem 5; usability majors; a11y major]** |
| Callout family (7 skins) + objectives scope guard + mid-lesson quote skin | **B+C (NEW)** | §4.5. **[Problem 3; build minor]** |
| "Teaching this unit" collapse | **B (NEW)** | Textbook: `<details>` collapsed; tutor: open. |
| Figure frame + dark lift of scaffolding **and colored text** | **C** | §4.6 all-CSS; figures untouched (tests green). Test: no unlifted colored `<text fill>` under dark. **[perf blocker #2]** |
| Cross-site refcode/reveal unification (`.refcode`-class targeting; `.refcard` on `.tproblem`; shared summary style) | **B+C (NEW)** | §4.8 in `build_tutor_guide`. Cross-site shape assertion. **[perf major #5]** |
| Currency `$` guard | **B (NEW)** | Render `$` (and any rendered literal `\$`) as `<span class="cur">$</span>` in a post-pass so a dollar can never concatenate into an accidental `$$`; also clears the verified backslash-dollar artifact (unit-07). Test: no `$$` in a text node outside a math placeholder; no `\$` outside math. **[math major (currency); perf minor (backslash-dollar) — both verified]** |
| Top bar, wordmark, progress hairline, theme glyph, `@supports` backdrop | **T+C** | §4.7. `a1-theme` key + `dark`-class logic unchanged (sacred). |
| Landing / index catalog cards + heroes | **B+C** | Reuse the template `<h1>` (no second `<h1>`). |
| Imagery assets | external (`nano-banana`) + **B** | §5.1: SVG-first; raster ≤80KB WebP/AVIF, lazy, `<picture>` theme-swap, budget asserted. Launches with zero raster. **[perf blocker #1]** |
| Motion | **C (+tiny T)** | §6 under reduced-motion guard; reveal post-KaTeX, LCP-excluded. **[perf minor; build major]** |
| `build_all.py` + aggregate `--check` | **NEW file** | One command regenerates + gates all four + smoke. **[build blocker #4; perf major #7]** |
| Print stylesheet (force details open; reflow rail stamps inline; clear grid on figure/.worked/body; opaque topbar; single-column key) | **C (NEW)** | §9. Smoke assert: print CSS contains a details-open rule. **[perf major (print)]** |

### Test updates required (summary)
- **Keep green (no change):** `test_check_clean`, integration byte-equality, `test_deeplink_ids_present` (ids preserved on the same elements), `test_one_h1_per_page`, `test_figure_svg_embedded`, `test_math_escaped_in_arrays`, `test_definition_and_check_anchors`, smoke figure-embedding.
- **Add:** (1) inline-math glyph fallback present + `.imath` wraps `⇒`/`√`; (2) no unlifted colored `<text fill>` under `html.dark`; (3) every coded `<li>` has `.refcode` first; (4) unit-05 "Plot & locate" group-head exists, 5.1.9/5.1.10 siblings; (5) deep-linking a `.N` practice id leaves its answer `<details>` closed; (6) answer-key `<ol>` has one `<li>` per answer with matching count; (7) print CSS forces `details[open]`; (8) cross-site refcode + summary markup shape identical across the three sites; (9) no `$$` in a non-math text node and no `\$` outside math; (10) per-image byte budget (when raster ships).

### Hard-constraint ledger (all honored)
Single shared CSS + single template → all three sites move together (one `build_all`). KaTeX `$$…$$` and literal `$` untouched (`_protect_math` shields every transform; refcodes are mono `<a>`; new currency guard prevents accidental `$$`). Dark mode = full light + dark token sets; `a1-theme` key and `dark` class unchanged. Deep-linking — every SACRED id (`5.3.w1`, `5.1.1`, `5.1.d1`, `5.1.c1`, `5.6.f1`, `12.*`, `A.*`) stays an element `id`, restyled never renamed; `:target` highlights + scrolls with a 5rem offset set **on the content element**, enhanced. Figures stay sympy-accurate SVG with the existing palette, framed not redrawn. Voice plain/instructional, **no emoji**. The `--check` byte-equality gate satisfied by `build_all` regenerating + committing all four after the change.

---

## 8 · ORDERED IMPLEMENTATION PLAN

Each step is independently committable and leaves the byte-equality gate green (run `python _verification/build_all.py && python _verification/build_all.py --check` after every step). Earlier steps are safe even if later steps slip.

1. **Scaffolding & gate.** Add `build_all.py` (generate + aggregate `--check` incl. smoke). Make `_page(... , *, surface="textbook")` keyword-only; emit `data-surface`. No visual change yet. Confirm all four `check()` + smoke still pass. **[build blocker #4]**
2. **CSS string, part A — foundation.** Replace `CSS` with §1–3 tokens, math-glyph stacks (§1.1), modular scale, quad ground (`::before`, no fixed-attach), spacing ramp, plate motif, the two-blue link rule, the corrected `*-text` tokens, full light+dark+guide+tutor+appendix token sets, and the `prefers-contrast`/`forced-colors`/`reduced-data` blocks. Regenerate; visually QA one unit + landing. **[a11y #1/#2/#3, perf (tables), build/usability (mobile grid)]**
3. **Font loading.** Add preconnect + axis-scoped swap link + metric-matched fallback descriptors + preload (§1.3). **[perf (loading)]**
4. **Template & nav.** Reskin `.topbar` (wordmark, breadcrumb→`--link`, SVG theme glyph keeping `#theme`/`a1-theme`, `@supports` backdrop, progress hairline). Add the copy-button + open-details-on-target + focus-move script lines. `scroll-margin-top` on content elements. **[a11y blocker (deep-link focus), math minor]**
5. **Markdown pre-pass spine.** Implement the fence/math-aware label pre-pass (blank line before each `**Label:**`, tolerant regex, `cl-*` wrappers), the swallowed-subheading/loose-item normalization, and the practice-run scoping. This is the riskiest change — land it behind thorough fixture tests on units 02/05/08/10/11/appendix before styling. **[build blocker #1/#3, usability blocker, math]**
6. **Refcode system.** Post-pass: per-`li` marker suppression, loose-`<p>` unwrap, single-number stamp (trailing segment visible, full code in `aria-label`/copy/href), per-context placement, kind edges. Add the "coded `<li>` first-child" assertion. **[Problem 1; usability blocker #2/#3]**
7. **CSS string, part B — components.** Callouts (7 skins + objectives scope + quote skin), worked card (math-scroll inset, robust body), practice cards (one number, shape-based states), figure frame + dark colored-text lift. **[Problems 3/5; perf blocker #2]**
8. **Answer-key reveal.** Pre/post-pass: tolerant detector, wrap label + following blocks, rebuild run-on into a real `<ol>`, native `<details>` + shape-chevron, single column, spoiler-guarded auto-open, answer id namespace, currency guard. Per-set only. **[Problem 2; usability blocker #1; math blocker #3; build blocker #2; a11y blockers]**
9. **Cross-site unification.** `build_tutor_guide`: `.refcard` on `.tproblem`, shared summary styling; `build_student_guide`/`build_landing`: catalog cards + hero slots + surface tint. Add the cross-site shape assertion. **[perf major #5; Problem 6]**
10. **Motion.** Add §6 keyframes under the reduced-motion guard; gate the load reveal to post-KaTeX and exclude LCP elements. **[perf minor; build major]**
11. **Print stylesheet.** Replace the one-line print block with §9. Add the details-open smoke assert. **[perf major (print)]**
12. **Imagery (last, additive).** SVG section glyphs + unit-opener line-art (token strokes). Only then, if approved, `nano-banana` raster under the ≤80KB budget with lazy/`<picture>` wiring and the byte-budget assert. Site is already complete without this. **[perf blocker #1; Problem 4]**
13. **Final gate.** `build_all.py --check` clean; full `pytest`; manual deep-link/keyboard/screen-reader/dark/mobile/print pass on units 05, 11, 12, appendix + all three index pages; commit all regenerated output.

---

## 9 · PRINT (courtesy) — **[RESOLVED: perf major (print fallback)]**
```css
@media print{
  body::before, figure.fig, .worked, .practice{background-image:none !important;}  /* kill ALL grid grounds, not just body */
  .topbar{position:static; backdrop-filter:none; background:#fff;} #theme,.topbar .progress{display:none;}
  details{display:block;} details[open], details{}; details > summary{display:none;} details > *{display:revert;}  /* force every reveal open */
  li.coded .refcode,.worked .refcode,.practice-item .refcode{position:static; margin-left:0; width:auto; text-align:left;}
  .ak-body{columns:1;} a{color:inherit; text-decoration:none;}
  .worked,.practice-item,figure.fig{break-inside:avoid;}
}
```

---

## 10 · ONE LINE
*The page is the graph paper the math is drawn on; the reference code is the one part-number stamped in the margin (and it is the only number you see); the figure palette is the hierarchy doing double duty — a serious, screen-native engineering notebook you can deep-link into, read in the dark, and quote to a tutor.* That is GRIDPAPER.

---

## 11 · DELIBERATELY DEFERRED (minor, non-blocking)
1. **Per-problem answer reveal** — cut from v1; only viable from a code-keyed structured answer datastore (the tutor guide already has per-problem `answer` fields), never by splitting the presentation blob. Revisit when/if that datastore is built for the textbook. **[usability blocker #1, math blocker #3, build blocker #2 all close by cutting it now.]**
2. **Ids for prose / `*wN*` worked examples** — they stay id-less in v1 (SACRED list-form `.wN` ids are preserved). Add a pre-pass to inject `{#lesson.wN}` later if linkability is wanted.
3. **Self-hosting the fonts** into the pinned-CDN model — improves repeat-load caching on GitHub Pages; launch uses Google Fonts with preconnect/swap/metric-matched fallbacks, which is FOIT-free and CLS-safe.
4. **`currentColor`-driven figure labels in `figures.py`** — cleaner than the scoped dark CSS attribute-lift, but requires regenerating all SVGs; the CSS lift fully resolves the contrast hole now without touching assets.
5. **Right-gutter mini-TOC** — ships only at ≥90rem from the existing `toc` output; not present on smaller screens by design.
6. **Per-unit topic-color ramp** for index spines and imagery accents — a small curated map (linear→blue, quadratics→purple, …); ships with imagery (step 12), not required for the type/layout system.

**Files reviewed to ground this final spec (all verified, not assumed):** `_verification/build_textbook.py` (`CSS` L179, `_convert_anchors` L84, `_id_worked_practice` L54, `_ensure_list_blank_lines` L103, `md_to_body` L123, `_page` L133 signature, `_unit_pages` L224), `_verification/build_tutor_guide.py` (`.tproblem`/`.refcode`/`<details>` at L43–51 — cross-site structure), `_verification/build_student_guide.py`, `_verification/build_landing.py` (all import `build_textbook.CSS`/`_page`), `_verification/tests/test_textbook.py` + `test_integration.py` + `_verification/smoke_test.py` (the SACRED-id, one-`<h1>`, figure-embed, byte-equality contract and the four-site + smoke check surface), `docs/textbook/unit-05.html` (live double-number; loose `<li><p>` at 5.1.9/5.1.10 and 5.2.4–5.2.7; glued Goal/Why/New-terms `<strong>` in one `<p>`; single-`<li>` run-on answer key), `algebra-1-tutor/figures/5.3.f1.svg` (palette + colored `<text fill>` labels), the unit markdown corpus (verified counts: ⇒×121, →×538, √×161, ²×603 etc. all outside `$$`; ` · `×359 used as both separator and multiplication incl. unit-05 `(4 · -1/4 = -1)`; answer-key label variants incl. `**Answer key (mean · median · mode · range):**`; worked-label variants colon/no-colon/singular; `\$` currency from unit-07).