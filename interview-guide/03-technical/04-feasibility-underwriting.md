# Feasibility & underwriting

The core file for land/BD and deal-analyst roles. Uses REF-W (see `00-how-to-use.md`) throughout. Every figure is a labelled **assumption**. Market rates in Pune and Mumbai move quarterly, so refresh them from IPC reports and MahaRERA comps before an interview.

## Primer: concepts before mechanics

**What a feasibility answers.** Three questions, in order:
1. **What can we build?** The area statement: plot → FSI → FSI area → carpet → construction area.
2. **What will it sell for, and how fast?** Price and absorption, from comparables.
3. **Is it worth the risk?** Costs and timing give profit, margin, IRR and peak funding, which are then compared with the firm's hurdles and stressed.

A feasibility is a **decision tool**, not a forecast. Its job is to show which few assumptions decide the answer. In REF-W those are price, absorption and TDR cost, so the conversation with the promoter can focus on them.

**The area chain (UDCPR residential, REF-W):**

| Step | REF-W | Note |
|---|---|---|
| Gross plot | 8,094 sq m (2 acres) | 1 acre = 4,047 sq m = 43,560 sq ft |
| Less road widening/deductions | 394 sq m | from DP remarks. In-situ FSI or TDR may compensate (**verify**) |
| Net plot for FSI | 7,700 sq m | |
| × (basic 1.1 + premium 0.5 + TDR 0.9) | × 2.5 = 19,250 sq m | TDR depends on road width (18 m here) |
| + ancillary 60% | + 11,550 = 30,800 sq m | |
| FSI area | 30,800 sq m = **3,31,528 sq ft** | × 10.764 |
| Carpet (RERA) at 78% | **2,58,592 sq ft** | the key efficiency assumption |
| Construction area at 1.30× FSI area | **4,30,987 sq ft** | adds parking, services, non-FSI areas |

**Revenue** = carpet × rate (₹7,500) = ₹193.9 cr. Parking, floor rise and other charges are excluded for prudence. GST on under-construction residential (5% without ITC, 1% affordable: **verify**) is collected and paid through, so it's excluded from revenue and cost.

**Cost stack (REF-W, ₹ cr):**

| Item | ₹ cr | ₹/sq ft carpet | Basis |
|---|---|---|---|
| Land | 16.00 | 619 | ₹8 cr/acre |
| Stamp duty | 1.12 | 43 | 7% |
| Premium FSI | 1.73 | 67 | 0.5 × 7,700 × 50% × ASR ₹9,000/sq m |
| TDR | 16.41 | 635 | 74,594 sq ft × ₹2,200 |
| Ancillary premium | 1.04 | 40 | 11,550 sq m × 10% × ₹9,000 |
| Other statutory/approvals | 4.97 | 192 | ₹150/sq ft of FSI area |
| Construction | 99.13 | 3,833 | ₹2,300/sq ft construction area |
| Professional fees | 3.97 | 153 | 4% of construction |
| Marketing & brokerage | 9.70 | 375 | 5% of revenue |
| Admin/overheads | 3.88 | 150 | 2% of revenue |
| Finance | 5.00 | 193 | plug for a modest CF line |
| **Total** | **162.9** | **6,299** | |
| **Profit** | **31.0** | 1,199 | **16.0% of revenue** |

**Return metrics:**
- **Margin on revenue** (16.0%): what promoters quote first. The hurdle for mid-segment Pune is often 18–25% (assumption).
- **Unlevered project IRR** (23.6%): uses quarterly cash flows, with collections 10% on booking plus 90% linked to construction progress. Finance cost is excluded because the IRR is unlevered.
- **Equity IRR:** higher with construction finance. Depends on the debt drawdown.
- **Peak funding** (₹54.7 cr at about Q5): how much capital the project needs at its worst point. It decides whether the firm can afford the deal at all.
- **Equity multiple / profit ÷ peak funding:** ₹36 cr pre-finance surplus ÷ ₹54.7 cr ≈ 0.66×.

