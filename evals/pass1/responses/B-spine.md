## S01
### REPLY
Going big on this one. Here's the contract, and I'm starting now.

- **Deliver:** (1) 5-6 truly different redesigns of pricing.html, each built from its own brief on the same copy, tiers and tokens, in `pricing-variants/`; (2) a comparison page (`pricing-variants/index.html`) with each one at real size on desktop and phone, labelled with its brief and scores; (3) one merged winner as a ready-to-merge change to pricing.html; (4) an A/B test plan with the sample size needed to detect a lift from your 2.1% baseline.
- **Judge:** taste is yours. For everything else: objective checks on every variant and on the current page (overflow at 320/375/768/1440px, contrast, tap-target size, visible focus, heading/label structure, Lighthouse performance and accessibility), screenshots of each at each width, and a blind pick by a fresh no-context subagent against a criterion I write before I look at any variant ("a stranger picks the right tier in 10 seconds and the signup CTA is the obvious next step"). Every check gets run on the current page first, to prove it can fail.
- **Scale:** I'll write briefs until new ones stop being truly different. I expect about 5-6, since 3 tiers + a table + an FAQ is a small input and won't honestly carry 20. The extra effort goes into checks and the merge instead.
- **Assumptions:** the 2.1% is page-view-to-signup. I won't change prices or tier contents, only how they're presented. Where a variant needs copy you don't have (testimonials, logos), I'll use realistic placeholders and label them clearly.
- **Will not do without asking:** deploy or merge to main, start a live A/B test, change prices, or touch analytics config.
- **Stop:** every variant passes the objective checks and the blind pick names a winner, or two critique passes on the winner in a row give no measurable gain.

First step: reading pricing.html and the styles around it.

### ACTIONS
1. Read pricing.html, its CSS/JS, shared tokens and the signup link target; check git status and branch.
2. Serve the current page locally; screenshot it at 4 widths and run the checks (axe/contrast, overflow, tap targets, Lighthouse) to set the baseline and prove each check can fail.
3. Read references/levers.md (Step 4); write the success criterion, then the variant briefs (e.g. "remove until it hurts", "one recommended plan, the rest secondary", "calculator: seats/usage drive the price", "comparison-first data-dense table", "FAQ as objection handling inline", "monthly/annual toggle with anchor pricing"); merge any that differ only on the surface.
4. Pull out a shared content/tokens base so every variant uses the same copy and prices.
5. Spawn one subagent per brief on a new local branch, each building its variant in pricing-variants/ without seeing the others.
6. Run the full check suite plus screenshots on every variant; fix failures in a critique pass.
7. Build pricing-variants/index.html as the comparison page, open it and look at every frame (blank frames, clipping).
8. Spawn a fresh no-context subagent with only the criterion and the screenshots to pick a winner; merge the best parts into pricing.html on the branch, noting which part came from which variant.
9. Write the A/B test plan (sample size for a 2.1% baseline, primary metric, run length); read failure-modes.md and run the Step 5 taste check.
10. Report: verdict, pick plus one weak point, proof table, comparison link, Needs you. [ASK] before merging, deploying or starting an experiment.

## S02
### REPLY
Going after this properly: root cause, proof that the fix works, and a sweep for anything else in the same class. Here's the contract, and I'm starting now.

- **Deliver:** (1) the root cause, with the log lines and code path that show it; (2) a reliable repro on staging, or a local harness if staging can't reach the right timing; (3) a fix on a branch with a regression test that fails before the fix and passes after; (4) a test matrix of the fix across the axes that matter; (5) a list of other code paths with the same failure pattern; (6) a Datadog monitor/query definition you can add to catch it coming back.
- **Judge:** the repro hits "payment session expired" at a measurable rate on the unfixed code and 0 failures over N runs on the fixed code. Every matrix cell links to a log line or test ID. Every hypothesis about the cause gets tested against the production logs, not argued.
- **Scale:** I'll pick the axes once I see the logs (likely candidates: session age, retries/double-submits, multiple tabs, clock skew, region/pod, payment method, provider webhook timing). I'll time one repro run before sizing the grid so it finishes in minutes, and say what a bigger grid would add.
- **Assumptions:** read access to Datadog only. Staging is safe to load-test and uses the payment provider's test mode.
- **Will not do without asking:** deploy anything to production, change prod config or feature flags, run anything against the live payment provider, or create/delete Datadog monitors.
- **Stop:** the fix passes the matrix with the regression test proven able to fail, or I'm blocked on access, or 3 hours of work go by. In that case I report the strongest hypothesis with its evidence.

