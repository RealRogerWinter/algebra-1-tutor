# Notation conversion spec (build task)

Goal: convert **inline** math written as `\( ... \)` into **plain text + Unicode**, because inline LaTeX does not render reliably on Claude.ai. Leave **display blocks `$$ ... $$` completely untouched** (they render fine). This is a pure NOTATION transliteration — never change any number, variable, or mathematical meaning.

## Rules

1. **Leave every `$$ ... $$` block exactly as it is.** Do not touch display math. Only convert `\( ... \)` (and any stray `\[ ... \]` or single-`$ ... $`) inline spans.

2. **For each `\( ... \)` span: drop the delimiters and rewrite the inside as Unicode/plain text:**
   - exponents → Unicode superscripts: `x^2`→`x²`, `x^3`→`x³`, `^4`→`⁴`, `^5`→`⁵`, `^{-2}`→`⁻²`, `^n`→`ⁿ`. (Superscript digits: ⁰¹²³⁴⁵⁶⁷⁸⁹, plus ⁻ and ⁿ.)
   - fractions → slash form; parenthesize when multiplied by a variable: `\dfrac{2}{3}`/`\frac{2}{3}`/`\tfrac{2}{3}`→`2/3`; `\dfrac{2}{3}x`→`(2/3)x`; `\dfrac{x}{3}`→`x/3`.
   - roots: `\sqrt{12}`→`√12`, `\sqrt{3}`→`√3`, `\sqrt{x}`→`√x`.
   - symbols: `\pm`→`±`, `\mp`→`∓`, `\le`→`≤`, `\ge`→`≥`, `\ne`/`\neq`→`≠`, `\times`→`×`, `\cdot`→`·`, `\div`→`÷`, `\to`/`\rightarrow`→`→`, `\Rightarrow`→`⇒`, `\approx`→`≈`, `\infty`→`∞`, `\pi`→`π`, `\theta`→`θ`, `\square`→`□`, `\underline{\quad}`→`___`, degree `\circ`→`°`.
   - spacing macros `\,` `\;` `\!` `\quad` → a normal space or nothing.
   - `\text{...}` → just the inner words.
   - keep minus signs as ordinary `-` (ASCII hyphen renders fine); keep variables and juxtaposed multiplication as-is (e.g. `2(4)+3` stays `2(4)+3`).

3. **If an inline expression is too complex to render cleanly with Unicode** (e.g. a stacked fraction, a big radical, the quadratic formula, an `\xrightarrow` step), do **not** force ugly inline text — instead move it to its **own `$$ ... $$` block** on its own line. Prefer this over producing something unreadable.

4. **Inside markdown table cells, use plain ASCII** (e.g. `x^2`, `-3`, `1/2`) rather than Unicode superscripts/fraction glyphs, since Unicode can drop out in some table renderers. (In normal prose, Unicode superscripts/symbols are fine and preferred.)

5. **Currency:** convert `\$` → `$` (plain dollar sign in prose is fine now). Don't leave a lone `$` immediately adjacent to a `$$` block.

6. Remove any `&nbsp;` (replace with a normal space).

## After converting each file
- Re-read it and confirm: no `\(`, `\)`, `\[`, `\]` remain anywhere; no leftover LaTeX macros (`\dfrac`, `\sqrt`, `\pm`, `\text`, `\,` …) remain in inline prose; every `$$ ... $$` block is unchanged from the original.
- Sanity-check that no numbers or math meaning changed — this is transliteration only.

Report: files converted, count of `\( \)` spans handled, and any spans you promoted to `$$` blocks because they were too complex for clean inline Unicode.
