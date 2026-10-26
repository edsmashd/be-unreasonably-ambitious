# Be Unreasonably Ambitious

**A Claude skill that asks for what you would never ask a human helper, and proves the result.**

You do not ask a colleague for ten designs, a hundred checks, a third full retest, and a video as proof. It is rude, or it costs too much. A model does not get tired, is not offended, and has no other work today.

This skill turns that into a method. At each step the agent asks: *would I hold back from asking a human for this?* If the only reason is cost or politeness, it does it. Then it proves the result with evidence you can recheck in one minute.

It is not about volume. Ten weak variants are worse than three strong ones. Every variant, test cell or format must earn its place: a better pick, a failure found, or work taken closer to where it is used. The skill keeps the user's attention as the scarce resource: *make many, show few.*

## What it does

- **Divergent variants.** It writes a different brief for each variant before building any of them, builds each one in isolation, and puts them on one comparison page. A blind pick is made against a criterion written first.
- **Matrices with proof.** It names the axes, times one cell, and sizes the grid to finish in minutes. Each cell links to a log line, a screenshot or a test ID. Each check is first run on a known-bad input, because a check that has never failed proves nothing.
- **Work taken to its destination.** It finds where the work lands (WordPress blocks, the repo, the deck) and finishes it there. It stops at the destination and makes no unasked formats.
- **A handoff contract** for long hands-off runs: what it will deliver, the judge, the scale, assumptions, a stop rule and a budget. Then it starts without waiting.
- **A field guide** for what "unreasonable but sane" means in design, code, bugs, writing, data, research, strategy, media and prompts.
- **Restraint where it belongs.** A typo gets fixed, plus a repo-wide search, in two lines.
- **Permission stays fixed.** "Ambition raises the standard, not the permissions." It asks before spending money, pushing, deploying, sending or deleting.

## Install

**Claude Code (plugin):**

```
/plugin marketplace add edsmashd/be-unreasonably-ambitious
/plugin install be-unreasonably-ambitious@be-unreasonably-ambitious
```

**Claude Code (manual):** copy `plugins/be-unreasonably-ambitious/skills/be-unreasonably-ambitious/` to `~/.claude/skills/` (personal) or to `.claude/skills/` in a project.

**claude.ai:** download `be-unreasonably-ambitious.zip` from [Releases](../../releases). Then upload it under Customize > Skills (Settings > Features on some plans).

Cost: about 340 tokens are always loaded per session (the name and description). About 3,400 more load when the skill fires. Reference files load only at the step that needs them.

## Use

```
/be-unreasonably-ambitious redesign our pricing page
/be-unreasonably-ambitious fix this intermittent checkout bug
/be-unreasonably-ambitious rewrite this prompt for my agent: "Write a blog post about our new feature."
```

As a plugin, the command carries the plugin prefix: `/be-unreasonably-ambitious:be-unreasonably-ambitious`. It also triggers on phrases such as "be unreasonable", "overkill this", "spare no token", "dazzle me", "I want irrefutable proof" and "give me 20 variations".

For ambition that makes the work better but not bigger, use the original [be-ambitious](https://github.com/robonuggets/be-ambitious).

## Evidence

The skill was tested on itself. Four isolated rewrites, the previous version and two controls were scored blind on 12 scenarios with hidden rubrics. The two judges in each pass agree at r = 0.96.

| Version | Overall (1–10) | Worst scenario |
|---|---|---|
| **v3 (this)** | **8.79** | **8** |
| v2.2 (previous) | 8.33 | 7 |
| best single rewrite | 8.46 | 7 |
| no skill | 5.08 | 4 |

The full record has the scenarios, every response, the blind packets, the judgements and the scripts. See [`evals/`](evals/) and [how it was built](docs/how-it-was-built.md), including the limits of this kind of eval.

## Repository

```
plugins/be-unreasonably-ambitious/skills/be-unreasonably-ambitious/   the skill (SKILL.md + references/)
.claude-plugin/marketplace.json                                      plugin marketplace
docs/sources.md                                                      every source, quote-checked
docs/how-it-was-built.md                                             versions, evals, results, limits
evals/                                                               scenarios, responses, judgements, results
tools/                                                               lint, blind packet builder, scorer
reference/be-ambitious-original/                                     the MIT original this extends
history/                                                             v2.2, v3.0 and the four v3 candidates
```

## Credits

- [be-ambitious](https://github.com/robonuggets/be-ambitious) by RoboNuggets (MIT), the base this extends.
- Felix Rieseberg, [How to be more ambitious: a tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/): Speed, Altitude, Depth and Range, and the "deeper, not bigger" prompt.
- Thorsten Ball, for the "not a human" framing: ["give me irrefutable proof that this works. Dazzle me."](https://registerspill.thorstenball.com/p/joy-and-curiosity-99), ["Run through a matrix of test cases"](https://ampcode.com/notes/what-i-want-to-tell-you-about-orbs), ["You can ask them unreasonable things"](https://ampcode.com/time-capsules/6).
- A post titled "Be unreasonable" started this skill. We could not find its source. If you know it, please open an issue.

## License

MIT. See [LICENSE](LICENSE).
