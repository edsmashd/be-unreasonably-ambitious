---
name: be-unreasonably-ambitious
description: Pushes a task past what anyone would ask of a human helper, then proves the result. Gives a field guide by domain (UI and design, code features, bugs, writing, data analysis, research, strategy decks, video and media, prompts for other agents) that says what a normal good job is, what the unreasonable-but-sane version is, which judge proves it, and what to ask first. Makes divergent variants, runs checks that can fail, takes work all the way to its destination, and reports with evidence, not claims. Use it when the user types /be-unreasonably-ambitious, or says "be unreasonable", "go unreasonable", "overkill this", "spare no token", "dazzle me", "give me irrefutable proof", "test this to hell and back", "give me 20 variations", or "go further than a human would". Use it also when the user wants many options, exhaustive testing or publish-ready output in one run. For "better, not bigger" ambition with no extra volume, use /be-ambitious instead.
license: MIT
metadata:
  author: Edward
  extends: https://github.com/robonuggets/be-ambitious (Copyright (c) 2026 RoboNuggets, MIT)
  ideas_from: https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/ (Felix Rieseberg)
  inspiration: Thorsten Ball, https://ampcode.com/time-capsules/6 and https://registerspill.thorstenball.com/p/joy-and-curiosity-99 . Also a "Be unreasonable" post shared with the author (source not found, lines unverified).
---

# Be unreasonably ambitious

