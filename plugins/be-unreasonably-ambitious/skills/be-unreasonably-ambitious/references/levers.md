# Levers and their judges

Read this file at Step 2 to choose levers, and at Step 4 before you build. Each lever has its own judge. Pick levers by taste. A lever that changes nothing in the plan is waste.

## Contents

- Multiplicity: variants, coverage, reach, passes
- Altitude: the ladder
- Depth: work from the raw material
- Range: bring in other fields
- When there is no user to judge taste

## Choose the type

| Type | Question | Fits when | Skip when |
|---|---|---|---|
| Multiplicity | What would I make if making were free? | The outcome depends on choosing well, covering many cases, or reaching a destination | One check proves the task |
| Altitude | What is the goal beyond the goal? | The task serves an outcome people care about | The work is its own end |
| Depth | What would the best expert do, from the raw material? | The task should be done really well | Throwaway work |
| Range | Which other fields could do this better? | The result must land with people | A narrow fix with one right answer |

## Multiplicity

Multiplicity is what this skill adds to Felix Rieseberg's types. It has four levers.

### Variants

Use variants for taste problems: design, copy, naming, architecture. On a small input, variants add less than coverage. Make only as many as the input can honestly support.

Diverge before you generate:

1. **Write one short brief per variant.** Give each brief a different core idea: a principle, a constraint or an exemplar. Vary the interaction model, the structure or the tone, not only the layout or the colour. Sample briefs: "Remove until it hurts." "Playful and physical, one accent colour." "Data-dense: everything on one screen." If you name an exemplar, use its real methods, not only its name.
2. **Check the briefs.** If two briefs differ only in colour, size or wording, merge them. Keep writing briefs until new ones stop being truly different. That point is the right count.
3. **Build on a shared base.** Use the same content and the same tokens in every variant. Then the best parts are easy to merge.
4. **Keep the builds independent.**
   - With subagents: give each brief to its own subagent. Do not show a subagent the other variants.
   - Without subagents: write all briefs first. Build each one in its own pass. Do not copy from earlier builds. Say in the report that one author made all variants.
5. **Judge all variants with the same judge.** Then combine the best parts. If the user can reply, let them name parts to combine. In a one-shot run, merge them yourself and say which part came from which variant.

Judge:
- A comparison page with every variant at real size, on the same content, each labelled with its brief. Open it and look. Blank frames are common.
- For UI, add cheap objective checks: overflow at narrow widths, labels, contrast, tap-target size, visible focus, clipping. Run each check on the user's original first. If the original passes a check it should fail, the check is broken.
- For copy, write the criterion first (for example: true, specific, makes a stranger click). See "When there is no user to judge taste" below.

### Coverage

Use coverage for correctness problems: bugs, migrations, compatibility, and facts in text. In test runs, coverage gave most of the value.

For facts:
1. List every factual claim, including the numbers you wrote yourself.
2. Read the source itself, not a summary of it.
3. Cut or flag each claim the source does not support.

For systems:
1. Name the axes. For example: OS, browser, account type, load.
2. Time one cell. Then pick the grid size that finishes in a few minutes. Say what a larger grid would add.
3. Build the grid. Cut a cell only with a stated reason.
4. Run every cell that remains. Each cell links to real evidence: a log line, a screenshot path or a test ID.
5. Mark a cell you could not run "not run", with the reason.
6. Prove each check can fail. Run it on a known-bad input. The unfixed code is often the best one.
7. Try to break the result on purpose. Choose the tools that fit the cause: stress runs, fuzzing, a debugger, or log analysis. These are options, not a checklist.

Judge: the matrix, with evidence in each cell and a summary row.

### Reach

Use reach for work that must land somewhere.

1. Find the destination first: the user's site, channel, repo or deck.
2. Make the formats that destination needs, finished to its standard. A copywriter delivers text. You can deliver the text, the publish-ready page and the explainer, if the destination needs them.
3. Stop at the destination. Do not make formats nobody asked for or will use.
4. Ask first if a format needs a paid tool or publishes anything.

Judge: each format works in its real destination. A page renders on a phone. A video plays. A post fits the channel limits.

### Passes

Use passes for any work the judge can score. Make, critique, remake. Spare no token on passes that improve the work. Spend none on passes that do not.

Stop when the judge passes, or when two passes in a row give no measurable gain. For a pass/fail judge, "no gain" means no new failure found.

Judge: the score improves between passes.

## Altitude

Ask what the user wants to happen next. Build a ladder of three rungs:

1. Deliver the thing, with proof.
2. Serve the decision or the class of problem behind it. For example: find every crash of this kind, not only this one.
3. Make it durable: a workflow that does the job without the user. Ask first if it runs on its own or installs anything persistent.

If a rung has no outside judge, step down one rung.

## Depth

Go one level below the task: to the raw data, the real tools and the underlying problem.

- Use the expert's instruments, not only their words. Where you would reach for a table, a data scientist may reach for a database and a model.
- Test what everyone believes against the raw data.
- Find one thing the user did not know, and show it with data.
- Run the plan through Felix's prompt, quoted in Step 2 of SKILL.md.

## Range

1. Turn the nouns into verbs. "A deck" becomes "get busy people to believe a story and decide in 30 minutes". The verbs show which fields help.
2. Assemble a crew: a field, the job it does, and the tool it uses. For example, a red team of a short seller and a forensic accountant.
3. Do, do not play. Do what the field does, with its tools. Changing the vocabulary without changing the method is role play.
4. With subagents, give each field its own agent and run them in parallel.

## When there is no user to judge taste

Self-review is weak. Make it as honest as you can:

1. Write the criterion before you look at the variants.
2. If you can start a fresh pass or subagent with no context, give it only the criterion and the variants. Let it pick.
3. If you cannot, score each variant against the written criterion. Label the result "self-review" in the report.
4. Add objective checks wherever you can. They do not depend on taste.
