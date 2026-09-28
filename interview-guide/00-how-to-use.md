# How to use this guide

Target roles: developer-side land/BD, feasibility and underwriting, JDA and redevelopment, and liaison, in Pune and Mumbai. After those come RE capital markets, fund investing, construction finance and asset management. Start date: May 2027.

## What's where

| File | Use it for | Time to finish once |
|---|---|---|
| `01-interview-formats.md` | What each firm type's rounds look like | 45 min |
| `02-firm-playbooks/` | One file per target firm: snapshot, deals, likely questions, questions to ask | 20 min each |
| `03-technical/` | Seven function files: primer, 15 Q&A, 5 worked numeric problems, traps | 3–4 h each |
| `04-cases/` | Twelve full cases with numbers | 60–90 min each |
| `05-model-defence.md` | 40 hostile questions on a feasibility model | 3 h |
| `06-behavioural-and-story.md` | TMAY, STAR answers, the awkward questions | 2 h, then rehearse aloud |
| `07-30-day-plan.md` | Day-by-day schedule | — |
| `mock.md` | Run a mock interview with Claude | 45 min per mock |
| `quiz.py` | Random drill from every file | 10–20 min |
| `research-gaps.md` | What couldn't be verified from this container; pages for you to open and paste in | — |

## The reference feasibility (read this first)

Most numeric material uses one reference project so the numbers stay consistent. It's called **REF-W**.

- 2 acres gross (8,094 sq m) in Wagholi, Pune. Net plot for FSI: 7,700 sq m after road widening. The access road is 18 m.
- FSI: basic 1.1 + premium 0.5 + TDR 0.9 = 2.5. Ancillary FSI is 60% on top. FSI area = 30,800 sq m = 3.32 lakh sq ft.
- Carpet = 78% of FSI area = 2.59 lakh sq ft. Construction area = 1.30 × FSI area = 4.31 lakh sq ft (includes stilt/podium parking and services).
- Sale rate ₹7,500/sq ft carpet → revenue ₹194 cr.
- Costs (₹ cr): land 16.0 (₹8 cr/acre), stamp duty 1.1, premium FSI 1.7, TDR 16.4 (₹2,200/sq ft), ancillary premium 1.0, other statutory 5.0, construction 99.1 (₹2,300/sq ft of construction area), professional fees 4.0, marketing and brokerage 9.7, admin 3.9, finance 5.0. **Total 162.9.**
- Profit ₹31.0 cr = **16.0% of revenue**. Unlevered IRR **23.6%** over 15 quarters. Peak funding **₹54.7 cr** in quarter 3.
- Sensitivities (unlevered IRR): rate −10% → 12.2%; rate +10% → 34.4%; absorption stretched from 12 to 20 quarters → 13.4%; construction 4 quarters late → 22.4%; TDR at ₹3,000 → 18.5%; construction cost +10% → 16.6%; land at ₹10 cr/acre → 19.4%.

Every figure above is an **assumption** for teaching, not a market quote. The FSI table and premium rates follow UDCPR 2020 as generally described. **Verify current** with an architect or liaison consultant before quoting in an interview. The script that produced these numbers is described in `05-model-defence.md`.

The lesson REF-W teaches: outright land on the Pune fringe gives about 16% margin at these assumptions. A 10% price drop or a slow sell-through halves the IRR. That is why fringe deals are usually JDAs, and why the absorption assumption gets attacked hardest.

## Daily blocks

**30 minutes (busy days, travel, exam weeks)**
1. 10 min: `python quiz.py --n 5`. Say the answer aloud before revealing it.
2. 15 min: one numeric problem from `03-technical/`, on paper, timed.
3. 5 min: read one firm's "recent deals" section and say one sentence about it aloud.

**60 minutes (default)**
1. 10 min: quiz, weak topics first: `python quiz.py --weak --n 5`.
2. 30 min: one technical file section (5 Q&A, or 2 numeric problems), then close the file and re-answer.
3. 15 min: one firm playbook. Write your own answer to 3 of its 10 questions.
4. 5 min: log what you got wrong in a notebook, not just in the quiz log.

**90 minutes (weekends, after mocks)**
1. 15 min: quiz, 10 questions.
2. 45 min: one full case from `04-cases/`. Attempt the 5-minute framework with a timer, then do the numbers, then compare.
3. 20 min: one mock round (see `mock.md`), or rehearse `06-behavioural-and-story.md` aloud with a recording.
4. 10 min: re-read "common traps" in the function file you're weakest on.

## Order to work through

1. `06-behavioural-and-story.md`: fill in every `[FILL]` placeholder first. Everything else depends on a clean story.
2. `03-technical/04-feasibility-underwriting.md`, then `03-jda-redevelopment.md`, then `01-land-title.md`, then `02-approvals-liaison.md`. This is the priority order from CLAUDE.md.
3. `04-cases/01`–`04`, `07` and `08` (the land-side cases).
4. `05-model-defence.md`, once your own workbook is in `model/`.
5. `03-technical/05`–`07` (finance, asset management, capital markets).
6. Remaining cases.
7. Firm playbooks: the night before any conversation with a firm, plus a rolling one per day.

## Rules this guide follows

- Firm-specific claims carry a source link. Anything unsourced is labelled **"typical for this role type (unverified for this firm)"**. No question is attributed to a firm unless a public interview report shows it.
- Regulation specifics are marked **verify current** where they change often.
- Your answers must use only real experience. Where a placeholder says `[FILL]`, fill it with something you can defend under three follow-up questions, or delete the line.