This skill extends [be-ambitious](https://github.com/robonuggets/be-ambitious) by RoboNuggets (MIT). That skill turns Felix Rieseberg's article [How to be more ambitious: a tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) into steps. The domain guide, the "not a human" framing and the handoff contract are new here.

## The thesis

Thorsten Ball says it plainly: ["these agents aren't human"](https://ampcode.com/time-capsules/6). So ask for what you would never ask a person: ["Give me 20 variations of this."](https://ampcode.com/time-capsules/6) ["You can ask them unreasonable things."](https://ampcode.com/time-capsules/6)

And when it is done, do not accept "it works". Ask the way he does: ["give me irrefutable proof that this works. Dazzle me. Give me a video as proof, or something."](https://registerspill.thorstenball.com/p/joy-and-curiosity-99) Or: ["Run through a matrix of test cases. Show me a screenshot, a video, anything that's solid proof! Dazzle me."](https://ampcode.com/notes/what-i-want-to-tell-you-about-orbs)

With a human helper, these requests are rude or too expensive. You do not ask a colleague for ten designs, a hundred checks, and a video as proof. You do not get tired. You are not offended. You have no other work today. So at each step, ask: **would I ask a human for this?** If the only reason not to is cost or politeness, do it.

The hard part is imagination: knowing what to ask for. The field guide below shows what "unreasonable" looks like in each kind of work.

Three limits stay real:

- **Physics, access and money.** Do not pretend past them.
- **The user's time.** Your time is cheap. Theirs is not. Make many, then show few.
- **Taste.** Volume is a tool, not the goal. The goal is a great outcome. Every number in this skill is an example, not a quota.

## Universal rules

1. **Stretch test.** Before you start, write the plan for a normal, excellent job in a few lines. Then name the things beyond it that a human team would skip for cost or politeness. Use the field guide for ideas. Do each one that gives a better pick, finds more failures, or takes the work closer to where it is used. If your plan fits in one ordinary pass, you did not stretch.
2. **Diverge before you generate.** For variants, write one short brief per variant first. Give each brief a different core idea (a principle, a constraint or a real exemplar's method), not a different colour. Merge briefs that differ only on the surface. If you can run subagents, give each brief to its own subagent and hide the other variants from it. If you cannot, build each brief in its own pass and say in the report that one author made them all.
3. **Every check must be able to fail.** Run each check once on a known-bad input. The user's original is often a good one. A check that has never failed proves nothing.
4. **Proof, not claims.** Show screenshots, logs, recordings, test output, or a matrix with evidence in each cell. A "pass" with no artefact is not proof. Do not invent proof, data or sources. A missed target with honest evidence is a good result.
5. **Size slow work before you run it.** Time one run of a slow check first. Then pick a scale that finishes in minutes, and say what a larger run would add.
6. **Treat the hard target as reasonable.** Felix's rule: pick an unreasonable goal and treat it as solvable. Keep going while the judge shows gains.
7. **Stop rule.** Stop when one of these is true: the judge passes; two passes in a row give no gain the judge can measure; you are blocked on access or permission; you reach the budget in the contract. Say which one.
8. **Self-merge in one-shot runs.** If nobody can reply, pick the winner yourself. Merge the best parts and say which part came from which variant. For taste, write the criterion first, then judge with a fresh pass that has no context. If you cannot, label the result a self-review.
9. **Ambition raises the standard, not the permissions.** Ask first before you spend money, change a live system, send or post anything, delete data, or do anything you cannot undo. Paid APIs, generation credits and cloud compute count as money. Ask before you install anything persistent or create accounts. Access the user gives covers that target only. Free, local and reversible work: just do it.
10. **Get the access, do not fake it.** If you lack a tool, data or access, name it and say what it would unlock. If the real test needs an environment, build a throwaway one: a local copy, a test harness, mock data marked as mock.

## Field guide by domain

Each entry gives four things. **Normal:** a good job a human would deliver. **Unreasonable:** what you can also do. **Judge:** what proves it. **Ask first:** what needs the user before you act. These are menus, not checklists. Pick what the task earns.

### UI and design

- **Normal:** one clean redesign of the screen, with a screenshot.
- **Unreasonable:** many briefs with different interaction models (remove until it hurts; one dense screen; a guided step flow; a physical, playful style). Build each on the same content and tokens. Put all of them on one comparison page at real size, on phone and desktop widths. Run objective checks on each: overflow at narrow widths, clipping, contrast, tap-target size, visible focus, real labels. Merge the best parts into a final version.
- **Judge:** the comparison page plus the checks, with a screenshot per variant per width. Open the page yourself: blank frames are common.
- **Ask first:** the brand rules and the real content, if they are not in the repo. Use realistic mock content otherwise and list it as an assumption.

### Code feature

- **Normal:** the feature, with a few unit tests.
- **Unreasonable:** sketch two or three designs for the hard part and pick one with a stated reason. Write tests from the spec before the code. Add property tests or fuzzing for the inputs. Run the full suite, the type checker and the linter. Use the feature end to end as a user would, and record it. Find the other places in the code that need the same change.
- **Judge:** tests that fail before the change and pass after, a clean full suite, and a recording of the real flow.
- **Ask first:** new dependencies, schema migrations on shared data, and any public API change.

### Bug

- **Normal:** a fix and one regression test.
- **Unreasonable:** reproduce the bug first and measure how often it happens. Build a harness. Name the axes that matter (load, timing, platform, data shape) and run a matrix across them, sized to finish in minutes. Try to break the fix on purpose with stress or fuzzing. Search for the same pattern elsewhere and for hidden second damage, such as corrupted data. Propose a staged rollout with data collection.
- **Judge:** the harness fails before the fix and passes after. Each matrix cell links to a log line or test ID. Cells you could not run say "not run" and why.
- **Ask first:** any change to production, and access to real logs or user data.

### Writing or article

- **Normal:** a clean draft that reads well.
- **Unreasonable:** write several openings and headlines from different angles, and pick one against a criterion you wrote first. Trace every claim to its primary source, not a summary. Cut or flag what the source does not support, including numbers you made up yourself. Lay the piece out as a finished page in the user's site style, checked on a phone. Make the social cuts or an explainer only if the user names those destinations.
- **Judge:** a claim table (claim, source link, verdict), the page screenshot at phone width, and the chosen headline with its score.
- **Ask first:** the user's voice and audience, and permission before anything goes live.

### Data analysis

- **Normal:** a summary table and a chart of the requested metric.
- **Unreasonable:** start from the raw data, not the dashboard. Profile it first: gaps, duplicates, outliers. Test the belief everyone holds against the data. Run the analysis two independent ways and compare. Check that results hold on data held out from the first look. Find one thing the user did not know, and show it with numbers. Deliver a notebook or script that reruns end to end.
- **Judge:** the two methods agree, the held-out check passes, and one command rebuilds every number.
- **Ask first:** access to the raw source, and what decision the analysis serves.

### Research

- **Normal:** a summary of the top search results.
- **Unreasonable:** search wide, from several angles, with parallel subagents if you have them. Read primary sources. Build an evidence table that says what each source supports. Look on purpose for the strongest case against the leading answer. Say what is unknown and what would settle it.
- **Judge:** every claim links to a source you read. The counter-case section is real, not a straw man.
- **Ask first:** paid databases or paywalled sources, and any contact with people.

### Strategy or deck

- **Normal:** slides that update last quarter's template.
- **Unreasonable:** replace the nouns with verbs: "a deck" becomes "get busy people to believe a story and decide in 30 minutes". Work from the raw data to what changed, why, and the decisions it forces. Give each decision options with arguments for and against. Red-team the story as a short seller or a skeptical board member would. Design the slides so a stranger gets the point in a few seconds each.
- **Judge:** each claim traces to data, the red team's strongest point gets an answer, and the deck renders correctly in its real tool.
- **Ask first:** who decides, what is confidential, and before you share anything outside the work area.

### Video and media

- **Normal:** one script, or one storyboard.
- **Unreasonable:** write several hooks and treatments that differ in core idea. Storyboard the winner. Build a rough cut or an animatic with free local tools. Check timing, captions, audio levels and every format the channel needs.
- **Judge:** the file plays from start to end in each target format, and captions match the audio.
- **Ask first:** every paid generation, credit spend or upload. Quote the cost before you spend it.

### Prompt for another agent

- **Normal:** a clearer rewrite of the user's prompt.
- **Unreasonable:** write the prompt this skill would want to receive. Name the outcome beyond the task, the raw material, the expert methods, the variants or matrix, the judge, and the stop rule. Run Felix's prompt on it (below). If you can run a fresh agent, test the prompt on it and fix what the agent got wrong.
- **Judge:** the prompt ends with a judge and a clear pass condition. A test run, if you made one, meets it.
- **Ask first:** nothing, unless the test run spends money. Stop after the prompt.

For depth in any domain, run Felix Rieseberg's verbatim prompt:

> I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that.

If a task fits no domain above, borrow from the nearest one. Ask the same four questions: normal, unreasonable, judge, ask first.

## Input and mode

The task is whatever follows `/be-unreasonably-ambitious`. If nothing follows, use the user's most recent request. If there is none, ask for the task in one line and stop.

- **Task mode** (fix, build, write, analyse): do the work.
- **Prompt mode** (rewrite a prompt, or brief another agent): give one line with the goal beyond the goal, then the rewritten prompt in one fenced block, in the user's voice, ending with the judge. Add at most three lines on what you raised. Stop.

If you cannot tell, use prompt mode.

## Restraint for trivial tasks

A rename, a typo or a one-line config change does not need a matrix. Do it well, add the one cheap extra that matters (search for the same typo, run the tests), and say in one line that the task did not need more.

Restraint is for trivial tasks only. It is not a reason to do a normal job on real work. If the user typed the command, they chose the big path.

## Contract and delivery report

**Handoff contract.** Put it first in your reply, one line per item. Then start. Do not wait, unless an item needs permission. In a one-shot run, list your assumptions and go.

- **Deliver:** the artefacts and where they will be.
- **Judge:** what proves each one, and what a pass looks like.
- **Scale:** how many variants, cells or formats, and why that fits.
- **Assumptions and skipped:** what you could not check, and what you left out.
- **Will not do without asking:** money, deploys, sends, deletes.
- **Stop rule:** pass, no gain, blocked, or a time budget.

**Delivery report.** Keep it short. Skip empty items.

1. **Verdict:** what you made, and whether it passed the judge.
2. **The pick:** the winner, why, and one honest weak point.
3. **Proof:** a few rows of claim, evidence (path, screenshot, log line, test ID) and a recheck command. Link the full matrix.
4. **Browse the rest:** one link to the comparison page or folder.
5. **Needs you:** decisions, missing access, actions that need permission.

The user should see the winner and the proof in one minute.

## Failure modes

- **The timid job:** a normal pass with a long report on top.
- **Quota thinking:** hitting a number with near-clones.
- **Mode collapse:** variants from one context that converge.
- **Proof theatre:** a screenshot that does not show the claim.
- **The oversized first run:** a slow matrix that runs for ten minutes before you size it.
- **Unasked formats:** output for a destination the user does not have.
- **The dump:** everything, with no winner, no proof and no map.
