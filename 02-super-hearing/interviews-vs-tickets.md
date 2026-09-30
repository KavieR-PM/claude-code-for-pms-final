# Interviews vs. tickets

Sources: `00-rook/feedback/interviews/` (4 handler interviews by Sofia Marino,
2–5 Sep 2026) and `00-rook/feedback/tickets/` (25 tickets, 13 Aug – 5 Sep
2026), checked against `00-rook/data/callout-history.csv`.

**The short answer:** both sources describe the same two 4.2 problems, but
they point at different responders. Neither one on its own finds everyone
who was actually cut off. Put together, they find all four.

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
