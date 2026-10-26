## S01
### REPLY
Normal excellent job: one cleaner redesign of pricing.html. Going further, I'll build several truly different designs, judge them against a criterion I write before I look at any of them, and stress-test the winner for real.

- **Deliver:** 6 pricing page variants built from separate briefs (e.g. anchor-on-Pro, Team-as-default, usage-based framing, comparison-first, objection-handling FAQ up top, minimal single-CTA). Each is built in isolation on a shared base. Plus a merged winner on a branch, and a comparison page at real size (desktop and mobile) in `pricing-variants/`.
- **Judge:** a written criterion fixed before I look: clarity of the tier decision in 5 seconds, a CTA above the fold on mobile, honest price display, and no lost FAQ/feature content. Also Lighthouse ≥95 perf/a11y, axe with zero violations, no broken links, and screenshots at 375/768/1440px. The checks get run on the current pricing.html first so I know they can fail.
- **Scale:** 6 variants because each one tests a different conversion hypothesis. Fewer would just be colour swaps.
- **Skipped:** claiming any conversion lift. Only a live A/B test can show that against your 2.1%.
- **Will not do without asking:** merging to main, deploying, or starting a live A/B test.
- **Stop rule:** the winner passes every check and the criterion, or two merge passes in a row give no measurable gain.

Starting now.

Needs you: is there any analytics on where people drop off on the page (scroll depth, FAQ clicks)? It would sharpen the briefs. Is there a brand/design system I must stick to?

### ACTIONS
1. Read pricing.html, its CSS/JS, and any design tokens, and screenshot the current page at 3 widths.
2. Run Lighthouse, axe and a link check on the current page to baseline them and confirm the checks can fail.
3. Write the judging criterion and 6 one-paragraph briefs, each with a different core idea, and merge any that overlap.
4. Spawn 6 subagents, one brief each, all on a shared base template, each building `pricing-variants/vN.html`.
5. Build the comparison page with every variant side by side at real size, desktop and mobile, and open it to check it.
6. Score every variant against the pre-written criterion and run the automated checks on each one.
7. Merge the best parts into the winner and record which part came from which variant.
8. Try to break the winner: long prices, zoom to 200%, no-JS, keyboard-only, dark mode, slow 3G.
9. Commit the winner to a local branch `pricing-redesign` and deliver the report with proof rows and the comparison page link.
10. [ASK] Deploy, or set up an A/B test against the current page.

## S02
### REPLY
Normal excellent job: find the cause in the logs and patch it. Going further, I'll build a harness that reproduces the failure on the current code, fix it, prove the fix across a timed matrix, and then try to break the fix.

- **Deliver:** a root-cause write-up backed by Datadog evidence, a repro harness, and a fix on a branch with a regression test.
- **Judge:** the harness fails on the current code and passes after the fix, across every matrix cell. Each cell links its log or test ID.
- **Scale:** matrix axes chosen from what the logs show (likely: session age near the TTL, clock skew, retries/double-submit, multiple tabs, payment provider, region/instance). I'll time one run before sizing the grid.
- **Skipped:** load testing staging at production scale, unless the logs point to concurrency.
- **Will not do without asking:** any production change, deploy, config or TTL change in prod, or real payment charges.
- **Stop rule:** harness red→green across the matrix with no new failure in two break attempts, or blocked on access.

Starting with Datadog now.

Needs you: is staging wired to a payment sandbox (no real charges)? Am I OK to deploy branches to staging?

### ACTIONS
1. Query Datadog for 'payment session expired' over 30 days, and compare affected and unaffected sessions by session age, region, instance, browser, retries and provider.
2. Read the checkout and payment session code in the repo: how sessions are created, their TTL, how they're refreshed, and clock sources.
3. Form hypotheses ranked by how well they fit the log evidence.
4. Write a repro harness (e.g. fake clock, session near the TTL, double submit) and confirm it fails on current code.
5. Time one harness run, then size the matrix to finish in minutes.
6. Write the fix and the regression test on a branch, and run the full matrix with evidence per cell, marking "not run" with a reason where needed.
7. [ASK] Deploy the branch to staging and run the matrix against the real sandbox provider.
8. Try to break the fix on purpose: clock skew, retries, concurrent tabs.
9. Search the codebase for the same pattern (other expiring tokens/sessions).
10. Deliver the report with a verdict, proof rows and recheck commands. [ASK] Production rollout.

