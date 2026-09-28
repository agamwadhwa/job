"""REF-W reference feasibility: the numbers used throughout interview-guide/.

Pure Python, no dependencies. Every input is an assumption; change them and re-run.

Usage:
    python interview-guide/ref_w.py              # base case + sensitivities
    python interview-guide/ref_w.py --grid       # IRR grid: absorption x price (Case 09)
"""
from __future__ import annotations

import argparse

SQFT_PER_SQM = 10.7639

BASE = dict(
    net_plot_sqm=7700, basic=1.1, premium=0.5, tdr=0.9, ancillary=0.60,
    efficiency=0.78, cons_multiplier=1.30,
    rate=7500, cons_rate=2300, tdr_price=2200, asr=9000,
    premium_pct_asr=0.50, ancillary_pct_asr=0.10, statutory_psf=150,
    prof_fees=0.04, marketing=0.05, admin=0.02,
    land_cr=16.0, stamp=0.07, finance_cr=5.0,
    appr_q=3, cons_q=12, absorb_q=12, booking=0.10, discount=0.14,
)


def areas(p: dict) -> dict:
    fsi_base = p["net_plot_sqm"] * (p["basic"] + p["premium"] + p["tdr"])
    fsi_sqm = fsi_base * (1 + p["ancillary"])
    fsi_sf = fsi_sqm * SQFT_PER_SQM
    return dict(fsi_base_sqm=fsi_base, fsi_sqm=fsi_sqm, fsi_sf=fsi_sf,
                carpet_sf=fsi_sf * p["efficiency"], cons_sf=fsi_sf * p["cons_multiplier"],
                tdr_sf=p["net_plot_sqm"] * p["tdr"] * SQFT_PER_SQM)


def costs(p: dict) -> dict:
    a = areas(p)
    rev = a["carpet_sf"] * p["rate"] / 1e7
    cons = a["cons_sf"] * p["cons_rate"] / 1e7
    return dict(
        revenue=rev,
        land=p["land_cr"], stamp=p["land_cr"] * p["stamp"],
        premium=p["net_plot_sqm"] * p["premium"] * p["asr"] * p["premium_pct_asr"] / 1e7,
        tdr=a["tdr_sf"] * p["tdr_price"] / 1e7,
        ancillary=a["fsi_base_sqm"] * p["ancillary"] * p["asr"] * p["ancillary_pct_asr"] / 1e7,
        statutory=a["fsi_sf"] * p["statutory_psf"] / 1e7,
        construction=cons, prof_fees=cons * p["prof_fees"],
        marketing=rev * p["marketing"], admin=rev * p["admin"], finance=p["finance_cr"],
    )


def cash_flows(p: dict) -> list[float]:
    """Quarterly unlevered cash flows (finance cost excluded)."""
    c = costs(p)
    aq, cq, sq = p["appr_q"], p["cons_q"], p["absorb_q"]
    n = aq + max(cq, sq) + 1
    out = [0.0] * n
    out[0] += c["land"] + c["stamp"] + 2.0                       # land, stamp, early approvals
    out[aq - 1] += c["statutory"] - 2.0 + c["premium"] + c["ancillary"]
    out[aq] += c["tdr"]                                          # TDR loaded at plan approval
    for q in range(aq, aq + cq):
        out[q] += (c["construction"] + c["prof_fees"]) / cq
    sold = [1 / sq if aq <= q < aq + sq else 0.0 for q in range(n)]
    cum, billed_prev, flows = 0.0, 0.0, []
    for q in range(n):
        cum += sold[q]
        progress = min(max((q - (aq - 1)) / cq, 0.0), 1.0)
        billed = cum * (p["booking"] + (1 - p["booking"]) * progress)
        inflow = (billed - billed_prev) * c["revenue"]
        billed_prev = billed
        out[q] += sold[q] * c["revenue"] * (p["marketing"] + p["admin"])
        flows.append(inflow - out[q])
    return flows


def irr(flows: list[float]) -> float:
    npv = lambda r: sum(f / (1 + r) ** i for i, f in enumerate(flows))
    lo, hi = -0.9, 5.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if npv(mid) > 0 else (lo, mid)
    return mid


def summary(p: dict) -> dict:
    c = costs(p)
    total = sum(v for k, v in c.items() if k != "revenue")
    flows = cash_flows(p)
    running, peak = 0.0, 0.0
    for f in flows:
        running += f
        peak = min(peak, running)
    return dict(revenue=c["revenue"], total_cost=total, profit=c["revenue"] - total,
                margin=(c["revenue"] - total) / c["revenue"],
                irr=(1 + irr(flows)) ** 4 - 1, peak_funding=-peak)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--grid", action="store_true")
    args = ap.parse_args()
    if args.grid:
        prices = [6750, 7125, 7500, 7875]
        print("quarters | " + " | ".join(f"₹{x:,}" for x in prices))
        for q in [8, 12, 16, 20, 24]:
            row = [f"{summary({**BASE, 'absorb_q': q, 'rate': x})['irr']:.1%}" for x in prices]
            print(f"{q:>8} | " + " | ".join(row))
        return
    a, c, s = areas(BASE), costs(BASE), summary(BASE)
    print(f"FSI area {a['fsi_sf']:,.0f} sq ft | carpet {a['carpet_sf']:,.0f} | construction {a['cons_sf']:,.0f}")
    for k, v in c.items():
        print(f"  {k:<13} ₹{v:7.2f} cr")
    print(f"Total cost ₹{s['total_cost']:.1f} cr | profit ₹{s['profit']:.1f} cr ({s['margin']:.1%}) | "
          f"IRR {s['irr']:.1%} | peak funding ₹{s['peak_funding']:.1f} cr")
    print("Sensitivities (unlevered IRR):")
    for label, change in [("price -10%", {"rate": 6750}), ("price +10%", {"rate": 8250}),
                          ("absorption 20q", {"absorb_q": 20}), ("construction +4q", {"cons_q": 16}),
                          ("TDR ₹3,000", {"tdr_price": 3000}), ("construction cost +10%", {"cons_rate": 2530}),
                          ("land ₹10 cr/acre", {"land_cr": 20.0})]:
        print(f"  {label:<24} {summary({**BASE, **change})['irr']:.1%}")


if __name__ == "__main__":
    main()
