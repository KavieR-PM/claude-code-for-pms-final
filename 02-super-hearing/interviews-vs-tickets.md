# Interviews vs. tickets

Sources: `00-rook/feedback/interviews/` (4 handler interviews by Sofia Marino,
2–5 Sep 2026) and `00-rook/feedback/tickets/` (25 tickets, 13 Aug – 5 Sep
2026), checked against `00-rook/data/callout-history.csv`.

**The short answer:** both sources describe the same two 4.2 problems, but
they point at different responders. Neither one on its own finds everyone
who was actually cut off. Put together, they find all four.

## Why prioritize this now

> 4.2 knocked four busy, reliable responders out of rotation after a
> single bad week, and our scoring has no way to bring them back: in one
> responder's words, *"starting to wonder if im still even in the
> system."* That fear has spread well beyond those four. About 4 in 10
> callout tickets essentially ask "is my account broken?", mostly from
> responders who are still getting work, because nobody can see what
> they've been offered or missed. Meanwhile the work is piling onto fewer
> people (*"Mite thinks Mite's been forgotten. Gale's exhausted."*), and
> overload is the one problem support will never hear about until those
> responders start missing offers too. Because we're paid per active
> responder, this will show up as lost customers before it shows up on a
> dashboard. We should fix the timeout and the scoring in the next
> release, and give responders a view of their recent offers so they stop
> guessing.

"Four responders" and "one bad week" come from the undocumented callout CSV
and a simulation of the scoring rules. Until Wen and Ravi confirm them, open
with "our early data suggests." "4 in 10" counts tickets, not responders,
and three people wrote more than a third of them.

## In plain words

*The whole story, simple enough for a fifth grader.*

**The story.** Some heroes get jobs on their phones. When a job pops up,
they tap "yes" to take it. On August 12, the company changed the app.

**Problem 1: "The job ran away before I could tap it!"** The change gave
heroes less time to say yes: 60 seconds instead of 90. So lots of jobs ran
away to someone else. *Why?* Think of a hero upstairs when the phone buzzes
downstairs. By the time they run down the stairs, the 60 seconds are up
and the job is gone. With 90 seconds, they used to make it. The notes and
the chart agree. ✅

**Problem 2: "My phone never rings anymore!"** Only 4 heroes really
stopped getting jobs. Here's why, we think.

- **It's like a points game.** Every hero has a score, and the app offers
  jobs to the highest scores first. Take a job: you get a few points ⬆️.
  Miss a job or say no: you lose even more points ⬇️. Missing costs more
  than taking earns, so you have to take more than half your jobs just to
  stay even.
- **One bad week changed everything.** Right after the change, lots of
  jobs ran away because of the shorter timer. These 4 heroes had the
  unluckiest week, lost lots of points and dropped to the bottom of the
  line.
- **At the bottom of the line, you almost never get picked.** You only get
  asked if everyone above you says no. When a job finally came, it was a
  surprise, they weren't ready, and it ran away too, so they lost even more
  points.
- **There's no way back.** Points never go back up by themselves. The only
  way up is to take jobs, and they can't get any jobs to take. They're
  stuck. 😞

These 4 weren't bad heroes. Before the change, they were some of the best.
One bad week knocked them down, and the game won't let them back up.

**What about everyone else who said "my phone never rings"?** The chart
says most of them were still getting plenty of jobs, so their notes don't
match. Best guesses:

- When a job runs away, it just disappears from the phone with no message.
  A hero might never know they missed one.
- Heroes can't see a list of the jobs they got or missed, so they're
  guessing.
- The phone might not be buzzing for some jobs, because of another change
  in the same update.

**Counting the notes:** 7 were right ✅, 4 were a little bit right 🤏, 14
didn't match the chart ❌.

**What we should do:**

1. Give heroes more time to tap "yes" again.
2. Fix the points game so a bad week doesn't stick forever, and help the 4
   stuck heroes get back in line.
3. Show heroes a list of the jobs they got and missed, so they stop
   worrying their account is broken.
4. Ask the grown-ups who built the app and the chart to check every job
   and prove which guess is right.

## Problem areas at a glance

