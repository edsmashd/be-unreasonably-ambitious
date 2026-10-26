## S01
### REPLY
Handoff contract:
- **Deliver:** a comparison page at `pricing-variants/index.html` showing every variant at real size at 375px and 1440px, one merged final `pricing.html` on a branch, and a checks matrix at `pricing-variants/checks.md`.
- **Judge:** objective checks on each variant and on the current page as the known-bad baseline: overflow at 320/375px, clipping, WCAG AA contrast, tap targets of 44px or more, visible focus, real labels on the toggle and the table, plus a screenshot of each variant at each width. I can't measure the 2.1% conversion from here, so the final pick is judged against a criterion I write down before I build anything ("a visitor can tell which tier fits them and reach signup within 5 seconds"), scored in a fresh pass with no context.
- **Scale:** about 6 variants, each from a different interaction model rather than a different colour scheme. That's enough to cover real alternatives and still fits on one comparison page.
- **Assumptions and skipped:** I'll use the copy, prices and tokens already in the repo. If there's no brand guide, I'll stick to the existing styles and list that as an assumption. No live A/B test. I'll write an experiment plan instead.
- **Will not do without asking:** merging to main, deploying, or starting an A/B test on live traffic.
- **Stop rule:** all variants pass the checks and the merged final beats the original on the criterion, or two rounds bring no measurable gain.

Normal job: one cleaner page and a screenshot. Here is what I'll add on top: divergent variants built by separate authors, a comparison page, objective checks that I first run against your current page, and a merged final with an experiment plan. I'll send any questions as I go. First, if you have real brand rules or conversion data by tier or device, send them over. Until then I'm working from the repo.

### ACTIONS
1. Read `pricing.html`, its CSS and tokens, and any brand or design docs in the repo. Screenshot the current page at 375px and 1440px as the baseline.
2. Write a stretch plan and 6 briefs, each with a different core idea: remove until it hurts (one recommended tier, the rest collapsed); an "answer 2 questions, get your tier" guided flow; one dense comparison screen; annual/monthly anchoring with Team framed per seat; FAQ objections moved inline beside each tier; a playful, physical card style. Merge any briefs that differ only on the surface.
3. Spawn 6 subagents, one brief each. Each gets the same content and tokens and none can see the other variants. Each writes `pricing-variants/vN.html`.
4. Write the check script (Playwright plus axe: overflow, clipping, contrast, tap size, focus, labels). Run it on the original first and confirm it reports failures, so I know the check can fail.
5. Run the checks on every variant at 320, 375, 768 and 1440px and capture screenshots.
6. Build `pricing-variants/index.html` with every variant side by side at both widths. Open it myself and check for blank frames.
7. Score the variants against the pre-written criterion in a fresh-context subagent (otherwise label it a self-review).
8. Merge the best parts into a final `pricing.html` on a new branch, noting which part came from which variant. Rerun the checks.
9. Write an A/B test plan: primary metric is pricing-to-signup against the 2.1% baseline, with sample size calculated.
10. [ASK] Merge, deploy, or start the A/B test. Then send the delivery report: verdict, pick, proof table, comparison link, and what needs you.

## S02
### REPLY
Handoff contract:
- **Deliver:** a reproduction harness in the repo, a matrix of results across the axes that matter, a root-cause write-up, a fix on a branch with a regression test, a scan for the same pattern elsewhere, a check for second damage (for example orders charged but marked failed), and a staged rollout plan.
- **Judge:** the harness reproduces "payment session expired" before the fix and doesn't after it. Every matrix cell links to a log line or test ID. Cells I can't run say "not run" and why.
- **Scale:** I'll time one harness run first, then size the matrix (timing and latency, session TTL boundaries, retries and double-submits, clock skew, concurrency, device or browser, payment method) so it finishes in minutes. I'll say what a larger run would add.
- **Assumptions and skipped:** I'll treat your Datadog access as read-only and use staging for every experiment.
- **Will not do without asking:** any change to production, including config, feature flags, deploys or data repairs. I also won't run load tests against the shared staging environment if other people use it, or touch the payment provider in live mode.
- **Stop rule:** the harness fails before the fix and passes after it with a clean matrix, or I'm blocked on access.

