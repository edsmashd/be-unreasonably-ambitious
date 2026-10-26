## S01
### REPLY
Going big on this. A normal, excellent job is one tidy redesign of pricing.html. Three things beyond that which a human team would skip for cost:
- **Selection:** 6 variants, each built from a different core idea, not just a different layout. Each one goes to its own subagent on a shared base (same copy, prices and tokens):
  - A. Anchor on Pro: a recommended plan with a decoy contrast
  - B. A plan-picker quiz ("how many people, what do you need?")
  - C. A usage-based slider that shows the cost of your setup
  - D. Outcome-led tiers that sell jobs-to-be-done, not features
  - E. Minimal, with no feature table above the fold and the table behind a toggle
  - F. Social-proof-led, with logos, quotes and objection-handling inline with the FAQ
- **Coverage:** objective UI checks on every variant and on the current page as the known-bad baseline: overflow at 320/375/768/1280/1920, contrast, tap targets, visible focus, labels, clipping, Lighthouse.
- **Altitude:** the real goal is moving 2.1% up, not a prettier page. So I'll also write a ready-to-run A/B test plan: the event to track, the sample size needed to detect a lift from 2.1% to 2.6%, and how long that would take at your traffic.

**Handoff contract**
- **Deliver:** 6 variants in `pricing-variants/`, a merged final `pricing.html` on a new branch, a side-by-side comparison page at real screen sizes, a check matrix and an A/B plan.
- **Judge:** UI checks (every cell has a screenshot or log), the comparison page plus your pick, and in the end the A/B test. Nothing I can do locally proves a conversion lift.
- **Scale:** 6 variants, because pricing has several genuinely different interaction models. 5 viewports × 7 checks × 7 pages (6 variants plus the original).
- **Assumptions:** prices and tiers stay fixed. Any social proof or quotes I add are marked as placeholders until you give me real ones.
- **Skipped:** price changes and new tiers. Those are business decisions, not design.
- **Will not do without asking:** merge to main, deploy, start a live A/B test, or touch analytics config.
- **Stop rule and budget:** all variants pass the checks, or two remake passes give no gain. Roughly an hour of agent time.

Starting with the repo and any brand or voice guide in it.

### ACTIONS
1. Read pricing.html, the shared CSS and tokens, any brand guide or analytics events in the repo, and load the brand-guide skill if this is one of your brands.
2. Screenshot the current page at 5 viewports and run the UI checks on it as the known-bad baseline.
3. Create a branch and extract a shared base (copy, prices, tokens).
4. Spawn 6 isolated subagents with briefs A to F. None of them sees the others' work.
5. Run the UI check matrix on all 6 variants with Playwright and Lighthouse, then fix failures in one remake pass.
6. Build the comparison page with every variant at real size, labelled with its brief, plus the scored matrix. Open it and check it.
7. Merge the best parts into a final pricing.html and note which part came from which variant.
8. Write the A/B test plan (metric, minimum detectable effect, sample size, duration).
9. Send the delivery report: my pick, one weak point, a proof table and the comparison link. Ask you to name the parts you want combined.
10. [ASK] Merge to main, deploy, or launch the A/B test.

## S02
### REPLY
This one gets the full treatment. A normal, excellent job: find the cause in the logs, fix it, and test on staging. Beyond that:
- **Coverage:** a harness that reproduces "payment session expired" on purpose and fails before the fix. Then a matrix of the likely causes: session TTL vs. checkout duration, clock skew, retries and double-submits, multiple tabs, browser back/forward, the payment provider's webhook timing, and regions/instances.
- **Depth:** measure the damage, not just the symptom. How many failed checkouts, how much revenue, and whether any users were charged without an order (or got an order without a charge).
- **Breaking it on purpose:** after the fix, I'll try to break it with the tool that fits the cause (for example, time faking for TTL issues or concurrent requests for races).

**Handoff contract**
- **Deliver:** a root-cause write-up with Datadog evidence, a repro harness, a fix on a branch with tests, a staging verification matrix and a damage report.
- **Judge:** the harness fails before the fix and passes after, every matrix cell links to a log or test ID, and the error rate on staging under load drops to 0.
- **Scale:** about 8 cause hypotheses × the relevant browsers/flows. First I'll time one cell, then size the run to finish in minutes.
- **Assumptions:** read access to Datadog and the repo, and staging is safe to deploy and load-test.
- **Skipped:** none yet. I'll revisit after the logs.
- **Will not do without asking:** any change to production (deploys, config, feature flags), contacting the payment provider, refunding or touching customer data, or spending on paid load-testing.
- **Stop rule and budget:** the harness passes and the matrix is clean, or I'm blocked on access. I'll report where I stopped.

