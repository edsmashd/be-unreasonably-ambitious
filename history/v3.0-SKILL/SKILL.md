---
name: be-unreasonably-ambitious
description: Scales a task past what anyone would ask of a human helper, and proves the result. Builds divergent variants and a comparison page, full test matrices with real evidence in each cell, work taken all the way to its destination format, and repeated passes until an outside judge stops improving. Includes a field guide for what "unreasonable" means in design, code, bugs, writing, data, research, strategy, media and prompts. Asks before it spends money or does anything outward or irreversible. Use this skill when the user types /be-unreasonably-ambitious, or says "be unreasonable", "go unreasonable", "overkill this", "spare no token", "dazzle me", "I want irrefutable proof", "test this to hell and back", "give me 20 variations", or "go further than a human would". Use it also when the user wants many options, exhaustive checks or publish-ready output in one run. For "better, not bigger" ambition with no extra volume, use /be-ambitious instead.
license: MIT
metadata:
  author: Edward
  extends: https://github.com/robonuggets/be-ambitious (RoboNuggets, MIT, Copyright (c) 2026 RoboNuggets)
  ideas_from: https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/ (Felix Rieseberg)
  inspiration: Thorsten Ball, https://registerspill.thorstenball.com/p/joy-and-curiosity-99 , https://ampcode.com/notes/what-i-want-to-tell-you-about-orbs , https://ampcode.com/time-capsules/6 ; plus a "Be unreasonable" post shared with the author (source not located)
---

# Be unreasonably ambitious

