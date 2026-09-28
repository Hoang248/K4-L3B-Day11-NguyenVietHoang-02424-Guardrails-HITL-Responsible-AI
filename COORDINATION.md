# Coordination and Anti-overlap Contract

## Ownership matrix

| Work item | Responsible | Accountable | Consulted | Artifact |
|---|---|---|---|---|
| Scope/requirements | `Nguyen Viet Hoang` | `Nguyen Viet Hoang` | `Key Coach` | `PROJECT_CONTEXT.md`, `docs/scope-memo.md` |
| Harness/context | `Nguyen Viet Hoang` | `Nguyen Viet Hoang` | `Key Coach` | root harness files, `docs/DECISION_LOG.md` |
| CP2 guardrails | `Nguyen Viet Hoang` | `Nguyen Viet Hoang` | `Key Coach` | `src/guardrails/` |
| CP3 implementation | `Nguyen Viet Hoang` | `Nguyen Viet Hoang` | `Key Coach` | `src/assignment/`, generated `outputs/` |
| CP4 red-team execution | `Nguyen Viet Hoang` | `Nguyen Viet Hoang` | `Key Coach` | `src/attacks/`, generated attack outputs |
| Validation/release | `Nguyen Viet Hoang` | `Nguyen Viet Hoang` | `Key Coach` | `tests/`, `scripts/grade.py` report |

## Write locks

- Một artifact chỉ có đúng một writer tại một thời điểm; hiện tại là owner duy nhất.
- Không sửa `tests/`, `schemas/`, `RUBRIC.md`, `RULES.md` hay protected data để làm pass.
- Review/validation không tự sửa implementation trong cùng lượt nếu chưa ghi rõ repair task.
- Không tạo thủ công `outputs/*.json`; lệnh lab là writer của các file đó.
- Không thay đổi GitHub/task tracker mặc định; push chỉ khi owner yêu cầu rõ.

## Dependency order

```text
context → scope → contract → CP2 implementation → CP3 artifacts → CP4 live attacks → review → submission
```

CP4 không được coi là complete khi provider/key chưa được cấu hình. CP5 không được coi là
complete khi artifacts thiếu hoặc public tests/schema chưa pass.

## Acceptance criteria

- CP2 accepts safe banking questions and blocks injection/off-topic/credential extraction.
- CP3 produces schema-valid generated results, audit and metrics artifacts.
- CP4 is marked `pending` until Red and Red Advance have live provider evidence.
- Every handoff records owner, changed paths, validation, limitation and stop condition.

## Conflict protocol

Khi hai kết luận hoặc artifact khác nhau:

1. Không tự chọn kết quả nghe hợp lý hơn.
2. Ghi conflict với path, snapshot/commit, owner và claim bị ảnh hưởng.
3. Giữ trạng thái `pending`, `needs_review` hoặc `blocked`.
4. Owner/Key Coach quyết định.
5. Chỉ sau quyết định mới cập nhật plan hoặc generated artifact.

## Parallel work rule

Chỉ chạy song song khi path ghi khác nhau, input snapshot đã freeze, không cùng tạo manifest
và downstream biết rõ version. Hiện tại đây là bài cá nhân; xử lý tuần tự là mặc định.

## Handoff order

1. Scope → Owner/Coordinator.
2. Owner → CP2/CP3 Builder.
3. Builder → Validation/Harness.
4. Validation → Owner.
5. Owner → CP4 hoặc stop/submission.