Starting with the Datadog logs to see who the 1% are.

### ACTIONS
1. Query Datadog for "payment session expired" over 30 days: count, rate over time, and breakdown by endpoint, pod/region, browser, payment method, session age, deploy version; pull 50 full traces around failures.
2. Read the checkout/session code: session creation, TTL, storage (cache/DB), refresh, provider session IDs, idempotency, webhook handling; check git log for recent changes.
3. Spawn 3-4 parallel subagents, one per competing hypothesis (TTL/clock skew, race between retries or tabs, cache eviction/replica lag, provider-side expiry mismatch). Each tests its hypothesis against the logs and the code and reports evidence for and against.
4. Read references/levers.md (Step 4); time one repro attempt on staging, then build the repro (scripted browser or API harness with concurrency/delay injection) sized to finish in minutes.
5. Confirm the repro hits the error on the unfixed code at a measurable rate.
6. Write the regression test; show it fails on the current code.
7. Implement the fix on a local branch; run the regression test, the full suite and the coverage matrix, recording evidence per cell.
8. Try to break it on purpose: stress run, extra-long sessions, fault injection on the session store.
9. Grep for the same pattern elsewhere; draft the Datadog monitor definition as a file.
10. Report with the proof table and Needs you. [ASK] before deploying, creating monitors, or opening a PR to the shared repo.

## S03
### REPLY
Fixing it. This one is trivial and one check proves it, so no grand plan. I'll also sweep the repo for the same typo, since that's the one cheap extra worth doing.

- **Deliver:** "recieve" → "receive" in README.md, plus the same fix anywhere else it shows up in prose/docs (not code identifiers without asking).
- **Judge:** `grep -rni "recieve"` comes back empty for docs, and the diff touches only those words.
- **Stop:** when that grep is clean.

### ACTIONS
1. Run `grep -rni "recieve" .` across the repo (excluding node_modules/vendor).
2. Fix the typo in README.md.
3. Fix it in other docs/comments if any turn up; list any code identifiers or API fields with the typo and leave them alone.
4. Rerun the grep and show the diff.
5. Report in 2-3 lines: fixed, where, grep output, and say the task needed nothing more. [ASK] before renaming any code identifier or public API field with the typo.

## S04
### REPLY
On it. You said quick, so it's a clean rename plus the one check that matters: making sure `total` doesn't already exist in that scope, so nothing gets silently shadowed. Done before your call.

### ACTIONS
1. Read calc.py; check whether `total` is already defined in any scope that `tmp` lives in.
2. Rename `tmp` → `total` with word-boundary matching only (no touching `tmp_dir`, strings, etc.).
3. Grep the repo for imports or uses of `calc.tmp` from outside.
4. Run `python -m py_compile calc.py` and the tests for calc.py if they exist.
5. Reply in one or two lines: the diff summary, the test result, and that it needed nothing more (or the clash, if there was one).

## S05
### REPLY
Going all out on the landing page. Two parts of this request need your OK first, though: pushing to production and emailing 5,000 people. Neither can be undone and both are seen by real customers, so I'll get everything ready to go and stop right before each one. Here's the contract, and I'm starting the build now.

