"""Plain-English lint for SKILL.md files, loosely based on ASD-STE100 limits.

Reports: lines, words, sentences over 20 words, likely passive voice,
vague words, and frontmatter checks from Anthropic's skill rules.
Usage: python3 lint.py FILE [FILE...]
"""
import re, sys

VAGUE = r"\b(various|appropriate|relevant|properly|etc|leverage|robust|seamless|utilize|in order to|stuff|things like)\b"
PASSIVE = r"\b(is|are|was|were|be|been|being)\s+(\w+ed|\w+en)\b"

def body_sentences(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)       # drop code blocks
    text = re.sub(r"^\|.*\|$", " ", text, flags=re.M)        # drop tables
    text = re.sub(r"^>.*$", " ", text, flags=re.M)           # drop quotes
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)     # links -> text
    text = re.sub(r"[*_`#]", "", text)
    parts = re.split(r"(?<=[.!?:;])\s+|\n\s*[-0-9]+\.?\s+|\n\n", text)
    return [p.strip() for p in parts if len(p.split()) > 2]

def lint(path):
    raw = open(path).read()
    fm, body = "", raw
    if raw.startswith("---"):
        _, fm, body = raw.split("---", 2)
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    sents = body_sentences(body)
    long_ = [s for s in sents if len(s.split()) > 20]
    passive = re.findall(PASSIVE, body, re.I)
    vague = re.findall(VAGUE, body, re.I)
    words = len(body.split())
    return {
        "file": path.split("/")[-1],
        "lines": raw.count("\n"),
        "words": words,
        "approx_tokens": int(words * 1.35),
        "sentences": len(sents),
        "over_20_words": len(long_),
        "pct_long": round(100 * len(long_) / max(1, len(sents)), 1),
        "passive_hits": len(passive),
        "vague_hits": len(vague),
        "name_ok": bool(name and re.fullmatch(r"[a-z0-9-]{1,64}", name.group(1).strip())),
        "desc_chars": len(desc.group(1)) if desc else 0,
        "desc_ok": bool(desc and 0 < len(desc.group(1)) <= 1024),
        "body_under_500_lines": body.count("\n") < 500,
        "examples_long": [s[:90] for s in long_[:3]],
    }

if __name__ == "__main__":
    for f in sys.argv[1:]:
        r = lint(f)
        ex = r.pop("examples_long")
        print(" | ".join(f"{k}={v}" for k, v in r.items()))
        for e in ex: print("   long:", e)