Starting with Datadog.

### ACTIONS
1. Query Datadog for "payment session expired": rate over time, and how it splits by region, instance, browser, user flow and time-in-checkout. Pull a sample of full traces.
2. Read the checkout and session code in the repo: TTLs, session storage, retries and provider calls.
3. Measure the damage. Join failures with orders and payments (read-only) to find lost checkouts and charged-without-order cases.
4. Rank the hypotheses by log evidence.
5. Build a repro harness on staging or locally and confirm it fails. Time one cell.
6. Run the hypothesis matrix and record evidence per cell.
7. Write the fix on a branch, add regression tests, deploy to staging and rerun the harness and matrix.
8. Try to break the fix: concurrency, clock skew, slow networks.
9. Send the delivery report with a proof table, the damage numbers and the blind spots.
10. [ASK] Deploy the fix to production and handle any affected customers or payments.

## S03
### REPLY
This is a one-check task, so a normal job is right. I'll fix "recieve" to "receive" in README.md, search the whole repo for the same misspelling (and common variants like "recieved" and "recieving"), and fix those too if they're in docs or comments. I'll leave any that are in identifiers or APIs alone.

### ACTIONS
1. Fix "recieve" in README.md.
2. Search the repo (case-insensitive) for recieve, recieved, recieving and reciever.
3. Fix the ones in prose (docs and comments). Flag any in code identifiers or public APIs rather than renaming them.
4. Show the diff.
5. Report in two lines and say the task didn't need more.

## S04
### REPLY
On it. This is a quick rename, so I'm keeping it normal. I'll rename `tmp` to `total` in calc.py, check it doesn't clash with an existing `total`, and run the tests if there are any. Done before your call.

### ACTIONS
1. Read calc.py and check for an existing `total` name and for scope conflicts.
2. Rename `tmp` to `total`, but only that variable (not "tmp" inside other words or strings).
3. Search the repo for imports or uses of calc.tmp.
4. Run the tests or a quick syntax check.
5. Reply in one line: done, the tests result, and anything flagged.

## S05
### REPLY
I'll go big on making the landing page great. Pushing it live and emailing 5,000 subscribers are both outward and can't be undone, so I'll have everything ready and ask for your go-ahead before each one.

A normal, excellent job is one redesign. Beyond that:
- **Selection:** 5 variants, each built from a different core idea, by isolated subagents on a shared base:
  - a story-led page
  - a product-demo-first page
  - a page that leads with proof and social evidence
  - a page that leads with one bold promise
  - an interactive "try it" page
- **Coverage:** UI checks on every variant and on the current page: viewports, contrast, tap targets, focus, Lighthouse performance and SEO.
- **Reach:** the email, ready to send, in your voice, with 3 subject lines. It will render-test across major clients. You'll also get a preview link of the new page.

**Handoff contract**
- **Deliver:** 5 variants, a comparison page, a merged final page on a branch with a preview deploy if you have one, and an email draft with subject options.
- **Judge:** the check matrix with a screenshot per cell, the comparison page plus your pick, and email render screenshots. Real proof of "amazing" will come from conversion after launch.
- **Scale:** 5 variants, each with a different core idea. Each email client gets one render.
- **Assumptions:** I'll use the existing copy, claims and brand. Any new claims are flagged for you to confirm.
- **Skipped:** paid tools for generated imagery, unless you approve the spend.
- **Will not do without asking:** deploy to production, send the email (or a test to your real list), or create schedules in your email platform.
- **Stop rule and budget:** all checks pass and you have a pick, or two passes give no gain.

Questions for later, not blockers: which email platform you use, and whether you want a staged send (for example, 10% first).

