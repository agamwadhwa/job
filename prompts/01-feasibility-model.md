# Cloud session: build a feasibility model you can defend

Paste into a Claude Code cloud session on this repo. First upload your current model to `model/` (make the repo private before you do).

---
Build `model/` into a land feasibility model for a Pune urban-fringe residential plot that compares outright purchase with a JDA. Every number must be traceable and defensible in an interview.

1. Read the existing workbook in `model/` if there is one. List every hard-coded input and mark where each came from (IGR e-ASR, UDCPR 2020, PMRDA circular, MahaRERA filing, or "assumption").
2. Rebuild the model as `model/build.py`, which writes `model/feasibility.xlsx` using openpyxl. It needs these sheets:
   - Inputs, with a source column
   - Area statement: plot, deductions, base FSI, premium FSI, TDR, ancillary, carpet, saleable
   - Costs: land/JDA share, approvals and premiums, construction, soft costs
   - Revenue and absorption
   - Monthly cash flow
   - Returns: IRR, NPV, margin, peak funding
   - Sensitivity: price, cost, absorption, FSI
   - Outright vs JDA comparison
3. Add `tests/test_model.py` to check that areas reconcile, the cash flow sums, and IRR is stable.
4. Write `model/DEFENCE.md`: 40 hostile interview questions (from a land head, a CFO and a lender), each with a two-to-three-line answer that points to a specific cell or assumption.
5. Write `model/GO_NO_GO.md`: a two-page management note in the format a developer's deal team uses. Cover the recommendation, key numbers, risks and next steps.
Keep all assumptions conservative and labelled. Do not invent data sources. Where data is missing, say so and use a clearly marked placeholder.
