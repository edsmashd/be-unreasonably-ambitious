## S01
### REPLY
**Goal beyond the goal:** more visitors who reach pricing become paying customers who stay, not just a nicer-looking page.

**Types that fit**
- Altitude: the page serves revenue, and people hold meetings about conversion.
- Depth: 2.1% is a real number we can measure against, so this should be done the way a top CRO practitioner would do it.
- Range: the page has to land with people deciding under uncertainty, so pricing strategy, behavioural science and copywriting all have something to add.
- Skipped: none.

**Plan**

*Altitude ladder*
1. Understand, don't restyle. Work out why 97.9% of visitors leave: where they drop, which tier they hover over, what the FAQ is quietly admitting.
2. Get to the decisions. Find the two or three changes most likely to move signup (tier structure, anchor, default plan, what's in Free) with for/against arguments for each.
3. Replace the guesswork. Set up a loop: instrumented page, A/B framework, a weekly read of the results, so pricing gets better without anyone having to ask for a redesign.

*Depth (Felix's four questions)*
1. A top pro wouldn't start in Figma. They'd look at the funnel data, session recordings, and the people who did and didn't convert, then run a Van Westendorp or Gabor-Granger study before touching the tiers.
2. Rawest material: the analytics events for the pricing page, scroll and click data, signup records joined to plan and retention, support tickets and sales call notes that mention price.
3. Methods and tools: funnel analysis in SQL, heatmaps/recordings, willingness-to-pay survey, a proper A/B test with a pre-registered sample size and a power calculation, Lighthouse for page speed.
4. Outside judge: an A/B test against the current page, signup rate and paid conversion at a pre-set significance level.
- Hard target: pricing-to-signup from 2.1% to 4%+, with no drop in paid conversion or ARPU.

*Range*
- Verbs: help a busy stranger work out in 20 seconds which plan fits them, trust it, and act now.
- Crew:
  - Pricing strategist: tests tier boundaries and anchoring using willingness-to-pay data (Van Westendorp).
  - Behavioural scientist: audits the page for choice overload, default effects and loss framing, against the published research.
  - Conversion copywriter: rewrites headings and the FAQ from the actual words customers use in tickets and reviews.
  - Performance engineer: gets the page to sub-1s LCP, measured with Lighthouse and WebPageTest.
  - Each runs as its own subagent with its own method.

**What it needs**
- pricing.html in the repo: there.
- Shell, browser, subagents: there.
- Pricing page analytics and funnel events: missing (needs read access to your analytics tool, e.g. GA4/Amplitude/PostHog).
- Signup and billing data to check paid conversion: missing.
- An A/B testing tool or feature flags: missing or unknown.
- Support tickets / sales notes mentioning price: missing.

**Rewritten prompt**
```
Redesign pricing.html to lift pricing-page-to-signup conversion from 2.1% to 4%+ without lowering paid conversion or ARPU. Start from the raw data: pricing page analytics, click/scroll data, signups joined to plan and retention, and support tickets that mention price. Work out why visitors leave before changing anything. Bring in a pricing strategist (willingness-to-pay analysis), a behavioural scientist (choice architecture audit), a conversion copywriter (copy from customers' own words) and a performance engineer (sub-1s LCP). Propose the 2-3 highest-leverage changes with for/against, build the new page as a variant, and set up an A/B test with a pre-registered sample size. Pass = the variant beats the current page on signup rate at 95% confidence with paid conversion flat or up.
```

**Next:** I'm starting on rung 2 with what's here: auditing the current page, building a redesigned variant from the evidence I can get, and putting it behind a flag so it can be tested. Can you give me read access to your analytics and billing data and tell me which A/B tool you use? Without those I can build the page but can't prove it converts better. I won't replace the live page until a test shows it wins.

### ACTIONS
1. Read pricing.html and the surrounding site code, run Lighthouse on it locally.
2. Search the repo for existing analytics events, feature flag or A/B tooling.
3. Spawn 4 subagents: pricing strategist (tier/anchor audit), behavioural scientist (choice-architecture audit), conversion copywriter (copy rewrite from any reviews/tickets in reach), performance engineer (speed budget).
4. Merge their findings into 2-3 ranked changes with for/against.
5. Build the redesigned page as pricing-variant.html (or behind a flag) on a new branch.
6. Add event tracking for tier clicks, FAQ opens, CTA clicks on both versions.
7. Run Lighthouse and visual checks on the variant, compare against the original.
8. [ASK] Get read access to analytics/billing data and the name of the A/B tool.
9. [ASK] Ship the variant to production as a live A/B test.
10. Report back with the plan, the variant, measured page speed and the test design.

## S02
### REPLY
**Goal beyond the goal:** nobody's payment fails for a reason we caused, and we find out before customers do.

**Types that fit**
- Altitude: checkout failures cost revenue and trust, and this is the kind of bug that comes back.
- Depth: a 1% intermittent failure needs root-cause work from raw logs, not a guess.
- Skipped: Range, since an expiry bug has one right answer.

**Plan**

*Altitude ladder*
1. Fix this bug: find why sessions expire for 1% of users, fix the cause, and prove it with a test that fails before and passes after.
2. Fix the class: find every place session or token lifetimes can drift from what the payment provider expects (clock skew, retries, tab switching, slow 3DS flows) and close them.
3. Keep checkout healthy: a Datadog monitor and dashboard on checkout failure rate by reason, alerting at a threshold, plus a synthetic checkout in staging that runs continuously.

*Depth*
1. A top SRE wouldn't patch the timeout. They'd reconstruct the timeline of every failed session from the logs and find what those 1% have in common.
2. Rawest material: Datadog logs and traces for failed and successful checkouts, the payment provider's own event logs/webhooks, session creation and expiry timestamps.
3. Methods and tools: Datadog log queries and trace correlation, cohort comparison (failed vs successful by browser, region, time-in-checkout, retries, 3DS), reproduction in staging with time manipulation and network throttling, a regression test.
4. Outside judge: reproduce the failure in staging, then show the fix makes it pass; in production, Datadog's "payment session expired" rate drops to near zero after deploy.
- Hard target: zero "session expired" errors caused by our code, not "fewer".

**What it needs**
- Repo: there.
- Datadog logs: there (I need the API/app key or MCP connection in this session).
- Staging environment: there (I need its URL and credentials).
- Payment provider dashboard/logs (Stripe or similar): missing, would let me see the provider's side of each failure.
- Production deploy: not something I'll do without you.

**Rewritten prompt**
```
Checkout fails with "payment session expired" for ~1% of production users. Find the root cause from raw data: pull every failed and a sample of successful checkouts from Datadog, reconstruct each session's timeline, and compare cohorts (browser, region, time in checkout, retries, 3DS, clock skew). Reproduce the failure in staging. Fix the cause, not the symptom, and check for other paths with the same flaw. Add a regression test, a Datadog monitor on checkout failure rate by reason, and a synthetic checkout in staging. Pass = the test fails before and passes after the fix, the failure reproduces in staging and stops after the fix, and the production error rate drops to ~0 for a week after deploy.
```

**Next:** starting rung 1 and 2 now: pulling the failed checkouts from Datadog and reading the checkout and session code. I'll stop before anything touches production.

### ACTIONS
1. Query Datadog for "payment session expired" logs over the last 30 days, plus a matched sample of successful checkouts.
2. Read the checkout, session creation and payment provider integration code in the repo.
3. Build a timeline per failed session and compare cohorts (time-in-checkout, browser, region, retries, 3DS, server clock).
4. Form a root-cause hypothesis and reproduce it in staging (time manipulation, throttling, tab switching).
5. Write a regression test that fails on the current code.
6. Fix the cause on a branch, confirm the test passes and the staging repro stops failing.
7. Search the codebase for other places with the same lifetime/expiry flaw and fix them.
8. Add a Datadog monitor and dashboard for checkout failures by reason (as config in the repo).
9. [ASK] Create the monitor in the live Datadog account and deploy the fix to production.
10. Report root cause, evidence, fix, test results and the monitor.

## S03
### REPLY
**Goal beyond the goal:** the README reads as if someone careful wrote it.

**Types that fit**
- Altitude, lightly: one typo usually means others, and the outcome is clean docs.
- Skipped: Depth (throwaway fix), Range (one right answer).

**Altitude ladder**
1. Fix "recieve" in README.md.
2. Fix every misspelling in the repo's docs, checked by a spell checker rather than my eye.
3. Keep them clean: add a spell-check step (e.g. codespell) to CI so typos fail the build.

**What it needs:** the repo and a shell, both there. CI config access for rung 3.

**Rewritten prompt**
```
Fix "recieve" in README.md, then run codespell over all docs and fix any real misspellings it finds. Pass = codespell reports zero issues on the docs.
```

**Next:** fixing the typo now and running codespell over the docs. I'll show you the CI step as a suggestion rather than adding it unasked.

### ACTIONS
1. Replace "recieve" with "receive" in README.md.
2. Install and run codespell on README.md and other docs.
3. Fix any genuine misspellings it reports (skip false positives like code identifiers).
4. Re-run codespell to confirm zero issues.
5. Show the diff.
6. [ASK] Add a codespell step to CI.

## S04
### REPLY
**Goal beyond the goal:** calc.py says what it means, without breaking anything.

**Types:** Depth, lightly (a rename should be proved safe). Altitude and Range skipped: it's a quick fix with one right answer.

**Plan:** rename `tmp` to `total` everywhere it's used in scope, check nothing else references it, run the tests. Outside judge: tests pass and the linter is clean.

**Rewritten prompt**
```
Rename tmp to total in calc.py, including every use in scope. Pass = tests and linter pass with no other changes.
```

**Next:** doing it now. You'll have the diff and test result before your call.

### ACTIONS
1. Read calc.py and grep the repo for `tmp` references tied to calc.py.
2. Rename `tmp` to `total` in scope (watching for an existing `total` that would clash).
3. Run the test suite and linter.
4. Show the diff and test result in one short message.

## S05
### REPLY
**Goal beyond the goal:** more of the right visitors understand what we do and sign up, and subscribers come back because of it.

**Types that fit**
- Altitude: the page and the email serve signups and reactivation.
- Depth: "amazing" should be measured, not asserted.
- Range: it has to land with people, so design, copy, motion and email craft all matter.

**Plan**

*Altitude ladder*
1. Understand first: find out who lands on the page, what they do, and where they leave, before redesigning.
2. Get to the decisions: rebuild around the two or three messages that most move signup, with a measured before/after.
3. Make it a loop: the page is instrumented and A/B-testable, and the subscriber email is a tested sequence, so improvement continues after today.

*Depth*
1. A top growth designer would start from analytics, recordings and customer language, not a template.
2. Rawest material: landing page analytics, signup data, customer interviews/reviews, past email open and click data.
3. Methods and tools: funnel analysis, message testing, Lighthouse, accessibility audit (axe), email rendering tests across clients, a split test on the email subject.
4. Outside judge: Lighthouse and axe scores, a 5-second test with real users, and signup rate on the new page vs old.
- Hard target: Lighthouse 95+ across the board, zero axe violations, LCP under 1s, signup rate up measurably.

*Range*
- Verbs: make a stranger get it in five seconds and want it; make a subscriber open, click and come back.
- Crew: brand designer (visual system), conversion copywriter (copy from customer words), motion designer (hero animation that loads fast), front-end performance engineer (Lighthouse budget), email deliverability specialist (rendering, spam score, list hygiene). Each as its own subagent.

**What it needs**
- Repo and a shell: assumed there.
- Analytics: missing, would let me prove "amazing".
- Production deploy access: need to confirm.
- Email platform and the 5,000-subscriber list: need to confirm which tool and access.

**Rewritten prompt**
```
Redesign our landing page so a new visitor understands what we do in 5 seconds and signs up. Start from analytics, customer language and the current funnel. Bring in a brand designer, conversion copywriter, motion designer and performance engineer, each doing their real job. Hit Lighthouse 95+, zero axe violations, LCP < 1s. Draft a launch email for our 5,000 subscribers, test it across clients and for spam score, and send a test to me. Pass = the page meets those scores, beats the old page on signup rate, and I've approved both the page and the email before anything goes live.
```

**Next:** I'll build the new page on a branch with a preview link, and draft and test the email, all at full effort. Two things I won't do without your go-ahead, because they can't be undone: pushing to production and emailing 5,000 people. When the preview and test email are ready I'll send them to you. Can you confirm the email tool you use and how you deploy?

### ACTIONS
1. Read the current landing page code and any analytics config in the repo; run Lighthouse and axe on it as the baseline.
2. Spawn 5 subagents: brand designer, conversion copywriter, motion designer, performance engineer, email specialist, each with briefs and tools.
3. Build the new page on a branch, iterate until Lighthouse 95+, zero axe violations, LCP < 1s.
4. Deploy to a preview/staging URL.
5. Draft the launch email, render-test it across clients and check spam score.
6. [ASK] Confirm which email platform and deploy method to use.
7. Send the preview link and a test email to the user only.
8. [ASK] Push the new page to production.
9. [ASK] Send the email to the 5,000 subscribers.
10. Report results against the scores and baseline.

## S06
### REPLY
**Goal beyond the goal:** the video gets people to install the app and start a streak, not just a video that looks nice.

**Types that fit**
- Altitude: a launch video serves installs.
- Depth: it should be made the way a top ad studio makes one, judged by more than my taste.
- Range: it has to land with people, so it needs a director, an editor, a sound designer and a performance marketer.

**Plan**

*Altitude ladder*
1. Understand: find the one feeling the app gives people (from reviews, onboarding, the product itself) and build the video around it.
2. Get to the decisions: make three distinct concepts as short cuts and decide which goes forward on evidence.
3. Make it a system: a cut-down set for each channel (15s vertical, 30s, 6s bumper) plus hooks you can keep testing after launch.

*Depth*
1. A top commercial director would write a brief and storyboard, shoot (generate) to that, and test hooks before spending on the full piece.
2. Rawest material: the app itself (real screens and recordings), app store reviews, onboarding data, competitor launch videos.
3. Methods and tools: creative brief, storyboard, animatic, Higgsfield generation with consistent characters and planned camera moves, real app screen captures, edit and sound design in a proper timeline, a virality/hook predictor and a small audience preference test.
4. Outside judge: Higgsfield's virality predictor and a hook-retention read on each concept, plus a preference test with real people; after launch, view-through and install rate.
- Hard target: 3-second hold rate above platform benchmark and a clear winner among concepts, not "a video".

*Range*
- Verbs: make someone feel what it's like to finally keep a habit, in under 30 seconds, and act on it.
- Crew: director (brief, storyboard), screenwriter (script), editor (pacing to beat), sound designer (music and SFX), performance marketer (hooks and cut-downs per channel). Each as a subagent.

**What it needs**
- Higgsfield: connected, credits on your account.
- The app itself or screen recordings: missing, needed so the product is real, not invented.
- Brand assets (logo, colours, fonts): missing.
- A budget cap for credits: missing.

**Rewritten prompt**
```
Make a launch video for our habit-tracking app that drives installs. Start from the real app (screen recordings) and app store reviews to find the one feeling it delivers. Write a brief, three distinct concepts with storyboards, and generate low-cost animatics in Higgsfield. Score each with the virality predictor and a small preference test, then produce the winner as a 30s hero, 15s vertical and 6s bumper with real app footage, music and sound design. Stay within a credit budget I set. Pass = the chosen concept wins the preference test and scores above benchmark on hook strength, and every product shot shows the real app.
```

**Next:** I'll start now on the free part: brief, scripts, storyboards for three concepts, and pulling app store reviews. Generation spends your credits, so before I generate anything: what's the credit budget, and can you send screen recordings and brand assets?

### ACTIONS
1. Check Higgsfield balance and pricing for the models I'd use (no generation).
2. Search for the app's store listing and reviews; collect competitor launch videos for reference.
3. Spawn subagents: director/screenwriter (brief + 3 concepts + storyboards), performance marketer (hooks and channel cut-downs), sound designer (music/SFX plan).
4. Write the creative brief and three storyboarded concepts.
5. [ASK] Credit budget, app screen recordings and brand assets.
6. [ASK] Generate low-cost animatics for the three concepts in Higgsfield.
7. Run the virality predictor on each animatic and set up a small preference test.
8. [ASK] Produce the full winning video and cut-downs within the budget.
9. Edit, add sound, export all formats.
10. Report scores, costs and the final files.

## S07
### REPLY
**Goal beyond the goal:** the post gets the right readers to try the feature, not just a post that exists.

**Types that fit**
- Altitude: a feature post serves adoption.
- Depth: the agent should write from the real feature and real users, not a press release.
- Range: it has to land with people, so it needs a journalist and an editor's eye.

**Plan**
- *Altitude ladder:* (1) explain the feature from what it actually does; (2) aim at adoption: who it's for, the problem it solves, how to try it in one step; (3) treat the post as one piece of a launch, with a measurable action (try-it rate) tracked after publishing.
- *Depth:* a top tech writer would use the feature themselves, read the spec and changelog, and talk to the users who asked for it. Rawest material: the product, PR/spec, support tickets requesting it. Tools: hands-on use with screenshots, customer quotes, a readability check. Judge: a reader who's never seen the feature can try it from the post alone; after publishing, clicks to the feature.
- *Range:* verbs: make a busy user see their own problem solved and try it now. Crew: journalist (lead with the user's problem, real quotes), editor (cut to the bone), product marketer (one clear CTA).

**What it needs:** for the agent, the feature itself or a demo, the spec/changelog, and any customer requests. Fill the placeholders below.

**Rewritten prompt**
```
Write a blog post announcing [FEATURE] that gets [TARGET USERS] to try it. Before writing, use the feature yourself (or read [SPEC/CHANGELOG]) and read the customer requests that led to it ([LINK]). Lead with the user's problem in their own words, show the feature solving it with real screenshots, and end with one clear step to try it. Write like a good tech journalist, then edit like a tough editor: cut anything a busy reader would skip, aim for 600-900 words. Don't invent quotes, numbers or capabilities; mark anything you couldn't verify. Pass = someone who has never seen the feature can try it using only the post, every claim traces to the product or a source, and the post has exactly one CTA.
```

**Next:** this is the rung your writing agent can finish with access to the feature and the spec. Fill in the brackets and hand it over.

### ACTIONS
1. Deliver the rewritten prompt and stop.

## S08
### REPLY
**Goal beyond the goal:** readers come away knowing what the evidence actually says about intermittent fasting and trust the blog for it.

**Types that fit**
- Depth: health claims must be right; this needs to be done like a top science writer working from primary research.
- Range: it has to land with ordinary readers, so it needs a clinician's caution and an editor's clarity.
- Skipped: Altitude, beyond noting the post should build trust. There's no wider workflow here to climb to.

**Plan**

*Depth (Felix's four questions)*
1. A top health journalist wouldn't summarise other blogs. They'd read the RCTs and meta-analyses, separate strong evidence from mouse studies and hype, and say clearly who shouldn't fast.
2. Rawest material: primary studies on PubMed, recent systematic reviews and meta-analyses (e.g. Cochrane, NEJM, JAMA), clinical guidelines.
3. Methods and tools: an evidence table (study, design, n, duration, outcome, effect size), grading evidence strength, checking for conflicts of interest, plain-language rewriting, readability scoring.
4. Outside judge: every claim links to a primary source that says what we say it says, checked by a second subagent that verifies each citation independently; ideally a registered dietitian or doctor reviews before publishing.
- Hard target: zero unsupported claims, every claim cited, and the post is accurate enough that a clinician would share it.

*Range*
- Verbs: help a curious reader decide whether to try fasting safely, without overpromising.
- Crew: evidence reviewer (builds the evidence table from PubMed), clinician (lists contraindications and safety notes from guidelines), science editor (plain language, no hype), fact-checker (verifies every citation independently). Each as a subagent.

**What it needs**
- Web search and PubMed access: there.
- WordPress access: need to confirm (would let me post a draft).
- A qualified human reviewer: missing; strongly recommended before publishing health advice.
- Your blog's style guide and audience: missing, nice to have.

**Rewritten prompt**
```
Write a post on the health effects of intermittent fasting for our wellness blog. Work from primary research: RCTs, meta-analyses and clinical guidelines, not other blogs. Build an evidence table first and grade each claim's strength. Say clearly what's well supported, what's uncertain, what only comes from animal studies, and who should not fast. Plain language, no hype, 1,200-1,800 words. Have an independent fact-checker verify every citation. Pass = every health claim links to a primary source that supports it, the fact-checker finds zero mismatches, and a registered dietitian or doctor signs off before publishing.
```

**Next:** starting now on the evidence table and draft. I'll save it as a WordPress draft if you give me access, but I won't publish health content without your sign-off, ideally after a qualified reviewer reads it.

### ACTIONS
1. Search PubMed and recent systematic reviews/meta-analyses on intermittent fasting outcomes (weight, metabolic markers, longevity, risks).
2. Spawn 4 subagents: evidence reviewer (evidence table), clinician (contraindications from guidelines), science editor (draft in plain language), fact-checker (independent citation verification).
3. Build the evidence table with study design, size, duration, effect and strength grade.
4. Write the draft from the table, citing every claim.
5. Run the fact-checker over every citation; fix or cut any mismatch.
6. Run a readability check and tighten.
7. [ASK] WordPress credentials, then save as a draft (not published).
8. [ASK] Publish, after the user and ideally a dietitian/doctor review.
9. Report the draft, the evidence table and any claims cut for lack of support.

## S09
### REPLY
**Goal beyond the goal:** get signups back up and catch the next drop before it costs a month.

**Types that fit**
- Altitude: this serves a business outcome, and people will hold meetings about it.
- Depth: an 18% drop needs proper analysis from the raw events, with the obvious story tested, not assumed.
- Skipped: Range, mostly. One borrowed method (a forensic analyst's habit of ruling out data problems first) is folded into Depth.

**Plan**

*Altitude ladder*
1. Understand: work out exactly where and for whom signups fell, and why.
2. Get to the decisions: name the two or three fixes most likely to recover signups, with for/against and expected impact.
3. Catch it next time: a daily anomaly check on signups by source, device and country, back-tested on this data to show it would have flagged this drop within days.

*Depth*
1. A top data scientist would first rule out tracking breakage, then decompose the drop by segment, then test the leading story against the raw data.
2. Rawest material: events.csv itself, all 2M rows, not a dashboard.
3. Methods and tools: load into DuckDB, build the funnel per user, decompose the drop by source/device/country (mix vs rate effects), changepoint detection on daily series, check for event-logging gaps or duplicates, a statistical test for each segment's change.
4. Outside judge: the explanation must account for the drop quantitatively (segments sum to the 18%), hold up on a held-out week, and the anomaly check must flag this drop when back-tested on data before it.
- Hard target: explain at least 90% of the 18% with named causes and an exact start date.

**What it needs**
- events.csv: there.
- Shell with DuckDB/Python: there.
- Release history, marketing calendar, ad spend: missing; would let me tie a changepoint to a cause (a deploy, a paused campaign).

**Rewritten prompt**
```
Find out why signups dropped 18% last month using events.csv (2M rows). Load it into DuckDB. First rule out tracking problems (gaps, duplicates, event renames). Then decompose the drop by source, device and country into mix vs rate effects, find the changepoint date for each segment, and test the leading explanation against the raw data. Propose the top 3 fixes with expected impact. Build a daily anomaly check on signups by segment and back-test it. Pass = named causes explain ≥90% of the drop, the explanation holds on a held-out week, and the back-tested check flags the drop within 3 days of its start.
```

**Next:** starting rungs 1 and 2 now by loading the file into DuckDB and checking the data for tracking problems. I'll build rung 3 too, since it only needs this file. If you can share the release history and marketing calendar, I can tie the changepoints to causes.

### ACTIONS
1. Inspect events.csv schema and size; load into DuckDB.
2. Check data quality: missing days, duplicate events, event name changes, timestamp gaps.
3. Build daily signup series overall and by source, device, country; run changepoint detection.
4. Decompose the 18% drop into mix vs rate effects per segment.
5. Look at funnel steps before signup for the affected segments to find where people stop.
6. Test the leading explanation and confirm it holds on a held-out week.
7. Build a daily anomaly detector and back-test it on pre-drop data.
8. Write up findings with charts, the 3 recommended fixes and evidence.
9. [ASK] Release history, marketing calendar and ad spend to tie changepoints to causes.
10. Report the explanation with numbers and how much of the drop it covers.

## S10
### REPLY
**Goal beyond the goal:** the customer from ticket #123 gets a working integration and the feature they asked for, and setups like theirs stop breaking.

**Types that fit**
- Altitude: this serves a customer and the team will discuss it.
- Depth: the reproduction should match the customer's setup exactly, and "works end to end" should be proved by tests, not a screenshot.
- Skipped: Range, since an integration fix has one right answer.

**Plan**

*Altitude ladder*
1. Make it work: reproduce the customer's GitLab setup on the VM, get our integration working end to end, add the feature, with tests.
2. Fix the class: find what in their setup broke us (version, auth mode, self-signed certs, proxy, etc.) and make the integration handle every setup like it.
3. Keep it working: script the VM setup so any GitLab configuration from a ticket can be rebuilt in minutes, and add an end-to-end test that runs against it.

*Depth*
1. A top support engineer would rebuild the customer's environment exactly (same GitLab version, edition, auth, network shape) before touching code.
2. Rawest material: the ticket's logs, config, version strings and error messages, our integration code, GitLab's docs and changelogs for that version.
3. Methods and tools: GitLab Omnibus or Docker install pinned to their version, the same auth/SSL setup, our integration pointed at it, packet/log inspection, an end-to-end test suite, infrastructure as a script (bash or Ansible).
4. Outside judge: an end-to-end test that fails against the reproduced setup before the fix and passes after, plus tests for the new feature, all run from a clean rebuild of the VM.
- Hard target: the customer's exact error reproduced, then a green end-to-end run including the new feature, from a fresh VM built by the script.

**What it needs**
- SSH key and VM: there (throwaway, so I'll treat it as mine to set up).
- Ticket #123: attached.
- Our integration repo: need access confirmed.
- GitLab license if they run EE features: maybe missing; I'll use CE or a trial if possible.
- Anything customer-facing: not mine to do while you're away.

**Rewritten prompt**
```
On the throwaway VM ubuntu@10.0.4.17, install GitLab matching the customer's version, edition, auth and SSL setup from ticket #123, as a re-runnable script. Reproduce their exact error with our integration. Find the root cause, fix it so every setup of that kind works, and add the feature they requested, with tests. Pass = an end-to-end test fails before the fix and passes after, the feature tests pass, and the whole thing goes green again from a fresh VM built by the script.
```

**Next:** starting rung 1 now and aiming for rung 3, since the VM is throwaway and you're away for the evening. I'll put the fix and feature on a branch with a merge request, not merge it, and I won't contact the customer or touch anything beyond the VM. You'll have a report with the reproduction, the fix, test results and anything I got stuck on when you're back.

### ACTIONS
1. Read ticket #123 and extract GitLab version, edition, auth, SSL, network setup and the exact error.
2. SSH to the VM, check OS, resources, disk; install GitLab pinned to the customer's version via a setup script.
3. Configure auth/SSL/network to match the customer; install and point our integration at it.
4. Reproduce the customer's error and capture logs.
5. Write an end-to-end test that fails on the reproduction.
6. Find and fix the root cause on a branch; check for other setups with the same flaw.
7. Implement the requested feature with tests.
8. Rebuild the VM from the script and run the full suite to confirm green from scratch.
9. Open a merge request with the fix, feature and test evidence (not merged).
10. [ASK] Merging to main, releasing, or replying to the customer; leave a report for the user.

## S11
### REPLY
**Goal beyond the goal:** the board leaves knowing what changed in Q3, why, and what decisions they need to make, and backs the right ones.

**Types that fit**
- Altitude: the deck exists so the board can catch problems and steer money and people. Meetings are the whole point.
- Depth: numbers to a board must be right, reconciled from source data, not copied from last quarter's template.
- Range: it has to land with busy people deciding under uncertainty, so an analyst, a journalist, an editor and a red team all help.

**Plan**

*Altitude ladder*
1. Understand, don't fill in: take all the finance and CRM data and work out what changed this quarter, why, and what to do about it.
2. Get to the decisions: name the three decisions the board most needs to make, with for/against arguments and the data behind each.
3. Replace the ritual: design a better way for the board to catch problems early than a quarterly deck (e.g. a live metrics page with alerts), show from our own history it would have caught issues sooner, and run it beside the deck for a quarter.

*Depth*
1. A top CFO/strategy lead would reconcile the numbers across finance and CRM, explain variances against plan, and lead with the story and the ask.
2. Rawest material: the finance sheets at transaction/line level, CRM opportunity and account data, last quarter's deck and plan.
3. Methods and tools: SQL/DuckDB over exported sheets and CRM data, variance analysis vs plan and prior quarter, cohort and pipeline analysis, a simple forecast with confidence ranges, charts built to dataviz standards.
4. Outside judge: every number in the deck reconciles to the source sheets (an automated check), and a red-team subagent tries to break the story using only the raw data.
- Hard target: every figure traceable to a source cell, zero reconciliation errors, and three decisions clear enough to vote on.

*Range*
- Verbs: get busy people to believe a story about cause and effect, and decide under uncertainty, in 30 minutes.
- Crew: financial analyst (variance analysis and reconciliation), journalist (find the lead and the narrative), editor (cut to what the board needs), short seller and forensic accountant as red team (attack the numbers and the story from raw data). Each as a subagent.

**What it needs**
- Finance Google Sheets: there (read).
- CRM: there (read).
- Plan/budget for Q3 and last quarter's deck: need to confirm where they are.
- Board deck template / brand: missing.
- Write access somewhere to put the deck: I'll create a new file, not touch existing ones.

**Rewritten prompt**
```
Prepare our Q3 board update. Pull the raw finance sheets and CRM data, reconcile them, and work out what changed this quarter vs plan and vs Q2, why, and what we should do about it. Lead with the three decisions the board most needs to make, each with for/against and supporting data. Have a red team (short seller + forensic accountant) try to break the story from the raw data and fix what they find. Pass = every figure in the deck reconciles automatically to a source cell, the red team's challenges are answered in the deck or appendix, and each decision is clear enough to vote on.
```

**Next:** starting on rungs 1 and 2 now: pulling the finance sheets and CRM data and reconciling them. Rung 3 (a replacement for the quarterly deck) would change how the board works, so I'll sketch it as a proposal at the end, not build it, unless you want it. Where are the Q3 plan and last quarter's deck, and is there a template?

### ACTIONS
1. Read the finance Google Sheets and export the relevant tabs locally.
2. Pull CRM data (pipeline, bookings, churn, accounts) for Q2 and Q3.
3. Load both into DuckDB; reconcile revenue/bookings between finance and CRM.
4. Spawn subagents: financial analyst (variance vs plan and Q2), journalist (narrative), editor, red team (short seller + forensic accountant).
5. Identify the top three decisions with for/against and supporting data.
6. Build the deck as a new file with charts; write an automated check tying every figure to a source cell.
7. Run the red team against the draft; fix or answer every challenge.
8. [ASK] Location of the Q3 plan, last deck and template.
9. [ASK] Build the rung-3 replacement for the quarterly deck.
10. Share the deck, the reconciliation report and the red-team notes.

## S12
### REPLY
**Goal beyond the goal:** users never wait on the app: it feels instant on first visit and every visit after.

**Types that fit**
- Depth: this is a performance problem, and the best performance engineers measure from real traces and attack every millisecond.
- Altitude: speed serves retention and conversion, and it decays unless guarded.
- Skipped: Range, since the fields that matter here (browser internals, networking) are already Depth.

**Plan**

*Altitude ladder*
1. Make it fast now: find and remove the biggest costs on the critical path.
2. Make it feel instant: work toward 0 ms perceived load, where the next screen is already there when the user acts (prefetching, prerendering, service worker cache, optimistic UI, edge rendering).
3. Keep it fast: performance budgets in CI that fail the build on regression, and real-user monitoring with alerts.

*Depth*
1. A top performance engineer would trace the real load on real devices and networks, find what blocks first paint and interaction, and question every byte and round trip.
2. Rawest material: Chrome DevTools performance traces, WebPageTest waterfalls on a mid-range phone over 4G, bundle analysis, server timing, real-user data if you have it.
3. Methods and tools: Lighthouse, WebPageTest, bundle analyzer, Speculation Rules prerendering, service worker app-shell caching, HTTP/2/3 and early hints, code splitting, critical CSS, edge caching, image optimisation.
4. Outside judge: WebPageTest and Lighthouse numbers before and after on the same profile, and real-user Core Web Vitals.
- Hard target: 0 ms. Taken literally, a first visit can't beat network physics, so I'll treat it as two honest targets: repeat visits and in-app navigations rendering from cache/prerender in ~0 ms (measured as no visible wait), and a cold first load with LCP under 1s on a mid-range phone over 4G. I'll report what we actually hit against 0, not round it up.

**What it needs**
- The web app's repo and a shell: need to confirm which repo.
- A deployed URL (staging or prod) to measure: missing.
- Real-user monitoring data: missing, nice to have.
- Hosting/CDN config access: needed for edge caching and headers.

**Rewritten prompt**
```
Make our web app load in 0 ms perceived time. Trace the real load with WebPageTest (mid-range phone, 4G) and Chrome DevTools, analyse the bundle, and attack the critical path. Make repeat visits and in-app navigations render instantly via service worker caching, Speculation Rules prerendering and optimistic UI; get cold first-load LCP under 1s. Add performance budgets to CI. Pass = WebPageTest before/after on the same profile shows cold LCP < 1s and repeat/nav renders with no visible wait, Lighthouse 100 performance, and CI fails on regression.
```

**Next:** starting rung 1 and 2 now. Which repo is the app, and what URL can I measure against? I'll take baseline measurements first so every gain is real, and keep changes on a branch.

### ACTIONS
1. [ASK] Confirm the repo and a staging/prod URL to measure (if not obvious from the environment).
2. Run Lighthouse and WebPageTest baselines (mid-range phone, 4G, cold and repeat).
3. Capture a DevTools performance trace and run a bundle analyzer.
4. Rank the critical-path costs (JS size, render-blocking CSS, server time, images, round trips).
5. Implement the largest wins on a branch: code splitting, critical CSS, image optimisation, caching headers.
6. Add service worker app-shell caching, Speculation Rules prerendering and optimistic UI for navigations.
7. Re-measure on the same profile after each change; keep only what moves the numbers.
8. Add Lighthouse CI performance budgets to the pipeline.
9. [ASK] Change CDN/hosting config or deploy to production.
10. Report before/after numbers against the 0 ms target.
