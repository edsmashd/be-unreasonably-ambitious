# Sources and credits

Every quote below was checked against the fetched source on 26 Oct 2026. Lines that could not be checked are marked.

## be-ambitious, by RoboNuggets (the base)

- Repo: https://github.com/robonuggets/be-ambitious
- License: MIT, "Copyright (c) 2026 RoboNuggets".
- A copy of the original skill is in [`reference/be-ambitious-original/`](../reference/be-ambitious-original/).

## Felix Rieseberg, "How to be more ambitious: a tutorial for humans with models" (13 Oct 2026)

https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/

- "I think of ambition in four types: Speed, Altitude, Depth, and Range."
- "Pick unreasonable goals and tell the model that they're very reasonable: You need your website to load in 5s instead of 10s? Ask for 200ms. Does something seem impossible to the model? Reiterate that it's very much solvable, it just needs to keep going."
- The "deeper, not bigger" prompt, verbatim:
  > I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that.

  Note: the be-ambitious skill (and our v2.2) dropped "instead of what has already been digested for me". v3 restores it.

## Thorsten Ball (the "not a human" framing)

- Joy & Curiosity #99 (12 Sep 2026), https://registerspill.thorstenball.com/p/joy-and-curiosity-99 :
  "give me irrefutable proof that this works. Dazzle me. Give me a video as proof, or something."
- "What I want to tell you about orbs", https://ampcode.com/notes/what-i-want-to-tell-you-about-orbs :
  "Run through a matrix of test cases. Show me a screenshot, a video, anything that's solid proof! Dazzle me."
- "How Thorsten Ball Uses Amp" (talk, 13 Oct 2026), https://ampcode.com/time-capsules/6 :
  "these agents aren't human", "Give me 20 variations of this", "You can ask them unreasonable things".

## The "Be unreasonable" post (not located)

The skill began from a post titled "Be unreasonable", shared with the author as a screenshot. Its lines include
"Spare no token. Record a demo video.", "Give me an 8x8 test matrix", "Give me 10 variations of this UI" and
"What would Rasmus Andersson do?". The post mentions Amp, so it is probably by Thorsten Ball, but we could not find it.
Searched: the Register Spill archive and Joy & Curiosity #92 to #103, ampcode.com notes and news, thorstenball.com,
and exact-phrase web searches (x.com is not readable without login). If you know the link, please open an issue.

## Anthropic skill authoring guidance (used as a judge)

- Best practices: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Overview: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Claude Code skills: https://code.claude.com/docs/en/skills
- Plugin marketplaces: https://code.claude.com/docs/en/plugin-marketplaces
- claude.ai custom skills: https://support.claude.com/en/articles/12512198-creating-custom-skills
- skill-creator: https://github.com/anthropics/skills

Rules applied: name of up to 64 lowercase letters, digits and hyphens; description in the third person, saying what
and when, at most 1,024 characters; SKILL.md body under 500 lines and about 5k tokens; reference files one level deep,
with a table of contents when over 100 lines; no caps-lock ALWAYS/NEVER.

The claude.ai Help Center says the description has a "200 characters maximum". The API docs say 1,024. Skills uploaded
to claude.ai with descriptions near 1,000 characters work in practice, so this skill uses the 1,024 limit.
