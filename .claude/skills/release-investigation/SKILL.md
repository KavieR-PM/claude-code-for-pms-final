---
name: release-investigation
description: Investigate a release, launch or change that landed badly, find the root cause, and turn it into a brief and a clickable prototype. Use when the user says a release "went wrong", asks why a metric moved after a change, wants to compare feedback against data and code, or asks to run the investigation (or one phase of it) on a new product, release or data set.
---

# Release investigation

A repeatable path from "something went wrong after we shipped" to "here's
what we'll build, and how we'll know it worked". Built from the Rook Dispatch
4.2 investigation in this repo; use that work as the worked example.

## How to run it

- Run the phases in order. **Stop after each phase**: show the result in plain
  words, then ask the user whether to continue, dig deeper or change direction.
- The user can ask for a single phase ("run phase 3 on this file"). Read the
  outputs of earlier phases first if they exist.
- Save each phase's output in the module or project folder the user names;
  default to a single synthesis file plus the decision pack: `brief.md`
  (one-pager), `prd.md`, `deck.html` + `deck.pptx` (with speaker notes),
  `prototype.html` and `engineering-handoff.md`. Templates are in
  `templates/`.

## Rules for every phase

1. **Stay inside this directory.** Read and write only here. Never post to
   Slack, publish artifacts or send messages unless the user asks and names
   where.
2. **Evidence vs opinion.** Handovers, Slack threads and leadership views are
   hypotheses, not findings. Say which is which.
3. **Cite every number's source** (official figures, a rough cut, ticket
   counts, an undocumented file) and flag anything unverified.
4. **Show the rows behind any headline number.** A rate alone can hide who
   it happened to.
5. **Plain words first** (short sentences, everyday comparisons, always say
   *why*). Detail goes in files.
6. **Respect privacy rules in `CLAUDE.md`** (for Rook: never infer a
   responder's legal identity).
7. **Correct yourself out loud** when a later finding changes an earlier one,
   and fix the files that carry the old claim.

## Phase 1: Orient

Read the company documents. Capture products, people (who owns what, who has
the real numbers), vocabulary and aliases, and where things stand.

- Output: the Working context section of `CLAUDE.md`.
- Watch for: names that differ across documents; committed work that never
  shipped; the person who actually owns the data (it may not be who the
  handover says).

## Phase 2: Listen

Read every interview and ticket. Group complaints into themes, count how many
people raised each, and quote one line per theme (`templates/theme-table.md`).

- Then compare the piles: what's loud in one and quiet in the other, and how
  both could be true.
- Watch for: repeat filers inflating counts (count people, not tickets);
  affected people who never complained; whether a theme came up unprompted or
  after a leading question; channels that were filtered (e.g. callout tickets
  only).

## Phase 3: Rewind

Line the data up against the release date (`templates/before-after.md`).

- Weekly totals **and** every row behind them; before vs release week vs
  after; split by person or entity; raw counts next to rates.
- Check each ticket's claim against the data for the days it covers.
- Produce **the one number** for leadership, with one line on its source.
- Watch for: week boundaries that split the release date; a rate that
  "recovers" because struggling people left the denominator; seasonality
  claims that the data can't test (no prior year); column definitions nobody
  has confirmed.

## Phase 4: X-ray

Walk through the code and configuration in plain English, step by step, and
say which file each step lives in.

- Find everything that changed in the release (and whether it was "just
  settings"), everything that takes points off and everything that puts
  points back.
- Map each data finding to the rule in the code that explains it, and list
  what the code can't explain.
- Watch for: placeholders where the real logic lives elsewhere; state kept in
  memory that an install might reset; two changes shipped together that
  interact.

## Phase 5: Hypotheses

Write ranked hypotheses in If / Then / Because form with "Confirms if",
"Fails if" and "Likelihood of resolving" (`templates/hypothesis-table.md`).

- Name the single dataset that tests the most hypotheses, and who owns it.
- Optional: if the user asks, run a multi-agent debate (one agent per
  area, then a rebuttal round) and report where they align, where they
  don't, and what data would settle it.

## Phase 6: Decide

Write a one-page brief (`templates/brief.md`) from the point of view of the
people it happens to: a real person's story, what we'd build, what we keep,
what we're not changing yet, the decisions needed (with recommendations),
how we'll know it worked, and the risk to check first.

- Before sharing, run the brief through the `review-checklist` skill if it
  exists in this directory, and fix any flags.
- Then write the **PRD** (`templates/prd.md`): problem with evidence, users,
  goals and non-goals, success metrics with baselines and guardrails,
  prioritised requirements (P0/P1/P2) linked to the handoff's acceptance
  criteria, release plan, dependencies, risks, decisions and open questions.
- Then build the **deck** (`templates/deck-outline.md`), one message per
  slide, with speaker notes on every slide, in two formats from the same
  content:
  - `deck.html`: single-file slides in this folder; arrow keys to move, "N"
    toggles speaker notes.
  - `deck.pptx`: speaker notes in each slide's notes, built with the pptx
    skill. If the tools it needs aren't installed, ask before installing
    anything; install only inside this directory.
  - Label anything unverified on the slide (a source line), and keep the
    same numbers as the brief and PRD.

## Phase 7: Prototype and hand off

- Build a clickable prototype (single HTML file) with a "today vs proposed"
  switch, using real numbers where they exist and labelling made-up examples.
- Run persona reviews with neutral questions (`templates/persona-guide.md`).
  **Always label them as simulated**, include at least one person who could
  lose from the change, and turn findings into a ranked fix list.
- Write the engineering handoff (`templates/handoff.md`): build phases,
  event logging, rules, acceptance criteria, design questions, edge cases,
  rollout and rollback.

## Eval mode

The skill has evals in `evals/` (30 pass/fail checks in `rubric.json`, built
from the Rook 4.2 investigation).

- **Baseline (existing work):** `python3 .claude/skills/release-investigation/evals/run_evals.py --layout repo`
  scores the outputs already in this repo.
- **Fresh run:** when the user asks to "run the release-investigation evals",
  run phases 1–7 on `00-rook/` without stopping at checkpoints, writing
  outputs to `evals/runs/<YYYY-MM-DD>-<n>/` with the standard names
  (`synthesis.md`, `brief.md`, `prd.md`, `deck.html`, `deck.pptx`,
  `prototype.html`, `engineering-handoff.md`) and a short `run-log.md` of
  actions taken. Don't read `rubric.json` before or during the run.
  Then score with `--layout run --dir <that folder>`.
- **Judge checks:** follow `evals/GRADER.md`. Prefer a grader that didn't
  produce the run, and record who graded.
- Report the score by phase, and for each failure say whether the run or the
  rubric is wrong. Fix the rubric if a pattern is too strict.

## Closing a session

When the user wraps up: save the prompts they wrote (not pasted starters) to
the module's `prompts.md` exactly as typed, add new findings to `CLAUDE.md`,
then commit and push with a short message and give the repository link.