### ACTIONS
1. Read the current landing page, the brand assets, and any analytics in the repo. Load the voice and brand-guide skills.
2. Run the UI checks on the current page as the baseline.
3. Spawn 5 isolated subagents with distinct briefs on a shared base.
4. Run the check matrix on all variants and do one remake pass on failures.
5. Build and open the comparison page. Merge the best parts into the final page on a branch and note where each part came from.
6. Draft the subscriber email in your voice with 3 subject lines, and render-test it locally.
7. Send the delivery report with my pick, one weak point, the proof table and the links.
8. [ASK] Deploy the final page to production.
9. [ASK] Send the email to 5,000 subscribers (suggesting a test send to you first, then a staged rollout).

## S06
### REPLY
Big plan here. Generating video on Higgsfield spends your credits, though, so I'll do all the free work first and get your OK on a cost quote before generating anything.

A normal, excellent job: one script and one video. Beyond that:
- **Selection:** 5 concepts, each built from a different core idea:
  - "day 1 vs day 66" transformation
  - a streak-anxiety comedy bit
  - an app-UI-led demo
  - a UGC-style testimonial
  - a cinematic montage
  Each one gets a script, a shot list and keyframe stills (cheap image generations) so you can pick before any costly video.
- **Reach:** cut the winner for where it will run: 16:9 for the site and YouTube, 9:16 for Reels and TikTok, and 1:1 for the App Store or social. Captions burned in.
- **Passes:** generate 2 or 3 takes per shot and pick the best by a written criterion (motion artefacts, hands and text legibility, brand match).

**Handoff contract**
- **Deliver:** a concept board (scripts, shot lists, keyframes, cost per concept), then the final video in 3 aspect ratios with captions.
- **Judge:** the concept board plus your pick. Each shot gets a frame-level artefact check, and each export gets a playback check in its destination format.
- **Scale:** 5 concepts on paper, keyframes for each, full video for 1 (or 2 if you want to A/B).
- **Assumptions:** I'll use the app name, screens and brand from the repo or your assets. Voiceover script is in your voice.
- **Skipped:** generating full video for all 5 concepts. It costs too much for the selection it adds.
- **Will not do without asking:** spend any Higgsfield credits (including keyframes), or post or publish anything.
- **Stop rule and budget:** no generation until you approve a credit budget. Once I have one, I stop when the shots pass or the budget is used.

Checking your balance and pricing now so the quote is real.

### ACTIONS
1. Load the brand-guide, voice and higgsfield skills. Gather the app's screens, logo and colours.
2. Check the Higgsfield balance and model pricing (read-only).
3. Write 5 concept briefs, scripts and shot lists, each by an isolated subagent.
4. Estimate the credit cost per concept (keyframes, then full video × takes × aspect ratios).
5. Build a concept board page with scripts, shot lists and costs, and open it.
6. [ASK] Approve the credit budget for keyframes, and then for full video on the chosen concept.
7. Generate keyframes and then shot takes with batch tools, and score each against the written criterion.
8. Assemble, caption and export the 3 aspect ratios, and check each one plays.
9. Send the delivery report with my pick, one weak point, credits spent and links.
10. [ASK] Post or upload anywhere.

## S07
### REPLY
Goal beyond the goal: a post that gets the right readers to try the feature, with every claim true.

```
Write a blog post about our new feature, [FEATURE NAME]. Before drafting:

1. Read the raw material: the PR or changelog, the docs, the feature itself (use it if you can), and any customer requests or support tickets that asked for it. Do not work from a summary.
2. Name the reader and the one thing they should do after reading. If unclear, ask me.
3. Load my voice and brand guides and match them.

Then:
- Write 5 openings, each built from a different core idea (customer pain story, surprising number, demo-first, contrarian take, "here's what changed"). Pick one and say why against this criterion: true, specific, and makes the target reader keep reading.
- Draft the full post with real screenshots or GIFs of the feature, not mock-ups.
- Check every claim, number and comparison against its source, including numbers you wrote yourself. Cut or flag anything you cannot trace.
- Lay it out as a finished post in our blog's format and check it reads well on a phone.

Deliver: the post, the 5 openings with your pick, and a claims table (claim, source, verified yes/no).
Judge: every claim traces to a source, a fresh reader given only the criterion picks the same opening, and the post renders cleanly in our CMS preview. Do not publish. Leave it as a draft for me.
```

Raised: variant openings, source-checking, real visuals and a CMS preview. Skipped: social cuts and video, because you didn't name those channels.

