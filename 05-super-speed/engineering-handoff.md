# Engineering handoff: bringing quiet responders back

**Owner (product):** Dispatch PM · **Engineering owner:** Wen Li (with Marcus Oyelaran)
**Design:** Sofia Marino · **Support:** Nadia Hoffmann · **Data:** Ravi Menon
**Status:** draft for engineering review · updated 8 Oct 2026

**Read with:** the brief (`05-super-speed/brief.md`), the clickable prototype
(`05-super-speed/prototype.html`) and the full analysis
(`02-super-hearing/interviews-vs-tickets.md`).

**What changed in this version:** richer offer context; a near-miss grace
window; a second buzz; instant "It's yours" confirmation; a "You missed a
callout" flag with responder-reported reasons; "I'm free now" puts a
responder first in line; a "You're back on the list" message; softer status
wording.

**Second round (8 Oct):** leave-by and arrive-by times replace "10 minutes
to get there"; "I'm free now: put me first" is always on the home screen,
with limits (once every 4 hours; rests until tomorrow after a miss while
first in line); a reassurance line under the missed reasons; "Too far
away" offers a personal drive-time limit; a failed test alert gives fixes
and a route to Support; handlers can mark a responder ready or ease an
overloaded one off for 3 hours.

These came from two rounds of prototype reviews with responder personas
(Vesper, Captain Vantage, The Undertow, Cindermark, Meteor Mite, The Gale).
Those sessions were simulated, so real sessions with Sofia should confirm
them. The prototype's comic "Rook Signal" look is an exploratory visual
direction, not Rook's design system; Sofia maps it to the real components.

---

## 1. Summary

Since 4.2 (12 Aug), four of 16 responders went from about 12 offers a week to
0–1 and never recovered. The 60-second answer window caused a week of missed
offers; the scoring rules then locked them out, because a timeout is scored
exactly like a decline (`offer.py:30`), a miss costs more than an accept earns
(−0.12 vs +0.08), and nothing ever restores points (`history.py:30`). Nobody
could see it happening: missed offers vanish silently from the phone, the
offer itself says little about where the incident is, and the console shows
no difference between a quiet responder and a busy one.

We want to fix the scoring, give responders enough context to decide fast,
give near misses a fair second chance, and make missed opportunities visible
to responders and handlers.

## 2. Goals and non-goals

**Goals**

1. Missing an offer no longer pushes a responder out of rotation.
2. Every offer tells the responder what, where, how far and how urgent at a glance.
3. A near miss (tap just after the window) can still win, without slowing dispatch.
4. Every missed offer comes back to the responder as a flag they can explain in one tap.
5. Handlers see who has gone quiet or overloaded, and why.
6. We record enough about every offer to tell a slow answer from an offer that never reached the phone.

**Non-goals (this release)**

- Changing the 60-second answer window. The grace window and the data from
  phase 1 come first.
- Reverting the 4.2 proximity weights. They were requested by responders
  covering wide areas and did not cause the collapse.
- Mutual aid / cross-region cover (Q4 exploration).

## 3. Build order

| Phase | What | Why first | Depends on |
|---|---|---|---|
| **1** | Offer event logging | Invisible, small, and every later phase needs it. Also answers the open root-cause question (timer vs phone). | Notification delivery receipts (§11, Q2) |
| **2** | Scoring change + one-time reset of the four | Stops the harm | Helen's decisions (§12) |
| **3** | Offer card: context, grace window, second buzz, instant result | Fixes the moment of the miss | Incident data for the card (§11, Q11) |
| **4** | "You missed a callout" flag, "I'm free now", recent offers list | Answers "is my account broken?" (~40% of tickets) and collects the reason for every miss | Phase 1 |
| **5** | Handler console: flags, reasons, alerts, sounds, dark mode | What Kip asked for | Phases 1 and 4 |

---

## 4. Phase 1: offer event logging

One row per offer. Logging must be asynchronous and must never delay dispatch.

