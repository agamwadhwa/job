# Model defence: 40 hostile questions

> **Status: needs re-mapping.** `model/` holds no workbook yet (only `README.md`). These questions are written against a **standard Pune residential feasibility**: REF-W, implemented in `ref_w.py`, with the notional cell map below. When your own workbook is added to `model/` (after the repo is made private), re-map every `Sheet!Cell` reference to your actual cells and replace REF-W numbers with yours. A cloud session can do the re-mapping: point it at this file and the workbook.

## Notional cell map (REF-W)

| Sheet | Cell | Item | REF-W value |
|---|---|---|---|
| Inputs | C4 | Gross plot (sq m) | 8,094 |
| Inputs | C5 | Deductions (road widening, reservations) | 394 |
| Inputs | C6 | Net plot for FSI | 7,700 |
| Inputs | C7 | Road width (m) | 18 |
| Inputs | C8 / C9 / C10 | Basic / premium / TDR FSI | 1.1 / 0.5 / 0.9 |
| Inputs | C11 | Ancillary % | 60% |
| Inputs | C12 | Carpet efficiency (carpet ÷ FSI area) | 78% |
| Inputs | C13 | Construction area multiplier | 1.30 |
| Inputs | C15 | Sale rate (₹/sq ft carpet) | 7,500 |
| Inputs | C16 | Construction rate (₹/sq ft construction area) | 2,300 |
| Inputs | C17 | TDR price (₹/sq ft) | 2,200 |
| Inputs | C18 | ASR open land rate (₹/sq m) | 9,000 |
| Inputs | C19 / C20 | Premium % / ancillary % of ASR | 50% / 10% |
| Inputs | C21 | Other statutory (₹/sq ft FSI area) | 150 |
| Inputs | C22 / C23 / C24 | Professional fees / marketing / admin | 4% / 5% / 2% |
| Inputs | C25 / C26 | Land (₹ cr) / stamp duty | 16.0 / 7% |
| Inputs | C27 | Finance (₹ cr) | 5.0 |
| Inputs | C29 / C30 / C31 | Approval / construction / absorption quarters | 3 / 12 / 12 |
| Inputs | C32 | Booking % (rest construction-linked) | 10% |
| Inputs | C33 | Discount rate | 14% |
| Area | D7 / D8 / D9 | FSI area / carpet / construction area (sq ft) | 3,31,528 / 2,58,592 / 4,30,987 |
| Costs | E5:E16 | Cost lines; E17 total | total 162.9 |
| Costs | E19 / E20 | Profit / margin | 31.0 / 16.0% |
| CashFlow | row 10 / 20 / 30 / 31 | Collections / outflows / net / cumulative | — |
| CashFlow | C35 / C36 / C37 | IRR (annualised) / peak funding / NPV | 23.6% / 54.7 / — |
| Sensitivity | B5:F10 | Price × absorption IRR grid | see Case 09 |

**The rule for every answer:** name the cell, state the assumption and its source, give the sensitivity, and say what you'd do to verify it. If you don't know, say what you'd check. Never defend a number you can't source.

---

## Land head (10)

### Q1 [model] Your efficiency is 78% (Inputs!C12). Where does that come from? Our architect gets 72%.
It's an assumption for a UDCPR building with 60% ancillary, where common areas are largely covered by ancillary FSI. I haven't yet validated it against a design. A 6-point drop to 72% cuts carpet by 7.7%, and revenue falls by about ₹15 cr, which takes the margin from 16% to about 9.6% (IRR about 14.9%). I'd defer to the architect's area statement: it's the single number I'd replace first. My question back would be what drives the 72%: balcony treatment, floor plate shape, or fire staircases counted in FSI?

### Q2 [model] Why do you deduct only 394 sq m (Inputs!C5)?
It's a placeholder (about 5%) for road widening. The real figure comes from DP remarks. I'd also check whether UDCPR lets us keep FSI on the surrendered strip in-situ or take TDR for it. If in-situ FSI applies, the FSI base in Inputs!C6 should be gross, not net, which adds about 5% of area. Both directions matter, which is why the DP remarks are my first diligence item.

