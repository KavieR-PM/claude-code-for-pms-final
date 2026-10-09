"""Score a release-investigation run against rubric.json.

Usage (from the repo root):
    python3 .claude/skills/release-investigation/evals/run_evals.py --layout repo
    python3 .claude/skills/release-investigation/evals/run_evals.py --layout run --dir <run folder>
Options:
    --judge <file>   judge answers (default: newest evals/results/*-judge.json
                     whose "target" matches this layout/dir)

'auto' checks run here. 'judge' checks are read from the judge file, which a
grader writes by following GRADER.md. Exit code is 0 only if every check passes.
"""
import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]


def read_text(path):
    if path.suffix == ".pptx":
        return ""
    return path.read_text(errors="ignore")


def resolve(files, base):
    return [base / f for f in files]


def run_auto(check, paths):
    present = [p for p in paths if p.exists()]
    if not present:
        return False, "output file missing: " + ", ".join(str(p.relative_to(REPO)) if p.is_relative_to(REPO) else str(p) for p in paths)
    if check.get("exists"):
        return True, "file exists"
    text = "\n".join(read_text(p) for p in present)
    if "max_words" in check:
        n = len(re.findall(r"\b\w[\w'’-]*\b", text))
        return n <= check["max_words"], f"{n} words (max {check['max_words']})"
    missing = [pat for pat in check.get("all", []) if not re.search(pat, text, re.I | re.S)]
    return not missing, ("all patterns found" if not missing else "not found: " + "; ".join(missing))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--layout", choices=["repo", "run"], default="repo")
    ap.add_argument("--dir", default=None, help="run folder (layout=run)")
    ap.add_argument("--judge", default=None)
    a = ap.parse_args()

    rubric = json.loads((HERE / "rubric.json").read_text())
    base = REPO if a.layout == "repo" else Path(a.dir).resolve()
    target = "repo" if a.layout == "repo" else str(base)
    layout = rubric["layouts"][a.layout]

    judge = {}
    jpath = Path(a.judge) if a.judge else None
    if not jpath:
        cands = []
        for p in sorted((HERE / "results").glob("*-judge.json")):
            try:
                if json.loads(p.read_text()).get("target") == target:
                    cands.append(p)
            except json.JSONDecodeError:
                pass
        jpath = cands[-1] if cands else None
    if jpath:
        judge = json.loads(jpath.read_text()).get("answers", {})

    rows, phase_score = [], {}
    passed = total = not_judged = 0
    for c in rubric["checks"]:
        total += 1
        if c["type"] == "auto":
            ok, detail = run_auto(c, resolve(layout.get(c["output"], []), base))
        else:
            ans = judge.get(c["id"])
            if ans is None:
                ok, detail = False, "not judged yet"
                not_judged += 1
            else:
                ok, detail = bool(ans.get("pass")), ans.get("evidence", "")
        passed += ok
        ph = phase_score.setdefault(c["phase"], [0, 0]); ph[0] += ok; ph[1] += 1
        rows.append((c["id"], c["phase"], c["type"], ok, detail, c["why"]))

    print(f"release-investigation evals · layout={a.layout} · judge={jpath.name if jpath else 'none'}")
    print(f"Score: {passed}/{total} checks passed ({passed / total:.0%})" + (f" · {not_judged} not judged" if not_judged else ""))
    print("\nBy phase:")
    for ph, (p, t) in phase_score.items():
        print(f"  {ph:<14} {p}/{t}")
    fails = [r for r in rows if not r[3]]
    if fails:
        print("\nFailed or not judged:")
        for cid, ph, typ, ok, detail, why in fails:
            print(f"  {cid:<3} [{typ}] {why}\n       -> {detail}")
    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