| Field | Description | Notes |
|---|---|---|
| `offer_id` | Unique per offer | |
| `callout_id` | The callout this offer belongs to | |
| `responder_id` | Internal record ID only | **Never** a legal identity (Security Policy 4.1) |
| `rank_position` | Place in line for this callout | 1 = asked first |
| `priority_reason` | `normal` or `first_in_line` | Set when "I'm free now" moved them to the front (§8) |
| `score_components` | Proximity, recent acceptance, capability at ranking time | Also answers Marcus's question (hypothesis #11) |
| `score_before` / `score_after` | Recent-acceptance score before and after | |
| `drive_minutes` / `distance_km` | As shown on the offer card | Needed for "Too far away" analysis |
| `sent_at` | Server time the offer was pushed | |
| `delivered_at` | Time the device received it | Null if never delivered |
| `opened_at` | Time the offer was first shown on screen | Null if never seen |
| `second_buzz_at` | Time the 30-second reminder fired | |
| `answered_at` | Time of the responder's tap | Including taps in the grace window and after it |
| `outcome` | `accepted`, `accepted_grace`, `declined`, `timed_out`, `lost_race`, `tapped_late` | `accepted_grace`, `lost_race` and `tapped_late` are new |
| `missed_reason` | Responder's one-tap answer, or null | See §7 for values |
| `missed_reason_at` | When they answered | |
| `timeout_seconds` / `grace_seconds` | Windows in force | 60 / 15 at launch |
| `callout_result` | `filled`, `unfilled`, `cancelled` | On the callout |

**Acceptance criteria**

- **1.1** Every offer produces exactly one event row, including offers lower in the list.
- **1.2** Taps during or after the grace window are stored with the real `answered_at` and the right `outcome`.
- **1.3** `delivered_at` is populated for at least 95% of offers to online devices.
- **1.4** Median dispatch time (callout created → first offer sent) does not increase.
- **1.5** Data is queryable by Ravi within 24 hours.

---

## 5. Phase 2: scoring change

| Rule | Today | Proposed | Status |
|---|---|---|---|
| Accept (incl. in grace window) | +0.08 | +0.08 | No change |
| Decline ("Not this one") | −0.12 | −0.12 | No change |
| Timed out / tapped late / lost the grace race | −0.12 | **0** | Recommended; Helen to confirm (§12) |
| Recovery over time | None | Not needed if misses cost 0; revisit after 4 weeks | Helen to decide |
| One-time reset | n/a | Set the four affected responders to 1.0 at release, then show "You're back on the list" | After handlers confirm phones work |

**Why misses should cost 0.** In the root-cause analysis (four analysts,
replaying the summer under different rules), not penalizing timeouts was the
only scoring change that freed all four stuck responders in every scenario,
and it doesn't require changing the answer window. A decline is still a real
"no" and keeps its cost, which preserves Wen's 2019 intent: someone who
stops taking work still drops; someone who had a bad week doesn't.

**Acceptance criteria**