**Absorption** is the silent killer. A construction-linked payment plan means cash comes as the building rises, but only for flats already sold. Unsold flats at completion bring no collections until sold. That's why REF-W's IRR drops from 23.6% to 13.4% when sell-out stretches from 12 to 20 quarters.

**Sensitivities to run every time:** price ±10%, absorption +50%, construction cost +10%, TDR price +35%, approval delay +2 quarters. Plus a **break-even** on the most sensitive variable. On REF-W, price can fall **17.2%** (to about ₹6,211/sq ft) before profit hits zero.

## 15 interview questions with model answers

### Q1 [feas] Take me from a 2-acre plot to sellable area.
2 acres is 8,094 sq m. First I'd check DP remarks for road widening or reservations and deduct them. Say that leaves 7,700 sq m net. Then check road width, because the TDR cap depends on it. On an 18 m road under UDCPR: basic 1.1, premium 0.5, TDR 0.9, so 2.5 FSI, or 19,250 sq m. Add ancillary FSI at 60%, 11,550 sq m, for 30,800 sq m, which is about 3.32 lakh sq ft of FSI area. Carpet at about 78% efficiency gives roughly 2.59 lakh sq ft of RERA carpet to sell. For cost, construction area is larger than FSI area because of parking and services, so about 1.3×, or 4.3 lakh sq ft. The two numbers I'd flag as needing the architect's confirmation are the efficiency and the TDR band.

### Q2 [feas] What's the difference between carpet, built-up, super built-up and FSI area?
Carpet (as RERA defines it) is the usable area inside the flat's external walls, including internal walls, excluding balconies, services shafts and open terraces. It's the only legal basis for pricing now. Built-up adds the external walls and, in older usage, the balcony. Super built-up adds a share of common areas like lobbies, staircases and amenities. It was the traditional pricing basis before RERA and is still used informally. FSI area is a regulatory measure: the area that counts against the permissible FSI under the DCR. It isn't a sales measure. In a feasibility I convert FSI area to carpet using an efficiency ratio (78% in REF-W), and FSI area to construction area (1.3×) for cost. Mixing these up is the most common feasibility error.

### Q3 [feas] How do you set the sale price for a new launch?
Build it from comparables. Take 5–8 RERA-registered projects within 1–2 km with similar product, and record the carpet rate, launch date, possession date, and units sold per month from MahaRERA QPRs. Adjust each for location (main road vs interior), brand, amenities, size mix and possession timing (a ready project commands a premium over a launch). The adjusted range gives a base price. Then position it: launch pricing is usually slightly below the market to drive early velocity, with escalation by phase. I'd sanity-check against resale prices in older projects nearby and against affordability: at the ticket size for the target buyer, what EMI results? REF-W uses ₹7,500/sq ft for Wagholi (assumption: verify with current comps).

### Q4 [feas] How do you estimate absorption, and why does it matter so much?
From comparables: units sold per month in similar nearby projects over recent quarters (MahaRERA QPRs, IPC micro-market data), adjusted for our pricing and brand. Cross-check against micro-market totals: if the area sells 300 units a month across all projects and we launch 700 units, a 10–15% share implies about 30–45 units a month, so 15–23 months to sell out. It matters because collections are construction-linked only for sold units. Slow sales mean the developer funds construction with equity or debt. And unsold stock at completion carries marketing and holding costs, and sometimes price cuts. In REF-W, stretching sell-out from 12 to 20 quarters cuts IRR from 23.6% to 13.4%. That's more damage than a 10% cost overrun.

### Q5 [feas] Margin on revenue vs IRR: which matters more?
They answer different questions, so both. Margin (16% on REF-W) tells you how much buffer there is against price or cost shocks, since profit as a share of revenue is how much prices can fall before you lose money, roughly. IRR (23.6%) tells you the return per unit of capital per unit of time. It rewards speed and penalises delay. A project can have a high margin and poor IRR if it takes 8 years, like many redevelopment projects. It can have a low margin and high IRR if it's capital-light and fast, like plotted development or DM. Promoters of family-run developers often think in margin. Listed developers and funds think in IRR and ROCE. I'd present both, plus peak funding, because that decides whether we can afford the deal at all.