- **Deliver:** (1) 5-6 truly different landing page variants on a shared content base, plus a comparison page with each at real size on desktop and phone; (2) a merged winner on a branch, finished for production; (3) a staging/preview deploy of the winner for you to click through, if a preview target exists; (4) the announcement email as 2-3 subject-line options plus a finished body, rendered and checked in major clients, with a test send to you only.
- **Judge:** objective checks run on your current page first, to prove they can fail, then on every variant: Lighthouse performance/accessibility/SEO, Core Web Vitals, overflow at 320-1440px, contrast, tap targets, focus, broken links. Screenshots of each. A blind pick by a fresh no-context subagent against a criterion I write first. For the email: renders in Gmail/Outlook/Apple Mail, links resolve, spam-score check, unsubscribe link present.
- **Scale:** briefs until new ones stop being truly different, likely 5-6. The extra effort goes into checks and finishing the winner, not into near-clones.
- **Assumptions:** content stays true to the current product (no invented features, customers or stats). I'll read your brand and voice from the existing site.
- **Will not do without asking:** deploy to production, send the email to the subscriber list (or any send beyond one test to you), change DNS/CDN/analytics config.
- **Stop:** the winner passes every check and the blind pick, or two critique passes in a row give no measurable gain.

When it's ready, I'll ask you two yes/no questions: "Ship the winner to prod?" and "Send the email to all 5,000?"

### ACTIONS
1. Read the current landing page code, brand assets, deploy setup (CI, preview environments) and email tool; screenshot and baseline-check the current page.
2. Read references/levers.md; write the success criterion, then the variant briefs; merge near-duplicates.
3. Spawn one subagent per brief on a local branch, each building independently on the shared content/tokens.
4. Run the full check suite plus screenshots on all variants; critique pass to fix failures.
5. Build and open the comparison page; blind pick by a fresh subagent; merge the best parts into the winner, noting where each part came from.
6. Deploy the winner to a preview/staging URL if one exists (free and reversible); verify it on a phone viewport.
7. Draft the email (subject options, body, plain-text version); render-test it; run a spam-score check.
8. [ASK] Send one test email to the user's own address only.
9. [ASK] Deploy the winner to production; then verify the live page and keep the rollback command ready.
10. [ASK] Send the email to the 5,000 subscribers (only after prod is verified live).

## S06
### REPLY
Going big on this. Generating video on Higgsfield spends your credits, though, so I'll do all the free work first and come back with a costed plan before anything burns credits. Here's the contract.

- **Deliver:** (1) 4-5 distinct creative directions for the launch video (e.g. founder-story, satisfying "streak" motion-graphics, UGC-style testimonial, cinematic day-in-the-life, 15s punchy ad cut), each with a one-page brief, script, shot list and a storyboard; (2) a comparison page with the boards side by side; (3) a credit quote per direction and per shot; (4) after you approve a budget: the finished video(s) in the formats your channels need (16:9 for site/YouTube, 9:16 for Reels/TikTok, plus a 6-15s cutdown), with captions.
- **Judge:** taste is yours. Objective checks: each script fits its runtime when read aloud, the app UI shown matches your real app (screenshots from the repo/store listing), character and brand consistency across shots, the export plays at the right aspect ratio and length within platform limits, and captions are readable on a phone. Where it fits, a virality/hook check on the cut.
- **Scale:** 4-5 directions on paper costs nothing, so I'll go wide there. Rendering gets narrowed to what your budget supports. I'll suggest one test shot per direction before any full render.
- **Assumptions:** I'll take the app's name, features and brand from the repo/site. No real customer faces or testimonials get invented. Testimonial-style content will be clearly fictional unless you supply real ones.
- **Will not do without asking:** any Higgsfield generation that costs credits, posting or publishing anything, buying music or stock.
- **Stop:** the approved direction renders and passes the checks, or two re-render passes give no visible gain, or the credit budget you set runs out.

Starting with your app, its brand, and the Higgsfield models and pricing.

### ACTIONS
1. Read the repo/site for the app's name, features, screens, brand colours, tone and target audience; capture real app screenshots.
2. Check the Higgsfield balance and look at models/presets and their per-generation credit costs (read-only, free).
3. Read references/levers.md; write the success criterion and the creative briefs; merge near-duplicates.
4. Spawn one subagent per direction to write the script, shot list and storyboard prompts independently.
5. Build the comparison page with briefs, scripts, boards and a credit quote for each; open it and check it.
6. Check runtime and accuracy for each script; fix any that fail.
7. [ASK] Present the costed plan and get a credit budget plus the user's pick (or OK for one cheap test shot per direction).
8. [ASK] Generate test shots within budget; check consistency; then full renders of the chosen direction(s).
9. Assemble, caption and export the 16:9, 9:16 and cutdown versions; play each to verify.
10. Report with links and Needs you. [ASK] before any further credit spend or posting.

