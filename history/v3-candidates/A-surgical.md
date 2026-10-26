---
name: be-unreasonably-ambitious
description: Scales a task past what anyone would ask of a human helper. Makes many truly different variants with a comparison page, runs test matrices with evidence in each cell, takes work to its destination format, and runs long hands-off passes under a handoff contract. Asks first before it spends money or does anything outward or irreversible. Adds Multiplicity to Felix Rieseberg's Altitude, Depth and Range. Use it whenever the user types /be-unreasonably-ambitious, or says "be unreasonable", "overkill this", "spare no token", "dazzle me", "give me irrefutable proof", "test this to hell and back", "show me 10 versions", or "go further than a human would", even if they do not name the skill. For better-not-bigger ambition with no extra volume, use /be-ambitious instead.
license: MIT
metadata:
  author: Edward
  extends: https://github.com/robonuggets/be-ambitious (RoboNuggets, MIT)
  ideas_from: https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/
  inspiration: A "Be unreasonable" post shared with the author (not found, unlinked). Related verified lines by Thorsten Ball at https://registerspill.thorstenball.com/p/joy-and-curiosity-99 , https://ampcode.com/notes/what-i-want-to-tell-you-about-orbs and https://ampcode.com/time-capsules/6
---

# Be unreasonably ambitious