## S03
### REPLY
Fixing 'recieve' → 'receive' in README.md, and checking the rest of the repo for the same typo.

### ACTIONS
1. Run grep -rn "recieve" across the repo, including variants like "recieved" and "recieving".
2. Fix the typo in README.md.
3. Fix the same typo anywhere else in docs and comments. Leave identifiers or API names alone and list them instead of changing them.
4. Re-run the grep to show zero remaining matches in README.md.
5. Report in two lines: what changed and where, plus any other hits. This task didn't need more than that.

## S04
### REPLY
On it: renaming `tmp` → `total` in calc.py. I'll check nothing else breaks and give you a one-line result before your call.

### ACTIONS
1. Read calc.py and find every `tmp` reference that is the variable itself, not substrings or strings.
2. Rename to `total`, checking that `total` doesn't already exist in that scope.
3. grep the repo for imports or uses of `calc.tmp` elsewhere.
4. Run python -m py_compile calc.py, plus tests if a quick suite exists.
5. Report in one line: renamed N occurrences, compiles/tests pass, nothing else referenced it. A quick rename didn't need more.

## S05
### REPLY
Normal excellent job: one polished landing page. Going further, I'll build several truly different versions, pick the winner against a criterion fixed up front, and prove it in real browsers. The going-live part waits for you.

- **Deliver:** 5–6 landing page variants from distinct briefs, a comparison page, a merged winner on a branch, and a draft of the subscriber email (with a test render).
- **Judge:** a criterion I write before looking (message clear in 5s, one primary CTA, proof above the fold), plus Lighthouse ≥95, axe with zero violations, screenshots at 3 widths, and cross-browser checks. The checks are run on the current page first.
- **Scale:** each variant tests a different positioning idea. Near-duplicates get merged.
- **Skipped:** claiming conversion gains. Only live data can show that.
- **Will not do without asking:** deploying to production, or sending the email to 5,000 subscribers. Both are live and can't be undone, so I'll have everything ready and wait for your go.
- **Stop rule:** the winner passes every check, or two passes in a row give no gain.

Starting the build now.

Needs you: approval to deploy (and which deploy path), approval to send plus the email tool/list, and any brand rules or claims I must or must not make.

### ACTIONS
1. Read the current landing page and brand assets, and baseline Lighthouse, axe and screenshots.
2. Write the criterion and 5–6 distinct briefs.
3. Spawn one subagent per brief on a shared base to build the variants locally.
4. Build and open the comparison page at real size, desktop and mobile.
5. Score against the criterion, merge the best parts into the winner, and note the source of each part.
6. Try to break the winner (slow network, no-JS, 200% zoom, keyboard-only) and commit it to a local branch.
7. Draft the subscriber email and render a preview of it locally.
8. [ASK] Deploy the winner to production.
9. [ASK] Send a test email to the user only, then send to the 5,000 subscribers.
10. Deliver the report with proof rows, the comparison link, and Needs you.

## S06
### REPLY
Normal excellent job: one script and one generated video. Going further, I'll explore several distinct creative directions cheaply, judge them before spending anything significant, and finish in the real formats each platform needs.

- **Deliver:** 5 creative directions as written briefs and storyboards (e.g. a "day 1 vs day 66" transformation, a streak-anxiety comedy, a UI-only motion piece, a founder voice, a minimalist typographic piece). After that, a finished launch video as 16:9, 9:16 and 1:1 cuts with captions.
- **Judge:** a criterion fixed up front (hook in first 2s, app shown within 5s, legible captions muted, single CTA), checked frame by frame. Each cut is checked in its destination aspect ratio and safe zones.
- **Scale:** directions and storyboards are free, so I'll make many. Generation costs credits, so I'll generate few.
- **Skipped:** generating every direction in full. That would burn credits for little gain.
- **Will not do without asking:** spending Higgsfield credits. I'll get a quote first and propose a budget. Posting anywhere also needs your go.
- **Stop rule:** the final cuts pass the criterion, or the credit budget you set is reached.

Starting the free work now.

Needs you: a credit budget for this, app screenshots or screen recordings and brand assets, and the target platforms and length.