### Q3 [model] You've assumed an 18 m road for 0.9 TDR (Inputs!C7, C10). Have you measured it?
No. The input comes from the listing. The TDR cap depends on the existing, physically open road width as the authority reads it, not the DP proposal. If the road is 15 m, TDR drops (verify the table band) and FSI area falls roughly 10%. I'd measure on site, check the DP remarks, and confirm with the liaison consultant how PMC treats this road.

### Q4 [model] Land at ₹8 cr/acre (Inputs!C25). The landowner wants ₹10 cr. Can we pay it?
At ₹10 cr/acre, IRR falls from 23.6% to 19.4% and margin to about 13.8%. If our hurdle is a 20% IRR, the residual land value at 20% (discounted) is about ₹19.4 cr, i.e. ₹9.7 cr/acre. So ₹10 cr is just over the line on IRR and well below on margin. I'd counter at ₹8.5–9 or propose a JDA around 13–15% revenue share.

### Q5 [model] Why is TDR loaded in one shot at Q3 (CashFlow row 20)?
Simplification: the model buys all TDR at plan approval. In practice we could load in phases if approvals are staged by building, which lowers peak funding. The trade-off is TDR price risk: at ₹3,000, IRR falls to 18.5%. I'd show both a one-shot and a staged version.

### Q6 [model] What's your land comp evidence?
Currently none in the model: ₹8 cr/acre is an assumption. I'd add a comps tab with 3–5 recent registered deals or IPC-reported transactions, converted to ₹ per FSI sq ft and adjusted for road width, approval status and date. REF-W's ₹483/FSI sq ft should fall in that range, or the land input is wrong.

### Q7 [model] Where are title and approval risks in your model?
They aren't in the cash flows. They're binary risks that a model handles poorly. I'd add an approval delay scenario (+2 quarters costs about 2 IRR points plus carry and inflation) and treat title as a gating condition, not a sensitivity. The risk section of the IC note covers what the model can't.

### Q8 [model] Your 12-quarter absorption (Inputs!C31) implies how many units a month?
About 380 units (at about 680 sq ft average) over 36 months ≈ 10.5 per month. In a Wagholi-like micro-market selling about 120 units a month, that's a 9% share. It's plausible for a fair-share launch, but only if months of inventory aren't excessive. The evidence should come from MahaRERA QPRs of 5–8 comps, which I'd add as a tab.

### Q9 [model] What if the 60% ancillary isn't available to us?
Then FSI area falls from 30,800 to 19,250 sq m. Common areas would eat into the FSI area available for flats, and the efficiency would drop sharply. The project wouldn't work at this land price. Ancillary is standard under UDCPR for residential (verify current rules), so this is a question for the liaison consultant, not an assumption to flex.

### Q10 [model] Why not model parking income?
Prudence. Parking and other charges are excluded from revenue (Inputs has no parking line). Under RERA, covered parking can be sold. If comps show ₹3–5 lakh per slot, adding it lifts revenue by maybe 2–4%. I'd add it only with comps evidence.

## CFO (10)

### Q11 [model] Your IRR (CashFlow!C35) is unlevered. What's the equity IRR?
The model doesn't show it yet. With construction finance funding part of construction at 11–12%, equity IRR would be higher than 23.6%, and the exact lift depends on drawdown. I'd add a debt block (drawdown, interest, sweep repayment) rather than guess. Case 05-type interest on a ₹60 cr line is ₹15.5 cr, so the structure matters.

### Q12 [model] Finance cost is a ₹5 cr plug (Inputs!C27). Justify it.
I can't fully. It's a placeholder for a modest CF line. A ₹60 cr line over 14 quarters at 11.5% costs about ₹15.5 cr, which would cut the margin to about 10.6%. The honest fix is to model the debt properly. Until then I'd present the unlevered IRR as the primary metric and flag the margin as pre-financing-structure.

### Q13 [model] Is GST in your revenue?
No. Under-construction residential GST (5% without ITC, 1% affordable: verify) is collected from buyers and paid to government, so it's excluded from both revenue and cost. If the model included it, revenue would be overstated.

