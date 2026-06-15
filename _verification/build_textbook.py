"""Generate the HTML textbook from the unit .md prose + SSOT + bundled figures (build tooling).

Each lesson is its own page (unit-NN-M.html), reached from a persistent left sidebar and linear
prev/next nav; each unit also gets a short overview page (unit-NN.html), and the book opens with a
how-to-use page. The math source is the student copy in textbook-src/ (falling back to the tutor
unit .md), kept in lockstep with the SSOT-verified math by check_textbook_src.py. Math renders via
KaTeX (a pinned CDN is fine for a website). Reference codes become deep-link targets; bundled figure
SVGs are embedded inline.

CLI:
  python _verification/build_textbook.py            # (re)generate docs/textbook/
  python _verification/build_textbook.py --check    # verify the committed site is current
"""
import argparse, glob, html as _html, os, re, sys
import markdown as mdlib
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
UNIT_MD = os.path.join(REPO_ROOT, "algebra-1-tutor", "references", "units")
TEXTBOOK_SRC = os.path.join(REPO_ROOT, "textbook-src")
FIG_DIR = os.path.join(REPO_ROOT, "algebra-1-tutor", "figures")
OUT_DIR = os.path.join(REPO_ROOT, "docs", "textbook")
ASSETS_DIR = os.path.join(REPO_ROOT, "docs", "assets")
KATEX = "0.16.11"
ANCHOR_RE = re.compile(r"\{#([^}\s]+)\}")
FCODE_RE = re.compile(r"^(?:[1-9]|1[0-2]|A)\.\d+\.f\d+[a-z]?$")
_CODE_RE = re.compile(r"^([0-9]+|[A-Z])\.(\d+)\.(.+)$")  # scope.lesson.item (3-part lesson codes only)


def _label_for(code):
    """Plain-words description of a reference code, for the launcher prompt. Pure function of the
    code string (no SSOT lookup) so the generated prompt is deterministic. Two-part bank codes
    (mis.3, vis.t1, met.<slug>) fall back to the bare code."""
    m = _CODE_RE.match(code)
    if not m:
        return f"reference {code}"
    scope, lesson, item = m.groups()
    clause = f" in Lesson {scope}.{lesson}"
    mw = re.match(r"^(?:w|ex)(\d+)([a-z]?)$", item)
    if mw:
        return f"worked example {mw.group(1)}" + (f", part {mw.group(2)}" if mw.group(2) else "") + clause
    mp = re.match(r"^(\d+)([a-z]?)$", item)
    if mp:
        return f"practice problem {mp.group(1)}" + (f", part {mp.group(2)}" if mp.group(2) else "") + clause
    if re.match(r"^d\d+$", item):
        return "a key term" + clause
    if re.match(r"^c\d+$", item):
        return "a check-for-understanding question" + clause
    if re.match(r"^f\d+[a-z]?$", item):
        return "the figure" + clause
    if re.match(r"^h\d+$", item):
        return "a how-to" + clause
    return f"reference {code}" + clause


def _prompt_for(code):
    """The ready-to-paste tutor-launch prompt for a reference code."""
    return (f"Use the Algebra 1 tutor skill to help me with {_label_for(code)} "
            f"(reference {code}). Pull it up, then ask whether I'd like you to explain it, "
            f"work through it together, or answer a specific question.")


def _ssot():
    sys.path.insert(0, HERE)
    import generate
    return generate.load_ssot()


def _md_path(uid):
    """Prefer the student-facing textbook source (textbook-src/); fall back to the tutor lesson
    source for any unit not yet rewritten, so the site always builds completely. The SSOT-verified
    math is kept identical between the two by check_textbook_src.py."""
    if uid == "A":
        cand = os.path.join(TEXTBOOK_SRC, "appendix-statistics.md")
        return cand if os.path.exists(cand) else os.path.join(UNIT_MD, "appendix-statistics.md")
    hits = glob.glob(os.path.join(TEXTBOOK_SRC, f"unit-{int(uid):02d}-*.md"))
    return hits[0] if hits else glob.glob(os.path.join(UNIT_MD, f"unit-{int(uid):02d}-*.md"))[0]


# --- preprocessing (operates on the raw markdown before conversion) ------------------------------
def _protect_math(text):
    blocks = []
    def repl(m):
        blocks.append(m.group(0))
        return f"\x00M{len(blocks)-1}\x00"
    return re.sub(r"\$\$.*?\$\$", repl, text, flags=re.DOTALL), blocks


def _restore_math(htmltext, blocks):
    for i, b in enumerate(blocks):
        # KaTeX auto-render reads textContent; HTML-escape so '<', '&' in LaTeX survive to the text node
        htmltext = htmltext.replace(f"\x00M{i}\x00", _html.escape(b, quote=False))
    return htmltext


# Typeset numeric set-literals like {3, 7, 9} as inline math. Runs on the math-protected text (so it
# never sees a $$ block's internals) and BEFORE the anchor/practice passes (so a set is an opaque
# sentinel by the time those parse). The wrapped \(\{...\}\) form is parked in the same `blocks` table
# _restore_math reads, so it survives markdown verbatim and KaTeX renders it inline. The source .md
# stays plain text (no inline-math tokens), so check_notation.py still passes. Only digit/separator
# braces match, so {#code} anchors (a '#') and prose braces containing letters are left alone.
_SET_RE = re.compile(r"(?<!\$)\{[\d\s.,()+−-]*\d[\d\s.,()+−-]*\}")   # (?<!\$) leaves currency ${..} alone
_CODESPAN_RE = re.compile(r"(```.*?```|`[^`\n]+`)", re.DOTALL)       # capture code spans/fences (kept literal)


def _protect_sets(text, blocks):
    def repl(m):
        inner = m.group(0)[1:-1].replace("−", "-")   # ASCII minus renders in KaTeX math mode
        blocks.append(r"\(\{" + inner + r"\}\)")
        return f"\x00M{len(blocks) - 1}\x00"
    # apply only outside code spans/fences, so a numeric set/dict literal in a code example stays literal
    parts = _CODESPAN_RE.split(text)
    for k in range(0, len(parts), 2):                # even segments are the non-code text (odd = code)
        parts[k] = _SET_RE.sub(repl, parts[k])
    return "".join(parts)


# A single-line $$ chain of steps joined by arrow connectors overflows a narrow column. Restack it as
# a left-aligned \begin{aligned} block (one step per row) so it wraps to the column on any screen.
# Only \begin{aligned}, row breaks and '&' marks are inserted — every math token is preserved
# verbatim, so values never change and the build stays byte-deterministic. Arrays, already-stacked
# (\\) and other \begin{} blocks are left untouched; short single-connector steps stay inline.
_CHAIN_CONN = {"xrightarrow", "longrightarrow", "Longrightarrow", "rightarrow",
               "Rightarrow", "implies", "mapsto", "to"}
_MACRO_RE = re.compile(r"\\[a-zA-Z]+|\\.", re.DOTALL)
_ROW_TAIL_RE = re.compile(r"(?:\\q?quad|\\[;,:!]|\\ |\s)+$")


def _stack_chain(block):
    if not (block.startswith("$$") and block.endswith("$$")):
        return block
    inner = block[2:-2]
    if "\n" in inner.strip() or "\\begin{" in inner or "\\\\" in inner or "&" in inner:
        return block   # arrays / already-stacked / blocks already using alignment cells: leave as-is
    breaks, depth, i, n, nconn = [], 0, 0, len(inner), 0
    while i < n:
        ch = inner[i]
        if ch == "\\":
            m = _MACRO_RE.match(inner, i)
            tok = m.group(0) if m else ch
            if depth == 0 and tok[1:] in _CHAIN_CONN:
                breaks.append(i); nconn += 1
            elif depth == 0 and tok == "\\text" and re.match(r"\{\s*Check", inner[i + 5:]):
                breaks.append(i)
            i += len(tok); continue
        if ch in "{[":           # track [] too, so a connector inside \xrightarrow[..]{..} isn't a break
            depth += 1
        elif ch in "}]":
            depth -= 1
        i += 1
    if not breaks or (nconn < 2 and not (nconn == 1 and len(inner.strip()) > 60)):
        return block
    cuts = [0] + breaks + [n]
    rows = [_ROW_TAIL_RE.sub("", inner[cuts[k]:cuts[k + 1]].strip()).strip()
            for k in range(len(cuts) - 1)]
    rows = [r for r in rows if r]
    # need >=2 rows AND every step row an equation, so a term-by-term sequence walk (4 -> 9 -> 14 ...,
    # no '=' on the step rows) stays inline rather than exploding into a tall ladder.
    if len(rows) < 2 or any("=" not in r for r in rows[1:]):
        return block
    return "$$\\begin{aligned}\n&" + " \\\\\n&".join(rows) + "\n\\end{aligned}$$"


def _id_worked_practice(text):
    """Insert {#code} markers after each Worked-example and Practice-problem number, lesson-aware,
    so they become deep-link targets like the explicit anchors. (In-memory only; not the source.)"""
    lines = text.split("\n")
    spans = [(i, m.group(1)) for i, ln in enumerate(lines)
             for m in [re.match(r"^## Lesson ([0-9A]+\.\d+):", ln)] if m]
    for li, (lstart, lid) in enumerate(spans):
        lend = spans[li + 1][0] if li + 1 < len(spans) else len(lines)
        block, wk, pk, infence = None, 0, 0, False
        for j in range(lstart, lend):
            ln = lines[j]
            if ln.lstrip().startswith("```"):
                infence = not infence; continue
            if infence:
                continue
            if ln.startswith("**Worked example"):
                block = "w"; continue
            if ln.startswith("**Practice problem"):
                block = "p"; continue
            if ln.startswith("**") or ln.startswith("## "):
                block = None; continue
            if block and re.match(r"^\d+\. ", ln):
                # code EVERY problem marker on the line, so several packed one-per-line (e.g.
                # "1. a  2. b  3. c") each get their own sequential code, not just the line-leading one.
                def _inject(m, _b=block, _l=lid):
                    nonlocal wk, pk
                    if _b == "w":
                        wk += 1; c = f"{_l}.w{wk}"
                    else:
                        pk += 1; c = f"{_l}.{pk}"
                    return f"{m.group(0)}{{#{c}}} "
                lines[j] = _PROB_MARK.sub(_inject, ln)
    return "\n".join(lines)


def _attr(s):
    """Escape a string for an HTML double-quoted attribute, keeping apostrophes literal so the
    prompt round-trips verbatim through python-markdown's raw-HTML passthrough (no entity that a
    later markdown pass could double-escape)."""
    return _html.escape(s, quote=False).replace('"', "&quot;")


def _refcode_badge(code, launcher):
    """The visible, linkable refcode badge. When launcher=True it also carries the tutor-launch
    prompt (data-prompt) + an aria-label so the textbook's refcode script can show and copy it."""
    base = f'<a class="refcode" id="{code}" href="#{code}"'
    if not launcher:
        return base + f">{code}</a>"
    return (base + f' data-prompt="{_attr(_prompt_for(code))}"'
            f' aria-label="{_attr("Copy a tutor prompt for " + _label_for(code))}">{code}</a>')


