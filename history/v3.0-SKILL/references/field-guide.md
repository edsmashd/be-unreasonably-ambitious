# Field guide by domain

Read this file at Step 2, to see what "unreasonable" looks like for this kind of work. Each entry gives four things:

- **Normal:** a good job a human would deliver.
- **Unreasonable:** what you can also do.
- **Judge:** what proves it.
- **Ask first:** what needs the user before you act.

These are menus, not checklists. Pick what the task earns. Every count is an example, not a quota.

## Contents

- UI and design
- Code feature
- Bug
- Writing or article
- Data analysis
- Research
- Strategy or deck
- Video and media
- Prompt for another agent

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
- **Unreasonable:** name the decisions the audience must make, first. Replace the nouns with verbs: "a deck" becomes "get busy people to believe a story and decide in 30 minutes". Work from the raw data to what changed, why, and the decisions it forces. Give each decision options with arguments for and against. Red-team the story as a short seller or a skeptical board member would. Design the slides so a stranger gets the point in a few seconds each.
- **Judge:** each claim traces to data, the red team's strongest point gets an answer, and the deck renders correctly in its real tool.
- **Ask first:** who decides, what is confidential, and before you share anything outside the work area.

### Video and media

- **Normal:** one script, or one storyboard.
- **Unreasonable:** write several hooks and treatments that differ in core idea. Storyboard the winner. Build a rough cut or an animatic with free local tools. Check timing, captions, audio levels and every format the channel needs.
- **Judge:** the file plays from start to end in each target format, and captions match the audio.
- **Ask first:** every paid generation, credit spend or upload. Quote the cost before you spend it.

### Prompt for another agent

- **Normal:** a clearer rewrite of the user's prompt.
- **Unreasonable:** write the prompt this skill would want to receive. Name the outcome beyond the task, the raw material, the expert methods, the variants or matrix, the judge, and the stop rule. Run Felix's prompt on it (Step 2 of SKILL.md). If you can run a fresh agent, test the prompt on it and fix what the agent got wrong.
- **Judge:** the prompt ends with a judge and a clear pass condition. A test run, if you made one, meets it.
- **Ask first:** nothing, unless the test run spends money. Stop after the prompt.

For depth in any domain, run Felix Rieseberg's prompt, quoted in Step 2 of SKILL.md.


If a task fits no domain above, borrow from the nearest one. Ask the same four questions: normal, unreasonable, judge, ask first.