Updated 30 Sep 2026 with the ticket breakdown, the before/after comparison,
the disagreement analysis and a closer read of the callout data (see "Data
source: callout history" at the end). Last column, compared with the first
version of this table: 🆕 new row · ⬆️ severity raised · ✏️ numbers or
wording updated · — unchanged.

| # | Problem area | How big | Evidence (data · tickets · interviews) | Confidence | Severity | Next step (who) | Change |
|---|---|---|---|---|---|---|---|
| 1 | **Responders cut off by the scoring spiral** | 4 of 16 (25%) went from 49 offers a week combined to 3. Good responders before (69–87% acceptance). **None recovered:** 3 of 25 offers accepted since, 0 of 9 in the last two weeks | ✅ 40 rows · 2 of 4 found · 2 of 4 found (Dot's only after a prompt) | High that it happened. Medium on cause | 🔴 High: permanent without a fix | Actual scores for everyone near the bottom (Wen). A score reset or recovery mechanism, since a timeout change alone won't bring them back | ✏️ |
| 2 | **Offer timeout too short** (60s) | Acceptance 77% → 54% in release week. The other 12 are still about 5 points down (75–79% → 69–74%) | ✅ · 9 tickets (4 vanished + 5 rare-then-lost) · 3 of 4, all unprompted | High | 🔴 High | Declines vs timeouts, and answers in 60–90s (Ravi/Wen) | ✏️ |
| 3 | **Nobody can see their own offers** ("is my account broken?") | About 10 tickets (40%). Missed offers are silently removed from the phone, and there's no history screen | Code · ✅ 40% · 1 second-hand | High that the gap exists | 🔴 High: spreads fear beyond the four. **Quick win** | "Your recent offers" view (Sofia/Wen) | 🆕 |
| 4 | **Affected responders who don't complain** | 2 of the 4 cut off filed 0 tickets | ✅ · ❌ missed · by chance | High | 🔴 High | Same score pull as #1 | — |
| 5 | **Notifications may not be firing** (4.2's re-offer push fix) | Unknown. Could explain "phone never goes off" | Release notes · consistent · — | Low: hypothesis | 🟠 Unknown | Check whether the push fix suppressed notifications (Wen) | 🆕 |
| 6 | **Work concentrated on fewer people** | The other 12 now get 98% of all offers (was 72%). Top-4 share 32% → 48%. Halfmoon nearly fell too | ✅ · 0 · 1 of 4 (Kip) | Medium | 🟠 Medium: support will never see it | Track weekly. Add Halfmoon to the offer-log request (Ravi/Wen) | ⬆️ |
| 7 | **Fewer callouts filled** | Accepted pings 132/wk → 96, 104, 108, 120 (still −9%). About 100 fewer over four weeks. Pings sent also down 4–8% | ✅ · — · — | Low on cause: fewer incidents (seasonal) **or** callouts not filled through Dispatch | 🟠 Unknown: could be a hidden coverage problem | Weekly incidents, unfilled callouts and coverage gaps, including Aug 2025 (Ravi). Routing overrides since 12 Aug (Wen, audit log) | ✏️ |
| 8 | **The headline metric hides the problem** | Acceptance rate "recovers" to 73% partly because the four stopped being offered work, while callouts filled stay down | ✅ · — · — | High | 🟠 Medium: leadership sees recovery that isn't there | Report callouts filled and coverage gaps alongside acceptance (Ravi) | 🆕 |
| 9 | **Tickets don't match the data** | 14 of 25 tickets contradicted, 7 backed, 4 partial. 3 people wrote 36% | ✅ conflict · ✅ conflict · — | High that it exists. Partly explained (#3, #5), not for Nightwell | 🟠 Medium | Offer log (sent → delivered → seen → accepted/timed out) for Vesper, Nightwell, Bulwark, Halfmoon (Wen/Ravi) | ✏️ |
| 10 | **Alerts easy to miss or hard to tell apart** | — | — · 0 · 3 of 4 | Medium | 🟠 Medium: makes #2 and #3 worse, but won't fix #1 | Redesign input (Sofia) | ⬆️ |
| 11 | **Console hard to read** | — | — · 0 · 3 of 4 | Medium | 🟢 Low | Redesign backlog (Sofia) | — |
| 12 | **Saved filters silently reset** | — | — · 0 · 1 of 4 | Low | 🟢 Low | Ask whether console tickets exist (Nadia) | — |
| 13 | **Supply requisitions stuck in one queue** | 11-day wait on cracked armor | — · 0 · 1 of 4 | Low | 🟢 Low for Dispatch | Pass to the Supply PM | — |

Rows 1–4 are the core: the timeout triggered the drop, the scoring rules
made it permanent, and nobody (including support) can see who's affected.
Fixing only the timeout won't bring back the four responders already stuck
at zero. Row 3 is the quick win to ship alongside the timeout and scoring
fix. Row 7 settles the seasonality argument, and row 8 is why the usual
dashboard won't show any of this.

## Themes by source

| Theme | Tickets (25) | Interviews (4) |
|---|---|---|
| **Phone goes quiet / no callouts** | **18 tickets** (72%), about 11 responders | 2 of 4 (Kip, Dot) |
| **Callout vanishes before they can answer** | **9 tickets** (36%), 8 responders | 3 of 4 (Ambrose, Dot, Halloran) |
| **Both at once: a rare offer, then lost** | 5 tickets (T-011, 019, 020, 023, 025) | 1 of 4 (Dot) |
| Alerts, readability, filters, Supply | **0 tickets** | 1–3 of 4 each |

Two tickets (T-020 and T-025) report both problems, so the first two rows
add up to more than 25. The 72% quiet share matches Nadia's rough "two
thirds."

## Where they agree

- **The two 4.2 problems are real, and they're linked.** Five tickets tell
  the same story: *"first one in weeks and it vanished before i could even
  swipe"* (T-023). That's the connection Dot made once Sofia asked about quiet weeks.
  A responder who rarely gets offers loses the few they get to the
  60-second timeout, which pushes their score down further.
- **The timing lines up with the release.** Tickets point to 12 August
  (*"no callouts since the 12th"*, T-008). Interviews say it's happening
  "lately" or "more than it used to."
- **One incident appears in both.** Ambrose filed T-001 on 13 August and
  described the same "coat and one boot on" moment to Sofia three weeks
  later. That's a useful check that both sources are reporting the same
  events.

## Where they disagree

### 1. They point at different responders

Compared against the four responders who were actually cut off in the
callout data:

| Cut off in data | In tickets? | In interviews? |
|---|---|---|
| Farlight | ✅ T-018 | — |
| The Undertow | ✅ T-013, 019 (T-005 is too early; see Timing) | — |
| Meteor Mite | — | ✅ Kip |
| Vesper | — | ✅ Dot |

The only responder who appears in both sources is Captain Vantage, and he
isn't one of the four.

### 2. The tickets overstate how widespread the problem is

Of the 11 responders with a "quiet" ticket, the callout data shows:

- 2 cut off (Farlight, The Undertow)
- 2 somewhat down (Corporal Ashgrove 10→7, Halfmoon 11→8 pings a week)
- **7 steady or rising** (Nightwell, Ironvale, Stormwrack, Cindermark,
  Sgt. Falkirk, The Drift, The Longcast)

Every quiet claim in the interviews matches the data.

### 3. The tone is very different

Tickets, especially the ones responders filed from their phones, sound
alarmed: *"is my account broken"*, *"starting to wonder if im still even
in the system."* Handlers in interviews play it down: *"I notice it, I
don't dwell on it"* (Ambrose), *"these things happen"* (Halloran). Going
by tone alone, you'd think it's a crisis from the tickets and a minor
annoyance from the interviews.

### 4. The interviews explain *why*; the tickets don't

Dot's *"it didn't used to feel like a fair race, phone to stairs"* and
Ambrose's observation that a slower response *"still landed him the job
more often than not, and lately that doesn't seem to hold"* describe the
timeout penalty in plain words. The tickets only report symptoms.

### 5. Console issues only show up in interviews

No ticket mentions alerts, text size, dark mode or filters, even though
Priya expected the filter change to generate tickets. This may just be how
the tickets were selected: Nadia's thread was about *callout-related*
tickets, so this folder may have been filtered to those. Check with Nadia
before concluding there are no console complaints.

## Timing

Tickets run 13 Aug – 5 Sep; the callout data ends the week of 31 Aug.
Checking each claim against the weeks it actually covers changes the
picture in four ways.

1. **Some complaints describe problems that started *before* 4.2 shipped
   on 12 August.** T-002 (14 Aug, "six days", so since about 8 Aug), T-005
   (19 Aug, "since the start of the month"), T-012 (25 Aug, "about a
   month") and T-016 (28 Aug, "slow first half of August"). Ambrose says
   in both T-001 and his interview that losing a callout "isn't the first
   time" this year. 4.2 can't have caused anything that started before it
   shipped. That gives some support to Priya's view that something else is
   going on, but the callout data shows no dip before the release (the
   week of 3 Aug was the best, at 78%). So these complaints conflict with
   the data too.
2. **Matching each ticket to its dates makes the conflict with the data
   sharper.** Nearly every "quiet" claim is still contradicted for the
   days it covers. For example, Nightwell's "nothing in like 10 days"
   (22 Aug) covers weeks with 16 and 18 pings. The Undertow's first
   ticket (T-005, 19 Aug) is contradicted as well: the data shows 27 pings
   from 1 to 19 August. Only his later tickets (26 and 31 Aug) match. Even
   the responders who really were cut off started complaining before the
   data shows any drop.
3. **The order of the complaints fits the explanation of what went
   wrong.** The first tickets (13–20 Aug) are mostly about offers
   *vanishing* (T-001, 003, 007), the immediate effect of the 60-second
   timeout. The four cut-off responders only drop in the data from the
   week of 17 Aug, and their matching "quiet" tickets arrive after that.
   The "rare offer, then lost" tickets all come late (T-011 on 24 Aug,
   then T-019, 020, 023, 025). That's the expected order if the timeout
   cut first, scores then fell, and the few remaining offers were lost too.
4. **Ticket volume shows no trend, and it overcounts people.** About 8
   tickets arrived each week from 17 Aug on, matching Nadia's "not getting
   worse, not getting better." Several people filed three times each (The
   Undertow; Ironvale; Nightwell together with her handler), so the 18
   "quiet" tickets come from 11 responders. Count responders, not tickets.

**Where the evidence ends:** nothing here covers September after the
first week, so whether things recovered still needs Ravi's data.

## What this means

- **Don't use either source alone to size the problem.** Tickets
  over-count, since several busy responders say they're getting nothing.
  Interviews under-count, since only four people were asked, about
  something else. Only the callout data tells you who was actually cut
  off.
- **The affected responders who stay quiet are the real risk.** Meteor
  Mite and Vesper were cut off and never filed a ticket. Other responders
  like them may exist. When Wen pulls actual scores, ask for **everyone
  near the bottom of the ranking**, not just the people who complained.
- **Ask Ravi and Nadia about the gap.** Why do Nightwell, Ironvale and
  Stormwrack say "nothing" while the data shows 12–21 pings a week? Either
  the data counts offers the responder never actually received on their
  phone, or the tickets are mistaken. Settling that is the most important
  open question in Module 2.

## Other ways to split the data

The callout CSV only has week, responder, handler, pings sent and pings
taken, but splitting it five more ways makes the picture much sharper.
"Before" means the six weeks from 29 Jun to 3 Aug; "release week" is the
week of 10 Aug; "after" is the three weeks from 17 Aug.

### 1. The cut-off four were not weak responders

| | Pings a week before | Acceptance before | Release week | Pings a week after |
|---|---|---|---|---|
| Vesper | 13.8 | **82%** (highest of all 16) | 6/12 (50%) | 2.7 |
| Farlight | 12.0 | 74% | 4/10 (40%) | 1.3 |
| The Undertow | 12.0 | 78% | 4/11 (**36%**) | 2.0 |
| Meteor Mite | 11.2 | 69% | 4/10 (40%) | 2.3 |
| The other 12 | 6–15 | 73–84% | 50–64% | 7–20 |

All four were busier than the median responder and accepted at normal
rates. **One bad week, the week of the release, is what separates them.**
The three worst release-week rates of all 16 belong to them. This isn't
the system screening out unreliable responders. It knocked out good ones
after a single bad week.

### 2. Rerunning the scoring rules reproduces the four exactly

Applying `history.py`'s rules (+0.08 per accept, −0.12 per miss, floor 0,
ceiling 1, no recovery) to each responder's weekly totals:

- **Only the four fall to about 0** (Vesper 0.76 → 0.36 → 0.12 → 0).
- **Everyone else is back at or near 1.0 within a week or two.** Nightwell
  dips to 0.88, then recovers.

This is an approximation: weekly totals rather than individual offers, and
an assumed 0.5 starting score. It strongly supports the explanation, but
Wen's real scores are still the proof.

**One case it doesn't explain:** Sgt. Bulwark had a release week almost
identical to Vesper's (5/10 vs 6/12), yet kept his volume. Something else,
most likely proximity, since that now counts most, decided which of them
fell. The CSV has no location data, so ask Wen.

### 3. Kip's two responders are a natural experiment

Same handler, same city, same week:

| Week | Meteor Mite | The Gale |
|---|---|---|
| 3 Aug | 11 sent / 8 taken | 13 / 10 |
| 10 Aug (release) | 10 / **4** | 15 / 9 |
| 17 Aug | 4 / 1 | 17 / 12 |
| 31 Aug | 1 / 0 | 21 / 16 |

Handler setup, region and incident volume are all the same for both. The
only difference is how each did in release week. That rules out "the
handler set something up wrong" and "it's a quiet region." It is exactly
Kip's *"Mite thinks Mite's been forgotten. Gale's exhausted."*

### 4. Work is being concentrated on fewer people

The busiest four responders' share of all pings went from **32%** (steady
all summer) to 42%, 46%, then **48%**. The Gale, Nightwell, Stormwrack and
Captain Vantage each went from about 13 to about 20 pings a week, and their
acceptance slipped from about 77% to 72%. That's consistent with Kip's
"exhausted," but it's a small dip, so treat it as a watch item. If the
winners burn out, their acceptance drops and the same spiral could catch
them.

### 5. Fewer callouts are getting accepted

Accepted pings per week were 131–134 all summer, then 96, 104, 108, 120.
Pings sent barely changed. So either there were fewer incidents (which
would support Priya's seasonal view) or more callouts ran down the whole
list with no taker. **The CSV can't tell these apart.** That's the real
test of the seasonal question.

### Splits the CSV can't do (ask Ravi and Wen)

| Split | What it would settle |
|---|---|
| **Declines vs timeouts** (`no_answer` in `offer.py`) | Whether the timeout, not reluctance, drove the release-week misses |
| **Time to answer**, especially 60–90 seconds | How many offers would have been accepted under the old 90s timeout |
| **Incidents and coverage gaps per week, including Aug 2025** | Whether August is really seasonal, and whether callouts are going unfilled |
| **Travel time per responder** | Why Vesper fell and Bulwark didn't |
| **Offers sent vs delivered to the phone** | The tickets-vs-data conflict (busy in the data, "nothing" in the tickets) |
| **Weeks after 31 Aug** | Whether anyone has recovered (the simulation says nobody can) |

### How this connects to the interviews

- Every interview claim lines up with a split above. Dot's "race to the
  stairs" is the release-week miss. Her "quiet weeks" is Vesper's score at
  zero. Kip's two cards are split 3. Ambrose's sense that slower answers
  "still landed him the job" is Vantage staying at the top after 8/13 in
  release week.
- **The data adds what the interviews couldn't see:** being cut off
  doesn't depend on how good or reliable a responder is. It depends on one
  week, and, from the scoring rules, it's permanent without a fix.

## Breaking the tickets down further

### Three kinds of ticket, not two

Classifying each ticket by its main complaint, with no double counting:

| Ticket type | Tickets | Responders | Example |
|---|---|---|---|
| **Quiet only**: "my phone never goes off" | 16 | 11 | *"is my account broken. nothing in like 10 days"* (T-009) |
| **Rare offer, then lost** | 5 | 5 | *"first one in weeks and it vanished before i could even swipe"* (T-023) |
| **Vanished only** | 4 | 4 | *"literally had my thumb on the screen and it switched to someone else"* (T-015) |

### Checked against the callout data

| Ticket type | Responder was cut off | Responder somewhat down | Responder steady or rising |
|---|---|---|---|
| Quiet only (16) | 3 (T-005, 013, 018)* | 4 (Ashgrove, Halfmoon) | 9 (Nightwell, Ironvale, Stormwrack, Falkirk, Longcast, Drift) |
| Rare offer, then lost (5) | 1 (T-019, The Undertow) | 0 | 4 (Nightwell, Cindermark, Drift, Ironvale) |
| Vanished only (4) | 0 | 0 | 4 (Vantage, Falkirk, Longcast, Cindermark) |

\*T-005 came before The Undertow's drop shows up in the data, so only
T-013 and T-018 actually match.

**7 tickets are backed by the data, 4 are partly backed (a real but
smaller dip) and 14 are contradicted.** The vanished complaints hold up
well, since the timeout affects everyone. The quiet complaints mostly
don't.

### Other ways to cut them

| Cut | What it shows |
|---|---|
| **Who filed** | Handlers filed 15, responders 10. Accuracy is about the same: 1 of 12 handler "quiet" claims matches the data, and 1 of 6 responder ones. |
| **Repeat filers** | 25 tickets come from 12 responders. Nightwell, Ironvale and The Undertow filed 3 each, making 36% of all tickets, and 2 of those 3 are contradicted by the data. |
| **What they ask for** | About 10 tickets (40%) essentially ask "is my account broken?" Handlers have nothing to tell them, and T-008 notes responders can't see their own history. |
| **Handler-assigned severity** | 1 High, 8 Medium, 6 Low. The only High (T-019) is a rare-offer-then-lost ticket, the type with the strongest language. |

### Where to focus

1. **The root fix (problem areas 1, 2 and 4).** The 7 tickets the data backs,
   plus the rare-offer-then-lost tickets, all point to the timeout and the
   scoring rules.
2. **A visibility gap you can close however the root cause turns out.** A
   timed-out offer is silently removed from the phone (`withdraw_from_device`
   in `offer.py`), and responders have no history screen, so they can't
   tell "not offered" from "missed." A "your recent offers" view would cut
   these tickets. This is a possible explanation, not a confirmed one: it
   can't explain Nightwell reporting "nothing" while the data shows her
   accepting 14–15 a week.
3. **Don't size the problem from ticket counts.** Three people wrote 36% of
   the tickets, and most "quiet" claims don't match the data.

## Before vs after the release

The callout data is weekly, with weeks starting on Mondays, and 4.2 shipped
on **Wednesday 12 August**, so the split is into three periods rather than
at the release date itself:

| Period | Weeks | Dates | Contains |
|---|---|---|---|
| Before | 6 | 29 Jun – 9 Aug | Entirely before 4.2 |
| Release week | 1 | 10 – 16 Aug | Mixed: Mon–Tue before 4.2, Wed–Sun after |
| After | 3 | 17 Aug – 6 Sep | Entirely after 4.2 |

The release week includes about two pre-release days, so its 54% probably
understates the first days of 4.2. "Before" is 6 weeks and "after" is 3, so
the comparison uses weekly averages. The ticket timing section above uses
exact ticket dates instead.

| | Before | Release week | After | Same or different? |
|---|---|---|---|---|
| Pings sent per week | 172 | 177 | 162 | About the same (−6%) |
| Responders getting pings | 16 | 16 | 16 → 15 | About the same at first, then one reaches zero |
| Acceptance, the 12 not cut off | 77% | 58% | 69–74% | Dipped, then mostly recovered |
| **Acceptance, everyone** | **77%** | **54%** | **68%** | **Different**: hasn't recovered |
| **Pings accepted per week** | **132** | **96** | **111** | **Different**: about 16% fewer |
| **Pings per responder** | **6 – 16** | 7 – 16 | **0 – 21** | **Different**: much wider spread |
| **Share going to the top 4** | **32%** | 33% | **42 – 48%** | **Different**: concentrating |
| The four cut off | about 12 each | 4–6 accepted | 1 – 4 | Different |
| Timeout / weights (from the code) | 90s, proximity 0.45 | changed mid-week | 60s, proximity 0.60 | Different |

- **About the same amount of work went out.** Pings sent held steady,
  which counts somewhat against a big seasonal drop in incidents. It isn't
  conclusive, because pings include re-offers.
- **It went to different people.** Before, everyone got 6–16 pings a
  week. After, it ranges from 0 to 21.
- **The part that looks like recovery comes from the responders still
  getting work.** The 12 who weren't cut off got back to 69–74%, possibly
  by adapting, as Dot did by keeping the phone in his pocket. The four who
  were cut off didn't recover at all.
- **The release week is the turning point.** Nothing changed in how much
  work went out, and a lot changed in who got it.

## Loud in one pile, quiet in the other

### Loud in the interviews, rare or absent in the tickets

| Theme | Interviews | Tickets | Example |
|---|---|---|---|
| **Alerts easy to miss or indistinguishable** | 3 of 4 | 0 | *"right now Mite and Gale both just go "bing""* (Kip) |
| **Console hard to read** (text size, no dark mode) | 3 of 4 | 0 | *"at a glance I sometimes cannot tell engaged from available"* (Ambrose) |
| **The handler's own needs**: tell *me* when something comes in | 2 of 4 | 0 | *"maybe something that tells me too, not just him"* (Dot) |
| **Overload** | 1 of 4 | 0 | *"Gale's exhausted."* (Kip) |
| **Why it's happening, not just what** | 2 of 4 | 0 | *"a slower-arriving response of his still landed him the job more often than not"* (Ambrose) |
| **Praise** (saved filters, maintenance scheduling) | 2 of 4 | 0 | *"I noticed within the hour"* (Ambrose, on filters) |
| **Supply** (requisitions, failure reports, catalog) | 1 of 4 | 0 | *"it goes into a void"* (Halloran) |

### All over the tickets, rarely or never raised in the interviews

| Theme | Tickets | Interviews | Example |
|---|---|---|---|
| **"Phone never goes off" as the main complaint** | 16 of 25 (64%) | 2 of 4, only 1 unprompted | *"nothing all week?? is this thing broken"* (T-006) |
| **"Is my account broken?"** | about 10 (40%) | 1, second-hand (Kip relaying Mite) | *"starting to wonder if im still even in the system"* (T-013) |
| **Asking Rook for an answer** | about 6 handler tickets | 0 as a request | *"I'd like something more to tell her than 'I don't know.'"* (T-018) |
| **No way to see their own history** | 1 (T-008) | 0 | *"she asked if there was a way to see her own history and I had to tell her there isn't"* |
| **Emotional harm to responders** | 5+ | 0 | *"landed badly"* (T-019), *"pretty hard on her"* (T-025) |
| **Precise dates and counts** | Most handler tickets | 0 | *"no callouts since the 12th ... nine days straight"* (T-008) |

### Why they differ

- **Different channels.** Tickets are filed when something feels broken,
  and this folder is probably filtered to callout issues. The interviews
  were console research, so callout issues only came up when handlers
  raised them.
- **Different speakers.** Tickets speak for the responder and are anxious.
  Interviews speak for the handler and are calm. Nobody files a ticket
  saying "too much work," so overload only shows up in an interview.
- **Different strengths.** Tickets give dates and emotion but not causes.
  Interviews give causes but not scale.

**What this means:** the biggest ticket theme ("is my account broken?") is
a visibility problem nobody in the interviews was asked about. The biggest
interview themes (alerts, readability) don't appear in support data, so
check with Nadia whether console tickets exist. Overload is the blind
spot: support won't see it until the busiest responders start missing
offers.

## If both piles are telling the truth

They can both be right because they describe **different slices of an
uneven problem**. 4.2 didn't make things a little worse for everyone. It
made things much worse for a few responders and slightly better for
others. The average barely moved, but individual experiences went to
opposite extremes. Kip shows it within one household: *"Mite thinks
Mite's been forgotten. Gale's exhausted."*

| They disagree on | How both can be true |
|---|---|
| **How widespread "quiet" is** (64% of tickets vs 1 of 4 interviews unprompted) | Tickets come from the affected, because people file when something hurts. The interviewees were picked for console research, so they're a mix: Bulwark is steady and Vantage is doing better than ever. |
| **Tone** (anxious vs calm) | A ticket is a responder at their worst moment, often written from the phone. An interview is a handler weeks later, on a design call. Ambrose is calm in both of his, so the gap is who's speaking, not exaggeration. |
| **Console issues** (interviews only) | The ticket folder is probably filtered to callout tickets, and the interviews were about the console. Each pile only contains what it was set up to collect. |
| **Overload** (interviews only) | Nobody files a ticket saying "too much work." It surfaces only when someone asks. |
| **Vanishing offers** (both agree) | The one problem that affects everyone, so both piles report it. That supports the idea that the other disagreements come from who each pile heard from. |

### The hard case: tickets vs the callout data

For 7 responders, the tickets say "nothing" while the data says 12–21
pings a week. One way both could be partly true:

- **"My phone never goes off" might be literally true even when offers
  were sent.** In `offer.py`, an unanswered offer is silently removed from
  the phone after 60 seconds (`withdraw_from_device`). A responder whose
  phone is upstairs could have offers sent, timed out and removed without
  ever noticing. The system counts those as sent, and penalizes them.
- **A second lead:** 4.2 also shipped a fix for *"duplicate push
  notification on re-offer."* If that fix stopped some notifications from
  buzzing, offers would show up in the app but the phone would never go
  off. This is only a hypothesis; ask Wen.

**Where that stops working:** it explains high pings *sent*, not high
pings *accepted*. The data shows Nightwell accepting 14–15 a week and
Stormwrack 12–15. Nobody accepts that many jobs and then reports "nothing
in 10 days." For those responders, both can't be right: either the CSV is
labeled or measured differently than we think, or the tickets are wrong.
That's the question for Ravi.

### What this changes

- **The two piles are complementary, not contradictory.** Tickets
  over-represent the hurt, and interviews over-represent the fine. It's a
  distribution problem, which is why the overall acceptance rate hid it.
- **The best single test:** an offer log showing *sent → delivered →
  notified → seen → accepted or timed out*, with timestamps, for Vesper
  (cut off), Nightwell (contradicted) and Bulwark (steady). Ask Wen and
  Ravi.

## Why the four never recovered

The data points to a trap: once they fell, the few offers they still got
made things worse, and nothing in the system pulls them back up.

### 1. They almost never accept the offers they still get

| | Offers | Accepted | Rate |
|---|---|---|---|
| Before (weekly avg, all four) | 49 | 37 | 75% |
| Three weeks after | 25 total | 3 total | 12% |
| Last two weeks | 9 | 0 | 0% |

Every miss costs 0.12 and a responder must accept at least 60% just to
hold their score. At 12%, each offer they receive pushes them further down.

### 2. Being last in line means getting the leftovers

*An inference from the code, not shown directly by the CSV.* Offers go down
the ranking one at a time, so a responder at the bottom is only reached
when everyone above has already said no. The few callouts they see are
probably the ones nobody else wanted. That would explain why their
acceptance is so far below their own pre-release rate of 69–87%.

### 3. Rare offers are easy to miss

Before, they got about 12 offers a week, so an offer was routine. Now one
arrives every week or two, unexpectedly, with 60 seconds to answer. Dot:
*"by the time he's actually got a thumb on the screen — it's gone."* A
missed rare offer lowers the score, which makes the next offer rarer still.

### 4. The way out needs a floor they've fallen below

Halfmoon had nearly the same release week (55%), then another poor one,
then accepted 7 of 8 in the week of 31 Aug and climbed back. She could,
because she kept getting 8–9 offers a week. None of the other 12 ever fell
below 7 offers a week. The four fell to 0–5 within one week, so they never
got enough chances to recover.

### 5. It isn't their availability or setup

Farlight's handler checked her availability window and found it set
correctly (T-018). The Undertow is aquatic-tagged and incidents needing that
tag kept coming (T-005). The interviews describe responders waiting by the
phone, not stepping back.

### Why it's permanent: the code

`history.py` has no drift back toward neutral (Wen's 2019 TODO considered
it and left it out). The only way to raise a score is to accept offers, and
they barely get any. Scoring the weekly numbers with those rules sends all
four to about 0 and keeps them there, while everyone else recovers.

### What the data can't tell us

- Declines vs timeouts: are they turning offers down or missing them?
- Their actual rank and score today.
- Whether anyone has come back since 31 Aug.

All three come from Wen's offer log.

**For the fix:** changing the timeout won't bring these four back, because
they barely get offered anything. Getting them out needs a score reset or a
recovery mechanism: a drift back toward neutral, or a minimum number of
offers per week for every available responder.

## Data source: callout history

All figures below come from `00-rook/data/callout-history.csv`: 160 rows,
16 responders × 10 weeks (29 Jun – 31 Aug 2026), with columns
`week_starting`, `responder`, `handler`, `pings_sent`, `pings_taken`.
`pings_taken` is treated as accepted offers. The file's origin and column
definitions aren't documented, and Ravi hasn't checked it against the
official figures. Weeks start on Monday; 4.2 shipped on Wednesday 12 Aug,
so the week of 10 Aug is mixed.

### Weekly totals: all 16, the four, the other 12

| Week | Period | All: sent / taken | All: rate | Four: sent / taken | Four: rate | Four: share of offers | Other 12: sent / taken | Other 12: rate |
|---|---|---|---|---|---|---|---|---|
| 29 Jun | Before | 172 / 132 | 76.7% | 49 / 36 | 73.5% | 28.5% | 123 / 96 | 78.0% |
| 6 Jul | Before | 170 / 131 | 77.1% | 48 / 37 | 77.1% | 28.2% | 122 / 94 | 77.0% |
| 13 Jul | Before | 174 / 133 | 76.4% | 48 / 36 | 75.0% | 27.6% | 126 / 97 | 77.0% |
| 20 Jul | Before | 176 / 132 | 75.0% | 50 / 37 | 74.0% | 28.4% | 126 / 95 | 75.4% |
| 27 Jul | Before | 170 / 132 | 77.6% | 50 / 40 | 80.0% | 29.4% | 120 / 92 | 76.7% |
| 3 Aug | Before | 172 / 134 | 77.9% | 49 / 37 | 75.5% | 28.5% | 123 / 97 | 78.9% |
| **10 Aug** | **Release** | 177 / **96** | **54.2%** | 43 / 18 | **41.9%** | 24.3% | 134 / 78 | **58.2%** |
| 17 Aug | After | 158 / 104 | 65.8% | **16** / 3 | 18.8% | 10.1% | 142 / 101 | 71.1% |
| 24 Aug | After | 162 / 108 | 66.7% | **6** / 0 | 0% | 3.7% | 156 / 108 | 69.2% |
| 31 Aug | After | 165 / 120 | 72.7% | **3** / 0 | 0% | **1.8%** | 162 / 120 | 74.1% |

### Raw counts vs the pre-release average

| Week | Sent | vs before | Taken | vs before | Missed | vs before | Rate |
|---|---|---|---|---|---|---|---|
| Before (6-week avg) | 172 | — | 132 | — | 40 | — | 77% |
| 10 Aug | 177 | +3% | 96 | −27% | 81 | +103% | 54% |
| 17 Aug | 158 | −8% | 104 | −21% | 54 | +35% | 66% |
| 24 Aug | 162 | −6% | 108 | −18% | 54 | +35% | 67% |
| 31 Aug | 165 | −4% | 120 | −9% | 45 | +13% | 73% |

The rate recovers faster than the counts because the denominator shrank
for a bad reason: offers to the four, who were missing them, mostly
stopped. About 100 fewer offers were accepted over four weeks than at the
old pace. Fewer offers accepted *and* sent means either fewer incidents
(partly supporting the seasonal view) or callouts not being filled through
Dispatch (a coverage problem). The CSV can't tell which.

### Every row, by responder

Each cell is one CSV row, `pings_sent/pings_taken`. The four cut-off
responders are in bold.

| Responder | Handler | 29 Jun | 6 Jul | 13 Jul | 20 Jul | 27 Jul | 3 Aug | 10 Aug | 17 Aug | 24 Aug | 31 Aug | Before → after (offers/wk) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Farlight** | Linda Pruitt | 12/9 | 12/9 | 11/8 | 12/9 | 13/10 | 12/8 | 10/4 | 3/0 | 1/0 | 0/0 | 12.0 → 1.3 |
| **Meteor Mite** | Kip | 11/7 | 12/9 | 10/6 | 11/7 | 12/9 | 11/8 | 10/4 | 4/1 | 2/0 | 1/0 | 11.2 → 2.3 |
| **The Undertow** | Desmond Okafor | 12/9 | 11/9 | 12/9 | 13/10 | 12/10 | 12/9 | 11/4 | 4/1 | 1/0 | 1/0 | 12.0 → 2.0 |
| **Vesper** | Aunt Dot | 14/11 | 13/10 | 15/13 | 14/11 | 13/11 | 14/12 | 12/6 | 5/1 | 2/0 | 1/0 | 13.8 → 2.7 |
| The Gale | Kip | 13/10 | 12/9 | 13/10 | 14/11 | 13/11 | 13/10 | 15/9 | 17/12 | 20/14 | 21/16 | 13.0 → 19.3 |
| Captain Vantage | Mr. Ambrose | 12/10 | 13/10 | 12/8 | 11/7 | 12/9 | 12/9 | 13/8 | 15/11 | 17/13 | 18/13 | 12.0 → 16.7 |
| Nightwell | Marjorie Sung | 15/11 | 14/10 | 15/12 | 16/12 | 15/11 | 15/12 | 16/9 | 18/14 | 20/13 | 21/15 | 15.0 → 19.7 |
| Sgt. Falkirk | Owen Bramwell | 10/9 | 10/8 | 11/8 | 10/8 | 9/7 | 10/8 | 11/7 | 13/9 | 15/11 | 16/11 | 10.0 → 14.7 |
| Stormwrack | Renata Kovač | 13/10 | 13/11 | 12/9 | 14/12 | 13/10 | 13/10 | 14/8 | 16/12 | 18/13 | 19/15 | 13.0 → 17.7 |
| Ironvale | Teresa Alvarez | 8/6 | 8/5 | 9/8 | 8/6 | 7/5 | 8/7 | 9/5 | 10/6 | 11/8 | 12/9 | 8.0 → 11.0 |
| Cindermark | Farid Haddad | 9/7 | 9/8 | 8/6 | 10/7 | 9/7 | 9/8 | 10/6 | 11/8 | 12/8 | 12/9 | 9.0 → 11.7 |
| Sgt. Bulwark | Halloran | 9/7 | 9/7 | 10/8 | 9/7 | 8/5 | 9/7 | 10/5 | 10/8 | 11/7 | 11/8 | 9.0 → 10.7 |
| The Drift | Beatrice Calloway | 6/5 | 6/5 | 7/6 | 6/5 | 6/5 | 6/5 | 7/4 | 7/5 | 8/6 | 8/5 | 6.2 → 7.7 |
| The Longcast | Graham Petrov | 7/5 | 7/5 | 8/7 | 7/5 | 7/5 | 7/5 | 8/5 | 8/6 | 9/5 | 9/7 | 7.2 → 8.7 |
| Corporal Ashgrove | Yusuf Demir | 10/8 | 11/9 | 10/7 | 9/7 | 10/8 | 10/8 | 10/6 | 8/5 | 7/5 | 7/5 | 10.0 → 7.3 |
| Halfmoon | Simone Fischer | 11/8 | 10/7 | 11/8 | 12/8 | 11/9 | 11/8 | 11/6 | 9/5 | 8/5 | 8/7 | 11.0 → 8.3 |

**The one number for leadership:** 4 of 16 responders went from about 12
offers a week to 0–1 (49 a week combined → 3), and none has recovered.

## Tickets vs the callout data: who wrote in, and when the numbers moved

They agree on offers vanishing and mostly disagree on going quiet. The
vanishing tickets arrive in step with the numbers. The early, loud "quiet"
tickets come before the data moves and contradict it. The true ones arrive
one to two weeks after the numbers moved.

### Timeline

| Week | Tickets filed | Of which "vanished" | Of which "quiet" / rare-then-lost | All responders: acceptance | Pings accepted | The four: offers received |
|---|---|---|---|---|---|---|
| 3 Aug | 0 | — | — | 77.9% | 134 | 49 |
| **10 Aug** (4.2 ships Wed 12th) | **2** (13, 14 Aug) | 1 | 1 | **54.2%** ⬇ | **96** ⬇ | 43 |
| 17 Aug | 8 | 2 | 6 | 65.8% | 104 | **16** ⬇ |
| 24 Aug | 8 | 1 | 7 | 66.7% | 108 | 6 |
| 31 Aug | 7 | 0 | 7 | 72.7% | 120 | 3 |

- **The first ticket came the morning after the release.** T-001 (13 Aug)
  is about a callout lost on the evening of the 12th. Vanishing complaints
  line up with the release-week acceptance drop.
- **The first "quiet" ticket came on 14 Aug**, two days after the release,
  describing six days of quiet. That starts before 4.2 shipped, and the
  data shows Corporal Ashgrove getting 10 offers in each of those weeks.
- **Offer volume only drops in the week of 17 Aug, and only for four
  responders.** The "quiet" complaints started a week before the data
  shows anyone going quiet.
- **The tickets that do match came late.** The Undertow's matching tickets
  start on 26 Aug and Farlight's on 30 Aug, one to two weeks after their
  numbers fell. Mite and Vesper never wrote in.
- **Ticket volume doesn't follow the numbers.** It held at about 8 a week
  while acceptance was improving.

### Ticket by ticket

Each ticket is checked against the CSV weeks its own words cover
(`sent/taken`).

| Ticket | Filed | Responder | Says | Data for that period | Agree? |
|---|---|---|---|---|---|
| T-001 | 13 Aug | Captain Vantage | Offer moved on before he reached the phone | 10 Aug: 13/8 (5 missed) | ✅ Consistent |
| T-002 | 14 Aug | Corporal Ashgrove | No callouts in 6 days | 3 Aug: 10/8, 10 Aug: 10/6 | ❌ (and starts before 4.2) |
| T-003 | 17 Aug | Sgt. Falkirk | Gone before he opened the app | 17 Aug: 13/9 | ✅ Consistent |
| T-004 | 18 Aug | Nightwell | Second week of almost nothing | 3 Aug: 15/12, 10 Aug: 16/9, 17 Aug: 18/14 | ❌ |
| T-005 | 19 Aug | The Undertow | One callout since start of month | 3 Aug: 12/9, 10 Aug: 11/4, 17 Aug: 4/1 | ❌ Too early |
| T-006 | 20 Aug | Corporal Ashgrove | Nothing all week | 17 Aug: 8/5 | ◐ A dip, not nothing |
| T-007 | 20 Aug | The Longcast | Gone by the time he unlocked | 17 Aug: 8/6 | ✅ Consistent |
| T-008 | 21 Aug | Ironvale | No callouts since the 12th | 10 Aug: 9/5, 17 Aug: 10/6 | ❌ |
| T-009 | 22 Aug | Nightwell | Nothing in about 10 days | 10 Aug: 16/9, 17 Aug: 18/14 | ❌ |
| T-010 | 23 Aug | Halfmoon | More than a week with nothing | 10 Aug: 11/6, 17 Aug: 9/5 | ◐ A dip, not nothing |
| T-011 | 24 Aug | Nightwell | First offer in 10 days, then lost it | 17 Aug: 18/14, 24 Aug: 20/13 | ❌ |
| T-012 | 25 Aug | The Longcast | Quiet this week | 24 Aug: 9/5 | ❌ |
| T-013 | 26 Aug | The Undertow | Nothing again this week | 24 Aug: 1/0 | ✅ |
| T-014 | 27 Aug | Stormwrack | Quietest since joining | 24 Aug: 18/13 | ❌ |
| T-015 | 27 Aug | Cindermark | Switched while thumb on screen | 24 Aug: 12/8 | ✅ Consistent |
| T-016 | 28 Aug | Sgt. Falkirk | Quiet again this past week | 17 Aug: 13/9, 24 Aug: 15/11 | ❌ |
| T-017 | 29 Aug | Ironvale | Still nothing | 17 Aug: 10/6, 24 Aug: 11/8 | ❌ |
| T-018 | 30 Aug | Farlight | Almost 2 weeks, no callouts | 17 Aug: 3/0, 24 Aug: 1/0 | ✅ |
| T-019 | 31 Aug | The Undertow | First in 2 weeks, then lost it | 17 Aug: 4/1, 24 Aug: 1/0, 31 Aug: 1/0 | ✅ |
| T-020 | 1 Sep | Cindermark | 10 days, 1 callout, lost it | 24 Aug: 12/8, 31 Aug: 12/9 | ❌ |
| T-021 | 2 Sep | Halfmoon | Week 2 of nothing | 24 Aug: 8/5, 31 Aug: 8/7 | ◐ A dip, not nothing |
| T-022 | 3 Sep | The Drift | About 3 weeks, 2 callouts | 7–8 a week throughout | ❌ |
| T-023 | 3 Sep | The Drift | First in weeks, vanished | 7–8 a week throughout | ❌ On the "first in weeks" part |
| T-024 | 4 Sep | Stormwrack | So dead lately | 24 Aug: 18/13, 31 Aug: 19/15 | ❌ |
| T-025 | 5 Sep | Ironvale | First in about a month, lost it | 9–12 a week throughout | ❌ |

**Tally:** 7 agree (the 4 "vanished" tickets are consistent with that
week's misses, and 3 "quiet" tickets from the cut-off responders match), 4
partly agree (real dips for Ashgrove and Halfmoon, but not "nothing"), and
14 are contradicted.

### Do they agree?

- **On offers vanishing, yes.** Those tickets start the day after the
  release, in the same week acceptance falls from 78% to 54%.
- **On going quiet, mostly no.** Most "quiet" tickets come from responders
  the data shows getting as many offers or more. Several describe quiet
  that started before 4.2. Only the cut-off responders' tickets match, and
  they arrive after their numbers moved.
- **For some responders, the ticket and the data can't both be right.**
  Nightwell accepted 14 offers in the week she reported "nothing in about
  10 days." The Drift had 7–8 offers a week while his handler reported "2
  callouts" in 3 weeks. Either the CSV measures something other than we
  assume, or those tickets are wrong. Ravi needs to settle which, and Wen's
  offer log (sent → delivered → seen → accepted/timed out) would answer it
  directly.

## Was it just a quiet August?

Priya's view was that the drop was mostly August being quiet. **Short
answer: mostly no, but the callout file can't settle it completely.** It
only covers 29 Jun – 31 Aug 2026, with no data from last year, so it
can't show what a normal August looks like.

1. **Early August wasn't quiet.** The week of 3 Aug was the best week of
   the summer (78 of every 100 offers accepted). The drop came all at once
   in the week of the update (54 of 100). A season slows down gradually;
   this was like flipping a switch.
2. **A quiet month would hit everyone. This didn't.** 12 responders got
   more offers than before, and 4 got almost none. A slow month doesn't
   pick out four people; the scoring rules do. Kip's two responders show
   it best: same city, same weeks, Meteor Mite went from 11 offers to 1
   while The Gale went from 13 to 21.
3. **One part could be August.** After the update, accepted offers fell
   about 16% and offers sent fell 4–8%. That could mean fewer emergencies
   (a quiet August) or callouts not getting filled. The file can't tell
   which.
4. **"It'll come back in September" can't be checked.** The file stops at
   the end of August.

**Verdict:** "it was just August" doesn't fit, because the drop started
exactly with the update and hit 4 responders hard while others got busier.
"August made it a bit worse" is possible. To know for sure, ask Ravi for
last August's numbers and for the number of incidents per week.
