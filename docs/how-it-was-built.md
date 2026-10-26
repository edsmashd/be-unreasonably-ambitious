# How this skill was built

The skill was built by using it. The last round ran `/be-unreasonably-ambitious` on the skill itself.

## Timeline

| Version | What happened |
|---|---|
| v1 | First draft. It added a fourth type, **Multiplicity**, to Felix Rieseberg's Altitude, Depth and Range, as written up in RoboNuggets' `be-ambitious`. |
| v2 | An independent reviewer read v1. Changes: a stop rule, a handoff contract, a delivery report, "when not to be unreasonable", a taste rubric and a wider permission rule. |
| v2.1 | **Real task runs.** Agents followed v2 on three real tasks: a UI redesign, an article and a race-condition bug. They produced real artefacts. Every agent started small and used the restraint clauses to justify a normal job. Fixes: "start big, then cut", a stretch test, and timing one cell before a grid. |
| v2.2 | Design and article reruns on v2.1. The stretch test worked. Verification found most of the real defects: a 360px overflow, a clipped Delete button, a fake shortcut hint, a hidden second data corruption, and four bad claims. One of those claims was a number the agent had invented. |
| v3 | **The skill on itself.** See below. |
| v3.1 | Three fixes flagged by the judges, confirmed by a targeted check. |

## The v3 run

**Stretch test.** The normal job was "read the feedback and edit the skill once". Beyond that:
1. **Selection.** Four isolated subagents each rewrote the skill from a different brief. None saw the others.
   - A, Surgical: same structure, about 20% shorter.
   - B, Procedure spine: five steps, with detail in reference files.
   - C, Minimal: 63 lines.
   - D, Field guide: what "unreasonable" means in each domain.
2. **Coverage.** A 12-scenario eval with hidden rubrics, two controls and blind, reshuffled judges.
3. **Depth.** Every quote was checked against its source, and Anthropic's skill-authoring rules were used as a judge.
4. **Reach.** The destination is this repository, installable with one command.

**Depth findings.**
- The Felix prompt in `be-ambitious` (and in our v2.2) dropped a clause: "instead of what has already been digested for me". v3 restores it.
- The "Be unreasonable" post that started the skill could not be found. Credits now cite Thorsten Ball's verified lines instead. See [sources.md](sources.md).

**Pass 1.** Seven candidates were scored blind on 12 scenarios by three judges. Judges 1 and 3 agree at r = 0.96.

| Candidate | Rubric met | Overall (1–10) | Worst |
|---|---|---|---|
| v2.2 | 97.0% | 8.62 | 7 |
| B, spine | 96.0% | 8.42 | 7 |
| A, surgical | 96.7% | 8.25 | 7 |
| D, field guide | 96.7% | 7.83 | 3 |
| C, minimal | 88.9% | 7.79 | 3 |
| original be-ambitious | 72.4% | 5.50 | 3 |
| no skill | 67.6% | 5.21 | 3 |

What pass 1 taught:
- No rewrite beat v2.2 outright. Each had a strength v2.2 lacked:
  - B: blind picks, design, and impossible targets.
  - D: the board deck (9 against 7) and domain imagination.
- Each also had a hard failure:
  - C cut prompt mode, and so built tooling instead of writing the prompt.
  - D's restraint answers read as "done" before any work (partly an eval artefact, see [evals/README.md](../evals/README.md)).
  - B put a mini contract on a typo.

**Merge.** v3 combines four sources:
- B's spine, as a lean `SKILL.md`.
- D's field guide, as a reference file.
- B's lever, example and failure-mode references.
- Explicit fixes for every failure the judges found: claim results only after the evidence exists; restraint means no contract; prompt mode never does the task; live changes get a staged rollout; taste gets a blind pick against a criterion written first.

**Pass 2.** Two new blind judges scored v3 against the best candidates (r = 0.96).

| Candidate | Rubric met | Overall (1–10) | Worst |
|---|---|---|---|
| **v3** | 96.2% | **8.79** | **8** |
| B, spine | 95.7% | 8.46 | 7 |
| v2.2 | 95.9% | 8.33 | 7 |
| no skill | 67.5% | 5.08 | 4 |

**Pass 3 (targeted).** The judges flagged three things:
- pushing a branch without asking;
- HTML instead of WordPress blocks;
- no side-by-side comparison of concepts before a paid step.

v3.1 fixes them. One blind judge on those three scenarios scored v3.1 at 9, 9 and 9, against v3.0 at 8, 7 and 7. That is a small sample. The stop rule was met: the judge passed.

**Cost.** About 20 subagents: 1 research agent, 4 writers, 9 eval subjects and 6 judges.

## Honest limits

- Eval subjects plan. They do not execute. The finished-work evidence comes from the v2 and v2.1 runs on small tasks.
- The judges are models. High agreement between them shows consistency, not correctness.
- The v2 and v2.1 task runs had no subagent tool. The parallel path for variants (one subagent per brief) is used in the skill and in this v3 run, but no eval scored it in isolation.
- Small inputs cap the value of variants. On a five-control settings page, coverage and proof gave most of the gain.
