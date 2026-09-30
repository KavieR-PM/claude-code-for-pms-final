# Interviews vs. tickets

Sources: `00-rook/feedback/interviews/` (4 handler interviews by Sofia Marino,
2–5 Sep 2026) and `00-rook/feedback/tickets/` (25 tickets, 13 Aug – 5 Sep
2026), checked against `00-rook/data/callout-history.csv`.

**The short answer:** both sources describe the same two 4.2 problems, but
they point at different responders. Neither one on its own finds everyone
who was actually cut off. Put together, they find all four.

## Why prioritize this now

> 4.2 didn't just make offers harder to catch. It knocked four busy,
> reliable responders out of rotation after a single bad week, and our
> scoring has no way to bring them back: in one responder's words,
> *"starting to wonder if im still even in the system."* Every week we
> wait, their work piles onto fewer people (*"Mite thinks Mite's been
> forgotten. Gale's exhausted."*), and those busiest responders are one
> bad week away from the same spiral. Because we're paid per active
> responder, and the people hit hardest are the ones *not* filing tickets,
> this will show up as lost customers before it shows up on a dashboard.
> Fixing the timeout and the scoring in the next release costs far less
> than winning these responders back later.

"Four responders" and "one bad week" come from the undocumented callout CSV
and a simulation of the scoring rules. Until Wen and Ravi confirm them, open
with "our early data suggests."

## Problem areas at a glance

| # | Problem area | How big | Data | Tickets | Interviews | Confidence | Severity | Next step (who) |
|---|---|---|---|---|---|---|---|---|
| 1 | **Responders cut off by the scoring spiral** | 4 of 16 (25%) dropped from about 12 pings/wk to 0–3. About 45 pings/wk moved to others | ✅ All 4 | 2 of 4 found | 2 of 4 found | High that it happened. Medium on the cause | 🔴 High: permanent without a fix | Actual scores for everyone near the bottom of the ranking (Wen) |
| 2 | **Offer timeout too short** (60s) | Acceptance 78% → 54% in release week. Others recovered to 74% | ✅ | 9 tickets, 8 responders | 3 of 4 | High | 🔴 High: it set off #1 | Declines vs timeouts, and answers in 60–90s (Ravi/Wen) |
| 3 | **Affected responders who don't complain** | 2 of the 4 cut off filed 0 tickets | ✅ | ❌ Missed | ✅ By chance | High | 🔴 High: others may exist | Same score pull as #1. Contact the four handlers once confirmed |
| 4 | **Fewer callouts accepted** | 133/wk → 96–120/wk (−10% to −28%). Pings sent flat | ✅ | — | — | Low on the cause | 🟠 Unknown: seasonal or unfilled? | Incidents and coverage gaps per week, including Aug 2025 (Ravi) |
| 5 | **Tickets don't match the data** | 7 of 11 "quiet" responders are steady or rising. 4 complaints predate 4.2 | ✅ Conflict | ✅ Conflict | — | High that it exists. Cause unknown | 🟠 Medium | Offers sent vs delivered (Ravi). How tickets were selected (Nadia) |
| 6 | **Work concentrated on fewer people** | Top-4 share 32% → 48% | ✅ | — | 1 of 4 | Medium | 🟡 Watch | Track weekly (Ravi) |
| 7 | **Alerts easy to miss or hard to tell apart** | — | — | 0 | 3 of 4 | Medium | 🟡 Medium: makes #2 worse | Redesign input (Sofia) |
| 8 | **Console hard to read** | — | — | 0 | 3 of 4 | Medium | 🟢 Low | Redesign backlog (Sofia) |
| 9 | **Saved filters silently reset** | — | — | 0 | 1 of 4 | Low | 🟢 Low | Check for console tickets (Nadia) |
| 10 | **Supply requisitions stuck in one queue** | 11-day wait on cracked armor | — | 0 | 1 of 4 | Low | 🟢 Low for Dispatch | Pass to the Supply PM |

Rows 1–3 are one problem: the timeout triggered the drop and the scoring
rules made it permanent. Fixing only the timeout won't bring back the four
responders already stuck at zero. Row 4 is what settles the seasonality
argument.

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
  swipe"* (T-023). That's exactly the connection Dot made without prompting.
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

1. **The root fix (problem areas 1–3).** The 7 tickets the data backs,
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
