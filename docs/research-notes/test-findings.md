# Evidence from earlier test runs (v2 and v2.1)

Five real task runs by agents that followed the skill (design x2, article x2, bug x1). Small fixtures:
a 5-control settings page, a short phone-battery article, a 3-line race condition in a Python counter.

## What worked
- Proof with recheck commands. Agents produced matrices, logs, screenshots and commands to rerun.
- Verification caught real defects a normal pass would ship: a 360px overflow, a clipped Delete button,
  a fake keyboard-shortcut hint, a hidden second data corruption (by_page), and 4 bad claims in an article,
  one of them a number the agent itself had invented.
- "A check that has never failed proves nothing": running checks on a known-bad input (the user's original)
  exposed a contrast check that could not fail.
- The stretch test (normal plan, then three things a human team would skip) stopped the timid start in v2.1.

## What failed or was weak
- v2: all agents started small and used restraint clauses ("When not to", "Earned", "taste decides") to justify
  a normal job. Self-rated gain: 10-30% over a careful normal pass for about 3x effort.
- Volume levers (variants) added little on small inputs. Verification and coverage gave most of the value.
- Mode collapse risk: test agents had no subagent tool, so all variants came from one author.
- Oversized first run: a bug matrix ran past 10 minutes before the agent cut it.
- Ceremony: the 6-part delivery report and 8-line contract felt heavy for small results.
- One-shot runs: nobody can reply to "let the user name parts to combine"; agents needed a self-merge rule.
- Taste judge without a user: agents had only self-review.
- Example lines anchored behaviour ("eight to twelve briefs" fought the "no quotas" rule; the bug example's
  "debugger, logs, fuzzing" read as a checklist).

## Author's (Edward's) intent, non-negotiable
- Thesis: stop treating models like human assistants. Ask for what would be rude or too costly to ask a human:
  10 designs not 1, 100 checks not 5, the article plus publish-ready page plus explainer, irrefutable proof.
- Not physics-breaking. Not volume for its own sake. Guided by taste. The goal is great outcomes in the process,
  not certain deliverables or certain numbers. Numbers are examples, never quotas.
- Ask before spending money or irreversible/outward actions.
- Keep credit to RoboNuggets (be-ambitious, MIT) and Felix Rieseberg. Inspiration: a "Be unreasonable" post
  (likely Thorsten Ball, Amp).
- Written in plain, simplified technical English (ASD-STE100 style): short sentences, one idea each, active voice.