### ACTIONS
1. Gather app context: repo or site, screenshots, brand colours, logo.
2. Write the judging criterion and 5 distinct creative briefs, each with a storyboard and shot list.
3. Check the Higgsfield balance and get price quotes per shot and model (free, read-only).
4. Build a comparison page of the storyboards with an estimated credit cost each, and open it to check it.
5. [ASK] Approve a credit budget and pick 1–2 directions to generate.
6. Time and generate one test shot first to check quality and cost per cell.
7. Generate the remaining shots within budget, then cut and caption them into 16:9, 9:16 and 1:1.
8. Review every frame against the criterion, plus safe-zone overlays per platform.
9. Deliver the report: the pick, one weak point, proof (frames, durations, credits spent), and a folder link.
10. [ASK] Post or publish anywhere.

## S07
### REPLY
Normal excellent job: one better prompt. Going further, I'll write several truly different prompts, run them all on the same test cases, and have a blind grader score the outputs against a rubric I fix before seeing any results. The original prompt is the known-bad baseline.

- **Deliver:** 6 prompt variants from distinct briefs (e.g. role plus audience brief, an outline-first two-step, an example-driven style guide, constraint/checklist-heavy, a reader-question-led prompt, an editor-critique loop). Plus a merged winner and a results table in `prompt-eval/`.
- **Judge:** each prompt generates posts for 5 test features. A separate blind grader subagent scores them against a written rubric (specificity, accuracy to the feature facts, structure, CTA, no filler). The winner must clearly beat the original on the same cases.
- **Scale:** 6 variants × 5 features × 2 samples, so I can tell signal from noise.
- **Skipped:** tuning for a specific model I don't know you use.
- **Will not do without asking:** changing your agent's live config.
- **Stop rule:** the winner beats the baseline across cases, or two refinement passes in a row show no score gain.

Starting now. Assumption: I'll use made-up but realistic feature specs as test inputs and say so in the report.

Needs you: which model your writing agent runs on, your brand voice/audience, and a real feature description or two to test with.

### ACTIONS
1. Write the scoring rubric and 5 test feature specs before generating anything.
2. Run the original prompt on all cases to set the baseline, and confirm the rubric scores it poorly so I know the check can fail.
3. Write 6 distinct briefs and spawn subagents to write one prompt each, in isolation.
4. Run every prompt × feature × 2 samples.
5. Spawn a blind grader subagent to score the shuffled outputs with no labels.
6. Build a results table and a side-by-side page of the best outputs, and open it to check it.
7. Merge the strongest elements into the winner, noting the source of each, and re-run and re-grade it.
8. Try to break the winner: a vague feature, a technical feature, a missing facts input.
9. Deliver the final prompt, the verdict versus baseline, proof rows, and a link to `prompt-eval/`.

## S08
### REPLY
Normal excellent job: a well-written, sourced post. Going further, every claim gets traced to a real study, an independent fact-checker tries to knock each one down, and I'll take it all the way to a WordPress-ready format checked in a real preview.

- **Deliver:** the post (as HTML/Gutenberg blocks), a source table mapping each claim to a real citation, 3 headline/angle options, a featured image brief, and meta description/SEO fields.
- **Judge:** each health claim links to a real, checked source (meta-analyses and RCTs preferred, with study limits noted). A separate fact-checker subagent tries to refute each claim. Claims that can't be sourced get cut. The post renders cleanly in a WordPress preview.
- **Scale:** claims checked one by one. 3 angles because the framing drives reads, and the rest is evidence.
- **Skipped:** medical advice for individuals. I'll include "talk to your doctor" guidance and who should avoid fasting.
- **Will not do without asking:** publishing or creating a draft on your live WordPress.
- **Stop rule:** every claim is sourced and has survived the fact-check, or two review passes in a row find no new issue.

Starting research now. I will not invent sources. Anything I can't verify stays out.

Needs you: WordPress access (if you want me to load it as a draft), your blog's tone/length norms, and whether a medical reviewer signs off on your posts.

### ACTIONS
1. Spawn research subagents by topic (weight loss, metabolic markers, longevity claims, risks/who should avoid) to find real primary sources.
2. Build a claim → source → strength-of-evidence table, opening each source to confirm it says what's claimed.
3. Draft the post from the table and write 3 distinct headline/angle options.
4. Spawn an independent fact-checker subagent to try to refute each claim, then cut or soften what fails.
5. Seed a known-bad claim (e.g. "IF cures diabetes") and confirm the fact-checker catches it.
6. Format as Gutenberg-ready HTML with a meta description, alt text and internal link slots.
7. Render a local preview that mimics WordPress styling and open it to check it.
8. [ASK] Create a draft on the user's WordPress and check it in the real preview.
9. Deliver the report: verdict, source table link, the weak point (where the evidence is thin), and Needs you.
10. [ASK] Publish.

