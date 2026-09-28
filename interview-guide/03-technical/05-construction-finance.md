# Project & construction finance

Covers LTC, LTV, DSCR, security cover, escrow, the RERA 70% account, and lender diligence. Rates are **assumptions** (Indian bank/NBFC developer lending in 2026). Regulatory limits are **verify current**.

## Primer: concepts before mechanics

**Why developers borrow.** Construction-linked payment plans mean buyers pay as the building rises, but only for flats already sold, and with a lag. The gap between spending and collecting is funded by equity or debt. Debt is cheaper than equity when the project is sound, so developers use **construction finance (CF)**: a loan to build a specific project, repaid from its sales.

**Who lends what (India, typical):**

| Lender | Product | Rate (assumption) | Will fund land? |
|---|---|---|---|
| Banks | CF, LRD | 9–11.5% | Generally **no**. RBI rules restrict bank lending for land acquisition (**verify current**) |
| HFCs/NBFCs (e.g. Tata Capital) | CF, structured CF, LAP | 11–14% | Limited, with conditions |
| AIFs/credit funds (e.g. Kotak Alts) | Structured debt (NCDs), mezzanine, last-mile | 14–20% | Yes, including land and approvals stage |
| SWAMIH-type funds | Last-mile funding for stalled projects | Varies | No, completion only |