### Q14 [model] Why no cost escalation?
It's a limitation. Construction runs from Q3 to Q14, so the midpoint is about 2 years out. At 5% annual inflation, average cost is about 10% above today's rate, roughly ₹10 cr, which is equivalent to the "cost +10%" sensitivity (IRR 16.6%). Equally, I've assumed no price escalation. I'd add both as paired inputs and show the net effect, and never add price escalation without cost escalation.

### Q15 [model] Your peak funding is ₹54.7 cr (CashFlow!C36). Can we fund it?
That's your call, but here's what drives it. Land (₹17.1 cr) + early approvals (Q0), plus TDR ₹16.4 cr (Q3), plus early construction, before collections catch up at about Q6. Levers: land payment schedule (see `03-technical/01` P5), staged TDR, or a JDA (peak falls to about ₹41 cr at a 15% revenue share).

### Q16 [model] Your margin is 16%. Our board wants 20%. Why should we look at this?
Because IRR (23.6%) and margin measure different things, and this project is short and capital-light for its size. But I'd put it plainly: at the board's margin rule, this deal only works at about ₹8.7 cr of land (the 20%-margin residual), or as a JDA. I'd present both.

### Q17 [model] Collections: 10% booking + 90% construction-linked (Inputs!C32). Is that realistic?
It's a typical construction-linked plan shape. Actual plans have specific milestones (plinth, slabs, finishing, possession). A 10/90 split applied to progress smooths them. A front-loaded plan (20% on booking) lowers peak funding but may slow sales. I'd replicate our actual standard plan.

### Q18 [model] What happens to cash if unsold units remain at completion?
The model assumes sell-out matches construction (12 quarters each). If sales lag, units sold after completion pay in full on booking, which the model captures. What it doesn't capture is holding cost (maintenance, property tax) and price pressure on completed inventory. At 20-quarter absorption, IRR is 13.4% before those costs.

### Q19 [model] Walk me through how RERA's 70% affects this model.
It doesn't bind here. 70% of revenue (₹136 cr) is less than land plus construction cost (about ₹144 cr), so no cash is trapped beyond cost. It would matter if margins were much higher. The model should still show the RERA account as a separate ledger for the lender.

### Q20 [model] Admin at 2% of revenue (Inputs!C24): what's in it?
Project-level overheads: site admin, security, insurance, legal. Corporate overhead allocation isn't included. If the firm allocates HQ costs to projects, add 1–2% and margin falls accordingly.

## Lender (10)

### Q21 [model] What's the security cover over the loan life?
Not in the model yet. I'd add a quarterly cover calc: (receivables from sold units + unsold inventory at 75% of current price) ÷ loan outstanding, and flag any quarter below 1.5×. The weakest point is likely around Q5–Q7: cost spent, receivables still small.

### Q22 [model] Your 12-quarter construction (Inputs!C30) for stilt + 14–22 floors: realistic?
For about 4.3 lakh sq ft of construction area, 36 months is achievable with a competent contractor, but tight if basements are involved. My site experience says the slab cycle is the thing to check: 7–10 days per floor typical. A 4-quarter delay costs only about 1.2 IRR points in the model (to 22.4%), but carry and inflation aren't modelled.

### Q23 [model] What's your cost-to-complete at Q8?
From CashFlow row 20: remaining construction after Q8 (Q9–Q14) is 6/12 of ₹103.1 cr ≈ ₹52 cr, plus marketing on the remaining sales. I'd compare it with receivables from units sold by Q8 to compute cost-to-complete cover. I'd add that ratio as a row for the lender.

### Q24 [model] How did you set ₹2,300/sq ft (Inputs!C16)?
It's an assumption within a ₹2,200–2,700 range for a Pune mid-segment tower on construction area. I haven't validated it with a QS. Structure is about 35–40%, finishes 25–30%, MEP about 20%. A 10% overrun costs 7 IRR points (to 16.6%). I'd get a contractor's indicative BOQ rate before IC.

### Q25 [model] Where's the contingency?
There isn't an explicit one. I'd add 5% of construction (about ₹5 cr) at the land stage, reducing as design firms up. Without it, the cost line is a point estimate that will almost certainly be exceeded.