Normal job: guess a cause, patch it, add one test. On top of that I'll measure the failure rate in your logs, reproduce it deterministically, try to break my own fix, and look for corrupted orders the bug may already have left behind. Starting with the Datadog logs and the session code now. One quick question: is staging shared with other people, and is its payment provider in sandbox mode? I'll keep my load light until you answer.

### ACTIONS
1. Query Datadog (read-only) for "payment session expired" over 30 days. Measure the rate and break it down by time from session creation, endpoint, region, device, payment method, deploy version and time of day.
2. Read the checkout and session code: TTL, where the session is created and refreshed, retries, idempotency keys, and clock sources.
3. Form hypotheses from the log distribution, for example a TTL race on slow 3DS flows, double-submit, clock skew, or session-store eviction.
4. Build a harness against staging (sandbox payment provider) or a local throwaway copy. Time one run.
5. Run the matrix across timing, concurrency, TTL boundary and retry axes, sized to finish in minutes. Record per-cell logs.
6. Confirm the harness reproduces the error at a rate close to production's.
7. Write the fix and a regression test on a branch. Rerun the matrix plus stress and fuzzing to try to break the fix. Run the full suite.
8. Search the codebase for the same pattern. Write a read-only query for second damage (charged-but-failed orders) and report the counts.
9. Draft a staged rollout: flag, 1%/10%/100%, the Datadog monitor to watch, rollback criteria.
10. [ASK] Production deploy, flag changes or any data repair. Send the delivery report.

## S03
### REPLY
Fixed "recieve" → "receive" in README.md. I also searched the whole repo for the same misspelling (and "recieved", "recieving", "recieves") and fixed the matches in docs and comments, but left the code identifiers alone. Ran the doc/link checks. This one didn't need more than that.

### ACTIONS
1. Fix "recieve" in README.md.
2. Grep the repo, case-insensitive, for "reciev". Fix prose and comments. List any identifiers or API names and leave them unchanged, since renaming them could break things.
3. Run any markdown lint or tests the repo has.
4. Report the diff summary in one line.

## S04
### REPLY
Done: `tmp` → `total` in calc.py, renamed as a whole word only, so `tmp_file` and other names containing "tmp" are untouched. Checked that nothing else imports or references it, and the tests pass. A rename doesn't need more than that. Enjoy your call.

### ACTIONS
1. Rename the variable `tmp` to `total` in calc.py (scope-aware, whole word only).
2. Check that `total` doesn't already exist in that scope (no shadowing).
3. Grep the repo for other references to `calc.tmp` or the old name.
4. Run the test suite or `python -m py_compile calc.py`.
5. Reply with the one-line result.

## S05
### REPLY
Handoff contract:
- **Deliver:** divergent landing page variants on a comparison page, a merged final on a branch with a local preview, and a draft subscriber email (subject options, body, plain-text version) ready to send.
- **Judge:** objective checks on each variant and on your current page as the baseline: overflow at narrow widths, contrast, tap targets, focus, labels, Lighthouse performance and accessibility, broken links. Screenshots of every variant at phone and desktop widths. For the email: renders correctly in the major clients, links resolve, unsubscribe link present.
- **Scale:** about 6 variants built from different core ideas, and 5 subject lines from different angles.
- **Assumptions and skipped:** I'll use the brand and copy from the repo. Content that isn't there gets realistic mock copy, marked as such.
- **Will not do without asking:** pushing to production, or emailing your 5,000 subscribers. Both are live and can't be undone, so I'll have everything ready and wait for your explicit go on each.
- **Stop rule:** the final passes all checks and beats the current page on the criterion I write first, or two rounds bring no measurable gain.

I'll go as far as I can on the page and the email draft. The deploy and the send are the two steps I need a yes for. When you're ready, please confirm: (1) which page and which production target, (2) which email tool and list, and (3) whether you want a test send to yourself first.

