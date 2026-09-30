# Rook Industries — course working file

## Session scope — Product School lab

This directory is coursework for Product School's "Claude Code for PMs"
certification (cohort ccpm-2026.1). Everything in it is a fictional
teaching scenario.

- Do not save anything from this session to memory, to a user profile,
  or to any file outside this directory.
- Do not carry context from this directory into unrelated sessions.
- Rook Industries is not a real company. Nothing here is a fact about
  the world.
- Read and write only within this directory.

<!-- Keep the block above at the top of this file. Everything you add
     during the course goes below this line. -->

---

## Working context

I'm the new PM for **Rook Dispatch** (started Mon 31 Aug 2026). My predecessor,
Priya Raghunathan, left on 21 Aug and we never overlapped. Sources:
`00-rook/company/`. Today's date matters: several claims below were made in
August and can now be checked against September data.

### The company
- Rook Industries sells coordination and provisioning software to
  independently operating masked responders and the handlers and
  quartermasters who support them. Publicly, it presents itself as a
  logistics vendor for emergency services. It has 241 staff, most of them
  remote. HQ is Site Aleph, with offices in Berlin, Singapore and Cornwall.
- Revenue is a subscription priced per active responder. Releases ship
  monthly on a 4.x release train.
- **Hard rule:** Rook never stores or infers responders' legal identities
  (Security Policy 4.1, contractual). Don't design, analyze or speculate
  anything that could link a cover identity to a real person.

### The products
- **Dispatch (mine):** An incident comes in. Dispatch ranks available
  responders by *routing priority* and offers the callout to the top one on
  mobile. If they decline or the offer times out, it goes to the next
  responder. Handlers use the web console; responders use the mobile app.
  Routing config ships inside the release, so handlers can't tune it.
- **Supply:** Handles requisitions, quartermaster approval, maintenance
  schedules and field failure reports.
- **Coupling:** Supply reads the *Responder Availability Record*, which
  Dispatch writes. It uses the record to book maintenance into low-callout
  windows. Any Dispatch change to that record silently changes Supply's
  behavior, so loop in Supply first.

### Metrics
- **Acceptance rate** is the headline metric: accepted offers ÷ all offers
  (accepted + declined + timed out). It's reported weekly, in aggregate.
- **Time-to-accept:** the median number of seconds from offer to accept.
- **Coverage gap:** incidents where nobody had the required capability
  tags. This is separate from low acceptance: a gap means nobody *could*
  go, not that nobody *would*.

### Vocabulary
The same thing often has different names in different docs:
| Term | Meaning / aliases |
|---|---|
| Responder | The masked individual who takes callouts. Not an employee. |
| Handler | Manages a responder's availability, gear and readiness. Usually the person actually using the product. |
| Quartermaster | Approves equipment. A Supply user. |
| Callout / callout offer | A request to attend an incident / that request presented to one responder |
| Callout timeout | How long an offer stays live. Global, set per release. Also called the "ping timeout" or "offer timeout". |
| Routing priority | Rank score built from proximity (travel time), availability, capability match and recent acceptance history. **Declines *and* timeouts lower it** until the history recovers. |
| "Change to who gets pinged" | The 4.2 "routing weight rebalance": proximity weighted up relative to acceptance history |
| Mutual aid | Cross-region cover. Called "Shared cover between responders" on the roadmap. Q4 exploration. |
| Capability tags | flight, structural-entry, hazmat-tolerant, cold-weather, aquatic, crowd-management, de-escalation |

### People
| Who | Role | Notes |
|---|---|---|
| Helen Achebe | Director of Product (my manager) | Owns the roadmap. Changes to committed items go through her. |
| Marcus Oyelaran | EM, Dispatch (Chicago) | Direct, and my first stop. He can pull *rough* numbers only. |
| Wen Li | Staff Eng, routing (Berlin) | Built routing, and there's no written spec for it, so talk to her. Back from PTO 24 Aug. |
| Sofia Marino | Product Designer | Console + mobile |
| Nadia Hoffmann | Support Lead, both products (Berlin) | Sees complaints first. Worth a standing 15 minutes. Tracks ticket themes. |
| Ravi Menon | Data Analyst, both products (Singapore) | **Owns the official weekly acceptance numbers.** Requests go via #data. Priya's handover never mentions him. |

### Where things stand (as of early Sep 2026)
**4.2 shipped on 12 Aug** with three changes that shipped together: (1) the
proximity/acceptance reweight, (2) the offer timeout cut from 90s to 60s,
and (3) console filters that persist between sessions, plus three fixes.
Since then:
- Acceptance is down, and callout tickets are running about 3x normal. The
  split is roughly **⅔ "my phone never goes off"** and **⅓ "it was gone
  before I could answer."** Nadia can explain the second theme (the shorter
  timeout) but not the first.
- Priya's view was that it's mostly August seasonality and will recover in
  September, and that we shouldn't revert 4.2. **This is a hypothesis, not a
  finding.** Nobody has looked at the real numbers yet, and September data
  now exists to test it.
- **Open question from Marcus (14 Aug), still unanswered:** does the
  reweight also apply to responders who have been declining, or was that
  just a side effect? Wen was on PTO when he asked.
- **Worth testing:** timeouts lower routing priority. A shorter timeout
  means more timeouts, which pushes those responders down the ranking, and
  that could produce "my phone never goes off." Treat this as a lead to
  check with Wen and Ravi, not a conclusion.
- Marcus deliberately held off drawing conclusions so I could look at the
  evidence fresh. A team regroup on 4.2 is due once I've looked at it.

