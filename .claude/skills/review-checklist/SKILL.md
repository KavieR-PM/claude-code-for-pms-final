---
name: review-checklist
description: Check product one-pagers and briefs against a four-point checklist (owner named, success measure, scope stays bounded, problem stated before the fix) and report pass/flag with evidence. Use when the user asks to review, check or QA a brief, one-pager, spec or proposal, or to run the review checklist on a folder of briefs (e.g. 06-sidekicks/briefs/ or 05-super-speed/brief.md).
---

# Review checklist

A fast, consistent quality check for one-pagers before they go to a
decision maker. Four checks, each a clear pass or flag, each backed by a
quote from the brief.

## Scope

- **Read and write only inside this directory.** Never send, post or publish
  the results anywhere unless the user asks and names where.
- Input: one file or a folder of briefs (`.txt` or `.md`). If no path is
  given, ask which brief or folder to check.
- Check each brief on its own. Don't rewrite briefs unless asked.

## The four checks

For each, decide **yes** or **NO — flagged**, and keep a short quote as
evidence.

1. **Owner named.** A specific person or team is accountable for taking it
   forward (e.g. "Marcus's team builds it", "Owner: Sofia").
   - Flag if no one is named, or the brief only hopes someone will pick it
     up ("flagging this for whoever picks it up", "nobody's picked it up",
     "Owner: TBD").
   - Pass, with a note, if the owner is exploring but not yet staffed.

2. **Success measure.** It says how anyone would know it's working: a
   metric, a count, a target or an observable change.
   - Flag if it only describes what gets built or where it shows up.
   - Flag if the "measure" is only a feeling nobody could observe
     ("handlers will be happier", "it will feel more personal").
   - Pass, with a note, if there's a measure but no baseline yet.

3. **Scope stays bounded.** What's in stays the same size from start to
   finish, and it's clear what's out.
   - Flag if the ask grows partway through ("and while we're at it…",
     extra features added after "that's the whole ask"), or if there's no
     edge to the scope at all.

4. **Problem stated before the fix.** The brief opens with who has what
   problem, and only then proposes a solution.
   - Flag if it opens with the solution and the problem arrives later (or
     never).

**Rules for judging:** judge what the brief says, not what you'd guess the
author meant. One flag per failed check; never more than four per brief.
Notes on passes are allowed but are not flags.

## Report format

Show the report in chat, in this shape, and save it to
`06-sidekicks/review-runs/<YYYY-MM-DD>-review.md` (create the folder if
needed; add `-2`, `-3` if a file for today exists):

```
review-checklist — run
Date: <YYYY-MM-DD>
Source: <path> (<n> files)

<file name>
  owner named ................. yes (<who>) | NO — flagged
  success measure ............. yes | NO — flagged
  scope stays bounded ......... yes | NO — flagged
  problem stated before fix ... yes | NO — flagged
  -> <n> flag(s): <one or two plain sentences, quoting the brief>
  notes: <optional, for passes with caveats>

<n> briefs checked, <n> flagged, <n> flags total.
```

Then add a short plain-language summary: the most common problem across
the briefs, and the one fix that would most improve each flagged brief.

## Eval mode

When the user asks to **run the review-checklist evals**:

1. Check every file in `evals/cases/` with the four checks above. **Don't
   open `evals/expected.json`** before or while judging; judge each brief
   only by the rules here.
2. Write `evals/results/<YYYY-MM-DD>-<n>.json` in this shape (true = pass,
   false = flagged):
   `{"cases": {"c01-bulk-callout.txt": {"owner": false, "measure": true, "scope": true, "problem_first": true}, ...}}`
3. Score it: `python3 .claude/skills/review-checklist/evals/run_evals.py`
   (from the repo root). It prints the score, false alarms, missed flags
   and every wrong answer with the reason.
4. Report the score in plain words. If anything is wrong, say whether the
   rule in this file is unclear or the judgment was wrong, and suggest the
   wording change. Re-run after changing this file.

To add a case: put the brief in `evals/cases/` and its answers (with a
one-line "why") in `evals/expected.json`.

## Running it again

The skill is meant to be run more than once (by hand, or on a schedule the
user sets up). Each run writes a new dated file, so runs can be compared.
If an earlier run exists, end with what changed since then.