def _convert_anchors(text, launcher=False):
    """Turn {#code} into a visible, linkable refcode badge; embed the bundled SVG for f-codes.
    launcher=True (the HTML textbook) also attaches the tutor-launcher prompt to each badge."""
    out = []
    for ln in text.split("\n"):
        fcodes = [c for c in ANCHOR_RE.findall(ln)
                  if FCODE_RE.match(c) and os.path.exists(os.path.join(FIG_DIR, c + ".svg"))]
        ln = ANCHOR_RE.sub(lambda m: _refcode_badge(m.group(1), launcher), ln)
        out.append(ln)
        for c in fcodes:
            svg = open(os.path.join(FIG_DIR, c + ".svg"), encoding="utf-8").read().strip()
            out += ["", f'<figure class="fig" id="fig-{c}">{svg}<figcaption><b>Figure {c}</b></figcaption></figure>', ""]
    return "\n".join(out)


_ILLUS_RE = re.compile(r"<!--\s*illus:([a-z0-9-]+)\s*-->")

# Inline metaphor illustrations (textbook-only). The student source carries a `<!--illus:slug-->`
# marker at the metaphor sentence; the build swaps it for docs/assets/illus-<slug>.jpg with the
# descriptive alt below (the alt carries the meaning if the image fails to load). These are NOT part
# of the {#code} reference-code system, so the grammar / drift / figure lints never see them.
_ILLUS = {
    "1-1-mystery-box": "A balance scale with a covered box on one pan, picturing the equals sign as two sides held in balance.",
    "1-3-tiers": "A vertical checklist with four boxes ticked in order from top to bottom, picturing a fixed step-by-step order.",
    "1-4-counters": "A cut-away building with floors above the ground and floors below ground, picturing negative numbers as below zero.",
    "1-5-empty-chair": "The number 4 sitting in a chair, picturing evaluating an expression by putting the value 4 in for x.",
    "2-1-cup-coins": "A balance scale holding a cup and coins, with the same number of coins lifted from both pans.",
    "2-2-dressing": "Socks put on before shoes, picturing inverse steps undone in reverse order.",
    "2-3-boxes-coins": "Three identical boxes beside two loose coins that cannot be combined together.",
    "2-3-area-distribute": "A rectangle split into two cells, picturing a factor distributed across a sum.",
    "2-4-both-pans": "Identical boxes removed from both pans of a balance scale by the same amount.",
    "2-5-pizza-fractions": "A smaller one-sixth slice beside a larger one-quarter slice: more sharers means smaller pieces.",
    "2-6-clear-fractions": "A fraction circle with an arrow to a solid whole circle, picturing clearing the fractions to get a whole-number equation.",
    "3-1-unit-rate": "A speedometer beside a car at a steady speed, picturing a unit rate like miles in one hour.",
    "3-2-cross-multiply": "Two fractions linked by a crossing X, picturing cross-multiplication.",
    "3-3-percent-triangle": "A 10-by-10 grid of 100 small squares with 25 of them shaded, picturing a percent as a count per hundred.",
    "4-1-input-output": "One input entering a machine and a single output leaving it.",
    "4-1-vertical-line-test": "A vertical line sweeping across a curve, picturing the vertical-line test.",
    "4-2-trays": "A machine with an in-tray of allowed inputs and an out-tray of produced outputs.",
    "5-3-staircase": "A staircase of equal rise-over-run steps climbing alongside a line, picturing slope.",
    "6-1-phrase-equation": "A phrase card turning into an equation card, picturing translation into symbols.",
    "6-2-drt": "A small road trip, picturing distance as rate multiplied by time.",
    "7-2-substitution": "One quantity plugged in to replace another, picturing substitution.",
    "7-3-add-equations": "Two equations stacked and added so that one variable cancels out.",
    "7-4-parallel-identical": "Parallel lines that never meet beside one identical line: no solution versus infinitely many.",
    "9-1-steps-vs-doubling": "Evenly spaced steps beside doubling jumps, picturing arithmetic versus geometric growth.",
    "10-1-repeated-mult": "A power shown as several equal copies multiplied together.",
    "10-2-sliding-decimal": "A decimal point sliding across scales of size, picturing scientific notation.",
    "10-3-algebra-tiles": "Algebra tiles sorted into groups by kind, picturing combining like terms.",
    "10-4-area-grid": "An area-model grid of cells, picturing the product of two binomials.",
    "11-1-un-distribute": "An area model run backward, picturing pulling a common factor out.",
    "11-2-area-reversed": "An area grid filled in reverse to recover its two binomial sides.",
    "11-3-diff-squares": "Mirror-image squares, picturing the difference-of-squares pattern.",
    "12-1-area-to-side": "A square's area giving back its side length, picturing a square root as un-squaring.",
    "12-4-complete-square": "A partial square completed by adding a small corner piece.",
    "a-1-mean-balance": "A row of dots balancing on a single point, picturing the mean as a balance point.",
    "a-3-two-way-grid": "A clean two-by-two grid of cells, picturing a two-way table.",
    "howto-what-is-algebra": "A gentle path winding toward a warm sunrise, picturing algebra as an inviting, worthwhile beginning.",
    "howto-using-claude": "An open book with a friendly speech bubble beside it, picturing reading along with a helpful companion tutor.",
}


def _convert_illus(text):
    """Swap each `<!--illus:slug-->` marker for an inline illustration figure when the asset
    docs/assets/illus-<slug>.jpg exists (else drop the marker, keeping any other text on the line).
    Fence-aware. Block-level HTML with blank lines around it passes through markdown untouched."""
    out, infence = [], False
    for ln in text.split("\n"):
        if ln.lstrip().startswith("```"):
            infence = not infence; out.append(ln); continue
        m = None if infence else _ILLUS_RE.search(ln)
        if m and os.path.exists(os.path.join(ASSETS_DIR, f"illus-{m.group(1)}.jpg")):
            slug = m.group(1)
            alt = _html.escape(_ILLUS.get(slug, ""))
            out += ["", f'<figure class="illus"><img class="illus-art" src="../assets/illus-{slug}.jpg" '
                        f'alt="{alt}" loading="lazy"></figure>', ""]
        elif m:
            out.append(_ILLUS_RE.sub("", ln))
        else:
            out.append(ln)
    return "\n".join(out)


# --- viz: embed a candidate visual element from _verification/viz/<module>.py -------------------
_VIZ_DIR = os.path.join(HERE, "viz")
_VIZ_RE = re.compile(r"<!--\s*viz:([a-z0-9_]+)#(\d+)\s*-->")
_VIZ_CACHE = {}


def _viz_module(name):
    """Import a viz module by file path (cached). Returns the module, or None if missing/broken."""
    if name not in _VIZ_CACHE:
        fp = os.path.join(_VIZ_DIR, name + ".py")
        mod = None
        if os.path.exists(fp):
            try:
                spec = importlib.util.spec_from_file_location("viz_" + name, fp)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
            except Exception:
                mod = None
        _VIZ_CACHE[name] = mod
    return _VIZ_CACHE[name]


_VIZ_CODE_MAP = None


def _viz_code(module, index):
    """The SSOT figure code for a viz sample, from figures.VIZ_FIGURES (None if unregistered)."""
    global _VIZ_CODE_MAP
    if _VIZ_CODE_MAP is None:
        _VIZ_CODE_MAP = {}
        try:
            import viz_figures as _figmod
            for f in getattr(_figmod, "VIZ_FIGURES", []):
                _VIZ_CODE_MAP[(f["module"], int(f["index"]))] = f["code"]
        except Exception:
            pass
    return _VIZ_CODE_MAP.get((module, int(index)))


def _convert_viz(text):
    """Swap each `<!--viz:module#index-->` marker for that module's sample, wrapped in a figure.
    Fence-aware; a missing module/index drops the marker. The figure HTML is STASHED behind a
    sentinel and restored AFTER markdown (see md_to_body + _restore_viz): viz HTML contains $$ math
    and \\textcolor{#hex}{...} whose `{#hex}` would otherwise be eaten by the {#code} anchor pass and
    mangled by markdown. Returns (text_with_sentinels, blocks)."""
    blocks, out, infence = [], [], False
    for ln in text.split("\n"):
        if ln.lstrip().startswith("```"):
            infence = not infence; out.append(ln); continue
        m = None if infence else _VIZ_RE.search(ln)
        if m:
            mod = _viz_module(m.group(1))
            sample = None
            if mod is not None:
                try:
                    sample = mod.samples()[int(m.group(2))]
                except Exception:
                    sample = None
            if sample is not None:
                code = _viz_code(m.group(1), int(m.group(2)))
                cap = _html.escape(sample.get("caption", ""))
                figcap = (f'<b>Figure {code}</b> &mdash; {cap}' if code else cap)
                fid = f' id="fig-{code}"' if code else ""
                fig = (f'<figure class="fig viz"{fid}>{sample["html"]}'
                       f'<figcaption>{figcap}</figcaption></figure>')
                out += ["", f"\x00V{len(blocks)}\x00", ""]
                blocks.append(fig)
            else:
                out.append(_VIZ_RE.sub("", ln))
        else:
            out.append(ln)
    return "\n".join(out), blocks


def _restore_viz(htmltext, blocks):
    for i, b in enumerate(blocks):
        htmltext = htmltext.replace(f"<p>\x00V{i}\x00</p>", b).replace(f"\x00V{i}\x00", b)
    return htmltext


_LIST_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s")
_BQ_LIST_RE = re.compile(r"^>\s*(?:[-*+]|\d+\.)\s")


def _ensure_list_blank_lines(text):
    """python-markdown needs a blank line before a list. The unit sources glue lists directly under
    a label (e.g. '**New terms:**' then '- ...'), so insert a blank before the first item of each
    list group. Fence-aware (never edits inside ``` blocks); handles blockquote lists with a '>' line."""
    out, prev, infence = [], "", False
    for ln in text.split("\n"):
        if ln.lstrip().startswith("```"):
            infence = not infence
            out.append(ln); prev = ln; continue
        if not infence:
            if _BQ_LIST_RE.match(ln):
                if prev.startswith(">") and prev.strip() != ">" and not _BQ_LIST_RE.match(prev):
                    out.append(">")
            elif _LIST_RE.match(ln) and not ln.startswith(">"):
                if prev.strip() != "" and not _LIST_RE.match(prev):
                    out.append("")
        out.append(ln); prev = ln
    return "\n".join(out)


# --- component blockify: wrap each "**Label:**" lesson part in a semantic, scannable block -------
_LABELS = [
    (re.compile(r'^\*\*Goal:\*\*\s*(.*)$'), "goal", "What you'll learn"),
    (re.compile(r'^\*\*Why it matters:\*\*\s*(.*)$'), "why", ""),
    (re.compile(r'^\*\*New terms:\*\*\s*(.*)$'), "terms", "New words"),
    (re.compile(r'^\*\*Worked examples?:?\*\*\s*(.*)$'), "worked", "Worked example"),
    (re.compile(r'^\*\*Watch for:\*\*\s*(.*)$'), "watch", "A common mix-up"),
    (re.compile(r'^\*\*Check for understanding[^*]*:\*\*\s*(.*)$'), "check", "Check yourself"),
    (re.compile(r'^\*\*Practice problems?:\*\*\s*(.*)$'), "practice", "Practice"),
    (re.compile(r'^\*\*Answer key[^*]*:\*\*\s*(.*)$'), "answers", "Answers"),
    (re.compile(r'^\*\*Teaching arc[^*]*:\*\*\s*(.*)$'), "note", "How this builds"),
    (re.compile(r'^\*\*Visuals to offer:\*\*\s*(.*)$'), "note", "Figures to use"),
    (re.compile(r'^\*\*Consolidate:\*\*\s*(.*)$'), "wrap", "Putting it together"),
    (re.compile(r'^\*\*Mix back in[^*]*:\*\*\s*(.*)$'), "note", "Mix back in"),
    (re.compile(r'^\*\*Looking ahead:\*\*\s*(.*)$'), "note", "Looking ahead"),
    (re.compile(r'^\*\*Threading forward[^*]*:\*\*\s*(.*)$'), "note", "Looking ahead"),
    (re.compile(r'^\*\*Progress Card[^*]*:\*\*\s*(.*)$'), "note", "Progress card"),
]
_KIND_WRAP = {"goal": ("div", "cl-goal"), "why": ("div", "cl-why"), "terms": ("div", "cl-terms"),
              "worked": ("section", "worked"), "watch": ("div", "cl-watch"), "check": ("div", "cl-check"),
              "practice": ("section", "practice"), "wrap": ("div", "cl-wrap"), "note": ("div", "cl-note")}