**Key ratios:**
- **LTC (loan to cost)** = loan ÷ total project cost (or ÷ construction cost, depending on the lender's definition). Lenders keep developer equity at risk: for example, LTC capped at 50–65% of total cost (assumption).
- **LTV (loan to value)** = loan ÷ value of security. For CF, security value = receivables from sold units + value of unsold inventory (often with a haircut) + land.
- **Security cover** = security value ÷ loan outstanding. Lenders want ≥ 1.5–2.0× (assumption).
- **DSCR** (for lease-backed loans) = NOI ÷ annual debt service (interest + principal). LRD lenders want ≥ 1.2–1.4× (assumption).
- **Cost-to-complete cover** = (receivables from sold units + undrawn committed funds) ÷ remaining cost to complete. Critical for stalled or late-stage projects.

**The escrow structure.** All collections go into a **collection/escrow account**. From there: 70% to the **RERA designated account** (usable only for that project's land and construction, with withdrawals certified in proportion to completion) and 30% to the developer's free account. The lender sits on top of this: it controls the escrow and **sweeps** a % of collections for repayment. Structuring must respect RERA. The lender's repayment from the RERA account is permissible only for loans used for that project's land/construction (**verify current MahaRERA position**).

**Security package (typical):**
- Mortgage on the project land and unsold inventory
- Hypothecation of receivables
- Escrow control
- Personal guarantee of the promoters
- Corporate guarantee
- Sometimes a pledge of shares in the project SPV
- A DSRA for LRD

**Disbursement mechanics:** tranches linked to construction milestones, certified by the **lender's independent engineer (LIE)**. Each tranche checks cost incurred vs budget, stage of work, sales performance vs plan, and compliance with covenants.

**Covenants:** minimum sales (units or ₹/quarter), minimum average price (to prevent fire-sale discounting), maximum cost overrun, no further debt without consent, cash sweep %, and an information covenant (monthly MIS, RERA QPRs).

## 15 interview questions with model answers

### Q1 [cf] What's construction finance and how is it repaid?
Construction finance is a term loan to a developer to fund construction of a specific project, disbursed in tranches as construction progresses and certified by the lender's engineer. It's repaid from the project's own sales collections, not from the developer's general income. All buyer payments go into an escrow account the lender controls, and an agreed share (say 20–40% of collections) is swept to repay principal and interest. Repayment usually starts after a moratorium, once sales and collections build up, and the loan closes before or around completion. Security is the project itself (land, unsold inventory, receivables) plus promoter guarantees. The lender is effectively betting on sales velocity at the underwritten price.

### Q2 [cf] Define LTC and LTV. Which matters more for a CF lender?
LTC is loan ÷ project cost. It tells the lender how much of the project the developer has funded with its own money, so how much skin in the game. LTV is loan ÷ value of the security. It tells the lender whether selling the security would repay the loan. For construction finance, both matter at different times. At sanction, LTC is the discipline: a cap (say 50–60% of total cost) ensures the developer's equity absorbs the first losses. During the loan, LTV and security cover are what the lender monitors, because the value of receivables and unsold inventory changes with sales and price. A project with a good LTC can drift to a poor LTV if prices fall or sales stall. That's why covenants include minimum sales and price.

### Q3 [cf] Why can't banks lend for land, and who fills the gap?
RBI rules generally prohibit banks from lending for land acquisition by developers: the prudential view is that land is speculative, illiquid and hard to value (**verify current RBI master direction and exceptions**). Banks can fund construction once land is owned and approvals are in. The gap in land and early-stage funding is filled by NBFCs, HFCs, and especially AIFs and credit funds, through structured debt like NCDs at higher rates, perhaps 14–20% (assumption). That's why fund raises like Kotak Alts' US$1 bn 14th RE fund matter for developers: they're the source of land and approvals-stage capital ([Realty n More](https://realtynmore.com/kotak-alts-secures-1-billion-adia-and-nps-korea/)).

### Q4 [cf] Explain the RERA 70% account from a lender's point of view.
RERA requires 70% of collections to go into a designated account, usable only for that project's land and construction costs, with withdrawals certified in proportion to completion. For a lender this is mostly positive: money can't be diverted to other projects or new land, so the project is more likely to complete, which protects the lender's security. The complication is repayment. The lender must structure the escrow so that repayment of a loan taken for this project's construction can be made from the designated account, which is generally allowed (**verify current MahaRERA guidance**). The 30% free portion may be pledged as well. Lenders therefore map the flow: collections → escrow → 70/30 split → sweep. Then they check that the sweep % is achievable within those limits.

### Q5 [cf] What is security cover and how do you compute it for a residential project?
Security cover = value of what the lender can realise ÷ outstanding loan. For residential CF: receivables (balance payable by buyers of sold units, which is fairly certain) + unsold inventory at current price with a haircut (say 20–25%, for fire-sale risk) + sometimes land value, all divided by loan outstanding. Lenders typically want 1.5–2.0× (assumption). It changes as the project progresses. Early on, cover rests on land and unsold inventory. Later, on receivables. The dangerous moment is mid-construction with weak sales: cost has been spent, receivables are small, and unsold inventory is valued at a price that may not hold. That's why covenants trigger additional security or cash sweeps when cover falls below a threshold.

### Q6 [cf] What's DSCR, and where is it used in real estate?
DSCR = net operating income ÷ debt service (interest + principal) over a period, usually annual. It's the core metric for lease rental discounting (LRD), where a bank lends against a leased commercial building's rent. Example: NOI ₹11.04 cr and annual debt service ₹9.80 cr gives DSCR 1.13×. Lenders typically want 1.2–1.4× (assumption), so this loan (₹70 cr at 9.5% over 12 years) is too large. At 1.3×, the maximum loan would be about ₹60.7 cr. For residential construction finance DSCR isn't meaningful, because there's no stable operating income. Security cover and cost-to-complete cover are used instead.

### Q7 [cf] Walk me through a lender's diligence on a Pune CF proposal.
Four streams. Legal: the title certificate and search, approvals (plan, CC, RERA), JDA terms if any, and litigation. Technical, by the LIE: plans vs site, construction stage, cost budget reasonableness, cost incurred vs claimed, and quality. Financial: the project cash flow (sales plan, price, collections, cost to complete), promoter group leverage, other projects' performance, and past lender defaults (CIBIL). Market: comps for price and absorption, and months of inventory in the micro-market. Output: a sanction note with loan size (LTC-limited), tenor, rate, security package, covenants (min sales, min price, cost overrun limit, sweep %), and disbursement conditions. My contracting background helps most on the technical stream: I know what a cost budget for a stilt+15 tower looks like and where overruns hide.

### Q8 [cf] What's a cash sweep and how would you set the %?
A cash sweep is the % of every collection that the lender takes automatically from the escrow for repayment. Set it so the loan is fully repaid comfortably before completion, typically with repayment done when about 70–80% of units are sold or construction is 80–90% complete. At the same time, the developer must keep enough to fund the remaining construction. The method: project collections quarterly, deduct the RERA-required construction spend, and find the sweep % that repays the loan by the target date, with headroom. If the required sweep leaves the developer short of cost-to-complete, the loan is too large or the tenor too short. Many deals also have a step-up sweep: a higher % if sales or price covenants are breached.

### Q9 [cf] What's cost-to-complete cover and why do last-mile lenders focus on it?
Cost-to-complete cover = (receivables from sold units + committed undrawn funding) ÷ remaining cost to complete the project. If it's above 1, the project can finish from its own resources. Last-mile lenders, like SWAMIH or credit funds financing stalled projects, focus on it because their risk is non-completion: if the building finishes, sold units pay their balances on possession and unsold units can be sold. Example: cost to complete ₹60 cr, receivables ₹35 cr → cover 0.58×, so the project can't finish without new money. Add unsold inventory of 1.2 lakh sq ft at ₹7,000 with a 20% haircut (₹67.2 cr) and total cover is 1.7×, enough to justify last-mile funding with priority over existing lenders.

### Q10 [cf] What covenants would you put in a CF loan, and which is most important?
Minimum sales per quarter (units and ₹). Minimum average realisation, so the developer doesn't dump inventory to meet sales covenants. Maximum cost overrun (for example 10%) before additional equity is required. Construction milestones. No additional debt or change in control without consent. Cash sweep %, with step-ups. RERA compliance. Monthly MIS and quarterly LIE reports. The most important, in my view, is the minimum sales/price pair, because sales velocity at the underwritten price drives everything: collections, security cover and repayment. A project that's building well but not selling is the classic stressed CF case. The covenant gives the lender the right to act early: a higher sweep, additional security, or step-in.

### Q11 [cf] What's LRD and why do developers with commercial assets use it?
Lease Rental Discounting is a loan against the future rent of a leased commercial property. The bank discounts the rent stream, lending an amount such that the rent (via escrow) services the loan, typically up to 10–15 years depending on lease tenure. Developers use it to unlock capital from completed, leased offices or malls without selling them, and redeploy the cash into new projects. It's cheaper than CF because the cash flow is contracted and stable: rates are closer to bank lending rates (assumption: 8.5–10%). The key underwriting items are tenant quality, lease tenure and lock-in (WALE), escalation clauses, DSCR, and LTV on the property's market value.

### Q12 [cf] Mezzanine vs senior debt vs structured equity?
Senior debt has first charge on security and first claim on cash flows. It's cheapest because it's safest: bank CF at around 10–11%. Mezzanine sits behind senior: second charge, or security over the promoter's shares or other assets. It costs more (15–20%) and often has an equity kicker. Structured equity is equity in the project SPV with a pre-agreed IRR and a promoter buyback obligation, which is economically closer to debt but ranks after all lenders. Returns are around 18–24% with upside sharing (all assumptions). Developers choose based on the stage (land stage rules out banks), existing leverage, and how much control they're willing to give. Funds use all three depending on the deal's risk.

### Q13 [cf] A project's sales are 40% below plan. What does the lender do?
First, diagnose: price too high, product mismatch, market slowdown, or developer execution issues? The lender's covenant triggers typically allow a step-up in the cash sweep, a stop on further disbursements until sales recover, additional security or promoter equity infusion, and in severe cases a price reset, or step-in to appoint another developer or sell in bulk. Practically, lenders prefer to fix sales rather than enforce: approve a targeted price cut, a revised payment plan, or channel-partner incentives, and let the project complete. Enforcement on residential projects is slow and destroys value. My view: the lender's best tool is early warning, which is why monthly MIS and LIE reports matter.

### Q14 [cf] How does a lender's independent engineer (LIE) add value?
The LIE is the lender's eyes on site. They certify that each disbursement matches actual work done: stage of construction and quantities executed vs the budget. They review the cost budget at sanction, flag overruns and delays, check quality, and confirm that construction follows approved plans (deviations are a legal risk to the security). They also verify cost-to-complete estimates. Good LIE reports catch problems months before they show up in financial statements, like a contractor slowing down because of unpaid bills. My contracting experience is directly relevant: I've seen RA bills and measurement books [FILL: only if true], and I know how progress can be overstated, for example by counting materials at site as work done.

### Q15 [cf] What happens to a lender when a developer goes into insolvency (IBC)?
Under the IBC, homebuyers are treated as financial creditors and sit on the committee of creditors alongside lenders. That dilutes the lender's control of the process. A resolution plan may prioritise completion for homebuyers. Project-wise insolvency has been recognised in some cases, where only the defaulting project is resolved (**verify current jurisprudence**). For a CF lender, this means security may not translate into quick recovery, and outcomes depend on the resolution plan. That's one reason lenders favour SPV structures (one project per company), strong escrow control, and early intervention before default, and why last-mile funding with priority is attractive in stalled projects.

## 5 numeric problems

### P1 [cf] Sizing a CF loan on REF-W
**Given (assumptions):** total project cost ₹162.9 cr, of which construction + professional fees = ₹103.1 cr. The lender caps the loan at 50% of total project cost and at 70% of construction cost, whichever is lower. The loan is for construction only (bank). Land is paid by equity.

**Solution:**
- 50% of total cost = ₹81.5 cr
- 70% of construction = ₹72.2 cr
- **Maximum loan ≈ ₹72 cr** (the lower). The developer funds land (₹17.1 cr), TDR and approvals (₹24.2 cr) and the rest of construction from equity plus collections.
- In practice, REF-W's peak funding is ₹54.7 cr (unlevered). The developer would size CF around that need, say ₹50–55 cr, not the maximum, to avoid paying interest on idle money.

**Point to make:** the eligible amount and the needed amount are different. Size to the cash-flow gap plus a buffer.

### P2 [cf] LRD sizing with DSCR
**Given (assumptions):** a leased office with annual rent ₹12 cr. Leakage and opex borne by the owner 8% → NOI ₹11.04 cr. The loan is at 9.5% per year for 12 years, amortising monthly. The lender requires a DSCR of 1.3×.

**Solution:**
- Monthly rate r = 0.095/12 = 0.00792. n = 144.
- Loan ₹70 cr → EMI factor gives annual debt service ₹9.80 cr → DSCR = 11.04/9.80 = **1.13×**. Fails.
- Loan ₹80 cr → DS ₹11.20 cr → DSCR 0.99×. Fails.
- Max debt service at 1.3× = 11.04/1.3 = ₹8.49 cr/year = ₹0.708 cr/month → loan = 0.708 × [1 − (1+r)^−144]/r ≈ **₹60.7 cr**.

**Point to make:** check LTV too. If the property is worth ₹130 cr (a 8.5% cap rate on ₹11.04 cr NOI), then ₹60.7 cr is a 47% LTV, which is comfortable. DSCR binds, not LTV.

### P3 [cf] Escrow waterfall
**Given (assumptions):** a quarter's collections are ₹30 cr. RERA split 70/30. The lender's sweep is 25% of gross collections, taken from the RERA account (the loan was for this project's construction). Construction spend this quarter is ₹16 cr.

**Solution:**
- RERA account receives ₹21 cr. Free account ₹9 cr.
- Sweep = 25% × 30 = ₹7.5 cr from the RERA account → RERA balance available for construction = 21 − 7.5 = **₹13.5 cr**
- Construction need ₹16 cr → shortfall **₹2.5 cr**, met from the free account (₹9 cr) → developer's free cash after = **₹6.5 cr**.

**Point to make:** always check that the sweep doesn't starve construction. If the free account can't cover the shortfall, the sweep is too aggressive, or the loan too large.

### P4 [cf] Cost-to-complete cover on a stalled project
**Given (assumptions):** remaining cost to complete ₹60 cr. Receivables from sold units ₹35 cr. Unsold inventory 1.2 lakh sq ft carpet at a current price of ₹7,000/sq ft. Haircut 20%.

**Solution:**
- Receivables-only cover = 35/60 = **0.58×**. The project can't complete from its sold units.
- Unsold value with haircut = 1,20,000 × 7,000 × 0.8 = **₹67.2 cr**
- Total cover = (35 + 67.2)/60 = **1.70×**
- A last-mile lender funding the ₹25 cr gap (60 − 35), with priority on the waterfall, is well covered if unsold units can be sold at ₹7,000 after completion.

**Point to make:** the whole case rests on unsold inventory selling. Check whether the price holds for a stalled project's brand. Buyers discount stalled projects, which is why the haircut exists.

### P5 [cf] Interest cost on a CF line
**Given (assumptions):** a ₹60 cr CF line at 11.5%. Drawn ₹10 cr per quarter for 6 quarters, held at ₹60 cr for 4 quarters, then repaid ₹15 cr per quarter for 4 quarters. Interest is on the average balance each quarter.

**Solution:**
- Quarter-end balances: 10, 20, 30, 40, 50, 60, 60, 60, 60, 60, 45, 30, 15, 0
- Sum of quarterly average balances = 540 (e.g. Q1 avg = (0+10)/2 = 5; Q2 = 15; … Q14 = 7.5)
- Interest = 540 × 11.5%/4 = **₹15.5 cr**

**Point to make:** REF-W's ₹5 cr finance plug assumes a much smaller, shorter line. With ₹15.5 cr of interest, REF-W's margin would fall from 16.0% to about 10.6% (profit ₹31.0 cr − ₹10.5 cr extra interest = ₹20.5 cr). That's why developers size CF to the real gap and repay early.

## Common traps and wrong answers
- **"Banks fund land."** Generally they can't (**verify current RBI rules**).
- **Confusing LTC and LTV**, or using a single ratio for all stages.
- **Using DSCR for residential CF.** Use security cover and cost-to-complete cover.
- **Setting a sweep % without checking construction funding.**
- **Treating unsold inventory at full price as security.** Always haircut.
- **Ignoring RERA's designated account in the repayment structure.**
- **Sizing the loan to the maximum eligible amount** rather than the funding gap.
- **Assuming insolvency gives a lender clean enforcement.** Homebuyers are financial creditors under the IBC.
