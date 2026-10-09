# PRD: Rook Signal, bringing quiet responders back

| | |
|---|---|
| **Product** | Rook Dispatch (responder app + handler console) |
| **Owners** | Dispatch PM (product) · Wen Li with Marcus Oyelaran's team (engineering) · Sofia Marino (design) · Nadia Hoffmann (support) · Ravi Menon (data) |
| **Decision maker** | Helen Achebe, Director of Product |
| **Status** | Draft for review · 8 Oct 2026 |
| **Related** | One-pager `brief.md` · Prototype `prototype.html` · Engineering handoff `engineering-handoff.md` · Analysis `02-super-hearing/interviews-vs-tickets.md` |

---

## 1. Problem

Release 4.2 (12 Aug 2026) cut the time to answer a callout from 90 to 60
seconds. In the release week, every responder missed more offers. Dispatch
scores a missed offer exactly like a "no", a miss costs more than an accept
earns, and nothing ever restores the score. So the responders who missed
the most fell to the back of the line, got almost no offers, and could never
earn their way back.

**The one number:** 4 of 16 responders went from about 12 offers a week to
0–1 (49 a week combined → 3), and none has recovered.

Nobody could see it:

- Missed offers vanish from the phone without a trace, so responders can't
  tell "not offered" from "missed". About 40% of tickets ask "is my account
  broken?"
- Two of the four stuck responders never filed a ticket.
- The headline metric, acceptance rate, "recovered" to 73% partly because
  the stuck responders stopped being offered work. Callouts filled are
  still about 9% down.
- Offers say little about the incident ("9 min away"), so responders can't
  decide quickly.

Sources: callout history CSV (not yet verified by Ravi), 25 support tickets,
four handler interviews, the dispatch-routing code, and a four-analyst
root-cause review. Details in the analysis file.

## 2. Users

| User | Who | What they need | Evidence |
|---|---|---|---|
| **Responder, slow to the phone** | Vesper (phone downstairs), Captain Vantage (suiting up) | Enough time and context to say yes; not to be punished for a near miss | Dot, Ambrose interviews; T-001 |
| **Responder, gone quiet** | Meteor Mite, Farlight, The Undertow | To know they still exist, why offers stopped, and a way back in | Kip interview; T-013, T-018 |
| **Responder, near miss** | Cindermark ("thumb on the screen") | A fair chance when they were a second late | T-015, T-020 |
| **Responder, overloaded** | The Gale | A way to ease off when picking up others' work | Kip interview |
| **Handler** | Kip (two responders), Aunt Dot | To see who's quiet or overloaded and why, and to act | Kip, Dot interviews |

## 3. Goals and non-goals

**Goals**

1. A missed offer never pushes a responder out of rotation.
2. Every offer gives enough context to decide in seconds.
3. Near misses get a fair second chance without slowing dispatch.
4. Every miss is visible to the responder and their handler, with a reason.
5. Responders and handlers have simple controls: "put me first", a distance
   limit, "ease off".
6. We can tell a slow answer from a phone that never alerted.

**Non-goals (this release)**

- Changing the 60-second answer window (decided after phase 1 data).
- Reverting the 4.2 proximity weights (requested by wide-area responders;
  did not cause the collapse).
- Cross-region cover (Q4 exploration).
- Rook's final visual design. The prototype's comic "Rook Signal" look is an
  exploratory direction; Sofia maps it to Rook's design system.

## 4. Success metrics

| Type | Metric | Baseline | Target | Source |
|---|---|---|---|---|
| **Primary** | Stuck responders back to ≥50% of their usual offers | 0 of 4 | 4 of 4 within 3 weeks | Offer log |
| **Primary** | Callouts filled per week | ~120 (was ~132 before 4.2) | ~132 | Ravi (to verify) |
| Secondary | "Is my account broken?" tickets | ~40% of callout tickets | Half that | Nadia |
| Secondary | Missed-callout flags answered | n/a | ≥50% within 7 days | Offer log |
| Secondary | Responders below 50% of usual for 2+ weeks without a handler flag | Unknown | 0 | Console |
| **Guardrail** | Median time to fill a callout | To measure in phase 1 | Rises by ≤10 s | Offer log |
| **Guardrail** | First-in-line accept rate | n/a | Close to the normal accept rate | Offer log |
| **Guardrail** | Coverage gaps from personal distance limits | 0 | Stays ~0 | Console |

**Reporting change:** the weekly acceptance report also shows callouts
filled and coverage gaps.

## 5. Requirements

Priorities: **P0** must ship for the fix to work · **P1** should ship in this
release · **P2** next. Acceptance criteria are in the engineering handoff
(section numbers in brackets).

### 5.1 Fair scoring (P0)

| # | As a… | I want… | So that… |
|---|---|---|---|
| R1 | responder | a missed offer (timeout, late tap, lost grace race) not to lower my standing | one bad stretch doesn't push me out [§5] |
| R2 | product team | a real "no" to still count | someone who stops taking work still drops, as Wen intended [§5] |
| R3 | stuck responder | my standing reset once, and a "You're back on the list" message | I get offers again and I know it [§5, §7] |
| R4 | product team | scores to survive installing a release | the fix itself can't restart the spiral [§5, 2.3] |

### 5.2 The signal: offer context and timing (P0/P1)

| # | Priority | Requirement |
|---|---|---|
| R5 | P0 | Every offer leads with urgency, incident type, **drive time** (largest), distance and area, skills needed [§6.1] |
| R6 | P0 | **Leave by / arrive by** times that include the drive; never a window shorter than the drive [§6.1] |
| R7 | P1 | A small map; a large Take It button usable with gloves; "Accept now, gear up after" [§6.1] |
| R8 | P1 | A second buzz at 30 seconds left [§6.2] |

