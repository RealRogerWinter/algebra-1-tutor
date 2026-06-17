# How to use this book

## What algebra is, and why it's worth your time

<!--illus:howto-what-is-algebra-->

You already do algebra in your head more often than you'd think. Algebra is just arithmetic with one new move: when a number is hidden, you let a letter stand in for it until you can work out what it is. That's the whole starting idea. The letter, often x, is a placeholder for a number you don't know yet, and the rest is the arithmetic you already do.

Most real questions come with a hidden number in them. Three of you split a $54 dinner evenly, and you want each share: that's 3x = 54, and x is the share. You're doubling a recipe that calls for 3/4 cup of flour, and you want the new amount. You're driving 150 miles and want to know how long it takes at 50 miles an hour, or how much of your paycheck is left after rent. Each one is a relationship between quantities, with one piece unknown. Writing it with a letter lets you pin the unknown piece down instead of guessing.

So algebra isn't a separate, harder kind of math sitting on top of arithmetic. It's a tool for answering questions you already care about, and it's a way of describing how quantities depend on each other so a pattern you've noticed can tell you what comes next. You learn it one small idea at a time, and each idea is a short step from the one before. If a page ever feels like too much at once, that's a sign to slow down, not a sign that this isn't for you. Plenty of capable adults meet algebra for the first time later on and do just fine, because every piece of it is built from arithmetic you already trust.

## Setting up the tutor in Claude

The tutor is a free **Claude skill** — a small add-on that turns Claude into your Algebra 1 teacher, with this whole book already in front of it. You set it up once, and from then on Claude knows the lessons, the worked examples, and every practice problem by its code.

The usual way is the Claude app or the website:

1. Download **[`algebra-1-tutor.zip`](https://github.com/RealRogerWinter/algebra-1-tutor/raw/main/algebra-1-tutor.zip)** (the skill file).
2. Open Claude — the **desktop or mobile app**, or **claude.ai** in a browser — and go to **Settings**. Turn on code execution under **Capabilities** (a recommended extra, not a requirement), then open **Features** and upload the `.zip` under **Skills**.
3. Start a new chat and just say what you want. The tutor wakes up on its own whenever you ask about algebra, even if you never use the word.

It works on the **free plan**. A larger model such as Opus tutors a little more sharply, but it isn't required, and the tutor checks its own arithmetic either way.

(If you use **Claude Code**, the terminal tool for developers, you can install the same tutor with two commands — the [project README](https://github.com/RealRogerWinter/algebra-1-tutor#readme) has them. There the graphs and notation don't render: math shows as raw text and figures as raw markup, so the app or website is the smoother place to learn.)

## How to use this book with Claude

<!--illus:howto-using-claude-->

Read it at your own pace. The book is written to be read straight through, on your own, with each lesson explaining itself. Take the worked examples slowly, try the practice, and check your answers against the key at the end of each lesson. There's no clock.

When you get stuck, or you just want more, ask Claude, your Algebra 1 tutor. Claude has this whole book in front of it, so you can lean on it the way you'd lean on a patient person sitting beside you.

A few things it's good for:

- **Point it at one exact item by its short reference code.** Every worked example and practice problem has a small code like 1.1.w2 (worked example 2 in Lesson 1.1) or 5.3.4 (practice problem 4 in Lesson 5.3). Say "explain 1.1.w2" or "walk me through 5.3.4," and Claude pulls up that exact item and works through it with you.
- **Ask for another angle.** If an explanation doesn't land, ask Claude to explain it a different way. A second picture often does it.
- **Solve a problem together, step by step.** Ask Claude to work a problem with you one line at a time, so you're doing the thinking, not just watching.
- **Get more practice.** When a skill is almost solid and you want a few more to lock it in, ask for extra problems like the ones you just did.
- **Upload a photo of your handwritten work.** Take a picture of what you wrote on paper and send it. Claude will read your steps, check them, and show you exactly where a line went sideways if one did.

### A walkthrough: getting unstuck

Say you are working through Lesson 5.3 and practice problem **5.3.4** won't come out right — you keep getting a slope that doesn't match the key. Beside the problem in the online book is its short code, `5.3.4`. Copy it, open your tutor chat, and paste a short request:

> **You:** Walk me through 5.3.4.

Claude has the book in front of it, so it pulls up that exact problem — and starts where a good teacher would, with you:

> **Claude:** Happy to. Before I show anything: what did you get, and where did it stop feeling right?
>
> **You:** I found the slope but it came out positive, and the key says negative.
>
> **Claude:** Let's check just that. Which two points did you use, and which one did you treat as the starting point?

From there you go back and forth. You do the thinking; Claude nudges. When you spot the slip yourself — say you counted the run right-to-left, so the sign flipped — you fix it, and *that* is what makes it stick. If an explanation still doesn't land, say so: *"Can you show that a different way?"* and Claude reaches for another picture. When it finally clicks, ask for one more like it to be sure: *"Give me a similar one to try on my own."*

That is the whole rhythm: copy a code, ask, talk it through, then prove it to yourself.

### Or let Claude teach the whole course

You don't have to drive. If you would rather be taught, just say so:

> **You:** I'd like to learn algebra from the beginning.

Claude will start at Lesson 1.1 and take you through in order — explaining a little, then handing the work back to you, checking that an idea really landed before moving on, and meeting you where you are if you already know some of it. At a good stopping point, ask for a **Progress Card**: a short, readable note of where you are and what comes next. Paste it back at the start of your next chat and Claude picks up right where you left off, since each conversation otherwise begins fresh.

Either way works, and you can switch between them — read on your own and call Claude in for the hard parts, or let it lead and read along. The book and the tutor are the same course, generated from one source, so they always agree.

You don't need any of this to begin. Open the first lesson and start reading. Claude is there for the moments you want a hand, and asking for one is part of how this works, not a sign you're behind.
