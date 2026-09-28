"""Drill random interview questions from every markdown file in interview-guide/.

A question is any heading of the form `### Q<n> [tag] question text` or `### P<n> [tag] title`.
The answer is everything under it up to the next heading of level 1–3.

Usage:
    python interview-guide/quiz.py                       # 10 random questions, any tag
    python interview-guide/quiz.py --function feas --n 10
    python interview-guide/quiz.py --weak --n 5          # prioritise topics you marked weak
    python interview-guide/quiz.py --list-tags

Tags: land, appr, jda, feas, cf, am, cap, model, behav, firm.
After each answer, press Enter to reveal it, then type y (got it) or n (weak).
"n" answers are logged to interview-guide/weak_topics.json.
"""
from __future__ import annotations

import argparse
import json
import random
import re
from collections import Counter
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOG = HERE / "weak_topics.json"
HEAD = re.compile(r"^###\s+([QP]\d+)\s+\[([a-z]+)\]\s+(.*)$")
STOP = re.compile(r"^#{1,3}\s")


def load_questions(root: Path = HERE) -> list[dict]:
    questions = []
    for md in sorted(root.rglob("*.md")):
        lines = md.read_text(encoding="utf-8").splitlines()
        i = 0
        while i < len(lines):
            m = HEAD.match(lines[i])
            if not m:
                i += 1
                continue
            body = []
            j = i + 1
            while j < len(lines) and not STOP.match(lines[j]):
                body.append(lines[j])
                j += 1
            questions.append({"id": f"{md.relative_to(root)}#{m.group(1)}", "tag": m.group(2),
                              "question": m.group(3).strip(), "answer": "\n".join(body).strip(),
                              "file": str(md.relative_to(root))})
            i = j
    return questions


def load_log() -> dict:
    if LOG.exists():
        try:
            return json.loads(LOG.read_text())
        except json.JSONDecodeError:
            pass
    return {"misses": {}, "tags": {}}


def save_log(log: dict) -> None:
    LOG.write_text(json.dumps(log, indent=2, ensure_ascii=False) + "\n")


def pick(questions: list[dict], n: int, tag: str | None, weak: bool, log: dict) -> list[dict]:
    pool = [q for q in questions if tag is None or q["tag"] == tag]
    if not pool:
        return []
    if weak and log["misses"]:
        weights = [1 + 3 * log["misses"].get(q["id"], {}).get("count", 0) + log["tags"].get(q["tag"], 0)
                   for q in pool]
        chosen, remaining = [], list(zip(pool, weights))
        while remaining and len(chosen) < n:
            q, _ = random.choices(remaining, weights=[w for _, w in remaining])[0]
            chosen.append(q)
            remaining = [(p, w) for p, w in remaining if p is not q]
        return chosen
    return random.sample(pool, min(n, len(pool)))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--function", "--tag", dest="tag", help="only questions with this tag")
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--weak", action="store_true", help="weight towards previously missed questions/tags")
    ap.add_argument("--list-tags", action="store_true")
    ap.add_argument("--seed", type=int)
    args = ap.parse_args()
    if args.seed is not None:
        random.seed(args.seed)

    questions = load_questions()
    if args.list_tags:
        for tag, count in sorted(Counter(q["tag"] for q in questions).items()):
            print(f"{tag:<6} {count}")
        return

    log = load_log()
    chosen = pick(questions, args.n, args.tag, args.weak, log)
    if not chosen:
        print(f"No questions found for tag {args.tag!r}. Try --list-tags.")
        return

    score = 0
    for k, q in enumerate(chosen, 1):
        print(f"\n[{k}/{len(chosen)}] ({q['tag']}) {q['question']}\n    from {q['file']}")
        input("    Answer aloud, then press Enter to reveal… ")
        print("\n" + q["answer"] + "\n")
        verdict = input("    Got it? [y/n] ").strip().lower()
        if verdict.startswith("n"):
            entry = log["misses"].setdefault(q["id"], {"question": q["question"], "tag": q["tag"], "count": 0})
            entry["count"] += 1
            entry["last"] = date.today().isoformat()
            log["tags"][q["tag"]] = log["tags"].get(q["tag"], 0) + 1
        else:
            score += 1
    save_log(log)
    weak_tags = ", ".join(f"{t} ({c})" for t, c in sorted(log["tags"].items(), key=lambda x: -x[1]))
    print(f"\nScore {score}/{len(chosen)}. Weak topics so far: {weak_tags or 'none'}")


if __name__ == "__main__":
    main()
