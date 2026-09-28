# 30-day plan

Assumes about 90 minutes a day on weekdays and 2–3 hours on weekends. Use the 30/60/90 blocks in `00-how-to-use.md` on busy days. Each day starts with a 10-minute quiz (`python interview-guide/quiz.py --weak --n 5`, or `--function <tag>` where shown).

Before day 1: fill every `[FILL]` in `06-behavioural-and-story.md` you can answer truthfully, and delete the rest.

## Week 1: foundations (land & feasibility)
| Day | Work | Quiz tag |
|---|---|---|
| 1 | `00-how-to-use.md` (REF-W section) + `03-technical/04` primer. Build the REF-W area statement on paper with no notes | feas |
| 2 | `03-technical/04` Q1–Q8. Say each answer aloud before reading it | feas |
| 3 | `03-technical/04` Q9–Q15 + P1–P2 | feas |
| 4 | `03-technical/04` P3–P5 + traps. Run `python interview-guide/ref_w.py` and change 3 inputs yourself | feas |
| 5 | `03-technical/01` land & title: primer + Q1–Q8 | land |
| 6 | `03-technical/01` Q9–Q15 + P1–P5 | land |
| 7 | Case 01 (Wagholi JDA) + Case 07 (title red flag). Framework in 5 minutes, then the numbers. **Excel drill #1** (below) | land, jda |

## Week 2: structures and approvals
| Day | Work | Quiz tag |
|---|---|---|
| 8 | `03-technical/03` JDA & redevelopment: primer + Q1–Q8 | jda |
| 9 | `03-technical/03` Q9–Q15 + P1–P5 | jda |
| 10 | **Mock #1:** HR (30 min) + land head (30 min) via `mock.md`. Write the fixes down | behav |
| 11 | `03-technical/02` approvals & liaison: primer + Q1–Q8 | appr |
| 12 | `03-technical/02` Q9–Q15 + P1–P5 | appr |
| 13 | Case 02 (Hinjawadi) + Case 03 (Andheri 33(7)(B)) | jda, feas |
| 14 | Case 08 (premium vs TDR) + Case 12 (Go/No-Go critique). **Excel drill #2** | appr, feas |

## Week 3: money side and the model
| Day | Work | Quiz tag |
|---|---|---|
| 15 | `03-technical/05` construction finance: all Q&A | cf |
| 16 | `03-technical/05` P1–P5 + Case 05 (stalled project) | cf |
| 17 | `03-technical/07` capital markets: Q1–Q8 + P1–P2 | cap |
| 18 | `03-technical/07` Q9–Q15 + P3–P5 + Case 11 (memo) | cap |
| 19 | `05-model-defence.md`: land head + CFO sections (20 questions), aloud, 60 seconds each | model |
| 20 | **Mock #2:** CFO (30 min) + IPC director (30 min) | model, cap |
| 21 | `05-model-defence.md`: lender + promoter sections. **Excel drill #3** | model |

## Week 4: breadth, firms and the final mock
| Day | Work | Quiz tag |
|---|---|---|
| 22 | `03-technical/06` asset management: all Q&A + P1–P5 | am |
| 23 | Case 06 (Chakan warehouse) + Case 10 (DM fee) | am, jda |
| 24 | Case 04 (plotted) + Case 09 (absorption) | feas |
| 25 | `01-interview-formats.md` + playbooks: Gera, ANAROCK, Aspect, Avener, Kotak | firm |
| 26 | Playbooks: Chaphalkar Karandikar, Raymond, Sunteck, Lodha, Rustomjee, Oberoi | firm |
| 27 | Refresh "recent deals" for your top 5 firms (news from the last month). Rehearse TMAY 60s + 2 min, recorded. **Excel drill #4** | behav |
| 28 | **Mock #3:** full panel (land head → CFO → HR, 45 min) for your #1 target firm | all |
| 29 | Fix the weakest 3 areas from mock #3. `quiz.py --weak --n 20` | weak |
| 30 | Light day: re-read traps sections in 03-technical/01–04, TMAY once, questions-to-ask for the next interview. Sleep | — |

## Excel speed drill (days 7, 14, 21, 27)
**Target: build an area statement and IRR from scratch in 30 minutes**, no template, blank workbook.

**Brief (change the inputs each time):** 2.5 acres, 5% road widening, road 15–24 m (TDR 0.9), basic 1.1 + premium 0.5, ancillary 60%, efficiency 78%, construction area 1.3×, rate ₹7,800, construction ₹2,400, TDR ₹2,300, land ₹9 cr/acre, 3 quarters to approval, 12 of construction, 12 of sales, 10% booking + 90% construction-linked.

**Checkpoints:**
| Minute | Must have |
|---|---|
| 5 | Inputs block, clearly separated, with units |
| 10 | Area statement: net plot → FSI → ancillary → FSI area (sq ft) → carpet → construction area |
| 15 | Cost stack with every line from REF-W, and total/margin |
| 25 | Quarterly cash flow: land, approvals, TDR, construction, collections (booking + progress-linked), marketing. Net and cumulative rows |
| 30 | IRR (`=(1+IRR(range))^4-1`), peak funding (`=-MIN(cumulative)`), and a 1-way sensitivity on price |

**Self-check:** set the inputs to REF-W's and confirm you get about ₹194 cr revenue, 16.0% margin, 23.6% IRR and ₹54.7 cr peak funding (`python interview-guide/ref_w.py`). Differences mean a formula error, or a different cash-flow convention you should be able to explain.

**Progression:** drill #1 untimed; #2 in 45 min; #3 in 35 min; #4 in 30 min. Keep each file and note where the time went.
