# Cloud session: sync and re-rank (routine, cheap)

---
I'll paste a JSON export from the Hunt Ledger tracker below. Merge it into hunt/roles.json: match on id, keep only the public posting fields, and never add contact names. Then run `python -m hunt.rank` and `python -m pytest -q`, commit, and open a PR summarising the new roles, closed roles and the top 5 by priority.
