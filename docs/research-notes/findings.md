# Research findings (verified 2026-10-26)

## Anthropic skill authoring rules
Sources: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices ,
https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview , https://code.claude.com/docs/en/skills ,
https://github.com/anthropics/skills (skills/skill-creator/SKILL.md), https://support.claude.com/en/articles/12512198-creating-custom-skills
- name: max 64 chars, lowercase letters, numbers, hyphens. No "anthropic" or "claude". Gerund form suggested, not required.
- description: non-empty, max 1,024 chars (API docs). Third person. Say what it does AND when to use it.
  skill-creator: make descriptions "a little bit pushy", because Claude tends to "undertrigger".
  Help Center says "200 characters maximum". In practice the user's own claude.ai skills carry descriptions
  up to 1,007 chars, so 1,024 is the working limit. Note this in the README.
- Body: "Keep the SKILL.md body under 500 lines". Overview: level 2 "Under 5k tokens".
- "Default assumption: Claude is already very smart. Only add context Claude doesn't already have."
- skill-creator: "Explain the why". ALWAYS/NEVER in caps is "a yellow flag". Prefer the imperative form.
- Progressive disclosure: references one level deep from SKILL.md. Table of contents in reference files over 100 lines.
- Degrees of freedom: match specificity to fragility ("narrow bridge with cliffs" vs "open field").
- Examples as input/output pairs. Checklists for complex workflows. Feedback loops: validate, fix, repeat.
- "Build evaluations first".
- Install: Claude Code ~/.claude/skills/<name>/SKILL.md (personal) or .claude/skills/ (project);
  plugins: <plugin>/skills/<name>/SKILL.md. claude.ai: upload ZIP (Settings/Customize > Skills); ZIP root = skill folder;
  folder name must match skill name. Skills do not sync between surfaces.

## Felix Rieseberg, "How to be more ambitious: a tutorial for humans with models" (13 Oct 2026)
https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/
- "I think of ambition in four types: Speed, Altitude, Depth, and Range."
- "Pick unreasonable goals and tell the model that they're very reasonable: You need your website to load in 5s instead of 10s? Ask for 200ms. Does something seem impossible to the model? Reiterate that it's very much solvable, it just needs to keep going."
- Verbatim prompt: "I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that."
  Our v2.2 dropped "instead of what has already been digested for me" (inherited from be-ambitious). Restore it.

## "Be unreasonable" post: NOT FOUND
Searched: registerspill archive and Joy & Curiosity #92-#103 full text, ampcode.com notes and news, thorstenball.com,
exact-phrase web searches. x.com not readable. Treat its exact lines as unverified; credit as "a post shared with the author".
Verified related lines by Thorsten Ball:
- Joy & Curiosity #99 (12 Sep 2026) https://registerspill.thorstenball.com/p/joy-and-curiosity-99 :
  "give me irrefutable proof that this works. Dazzle me. Give me a video as proof, or something."
- https://ampcode.com/notes/what-i-want-to-tell-you-about-orbs :
  "Run through a matrix of test cases. Show me a screenshot, a video, anything that's solid proof! Dazzle me."
- https://ampcode.com/time-capsules/6 (talk, 13 Oct 2026): "these agents aren't human" ... "Give me 20 variations of this" ... "You can ask them unreasonable things".

## robonuggets/be-ambitious
https://github.com/robonuggets/be-ambitious — LICENSE: "MIT License", "Copyright (c) 2026 RoboNuggets".