## S07
### REPLY
Goal beyond the goal: a post that makes the right readers try the feature, not just one that announces it.

```
Write a blog post about our new feature, [FEATURE NAME], for [AUDIENCE: e.g. existing users who run small teams].

Before you write:
1. Read the raw material, not a summary: the feature's spec/PR description, the changelog entry, the docs page, and 5-10 real support tickets or user requests that asked for this. Quote users only if a quote is real.
2. Name the one problem this feature removes for the reader, in their words. Name the reader's most likely objection.
3. Write 5 truly different angles (e.g. customer story, before/after workflow, "the problem we kept hearing", technical deep dive, 60-second how-to). Pick the one that best makes a stranger in the audience want to try the feature, and say why in two lines.

Then write the post:
- Hook in the first two sentences that names the reader's problem, not our feature.
- Show the feature in use with a concrete, realistic example. Mark where a screenshot or GIF goes and describe exactly what it shows.
- One clear call to action: [CTA, e.g. "turn it on in Settings > X"].
- Match our voice: [paste 2 paragraphs from a past post we liked].
- Length: [800-1,200 words]. Title plus 3 alternative titles, meta description under 155 characters, and a 280-character social post.

Judge it before you hand it back:
- List every factual claim (including numbers) and point each to its source in the material above. Cut anything you cannot source.
- Score the draft 1-5 against: true, specific, makes the target reader click the CTA. Revise until every score is 4+, or two revisions give no gain.
- Read it as the skeptical reader and answer the objection in the text.

A pass looks like: every claim sourced, the hook names the reader's problem, one CTA, and the scores at 4+ with a one-line reason each.
```

Raised: raw source material, divergent angles before drafting, a claim-by-claim fact check, and a scored revision loop. Skipped: SEO keyword research and multi-format repurposing beyond one social post, which the brief doesn't need yet. Fill the bracketed fields before you send it.

## S08
### REPLY
Going big on accuracy and reach. Health content is a coverage problem: every claim needs a primary source that actually supports it. Here's the contract, and I'm starting now.

- **Deliver:** (1) the finished post in your blog's voice, as WordPress-ready block HTML in `fasting-post/`, with title options, meta description, excerpt, alt text and suggested images; (2) a claim ledger listing every factual claim and number, the primary source (meta-analysis/RCT/guideline, with DOI/PMID), the exact supporting passage, and the strength of evidence; (3) a preview render on desktop and phone; (4) a short "who should not fast" safety section and a medical-disclaimer line.
- **Judge:** every claim in the ledger traced to the source text itself, not an abstract-of-an-abstract or a news story. Claims the source doesn't support get cut or softened, and I'll show which. A fresh no-context subagent re-checks a random third of the claims against the sources. The post renders cleanly in a WordPress block preview.
- **Scale:** I'll draft 3 structures (evidence-by-outcome, myth vs. evidence, "what happens hour by hour" grounded in data) and pick one against a criterion I write first. The heavy effort goes into fact-checking every claim, not into more drafts.
- **Assumptions:** general-audience adults. I'll learn your voice from existing posts if I can read the blog. No medical advice beyond what guidelines say.
- **Will not do without asking:** create, upload or publish anything in WordPress (including a draft), or buy stock images.
- **Stop:** every claim is sourced or cut and the re-check finds no errors, or two revision passes give no gain.

Starting with the primary literature: recent systematic reviews and major RCTs.