### Q6 [feas] What's peak funding and how do you reduce it?
Peak funding is the most negative point of the cumulative cash flow: the maximum capital the project needs before collections catch up. In REF-W it's about ₹54.7 cr around quarter 5, after the land, the TDR purchase and early construction, before construction-linked collections build up. To reduce it: defer land payments (payment schedule, or a JDA). Buy TDR in stages as floors go up rather than all at plan approval, if the regulations and design allow. Launch earlier: pre-launch bookings, if RERA-compliant after registration. Front-load the payment plan (e.g. 20% on booking instead of 10%). Use construction finance. Each has a cost: a JDA gives up margin, front-loaded plans slow sales, and debt adds interest. So the question is always which lever is cheapest for this deal.

### Q7 [feas] Walk me through the cost stack. Which items are most uncertain?
REF-W totals ₹6,300 per sq ft of carpet: land about ₹620, stamp about ₹45, premium and ancillary about ₹105, TDR about ₹635, other approvals about ₹190, construction about ₹3,830, professional fees about ₹155, marketing about ₹375, admin about ₹150 and finance about ₹195. The most uncertain are TDR, a market price that can move 30% in a year; construction, where the risk is steel and cement, labour, and specification creep; and the efficiency ratio, which isn't a cost but drives revenue per sq ft of construction. Land is certain once contracted. Statutory charges are formula-based but linked to ASR. So my sensitivities focus on TDR, construction and price.

### Q8 [feas] What construction cost would you assume for a Pune mid-rise, and why?
I'd give a range and a build-up rather than one number. For a stilt + 14–22 floor residential tower in Pune's mid-segment, ₹2,200–2,700 per sq ft of construction area is a plausible range for civil, MEP and finishes (**assumption**: refresh with a current QS or contractor quote). REF-W uses ₹2,300. The build-up: structure (RCC, formwork, reinforcement) about 35–40% of cost, finishes about 25–30%, MEP about 20%, external development and amenities the rest. My contracting experience helps here: I've seen how RA bills break down by item [FILL: only if true], and how variations and escalation add up. I'd add a 5% contingency for a feasibility at the land stage.

### Q9 [feas] How do you account for the time value of money in a feasibility?
Two ways. First, build a periodic cash-flow model (quarterly in REF-W): land and approvals at the start, TDR at plan approval, construction spread over 12 quarters, collections as 10% on booking plus 90% linked to construction progress for units sold. From that, compute IRR and NPV at the cost of capital. Second, include finance cost explicitly if there's construction finance: interest on the drawn balance each period. The margin-only "static" feasibility ignores timing, and so overstates the attractiveness of slow projects. Common mistakes: putting all revenue at the end, which understates IRR, or all at the start, which overstates it. Also forgetting that unsold units don't generate construction-linked collections.

### Q10 [feas] A landowner says "the builder next door paid ₹12 cr per acre". How do you respond?
Check whether it's a like-for-like comparison. Per acre is meaningless without road width, zone, FSI and title status. The neighbour may be on a 24 m road (more TDR), in a different zone, with approvals in place, or have paid in a JDA where headline "value" includes future revenue. I'd convert both parcels to land cost per FSI sq ft and compare. Then show the landowner my residual land value: at REF-W assumptions, a 16% margin supports about ₹16 cr for 2 acres (₹8 cr per acre), and a 20% target supports only about ₹8.7 cr (₹4.4 cr per acre). Nowhere near ₹12 cr per acre. If they insist, the gap is bridgeable only by a JDA, where they take part of the price risk, or by walking away.