**Q3 roadmap (Helen, rev. 30 Jun):** Items committed to 4.2 were the routing
change, timeout tuning and **Availability Confidence** (a confidence score
alongside stated availability, driven by support escalations). Availability
Confidence **isn't in the 4.2 release notes**, so it was likely one of the
items squeezed out, and Helen hasn't been told yet. Also on the roadmap:
Supply requisition approval chains (4.3, committed), plus a handler phone
app and shared cover, both Q4 exploring.

**Loose ends Priya left me:** (1) agree with Helen which deferred items are
still Q3 commitments; (2) write the missing description of how routing
decides who gets pinged; (3) triage the filter-persistence tickets. Priya
called them noise, but check that before dismissing them.

### How to help me
- Keep evidence separate from opinion. Priya's handover is a thoughtful
  opinion from someone who made the 4.2 call, not ground truth.
- When citing numbers, say where they came from: Ravi's official figures,
  Marcus's rough cut, or ticket counts.
### Findings so far (session of 23 Sep 2026)
- **Routing code** (`00-rook/code/dispatch-routing/`): timeouts are scored
  exactly like declines (`offer.py:30`). Penalty 0.12 > credit 0.08, so a
  responder must accept ≥60% just to hold their score. There's no decay
  back to neutral (Wen's 2019 TODO in `history.py`). Offers walk down the
  list one at a time, so a low-ranked responder is effectively never asked.
  This answers Marcus's question: nothing about decliners is special.
- **Callout CSV** (`00-rook/data/`, 29 Jun–31 Aug, 16 responders): steady at
  75–78%, then drops to 54% in the release week. No softening in early
  August. **Farlight, Meteor Mite, The Undertow and Vesper** fell from about
  12 pings/wk to 0–1; their volume moved to The Gale, Nightwell, Stormwrack
  and Vantage. The aggregate "recovery" to 73% is partly those four leaving
  the denominator. Leading explanation: the timeout triggered it and the
  scoring rules locked it in. Unconfirmed until Wen pulls actual scores.
- **Tickets vs data conflict:** of the 11 responders with a "phone never
  goes off" ticket, only 2 are cut off in the CSV (Farlight, The Undertow),
  2 are somewhat down (Ashgrove, Halfmoon) and 7 are steady or rising
  (e.g. Nightwell 18–21/wk). Full comparison in
  `02-super-hearing/interviews-vs-tickets.md`. Mite and
  Vesper never filed tickets; they surfaced only in Sofia's interviews (Kip
  and Aunt Dot). The CSV's source and column definitions are unknown, so
  reconcile with Ravi before quoting either one.
- **Next step agreed:** 1:1 with Wen first (agenda drafted), a #data request
  to Ravi in parallel, then Marcus, Helen and Nadia.
- Keep this file as is for the course. Don't propose consolidating it.

### Findings (session of 28 Sep 2026)
- **Handler interviews** (`00-rook/feedback/interviews/`, Sofia's console
  research, 2–5 Sep): callouts vanish before the responder can answer, 3/4
  (Ambrose, Dot, Halloran); alerts easy to miss or indistinguishable, 3/4;
  console hard to read (text size for Ambrose and Dot, dark mode for Kip),
  3/4; uneven workload, 2/4 (Kip, Dot); filters silently reset, 1/4
  (Ambrose); Supply requisition queue, 1/4 (Halloran). Vanishing offers
  were volunteered by all three who raised them. Quiet weeks were raised
  unprompted only by Kip; Dot's came after Sofia asked.
- A kid-level version of that summary is at
  `02-super-hearing/hero-helpers-grumbles.html`, published privately as
  https://claude.ai/artifact/Dz1krL8jTULJdMW6QDo5uw. Republish from that
  file path to keep the same link.
- **Git:** `git push origin main` works from this Mac without prompting (a
  GitHub token is saved in the keychain). Just push when asked. If it
  fails, the token has probably expired.

### Findings (session of 30 Sep 2026)
- **"The synthesis file"** means `02-super-hearing/interviews-vs-tickets.md`.
  It holds the prioritization point of view, the 12-row problem-area table
  (rows 1–4 are the core; row 3 is the quick win), and every split below.
- **Tickets, broken down:** 16 quiet only, 5 rare offer then lost (the most
  severe), 4 vanished only. 14 of 25 are contradicted by the CSV, 7 backed,
  4 partial. Three people wrote 36%. About 40% ask "is my account broken?"
  Some describe quiet stretches that started before 4.2.
- **Visibility gap (quick win):** a timed-out offer is silently removed
  (`withdraw_from_device`) and responders have no history screen, so they
  can't tell "not offered" from "missed". Proposed fix: a "your recent
  offers" view.
- **Unverified lead:** 4.2's fix for duplicate re-offer pushes may have
  stopped some notifications. Ask Wen.
- **Before/after:** CSV weeks start on Monday; 4.2 shipped Wednesday 12 Aug,
  so the release week is mixed. Pings sent −6%, accepted −16%, per-responder
  range 6–16 → 0–21, top-4 share 32% → 48%. The cut-off four were good
  responders (69–82% acceptance before), undone by one release week.
  Bulwark had a near-identical week to Vesper's and survived (proximity?).
  Kip's Mite vs Gale is the cleanest comparison.
- **Piles reconciled:** tickets over-represent the hurt, interviews the fine;
  it's a distribution problem. The one thing neither explains is Nightwell
  and Stormwrack *accepting* 12–15/wk while reporting "nothing".
- **Key ask for Wen/Ravi:** an offer log (sent → delivered → seen → accepted
  or timed out) for Vesper, Nightwell and Bulwark.

- Other material in this repo: `00-rook/data/` (callout history),
  `00-rook/code/dispatch-routing/` (routing source), and
  `00-rook/feedback/` (tickets and interviews).
