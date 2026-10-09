"""Score a review-checklist eval run against the answer key.

Usage (from the repo root):
    python3 .claude/skills/review-checklist/evals/run_evals.py [results.json]

With no argument, scores the newest file in evals/results/. A results file
has the same shape as expected.json's "cases": per file, true (pass) or
false (flag) for owner, measure, scope and problem_first.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
NAMES = {"owner": "owner named", "measure": "success measure", "scope": "scope bounded", "problem_first": "problem first"}


def main():
    key = json.loads((HERE / "expected.json").read_text())
    checks, expected = key["checks"], key["cases"]
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
    else:
        runs = sorted((HERE / "results").glob("*.json"))
        if not runs:
            sys.exit("No results files in evals/results/. Run the skill in eval mode first.")
        path = runs[-1]
    got = json.loads(path.read_text())
    got = got.get("cases", got)

    total = right = false_alarms = misses = 0
    per_check = {c: [0, 0] for c in checks}
    wrong_rows, missing = [], []
    for case, exp in expected.items():
        if case not in got:
            missing.append(case)
            continue
        for c in checks:
            total += 1
            per_check[c][1] += 1
            if got[case].get(c) == exp[c]:
                right += 1
                per_check[c][0] += 1
            else:
                if exp[c] and got[case].get(c) is False:
                    false_alarms += 1
                    kind = "false alarm (flagged a pass)"
                else:
                    misses += 1
                    kind = "missed flag (passed a problem)"
                wrong_rows.append(f"  {case:<38} {NAMES[c]:<16} {kind}  [{exp['why']}]")

    print(f"review-checklist evals · {path.name}")
    print(f"Score: {right}/{total} checks correct ({right / max(total, 1):.0%})")
    print(f"False alarms: {false_alarms} · Missed flags: {misses} · Cases missing from results: {len(missing)}")
    print("\nBy check:")
    for c in checks:
        r, t = per_check[c]
        print(f"  {NAMES[c]:<16} {r}/{t}")
    if wrong_rows:
        print("\nWrong answers:")
        print("\n".join(wrong_rows))
    if missing:
        print("\nMissing cases: " + ", ".join(missing))
    sys.exit(0 if right == total and not missing else 1)


if __name__ == "__main__":
    main()
