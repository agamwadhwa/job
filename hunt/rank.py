"""Rank every role in hunt/roles.json and write reports/ranking.md.

Usage: python -m hunt.rank
"""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from hunt.scoring import DEAD, FUNCTIONS, best_pairs, enrich

ROOT = Path(__file__).resolve().parent.parent
ROLES = ROOT / "hunt" / "roles.json"
REPORT = ROOT / "reports" / "ranking.md"
BAR = {0: "·", 1: "▁", 2: "▅", 3: "█"}


def main() -> None:
    roles = [enrich(r) for r in json.loads(ROLES.read_text())]
    live = sorted((r for r in roles if r.get("status") not in DEAD), key=lambda r: -r["priority"])
    keys = list(FUNCTIONS)

    lines = [f"# Role ranking — {date.today():%d %b %Y}", "",
             "Priority = 55% alignment to the 12 functions + 30% reach + 15% culture (AmbitionBox).",
             "Function strip order: " + ", ".join(v[0] for v in FUNCTIONS.values()), "",
             "| # | Pri | Align | Combo | Firm | Role | Exp | Culture | Functions | Status |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(live, 1):
        strip = "".join(BAR[r["scores"].get(k, 0)] for k in keys)
        link = f"[{r['role']}]({r['src']})" if r.get("src") else r["role"]
        lines.append(f"| {i} | {r['priority']} | {r['align']} | {r['combo']} | {r['firm']} | {link} | "
                     f"{r.get('exp','')} | {r.get('cRating') or 'n/a'} | `{strip}` | {r.get('status','')} |")

    lines += ["", "## Best two-step combinations", "",
              "| Coverage | Functions ≥2 | First move | Second move |", "|---|---|---|---|"]
    for cov, n, a, b in best_pairs(roles):
        lines.append(f"| {cov}% | {n}/12 | {a['firm']} – {a['role']} | {b['firm']} – {b['role']} |")

    REPORT.parent.mkdir(exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n")
    print(f"Wrote {REPORT.relative_to(ROOT)} with {len(live)} live roles")


if __name__ == "__main__":
    main()