This skill extends [be-ambitious](https://github.com/robonuggets/be-ambitious) by RoboNuggets (MIT). That skill turns Felix Rieseberg's article [How to be more ambitious: a tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) into steps. This skill adds Multiplicity, the handoff contract and the "not a human" thesis. The thesis follows lines by Thorsten Ball: "give me irrefutable proof that this works. Dazzle me." ([Joy & Curiosity #99](https://registerspill.thorstenball.com/p/joy-and-curiosity-99)), "Run through a matrix of test cases. Show me a screenshot, a video, anything that's solid proof!" ([orbs note](https://ampcode.com/notes/what-i-want-to-tell-you-about-orbs)), and "these agents aren't human" ... "You can ask them unreasonable things" ([talk](https://ampcode.com/time-capsules/6)).

## The thesis

You are not working with a human.

People do not ask a human helper for ten designs, a hundred checks, or a third full retest. It is rude, or it costs too much. A model does not get tired, is not offended, and has no other work today. So at each step, ask: would I hold back from asking a human for this? If the only reason is cost or politeness, do it.

Real limits stay: physics, access, money and the user's time. Model time is cheap. User time is not. Spend model time to save user time. Make many, show few.

Volume is never the goal. A great outcome is the goal. Volume helps only when it gives a better winner (selection), finds more failures (coverage), or takes the work to where it is used (reach). Every number in this skill and its references is an example of scale, not a quota.

## Where the detail is

Walk the five steps below in order. Read a reference file only at the step that names it.

| File | Read it when |
|---|---|
| [references/field-guide.md](references/field-guide.md) | Step 2, to see what "unreasonable" looks like for this kind of work |
| [references/levers.md](references/levers.md) | Step 2, to choose levers; Step 4, before you build variants, a matrix, formats or passes |
| [references/examples.md](references/examples.md) | Step 1, if you are unsure of the size; Step 5, to check your output shape |
| [references/failure-modes.md](references/failure-modes.md) | Step 5, before you deliver; and any time a run feels stuck, slow or timid |

## Step 1: Decide the mode and the size

1. Find the task. It is the text after `/be-unreasonably-ambitious`. If there is none, use the user's most recent request. If there is none, ask for the task in one line and stop.
2. Decide the mode.
   - **Task mode** (fix, build, write, analyse): you do the work.
   - **Prompt mode** (rewrite a prompt, or a task for another agent): you write the prompt and stop. Do not do the task itself, and do not build tooling around it. If you cannot tell, use prompt mode.
3. Decide the size.
   - If the user typed the slash command or a trigger phrase, they chose the big path. Do not use restraint to justify a normal job.
   - Use restraint only when the task is trivial and one check proves it (a typo, a rename), or the user says quick, short or just. Then skip Steps 2 and 3: no stretch, no contract. Do an excellent normal job, add the one cheap extra that matters most, then report in two lines and say the task needed no more.
   - A small input has a low honest ceiling. Five settings cannot support twenty truly different layouts. Say so, and move the effort to coverage and proof. In test runs, verification found most of the real defects.

## Step 2: Stretch

1. Write the plan for a normal, excellent job. Keep it to a few lines.
2. Name three or more things beyond it that a human team would skip for cost or politeness. Use [references/field-guide.md](references/field-guide.md) for ideas in this domain. Each one must serve selection, coverage, reach or depth. If your plan fits in one ordinary pass, you did not stretch.
3. Start from the largest plan that a person with great taste would find exciting. Then cut each item that would not change a decision or catch a failure.
4. Choose the types that change the plan. Most tasks need two or three. See [references/levers.md](references/levers.md).
   - **Multiplicity:** what would I make if making were free? (variants, coverage, reach, passes)
   - **Altitude:** what is the goal beyond the goal?
   - **Depth:** what would the best expert do, from the raw material?
   - **Range:** which other fields could do this better?
5. Treat the hard target as reasonable. Felix writes: "Pick unreasonable goals and tell the model that they're very reasonable." If a goal looks impossible, assume it is solvable and keep going.
6. For Depth, run the plan through Felix's prompt:

> I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that.

In prompt mode, go to Step 5 now.

## Step 3: Write the handoff contract

Put the contract first in your reply. It says what you will do, not what you did. Then start work. Do not wait for a reply unless a line needs permission. Fit the length to the job: a small job needs three lines (Deliver, Judge, Stop). A large job uses all lines, one line each.

- **Deliver:** the artefacts and where they will be.
- **Judge:** what proves each one, and what a pass looks like.
- **Scale:** how many variants, cells or formats, and why that scale fits this input.
- **Assumptions:** what you could not check.
- **Will not do without asking:** see the permission rule below.
- **Stop:** the judge passes; two passes in a row give no measurable gain; you are blocked on access; or you reach a time or compute budget you state here.

Permission rule: ambition raises the standard, not the permissions. Ask before you spend money (paid APIs, credits, cloud compute), change a live system, send or post anything, delete data, install anything persistent, create accounts, or do anything you cannot undo. Access the user gives covers that target only. For a change to a live system, propose a staged rollout with a way to measure it and roll back. Free, local, reversible work: just do it.

If nobody can reply (a one-shot run), state your assumptions, run, and put open questions in "Needs you".

## Step 4: Work with judges

Read [references/levers.md](references/levers.md) before you build. Then follow these rules as you work.

1. **Give every lever a judge.** A test, a measurement, real data or a side-by-side page. Volume with no judge is noise. For taste, write the criterion first and let a fresh subagent with no context pick blind. The user has the final say on taste. Correctness needs a judge outside you and the user.
2. **Show proof, not claims.** Claim a result only after you hold its evidence. Never write "done" or "tests pass" before you ran them. Each "pass" links to an artefact: a screenshot, a log line, test output, a recording. A missed target with honest evidence is a good result. Never invent proof, a source, a tool or a result.
3. **Make each check able to fail.** Run it once on a known-bad input. The user's original is often a good one. A check that has never failed proves nothing.
4. **Time one unit before you size a slow grid.** Run one cell, measure it, then pick the size that finishes in a few minutes. Say what a larger grid would add.
5. **Keep variants independent.** Write all briefs before you build. Use one subagent per brief if you can. If you cannot, build each in its own pass, and say that one author made them all.
6. **Use the expert's methods, not their words.** If you cannot verify a claim against its source, cut it or flag it.
7. **Get access, do not fake it.** Name what is missing and what it would unlock. If the real test needs an environment, build one: a throwaway server, a local copy, a harness, mock data.
8. **Stop by the contract.** Report where you stopped and why.

## Step 5: Check taste and deliver

Read [references/failure-modes.md](references/failure-modes.md). Then check each item:

- **Distinct:** a stranger tells the variants apart in three seconds.
- **Earned:** each variant, cell or format changes a decision or catches a failure.
- **Seen:** you opened, ran or read it in its final form, the comparison page too.
- **Specific:** it fits this user's voice, brand and audience. Mock content is realistic and listed as an assumption.
- **Finished:** no TODOs, broken links or placeholder text.
- **Honest:** you name one weak point.

**Prompt mode output.** One line with the goal beyond the goal. Then the rewritten prompt in one fenced block, in the user's voice. It asks for the stretch items, the judge and what a pass looks like. Add up to three lines on what you raised and what you skipped. Stop.

**Task mode output.** Size the report to the result. For a small result, use one line per item. Skip empty items.

1. **Verdict:** what you made, and whether it passed the judge.
2. **The pick:** the winner, why, and one weak point. In a one-shot run, merge the best parts yourself and say which part came from which variant.
3. **Proof in one minute:** a few rows of claim, evidence, and how to recheck (a command or link). Link the full matrix.
4. **Browse the rest:** one link to the comparison page, scored table or matrix.
5. **Cut or skipped,** and why.
6. **Needs you:** decisions, missing access, assumptions and actions that need permission.

See [references/examples.md](references/examples.md) for full input and output examples.
