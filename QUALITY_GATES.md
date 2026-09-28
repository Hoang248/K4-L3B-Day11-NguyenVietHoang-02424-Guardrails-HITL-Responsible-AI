# Quality Gates

## G0 — Context and scope

Pass when:

- problem statement, primary question và in/out-of-scope đã viết;
- workspace map, owner matrix và handoff rule tồn tại;
- không có hai lane cùng sở hữu một write path.

## G1 — Repository integrity

Pass when:

- working tree và snapshot được biết rõ;
- harness files tồn tại và validator pass;
- `.env`/secret không bị commit;
- smoke tests và starter contract không bị phá.

## G2 — CP2/CP3 defense and artifact integrity

Pass when:

- injection/topic/output filters fail-closed đúng yêu cầu;
- rate limiter, audit, monitoring, pipeline và deterministic egress pass tests;
- `outputs/results.json` khớp schema, safe queries không bị block nhầm và attacks bị block đủ;
- `audit_log.json` và `metrics.json` do command sinh ra.

## G3 — CP4 review/evidence

Pass when:

- năm adversarial prompts có kỹ thuật rõ ràng;
- Red và Red Advance đã chạy thật với provider/model hợp lệ;
- `outputs/attack_results.json` có evidence, leak/block/layer và limitation;
- live output không chứa API key thật ngoài artifact được phép của lab.

## G4 — Submission/research result

Pass when:

- `pytest tests/smoke -q`, `pytest tests/public -q` và `scripts/grade.py` có kết quả rõ;
- known limitations/failure cases được ghi;
- path/version/commit và handoff packet hoàn chỉnh;
- không claim vượt quá evidence; owner chấp nhận handoff.

## Status vocabulary

```text
pass        = evidence satisfies this gate
pending     = work exists but review/evidence is incomplete
blocked     = capability or decision is missing
failed      = a check found a defect
not_applicable = explicitly justified
```

Không tự chuyển `pending` hoặc `blocked` thành `pass`.