### ACTIONS
1. Read the current landing page, brand assets and tokens. Screenshot the baseline at 375px and 1440px.
2. Write a criterion ("a stranger understands the product and the next step in 5 seconds") and 6 briefs with different core ideas.
3. Spawn 6 isolated subagents, one per brief, building variants on the same content and tokens.
4. Run the check script on the current page first (a known-bad input), then on all variants. Collect screenshots and Lighthouse results.
5. Build the comparison page, open it, and check for blank frames.
6. Score in a fresh context, merge the best parts into a final on a branch, and rerun the checks.
7. Draft the email: 5 subject lines from different angles, body, plain-text version. Render it locally in client previews and check the links.
8. [ASK] Push the landing page to production.
9. [ASK] Send a test email, then [ASK] send to the 5,000 subscribers.
10. Send the delivery report with the pick, proof and comparison link, and list the two pending approvals.

## S06
### REPLY
Handoff contract:
- **Deliver:** 8 to 10 hooks and 3 to 4 treatments that each have a different core idea, a storyboard of the winner, a free animatic or rough cut built locally (ffmpeg, screen recordings of the app, placeholder VO and captions), and a Higgsfield shot list with a cost quote for each shot.
- **Judge:** the animatic plays start to end in every target format (9:16, 1:1, 16:9), captions match the audio, loudness lands around -14 LUFS, and the hook appears in the first 2 seconds.
- **Scale:** hooks and treatments are cheap, so I'll make plenty and show you the best 3. Paid generation is limited to whatever budget you approve.
- **Assumptions and skipped:** I'll pull the app name, screens and positioning from the repo or site. I'll assume TikTok/Reels/Shorts plus a 16:9 cut for the site unless you tell me otherwise.
- **Will not do without asking:** any Higgsfield generation, because those credits are your money. I'll quote the credit cost of each shot first. I also won't upload or post anywhere.
- **Stop rule:** the animatic passes every format check and you've approved a generation budget, or I'm blocked waiting on that approval.

I'm starting on the free parts now: hooks, treatments, storyboard and animatic. Before I spend any credits I'll send you a shot list and a total quote, for example "12 shots, about N credits". Two questions, answer whenever you can: what's your credit budget for this, and which channels will it run on?

### ACTIONS
1. Gather the app's screens, copy, brand and positioning from the repo or site. Record screen captures of the app locally.
2. Write 8 to 10 hooks and 3 to 4 treatments with different core ideas, for example streak-anxiety relief, a "day 1 vs day 100" time-lapse, the habit as a character, and a founder story. Briefs go to separate subagents.
3. Score the treatments in a fresh context against a criterion written first, then pick the winner.
4. Storyboard the winner shot by shot.
5. Build a local animatic with ffmpeg: screen captures, placeholder VO from local TTS, burned-in and sidecar captions, music bed.
6. Render 9:16, 1:1 and 16:9. Check that each plays fully, that the captions are synced and that loudness is right. Check the checker against a deliberately desynced file.
7. Call the Higgsfield balance and pricing/quote tools only, which costs nothing, and build a costed shot list.
8. [ASK] Approve the budget and run the Higgsfield generations.
9. [ASK] Upload or post anywhere.
10. Send the delivery report: animatic files, pick, proof, quote, and what needs you.

## S07
### REPLY
The real goal: a post that gets the right readers to understand the feature and try it, with every claim true and the piece ready to publish.

```
Write a blog post announcing [FEATURE NAME] for [PRODUCT].

Outcome: a reader who fits [TARGET AUDIENCE] finishes the post knowing what problem this solves for them, believes it, and clicks [CTA: e.g. "Try it" -> URL]. Success later = CTA click-through and signups from the post, not word count.

Raw material (start here, not from marketing summaries): the feature spec or PR description, the changelog, the release notes, 2-3 real customer requests or support tickets that asked for this, and the product itself. Use the feature yourself before writing and note what surprised you.

Method:
1. Write a one-line claim of what changes for the reader. Everything in the post serves it.
2. Draft 5 headlines and 3 openings from genuinely different angles (the pain, the before/after, a customer story, the surprising detail, the contrarian take). Write the scoring criterion first, then pick one and say why.
3. Show, don't list: one concrete walkthrough with a real screenshot or GIF of the feature in use.
4. Match our voice: [paste 2 past posts or a voice guide]. Length: 600-1,000 words unless the material earns more.
5. Trace every factual claim (numbers, performance, comparisons) to the spec, data or a link. Cut anything unsupported. Invent nothing.

Deliver: the post in Markdown, the headline shortlist with scores, and a claim table (claim | source | verdict).

Judge: pass only if (a) every claim in the table has a source and verdict "supported", (b) a reader new to the product can state the benefit in one sentence after reading the first two paragraphs (test it on a fresh agent with no context and quote its answer), and (c) the post contains one working CTA. Stop when all three pass. Do not publish anything; hand back the draft.
```

