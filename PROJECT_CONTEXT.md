# Project Context

## Identity

- Project: `K4-L3B-Day11-NguyenVietHoang-02424-Guardrails-HITL-Responsible-AI`
- Owner: `Nguyen Viet Hoang`
- Mentor/stakeholder: `Key Coach`
- Repository: `https://github.com/Hoang248/K4-L3B-Day11-NguyenVietHoang-02424-Guardrails-HITL-Responsible-AI`
- External workspace: `NONE`
- Current snapshot/version: `main @ 6b3ea99b2988d89fc2fac89d60787054d80864b7` + current uncommitted implementation

## Problem statement

Hoàn thành bài Lab Day 11 bằng cách xây Blue defense-in-depth cho chatbot ngân hàng
VinBank: input/output guardrails, rate limiting, audit/monitoring và egress policy;
thực hiện red-team trên Red và Red Advance; sinh artifact có thể kiểm tra và nộp theo
đúng README, CHECKPOINTS, RUBRIC, RULES và SUBMISSION.

## Research/product question

Blue pipeline có chặn được prompt injection/off-topic/secrets, giới hạn spam, ghi được
evidence và ngăn secret đi ra ngoài mà không chặn nhầm câu hỏi banking hợp lệ không?

## In scope

- Implement CP2: injection/topic detection, input plugin, secret/PII output filter.
- Implement CP3: rate limiter, audit log, monitoring, ordered pipeline, egress allowlist,
  assignment suite và generated JSON artifacts.
- Chuẩn bị CP4: năm adversarial prompts đúng kỹ thuật, chạy Red/Red Advance khi có key.
- Áp dụng reusable project harness: context, map, coordination, quality gates, validator
  và handoff evidence.

## Out of scope

- Không sửa rubric, public tests, schema, protected secrets hoặc starter red-agent policy.
- Không tạo notebook solution, không viết tay `outputs/*.json`, `grade_report.json` hoặc
  `lab_report.md`.
- Không push/merge GitHub và không gửi API request trả phí khi chưa có key/ủy quyền rõ.
- Không triển khai production banking service hay dùng dữ liệu ngân hàng thật.

## Non-negotiable constraints

- Blue model phải giữ nguyên OpenRouter `liquid/lfm-2.5-2.6b` theo `src/core/config.py`.
- Raw/protected input bất biến; pending evidence không được coi là verified.
- Secret/API key chỉ nằm trong môi trường local; không ghi vào repo hoặc log.
- Egress policy là deterministic code, không giao quyền quyết định cho LLM.
- High-risk action cần exact destination và human approval theo `src/agents/security_boundary.py`.
- Artifact CP3/CP4 phải được sinh bởi command của bài và lưu trong `outputs/`.

## Current evidence state

| Claim | Evidence path/link | Status | Limitation |
|---|---|---|---|
| Đây là bài Lab Day 11 cá nhân với CP1–CP5 | `README.md`, `RULES.md`, `CHECKPOINTS.md` | verified | Nội dung là yêu cầu lớp, không phải production spec |
| Repo local trùng GitHub origin | `git remote -v` | verified | Web fetch GitHub bị cache miss trong phiên này |
| Starter tree ban đầu sạch, chưa có `.env`/API keys | `git status`, environment check | verified | Không suy ra key có thể được cấp sau đó |
| CP2–CP3 implementation và generated defense artifacts | `outputs/results.json`, `outputs/audit_log.json`, `outputs/metrics.json` | verified | Đã chạy bằng bundled Python runtime |
| CP4 Red/Red Advance attack evidence | `outputs/attack_results.json`, `outputs/unsafe_attack_result.json`, `outputs/guards_attack_result.json` | verified | Gemini provider; Red 4/5 leaks, Red Advance 0/5 leaks; một quick smoke trước đó gặp 503 |
| Submission packaging/schema/public tests | `outputs/grade_report.json`, `outputs/lab_report.md` | verified | Grader technical_failure=false; owner vẫn cần review trước khi push |

## Decision authority

- Scope/product decision: `Nguyen Viet Hoang`
- Technical merge decision: `Nguyen Viet Hoang`
- Domain/legal approval, if applicable: `Key Coach`; không áp dụng cho production banking claim

## Current stop condition

Phần implementation và kiểm tra Pha 1–4 đã đạt pass signal. Chưa tuyên bố đã nộp bài
cho đến khi owner review diff, xử lý cảnh báo `.env` ở dòng 5–6, chọn bonus B1/B2
và tự quyết định push/submit lên GitHub.