- **2.1** A timed-out, late or lost-race offer does not change the recent-acceptance score.
- **2.2** A decline still subtracts 0.12; an accept, including in the grace window, adds 0.08.
- **2.3** **Installing the release does not reset any score.** Verify before ship; scores are held in memory in `history.py` (`_scores = {}`), and if production works the same way an install resets everyone to 0.5 (hypothesis #4).
- **2.4** The one-time reset applies only to the named responders, is logged, and triggers the "You're back on the list" message once.

---

## 6. Phase 3: the offer card

### 6.1 Context (what the responder sees first)

| Element | Example | Rule |
|---|---|---|
| Urgency | `Urgent` pill | From the incident's priority |
| Incident type | Building collapse | From the incident |
| **Drive time** (largest text) | 9 min drive | Same travel-time estimate routing uses (`availability.travel_time_minutes`) |
| Distance and area | 4.1 km from you · Harbor district | Area name, never an exact address on the lock screen |
| Mini map | "You" and the incident, with route line | Static image is fine |
| Needs | Needs structural entry · 2 people trapped | Required capability tags plus a short incident note |
| Leave by / arrive by | "Leave by 21:24 · arrive by 21:33" | **Arrive by** = offer time + drive time + prep time (default 10 min, configurable). **Leave by** = arrive by − drive time. Never show a window shorter than the drive. |
| Accept-first hint | "Accept now, gear up after." | Shown on every offer |
| First-in-line note | "You were first in line for this one." | Only when `priority_reason = first_in_line` |

### 6.2 Second buzz

A second alert (sound + vibration) at **30 seconds left**, and a third when
the grace window starts.

### 6.3 Near-miss grace window

When the 60 seconds run out:

1. The offer moves to the next responder **as today** (dispatch is not slowed).
2. The first responder's screen stays open for **15 seconds**: *"Still open: tap to grab it"*, same context line, button **"Grab it"** / **"Let it go"**.
3. **First accept wins**, whether it's the first responder (in grace) or the next responder (in their normal window).
4. The loser is told instantly: *"Another responder just took it. This doesn't count against you."*

### 6.4 Instant result

| Outcome | Message |
|---|---|
| Accepted (normal or grace) | **✓ It's yours** · context line · "Head out when you're ready; you have 10 minutes." |
| Lost the grace race / timed out | Opens the missed-callout flag (§7) |
| Declined | "Passed on this one" |

**Acceptance criteria**

- **3.1** Every offer shows urgency, type, drive time, distance, area and needs before the buttons.
- **3.2** The second buzz fires at 30 s left; a third fires at grace start.
- **3.3** During grace, exactly one responder can win a callout. Two near-simultaneous accepts never both succeed.
- **3.4** Result messages appear within 1 second of the decisive tap.
- **3.5** Dispatch timing for the next responder is unchanged by the grace window.

---

## 7. Phase 4: "You missed a callout"

Shown right after any miss (timed out, lost the grace race) and available
later from the recent offers list until answered.

**Content:** "You missed a callout" · the context line (type · drive time ·
distance · area) · "It went to another responder. This doesn't count against
you." · "What happened? One tap, optional."

**Reasons (one tap, optional):**

| Value (`missed_reason`) | Label | Follow-up |
|---|---|---|
| `away_from_phone` | I was away from my phone | "Thanks. This helps us fix the right thing." |
| `phone_did_not_alert` | My phone didn't alert me | Offer **"Send a test alert"** and report delivery time. If slower than 10 s: show fixes (battery saver off for Rook, allow lock-screen alerts), **"Test again"**, and **"Get help from Support"** (opens a ticket with the test results attached) |
| `saw_too_late` | I saw it too late | Thanks message |
| `already_on_callout` | I was already on a callout | Thanks message (and see §13: this may indicate an availability bug) |
| `too_far` | Too far away | Offer a personal limit: **"Only send callouts within 15 / 20 / 30 min"** or keep as is (§8.5) |

**Reassurance line** (always shown under the reasons): *"Your answer won't
change your offers. It helps us fix the right thing, and your handler sees it
too."*

**Actions:** Dismiss. ("I'm free now: put me first" lives on the home
screen, §8.)

**Recent offers list:** last 30 days, newest first. Each row shows the outcome,
the context line, the time, and for misses either "You said: …" or a
**"Tell us what happened"** button. Never show the score or the formula.

**Status note** (top of screen, plain and non-blaming):

| Condition | Note |
|---|---|
| 3+ of the last 5 offers missed | **Offers have slowed down.** A few recent callouts ran out of time before you could answer. Missed offers don't count against you. Keep your phone close and take the next one, and you'll be back to your usual pace. |
| Most recent offer accepted after a slow stretch | **You're moving back up.** |
| After the one-time reset | **You're back on the list.** We've reset your standing after the August change… (dismissible, shown once) |

**Acceptance criteria**

- **4.1** The flag appears within 5 seconds of a miss and stays answerable from the list for 7 days.
- **4.2** A reason is saved with one tap, shown as "You said: …", and visible to the responder's handler.
- **4.3** "Send a test alert" appears only after "My phone didn't alert me"; a slow result shows fixes and a Support route.
- **4.5** Choosing a reason never changes ranking or score.
- **4.4** Reasons are reportable by Ravi per responder and per week.

---

## 8. "I'm free now: put me first"

| Rule | Default (configurable) |
|---|---|
| Where | **Always on the responder's home screen** (not only after a miss), and from the handler console ("Mark ready") |
| Effect | Responder is placed **first in line** for the next qualifying callout, ahead of normal ranking |
| Qualifying callout | Within a **15-minute drive** and matching the responder's **capability tags** |
| Duration | **30 minutes**, or until used, whichever comes first |
| Shown to responder | "✓ You're first in line" message and a "First in line · 30 min" chip; the next offer says "You were first in line for this one." |
| Availability | Tapping it also confirms the responder as available |
| Two responders first in line for the same callout | Earlier tap wins; the other keeps their priority for the next one |
| How often | **Once every 4 hours** per responder (handler "Mark ready" counts toward the same limit). Button shows "Put me first: again at HH:MM". |
| A miss while first in line | Priority is used up; no score change (§5). The button **rests until the next day** ("Put me first: back tomorrow"). |

**Acceptance criteria**

- **8.1** The next qualifying callout is offered to the first-in-line responder first, and logged with `priority_reason = first_in_line`.
- **8.2** Priority expires after 30 minutes if unused.
- **8.4** The button is unavailable for 4 hours after use, and until the next day after a miss while first in line.
- **8.3** Non-qualifying callouts (too far, wrong skills) are ranked normally.

### 8.5 Personal drive-time limit

Set from the "Too far away" follow-up (and in settings). Callouts beyond the
responder's limit are not offered to them. **Track coverage gaps**: if many
responders set short limits, some incidents may find nobody; the console
should show how many responders in an area have a limit set.

- **8.5.1** A responder with a 20-minute limit is never offered a callout with a longer drive.
- **8.5.2** The limit can be changed or removed any time in settings.

> **Trade-off to watch:** this is a fairness boost that can slow dispatch if
> priority goes to someone who then misses again. Track the accept rate of
> first-in-line offers; if it falls well below the normal rate, tighten the
> radius or the duration.

---

## 9. Phase 5: handler console

| Element | Rule |
|---|---|
| **Usual level** | Median weekly offers over the previous 6 weeks, excluding weeks already flagged. Under 4 weeks of history: no flags. |
| **"Gone quiet" flag** | Offers in the last 7 days below **50%** of usual (configurable; Helen to confirm) |
| **"Carrying N× normal" flag** | Offers in the last 7 days above **1.4×** usual |
| **Reason line (quiet)** | Missed-offer share, split by outcome, plus the responder's own answers: e.g. "Mite says: phone didn't alert (2), away from phone (1)". Else "fewer jobs nearby" or "reason unclear". |
| **Reason line (overload)** | "Picking up work from nearby responders who've gone quiet" when applicable |
| **Actions** | Quiet: send a test alert · **mark ready** (uses the responder's "put me first", §8) · message · check availability. Overload: **ease off for 3 hours** · check in · adjust availability. |
| **Ease off** | For 3 hours the responder is offered a callout only if no other qualifying responder accepts first. Shown on their card as "Easing off · 3 h". |
| **Handler alert** | Optional per responder, off by default; fires when an offer is sent to that responder |
| **Alert sound** | Choice per responder |
| **Dark mode** | Console-wide toggle |

**Acceptance criteria**

- **5.1** A responder crossing the quiet threshold is flagged within 1 hour.
- **5.2** Flags show the reason, including the responder's missed-callout answers, and at least one action.
- **5.3** A handler with alerts on hears that responder's sound within 5 s of the offer.
- **5.4** Handlers see only their own responders.

---

## 10. Rules that must not break

| Rule | Detail |
|---|---|
| **Responder privacy** | No legal identity stored, shown or inferable (Security Policy 4.1). Offer history and missed reasons visible to the responder and their handler only. The responder who wins a grace race is never named to the loser. Security review before ship. |
| **Location on the lock screen** | Area name and drive time only, never an exact address, until the offer is accepted |
| **Supply contract** | Do not change the shape of the Responder Availability Record (`availability.current_record()`); Rook Supply reads it. "I'm free now" must not write to it in a new format. |
| **Dispatch speed** | Logging, flags, alerts and the grace window are asynchronous. No added latency to ranking or offering. |
| **Accessibility** | Body text at least 16 px; drive time is the largest text on the offer; WCAG AA contrast in light and dark. |

---

## 11. Technical design: questions for Wen and Marcus

A short design doc (2–4 pages) is needed because this touches routing, score
storage, notifications, the responder app, the console and reporting.

1. **Where are offer events stored, and for how long?** Who can query them?
2. **How do we get `delivered_at`?** Notification provider or app acknowledgement? What if neither?
3. **How does the app report a tap after the deadline**, given `offer.py` stops polling and withdraws the offer at 60 s?
4. **How are scores stored in production, and do they survive an install?** (2.3)
5. **Clock accuracy:** device vs server time for grace-window decisions.
6. **Can thresholds change without a release?** (quiet %, overload ×, grace seconds, first-in-line radius and duration)
7. **Failure modes:** phone offline, notification lost, logging down. Dispatch must keep working.
8. **Kill switch:** each phase behind a flag.
9. **What changed in the 4.2 "duplicate push notification on re-offer" fix**, and could it affect re-offers or the second buzz? (Hypothesis #3.)
10. **Is the `dispatch-routing` folder the full production code?** Travel time, push, polling and withdrawal are placeholders there.
11. **Where does incident context come from?** Type, urgency, area name and short note: are they captured at intake today, and reliably?
12. **Grace-window concurrency:** how do we guarantee a single winner when the first responder (in grace) and the next responder accept within milliseconds?
13. **First-in-line queue:** where is priority held, how does it interact with ranking, and how is it expired?

---

## 12. Decisions needed

From Helen:

| Decision | Recommendation |
|---|---|
| What a miss costs | **0** (declines still −0.12) |
| Grace window length | **15 s** at launch; revisit with phase 1 tap-time data |
| First-in-line radius and duration | **15-minute drive, 30 minutes** |
| "Put me first" limits | **Once every 4 hours; rests until tomorrow after a miss while first in line** |
| Prep time in the arrive-by calculation | **10 minutes** |
| Reset the four now or wait | Now, after handlers confirm phones work |
| "Gone quiet" threshold | 50% for a week; tune with Kip and Dot |

---

## 13. Edge cases

| Case | Expected behaviour |
|---|---|
| Phone offline when offer sent | `delivered_at` null; missed flag shows when the phone reconnects; no score change |
| More than one device | One offer; first delivery wins for `delivered_at`; a tap from any device counts |
| Two near-simultaneous accepts in grace | Exactly one wins; the other sees "Another responder just took it" |
| Personal drive limits leave nobody for a callout | Offer to the nearest responders anyway, ignoring limits, and log it as a coverage risk |
| Responder easing off is the only qualified one | Still offered; ease-off never causes an unfilled callout |
| "I was already on a callout" | If the responder was marked available while on a callout, flag it for engineering: the availability record may be wrong |
| First-in-line responder misses again | Priority used up; no score change; track first-in-line accept rate |
| Two responders first in line nearby | Earlier tap wins; the other keeps priority |
| Bulk callouts (several responders needed) | Each offer handled separately; grace and priority apply per offer |
| New responder (under 4 weeks) | No console flags; offer card and missed flags work normally |
| Handler with a large roster | Flags shown as a filterable list, not one alert per responder |
| Callout cancelled mid-offer or in grace | Show "This callout was cancelled"; no score change |

---

## 14. Measurement, rollout and rollback

**Success measures**

- The four are back to at least half their usual offers within 3 weeks.
- No responder sits below half their usual for 2+ weeks without a handler flag.
- Callouts filled per week returns to about 132 (now ~111–120).
- "Is my account broken?" tickets fall by half.
- At least 50% of missed-callout flags get a reason within 7 days.
- Grace-window wins and first-in-line accept rate are tracked weekly.
- Median time to fill a callout rises by no more than 10 s.

**Monitoring** (Ravi): callouts filled and unfilled per week; offers per
responder against usual; delivery delay; grace-window wins and losses;
missed reasons by type; first-in-line usage and accept rate.

**Reporting change:** the weekly acceptance report also shows callouts filled
and coverage gaps.

**Rollout:** phase by phase behind flags; start with one area (Kip's city),
then expand. Wen owns a two-week watch after each phase.

**Rollback:** turn the flag off; keep the event log running.

**Support readiness** (Nadia): help-article wording for the offer card, grace
window, missed-callout flag and "I'm free now". **Handler release notes** in
plain words on release morning.

---

## Appendix: where this comes from in the code

| Behaviour | Location |
|---|---|
| Timeout recorded as a decline | `00-rook/code/dispatch-routing/offer.py:30` |
| Penalty and credit values | `config.py:18–19` (+0.08 / −0.12) |
| No recovery (Wen's 2019 note) | `history.py:30–34` |
| Scores held in memory, default 0.5 | `history.py:15–22` |
| Offer pulled back at the deadline, no notice to responder | `offer.py:41–48` |
| Travel-time estimate used for ranking (reuse for the card) | `routing.py:45–54`, `availability.py:21–26` |
| Placeholders for push, polling, withdrawal, travel time | `offer.py:51–63`, `availability.py:21–26` |