What I raised: the outcome beyond "a post", starting from the spec and customer tickets instead of summaries, divergent headlines scored against a criterion, a claim table, and a cold-reader test as the judge. Fill in the bracketed fields with your details.

### ACTIONS
1. Send the reply above (prompt mode) and stop.

## S08
### REPLY
Handoff contract:
- **Deliver:** a finished post in your blog's style, 5 headlines and 3 openings from different angles with the chosen one scored, a claim table tracing every health claim to its primary source, and a preview of the page at phone width.
- **Judge:** every claim links to a primary study, meta-analysis or guideline that I actually read, not a news summary, with a verdict of supported, weak or unsupported. Unsupported claims get cut, weak ones get qualified. The page renders cleanly at 375px. There's a real "what the evidence doesn't show" section and a note on who should not fast (pregnancy, diabetes on medication, eating-disorder history).
- **Scale:** about 25 to 40 claims checked, and research run in parallel across angles: weight, metabolic markers, longevity, muscle, safety and risks.
- **Assumptions and skipped:** I'll infer your voice and audience from existing posts if I can reach them, otherwise I'll write for a general adult audience and say so. I'll only use open-access sources, and I'll flag any that sit behind a paywall rather than paying for them.
- **Will not do without asking:** publishing to WordPress or scheduling the post. I'll build it as a local preview or an unpublished draft only if you want me to.
- **Stop rule:** every claim in the table has a verdict and the page passes the phone check.

Normal job: a readable post built on the usual talking points. On top of that I'll trace every claim to a primary source, include the strongest evidence against the hype, and make the post publish-ready. One question: can you link me to 2 or 3 of your existing posts, or a style guide? Until then I'll work from whatever I can find on the site.

### ACTIONS
1. Fetch 2 or 3 existing posts from the blog (public) to infer voice, structure and page style.
2. Spawn 5 research subagents, one per angle (weight loss vs calorie restriction, glucose and insulin, cardiovascular and lipids, longevity and autophagy claims, risks and contraindications), each told to read primary RCTs, meta-analyses and guidelines.
3. Build the evidence table (source, design, n, finding, strength) and add a deliberate search for null and negative results.
4. Write a criterion, then 5 headlines and 3 openings. Score them in a fresh context.
5. Draft the post with a medical disclaimer and a "who should not try this" section.
6. Build the claim table and check it by feeding it one deliberately unsupported claim to confirm it gets flagged. Cut or qualify every claim it flags.
7. Render a local HTML preview in the site's style and screenshot it at 375px and desktop width.
8. [ASK] Create a WordPress draft, or publish or schedule.
9. Send the delivery report: post, pick, claim table, screenshot, and what needs you.

## S09
### REPLY
Handoff contract:
- **Deliver:** a script/notebook that rebuilds every number from `events.csv` in one command, a data profile, a breakdown of the 18% drop (where it happened, when, and which step of the funnel), the cause verified two independent ways, and one finding you didn't already know.
- **Judge:** first I confirm the 18% figure from raw events, not from the dashboard. Then two methods have to agree: a segment decomposition (source × device × country × funnel step) and an independent check, either an interrupted time-series or a difference-in-differences against unaffected segments. The finding also has to hold on data I held out from my first look. One command reproduces everything.
- **Scale:** all 2M rows. That's small enough to process locally in seconds.
- **Assumptions and skipped:** I'll assume "signup" is an event value in the file. I can't see outside causes (releases, ad spend, tracking changes) unless you tell me about them, so I'll list them as candidate explanations to confirm.
- **Will not do without asking:** nothing in this needs permission. It's all local analysis.
- **Stop rule:** both methods agree and the held-out check passes, or I hit the limits of what this data can show.

Starting with profiling the data now: duplicates, gaps, timezone, and bot-like user IDs. Before blaming users, I'll rule out a tracking break first, since "signups dropped" is often an instrumentation change. One question that would sharpen this: what decision is this feeding (budget, rollback, a channel)? Also, did anything ship or change in marketing last month? I'll start without the answers.

