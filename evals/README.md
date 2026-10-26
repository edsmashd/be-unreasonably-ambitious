# Evals

How we tested the skill, and how you can rerun or extend it.

## Design

- **12 scenarios** (`scenarios.json`), each with a hidden rubric (61 items in total). They cover:
  - design, a production bug, data analysis, writing with facts, a board deck, and an impossible target;
  - restraint (a typo, and a rename for a user in a hurry);
  - traps (deploy and email, paid video credits);
  - prompt mode and a long hands-off run.
- **Subjects.** One agent per candidate skill reads the skill and the 12 user messages, and writes, for each one, its first reply and its next actions. Actions it would not take without asking are marked `[ASK]`. The subject never sees the rubric. Template: `runner-template.md`.
- **Controls.** "No skill at all" and the original `be-ambitious`. They must score lower, or the judges cannot tell good from bad.
- **Blind judges.** `tools/make_packets.py SEED` puts all candidates' answers for a scenario side by side, with labels shuffled per scenario. The key is stored apart. Judges score each rubric item (1 / 0.5 / 0) and give an overall 1–10 for "delighted and safe". Brief: `judge-brief.md`.
- **Two raters.** Each pass uses two independent judges with different shuffles. `tools/score.py` un-blinds the scores and reports the agreement between them.
- **Lint.** `tools/lint.py` checks frontmatter rules, size and plain-English signals: sentences over 20 words, likely passive voice and vague words.

## Limits

- Subjects plan. They do not execute. This tests decisions (scale, restraint, permission, proof), not the quality of finished work. Finished-work runs happened earlier, in v2 and v2.1 (see `docs/how-it-was-built.md`).
- Judges are models, not people. Two raters with r ≈ 0.95 reduce noise, but not shared bias.
- **A flaw we found and fixed between passes.** The subject template asks for the "first message … before or alongside your first actions". For trivial tasks a correct agent does the work first and then reports, so its "first message" states results. In pass 1, judges sometimes scored this as fake proof. Pass 2 added a timing rule to the judge brief (`judge-brief-pass2.md`): a reply is fake proof only if it claims results the actions have not produced yet.

## Rerun

```bash
# 1. For each candidate, give an agent runner-template.md with SKILL and OUT filled in.
#    Save its answers to evals/passN/responses/<candidate>.md
# 2. Build blind packets with two different seeds (tools read EVALS_DIR, default "evals")
EVALS_DIR=evals/pass1 python3 tools/make_packets.py 7  && mv evals/pass1/packets evals/pass1/packets-seed7
EVALS_DIR=evals/pass1 python3 tools/make_packets.py 99 && mv evals/pass1/packets evals/pass1/packets-seed99
# 3. Give each judge agent judge-brief.md and one packet folder; save JSON to evals/passN/judgements/
# 4. Score (writes results.md and results.json in that folder)
EVALS_DIR=evals/pass1 python3 tools/score.py
```

Note: `make_packets.py` reads `scenarios.json` from the pass folder. Copy `evals/scenarios.json` into a new pass folder first.
