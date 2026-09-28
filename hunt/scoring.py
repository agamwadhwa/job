"""Scoring engine for the real-estate job hunt.

Every role is scored 0-3 on the 12 developer functions. The weights favour
land, JDA and feasibility, the functions the career plan is built around.
"""
from __future__ import annotations

from itertools import combinations

FUNCTIONS = {
    "land": ("Land & title", 3),
    "appr": ("Approvals & liaison", 2),
    "jda": ("JDA structuring", 3),
    "feas": ("Feasibility & underwriting", 3),
    "design": ("Design coordination", 1),
    "cf": ("Project & construction finance", 2),
    "proc": ("Procurement & contracts", 1),
    "deliv": ("Delivery", 1),
    "cost": ("Cost control & RA billing", 1),
    "lease": ("Institutional leasing", 1),
    "am": ("Asset management & monetization", 2),
    "cap": ("Capital raising", 2),
}
WEIGHTS = {k: w for k, (_, w) in FUNCTIONS.items()}
MAX_COVERAGE = 3 * sum(WEIGHTS.values())  # 66
REACH = {"A": 100, "B": 65, "C": 30}
DEFAULT_CULTURE = 3.6
DEAD = {"Closed", "Rejected", "Keywords only"}


def coverage(scores: dict) -> float:
    return sum(WEIGHTS[k] * scores.get(k, 0) for k in WEIGHTS)


def alignment(scores: dict) -> int:
    return round(100 * coverage(scores) / MAX_COVERAGE)


def combo(scores: dict) -> str:
    deal = max(scores.get(k, 0) for k in ("land", "jda", "feas"))
    money = max(scores.get(k, 0) for k in ("cf", "am", "cap"))
    if deal >= 2 and money >= 2:
        return "Deal + money"
    if sum(scores.get(k, 0) >= 2 for k in ("land", "jda", "feas", "appr")) >= 3:
        return "Deal core"
    if money >= 2:
        return "Money side"
    return "Single-function"


def culture_value(rating) -> float:
    try:
        return float(rating)
    except (TypeError, ValueError):
        return DEFAULT_CULTURE


def priority(scores: dict, reach: str, culture_rating=None) -> int:
    return round(
        0.55 * alignment(scores)
        + 0.30 * REACH.get(reach, 30)
        + 0.15 * (culture_value(culture_rating) / 5 * 100)
    )


def enrich(role: dict) -> dict:
    s = role.get("scores") or {}
    role = dict(role)
    role["align"] = alignment(s)
    role["combo"] = combo(s)
    role["nstrong"] = sum(1 for k in WEIGHTS if s.get(k, 0) >= 2)
    role["priority"] = priority(s, role.get("reach", "C"), role.get("cRating"))
    return role


def best_pairs(roles: list[dict], top: int = 6) -> list[tuple[int, int, dict, dict]]:
    """Two reachable roles (a first job and a next move) whose combined coverage is highest."""
    pool = [r for r in roles if r.get("reach") in ("A", "B") and r.get("status") not in DEAD]
    out = []
    for a, b in combinations(pool, 2):
        if a["firm"] == b["firm"]:
            continue
        union = {k: max(a["scores"].get(k, 0), b["scores"].get(k, 0)) for k in WEIGHTS}
        out.append((round(100 * coverage(union) / MAX_COVERAGE),
                    sum(1 for k in WEIGHTS if union[k] >= 2), a, b))
    out.sort(key=lambda x: (-x[0], -x[1]))
    return out[:top]