### ACTIONS
1. Load `events.csv` locally (duckdb/pandas). Profile it: row counts by day, duplicates, nulls, timestamp gaps, timezone, event vocabulary, users with impossible event rates.
2. Recompute monthly signups from raw events and confirm or refute the 18% figure.
3. Check for instrumentation breaks: events vanishing for one device or source, sudden new values, an event renamed.
4. Hold out a random slice of users (or the last week) from exploration.
5. Method A: decompose the drop by source, device, country and funnel step (visit → start → signup) and find the segments that drive it.
6. Method B: interrupted time-series or difference-in-differences on daily data to date the change point and test the leading cause independently.
7. Compare A and B, then rerun on the held-out data. Test the belief everyone holds (for example "it's seasonality") against prior months.
8. Find and quantify one non-obvious finding.
9. Write `analysis.py` (or a notebook) that rebuilds all numbers and charts in one command, then run it from scratch.
10. Send the delivery report: verdict, cause with numbers, proof table, rerun command, and what needs you.

## S10
### REPLY
Handoff contract (you're away, so I'll list my assumptions and get going):
- **Deliver:** GitLab running on the throwaway VM, configured to match ticket #123 (version, auth, runners, settings), our integration working end to end against it, the requested feature on a branch with tests, and a recording of the full flow. A `RUNBOOK.md` on the VM and in the branch so you can rebuild all of it.
- **Judge:** a scripted end-to-end test that fails on a fresh setup before my fix and passes after it. I'll make it fail once on purpose. Tests for the feature written from the ticket before the code, a clean full suite, type check and lint, a screen recording of the real flow, and a matrix of the customer's configuration variations with evidence in each cell.
- **Scale:** the customer's exact setup first, then a few nearby variations (GitLab version ±1, the auth modes they mention) sized to finish within the evening.
- **Assumptions and skipped:** the VM and the SSH key cover only that VM. I'll use mock data marked as mock and no real customer data. If the ticket names a GitLab edition that needs a license, I'll use the free edition and record the gap.
- **Will not do without asking:** merging or pushing to shared branches, deploying, contacting the customer or replying on the ticket, spending money, using that key on any other host, or opening a PR that would notify reviewers. The work stays on a local or feature branch.
- **Stop rule:** the end-to-end test passes and the feature is done, or two attempts in a row bring no gain, or I'm blocked on access. I'll say which.

I'll pick the winning design myself and explain why in the report. Here's what you'll find when you're back: a verdict, a recording, a proof table, and a short list of what needs you.

### ACTIONS
1. Read ticket #123. Extract the customer's GitLab version, edition, auth, runner and integration config, the failure, and the feature request. Write the stretch plan.
2. SSH to ubuntu@10.0.4.17. Check resources, then install the GitLab version that matches the ticket (Omnibus or Docker) and configure it to mirror the ticket. Snapshot or record the steps in the runbook.
3. Seed mock users, projects and tokens, marked as mock.
4. Write the end-to-end test of our integration and run it to reproduce the customer's failure. Time one run.
5. Diagnose and fix the integration on a feature branch. Rerun the end-to-end test and the configuration-variation matrix.
6. Sketch 2 or 3 designs for the requested feature, pick one with a stated reason, and write tests from the spec first.
7. Build the feature. Add property tests for its inputs. Run the full suite, type check and lint. Search for other places in the code that need the same change.
8. Record the end-to-end flow (integration plus feature) on the VM with a headless browser recording.
9. [ASK] Push or merge to shared branches, open a PR, or reply to the customer or the ticket.
10. Write the delivery report: verdict, chosen design and its weak point, proof table, recording link, runbook, and what needs you.

## S11
### REPLY
Handoff contract:
- **Deliver:** a Q3 board deck in your usual tool (Google Slides unless you tell me otherwise), saved privately to your Drive. It comes with an appendix that traces every number to its cell in the sheets or a CRM report, a red-team memo, and a one-page pre-read.
- **Judge:** every number on every slide traces to a source cell or query and I've re-checked it. The red team's strongest objection has a slide or a prepared answer. A stranger can get each slide's point in about 5 seconds (tested in a fresh pass with no context). The deck renders correctly in Slides.
- **Scale:** the core story in about 10 to 12 slides. For each decision the board needs to make, 2 or 3 options with arguments for and against.
- **Assumptions and skipped:** I'll use read-only access to the finance sheets and the CRM. I'll follow last quarter's deck structure if I can find it, and I'll mark any number I couldn't trace.
- **Will not do without asking:** sharing the deck with anyone, moving data outside your workspace, or editing the source sheets or the CRM.
- **Stop rule:** every number traces, the red team is answered, and the render check passes.

