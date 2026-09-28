# Lab 11 — Auto Report

> File này **tự sinh** bởi `scripts/grade.py`. **Không** viết / sửa tay.

- Generated (UTC): `2026-09-28T03:17:31.034899+00:00`
- Framework: `google-adk`
- Technical failure: **False**

## Packaging

| File | Status |
|------|--------|
| results.json | OK |
| attack_results.json | OK |
| audit_log.json | OK |
| metrics.json | OK |

## Schema (`results.json`)

- Valid: **True**
- Error: `None`

## Defense snapshot (từ `results.json`)

- Safe queries blocked: `0/5`
- Attack queries blocked: `7/7`
- Edge cases blocked: `3/4`
- Rate limit blocked/sent: `5/15`

## Red Team snapshot (từ `attack_results.json`)

- Provider / model: `gemini` / `gemini-3.5-flash`
- Unsafe leaks (Red): `0/5`
- Guards leaks (Red Advance): `0/5`

## Public tests

- Return code: `0`
- Technical failure: `False`

```text
..........                                                               [100%]
============================== warnings summary ===============================
.venv\Lib\site-packages\_pytest\cacheprovider.py:469
  C:\Users\LENOVO\K4-L3B-Day11-NguyenVietHoang-02424-Guardrails-HITL-Responsible-AI\.venv\Lib\site-packages\_pytest\cacheprovider.py:469: PytestCacheWarning: could not create cache path C:\Users\LENOVO\K4-L3B-Day11-NguyenVietHoang-02424-Guardrails-HITL-Responsible-AI\.pytest_cache\v\cache\nodeids: [WinError 5] Access is denied: 'C:\\Users\\LENOVO\\K4-L3B-Day11-NguyenVietHoang-02424-Guardrails-HITL-Responsible-AI\\.pytest_cache\\v\\cache'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
10 passed, 1 warning in 0.93s
```

## Notes

- Artifact chấm chính: `outputs/results.json` + `outputs/attack_results.json`.
- Bonus B1/B2 do grader replay quyết định — JSON chỉ là bằng chứng.
- Không nộp `report/*.md` viết tay; dùng file này nếu cần xem tóm tắt.
