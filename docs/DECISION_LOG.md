# Decision Log

| Date | Decision | Reason/evidence | Owner | Status |
|---|---|---|---|---|
| 2026-09-28 | Apply full reusable project harness at repo root | User explicitly requested harness use for the GitHub-linked lab repo | Nguyen Viet Hoang | accepted |
| 2026-09-28 | Preserve existing lab README/rules/checkpoints/submission docs | They are the assignment contract and must not be replaced by the harness | Nguyen Viet Hoang | accepted |
| 2026-09-28 | Treat CP4 live execution as pending without local provider keys | Environment check found no `.env`, OpenRouter, OpenAI or Google key | Nguyen Viet Hoang | pending |
| 2026-09-28 | Use `outputs/` only for command-generated artifacts | `RULES.md` and `CHECKPOINTS.md` prohibit hand-written submission JSON/report | Nguyen Viet Hoang | accepted |
| 2026-09-28 | Mark CP2–CP3 and packaging validated | Smoke/public tests, results schema and grader pass; generated metrics/audit exist | Nguyen Viet Hoang | accepted |
| 2026-09-28 | Record CP4 as evidence, not an unqualified model guarantee | Red/Red Advance artifacts show 4/5 Red leaks and 0/5 guarded leaks; a Gemini 503 occurred during a quick smoke | Nguyen Viet Hoang | accepted |