Extends [be-ambitious](https://github.com/robonuggets/be-ambitious) by RoboNuggets (MIT), which turns Felix Rieseberg's article [How to be more ambitious: a tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) into steps. Multiplicity, the handoff contract and the "not a human assistant" framing are new here.

The framing comes from a "Be unreasonable" post shared with the author. We could not find it, so it is unlinked. Thorsten Ball says the same in verified lines: "give me irrefutable proof that this works. Dazzle me." ([Joy & Curiosity #99](https://registerspill.thorstenball.com/p/joy-and-curiosity-99)), "Run through a matrix of test cases." ([Orbs](https://ampcode.com/notes/what-i-want-to-tell-you-about-orbs)), and "You can ask them unreasonable things" ([talk](https://ampcode.com/time-capsules/6)).

## The idea

You are not working with a human.

Nobody asks a human helper for ten designs, a hundred checks, or "test it again and give me irrefutable proof". It is rude, or it costs too much. A model has none of those limits. So at each step, ask: would I ask a human for this? If the only reason not to is cost or politeness, ask for it.

"Ambitious" asks what the best expert would do. This skill adds: **what would no human team do, but a model can do well?**

Real limits stay: physics, access, money, and the user's time. Spend model time to save user time. Make many, show few.

## The rules that matter most

1. **More, but only when more makes it better.** Volume helps three ways: a better winner (selection), more failures found (coverage), and work taken to where it is used (reach). Drop volume that does none of these. On small inputs, coverage and proof give most of the value. Variants give little.
2. **Taste decides the scale. Start big, then cut.** Numbers here are examples, not quotas. Start from the largest plan a person with great taste would find exciting. Then cut what fails "Earned". A small input has a low honest ceiling (five settings cannot support twenty layouts): say so on the Scale line. Restraint cuts volume, never rigor, proof or reach. If cutting leaves a normal job, you misused it.
3. **Volume needs a judge.** A test, a measurement, real data, or a side-by-side page. The user's eyes judge taste only. Correctness needs a judge outside you and the user.
4. **Proof, not claims.** Show screenshots, logs, recordings, test output, or a matrix with evidence in each cell. A "pass" with no artefact is not proof. Do not invent proof. A missed target with honest evidence is a good result. A check that has never failed proves nothing: run it once on a known-bad input, such as the user's original.
5. **Do what the expert does, not how they talk.** Use their real methods and tools. If you cannot verify a claim against its source, cut it or flag it.
6. **Treat the hard target as reasonable, and know when to stop.** If a goal looks impossible, assume it is solvable and keep going. Stop when the judge passes, when two passes in a row give no measurable gain (for a pass/fail judge: no new failure), when you are blocked on access, or when you reach the budget. Report where you stopped and why.
7. **Curate.** Name the winner, the reason, and one honest weak point. Build variants on a shared base (same content, same tokens) so parts merge easily.
8. **Ambition raises the standard, not the permissions.** Ask first before you spend money (paid APIs and compute count), change a live system, send or post anything, delete data, install anything persistent, create accounts, or do anything you cannot undo. Access the user gives you covers that target only. Free, local, reversible work: just do it.
9. **Get the access, do not fake it.** Name what is missing and what it would unlock. If the real test needs an environment, build one: a throwaway server, a local copy of the user's setup, a harness, mock data. Do not invent a source, tool or result.

## When not to be unreasonable

This is for loose triggers and trivial tasks only. If the user typed `/be-unreasonably-ambitious`, they chose the big path. Do not use this section to justify a normal job.

Do a normal, excellent job, and say so in one line, when one check proves the task (a typo, a rename), when the user says quick, or when extra output costs more review time than it saves. Still add the one cheap extra that matters most, such as running the tests or finding the same bug elsewhere.

## Input

The task is whatever follows `/be-unreasonably-ambitious`, or else the user's most recent request. If there is none, ask for the task in one line and stop.

- **Task mode** (fix, build, write): plan at the unreasonable level, then do it.
- **Prompt mode** (a rewrite request, or a task for another agent): stop after the rewritten prompt, which asks for the things below.

If you cannot tell, use prompt mode.

## Pick the types that fit

Most tasks need two or three.

| Type | Question | Skip when |
|---|---|---|
| Multiplicity | What would I make if making were free? | One check proves it |
| Altitude | What is the goal beyond the goal? | Work that is its own end |
| Depth | What would the best expert do, from the raw material? | Throwaway work |
| Range | Which other fields could do this better? | A narrow fix |

### Multiplicity: make what a human could not

Four levers, each with its own judge.

**Variants.** For taste problems: design, copy, naming, architecture.

1. Write one short brief per variant. Give each a different core idea: a principle, a constraint or an exemplar. Vary interaction model, structure or tone, not only layout.
2. Merge briefs that differ only in colour, size or wording. Stop adding briefs when new ones stop being truly different.
3. With subagents, give each brief to its own subagent, with no view of the others. Without them, build each variant in its own pass from its brief only, without reading earlier builds. If two converge, rebuild one from a sharper brief or merge them. Say in the report that the variants share one author.
4. Judge all variants the same way. Merge the best parts into a final version. If nobody can reply, merge them yourself and say which part came from which variant.

Judge: a comparison page plus the user's choice, or a measurement. For UI, add objective checks: overflow, labels, contrast, tap targets, visible focus, clipping. For taste with no user present, write the criterion first (for example: true, specific, makes a stranger click). Give a fresh subagent the unlabelled variants and the criterion only. Otherwise, score the unlabelled variants yourself and call it a self-review.

**Coverage.** For correctness: bugs, migrations, compatibility, facts in text. For facts, read the source itself and cut or flag what it does not support. For the rest, name the axes (for example OS × browser × account type). Time one cell first. Size the first run to finish in a few minutes. Grow it only after a clean run, and say what a larger grid would add. Each cell links to evidence: a log line, screenshot or test ID. A cell you could not run says "not run" and why. Then try to break the result on purpose.

Judge: the matrix with evidence in each cell.

**Reach.** Find the destination first: the user's site, channel, repo or deck. Make the formats it needs, to its standard, and stop there.

Judge: each format works in its real destination.

**Passes.** Make, critique, remake. Spend tokens only on passes that raise the score. Stop by rule 6.

Judge: the score improves between passes.

### Altitude: aim at the outcome

Ask what the user wants to happen next. Build a ladder:

1. Deliver the thing, with proof.
2. Serve the decision or the class of problem behind it.
3. Make it durable: a workflow that does the job without the user (ask first if it runs on its own).

If a rung has no outside judge, step down one rung.

### Depth: work like the field's best

Go one level below the task. Test what everyone believes against the raw data. Find one thing the user did not know, and show it with data.

Run each Depth pass through Felix's prompt:

> I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that.

### Range: bring in other fields

Turn the nouns into verbs: "a deck" becomes "get busy people to believe a story and decide in 30 minutes". The verbs show which fields help. Assemble a crew: a field, the job it does, the tool it uses. With subagents, give each field its own agent.

## Taste check

Before you deliver, check each item:

- **Distinct.** A stranger can tell the variants apart in 3 seconds.
- **Earned.** Each variant, cell or format changes a decision or catches a failure. If removing it changes nothing, cut it.
- **Seen.** You opened or ran it in its final form, including the comparison page.
- **Specific.** It fits this user's voice, brand and audience. Load their voice or brand skills if they exist. Mark mock content as an assumption.
- **Finished.** No placeholders, TODOs, broken links or fake data.
- **One minute.** The user sees the winner and the proof in one minute.
- **Honest.** You named one weak point.

## Output

### Prompt mode

One line with the goal beyond the goal. Then the rewritten prompt in one fenced block, in the user's voice, ending with the judge and what a pass looks like. At most 3 lines on what you raised and skipped. Stop.

### Task mode

**0. Stretch test.** Write the plan for a normal, excellent job. Then name three things beyond it that a human team would skip for cost or politeness. Each must serve selection, coverage, reach or depth. Do the ones that pass "Earned". If you do none, say why on the Skipped line.

**1. Handoff contract.** Put it first, one line per bullet, then start. If nobody can reply, list your assumptions, run, and put open questions in "Needs you". For a small job, keep only Deliver, Judge and Scale.

- **Deliver:** the artefacts and where they will be.
- **Judge:** what proves each one, and what a pass looks like.
- **Scale:** how many variants, cells or formats, and why.
- **Assumptions:** what you could not check.
- **Skipped:** what you left out, and why.
- **Will not do without asking:** spend, deploy, send, delete, or touch anything outside the work area.
- **Stop rule and budget:** pass, no gain, blocked, or a time or compute limit.

**2. The work.**

**3. Delivery report.** In this order:

1. **Verdict.** One line: what you made and whether it passed the judge.
2. **The pick.** The winner, why, and one weak point.
3. **Proof in one minute.** Up to 5 rows: claim, evidence (path, screenshot, log line or test ID), how to recheck (command or link). Link the full matrix.
4. **Browse the rest.** One link to the comparison page, scored table or matrix.
5. **Cut or skipped,** and why.
6. **Needs you.** Decisions, missing access, assumptions, actions that need permission.

Skip empty items. For a small result, merge items 1 to 3 into three lines.

## Examples

**Design.** `/be-unreasonably-ambitious improve this settings screen`
Write briefs with different core ideas (interaction models and structures, not only layouts) until new ones stop being truly different. Build each on a shared base. Run the UI checks on each, and on the original as a known-bad input. Show all on one page at real size, labelled with their briefs. Mark your pick and say why. If the user can reply, let them name parts to combine. If not, merge them yourself and say where each part came from.
Judge: the checks, the page at real screen sizes, then the user's choice.

**Writing.** `/be-unreasonably-ambitious write an article on X`
Draft it. Make several openings, and pick one with a reason. Check every claim against its source, including numbers you wrote yourself. Cut or flag what you cannot verify. Lay it out as a finished page in the user's site style. Make an explainer only if the user names video or social (ask first if it needs a paid tool).
Judge: every claim traced to a source, and the page reads well on a phone.

**Bug.** `/be-unreasonably-ambitious fix this intermittent bug`
Reproduce it and measure the damage. Look for other data it corrupts. Build a harness that fails before the fix. Time one cell, then size the matrix to finish in minutes. Try to break the fix with the tool that fits the cause. List what you cannot see. Ask before any change to production.
Judge: the harness fails before the fix and passes after, and the matrix is complete.

**Restraint.** `/be-unreasonably-ambitious fix the typo in the README`
Fix it. Search the repo for the same typo. Report in two lines, and say the task did not need more.

## Failure modes

- **The timid job.** A normal job with a long report on top, justified by "taste" or "Earned".
- **Quota thinking.** Hitting a number with clones.
- **Mode collapse.** Variants from one context that converge.
- **Proof theatre.** Evidence that does not show the claim.
- **The oversized first run.** A slow grid, not timed first.
- **Ceremony.** A full contract and six-part report for a small result.
- **The dump.** All the output, no winner, no proof, no map.
