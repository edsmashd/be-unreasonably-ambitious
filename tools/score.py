"""Un-blind judge JSON and report per-candidate scores.

Usage: python3 score.py
Reads evals/judgements/*.json and the matching evals/packets-seedN/key.json.
Writes evals/results.md and evals/results.json.
"""
import json, os, re, statistics as st, pathlib
from collections import defaultdict

ev = pathlib.Path(__file__).resolve().parent.parent / os.environ.get("EVALS_DIR", "evals")
rows = []  # (judge, scenario, candidate, rubric_pct, overall)
for f in sorted((ev / "judgements").glob("*.json")):
    seed = re.search(r"seed(\d+)", f.name).group(1)
    key = json.loads((ev / f"packets-seed{seed}" / "key.json").read_text())
    data = json.loads(f.read_text())
    for sid, labs in data.items():
        for lab, v in labs.items():
            r = v.get("rubric", [])
            rows.append((f.stem.split("-")[0], sid, key[sid][lab],
                         100 * sum(r) / len(r) if r else 0, v.get("overall", 0), v.get("note", "")))

by = defaultdict(list)
for j, s, c, rp, ov, _ in rows: by[c].append((j, s, rp, ov))
res = {}
for c, xs in by.items():
    res[c] = {"rubric_pct": round(st.mean(x[2] for x in xs), 1),
              "overall": round(st.mean(x[3] for x in xs), 2),
              "min_overall": min(x[3] for x in xs),
              "n": len(xs)}
order = sorted(res, key=lambda c: -res[c]["overall"])

# per-scenario overall, averaged across judges
sc = defaultdict(lambda: defaultdict(list))
for j, s, c, rp, ov, _ in rows: sc[s][c].append(ov)
# inter-rater: correlation of overall scores between the first two judges that rated the same items
pair = defaultdict(dict)
for j, s, c, rp, ov, _ in rows: pair[(s, c)][j] = ov
judges = sorted({j for j, *_ in rows})
agree = None
pairs = [(x, y) for i, x in enumerate(judges) for y in judges[i + 1:]]
for x, y in pairs:
    a = [(v[x], v[y]) for v in pair.values() if x in v and y in v]
    if len(a) > 2:
        xs, ys = zip(*a)
        agree = f"{x} vs {y}: r = {round(st.correlation(xs, ys), 2)} over {len(a)} shared items"
        break

lines = ["| Candidate | Rubric met % | Overall (1-10) | Worst overall | Ratings |", "|---|---|---|---|---|"]
lines += [f"| {c} | {res[c]['rubric_pct']} | {res[c]['overall']} | {res[c]['min_overall']} | {res[c]['n']} |" for c in order]
lines += ["", "Per-scenario overall (mean across judges):", "",
          "| Scenario | " + " | ".join(order) + " |", "|---" * (len(order) + 1) + "|"]
for s in sorted(sc):
    lines.append(f"| {s} | " + " | ".join(str(round(st.mean(sc[s][c]), 1)) if sc[s][c] else "-" for c in order) + " |")
lines += ["", f"Inter-rater agreement: {agree}"]
(ev / "results.md").write_text("\n".join(lines) + "\n")
(ev / "results.json").write_text(json.dumps({"summary": res, "rows": rows}, indent=1))
print("\n".join(lines))
