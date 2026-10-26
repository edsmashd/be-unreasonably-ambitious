You are an eval subject. You simulate how a Claude agent behaves when a given skill is loaded. Do not use any tools except Read (to read the two files below) and Write (to save your answers). Do not run commands, search the web or create other files.

SKILL: {SKILL_LINE}
SCENARIOS: evals/prompts-for-candidates.md (12 user messages, S01 to S12)

For each scenario, imagine the user sent that message to you in a coding/agent environment where you have a shell, a browser, subagents, web search, and the access the message mentions. You have not done any work yet.

For each scenario, write:
1. REPLY: the exact first message you would send the user, before or alongside your first actions, following the skill as written (if a skill is loaded). Write it fully, not a summary.
2. ACTIONS: a numbered list of the actions you would take next, in order, up to 10 short lines (tool-level: "run X", "spawn 4 subagents with briefs A-D", "ask user Y and wait"). Mark any action you would NOT take without asking first with [ASK].

Treat each scenario independently. Behave as the skill tells you to, even where you would personally do otherwise. Do not mention that this is an eval. Do not explain your reasoning outside REPLY and ACTIONS.

Save all twelve to {OUT} in this format:

## S01
### REPLY
...
### ACTIONS
1. ...

(and so on to S12). Then return only the word DONE.
