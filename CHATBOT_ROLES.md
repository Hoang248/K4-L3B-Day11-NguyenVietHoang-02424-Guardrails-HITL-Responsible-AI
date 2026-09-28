# Chatbot Roles and Thread Setup

Đây là project cá nhân. Các role dưới đây là ownership lanes, không mặc định tạo thêm
Codex thread hoặc cho phép nhiều writer cùng lúc.

## 00 — Coordinator / Owner

**Owner:** `Nguyen Viet Hoang`

**Purpose:** giữ context, scope, dependency, review diff và quyết định handoff.

**Can write:** harness docs, decision log, plan, merge decision.

**Cannot write:** protected data hoặc artifact chấm bằng tay.

## 01 — Scope/Research

**Purpose:** đọc README/checkpoints/rubric, phân biệt fact/inference/assumption/unknown,
chốt acceptance criteria.

**Can write:** scope memo và research notes.

**Cannot write:** implementation code, canonical output JSON.

## 02 — Builder

**Purpose:** implement một lane cụ thể.

**Allowed paths:** `src/guardrails/`, `src/assignment/`, `src/attacks/`, và harness validator
khi được giao.

**Cannot write:** tests/schema/protected secrets hoặc lane khác ngoài scope.

## 03 — Review/Harness

**Purpose:** chạy validator, pytest, schema/grader và lập finding.

**Can write:** validation report/handoff; generated outputs chỉ qua command chính thức.

**Cannot write:** implementation để tự làm mất finding nếu chưa có repair task.

## Thread naming nếu cần tách task

```text
K4-L3B-Day11-00-coordinator
K4-L3B-Day11-01-scope
K4-L3B-Day11-02-builder
K4-L3B-Day11-03-review
```