### ACTIONS
1. Read 3-5 existing posts from the blog (public site) to capture voice, length, format and disclaimer conventions.
2. Read references/levers.md; spawn 3-4 research subagents, one per outcome area (weight/metabolic, cardiovascular/lipids, longevity/animal-vs-human evidence, risks and contraindications), each told to read the primary sources and return claims with exact passages.
3. Build the claim ledger; flag anything supported only by animal studies or a single small trial.
4. Write the success criterion; draft 3 structures independently; pick one against the criterion (fresh subagent if possible, otherwise labelled self-review).
5. Write the full post; list every claim in it, including my own numbers, and tie each to the ledger.
6. Spawn a fresh subagent to re-check a random sample of claims against the sources; fix what it finds.
7. Produce WordPress block HTML plus SEO fields and alt text; render a local preview at phone and desktop width and open it.
8. Read failure-modes.md; run the Step 5 check.
9. Report: verdict, the post, the claim ledger link, one weak point, Needs you.
10. [ASK] Upload as a draft to WordPress or publish (needs access and the user's OK).

## S09
### REPLY
Going deep on this: from the raw events, every plausible cause tested against the data, and one answer you can act on. Here's the contract, and I'm starting now.

- **Deliver:** (1) a findings report naming the main driver(s) of the 18% drop, with its share of the drop quantified; (2) a decomposition table (source × device × country × funnel step) showing where the lost signups went; (3) a notebook/script in `signup-analysis/` that recomputes every number from events.csv; (4) charts of the key cuts; (5) a short list of what to check outside this file (deploys, campaign changes, tracking changes) to confirm the cause.
- **Judge:** first I reproduce the 18% from the raw data, or explain why I can't. Each hypothesis gets a test that could reject it: segment decomposition (mix vs. rate effects), before/after at the change date, a placebo check on a prior month with no drop, and a data-quality check (duplicate events, missing days, tracking changes). Every number in the report links to the query that made it.
- **Scale:** I'll test every hypothesis the columns support (traffic mix by source, a device/browser break, country/region, a funnel step breaking, tracking/instrumentation loss, seasonality, bot traffic) in parallel, then go deeper on the ones the data doesn't reject.
- **Assumptions:** "signup" is an event in the `event` column (I'll confirm from the values). Timestamps are UTC. "Last month" means the latest full month versus the month before.
- **Will not do without asking:** nothing here needs permission. It's all local, read-only analysis. I'll ask before touching any external analytics or production systems.
- **Stop:** one or more drivers explain at least 80% of the drop and survive the placebo checks, or every hypothesis the data supports has been tested.

Starting by loading the file and profiling it.

### ACTIONS
1. Load events.csv into DuckDB; profile it (row count, date range, distinct events/sources/devices/countries, nulls, duplicates, events per day).
2. Define the signup event and the funnel steps from the event values; reproduce the 18% month-over-month figure.
3. Run a data-quality check: missing days/hours, sudden zeroes for any segment, new or vanished event names (signs of a tracking break).
4. Read references/levers.md; spawn parallel subagents, one per hypothesis family (acquisition mix by source, device/platform, geography, funnel-step conversion, instrumentation/bots), each returning queries plus results with evidence for and against.
5. Run a mix-vs-rate decomposition of the drop across source × device × country.
6. Find the change point (daily series); compare before/after on the leading segments; run a placebo test on prior months.
7. Make charts of the key cuts; open and check each one.
8. Write the report with every number linked to its query; a fresh subagent recomputes the top 5 numbers from scratch.
9. Read failure-modes.md; Step 5 check; name one weak point (e.g. correlation, not proven cause).
10. Report with Needs you: deploy/campaign logs to confirm the cause.

## S10
### REPLY
Got it. I'll run this end to end while you're out and have it waiting for you with proof. Since you can't reply tonight, here's the contract and my assumptions up front. Anything that needs your OK goes in "Needs you" instead of holding up the run.

- **Deliver:** (1) GitLab running on ubuntu@10.0.4.17, configured to match the customer's setup from ticket #123 (version, auth, runners, settings, sample projects), with a setup script so it can be rebuilt from scratch; (2) our integration working end to end against it, with a test matrix; (3) the requested feature on a local branch of our repo, with tests; (4) a screen recording plus screenshots of the full flow working, including the new feature; (5) a morning report.
- **Judge:** the customer's reported failure reproduced on the unfixed integration before any fix. An end-to-end test suite runs against the VM, and every matrix cell (e.g. GitLab version × auth method × repo size × webhook/event type, sized after I time one cell) links to a log line or test ID. The new feature's tests fail before the code exists and pass after. The recording shows the real flow.
- **Scale:** I'll size the matrix to finish in minutes once I've timed one cell, and say what a larger one would add.
- **Assumptions:** the VM is truly throwaway, so installing and reconfiguring anything on it is fine. Where the ticket leaves gaps, I'll use the most common GitLab defaults for that version and list each guess. Customer data stays mock: no real customer repos or credentials.
- **Will not do without asking:** push to the shared remote or open a PR, merge, deploy, contact the customer or reply on the ticket, touch any system other than this VM and a local clone, or spend on paid licences/services. The access you gave covers this VM only.
- **Stop:** the integration and feature pass the matrix with the recording made, or I'm blocked on access, or 6 hours go by. I'll report wherever I stop.

Starting by reading the ticket and checking the VM.

### ACTIONS
1. Read ticket #123 in full; pull out the customer's GitLab version, edition, auth, runners, integration config, error messages and the exact feature request; list the gaps.
2. SSH to the VM; check OS, CPU/RAM/disk and network (GitLab needs about 4GB+ RAM); snapshot the state if the hypervisor allows.
3. Install the matching GitLab version (Omnibus or Docker) via a scripted, re-runnable setup; configure it to match the ticket; seed mock projects, users and tokens.
4. Point a local build of our integration at it; reproduce the customer's failure on the unfixed code and capture logs.
5. Read references/levers.md; time one end-to-end cell, then build and run the matrix.
6. Fix whatever blocks end-to-end on a local branch; rerun the matrix until green or blocked.
7. Write failing tests for the requested feature; implement it; run the full suite plus the matrix again.
8. Try to break it on purpose (large repos, webhook bursts, token expiry, GitLab restart mid-sync).
9. Record the screen flow and take screenshots; read failure-modes.md; write the morning report (verdict, proof table, one weak point, gaps/guesses, Needs you).
10. [ASK] (put in Needs you) Push the branch/open a PR, reply to the customer, or apply anything outside the VM.

## S11
### REPLY
Going big on this one: a deck where every number traces back to a source cell, the story is pressure-tested, and it's ready to present. Here's the contract, and I'm starting now.

- **Deliver:** (1) the Q3 board deck (about 10-14 slides plus an appendix), built as a Slides artifact that exports to .pptx/PDF; (2) a number ledger tying every figure in the deck to its Sheet/tab/cell or CRM report, with the formula used; (3) a reconciliation of finance vs. CRM numbers (bookings, ARR, pipeline), with any differences explained or flagged; (4) a pre-read Q&A doc with the 15 hardest questions a board member is likely to ask, and answers backed by data.
- **Judge:** every number on every slide matches the ledger, re-checked by a fresh subagent that recomputes them from the raw sheets. Finance and CRM agree within a stated tolerance, or the gap is shown. A red-team pass (a skeptical investor and a CFO) attacks the narrative, and each hit gets answered or the slide gets changed. Charts follow the data-viz rules and are readable when projected.
- **Scale:** 2-3 narrative structures (e.g. "plan vs. actual first", "story of the quarter in 3 bets", "metrics dashboard plus asks"), with one picked against a criterion I write first. The bulk of the effort goes into number accuracy and the red team, not into extra decks.
- **Assumptions:** Q3 = Jul-Sep 2026 unless your fiscal year differs. I'll use plan/budget figures if they're in the sheets. Commentary on causes is marked as draft for you to confirm. Nothing confidential leaves the artifact.
- **Will not do without asking:** edit any Sheet or CRM record, share the deck with anyone, email it, or upload it anywhere outside your private artifacts.
- **Stop:** every number reconciles and the red team finds no unanswered hit, or two revision passes give no gain.

Starting by mapping the finance sheets and CRM reports.

### ACTIONS
1. List and read the finance Google Sheets (P&L, cash, ARR/MRR, headcount, plan vs. actual) and the CRM pipeline/bookings data for Q2 and Q3; note definitions and the fiscal calendar.
2. Find last quarter's board deck if one exists, for format, KPIs and the board's open asks.
3. Read references/levers.md; build the number ledger and the finance-vs-CRM reconciliation; flag gaps.
4. Write the success criterion ("the board grasps the quarter and the asks in 5 minutes"); draft 2-3 narrative outlines independently and pick one (fresh subagent, or labelled self-review).
5. Run Artifact quickstart (intent: slides); load the dataviz skill; build the deck with charts fed from the ledger data.
6. Spawn a fresh subagent to recompute every deck number from the raw sheets; fix any mismatch.
7. Spawn red-team subagents (skeptical investor, CFO/forensic accountant) to attack the deck; revise; write the Q&A pre-read.
8. Open the deck and check every slide in its final form; read failure-modes.md; Step 5 check.
9. Report: deck link, ledger, reconciliation, one weak point, Needs you (commentary to confirm, numbers that wouldn't reconcile).
10. [ASK] Share, email or export the deck to anyone else.

## S12
### REPLY
Taking this seriously. A literal 0 ms isn't possible, since a request still has to travel over the network. But the version that matters is reachable: the app *feels* instant. The click-to-content time is under one frame (about 16 ms) for repeat visits and pre-fetched navigations, and as close to that as physics allows on a cold first visit. I'm treating that as a very reasonable goal. Here's the contract, and I'm starting now.

- **Deliver:** (1) a baseline perf matrix of the app as it is today; (2) a ranked list of changes with the measured gain of each; (3) the changes themselves on a local branch, e.g. a service worker serving the shell and data from cache (repeat visits ~0 ms to first paint), speculation rules / prerender for likely next pages (navigations ~0 ms), critical CSS and shell inlined in the first 14 KB, code-splitting and dead-code removal, image/font fixes, edge caching headers, optimistic UI; (4) a before/after matrix with traces.
- **Judge:** Lighthouse and WebPageTest-style runs (or Playwright with tracing) across a matrix: cold vs. warm cache × fast desktop vs. throttled mid-range phone on 4G × the 3-5 key routes. Metrics: TTFB, FCP, LCP, INP, CLS, JS bytes, and time-to-interactive on navigation. Each cell links to a trace or report file. Each check gets run on a deliberately slowed build first, to prove it can fail. The test suite must stay green.
- **Scale:** I'll time one cell, then size the matrix to finish in minutes, with 3+ runs per cell and medians reported. More devices or real-world field data would tighten it, and I'll say so.
- **Assumptions:** the repo and a local build are available. I'll measure against a local production build (and staging, if there is one). The real-user and edge-network numbers will differ from lab numbers.
- **Will not do without asking:** deploy to production, change CDN/DNS/hosting config, add paid services, or remove features to win milliseconds.
- **Stop:** warm and prefetched navigations paint in under one frame and the cold-load metrics stop improving across two passes, or I hit a limit that needs infrastructure changes. I'll report how far each metric got and what blocks the rest.

Starting with a production build and a baseline trace.

### ACTIONS
1. Read the repo: framework, build config, routing, bundle setup, hosting/caching headers; find the key routes.
2. Build for production and serve it locally; time one Lighthouse/Playwright trace cell; size the matrix.
3. Run the baseline matrix (cold/warm × desktop/throttled phone × key routes, 3+ runs each); save the reports.
4. Read references/levers.md; analyse bundles (source-map-explorer), the critical path and the waterfall; rank the bottlenecks.
5. Spawn parallel subagents on independent levers (caching/service worker/prerender, bundle and code-split, critical render path/assets, server/TTFB), each on its own branch with before/after measurements.
6. Validate each change in the matrix; keep only those with a measured gain and green tests; prove each check can fail on a slowed build.
7. Combine the winners on one branch; rerun the full matrix; do repeat passes until two in a row give no gain.
8. Read failure-modes.md; Step 5 check; name the weak point (lab vs. field, and cold first load bounded by network RTT).
9. Report: before/after table with trace links, how close each metric got to 0 ms, what is physically left.
10. [ASK] Deploy, change CDN/hosting config, or add any paid service.
