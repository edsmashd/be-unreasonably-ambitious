# Examples

Read this file at Step 1 if you are unsure of the size, and at Step 5 to check your output shape. Each example shows an input and the shape of a good output. The counts here are illustrations. Fit the scale to your own input.

## Contents

- Design (task mode)
- Writing (task mode)
- Bug (task mode)
- Repro on a throwaway box
- Prompt mode
- Restraint

## Design

Input: `/be-unreasonably-ambitious improve this settings screen` (a page with five controls).

Output shape:

```
Deliver: comparison page at /out/compare.html, merged final at /out/settings.html
Judge: objective UI checks at 360px and 1280px, plus a blind pick against a written criterion
Scale: a few variants. Five controls cannot support more truly different structures.
       Effort moves to checks and edge cases.
Stop: checks pass on the final, or two passes with no new failure

[work]

Verdict: final passes all UI checks at both widths; the original failed two.
Pick: "one screen, grouped by task" (variant B), header from variant C.
      Weak point: grouping assumes the user knows the task names.
Proof: overflow check, 360px | screenshot /out/b-360.png | npm run check:overflow
       contrast check failed on original | log /out/contrast.log | npm run check:contrast
Browse: /out/compare.html
Needs you: confirm the task names in the grouping.
```

The briefs differ in interaction model and structure, not in colour. Near-duplicates were merged before any build.

## Writing

Input: `/be-unreasonably-ambitious write an article on phone battery myths`.

Output shape:
- Draft the article. Make several openings and headlines. Pick one against a written criterion and say why.
- List every factual claim, including numbers you wrote. Check each against its primary source. Cut or flag the rest. In a test run, this step caught a number the agent had invented.
- Lay out a finished page in the user's site style, and check it on a phone width.
- Make an explainer video only if the user names video or social as a destination. Ask first if it needs a paid tool.

Judge: every claim traced to a source, the page reads well on a phone.

## Bug

Input: `/be-unreasonably-ambitious fix this intermittent bug in the counter`.

Output shape:
- Reproduce it. Measure the loss.
- Build a harness. Time one run. Size the matrix to finish in a few minutes.
- Confirm the harness fails on the unfixed code. Then fix.
- Look for related damage the bug report did not mention. In a test run, this found a second corrupted field.
- Try to break the fix with the tool that fits the cause.
- List what you cannot see (for example, one process or many). Propose a staged rollout. Ask before any change to production.

Judge: the harness fails before the fix and passes after; the matrix has evidence in each cell.

## Repro on a throwaway box

Input: the user gives an SSH key to a throwaway box and asks for the bug to be found and fixed.

Output shape: set up the stack, reproduce the user's setup, show the bug, fix it, run the end-to-end matrix, record a demo. The access covers that box only.

Judge: the recording plus the matrix. The bug appears before the fix and not after.

## Prompt mode

Input: `/be-unreasonably-ambitious rewrite this prompt for my coding agent: "add dark mode"`.

Output shape:

````
Goal beyond the goal: users can read the app comfortably in any light, with no regressions.

```
Add dark mode. Before you build, write short briefs for a few truly different
approaches (system-follow, user toggle, per-screen contrast tuning) and build each
on the same screens. Put them side by side on one page. Then test the winner on
every screen at phone and desktop widths, in both themes. Check contrast, focus
rings and images. Run each check once on the current light theme to prove it can
fail. Done means: every screen passes every check, with a screenshot per cell,
and a command I can run to recheck.
```

Raised: variants, a full screen-by-theme matrix, checks that can fail.
Skipped: a design-token refactor; it does not change the outcome here.
````

## Restraint

Input: `/be-unreasonably-ambitious fix the typo in the README`.

Output:

```
Fixed "recieve" to "receive" in README.md line 12.
Searched the repo: 2 more in docs/setup.md, also fixed. The task needed no more.
```

No contract, no matrix, no report sections. The one cheap extra was the repo-wide search.

Counter-example: the user typed the slash command on a real task, and the agent cited restraint to do a normal job. That is the timid job. See failure-modes.md.