### Q11 [feas] What's residual land value?
The maximum you can pay for land and still earn the target return. You compute it by starting from revenue and subtracting every cost except land, plus the required profit. On REF-W: revenue ₹193.9 cr, costs excluding land and stamp ₹145.8 cr, target margin 20% = ₹38.8 cr. Residual = 193.9 − 145.8 − 38.8 = ₹9.3 cr. Divide by 1.07 for stamp and it's about ₹8.7 cr for 2 acres, or ₹4.4 cr per acre. At a 16% target it's the ₹16 cr we assumed. That shows how sensitive land value is to the margin target: 4 points of margin halves what we can pay. That's why RLV is quoted with its assumptions, never alone.

### Q12 [feas] How do you stress-test a feasibility before IC?
Single-variable sensitivities first: price ±10%, absorption 12 → 16 → 20 quarters, construction +10%, TDR +35%, approval delay +2 quarters, efficiency −3 points. Then a combined downside: price −5%, absorption 16 quarters, cost +5%, all together. Then break-evens: what price or absorption makes profit zero, or makes IRR equal the cost of capital? On REF-W: price −10% → IRR 12.2%; absorption 20 quarters → 13.4%; cost +10% → 16.6%; TDR ₹3,000 → 18.5%; 4-quarter construction delay → 22.4%; break-even price about ₹6,211/sq ft. The IC question is then "how likely is the downside, and what's our mitigation?", for example a JDA to share price risk, or phasing to limit exposure.

### Q13 [feas] Should the feasibility include price escalation?
Show a base case with modest escalation and a flat-price case. Escalation is real: phases or towers launched later usually sell higher, and ignoring it understates value. But it's also where optimistic feasibilities hide their optimism. My rule: escalation no higher than the micro-market's long-run price CAGR from IPC data, applied per phase or per year from launch. Never applied to units already sold. Always paired with cost escalation, typically similar or higher since construction inflation runs 4–6% a year. Where the escalation assumption is what gets the project over the hurdle, the project doesn't clear the hurdle. I'd say that clearly at IC.

### Q14 [feas] What's the difference between project IRR and equity IRR?
Project (unlevered) IRR uses the project's cash flows before any debt: it measures the asset's return. Equity IRR uses cash flows to equity after debt drawdown, interest and repayment. If debt costs less than the project IRR, leverage raises equity IRR, and it raises risk: fixed interest must be paid whether units sell or not. REF-W's unlevered IRR is 23.6%. With construction finance at 11–12% (assumption) funding part of construction, equity IRR would be higher. The size of the lift depends on drawdown timing. Funds think in equity IRR (after their debt). Developers' IC decks show both. I'd never present only the levered figure, because it can make a weak project look good.

### Q15 [feas] What would make you recommend "no" on a feasibility that clears the hurdle?
Several things. The hurdle is cleared only through optimistic assumptions: price above comps, fast absorption, escalation. Title or approval risk that isn't priced: a pending suit, access through someone else's land, a reservation. Concentration: too much of the pipeline in one micro-market or one ticket size. Execution: the site needs capabilities we don't have, like deep basements or a height beyond our experience. Counterparty: a landowner with a history of disputes. Market timing: large competing launches nearby in the same quarter. A feasibility is a necessary condition, not a sufficient one. The recommendation note should say what would need to be true for "yes", and how we'd verify it.

## 5 numeric problems

### P1 [feas] Area statement in 5 minutes
**Given:** 3 acres gross in Hinjawadi Phase 2. Road widening 5% of gross. 24 m road → TDR 1.15 (**verify**). Basic 1.1, premium 0.5. Ancillary 60%. Efficiency 78%. Construction area 1.3× FSI area.

**Solution:**
- Gross = 3 × 4,047 = 12,141 sq m. Net = 95% = 11,534 sq m
- FSI factor = 1.1 + 0.5 + 1.15 = 2.75 → 31,718 sq m. × 1.6 ancillary = **50,749 sq m** = 5,46,261 sq ft FSI area
- Carpet = 78% = **4,26,084 sq ft**
- Construction area = 1.3 × 5,46,261 = **7,10,140 sq ft**

