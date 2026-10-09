# Bringing quiet responders back: what we'd build

**For:** Helen Achebe · **From:** Dispatch PM · **Date:** 8 Oct 2026 · **Status:** proposal, before anyone touches the code
**Owners:** Dispatch PM (product) · Wen Li with Marcus Oyelaran's team (engineering) · Sofia Marino (design)

## What's happening

Vesper took 8 of every 10 jobs all summer. When 4.2 cut the answer window
from 90 to 60 seconds, he started losing the race from upstairs to the phone
(*"by the time he's actually got a thumb on the screen — it's gone,"* says
Dot). Each miss quietly moved him down the line. By late August: **1 offer a
week, down from 14**, and nothing told him why. **Four of 16 responders are
stuck like this**; two never complained. Kip sees it on his console with no
explanation: *"Mite thinks Mite's been forgotten. Gale's exhausted."*

Wen asked in the code back in 2019 whether a bad stretch should fade. It
never did, and a missed offer has always counted the same as saying no.
In August that just fell out that way. **This time we decide it on purpose.**

## What we'd build *(click through it in `prototype.html`)*

1. **Missing an offer isn't saying no.** Misses and near misses cost nothing;
   a "no" still counts. The four get a fresh start: *"You're back on the list."*
2. **Offers that say where and how far.** Drive time first, then distance,
   area, a small map, skills needed, and *"Leave by 21:24 · arrive by
   21:33."* A huge Take It button and a second buzz at 30 seconds.
3. **A 15-second grace window.** *"Still open: tap to grab it."* First tap
   wins, both sides know instantly, and dispatch doesn't slow down.
4. **"You missed a callout."** Each miss comes back with its context and a
   one-tap reason (away from phone, phone didn't alert, saw it too late,
   already on a callout, too far), and the answer never changes their offers.
   It tells us whether to fix the timer, the phones, or neither.
5. **"I'm free now: put me first."** Always on the home screen: first in
   line for the next callout within a 15-minute drive. Once every 4 hours,
   and it rests until tomorrow after a miss while first in line.
6. **Handlers see it.** Kip gets "gone quiet" and "overloaded" flags with
   the reason, including the responder's own answers; he can mark Mite
   ready or ease The Gale off for 3 hours.

**We keep** the 4.2 closeness change (reverting it *"just trades one angry
group of responders for another,"* as Priya put it). **We don't change** the
60-second window yet; the grace window and the missed-callout answers come
first.

## Decisions I need from you

| Decision | My recommendation |
|---|---|
| What a missed offer costs | **Nothing**; a "no" still counts. Revisit if filling a callout slows by 10+ seconds |
| Reset the four now, or wait for data | **Now**, once Dot and Kip confirm the phones work |
| "Put me first" | **Tight**: 15-minute drive, matching skills, 30 minutes, once every 4 hours |

Also: **room in the next release** (logging and the scoring fix first),
**Sofia's time** on the screens, and **a yes to writing "how routing
decides"** in plain English. And ten minutes on **Availability Confidence**,
committed for 4.2 and never built.

## How we'll know it worked

- The four are back to at least half their usual offers within 3 weeks.
- "Is my account broken?" tickets fall by half (about 40% today).
- Callouts filled per week returns to about 132 (now 120), reported next to
  acceptance rate, which hid this.
- No responder sits below half their usual for 2+ weeks without a flag.

**One risk to check first:** if installing a release resets everyone's score
to the middle, the fix itself could restart the spiral. Wen confirms before
we ship, and owns a two-week watch after.

*Sources: callout history (not yet verified by Ravi), 25 tickets, four handler
interviews, the routing code, and simulated persona reviews (real sessions
with Sofia next). Detail in `engineering-handoff.md`.*