### Q26 [model] Your sale rate (Inputs!C15) is ₹7,500. Comps?
Not yet in the model. I'd build a comps tab from MahaRERA-registered projects within 1–2 km: carpet rate, launch date, units sold per quarter. If comps cluster at ₹7,100 (like the competitor in Case 09), my rate is 5% high and IRR drops to about 18%.

### Q27 [model] What's the downside case?
Price −5%, absorption 16 quarters, cost +5%, together. I haven't run that exact combination. The single-variable results are: price −10% → 12.2%, absorption 20q → 13.4%, cost +10% → 16.6%. I'd add a combined scenario switch in the Sensitivity sheet.

### Q28 [model] Break-even price?
About ₹6,211/sq ft, a 17.2% fall, holding everything else. I'd present it alongside historical Pune price drawdowns (verify with IPC data).

### Q29 [model] Your land is outright. What if we lend and the landowner has a claim?
The model can't answer that. It's a title question. As a lender I'd want the title certificate, search report, public notice results and mutation history before sanction, and a mortgage on the land.

### Q30 [model] Why should I trust a model you built with AI help?
Because I can walk through every line and change any input live, and the numbers reproduce in a separate script (`ref_w.py`) that gives the same outputs. The AI helped me build structure faster. The assumptions and checks are mine to defend, and I've shown you where they're weak (efficiency, finance, contingency). Only say this if it's true of your own workbook.

## Promoter (10)

### Q31 [model] In one line: do we buy it?
At ₹16 cr, it clears an IRR hurdle but not a 20% margin. I'd buy at ₹14 cr, or do a JDA at ≤ 15% revenue share, subject to clean title and a confirmed 18 m road.

### Q32 [model] My friend's project next door made 35%. Why is yours 16%?
Different land cost (earlier purchase), different efficiency, no TDR cost if they're on a different road, or a different timing in the cycle. I'd ask for their numbers, but I wouldn't assume their margin transfers.

### Q33 [model] Can we increase the price to ₹8,000?
+6.7% on price lifts IRR to about 30%. But it's only credible if comps and our product justify it. At ₹8,000 against a competitor at ₹7,100, absorption would likely slow, and the grid shows slower absorption costs more than the price gain.

### Q34 [model] Why not build more floors and sell more?
FSI caps the area, not floors. Extra floors on the same FSI means a smaller footprint and more open space, not more area to sell. More area needs more FSI (TDR up to the cap) or a different regulation.

### Q35 [model] Can we launch before approvals?
No. RERA prohibits advertising or selling before registration, which needs sanctioned plans and CC. The model starts sales at Q3 for this reason.

### Q36 [model] What's the worst that can happen?
Title defect found after launch: sales and lender disbursements freeze. Model-wise, a 20-quarter sell-out at a 10% lower price gives about 6.8% IRR. The model can show the second. The first is a diligence issue.

### Q37 [model] What's the one number you're least sure of?
Efficiency (Inputs!C12), then absorption. Both change revenue by double digits and neither is yet evidence-based.

### Q38 [model] If you had one more week, what would you add?
A comps tab (price, absorption), a debt block with equity IRR, cost escalation paired with price escalation, a contingency line, and the architect's area statement replacing my efficiency assumption.

### Q39 [model] Explain IRR to me without jargon.
It's the annual interest rate the project effectively pays us on our money, taking into account when we put money in and when we get it back. 23.6% here means our money grows roughly like a deposit at 23.6% a year, if the assumptions hold.

### Q40 [model] Why should I believe you over my experience?
You shouldn't, on the market. Your experience of the micro-market is better than my assumptions. The model's value is that it shows which of your judgements matter most: price and absorption, not the ₹1 cr in approvals. Tell me the rate and velocity you believe, and I'll show you what they mean.

---

## How to practise
- Have someone read a random question (`python interview-guide/quiz.py --function model --n 5`).
- Answer in under 60 seconds, pointing at the cell.
- After each session, list the questions where you said "I'd check". Those are the next model improvements.