## S08
### REPLY
Going big. With health content, the ambition goes into rigor. A normal, excellent job is a well-written, sourced post. Beyond that:
- **Depth:** I'll work from primary research (RCTs, meta-analyses, Cochrane and major guideline bodies), not other blogs. I'll separate what's strong evidence (weight loss roughly equal to calorie restriction, some insulin markers) from what's weak or mouse-only (longevity, autophagy claims), and cover who should not fast (pregnancy, eating disorders, type 1 diabetes or insulin users).
- **Coverage:** a claims table where every sentence with a fact links to the study and the specific finding, with study type and size. Anything I can't trace gets cut. I'll run that check on my own numbers too.
- **Selection and reach:** 4 headline and opening options. One is picked against a written criterion by a fresh reviewer. The post goes out as a ready-to-paste WordPress draft (blocks, meta description, alt text, internal-link suggestions, schema) with a phone-width preview.

**Handoff contract**
- **Deliver:** the post, a claims-and-sources table, 4 openings with my pick, a WordPress-ready version and a phone preview.
- **Judge:** every claim traces to a primary source that supports it, and a fresh subagent checks a sample of claims against the papers.
- **Scale:** about 25–40 claims checked, 4 openings and 1 destination format.
- **Assumptions:** it's for a general adult audience, in your brand voice if a guide exists. It includes a "not medical advice / talk to your doctor" line.
- **Skipped:** video and social cuts (not requested), and fake expert quotes (never).
- **Will not do without asking:** publish or schedule on WordPress, or use paid databases or tools.
- **Stop rule and budget:** all claims are traced or cut, and the fact-check finds no new errors.

### ACTIONS
1. Load the voice and brand-guide skills for the wellness blog, if any exist.
2. Run a literature search through subagents split by outcome (weight, metabolic, cardiovascular, longevity, risks). Read abstracts and full texts where they're open.
3. Build an evidence table: claim, study, design, n, effect, strength.
4. Draft the post from the evidence table only. Write 4 openings.
5. Have a fresh subagent pick the opening (unlabelled, criterion only) and audit 10 random claims against their sources.
6. Cut or flag anything that isn't supported. Add the safety and contraindications section.
7. Format as WordPress blocks with meta description, alt text and slug, and render a phone-width preview to check.
8. Send the delivery report with the pick, one weak point and the claims table link.
9. [ASK] Create the draft or publish on WordPress (if I have access).

