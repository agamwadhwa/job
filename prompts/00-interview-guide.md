# Cloud session: the complete interview guide and drill

Paste everything below the line into a Claude Code cloud session on this repo. It is a long job, so let it run.

---
Build `interview-guide/`, a complete interview preparation system for developer-side real-estate roles in Pune and Mumbai. The candidate graduates in May 2027 with an MBA in Advanced Project Management (NICMAR Pune) and a BBA in Business Analytics. He has 14 months at a construction contracting firm (government school projects) and an 8-week PMO internship at OneSubsea (SLB). He built a land feasibility model with AI help and is still learning to defend it.

## 0. Research first, then write
- Read `hunt/roles.json` and `reports/ranking.md`. The target firms are the top 25 by priority, plus these campus recruiters: Raymond Realty, Oberoi, Godrej & Boyce, JLL, Xanadu, Sunteck, Hinduja Renewables, KPMG.
- Use web search to collect real interview reports for each firm and role type: AmbitionBox interview pages, Glassdoor interviews, LinkedIn posts by people in these teams, and news on each firm's last 12 months of deals. Cite a source for every firm-specific claim. Anything not found must be labelled "typical for this role type (unverified for this firm)". Never invent a question and attribute it to a firm.

## 1. `00-how-to-use.md`
How to use the guide in 30, 60 and 90 minute daily blocks, and the order to work through the files.

## 2. `01-interview-formats.md`
How each firm type interviews: listed developers, mid-size promoter-led developers, IPCs (ANAROCK/JLL/CBRE/C&W/Colliers/Knight Frank), RE funds and NBFCs, valuation firms, and redevelopment firms. Cover the rounds (HR screen, technical, case or model test, promoter/MD round), what each round tests, typical duration, whether there are Excel tests, take-home cases, and presentations. Give sources where they exist.

## 3. `02-firm-playbooks/` (one file per target firm)
Each file covers:
- a snapshot (business mix, Pune/Mumbai projects, recent land deals/JDAs/redevelopments with dates and sources);
- what the specific role does;
- 10 likely questions, split between firm-specific and role-specific;
- "questions to ask them" (5 sharp ones about their deal pipeline);
- red flags to probe, using the AmbitionBox culture data in roles.json.

## 4. `03-technical/` (one file per function)
Files: land & title; approvals & liaison (UDCPR 2020, DCPR 2034, PMRDA/PMC/PCMC, CC/OC, RERA); JDA and redevelopment structuring (area share vs revenue share, Reg 33(7)(B)/33(9)/33(10) basics); feasibility and underwriting; construction finance (LTC, DSCR, escrow, RERA 70%); asset management and leasing (NOI, cap rate, LRD, REITs); capital markets and valuation (DCF, residual land value, comps).
Each file must have:
- a plain-language concept primer (concepts before mechanics);
- 15 interview questions, each with a model answer of about 120 words;
- 5 numeric problems with full worked solutions in ₹ using Pune/Mumbai numbers, with each assumption stated;
- common traps and wrong answers.

## 5. `04-cases/`
Twelve full cases with solutions:
- a JDA offer on 2 acres in Wagholi;
- outright vs JDA on a Hinjawadi plot;
- a society redevelopment in Andheri under 33(7)(B);
- a plotted development on the Pune fringe;
- a construction finance ask on a stalled project;
- a warehouse pre-lease on the Chakan corridor;
- a title red-flag case (7/12 mutation gap);
- a premium FSI vs TDR decision;
- an absorption slowdown sensitivity;
- a DM (development management) fee deal;
- an ANAROCK-style investment memo;
- a Go/No-Go note critique.
Each case needs the prompt, a 5-minute framework answer, the full numbers, and "what a strong candidate says that a weak one misses".

## 6. `05-model-defence.md`
If `model/` holds a feasibility workbook, generate 40 hostile questions about it (from a land head, CFO, lender and promoter) with answers tied to specific cells. If there is no workbook, generate the questions against a standard Pune residential feasibility and flag that they need re-mapping later.

## 7. `06-behavioural-and-story.md`
- A 60-second and a 2-minute "tell me about yourself" aimed at land/BD/feasibility roles.
- Answers for: "why not civil engineering"; "why real estate development"; "why this firm"; "where in 5 years"; "your contracting experience, what did you actually do"; "what did you do at OneSubsea"; "weakness"; "salary expectations"; "can you join in May 2027"; "you have only 14 months of experience". Write STAR answers from real experience only, with placeholders where he must fill in specifics. Never invent achievements.
- The family business question. If asked directly, confirm it honestly and briefly ("my family runs a contracting firm; I want developer-side depth first"), then steer back to the role. Don't volunteer it. Never deny it. Never display wealth.

## 8. `07-30-day-plan.md`
A day-by-day plan: which files each day, mock interviews on days 10, 20 and 28, and an Excel speed drill (build an area statement and IRR from scratch in 30 minutes).

## 9. Tools
- `quiz.py`: pulls random questions from all markdown files by tag (`--function feas --n 10`), hides the answer until Enter, and logs weak topics to `weak_topics.json`.
- `mock.md`: a script for running a mock interview with Claude, with interviewer personas (land head, CFO, IPC director, HR), a scoring rubric, and a feedback format.

## Quality bar
- Indian context only: ₹, sq ft/sq m, Maharashtra regulations. Put every figure in the right range and label it as an assumption.
- Mark regulation specifics that may have changed as "verify current".
- Direct, dense writing with no filler.
- Commit in logical chunks on a branch `interview-guide` and open a PR with a summary of what's in it and what still needs his input.
