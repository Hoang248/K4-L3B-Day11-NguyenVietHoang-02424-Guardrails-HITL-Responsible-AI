# Scope Memo — Day 11 Harness Application

## Confirmed facts

- The repository is an individual Day 11 lab about guardrails, HITL and red teaming.
- CP2–CP3 are implementation work for Blue defense; CP4 runs supplied Red and Red Advance.
- The GitHub origin supplied by the owner matches the local repository remote.
- Synthetic protected secrets and submission schema are part of the starter contract.

## Working interpretation

“Áp dụng template” means integrate the reusable harness files and use their ownership,
evidence and quality-gate rules while completing the existing lab. It does not mean
replacing the assignment README or inventing production requirements.

## Acceptance criteria

1. Harness validator sees all required files and passes.
2. CP2 filters detect required attacks, preserve safe banking queries and redact secrets.
3. CP3 produces schema-valid generated outputs and passes public tests.
4. CP4 remains `pending` until live provider execution is evidenced.

## Open questions

- Which Red provider will the owner use for CP4: OpenAI or Gemini?
- Which optional bonus will the owner choose: B1 Red leak or B2 Red Advance leak?