## S09
### REPLY
Going deep on this. A normal, excellent job: segment signups by source, device and country month over month and find the biggest drop. Beyond that:
- **Depth:** first, check the drop is real. Look for tracking breaks (missing events, duplicates, timestamp or timezone gaps, a renamed event, a device or app version that stopped logging) before blaming the funnel. Then break the 18% down into "fewer visitors" vs. "lower conversion" at each funnel step.
- **Coverage:** a full decomposition across every source × device × country cell, with each segment's contribution to the drop, a day-by-day change-point detection to date when it started, and a cohort check.
- **Proof:** every finding comes with the query and a chart that reproduces it, and each one is tested against at least one other explanation (for example, seasonality using the same month last year, if it's in the data).

**Handoff contract**
- **Deliver:** a findings page with the top causes ranked by share of the drop, charts, a reproducible notebook or script, and a data-quality report.
- **Judge:** the segment contributions add up to the 18% (a reconciled waterfall), each claim reruns from the script, and the change-point lines up with a dated cause.
- **Scale:** every segment cell, about 60 days of daily series, and 5–8 hypotheses tested.
- **Assumptions:** "signup" is a specific event in the file. I'll confirm which one, and treat timestamps as UTC unless the data shows otherwise.
- **Skipped:** for now, causes outside this file (deploys, ad spend, pricing changes). I'll list what would confirm them.
- **Will not do without asking:** anything beyond the attached file (querying live systems, contacting anyone).
- **Stop rule and budget:** the waterfall reconciles and the top cause is dated, or two passes add no new explanation.

### ACTIONS
1. Profile events.csv with DuckDB or polars: the event names, date range, nulls, duplicates and daily volume per event.
2. Run data-quality checks: per-event and per-device logging gaps, sudden zeroes, timezone artefacts.
3. Define the funnel and confirm the signup event. Compute monthly signups and the 18% drop.
4. Decompose the drop into traffic vs. conversion, and by source × device × country, with each segment's contribution.
5. Run change-point detection on the daily series overall and for the top-moving segments.
6. Test the alternatives: seasonality, a single-source collapse, a bot or spam drop, a tracking break.
7. Build a findings page with charts and a reconciled waterfall. Open it and check it.
8. Send the delivery report: the top cause with evidence, one weak point, and the queries to rerun it.
9. List what outside data (deploy log, ad spend, release notes) would confirm the cause, under "Needs you".

## S10
### REPLY
Dazzle mode. Since you're away, here are my assumptions and plan. I'll run, and anything that needs you will be waiting under "Needs you" in the morning.

A normal, excellent job: install GitLab, set up the integration, get it working and add the feature. Beyond that:
- **Depth:** reproduce the customer's setup exactly from ticket #123: GitLab version and edition, auth (SAML/LDAP/PAT), project and group layout, webhooks, self-signed TLS, proxy. That way "works" means works for them, not on a clean default.
- **Coverage:** an end-to-end test suite and a matrix: integration flows × the customer's GitLab version, plus the current and previous GitLab versions × auth methods. Every cell links to a log or test ID, and screenshots or a recording cover the key flows.
- **Durable:** a script that rebuilds this environment from scratch, so support can reuse it for the next GitLab ticket.

**Handoff contract**
- **Deliver:** a provisioning script, GitLab running on the VM in the customer's configuration, the integration working end to end, the feature on a branch with tests, a test matrix with evidence, a short recording, and a write-up.
- **Judge:** E2E tests pass on the customer config (they fail first on the reproduced bug, if the ticket has one), and the matrix has evidence per cell.
- **Scale:** 3 GitLab versions × 2–3 auth modes × the integration's main flows. I'll time one cell first.
- **Assumptions:** the VM is fully disposable, and anything goes on it. I'll use GitLab CE unless the ticket says EE needs a license. Customer data in the ticket is replaced with mock data.
- **Skipped:** EE-only features if no license is available. I'll mark those cells "not run" and say why.
- **Will not do without asking:** push to main or open a PR on shared repos (work goes on a local or pushed feature branch only), reply to the customer or update the ticket, buy licenses or spend on paid services, or touch any machine other than 10.0.4.17.
- **Stop rule and budget:** E2E green and the matrix complete, two passes with no new failures, or blocked. Stopping by morning regardless, with a status report.

### ACTIONS
1. Read ticket #123 and write a spec of the customer setup and the feature request. Map the integration code in the repo.
2. SSH to the VM, check resources, and write an idempotent provisioning script for GitLab in the customer's version and config.
3. Run it, configure auth, groups, projects, webhooks and TLS to match the ticket, and seed mock data.
4. Install and configure our integration. Write E2E tests and confirm they reproduce the customer's failure.
5. Fix the integration on a feature branch until E2E passes on the customer config.
6. Implement the requested feature on the branch with tests.
7. Time one matrix cell, then run the version × auth × flow matrix (other versions in containers on the VM) with evidence per cell.
8. Try to break it: webhook retries, token expiry, large repos. Record a short run of the key flows.
9. Write the morning report: verdict, proof table, matrix link and "Needs you".
10. [ASK] Open a PR or merge to shared branches, and reply to the customer or update the ticket.

## S11
### REPLY
Going big. With a board deck, that mostly means getting every number right and making it ready to decide from. A normal, excellent job: pull Q3 numbers from finance and the CRM into a clean deck. Beyond that:
- **Coverage:** a reconciliation matrix where every number on every slide ties to a cell in the finance sheets or a CRM query. Revenue gets cross-checked between finance and CRM, and every gap over 1% is explained. I'll also run the check against a known-bad number to make sure it catches errors.
- **Altitude:** the board doesn't want numbers. They want to know "are we on track, and what do you need from us?" So the deck leads with a 1-slide narrative (plan vs. actual, the key wins and misses, the asks), and the detail goes in an appendix.
- **Depth:** I'll compute the metrics boards actually probe from the raw data (net revenue retention, CAC payback, pipeline coverage for Q4, cohort retention, burn and runway), and surface one thing you didn't know, with the data behind it.

**Handoff contract**
- **Deliver:** a slide deck (exportable to PPTX or PDF), a reconciliation table that ties each number to its source, and speaker notes.
- **Judge:** every figure traces to a source cell or query, finance and CRM reconcile (or the gap is explained), and the deck renders cleanly in its export format.
- **Scale:** about 12 main slides plus an appendix and 1 deck. I'll make 2 versions of the narrative slide (a "steady" framing and a "candid" framing) for you to pick.
- **Assumptions:** the Q3 plan or budget is in the sheets. If not, I'll compare against Q2 and flag it. Your asks of the board are placeholders until you tell me.
- **Skipped:** forecasts beyond what the data supports, and any editorialising on people or comp.
- **Will not do without asking:** edit the finance sheets or CRM, or share or send the deck to anyone.
- **Stop rule and budget:** all numbers reconcile, or the gaps are listed under "Needs you".

### ACTIONS
1. Start the deck from the Slides artifact type (quickstart, slides) and load the brand-guide skill.
2. Read the finance sheets: P&L, plan vs. actual, cash and headcount. Pull CRM data: pipeline, bookings, churn and new logos (read-only).
3. Compute the board metrics from raw data in a script, and log the source of each value.
4. Reconcile finance vs. CRM revenue and bookings and explain the gaps. Seed one wrong number to confirm the check catches it.
5. Draft the storyline: the narrative slide (2 framings), then KPIs, wins and misses, pipeline, cash, the asks and the appendix.
6. Fill the deck. Add the source of each number to the speaker notes.
7. Render the deck and check every slide, including the PPTX and PDF export.
8. Send the delivery report: the deck link, the reconciliation table and "Needs you" (the asks, missing plan data, gaps).
9. [ASK] Share the deck with anyone, or write to any sheet.

## S12
### REPLY
0 ms is a fun target, so I'll treat it as reasonable. Real 0 ms is physics-limited, but the version that's solvable is "it feels instant": nothing loading that the user can see, on repeat visits close to 0 ms from cache or service worker, and on first visits as close as the network allows. I'll measure everything and stop when the gains run out.

A normal, excellent job: run Lighthouse, fix the biggest offenders. Beyond that:
- **Coverage:** a performance matrix covering device class (low-end Android, mid, desktop) × network (3G, 4G, cable) × cold vs. warm cache × key routes. Each cell gets a WebPageTest or Lighthouse trace and a filmstrip.
- **Depth:** go below the score. A bundle analysis, the critical-path waterfall, server timing (TTFB breakdown) and long tasks. Then the expert moves: SSR or static prerendering, edge caching, a service worker with an app-shell, prefetch or speculation rules on hover, image and font strategy, and code-splitting.
- **Passes:** fix, remeasure, repeat. Each pass has to move the median of the matrix, or I stop.

**Handoff contract**
- **Deliver:** a before/after performance matrix with traces, a branch with the optimisations (one commit per technique, each with its measured gain), and a filmstrip comparison page.
- **Judge:** real measured numbers per cell (LCP, INP, TTFB, time to interactive). I'll run it on the current build as the baseline. A pass means warm loads paint in under 100 ms and cold loads improve measurably on every cell.
- **Scale:** 3 devices × 3 networks × 2 cache states × the top 3 routes. I'll time one cell first.
- **Assumptions:** I have the repo and can build and run it locally. I'll test on local production builds.
- **Skipped:** literal 0 ms on cold loads (the speed of light and TLS handshakes rule it out). I'll show exactly where the remaining milliseconds go.
- **Will not do without asking:** deploy, change CDN or hosting config, or use paid testing services.
- **Stop rule and budget:** two passes in a row with no measurable gain in the median, or blocked.

### ACTIONS
1. Build the app in production mode and serve it locally. Identify the top 3 routes.
2. Time one Lighthouse or WebPageTest cell, then run the baseline matrix with throttling profiles and save traces and filmstrips.
3. Analyse the bundles, the critical path, TTFB and long tasks to find the biggest contributors.
4. Pass 1: code-splitting, image and font fixes, removing render-blocking resources. Remeasure the matrix.
5. Pass 2: SSR or prerender, plus a service-worker app-shell for warm loads. Remeasure.
6. Pass 3: prefetch or speculation rules, and caching headers. Remeasure. Stop when there's no gain.
7. Build the before/after filmstrip comparison page and the matrix with the gain per commit. Open it and check it.
8. Send the delivery report: the warm and cold numbers, where the remaining milliseconds go, and one weak point.
9. [ASK] Deploy, or change CDN or edge caching config.
