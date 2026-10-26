---
name: be-unreasonably-ambitious
description: Scales a task past what anyone would ask of a human helper, then proves the result. Builds many truly different variants and picks a winner, runs full test matrices with real evidence in each cell, takes work all the way to its destination format, and runs long hands-off jobs under a short contract. Use it whenever the user types /be-unreasonably-ambitious or says "be unreasonable", "go unreasonable", "overkill this", "spare no token", "dazzle me", "I want irrefutable proof", "test this to hell and back", "give me 20 variations", or "go further than a human would". Also use it when the user wants exhaustive verification or many options rather than one. For ambition that makes the work better but not bigger, use /be-ambitious instead.
license: MIT
metadata:
  author: Edward
  extends: https://github.com/robonuggets/be-ambitious (RoboNuggets, MIT)
  ideas_from: https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/ (Felix Rieseberg)
  inspiration: Thorsten Ball, "these agents aren't human ... You can ask them unreasonable things" (https://ampcode.com/time-capsules/6) and "give me irrefutable proof that this works. Dazzle me." (https://registerspill.thorstenball.com/p/joy-and-curiosity-99)
---

# Be unreasonably ambitious

Extends [be-ambitious](https://github.com/robonuggets/be-ambitious) by RoboNuggets (MIT), built on Felix Rieseberg's [How to be more ambitious](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/). The framing comes from Thorsten Ball: ["these agents aren't human"](https://ampcode.com/time-capsules/6), so ask for ["irrefutable proof"](https://registerspill.thorstenball.com/p/joy-and-curiosity-99).

## The thesis

You are not working with a human. With a human helper, some requests are rude or too costly: ten designs instead of one, a hundred checks instead of five, the article plus the finished page plus the explainer, "test it again and prove it". People do not ask. You have none of those limits. At each step, ask: would I hold back from asking a human for this? If the only reason is cost or politeness, do it.

Real limits stay: physics, access, money, and the user's time. Spend your time to save theirs. Make many, show few. Numbers in this skill are examples of scale, never quotas. Volume earns its place only if it gives a better winner, finds more failures, or takes the work closer to where it is used. Cut the rest.

## Before you start: stretch test

Write the plan for a normal, excellent job in one or two lines. Then name three things beyond it that a human team would skip for cost or politeness. Do each one that changes a decision or can catch a failure. If your final plan fits in one ordinary pass, you did not stretch.

## Rules

1. **Diverge before you generate.** For taste work (design, copy, naming, architecture), write one short brief per variant first. Give each brief a different core idea: a principle, a constraint, or an exemplar's real method. Merge briefs that differ only in colour, size or wording. Build each brief in isolation: a separate subagent if you have one, otherwise a separate pass that does not copy earlier builds. Say in the report if one author made all variants. Build on a shared base so parts merge easily, then merge the best parts yourself and say which part came from where.
2. **Every volume needs a judge.** Variants get a comparison page at real size plus a criterion you wrote before you looked. Coverage gets a matrix: name the axes, run every cell, link real evidence in each cell, mark unrun cells "not run" with the reason. Formats get tested in their real destination. Passes get a score that must improve. The user's eyes judge taste only. Correctness needs a judge outside you and the user.
3. **Make checks that can fail.** A check that has never failed proves nothing. Run each check once on a known-bad input; the user's original is often one. Then try to break your result on purpose.
4. **Time one cell first.** If runs are slow, time one before you size the grid. Pick a size that finishes in minutes. Say what a larger grid would add.
5. **Proof, not claims.** Do not write "it works". Show the screenshot, log line, test ID or recording, with a command to recheck. Open, run or read every artefact in its final form, including the comparison page. Never invent a source, tool, number or result. A missed target with honest evidence is a good result.
6. **Treat the hard target as reasonable, and stop on a rule.** Assume a hard goal is solvable and keep going. Stop when the judge passes, when two passes in a row give no measurable gain (or find no new failure), when you are blocked on access, or when you reach the budget. Report where you stopped and why.
7. **Ambition raises the standard, not the permissions.** Ask first before you spend money (paid APIs, credits, cloud compute), change a live system, send or post anything, delete data, install anything persistent, create accounts, or do anything you cannot undo. Access the user gives covers that target only. Free, local, reversible work: just do it. If you lack access, name what is missing and what it would unlock. If the real test needs an environment, build a throwaway one.

## Restraint

If the task is trivial and one check proves it, or the user says quick or just, do a normal excellent job. Add the one cheap extra that matters most, such as finding the same bug elsewhere. Say in one line that the task did not need more. If the user typed the command on a real task, do not use restraint to shrink it: keep the rigor and the reach, and cut only volume that changes nothing.

## Output

**Contract first.** Open with up to six one-line bullets, then start without waiting, unless a line needs permission. In a one-shot run, list assumptions and put open questions under "Needs you".

- **Deliver:** what you will make and where it will be.
- **Judge:** what proves each item, and what a pass looks like.
- **Scale:** how many variants, cells or formats, and why.
- **Skipped:** what you left out, and why.
- **Will not do without asking:** money, deploys, sends, deletes.
- **Stop rule:** pass, no gain, blocked, or a time or compute budget.

**Delivery report.** In this order, one line each for small results. Skip empty items.

1. **Verdict:** what you made and whether it passed the judge.
2. **Pick:** the winner, why, and one honest weak point.
3. **Proof:** up to five rows of claim, evidence, recheck command. Link the full matrix; do not paste it.
4. **Browse:** one link to the comparison page or folder.
5. **Needs you:** decisions, missing access, assumptions, actions that need permission.

## Example

`/be-unreasonably-ambitious fix this intermittent bug`. Normal job: find the cause, patch it. Stretch: a harness that fails before the fix, a timed matrix of runs across the axes that matter, a deliberate attempt to break the fix. Check that the harness fails on the original code. Ask before any production change. Judge: the harness fails before and passes after, every matrix cell has evidence.

`/be-unreasonably-ambitious fix the typo in the README`. Fix it. Search the repo for the same typo. Report in two lines.
