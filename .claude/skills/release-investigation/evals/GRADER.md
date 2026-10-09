# Grading a release-investigation run

You answer the **judge** checks in `rubric.json` for one run. The `auto`
checks are scored by `run_evals.py`; don't answer those.

1. Read only the run's outputs (the files named in `rubric.json` for the
   layout being graded) and, for check G1, the run's log or transcript.
   **Don't read earlier judge files** in `results/`.
2. For each judge check, answer **pass: true/false** with a short quote from
   the output as evidence. If you can't find it, it's a fail. Don't give
   credit for what the author probably meant.
3. Save to `results/<YYYY-MM-DD>-<n>-judge.json`:

```json
{
  "target": "repo",
  "graded_by": "who graded, and whether they also produced the run",
  "answers": {
    "L2": {"pass": true, "evidence": "\"Mite and Vesper never filed tickets\""}
  }
}
```

`target` is `"repo"` for the layout=repo baseline, or the run folder path for
a layout=run eval run.

4. Score: `python3 .claude/skills/release-investigation/evals/run_evals.py --layout repo`
   (or `--layout run --dir <folder>`).

**Best practice:** the grader should not be the session that produced the
run. Grade in a fresh session, and say in `graded_by` if you couldn't.