### 5.3 Near-miss grace window (P1)

| # | Requirement |
|---|---|
| R9 | After 60 seconds, the offer stays open 15 seconds ("Still lit: grab it") while the next responder is asked; first accept wins [§6.3] |
| R10 | Both responders know instantly: "It's yours" or "Another hero just took it" [§6.4] |
| R11 | Dispatch timing for the next responder is unchanged [§6.3] |

### 5.4 Missed signals and responder controls (P0/P1)

| # | Priority | Requirement |
|---|---|---|
| R12 | P0 | Every miss comes back as a "Signal missed" flag with context [§7] |
| R13 | P0 | One-tap optional reason: away from phone · phone didn't alert · saw it too late · already on a callout · too far away [§7] |
| R14 | P0 | "Your answer won't change your offers" under the reasons; answers never affect ranking [§7, 4.5] |
| R15 | P1 | "Phone didn't alert" runs a test alert; a slow result gives fixes and a route to Support [§7] |
| R16 | P1 | "Too far away" offers a personal drive-time limit (15 / 20 / 30 min) [§8.5] |
| R17 | P0 | Mission log of the last 30 days with outcome, context and the responder's reason; never the score [§7] |
| R18 | P1 | **"I'm free now: put me first"** always on the home screen: first for the next callout within a 15-min drive that matches skills, for 30 min; once every 4 hours; rests until tomorrow after a miss while first in line [§8] |

### 5.5 Handler HQ (P1)

| # | Requirement |
|---|---|
| R19 | "Gone quiet" flag (<50% of usual for a week) and "Overloaded" flag (>1.4×), with the reason and the responder's own answers [§9] |
| R20 | Actions: send a test alert, mark ready (uses the responder's "put me first"), message; ease off for 3 hours [§9] |
| R21 | Optional alert per responder with its own sound; night mode [§9] |

### 5.6 Measurement (P0)

| # | Requirement |
|---|---|
| R22 | Log every offer: sent, delivered, seen, answered (including late taps), outcome, reason, rank, priority, drive time, score before/after, callout result [§4] |

## 6. User experience

Click through the flows in `prototype.html` (switch between "Today (4.2)" and
"Proposed"):

1. **An offer arrives:** the full-screen signal, with leave-by and arrive-by
   times; second buzz at 30 s.
2. **Near miss:** "Still lit!" grace window → "It's yours!" or "Another hero
   got it".
3. **Miss:** "Signal missed" → one-tap reason → the follow-up for that
   reason.
4. **Put me first:** home screen → "First up!" → the next offer says "You
   were first up for this one."
5. **Handler HQ:** Mite "Gone quiet" with reasons and actions; The Gale
   "Overloaded" with "Ease off".

## 7. Release plan

| Phase | Ships | Why this order |
|---|---|---|
| 1 | Offer event logging (R22) | Invisible, small; settles timer vs phone and gives baselines |
| 2 | Fair scoring + reset of the four (R1–R4) | Stops the harm |
| 3 | The signal + grace window (R5–R11) | Fixes the moment of the miss |
| 4 | Missed signals, mission log, responder controls (R12–R18) | Visibility and a way back |
| 5 | Handler HQ (R19–R21) | Handlers see and act |

Each phase ships behind an on/off switch, starts in one area (Kip's city),
and has a two-week watch owned by Wen.

## 8. Dependencies

- Notification delivery receipts (for "didn't reach your phone").
- Incident data at intake: type, urgency, area, short note.
- Confirmation of how scores are stored in production.
- Ravi's definitions for the callout CSV, and September data.
- Supply: no change to the Responder Availability Record's shape.

## 9. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Installing a release resets everyone's score and restarts the spiral | Verify before ship (handoff 2.3) |
| "Put me first" slows urgent callouts if the first-in-line responder misses again | Tight limits; rests until tomorrow after a miss; track first-in-line accept rate |
| Personal distance limits create coverage gaps | Ignore limits if nobody else qualifies; show limits per area on the console |
| Two near-simultaneous accepts in the grace window | Single-winner guarantee (handoff Q12) |
| The CSV doesn't measure what we think | Phase 1 logging replaces it; Ravi confirms definitions |
| Persona feedback was simulated | Real sessions with Sofia before phase 3 |

## 10. Decisions needed (Helen)

| Decision | Recommendation |
|---|---|
| What a missed offer costs | Nothing; a "no" still counts |
| Reset the four now or wait | Now, after Dot and Kip confirm the phones work |
| "Put me first" limits | 15-min drive, matching skills, 30 min, once every 4 hours |
| Grace window length | 15 s at launch; revisit with phase 1 tap times |
| "Gone quiet" threshold | 50% for a week; tune with Kip and Dot |

## 11. Open questions

1. Where does incident type and urgency come from today, and is it reliable?
2. Did 4.2's "duplicate push on re-offer" fix delay or suppress alerts?
3. Is the routing folder we reviewed the full production code?
4. Should handler "mark ready" need the responder's consent?
5. Availability Confidence was committed for 4.2 and never built: does it
   fold into the "gone quiet" flag?

## 12. Launch and communication

- **Responders:** in-app "You're back on the list" for the four; a short
  "What's new" on first open after each phase.
- **Handlers:** plain-language release notes on release morning; a 10-minute
  walkthrough for Kip and Dot before the pilot.
- **Support:** help articles for the signal, grace window, missed flags and
  "put me first"; a reply for "why did my offers drop?".
- **Leadership:** weekly update with callouts filled, the four's recovery and
  the guardrails.
