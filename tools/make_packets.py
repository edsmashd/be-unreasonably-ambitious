"""Build blind judge packets: one file per scenario with shuffled anonymous labels.

Usage: python3 make_packets.py SEED
Reads evals/responses/*.md and evals/scenarios.json.
Writes evals/packets/SNN.md and evals/packets/key.json (label -> candidate).
"""
import json, os, random, re, sys, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
ev = root / os.environ.get("EVALS_DIR", "evals")
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
scen = json.loads((ev / "scenarios.json").read_text())
resp = {}
for f in sorted((ev / "responses").glob("*.md")):
    parts = re.split(r"^## (S\d\d)\s*$", f.read_text(), flags=re.M)
    resp[f.stem] = {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}
out = ev / "packets"; out.mkdir(exist_ok=True)
key = {}
for s in scen:
    cands = [c for c in resp if s["id"] in resp[c]]
    random.shuffle(cands)
    labels = [chr(65 + i) for i in range(len(cands))]
    key[s["id"]] = dict(zip(labels, cands))
    body = [f"# {s['id']}: user message\n\n> {s['prompt']}\n\n## Rubric\n"]
    body += [f"R{i+1}. {r}" for i, r in enumerate(s["rubric"])]
    for lab, c in zip(labels, cands):
        body.append(f"\n\n---\n## Response {lab}\n\n{resp[c][s['id']]}")
    (out / f"{s['id']}.md").write_text("\n".join(body))
(out / "key.json").write_text(json.dumps(key, indent=1))
print("candidates:", list(resp), "| packets:", len(scen))