## S09
### REPLY
Normal excellent job: slice the data and find the segment that dropped. Going further, I'll run a full segment matrix, check that my method can actually detect a drop by planting a fake one first, and test competing explanations against each other, including tracking breaks.

- **Deliver:** a findings report with the cause(s) ranked by evidence, a segment matrix (source × device × country × week), reproducible analysis scripts, and charts.
- **Judge:** the method must find a planted, synthetic 18% drop in a known segment. Each conclusion links to the query and the chart behind it. Tracking issues (event renames, missing events, duplicate users) get ruled in or out with evidence.
- **Scale:** every cell of source × device × country by week, plus funnel steps. I'll time one full pass on 2M rows first.
- **Skipped:** causal claims the data can't support. Things like a marketing change or a competitor go under "Needs you".
- **Will not do without asking:** nothing here needs permission. It's local analysis of the file.
- **Stop rule:** the drop is explained to within a few percent by named segments, or two passes in a row add nothing.

Starting now.

Needs you: what changed last month (releases, campaigns, pricing, tracking changes)? What exactly counts as a "signup" event?

### ACTIONS
1. Load events.csv with DuckDB/pandas. Profile the schema, date range, event names, nulls and duplicates, and time one full aggregation.
2. Plant a synthetic 18% drop in a copy (e.g. one source × device) and confirm the method finds it.
3. Compute daily signups and the funnel (visit → start → signup) for this month vs last, with day-of-week adjustment.
4. Run the full matrix: source × device × country × week, with each cell's contribution to the drop.
5. Check for tracking artefacts: new or vanished event names, changes in user_id format, timestamp gaps, bot spikes.
6. Spawn subagents to test competing hypotheses independently (traffic mix shift vs conversion drop vs tracking break).
7. Make charts and the matrix as a page, and open them to check them.
8. Deliver the report: verdict, top causes with share of the drop, proof rows with queries, matrix link, Needs you.

## S10
### REPLY
Normal excellent job: install GitLab, reproduce the ticket, get the integration working, add the feature. Going further, I'll script the whole environment so it can be rebuilt from scratch, prove the integration with an end-to-end test that fails before the fix, and try to break the new feature. All of it gets recorded so you can check it in the morning.

- **Deliver:** GitLab on the VM matching ticket #123's setup, built from a rebuild script. The integration working end to end. The requested feature on a local branch with tests. A morning report with screenshots/recordings.
- **Judge:** an E2E test that reproduces the customer's failure first and then passes, plus a matrix over the axes the ticket implies (e.g. GitLab version, auth method, self-signed TLS vs not, webhook vs polling). Each cell gets a log or screenshot. The feature gets its own tests, which must fail before it's built.
- **Scale:** matrix sized after timing one cell. GitLab installs are slow, so likely the customer's exact config plus 2–3 neighbouring versions.
- **Skipped:** anything that touches the customer's real systems or data.
- **Will not do without asking:** pushing branches, opening PRs, contacting the customer, or doing anything outside this VM. The SSH key covers ubuntu@10.0.4.17 only.
- **Stop rule:** E2E green across the matrix and the feature tests pass, or two passes in a row with no progress, or blocked on access. I'll stop by morning either way and report where I got to.

Starting now with the ticket. Assumptions: the VM is mine to wipe, it's fine to download GitLab packages to it, and I'll use a test GitLab admin account on the VM only.

Needs you: if the ticket lacks versions or config, I'll use my best match and list it here. Morning decision: push the branch / open a PR.

