# Reusable Project Harness — Applied to Day 11

This harness keeps the project scope, ownership, evidence state and quality gates explicit.
The assignment documents remain authoritative for lab behavior and submission format.

## Operating sequence

```text
context → scope → CP2 guardrails → CP3 pipeline/artifacts → CP4 live red-team → review → submission
```

## Rules carried over from the template

- One writer per artifact.
- Raw/protected inputs are immutable.
- `pending` and `blocked` are not `pass`.
- Every handoff records facts, assumptions, unknowns, artifacts, validation and limitations.
- Generated outputs are produced by the lab commands, not hand-written.

Run the validator from the repository root:

```powershell
.\scripts\validate-project-harness.ps1
```