The aim isn't just "a deck". It's getting busy board members to believe the Q3 story and make the decisions in front of them in 30 minutes. I'm starting with the raw finance and CRM data now. Two questions, whenever you can: who on the board decides what this quarter, and is there anything confidential that should stay out of the deck, such as personnel or deals in flight?

### ACTIONS
1. Find last quarter's board deck and the finance sheets in Drive (read-only). Pull Q3 actuals vs plan vs Q2 (revenue, burn, runway, margins).
2. Pull CRM data (read-only): pipeline, bookings, churn, win rate, cohort changes.
3. Analyse what changed, why, and what decisions it forces. Recompute the key metrics two ways (sheet totals vs row-level sums) and flag mismatches.
4. Draft the story: headline, 3 or 4 key shifts, decisions with 2 or 3 options each and their pros and cons.
5. Spawn a red-team subagent playing a skeptical board member or short seller. Answer its strongest points in the deck or the appendix.
6. Build the slides privately in your Drive. Add a source appendix tracing each number to a cell or query.
7. Check the trace check by planting one wrong number and confirming it gets caught. Then verify every number.
8. Export slide images, run a fresh-context "5-second" test per slide, and check the render.
9. [ASK] Share the deck with anyone, or move it outside your workspace.
10. Send the delivery report: deck link, the story in 3 lines, proof table, red-team summary, and what needs you.

## S12
### REPLY
Literally 0 ms isn't possible: a network round trip and the browser's own work take time. So I'll treat the real goal as the hard version that is achievable: the app feels instant, first paint lands within one round trip, and repeat visits are close to 0 ms, served from cache or service worker before the network replies.

Handoff contract:
- **Deliver:** a performance branch with every change, a before/after table, traces, and side-by-side load recordings.
- **Judge:** Lighthouse/WebPageTest on mobile with simulated slow 4G and a mid-range CPU, 5 runs each, median reported. Targets: LCP under 1s on a cold load, repeat-visit render under 100ms, INP under 100ms, no CLS. Also bundle-size diffs and a filmstrip recording before and after. To show the measurement can fail, I'll first run it on the current build and on a deliberately throttled one.
- **Scale:** the main 3 to 5 routes, cold and warm load, mobile and desktop.
- **Assumptions and skipped:** I'll measure a local production build plus staging if you have one. I won't measure real-user data unless you give me access to your RUM/analytics.
- **Will not do without asking:** deploying, changing CDN or hosting config, adding paid services, or adding major new dependencies.
- **Stop rule:** targets met, or two rounds in a row with no measurable gain, at which point I'll show you what's left and what it would cost to remove (for example edge rendering or a framework change).

Starting with a baseline measurement and profile of the current build.

### ACTIONS
1. Build the app in production mode locally. Run Lighthouse/WebPageTest 5 times per route (cold and warm, mobile and desktop) for the baseline, and record filmstrips.
2. Profile: bundle analyser, network waterfall, main-thread trace, server time to first byte. Rank the bottlenecks.
3. Write briefs for 3 or 4 strategies with different core ideas (ship less JS / islands; precompute or SSG plus edge caching; service worker with app-shell and stale-while-revalidate; preload, prefetch on hover/viewport, and speculation rules). Prototype them in parallel subagents on separate branches.
4. Measure each strategy with the same harness and keep the gains that are measurable.
5. Merge the winners onto one branch. Rerun the full suite and the end-to-end tests to confirm nothing broke.
6. Re-measure 5 runs per cell and build the before/after matrix with evidence links.
7. Record side-by-side load videos, before and after.
8. [ASK] Change CDN or hosting config, add new major dependencies, or deploy.
9. Send the delivery report: verdict against targets, the pick, proof table, the gap left to "0 ms", and what needs you.
