# AGENTS.md — Project Operating Rules

## Mission

Bạn đang làm việc trong `K4-L3B-Day11-NguyenVietHoang-02424-Guardrails-HITL-Responsible-AI`.
Mục tiêu hiện tại là hoàn thành Lab Day 11: Blue guardrails/pipeline ở CP2–CP3,
Red/Red Advance ở CP4, và artifact nộp ở CP5. Không tự mở rộng sang feature ngoài
phạm vi lab hoặc thay đổi logic chấm điểm.

## Before acting

1. Đọc `PROJECT_CONTEXT.md`, `WORKSPACE_MAP.md`, `COORDINATION.md` và `QUALITY_GATES.md`.
2. Đọc `README.md`, `RULES.md`, `CHECKPOINTS.md`, `RUBRIC.md` và `SUBMISSION.md` khi làm assignment.
3. Xác định lane/owner của task và kiểm tra working tree cùng thay đổi chưa commit.
4. Nếu repository có `.codegraph/`, dùng CodeGraph trước khi grep/find hoặc đọc lan man.
5. Nếu thiếu thông tin làm thay đổi phạm vi, ghi assumption trong handoff; không tự đoán thành fact.

## File and ownership rules

- Đây là bài cá nhân: `Nguyen Viet Hoang` là owner; mỗi artifact chỉ có một writer tại một thời điểm.
- Không sửa test, schema, protected secret hoặc rubric để làm bài pass.
- Không tạo thủ công artifact chấm trong `outputs/`; phải sinh bằng command được README/CHECKPOINTS quy định.
- Không xóa hoặc ghi đè raw/protected input; `data/protected/vinbank_secrets.json` là immutable.
- Không commit `.env`, API key, secret thật hoặc raw legal/PII ngoài phạm vi lab.
- Không dùng `git reset --hard`, `git checkout --` hoặc lệnh xóa diện rộng để làm sạch workspace.
- Mọi thay đổi phải có test hoặc validation phù hợp với rủi ro.

## Evidence rules

- Phân biệt fact, inference, assumption và unknown.
- `pending` là trạng thái hợp lệ và phải fail-closed.
- URL/hash/test pass không tự chứng minh domain/legal correctness.
- `outputs/results.json`, `outputs/attack_results.json` và report chỉ được xem là verified
  khi command sinh artifact đã chạy và validator/test tương ứng pass.
- Không đánh dấu CP4/Red/Red Advance pass nếu chưa chạy provider thật với key hợp lệ.

## Completion report

Mỗi lượt làm việc phải báo:

- mục tiêu và phạm vi đã xử lý;
- files changed;
- commands/tests và kết quả/exit code;
- commit hoặc working-tree state;
- limitation/blocker;
- next action và stop condition.