_STOP_RE = re.compile(r'^(#{1,6}\s|-{3,}\s*$|\*{3,}\s*$)')


def _svg(inner):
    return ('<svg class="cl-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + inner + '</svg>')


# small line-icon glyph per callout kind (currentColor -> inherits the eyebrow colour, theme-aware)
_ICONS = {
    "goal": _svg('<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r="1" fill="currentColor" stroke="none"/>'),
    "terms": _svg('<path d="M12 6.5C9.5 5 6 5 3.5 6.5V18C6 16.5 9.5 16.5 12 18C14.5 16.5 18 16.5 20.5 18V6.5C18 5 14.5 5 12 6.5Z"/><path d="M12 6.5V18"/>'),
    "watch": _svg('<path d="M6 9H17"/><path d="M14.5 6.5 17 9 14.5 11.5"/><path d="M18 15H7"/><path d="M9.5 12.5 7 15 9.5 17.5"/>'),
    "worked": _svg('<path d="M5 19.5V15L15.5 4.5 19.5 8.5 9 19Z"/><path d="M13.5 6.5 17.5 10.5"/>'),
    "practice": _svg('<rect x="4" y="4.5" width="15.5" height="15.5" rx="2.5"/><path d="M7.5 10 9 11.5 12 8.5"/><path d="M14 10H16.5"/><path d="M7.5 15H16.5"/>'),
    "check": _svg('<circle cx="12" cy="12" r="8.5"/><path d="M9.6 9.6a2.6 2.6 0 1 1 3.3 2.5c-.9.3-1.4.9-1.4 1.8"/><circle cx="11.5" cy="16.6" r=".9" fill="currentColor" stroke="none"/>'),
    "note": _svg('<circle cx="12" cy="12" r="8.5"/><path d="M12 11V16"/><circle cx="12" cy="8" r=".9" fill="currentColor" stroke="none"/>'),
    "wrap": _svg('<path d="M12 3.5 3.5 8 12 12.5 20.5 8Z"/><path d="M5.5 11.5 12 15 18.5 11.5"/>'),
}


def _match_label(line):
    for pat, kind, eyebrow in _LABELS:
        m = pat.match(line)
        if m:
            return kind, eyebrow, m.group(1)
    return None


def _blockify(text):
    """Wrap each labelled lesson part in a semantic block so the page reads as scannable cards,
    not a wall of text. Fence-aware; math is already protected to sentinels upstream. Inner
    markdown is processed by the md_in_html extension (markdown="1")."""
    lines = text.split("\n")
    out, i, n, infence = [], 0, len(lines), False
    while i < n:
        ln = lines[i]
        if ln.lstrip().startswith("```"):
            infence = not infence; out.append(ln); i += 1; continue
        if infence:
            out.append(ln); i += 1; continue
        lab = _match_label(ln)
        if not lab:
            out.append(ln); i += 1; continue
        kind, eyebrow, remainder = lab
        body, j, f2 = ([remainder] if remainder.strip() else []), i + 1, False
        while j < n:
            l2 = lines[j]
            if l2.lstrip().startswith("```"):
                f2 = not f2; body.append(l2); j += 1; continue
            if not f2 and (_match_label(l2) or _STOP_RE.match(l2)):
                break
            body.append(l2); j += 1
        while body and body[-1].strip() == "":
            body.pop()
        inner = "\n".join(body).strip("\n")
        if kind == "answers":
            wrapped = ('<details class="answers" markdown="1">\n'
                       '<summary><span class="tw"></span><span class="eyebrow">Answers</span>'
                       '<span class="hint">Try each one yourself first, then open to check.</span></summary>\n'
                       f'<div class="ak-body" markdown="1">\n\n{inner}\n\n</div>\n</details>')
        else:
            tag, cls = _KIND_WRAP[kind]
            eb = f'<span class="eyebrow">{_ICONS.get(kind, "")}{eyebrow}</span>\n\n' if eyebrow else ""
            wrapped = f'<{tag} class="{cls}" markdown="1">\n\n{eb}{inner}\n\n</{tag}>'
        out += ["", wrapped, ""]
        i = j
    return "\n".join(out)


_SUBHEAD_RE = re.compile(r'^\*[^*][^\n]*:\*\s*$')


def _space_subheads(text):
    """Detach an italic group sub-heading (e.g. *Plot & locate:*) from a preceding list item with a
    blank line, so it renders as its own group head instead of being glued into the last problem
    (the 'swallowed subheading' bug). Fence-aware."""
    out, infence = [], False
    for ln in text.split("\n"):
        if ln.lstrip().startswith("```"):
            infence = not infence; out.append(ln); continue
        if not infence and _SUBHEAD_RE.match(ln.strip()) and out and out[-1].strip() != "":
            out.append("")
        out.append(ln)
    return "\n".join(out)


_DIVIDER = ('<div class="ldiv" aria-hidden="true"><i></i>'
            '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.6">'
            '<path d="M12 3.5 20.5 12 12 20.5 3.5 12Z"/></svg><i></i></div>')


# --- per-question answer reveal: pair each practice problem with its own revealable answer -------
# Marker disambiguation (calibrated to the unit sources, which vary widely):
#  * Problems are authored one-per-line or packed with a 2-space gap, never split by a single space
#    mid-prose -> a problem marker must sit at a STRONG boundary (start | newline | 2+ spaces). This
#    stops a number that merely ends a sentence ("... sum to 47.") from being read as problem 47.
#  * Answer keys vary (packed single-space in unit-01, 2-space in unit-02/11, one-per-line in
#    unit-07, ' · '-separated in unit-12) and values legitimately contain ')'/'.'/'·' (ordered pairs
#    '(9, 3)', factorisations '5(x+3)', 'is 4)'). So answers are parsed by (a) detecting the key's
#    own marker delimiter ('.' vs ')') and searching only for that, (b) anchoring to each expected
#    problem number in turn, and (c) validating that no extracted value is a swallowed next-marker.
_PSUB_RE = re.compile(r'^\*[^*].*?\*$')                          # a whole-line *italic sub-head*
_PROB_MARK = re.compile(r'(?:^|(?<=\n)|(?<=\s\s))(\d+)\.\s')     # problem marker at a strong boundary
_BLOCK_WRAP = re.compile(r'^<(p|ol|ul|li)>\s*(.*?)\s*</\1>$', re.DOTALL)


def _md_inline(s):
    """Render a short markdown fragment (a practice problem or an answer) to inline HTML. Core
    markdown only (no toc/md_in_html) for deterministic, dependency-light output. Strip any single
    wrapping block element — <p>, or a stray one-item <ol>/<ul>/<li> markdown emits when a fragment
    happens to start with an enumerator — so the result is always phrasing content safe to drop into
    a <span>. Inline raw HTML (refcode badges) and math sentinels pass through unchanged."""
    h = mdlib.markdown(s.strip(), output_format="html5").strip()
    m = _BLOCK_WRAP.match(h)
    while m:
        h = m.group(2).strip()
        m = _BLOCK_WRAP.match(h)
    return h.replace(' markdown="1"', '')


def _flatten(text):
    """Block body -> one string with line structure kept as '\\n' (so a line-start marker stays
    detectable) and each line trimmed."""
    return "\n".join(ln.strip() for ln in text.splitlines()).strip()


def _split_practice_block(body):
    """-> ordered list of ('sub', text) and ('prob', int, text), problems in document order (the
    caller verifies they are strictly increasing). Problems may be packed several per line or run
    one-per-line; sub-heads sit on their own italic lines. _PROB_MARK only fires at a strong boundary
    so a number ending a sentence in problem prose is not mistaken for a marker."""
    segments, buf = [], []
    for raw in body.splitlines():
        st = raw.strip()
        if not st:
            continue
        if _PSUB_RE.match(st):
            if buf:
                segments.append(("content", "\n".join(buf))); buf = []
            segments.append(("sub", st.strip("*").strip()))
        else:
            buf.append(st)
    if buf:
        segments.append(("content", "\n".join(buf)))

    items = []
    for kind, text in segments:
        if kind == "sub":
            items.append(("sub", text)); continue
        marks = [(m.start(), m.end(), int(m.group(1))) for m in _PROB_MARK.finditer(text)]
        head = text[:marks[0][0]] if marks else text
        if head.strip():
            # content before the first problem (a shared $$ table/array, a figure, lead-in prose):
            # per-problem rows can't carry it, so flag it — the caller falls back to keep it visible
            items.append(("pre", head.strip()))
        for i, (_st, en, num) in enumerate(marks):
            stop = marks[i + 1][0] if i + 1 < len(marks) else len(text)
            items.append(("prob", num, text[en:stop].strip()))
    return items


def _render_practice(items, instr=""):
    """Render converted practice items (each 'prob' carrying its paired answer) to raw HTML. Inner
    problem/answer markdown is rendered up front via _md_inline (no md_in_html nesting). `instr` is
    the header's instructional remainder (e.g. '(solve by graphing …)'), kept as an intro line."""
    out = ['<section class="practice">',
           f'<span class="eyebrow">{_ICONS.get("practice", "")}Practice</span>']
    if instr:
        out.append(f'<p class="practice-intro">{_md_inline(instr)}</p>')
    for it in items:
        if it[0] == "sub":
            out.append(f'<p class="practice-sub">{_md_inline(it[1])}</p>')
        else:
            _, num, ptext, ans = it
            prob_html = _md_inline(ptext)
            # the reference-code badge already carries the number, so drop the plain "N." where a badge
            # is present; keep it only for rows that have no badge (so every problem keeps an identifier).
            lead = "" if 'class="refcode"' in prob_html else f'<span class="pnum">{num}.</span> '
            out.append(
                f'<div class="prow">'
                f'<span class="prob">{lead}{prob_html}</span>'
                f'<details class="qcheck"><summary>'
                f'<span class="qc-show">Reveal answer</span><span class="qc-hide">Hide</span>'
                f'<span class="vh"> to problem {num}</span></summary>'
                f'<span class="qa">{_md_inline(ans)}</span></details></div>')
    out.append("</section>")
    return "\n".join(out)


_PRAC_HDR = re.compile(r'^\*\*Practice problems?\b')   # broader than _blockify's colon-only label:
_ANS_HDR = re.compile(r'^\*\*Answer key\b')             # also matches '… (instruction):**' / '… **(note)'


def _hdr_kind(line):
    """Broad practice/answer header detection for pairing (independent of _blockify's strict
    _LABELS, which requires a colon *inside* the bold). Returns 'practice' | 'answers' | None."""
    if _PRAC_HDR.match(line):
        return "practice"
    if _ANS_HDR.match(line):
        return "answers"
    return None


def _practice_instr(header_line):
    """The instructional remainder of a practice header, e.g. '**Practice problems** (solve by
    graphing …):' -> '(solve by graphing …)'. Empty for a plain '**Practice problems:**'. Removes
    only the leading '**Practice problems**' wrapper and surrounding separator punctuation, so inline
    markdown inside the instruction (e.g. 'label **all** types') is preserved for _md_inline."""
    m = re.match(r'^\*\*Practice problems?[^*]*\*\*\s*(.*)$', header_line)
    t = (m.group(1) if m else "").strip()
    t = re.sub(r'^[\s.:•·–—-]+', '', t)        # drop leading separator punctuation ('**…**. Use …')
    t = re.sub(r'[\s:]+$', '', t)              # and a trailing colon ('(solve …):' -> '(solve …)')
    return re.sub(r'\s+', ' ', t).strip()


def _scan_pa_blocks(lines):
    """Yield (kind, start, end, instr, inner_text) for every Practice/Answer-key block. Fence-aware.
    A practice block runs until the next header/label/heading-or-divider stop. An ANSWER block is
    bounded to its contiguous enumeration — it stops at the first blank line after content — so a
    trailing note, a following teaching section, or a second practice set is NOT swallowed into the
    last answer. For practice, `inner_text` is the following problem lines (the header's instructional
    remainder is returned separately as `instr`); for answers it includes any text after the bold."""
    i, n, infence = 0, len(lines), False
    while i < n:
        ln = lines[i]
        if ln.lstrip().startswith("```"):
            infence = not infence; i += 1; continue
        if infence:
            i += 1; continue
        k = _hdr_kind(ln)
        if not k:
            i += 1; continue
        after = ln.split("**", 2)
        after = after[2] if len(after) > 2 else ""
        body = [after] if (k == "answers" and after.strip()) else []
        j, f2, started = i + 1, False, bool(body)
        while j < n:
            l2 = lines[j]
            if l2.lstrip().startswith("```"):
                f2 = not f2; body.append(l2); j += 1; continue
            if not f2:
                if _hdr_kind(l2) or _match_label(l2) or _STOP_RE.match(l2):
                    break
                if k == "answers" and l2.strip() == "":
                    if started:
                        break                       # blank after the enumeration ends the key
                    j += 1; continue                # skip blank(s) before it starts
                if l2.strip():
                    started = True
            body.append(l2); j += 1
        yield k, i, j, (_practice_instr(ln) if k == "practice" else ""), "\n".join(body).strip("\n")
        i = j


def _normalize_key(key_text):
    """Flatten an answer-key block, drop a leading italic '*(note)*', and detect its marker delimiter.
    -> (flattened_string, delim) with delim '.' or ')' (or None if the block has no marker)."""
    s = re.sub(r'^\*\([^)]*\)\*\s*', '', _flatten(key_text))
    m = re.search(r'(?:^|(?<=\s))\d+([).])\s', s)
    return s, (m.group(1) if m else None)


def _answers_for(key_text, nums):
    """Extract answers for the ordered problem numbers `nums`. Using the key's own marker delimiter
    and searching for each expected number's '<n><delim> ' in sequence (token-start) makes it immune
    to the OTHER delimiter inside a value (e.g. 'is 4)' / '(9, 3)' in a '.'-keyed list) and to ')'/'.'
    inside parenthesised values. Strips a trailing ' · ' item separator. Returns {n: answer}, or None
    if a marker is missing OR a value is empty or is itself a swallowed next-marker (-> fallback)."""
    s, delim = _normalize_key(key_text)
    if not delim:
        return None
    d = re.escape(delim)
    spans, pos = [], 0
    for nidx in nums:
        m = re.compile(r'(?:^|(?<=\s))%d%s\s' % (nidx, d)).search(s, pos)
        if not m:
            return None
        spans.append((nidx, m.start(), m.end())); pos = m.end()
    out = {}
    for i, (nidx, _st, en) in enumerate(spans):
        stop = spans[i + 1][1] if i + 1 < len(spans) else len(s)
        val = re.sub(r'\s*·\s*$', '', s[en:stop].strip()).rstrip(",;").strip()
        if not val or re.match(r'\d+[).]\s', val):       # empty, or a swallowed next-marker -> bail
            return None
        out[nidx] = val
    return out


def _key_numbers(key_text, universe):
    """Which of `universe` (the lesson's actual problem numbers) this answer block has markers for,
    using the key's own delimiter. Used only to decide whether a key is fully consumed and can be
    dropped; restricting to real problem numbers keeps a residual key (answers to non-practice
    prompts) from being dropped."""
    s, delim = _normalize_key(key_text)
    if not delim:
        return set()
    d = re.escape(delim)
    return {nidx for nidx in universe if re.search(r'(?:^|(?<=\s))%d%s\s' % (nidx, d), s)}


def _pair_practice_answers(text):
    """Convert each pairable Practice+Answer-key set in a lesson chunk to per-problem reveals and
    delete the consumed answer key(s). A set converts only if its problems parse to >=2 strictly
    increasing numbers AND every one has a matching answer (anchored parse); otherwise it is left
    untouched for _blockify (graceful fallback). Each set draws answers from the key block(s) that
    follow it (before the next set)."""
    lines = text.split("\n")
    blocks = list(_scan_pa_blocks(lines))
    practices = sorted(([s, e, instr, _split_practice_block(inner)]
                        for k, s, e, instr, inner in blocks if k == "practice"), key=lambda p: p[0])
    answers = [(s, e, inner) for k, s, e, _instr, inner in blocks if k == "answers"]
    if not practices or not answers:
        return text
    pstarts = [p[0] for p in practices]

    edits, used = [], set()
    for idx, (ps, pe, instr, items) in enumerate(practices):
        nums = [it[1] for it in items if it[0] == "prob"]
        if (len(nums) < 2 or len(set(nums)) != len(nums) or nums != sorted(nums)
                or any(it[0] == "pre" for it in items)):
            continue           # need >=2 strictly-increasing problems and no shared preamble/table
        nxt = pstarts[idx + 1] if idx + 1 < len(pstarts) else len(lines) + 1
        # Accumulate the following key block(s) only until this set's numbers are covered, then stop.
        # This both (a) skips a later key for OTHER problems (a 13-18 set after a 1-12 set) and
        # (b) avoids appending a second strand's re-numbered 1-3 key onto the last answer of a 1-8 set.
        want, parts, covered, cand = set(nums), [], set(), []
        for as_, ae, inner in answers:
            if not (ps < as_ < nxt) or want <= covered:
                continue
            parts.append(inner); covered |= _key_numbers(inner, want); cand.append((as_, ae))
        amap = _answers_for("\n".join(parts), nums)
        if amap is None:
            continue
        paired = [it if it[0] == "sub" else ("prob", it[1], it[2], amap[it[1]]) for it in items]
        edits.append((ps, pe, ["", _render_practice(paired, instr), ""]))
        used.update(cand)                              # only drop keys actually used by a conversion

    if not edits:
        return text
    for as_, ae, inner in answers:
        if (as_, ae) in used:                          # a residual/strand key (unused) keeps its box
            edits.append((as_, ae, None))

    edits.sort(key=lambda t: t[0])
    out, prev = [], 0
    for s, e, repl in edits:
        out.extend(lines[prev:s])
        if repl:
            out.extend(repl)
        prev = e
    out.extend(lines[prev:])
    return "\n".join(out)


def md_to_body(text, launcher=False):
    text, math = _protect_math(text)
    math = [_stack_chain(b) for b in math]   # stack long solve-chains so they wrap (no h-scroll)
    text = _protect_sets(text, math)         # typeset numeric set-literals {..} as inline math
    text = _convert_illus(text)
    text, vizblocks = _convert_viz(text)
    text = _id_worked_practice(text)
    text = _convert_anchors(text, launcher)
    text = _pair_practice_answers(text)
    text = _space_subheads(text)
    text = _blockify(text)
    text = _ensure_list_blank_lines(text)
    body = mdlib.markdown(text, extensions=["extra", "sane_lists", "toc", "md_in_html"], output_format="html5")
    # md_in_html strips the internal markdown="1" directive on some Python/lib versions but leaves it on
    # others (e.g. CPython 3.11.9 vs 3.11.15) — remove any residue so the output is byte-identical everywhere.
    body = body.replace(' markdown="1"', '')
    body = body.replace("<hr />", _DIVIDER).replace("<hr>", _DIVIDER)  # decorative lesson dividers
    body = body.replace(chr(92) + "$", "$")  # python-markdown leaves \$ literal; show currency as $ (math $$ stays protected)
    body = _restore_viz(body, vizblocks)
    return _restore_math(body, math)


# --- page model: one page per lesson, with a unit overview + a persistent sidebar ----------------
_LESSON_HDR = re.compile(r"(?m)^## Lesson ([0-9A]+\.\d+):[ \t]*(.*)$")


def _overview_fname(uid):
    return "appendix.html" if str(uid) == "A" else f"unit-{int(uid):02d}.html"


def _lesson_fname(lesson_id):
    scope, sub = lesson_id.split(".")
    return f"appendix-{sub}.html" if scope == "A" else f"unit-{int(scope):02d}-{sub}.html"


def _ssot_model(ssot):
    """Sidebar model (unit + lesson tree) straight from the SSOT — no unit .md reading needed. The
    guides feed this to _sidebar (with a prefix) to render the textbook's exact left rail, pointed
    into ../textbook/."""
    return [{"id": str(u.id), "title": u.title, "overview": _overview_fname(u.id),
             "lessons": [{"id": l.id, "title": l.title, "fname": _lesson_fname(l.id)} for l in u.lessons]}
            for u in ssot.units]


def _lesson_hero(lesson_id):
    """A per-lesson hero illustration lives at docs/assets/hero-<id>.jpg (lesson dots -> dashes).
    Auto-wired when the asset exists, so a lesson without one simply renders no hero art (and the
    build stays deterministic on the committed asset set)."""
    name = "hero-" + lesson_id.replace(".", "-")
    return f"../assets/{name}.jpg" if os.path.exists(os.path.join(ASSETS_DIR, name + ".jpg")) else None


def _split_unit(md):
    """Split a unit's markdown into the intro (everything before the first lesson) and a list of
    (lesson_id, lesson_title, chunk). Each chunk keeps its '## Lesson' header so the deep-link code
    pass still scopes it, but drops the trailing '---' inter-lesson divider (so no stray rule)."""
    hdrs = list(_LESSON_HDR.finditer(md))
    intro = re.sub(r"\n+-{3,}[ \t]*$", "\n", (md[:hdrs[0].start()] if hdrs else md).rstrip()).rstrip()
    lessons = []
    for i, m in enumerate(hdrs):
        end = hdrs[i + 1].start() if i + 1 < len(hdrs) else len(md)
        chunk = re.sub(r"\n+-{3,}[ \t]*$", "\n", md[m.start():end].rstrip()).rstrip()
        lessons.append((m.group(1), m.group(2).strip(), chunk))
    return intro, lessons


def _strip_lead(html, tag):
    return re.sub(rf"^\s*<{tag}[^>]*>.*?</{tag}>", "", html, count=1, flags=re.DOTALL)


def _sidebar(model, cur, *, prefix="", top_links=None):
    """The persistent left index: How-to-use / All-units, then every unit (current expanded).
    `prefix` is prepended to every href so a guide can point the same rail into ../textbook/;
    `top_links` (a list of (href, label) pairs) overrides the two default top entries."""
    if top_links is None:
        top_links = [("how-to-use.html", "How to use this book"), ("index.html", "All units")]
    out = ['<nav class="snav" aria-label="Contents">']
    for href, label in top_links:
        out.append(f'<a class="snav-top{" cur" if cur == href else ""}" href="{prefix}{href}">{label}</a>')
    out.append('<ol class="snav-units">')
    for unit in model:
        active = cur == unit["overview"] or any(cur == l["fname"] for l in unit["lessons"])
        ucur = " cur" if cur == unit["overview"] else ""
        label = "Appendix" if unit["id"] == "A" else f"Unit {unit['id']}"
        out.append(f'<li class="{"active" if active else ""}">')
        out.append(f'<a class="snav-unit{ucur}" href="{prefix}{unit["overview"]}">{label}. {_html.escape(unit["title"])}</a>')
        if unit["lessons"]:
            out.append('<ol class="snav-lessons">')
            for l in unit["lessons"]:
                lc = " cur" if cur == l["fname"] else ""
                out.append(f'<li><a class="snav-lesson{lc}" href="{prefix}{l["fname"]}">'
                           f'<span class="ln">{_html.escape(l["id"])}</span> {_html.escape(l["title"])}</a></li>')
            out.append('</ol>')
        out.append('</li>')
    out.append('</ol></nav>')
    return "\n".join(out)


def _pagenav(prev_link, next_link):
    if not prev_link and not next_link:
        return ""
    parts = ['<nav class="pagenav" aria-label="Previous and next page">']
    if prev_link:
        parts.append(f'<a class="pn-prev" href="{prev_link[0]}"><span class="pn-dir">&larr;&nbsp;Back</span>'
                     f'<span class="pn-title">{_html.escape(prev_link[1])}</span></a>')
    else:
        parts.append('<span></span>')
    if next_link:
        parts.append(f'<a class="pn-next" href="{next_link[0]}"><span class="pn-dir">Next&nbsp;&rarr;</span>'
                     f'<span class="pn-title">{_html.escape(next_link[1])}</span></a>')
    parts.append('</nav>')
    return "\n".join(parts)


# delegated controller for the reference-code tutor launcher (textbook pages only). Vanilla JS,
# no deps; event-delegated so it covers every .refcode badge; a position:fixed tooltip escapes the
# overflow:hidden on .worked/.answers cards. Plain string (not f-string) so its braces stay literal.
_REFCODE_JS = """
(function () {
  var tip = document.getElementById("rc-tip"), toast = document.getElementById("rc-toast");
  if (!tip || !toast) return;
  var toastT = 0, active = null;
  function hideTip() {
    tip.classList.remove("show"); tip.setAttribute("aria-hidden", "true");
    if (active) { active.removeAttribute("aria-describedby"); active = null; }
  }
  function showTip(a) {
    var p = a.getAttribute("data-prompt"); if (!p) return;
    tip.textContent = "";
    var h = document.createElement("span"); h.className = "rc-tip-h";
    h.textContent = "Tutor prompt (click the code to copy):";
    var q = document.createElement("span"); q.className = "rc-tip-q"; q.textContent = p;
    tip.appendChild(h); tip.appendChild(q);
    tip.setAttribute("aria-hidden", "false"); tip.classList.add("show");
    if (active && active !== a) active.removeAttribute("aria-describedby");
    active = a; a.setAttribute("aria-describedby", "rc-tip");  // expose the prompt text to screen readers
    var r = a.getBoundingClientRect(), t = tip.getBoundingClientRect();
    var top = r.top - t.height - 8;
    if (top < 8) {                                  // no room above: place below, then clamp to the viewport
      top = r.bottom + 8;
      if (top + t.height > window.innerHeight - 8) top = Math.max(8, window.innerHeight - t.height - 8);
    }
    var left = Math.max(8, Math.min(r.left + r.width / 2 - t.width / 2, window.innerWidth - t.width - 8));
    tip.style.top = top + "px"; tip.style.left = left + "px";
  }
  function showToast(msg) {
    toast.textContent = msg; toast.classList.add("show"); toast.setAttribute("aria-hidden", "false");
    if (toastT) clearTimeout(toastT);
    toastT = setTimeout(function () {
      toast.classList.remove("show"); toast.setAttribute("aria-hidden", "true");
    }, 2600);
  }
  function fallbackCopy(text, ok) {
    try {
      var ta = document.createElement("textarea"); ta.value = text;
      ta.style.position = "fixed"; ta.style.top = "-1000px"; ta.style.opacity = "0";
      document.body.appendChild(ta); ta.focus(); ta.select();
      var done = document.execCommand("copy"); document.body.removeChild(ta);
      if (done) { ok(); } else { showToast("Select the prompt above and copy it."); }
    } catch (e) { showToast("Select the prompt above and copy it."); }
  }
  function copyText(text, ok) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(ok, function () { fallbackCopy(text, ok); });
    } else { fallbackCopy(text, ok); }
  }
  document.addEventListener("pointerover", function (e) {
    var a = e.target.closest && e.target.closest(".refcode"); if (a) showTip(a);
  });
  document.addEventListener("pointerout", function (e) {
    var a = e.target.closest && e.target.closest(".refcode");
    if (a && !a.contains(e.relatedTarget)) hideTip();
  });
  document.addEventListener("focusin", function (e) {
    var a = e.target.closest && e.target.closest(".refcode"); if (a) showTip(a);
  });
  document.addEventListener("focusout", function (e) {
    if (e.target.closest && e.target.closest(".refcode")) hideTip();
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") hideTip(); });
  window.addEventListener("scroll", hideTip, true);
  window.addEventListener("resize", hideTip);
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest(".refcode"); if (!a) return;
    e.preventDefault();
    copyText(a.getAttribute("data-prompt") || a.textContent, function () {
      showToast("Copied. Paste it into Claude to start.");
    });
  });
})();
"""


# --- HTML template ------------------------------------------------------------------------------
def _lesson_page(title, body, model, cur, prev_link=None, next_link=None, *, subtitle="",
                 surface="textbook", hero=None, kicker="", home_href="index.html",
                 home_label="Algebra&nbsp;1", sidebar_prefix="", sidebar_top=None, brand_prefix="../"):
    kick = f'<div class="kicker">{_html.escape(kicker)}</div>' if kicker else ""
    if hero:
        lede = f'<p class="lede">{_html.escape(subtitle)}</p>' if subtitle else ""
        head_block = (f'<div class="hero"><div class="hero-text">{kick}'
                      f'<h1>{_html.escape(title)}</h1>{lede}</div>'
                      f'<img class="hero-art" src="{hero}" alt=""></div>')
    else:
        sub = f'<p class="subtitle">{_html.escape(subtitle)}</p>' if subtitle else ""
        head_block = f'{kick}<h1>{_html.escape(title)}</h1>\n{sub}'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{_html.escape(title)} — Algebra 1</title>
<script>try{{if(localStorage.getItem("a1-theme")==="dark")document.documentElement.classList.add("dark");}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..40,500..600&family=Source+Serif+4:ital,wght@0,400;0,600;1,400&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="textbook.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@{KATEX}/dist/katex.min.css" crossorigin="anonymous">
</head>
<body data-surface="{surface}">
<header class="topbar">
  <button id="menu" class="menu" type="button" aria-label="Open or close the contents menu" aria-expanded="false">☰&nbsp;Contents</button>
  <a class="home" href="{home_href}"><img class="brandmark" src="{brand_prefix}assets/logo.png" alt="" width="26" height="26" decoding="async">{home_label}</a>
  <span class="sp"></span>
  <button id="theme" type="button" aria-label="Toggle light or dark theme">◐&nbsp;Theme</button>
</header>
<div class="shell">
<aside class="sidenav" id="sidenav">
{_sidebar(model, cur, prefix=sidebar_prefix, top_links=sidebar_top)}
</aside>
<div class="content">
<main>
{head_block}
{body}
{_pagenav(prev_link, next_link)}
</main>
<footer><p>A friendly Algebra 1 textbook, made to be read alongside the Claude tutor. Math by KaTeX.</p></footer>
</div>
</div>
<div id="rc-tip" role="tooltip" aria-hidden="true"></div>
<div id="rc-toast" role="status" aria-live="polite" aria-hidden="true"></div>
<script defer src="https://cdn.jsdelivr.net/npm/katex@{KATEX}/dist/katex.min.js" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@{KATEX}/dist/contrib/auto-render.min.js" crossorigin="anonymous"></script>
<script>
document.addEventListener("DOMContentLoaded", function () {{
  renderMathInElement(document.body, {{delimiters: [{{left: "$$", right: "$$", display: true}}, {{left: "\\\\(", right: "\\\\)", display: false}}], throwOnError: false}});
  var root = document.documentElement, body = document.body;
  document.getElementById("theme").addEventListener("click", function () {{
    root.classList.toggle("dark");
    localStorage.setItem("a1-theme", root.classList.contains("dark") ? "dark" : "light");
  }});
  var menu = document.getElementById("menu");
  menu.addEventListener("click", function () {{
    var open = body.classList.toggle("nav-open");
    menu.setAttribute("aria-expanded", open ? "true" : "false");
  }});
  var sn = document.getElementById("sidenav");
  if (sn) sn.addEventListener("click", function (e) {{ if (e.target.closest("a")) body.classList.remove("nav-open"); }});
}});
</script>
<script>{_REFCODE_JS}</script>
</body>
</html>
"""


def _page(title, body, prev_link, next_link, subtitle="", *, surface="textbook", hero=None, kicker=""):
    """DEPRECATED, unused. The original single-column layout (topbar nav, no rail). The textbook,
    student guide, tutor guide, and landing now all render through _lesson_page (left index rail +
    hero); kept only for reference and safe to delete."""
    nav = ['<a class="home" href="index.html">Algebra&nbsp;1</a>']
    if prev_link:
        nav.append(f'<a href="{prev_link[0]}">&larr;&nbsp;{prev_link[1]}</a>')
    if next_link:
        nav.append(f'<a href="{next_link[0]}">{next_link[1]}&nbsp;&rarr;</a>')
    navhtml = " &nbsp;·&nbsp; ".join(nav)
    if hero:
        kick = f'<div class="kicker">{_html.escape(kicker)}</div>' if kicker else ""
        lede = f'<p class="lede">{_html.escape(subtitle)}</p>' if subtitle else ""
        head_block = (f'<div class="hero"><div class="hero-text">{kick}'
                      f'<h1>{_html.escape(title)}</h1>{lede}</div>'
                      f'<img class="hero-art" src="{hero}" alt=""></div>')
    else:
        sub = f'<p class="subtitle">{subtitle}</p>' if subtitle else ""
        head_block = f'<h1>{_html.escape(title)}</h1>\n{sub}'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{_html.escape(title)} — Algebra 1</title>
<script>try{{if(localStorage.getItem("a1-theme")==="dark")document.documentElement.classList.add("dark");}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..40,500..600&family=Source+Serif+4:ital,wght@0,400;0,600;1,400&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="textbook.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@{KATEX}/dist/katex.min.css" crossorigin="anonymous">
</head>
<body data-surface="{surface}">
<header class="topbar">
  <nav>{navhtml}</nav>
  <span class="sp"></span>
  <button id="theme" type="button" aria-label="Toggle light or dark theme">◐ Theme</button>
</header>
<main>
{head_block}
{body}
</main>
<footer><p>Generated from the unit source by <code>_verification/build_textbook.py</code>. Math by KaTeX.</p></footer>
<script defer src="https://cdn.jsdelivr.net/npm/katex@{KATEX}/dist/katex.min.js" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@{KATEX}/dist/contrib/auto-render.min.js" crossorigin="anonymous"></script>
<script>
document.addEventListener("DOMContentLoaded", function () {{
  renderMathInElement(document.body, {{delimiters: [{{left: "$$", right: "$$", display: true}}, {{left: "\\\\(", right: "\\\\)", display: false}}], throwOnError: false}});
  var t = document.getElementById("theme"), root = document.documentElement;
  t.addEventListener("click", function () {{
    root.classList.toggle("dark");
    localStorage.setItem("a1-theme", root.classList.contains("dark") ? "dark" : "light");
  }});
}});
</script>
</body>
</html>
"""


CSS = """/* ============================================================================
   Algebra 1 — visual design language (warm, friendly, calm; for a true beginner).
   One stylesheet shared by the textbook, student guide, tutor guide, and landing.
   Light is the default theme; a refined slate-ink dark is the alternate.
   ============================================================================ */
:root{
  --step--1:.86rem; --step-0:1rem; --step-1:1.18rem; --step-2:1.42rem; --step-3:1.7rem; --step-4:2.05rem; --step-5:2.45rem;
  --lh:1.68; --lh-tight:1.18;
  --measure:64ch; --wide:46rem; --rail:16rem;
  --serif-math:"STIX Two Text","Cambria Math";
  --radius:16px; --radius-sm:11px;
  --s2:.5rem; --s3:.8rem; --s4:1.15rem; --s5:1.9rem; --s6:2.8rem; --s7:4.2rem;
  /* LIGHT — warm cream (default) */
  --paper:#f8f4ea; --card:#fffdf6; --card-2:#fbf6ec;
  --ink:#2c2820; --ink-soft:#6c6457; --rule:#ece2d0;
  --blue:#2f74b0; --link:#1f6391; --violet:#7d5aa6; --rose:#bb5b4a; --leaf:#3f8f5e; --honey:#a9740f;
  --tint-blue:#eef3f7; --tint-honey:#f6efe0; --tint-rose:#f7ede9; --tint-leaf:#eef4ee;
  --shadow:0 1px 2px rgba(60,48,28,.05), 0 6px 22px -12px rgba(60,48,28,.18);
}
html.dark{
  /* DARK — refined slate ink */
  --paper:#191c20; --card:#22262c; --card-2:#1d2127;
  --ink:#e9e8e3; --ink-soft:#9aa1a9; --rule:#2e333a;
  --blue:#6fb0e8; --link:#8cc2ef; --violet:#c3a4e6; --rose:#ef9b8e; --leaf:#69cf97; --honey:#e0bd76;
  --tint-blue:#1d2530; --tint-honey:#272318; --tint-rose:#2a1f1c; --tint-leaf:#1c2722;
  --shadow:0 1px 2px rgba(0,0,0,.3), 0 10px 28px -16px rgba(0,0,0,.65);
}
/* per-surface paper tint (student guide cooler, tutor guide buff) */
body[data-surface="guide"]{--paper:#eef2f4; --card:#fdfefe; --card-2:#f5f9fb; --rule:#dde7ec; --tint-blue:#e9f1f6;}
body[data-surface="tutor"]{--paper:#f4efe3; --card:#fffdf6; --card-2:#faf4e7; --rule:#e7ddca;}
html.dark body[data-surface="guide"]{--paper:#141a20; --card:#1c232b; --card-2:#18202a;}
html.dark body[data-surface="tutor"]{--paper:#1b1a16; --card:#24221c; --card-2:#1f1d18;}

*{box-sizing:border-box}
html{font-size:112.5%; overflow-x:clip}   /* durable guard: a too-wide block can never scroll the page sideways */
body{margin:0; background:var(--paper); color:var(--ink);
  font:var(--step-0)/var(--lh) "Source Serif 4",var(--serif-math),Georgia,serif;
  -webkit-font-smoothing:antialiased; text-rendering:optimizeLegibility; text-wrap:pretty;}
h1,h2,h3{font-family:"Fraunces",var(--serif-math),Georgia,serif; font-weight:600; line-height:var(--lh-tight);
  font-optical-sizing:auto; text-wrap:balance; color:var(--ink);}
h1{font-size:var(--step-4); margin:.2rem 0 .5rem}
h2{font-size:var(--step-2); margin:var(--s7) 0 var(--s4); padding-top:var(--s5); border-top:1px solid var(--rule)}
h3{font-size:var(--step-1); margin:var(--s6) 0 var(--s3)}
p{margin:0 0 var(--s4)}
a{color:var(--link)} a:hover{text-decoration-thickness:2px}
strong,b{font-weight:600; color:var(--ink)}
.imath{font-family:var(--serif-math),"Source Serif 4",serif}
code{font:500 .9em "IBM Plex Mono",ui-monospace,Consolas,monospace; background:var(--card-2); padding:.06em .35em; border-radius:5px}
pre{background:var(--card-2); padding:.85rem 1rem; border-radius:var(--radius-sm); overflow:auto; border:1px solid var(--rule)}
pre code{background:none; padding:0}
hr{border:0; border-top:1px solid var(--rule); margin:var(--s6) 0}
.ldiv{display:flex; align-items:center; gap:1rem; margin:var(--s6) auto}
.ldiv i{height:1px; flex:1; background:var(--rule)}
.ldiv svg{color:var(--honey); opacity:.7; flex:none}
.eyebrow{font-weight:600; font-size:var(--step--1); letter-spacing:.01em; color:var(--ink-soft); display:flex; align-items:center; gap:.42rem; margin-bottom:.4rem}
.cl-ic{width:1.15em; height:1.15em; flex:none}

/* ---- top bar ---- */
.topbar{position:sticky; top:0; z-index:40; display:flex; align-items:center; gap:1rem;
  padding:.6rem 1.2rem; border-bottom:1px solid var(--rule);
  background:color-mix(in srgb,var(--paper) 88%,transparent); font-size:var(--step--1);}
@supports not (background:color-mix(in srgb,red,blue)){ .topbar{background:var(--paper)} }
.topbar nav{display:flex; gap:.9rem; flex-wrap:wrap; align-items:baseline}
.topbar a{color:var(--link); text-decoration:none} .topbar a:hover{text-decoration:underline}
.topbar .home{display:inline-flex; align-items:center; gap:.45rem; font-family:"Fraunces",serif; font-weight:600; font-size:var(--step-0); color:var(--ink)}
.topbar .home:hover{text-decoration:none}
.topbar .home .brandmark{width:1.55em; height:1.55em; flex:none; display:block}
.topbar .sp{margin-left:auto}
#theme,.menu{background:none; border:1px solid var(--rule); border-radius:999px; color:var(--ink-soft);
  cursor:pointer; padding:.3rem .7rem; font:inherit; font-size:var(--step--1)}
#theme:hover,.menu:hover{color:var(--ink); border-color:var(--blue)}
.menu{display:none}
@supports ((backdrop-filter:blur(1px)) or (-webkit-backdrop-filter:blur(1px))){
  .topbar{-webkit-backdrop-filter:blur(8px); backdrop-filter:blur(8px)} }

/* ---- app shell: left index rail + reading column ---- */
.shell{display:grid; grid-template-columns:var(--rail) minmax(0,1fr); align-items:start}
.content{min-width:0}
.sidenav{position:sticky; top:3.1rem; align-self:start; max-height:calc(100vh - 3.1rem); overflow:auto;
  padding:1.2rem .9rem 3rem; border-right:1px solid var(--rule); background:var(--paper); font-size:var(--step--1)}
.snav a{display:block; text-decoration:none; color:var(--ink-soft); border-radius:8px; padding:.3rem .55rem; line-height:1.35}
.snav a:hover{background:var(--card-2); color:var(--ink)}
.snav a.cur{color:var(--link); background:var(--tint-blue); font-weight:600}
.snav-top{font-weight:600; color:var(--ink)}
.snav-units{list-style:none; margin:.6rem 0 0; padding:0; counter-reset:none}
.snav-units > li{margin:.1rem 0}
.snav-unit{font-weight:600; color:var(--ink)}
.snav-lessons{list-style:none; margin:.05rem 0 .55rem; padding:0 0 0 .55rem; border-left:1px solid var(--rule); display:none}
.snav-units > li.active > .snav-lessons{display:block}
.snav-lesson .ln{font:600 .85em "IBM Plex Mono",monospace; color:var(--ink-soft); margin-right:.25rem}
.snav-lesson.cur .ln{color:var(--link)}

/* ---- reading column: calm centered measure; special blocks a touch wider ---- */
main{max-width:var(--wide); margin:0 auto; padding:1rem 1.3rem 4rem}
main > *{max-width:var(--measure); margin-inline:auto}
main > figure.fig, main > .worked, main > .practice, main > .answers, main > .hero,
main > table, main > .katex-display, main > .lesson-list, main > .pagenav, main > .tset, main > figure.viz{max-width:var(--wide)}
footer{max-width:var(--measure); margin:var(--s7) auto 0; padding:1.1rem 1.3rem; color:var(--ink-soft);
  font-size:var(--step--1); border-top:1px solid var(--rule)}

/* ---- unit hero + page kicker ---- */
.kicker{color:var(--blue); font-weight:600; font-size:var(--step--1); letter-spacing:.04em; margin:.6rem 0 .1rem}
.hero{margin:var(--s5) auto var(--s5); display:grid; grid-template-columns:1.05fr .95fr; gap:1.6rem; align-items:center}
.hero .kicker{margin:0}
.hero h1{margin:.3rem 0 .5rem}
.hero .lede{font-size:var(--step-1); color:var(--ink-soft); margin:0}
.hero-art{width:100%; height:auto; border-radius:var(--radius); box-shadow:var(--shadow); display:block; aspect-ratio:16/9; object-fit:cover}
html.dark .hero-art{filter:brightness(.9) saturate(.92)}
.subtitle{color:var(--ink-soft); font-size:var(--step-1); margin:.2rem auto var(--s5)}
@media (max-width:46rem){ .hero{grid-template-columns:1fr; gap:1rem} .hero-art{order:-1} }

/* ---- reference code: one quiet, friendly identifier ---- */
.refcode{font:500 .8em "IBM Plex Mono",ui-monospace,monospace; color:var(--ink-soft); text-decoration:none;
  background:var(--card-2); border:1px solid var(--rule); border-radius:999px; padding:.08em .55em; white-space:nowrap}
.refcode:hover,.refcode:focus-visible{color:var(--link); border-color:var(--blue)}
:target{scroll-margin-top:5rem}

/* ---- cross-material link (a guide pointing into the textbook, and back) ---- */
.xref{display:inline-flex; align-items:center; gap:.4rem; font-size:var(--step--1); font-weight:600;
  color:var(--link); text-decoration:none; background:var(--card-2); border:1px solid var(--rule);
  border-radius:999px; padding:.3rem .8rem}
.xref:hover,.xref:focus-visible{border-color:var(--blue); color:var(--link)}

/* ---- callout family (plain-language labels) ---- */
.cl-goal,.cl-terms,.cl-watch,.cl-note,.cl-check,.cl-wrap{background:var(--card); border-radius:var(--radius);
  padding:1.1rem 1.3rem; margin:var(--s6) auto; box-shadow:var(--shadow)}
.cl-goal{background:none; box-shadow:none; border-left:3px solid var(--blue); border-radius:0; padding:.3rem 0 .3rem 1.1rem}
.cl-goal .eyebrow{color:var(--blue)} .cl-goal p:last-child{margin-bottom:0} .cl-goal p{font-size:var(--step-1)}
.cl-why{font-size:var(--step-1); color:var(--ink-soft); line-height:1.55; margin:var(--s4) auto var(--s5);
  padding-left:1.1rem; border-left:2px solid var(--rule)}
.cl-terms{border-left:3px solid var(--violet)} .cl-terms .eyebrow{color:var(--violet)}
.cl-watch{background:var(--tint-honey); box-shadow:none; border:1px solid var(--rule)} .cl-watch .eyebrow{color:var(--honey)}
.cl-check .eyebrow{color:var(--leaf)} .cl-note{background:var(--card-2); box-shadow:none; color:var(--ink-soft)}
.cl-wrap{border-left:3px solid var(--leaf)} .cl-wrap .eyebrow{color:var(--leaf)}
.cl-goal p:last-child,.cl-terms :last-child,.cl-watch :last-child,.cl-note :last-child,.cl-check :last-child,.cl-wrap :last-child{margin-bottom:0}
.cl-terms ul,.cl-check ol,.cl-watch ul{margin:0; padding-left:0; list-style:none; display:grid; gap:.7rem}
.cl-terms li,.cl-check li,.cl-watch li{padding-left:0; min-width:0; overflow-wrap:break-word}
.cl-check ol{counter-reset:c}

/* ---- worked example ---- */
.worked{background:var(--card); border-radius:var(--radius); padding:1.2rem 1.4rem; margin:var(--s6) auto;
  box-shadow:var(--shadow); border-left:4px solid var(--blue)}
.worked .eyebrow{color:var(--blue)}
.worked ol,.worked ul{list-style:none; padding-left:0; margin:.4rem 0; display:grid; gap:1.1rem}
.worked li{padding-top:1.1rem; border-top:1px solid var(--rule); min-width:0; overflow-wrap:break-word} .worked li:first-child{padding-top:0; border-top:0}
.worked .katex-display{overflow-x:auto; padding:.3rem 0; margin:.5rem 0}
.worked :last-child{margin-bottom:0}
.worked,.answers{position:relative; overflow:hidden}
.worked::after,.answers::after{content:""; position:absolute; right:-22px; bottom:-22px; width:128px; height:128px; pointer-events:none; background:var(--blue); opacity:.05;
  --wm:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><circle cx='12' cy='12' r='10' fill='none' stroke='%23000' stroke-width='1.4'/><circle cx='12' cy='12' r='5.5' fill='none' stroke='%23000' stroke-width='1.4'/></svg>");
  -webkit-mask:var(--wm) center/contain no-repeat; mask:var(--wm) center/contain no-repeat}
.answers::after{background:var(--leaf)}

/* ---- practice / problem set: one clean column, wrap (never side-scroll) ---- */
.practice{margin:var(--s6) auto}
.practice .eyebrow{color:var(--ink-soft)}
.practice p em{font-style:normal; font-weight:600; font-size:var(--step--1); color:var(--ink-soft)}
.practice > p{margin:1.3rem 0 .5rem}
.practice ol{list-style:none; padding-left:0; margin:0; display:grid; gap:.6rem;
  grid-template-columns:repeat(auto-fill,minmax(min(100%,24rem),1fr))}
.practice li{display:flex; gap:.6rem; align-items:baseline; background:var(--card); border:1px solid var(--rule);
  border-left:2px solid var(--rule); border-radius:var(--radius-sm); padding:.6rem .85rem; box-shadow:var(--shadow);
  min-width:0; overflow-wrap:anywhere}
.practice li > .refcode{flex:0 0 auto}
.practice li:hover{border-color:var(--blue); border-left-width:4px}
.practice li:target{border-color:var(--blue); border-left-width:4px; background:var(--tint-blue)}
.practice li .katex{white-space:normal}
.practice li .katex-display{overflow-x:auto; margin:.3rem 0}

/* ---- answer key reveal ---- */
.answers{background:var(--card); border-radius:var(--radius); margin:var(--s6) auto; box-shadow:var(--shadow); overflow:hidden; border:1px solid var(--rule)}
.answers > summary{cursor:pointer; list-style:none; display:flex; align-items:center; gap:.6rem; padding:.9rem 1.25rem}
.answers > summary::-webkit-details-marker{display:none}
.answers .tw{width:.7rem; height:.7rem; border:2px solid var(--leaf); border-top:0; border-right:0;
  transform:rotate(-45deg); transition:transform .2s; flex:0 0 auto; margin-bottom:.12rem}
.answers[open] .tw{transform:rotate(45deg) translate(-1px,-1px)}
.answers summary .eyebrow{color:var(--leaf); margin:0}
.answers .hint{color:var(--ink-soft); font-size:var(--step--1)} .answers[open] .hint{display:none}
.answers .ak-body{padding:.1rem 1.4rem 1.1rem; overflow-wrap:break-word} .answers .ak-body > :last-child{margin-bottom:0}

/* ---- per-question answer reveal (textbook practice) ---- */
/* project visually-hidden helper, scoped to the reveal so the short '.vh' name can't hide anything else */
.qcheck .vh{position:absolute!important; width:1px; height:1px; padding:0; margin:-1px; overflow:hidden;
  clip:rect(0 0 0 0); white-space:nowrap; border:0}
/* scoped under .practice so the (0,1,1) '.practice > p' rule can't override these margins */
.practice .practice-intro{color:var(--ink-soft); font-size:var(--step--1); margin:.2rem 0 .7rem}
.practice .practice-sub{font-weight:600; font-size:var(--step--1); color:var(--ink-soft); margin:1.3rem 0 .5rem}
.prow{display:flex; gap:.5rem .9rem; align-items:baseline; flex-wrap:wrap; background:var(--card);
  border:1px solid var(--rule); border-radius:var(--radius); padding:.7rem .9rem; margin:.6rem 0}
.prow .prob{flex:1 1 60%; min-width:0; overflow-wrap:break-word}
.prow .pnum{color:var(--ink-soft); margin-right:.3rem}   /* shown only on rows without a refcode badge */
.prow .katex{white-space:normal} .prow .katex-display{overflow-x:auto; margin:.3rem 0}
.qcheck{margin-left:auto; flex:0 0 auto}
.qcheck > summary{cursor:pointer; list-style:none; display:inline-flex; align-items:center}
.qcheck > summary::-webkit-details-marker{display:none}
.qcheck .qc-show, .qcheck .qc-hide{font-size:var(--step--1); font-weight:600; color:var(--leaf);
  border:1px solid var(--leaf); border-radius:999px; padding:.28rem .7rem; background:var(--tint-leaf, transparent)}
.qcheck[open] .qc-hide{color:var(--ink-soft); border-color:var(--rule)}   /* muted 'Hide' once open */
.qcheck:not([open]) .qc-hide{display:none} .qcheck[open] .qc-show{display:none}
.qcheck .qa{align-items:center; gap:.4rem; margin-left:.55rem; font-weight:600; color:var(--leaf)}
.qcheck .qa::before{content:"\u2713"; font-weight:700}
.qcheck:not([open]) .qa{display:none} .qcheck[open] .qa{display:inline-flex}
@media (prefers-reduced-motion:no-preference){ .prow{transition:border-color .15s ease} }
/* print: show every answer (even un-opened reveals) and hide the toggle. The screen rule
   .qcheck:not([open]) .qa{display:none} has higher specificity, so !important is needed here. */
@media print{ .qcheck .qa{display:inline-flex !important} .qcheck > summary{display:none} }

/* ---- prev / next page nav ---- */
.pagenav{display:flex; gap:1rem; justify-content:space-between; align-items:stretch;
  margin:var(--s7) auto 0; padding-top:var(--s5); border-top:1px solid var(--rule)}
.pagenav a{display:flex; flex-direction:column; gap:.15rem; flex:1 1 0; max-width:49%; text-decoration:none;
  background:var(--card); border:1px solid var(--rule); border-radius:var(--radius); padding:.8rem 1.1rem; box-shadow:var(--shadow)}
.pagenav a:hover{border-color:var(--blue)}
.pagenav .pn-next{text-align:right; margin-left:auto}
.pagenav .pn-dir{font-size:var(--step--1); color:var(--ink-soft)}
.pagenav .pn-title{font-weight:600; color:var(--ink); font-family:"Fraunces",serif}

/* ---- unit overview: list of its lessons ---- */
.lesson-list ol{list-style:none; padding:0; margin:var(--s5) auto; display:grid; gap:.7rem}
.lesson-list li{margin:0}
.lesson-list a{display:block; background:var(--card); border:1px solid var(--rule); border-left:3px solid var(--blue);
  border-radius:var(--radius-sm); padding:.75rem 1.05rem; text-decoration:none; box-shadow:var(--shadow); color:var(--ink)}
.lesson-list a:hover{border-color:var(--blue)}
.lesson-list a b{font-family:"Fraunces",serif; color:var(--link); margin-right:.3rem}

/* ---- tutor-guide problem card (cross-site consistency) ---- */
.tproblem{background:var(--card); border:1px solid var(--rule); border-radius:var(--radius); padding:1rem 1.25rem; margin:var(--s4) auto; box-shadow:var(--shadow)}
.tproblem > .refcode{display:inline-block; margin-bottom:.5rem}
.tproblem > p{margin:.2rem 0 .6rem}
.tproblem .answers{margin:.5rem 0 0; box-shadow:none}
.tproblem .ans{margin:.7rem 0 0}

/* ---- figure (graph paper belongs here) ---- */
figure.fig{margin:var(--s6) auto; background:var(--card); border-radius:var(--radius); padding:1.1rem 1.1rem .7rem;
  box-shadow:var(--shadow); text-align:center; border:1px solid var(--rule);
  background-image:linear-gradient(var(--rule) 1px,transparent 1px),linear-gradient(90deg,var(--rule) 1px,transparent 1px);
  background-size:22px 22px}
figure.fig svg{max-width:100%; max-height:360px; height:auto; display:block; margin-inline:auto}
figcaption{color:var(--ink-soft); font-size:var(--step--1); margin-top:.6rem; text-align:left}
figcaption b,figcaption strong{color:var(--blue); font-weight:600}
html.dark figure.fig [stroke="#888"]{stroke:#7c8590} html.dark figure.fig text[fill="#888"]{fill:#9aa3b0}
html.dark figure.fig text[fill="#c0392b"],html.dark figure.fig [fill="#c0392b"]{fill:#ef9b8e}
html.dark figure.fig text[fill="#2980b9"],html.dark figure.fig [fill="#2980b9"]:not(line){fill:#6fb0e8}
html.dark figure.fig text[fill="#27ae60"]{fill:#69cf97} html.dark figure.fig text[fill="#8e44ad"]{fill:#c3a4e6}
html.dark figure.fig line[stroke="#2980b9"]{stroke:#6fb0e8} html.dark figure.fig line[stroke="#8e44ad"]{stroke:#c3a4e6}
/* #555 is a neutral gray hardcoded inline by the flowchart figures (sub-labels + an inner caption);
   lighten it in dark mode so the prose + equations stay legible. !important beats the inline style. */
html.dark figure.fig text[fill="#555"]{fill:#a7adb4}
html.dark figure.fig [style*="color:#555"]{color:#a7adb4 !important}

/* ---- inline metaphor illustration (raster; warm, decorative but meaningful) ---- */
figure.illus{margin:var(--s5) auto; max-width:30rem; text-align:center}
figure.illus img.illus-art{width:100%; height:auto; border-radius:var(--radius); box-shadow:var(--shadow); display:block}
html.dark figure.illus img.illus-art{filter:brightness(.92) saturate(.94)}

/* ---- viz: candidate visual elements embedded in lessons (svg / html / interactive) ---- */
figure.viz{margin:var(--s6) auto; max-width:var(--wide); background:var(--card); border:1px solid var(--rule);
  border-radius:var(--radius); padding:1.1rem 1.2rem .8rem; box-shadow:var(--shadow); overflow:hidden}
figure.viz figcaption{color:var(--ink-soft); font-size:var(--step--1); margin-top:.7rem; text-align:center}
figure.viz svg{max-width:100%; height:auto}
figure.viz .katex-display{overflow-x:auto}
figure.viz input[type=range]{width:100%; max-width:24rem}

/* ---- objectives blockquote & tables ---- */
blockquote{margin:var(--s5) auto; padding:1rem 1.25rem; background:var(--tint-blue); border:1px solid var(--rule);
  border-left:3px solid var(--blue); border-radius:var(--radius); color:var(--ink)}
blockquote :last-child{margin-bottom:0}
table{border-collapse:collapse; width:100%; margin:var(--s4) auto; font-size:.95em; background:var(--card); border-radius:var(--radius-sm); overflow:hidden}
th,td{border:1px solid var(--rule); padding:.45rem .65rem; text-align:left} th{background:var(--card-2); font-family:"IBM Plex Mono",monospace; font-size:.85em; font-weight:600}
.katex-display{overflow-x:auto; overflow-y:hidden; padding:.2rem 0; max-width:100%}

/* ---- landing / index catalogs ---- */
ul.units{list-style:none; padding:0; margin:var(--s5) auto; display:grid; gap:.9rem;
  grid-template-columns:repeat(auto-fill,minmax(min(100%,20rem),1fr))}
ul.units li{margin:0; background:var(--card); border:1px solid var(--rule); border-radius:var(--radius); padding:1rem 1.15rem; box-shadow:var(--shadow)}
ul.units a{text-decoration:none; font-size:var(--step-1)} ul.units a b{font-family:"Fraunces",serif}
.u{color:var(--ink-soft); font-size:.92em}
section.ug{margin:var(--s4) auto; background:var(--card); border:1px solid var(--rule); border-radius:var(--radius); padding:1rem 1.25rem; box-shadow:var(--shadow)}
section.ug h3{margin:.1rem 0 .4rem} section.ug :last-child{margin-bottom:0}
.toc{background:var(--card); border:1px solid var(--rule); border-radius:var(--radius); padding:.8rem 1.15rem}

/* ---- mobile: the rail slides in over the page ---- */
@media (max-width:62rem){
  .shell{grid-template-columns:minmax(0,1fr)}
  .menu{display:inline-flex; order:-1}
  .sidenav{position:fixed; top:0; left:0; height:100dvh; width:17rem; max-height:none; z-index:60;
    transform:translateX(-100%); transition:transform .2s ease; box-shadow:0 0 40px rgba(0,0,0,.3)}
  body.nav-open .sidenav{transform:none}
  body.nav-open::after{content:""; position:fixed; inset:0; background:rgba(0,0,0,.4); z-index:50}
}

/* ---- motion (reduced-motion safe) ---- */
@media (prefers-reduced-motion:no-preference){
  .practice li,.worked,figure.fig,#theme,.menu,ul.units li,.refcode,.xref,.lesson-list a,.pagenav a{transition:border-color .15s ease, box-shadow .15s ease, color .15s ease, transform .15s ease}
  ul.units li:hover,.lesson-list a:hover,.pagenav a:hover{transform:translateY(-1px)}
  :target{animation:flash 1.4s ease-out 1} @keyframes flash{0%{background:var(--tint-honey)}100%{background:transparent}}
}

/* ---- print (courtesy) ---- */
@media print{
  html{overflow-x:visible}   /* reset the screen-only clip guard so paged media can't drop content */
  .topbar,.sidenav,.pagenav{display:none} .shell{display:block} a{color:inherit; text-decoration:none}
  body,figure.fig{background-image:none}
  .answers[open] .ak-body, details > *{display:revert} details{display:block} .answers summary{display:none}
  .worked,.practice li,figure.fig,blockquote,ul.units li{break-inside:avoid; box-shadow:none}
}

/* ---- reference-code tutor launcher (textbook surface only) ---- */
body[data-surface="textbook"] .refcode{cursor:copy}
body[data-surface="textbook"] #rc-tip{position:fixed; z-index:80; max-width:min(92vw,30rem); margin:0;
  padding:.6rem .8rem; background:var(--card); color:var(--ink); border:1px solid var(--rule);
  border-radius:var(--radius-sm); box-shadow:var(--shadow);
  font:var(--step--1)/1.5 "Source Serif 4",var(--serif-math),Georgia,serif;
  opacity:0; visibility:hidden; pointer-events:none}
body[data-surface="textbook"] #rc-tip.show{opacity:1; visibility:visible}
body[data-surface="textbook"] #rc-tip .rc-tip-h{display:block; font-weight:600; font-size:.82em;
  letter-spacing:.01em; color:var(--ink-soft); margin-bottom:.25rem}
body[data-surface="textbook"] #rc-tip .rc-tip-q{display:block; color:var(--ink)}
body[data-surface="textbook"] #rc-toast{position:fixed; left:50%; bottom:1.4rem; transform:translateX(-50%);
  z-index:90; background:var(--ink); color:var(--paper); border-radius:999px; padding:.55rem 1.1rem;
  font:var(--step--1)/1.3 "Source Serif 4",Georgia,serif; box-shadow:var(--shadow);
  opacity:0; visibility:hidden; pointer-events:none; max-width:92vw}
body[data-surface="textbook"] #rc-toast.show{opacity:1; visibility:visible}
@media (prefers-reduced-motion:no-preference){
  body[data-surface="textbook"] #rc-tip{transition:opacity .12s ease}
  body[data-surface="textbook"] #rc-toast{transition:opacity .18s ease, transform .18s ease}
  body[data-surface="textbook"] #rc-toast.show{transform:translateX(-50%) translateY(-2px)}
}
"""


_UNIT_HERO = {"1": "numberline", "2": "balance", "3": "steps", "4": "machine", "5": "lines",
              "6": "modeling", "7": "systems", "8": "inequality", "9": "exponential", "10": "areamodel",
              "11": "factoring", "12": "arch", "A": "dots"}


def _index_html(ssot, model):
    items = []
    for u in ssot.units:
        href = _overview_fname(u.id)
        opt = " (optional)" if u.optional else ""
        label = "Appendix" if str(u.id) == "A" else f"Unit {u.id}"
        items.append(f'<li><a href="{href}"><b>{label}</b> · {_html.escape(u.title)}</a>{opt}'
                     f'<br><span class="u">{_html.escape(u.description)}</span></li>')
    body = ('<p class="subtitle">New here? Start with <a href="how-to-use.html">how to use this book</a>.</p>'
            '<ul class="units">' + "\n".join(items) + "</ul>")
    return _lesson_page("Algebra 1", body, model, "index.html", None, ("how-to-use.html", "How to use this book"),
                        subtitle="A complete, friendly Algebra 1 course you can read at your own pace.",
                        hero="../assets/index-hero.jpg")


def _intro_page(model, next_link):
    md = open(os.path.join(TEXTBOOK_SRC, "how-to-use.md"), encoding="utf-8").read()
    body = _strip_lead(md_to_body(md, launcher=True), "h1")
    return _lesson_page("How to use this book", body, model, "how-to-use.html",
                        ("index.html", "All units"), next_link, kicker="Start here")


def build_site(ssot):
    # read + split every unit once
    units_data = []
    for u in ssot.units:
        intro, lessons = _split_unit(open(_md_path(u.id), encoding="utf-8").read())
        units_data.append((u, intro, lessons))

    # sidebar model (every unit, with its lessons)
    model = [{"id": str(u.id), "title": u.title, "overview": _overview_fname(u.id),
              "lessons": [{"id": lid, "title": lt, "fname": _lesson_fname(lid)} for lid, lt, _ in lessons]}
             for u, _i, lessons in units_data]

    # linear page sequence for prev/next
    seq = [("how-to-use.html", "How to use this book")]
    for u, _i, lessons in units_data:
        seq.append((_overview_fname(u.id), "Appendix" if str(u.id) == "A" else f"Unit {u.id}"))
        for lid, _lt, _c in lessons:
            seq.append((_lesson_fname(lid), f"Lesson {lid}"))
    posn = {fn: k for k, (fn, _l) in enumerate(seq)}

    def around(fn):
        k = posn[fn]
        prev = seq[k - 1] if k > 0 else None
        nxt = seq[k + 1] if k + 1 < len(seq) else None
        return prev, nxt

    files = {"textbook.css": CSS}
    files["index.html"] = _index_html(ssot, model)
    files["how-to-use.html"] = _intro_page(model, around("how-to-use.html")[1])

    for u, intro, lessons in units_data:
        ov = _overview_fname(u.id)
        kicker = "Appendix" if str(u.id) == "A" else f"Unit {u.id}"
        # overview page: hero + unit intro + a list of its lessons
        intro_html = _strip_lead(md_to_body(intro, launcher=True), "h1")
        ll = ['<nav class="lesson-list" aria-label="Lessons in this unit"><ol>']
        for lid, lt, _c in lessons:
            ll.append(f'<li><a href="{_lesson_fname(lid)}"><b>Lesson {lid}</b>{_html.escape(lt)}</a></li>')
        ll.append("</ol></nav>")
        pl, nl = around(ov)
        files[ov] = _lesson_page(u.title, intro_html + "\n" + "\n".join(ll), model, ov, pl, nl,
                          subtitle=u.description, hero=f"../assets/{_UNIT_HERO.get(str(u.id), 'lines')}.jpg",
                          kicker=kicker)
        # one page per lesson
        for lid, lt, chunk in lessons:
            fn = _lesson_fname(lid)
            lbody = _strip_lead(md_to_body(chunk, launcher=True), "h2")
            pl2, nl2 = around(fn)
            files[fn] = _lesson_page(lt, lbody, model, fn, pl2, nl2, kicker=f"{kicker} · Lesson {lid}",
                                     hero=_lesson_hero(lid))
    return files


def generate():
    os.makedirs(OUT_DIR, exist_ok=True)
    files = build_site(_ssot())
    for name, content in files.items():
        open(os.path.join(OUT_DIR, name), "w", encoding="utf-8", newline="\n").write(content)
    return len(files)


def check():
    files = build_site(_ssot())
    issues = []
    for name, content in files.items():
        p = os.path.join(OUT_DIR, name)
        if not os.path.exists(p):
            issues.append(f"{name}: missing (run build_textbook.py)")
        elif open(p, encoding="utf-8").read() != content:
            issues.append(f"{name}: stale (run build_textbook.py)")
    return issues


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if a.check:
        iss = check()
        if iss:
            print("FAIL:\n  " + "\n  ".join(iss)); return 1
        print(f"textbook: {len(build_site(_ssot()))} files current."); return 0
    n = generate(); print(f"generated {n} textbook files -> {os.path.relpath(OUT_DIR, REPO_ROOT)}/"); return 0


if __name__ == "__main__":
    sys.exit(main())
