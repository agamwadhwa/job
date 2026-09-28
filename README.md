# job

Scoring, ranking and prep workspace for a 2027 real-estate job hunt (land, BD, feasibility, JDA, approvals, RE finance). Pune and Mumbai.

## What's here
| Path | What it does |
|---|---|
| `hunt/scoring.py` | Scores a role 0–3 on 12 developer functions, then computes alignment, priority, combo and the best two-role paths |
| `hunt/roles.json` | Current role snapshot |
| `reports/ranking.md` | Ranked table + best two-step combinations (auto-generated) |
| `prompts/` | Copy-paste instructions for Claude Code cloud sessions |
| `.github/workflows/rank.yml` | Re-runs tests and the ranking on every push |

## Run locally
```bash
python -m hunt.rank      # rebuild reports/ranking.md
python -m pytest -q      # check the scoring maths
```

## Using cloud sessions
Start a cloud session on this repo and paste one prompt from `prompts/`. Order of value:
1. `01-feasibility-model.md`: a model you can defend line by line (the main gap)
2. `02-application-pack.md`: one pack per top role
3. `03-interview-drill.md`
4. `05-deal-note.md`: turns a news deal into an outreach attachment
5. `04-sync-and-rank.md`: routine upkeep (cheap)

> Make this repo **private** before adding your resume, your model, or anything personal.
