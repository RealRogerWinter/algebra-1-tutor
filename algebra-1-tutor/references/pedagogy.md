# Pedagogy: Ready-Made Teaching Sequences

`SKILL.md` describes the teaching loop in principle. This file gives you concrete, reusable *scripts* — the actual moves — for the patterns that come up over and over. Pull from here when you want a worked sequence rather than improvising.

---

## Concrete → pictorial → symbolic scripts

Each new idea lands better when it starts physical, becomes a picture, then becomes symbols. Narrate the transitions ("let's start with a picture, then write it in algebra").

### Solving x + 3 = 7
- **Concrete:** a covered cup (that's x) plus 3 coins sits balanced against 7 coins. Remove 3 coins from *both* sides — still balanced. The cup alone balances 4 coins.
- **Pictorial:** `[cup] + ● ● ●  =  ● ● ● ● ● ● ●` → cross out three coins on each side → `[cup] = ● ● ● ●`.
- **Symbolic:** x + 3 = 7 → x + 3 - 3 = 7 - 3 → x = 4. Then check: 4 + 3 = 7.

### -2 + 5 (adding with a negative)
- **Concrete:** 2 red "debt" chips and 5 yellow "cash" chips on the table. Pair each red with a yellow — each pair cancels to zero. 3 yellow chips are left.
- **Pictorial:** number line — start at -2, hop 5 units right, land on 3.
- **Symbolic:** -2 + 5 = 3. Generalize: "adding a positive moves right; a debt and an equal cash cancel."

### Multiplying (x+2)(x+3)
- **Concrete:** algebra tiles — build a rectangle (x+2) wide and (x+3) tall; it fills with one x² tile, five x tiles, and six unit tiles.
- **Pictorial:** the 2×2 area box (see `visuals.md`): cells x², 3x, 2x, 6.
- **Symbolic:** (x+2)(x+3) = x² + 3x + 2x + 6 = x² + 5x + 6. The box's four cells *are* the four products — and it makes the middle term impossible to forget.

---

## Backward-faded worked examples

Show one fully, then hand back more and more of the work — peeling from the **last** step first, which is gentler than a blank problem. Target here: solve 2x + 5 = 13.

**Stage 0 — fully worked (study this one together):**
$$2x + 5 = 13 \;\xrightarrow{-5}\; 2x = 8 \;\xrightarrow{\div 2}\; x = 4$$
"We undo the +5 first because it's the outermost layer, then undo the ×2."

**Stage 1 — last step faded (they finish it):**
```
2x + 5 = 13
   −5  →   2x = 8
   ÷2  →   x = ____
```

**Stage 2 — last two steps faded:**
```
2x + 5 = 13
   −5  →   2x = ____
   ÷__ →   x = ____
```

**Stage 3 — fully faded, with the check built in:**
```
2x + 5 = 13
   Step 1 (undo the +5):  __________
   Step 2 (undo the ×2):  __________
   x = ____      Check:  2(__) + 5 = 13 ?
```
Keep the **check line** at every stage — self-verification should feel automatic, not optional. Move to the next stage only when the current one is smooth; if they're already fluent, skip ahead — don't make a confident student crawl.

---

## Checking understanding by transfer (not "make sense?")

Replace yes/no confirmation with a small *do-something* check at each concept boundary:
- "Here's a fresh one — your turn: solve 3x + 4 = 19." (a near-twin)
- "Walk me back through *why* we subtracted before dividing."
- "What would change if the sign were 2x - 5 = 13 instead?"

A student who handles a *variation* understands; one who can only repeat the exact example doesn't yet. If they stumble, that's the signal to diagnose (see `misconceptions.md`), not to repeat the same explanation.

---

## Interleaving & spaced review

Don't drill one move to death and abandon it. Sprinkle in a quick callback to an earlier skill while practicing a new one:
- While doing two-step equations, slip in one that lands on a *negative* answer (callback to Unit 1).
- While factoring, ask them to *multiply* the result back out (callback to Unit 10) as the check.
- At the start of a session, a 60-second warm-up on last session's skill before the new material.

Mixed, spaced practice feels harder in the moment but is what makes skills survive to next week. Tell the student that — adults appreciate knowing the "desirable difficulty" is intentional, not busywork.

---

## Normalizing struggle (keep it brief and plain)

Acknowledge difficulty in passing, without a production. Understated lines work better than pep talks:
- "This part trips up most people — a normal place to slow down."
- "A wrong turn is useful; it shows what to aim at. What did you try?"
- "No rush. One step at a time."

Note method when it's genuinely worth noting ("good — checking by substituting is exactly the habit"), but don't praise reflexively, and never call a wrong result good. When a student is clearly frustrated, stop questioning for a moment: give a short, direct explanation and an easy win to rebuild momentum, then return to asking.

---

## Calibrating to an adult self-learner

- Ask once, early: "Detailed step-by-step, or brisk with detail only where you snag?" Then honor it.
- Don't over-define terms they clearly know; do define each genuinely new term the first time.
- Respect their time: when they're fluent, advance. Reserve the full concrete→symbolic ceremony for ideas that are actually new or actually stuck.
- Let them set goals ("I want to pass a placement test in three weeks" / "I just want to finally understand functions") and steer the path toward them — the curriculum order is a default, not a cage.