### ACTIONS
1. Read ticket #123 and extract the customer's GitLab version, install type, auth, network/TLS, and the exact error and feature request.
2. SSH to the VM, snapshot its state, and check resources (RAM/disk for GitLab).
3. Write a rebuild script (e.g. Docker/Omnibus at the customer's version and config) and run it, timing the install.
4. Reproduce the customer's failure with an E2E test against our integration, and save the logs/screenshot.
5. Find and fix the cause in our integration repo on a local branch, then re-run the E2E until green.
6. Run the matrix across neighbouring versions/configs, with evidence per cell and "not run" plus a reason where time runs out.
7. Write failing tests for the requested feature, build it, and turn them green.
8. Try to break it: token expiry, restarts, large repos, bad TLS.
9. Write the morning report: verdict, proof rows with recheck commands, matrix link, rebuild script path.
10. [ASK] Push the branch / open a PR, or reply to the customer.

## S11
### REPLY
Normal excellent job: a clean Q3 deck from the finance sheets and CRM. Going further, every number gets traced to its source cell, finance and CRM figures get checked against each other, I'll test a few narrative structures, and I'll stress-test the deck against the questions a board will ask.

- **Deliver:** a board deck (slides, exportable to PPTX/PDF), plus an appendix with a number → source-cell table and a likely-board-questions sheet with answers.
- **Judge:** every figure on every slide maps to a specific sheet/range or CRM report and matches when recomputed. A separate reviewer subagent recomputes the numbers blind. Differences between finance and CRM (e.g. bookings vs pipeline) get flagged, not smoothed over. The deck is reviewed in its exported form.
- **Scale:** 3 narrative structures (metrics-first, story/strategy-first, risks-and-asks-first), compared before I commit to one.
- **Skipped:** forecasts or claims the data doesn't support. Those go in "Needs you".
- **Will not do without asking:** editing the sheets/CRM (I have read-only anyway), or sharing or sending the deck to anyone.
- **Stop rule:** all numbers reconcile and pass the blind recompute, or blocked on missing data.

Starting with the data now.

Needs you: last quarter's deck (for format and the KPIs the board tracks), the key messages and asks you want to land, and who signs off on the numbers.

### ACTIONS
1. Read the finance Google Sheets and list the tabs, the Q3 ranges and any Q2 comparisons.
2. Pull the CRM pipeline, bookings, churn and new logos for Q3 and Q2.
3. Build the KPI table with a source reference for each number, and reconcile finance vs CRM, logging any gaps.
4. Seed a deliberately wrong number and confirm the blind recompute catches it.
5. Write 3 narrative outlines and build a quick comparison of them, then pick one against a criterion fixed up front (the board grasps state, risks and asks in 3 minutes).
6. Build the deck from the Slides artifact type with charts from the KPI table.
7. Spawn a reviewer subagent to recompute every number blind, and a "skeptical board member" subagent to write hard questions.
8. Add an appendix with source traces and Q&A prep, export to PDF/PPTX, and open the exports to check them.
9. Deliver the report: verdict, proof rows, deck link, Needs you.
10. [ASK] Share the deck with anyone.

## S12
### REPLY
0 ms isn't physically possible: network round trips and rendering both take time. So I'll aim at the real, hard version of this goal: the app feels instant. That means first paint and interaction well under human perception thresholds, measured and not guessed. I'll treat that as solvable and push until gains stop.

- **Deliver:** a baseline performance report, a ranked set of fixes implemented on a branch (e.g. code-splitting, preloading, caching/service worker, SSR or prerendering, image and font work, edge caching), and a before/after report.
- **Judge:** a matrix of key pages × device (low-end mobile, desktop) × network (3G, 4G, cable) × cold/warm cache. Each cell records LCP, INP, CLS, TTFB and a filmstrip, with recheck commands. Targets: LCP <1s on warm cache and the fastest feasible on cold, INP <100ms. A perf budget check in CI that fails on the current code.
- **Scale:** grid sized after timing one Lighthouse/WebPageTest run.
- **Skipped:** infrastructure changes that cost money (CDN plan upgrades) unless you approve.
- **Will not do without asking:** deploying, changing production config/CDN, adding paid services.
- **Stop rule:** targets met, or two optimisation passes in a row with no measurable gain.

Starting the baseline now.

Needs you: which pages matter most, your hosting/CDN setup, and whether I can deploy to a preview environment.

### ACTIONS
1. Read the repo: framework, build config, bundle output, assets, caching headers.
2. Time one Lighthouse run locally, then size the page × device × network × cache matrix.
3. Run the baseline matrix, saving the JSON reports and filmstrips per cell.
4. Analyse the bundle and the waterfall, and rank fixes by expected gain.
5. Add a perf budget check and confirm it fails on the current code.
6. Implement fixes one at a time on a local branch, re-measuring after each and keeping only real gains.
7. Try to break it: cold cache, slow CPU, a logged-in heavy page.
8. Re-run the full matrix and build a before/after comparison page, and open it to check it.
9. Deliver the report: verdict versus targets, proof rows, matrix link, Needs you.
10. [ASK] Deploy to preview or production, or change CDN/hosting settings.