**Point to make:** a 24 m road adds 0.25 FSI over an 18 m road. On 11,534 sq m that's about 49,650 sq ft more FSI area (with ancillary), worth tens of crores of revenue. Road width is worth checking twice.

### P2 [feas] Cost stack and margin (REF-W)
**Given:** as in the primer.

**Solution:** total cost ₹162.9 cr, revenue ₹193.9 cr → profit **₹31.0 cr = 16.0%**. Cost per carpet sq ft ₹6,299 vs price ₹7,500, so ₹1,199/sq ft of profit.

**Point to make:** at 16%, REF-W is below a typical 18–20% hurdle. Options: negotiate land lower, go JDA, raise efficiency with the architect, or pass.

### P3 [feas] Quick IRR by hand
**Given (annual, ₹ cr):** Y0 −20 (land); Y1 −35 (approvals, TDR, construction); Y2 +10; Y3 +40; Y4 +40.

**Solution:**
- Total in 90, total out 55 → profit 35, multiple **1.64×**
- NPV at 14% = −20 − 30.70 + 7.69 + 27.00 + 23.68 = **+₹7.7 cr**, so IRR > 14%
- Try 20%: −20 − 29.17 + 6.94 + 23.15 + 19.29 = +0.21 → just above zero
- Try 21%: −20 − 28.93 + 6.83 + 22.58 + 18.66 = −0.86
- **IRR ≈ 20.2%**

**Point to make:** interviewers want the method (bracket, then interpolate), not decimals.

### P4 [feas] Price sensitivity and break-even
**Given:** REF-W. Marketing (5%) and admin (2%) vary with revenue, so 93% of any revenue change reaches profit.

**Solution:**
- 1% price change = 1% × ₹193.9 cr = ₹1.94 cr revenue → ₹1.80 cr profit
- Price −10% → profit = 31.0 − 18.0 = **₹13.0 cr (7.4% margin)**
- Break-even price fall = 31.0 ÷ (193.9 × 0.93) = **17.2%** → break-even rate ≈ **₹6,211/sq ft**

**Point to make:** a 16% margin project is roughly a 17% price-fall buffer. Pune's post-2014 slowdown saw flat-to-negative real prices for years in some micro-markets (speculation: verify with IPC history). 17% isn't a comfortable cushion.

### P5 [feas] Absorption and months of inventory
**Given (assumptions):** in Wagholi, 8 comparable projects sold a combined 360 units last quarter, and have 3,600 unsold units. Your project will have 380 units (about 680 sq ft average carpet × 380 ≈ 2.59 lakh sq ft).

**Solution:**
- Micro-market monthly sales = 360 ÷ 3 = 120 units. Months of inventory = 3,600 ÷ 120 = **30 months** (high: above about 18 is stressed, a rule of thumb)
- If you capture a fair share (380 of 3,980 total supply ≈ 9.5%), you'd sell ≈ 9.5% × 120 ≈ **11.5 units/month → 33 months ≈ 11 quarters**. That's close to REF-W's 12-quarter assumption, but only if you win a fair share against 30 months of competing stock.
- If you capture only 7 units/month: 380 ÷ 7 ≈ 54 months ≈ 18 quarters → IRR falls toward the 13–15% range (REF-W at 20 quarters is 13.4%).

**Point to make:** always tie your absorption assumption to a share of micro-market sales. A number without that link is a guess.

## Common traps and wrong answers
- **Using super built-up or FSI area as sellable area.** RERA carpet is the pricing basis.
- **Forgetting ancillary FSI**, or applying it to the plot area instead of the FSI area.
- **Ignoring road width** when setting TDR.
- **Quoting one IRR without timing assumptions**, or presenting a levered IRR as project IRR.
- **Putting all revenue at completion**, or assuming collections for unsold flats.
- **Including GST in revenue.**
- **Using a land comp per acre without FSI adjustment.**
- **Adding price escalation but not cost escalation.**
- **Answering "what's your IRR?" with a number but no sensitivity.** Always follow with "and it's most sensitive to X".
