# Make a scoped approval decision

> Record what can operate, who authorized it and why

**Goal:** Create an accountable acceptance outcome that another reviewer can reconstruct after the system changes.

## Before deciding

Check that the candidate baseline is stable, critical requirements are reviewed, adverse evidence is visible, material findings have a disposition, residual risk falls within delegated authority, and conditions can be enforced in practice.

## Procedure

1. Declare the **exact baseline** and intended operation under review.
2. Confirm evidence coverage and note all limitations and exclusions.
3. State whether the outcome is approved, conditional, deferred, rejected or suspended according to your policy vocabulary.
4. Define approved users, activities, geography, data and tool permissions, thresholds and deployment environments.
5. Enumerate conditions (e.g., human review before sensitive writes) with enforcing control and responsible owner.
6. List unresolved findings and their dispositions, plus any risk exceptions and expiry.
7. Identify the delegated human authority, review participants, date and reasoning.
8. Specify expiry or event-based reassessment triggers and the consequence of a failed condition.
9. Preserve the approval as a traceable record; do not overwrite old decisions after a new baseline is released.

## Sample decision statement

> **Illustrative only:** Baseline `BASE-042-2026-11` may be used for employee-facing policy retrieval in the internal staging pilot. Only approved document collections are in scope; external access and all record-write operations are excluded. The system owner must retain a working escalation path. Any model, tool-permission or retrieval-index change requires targeted impact review before expanded use. Authorized decision maker: *[organization-assigned name and role]*.

## Decision quality test

Could someone outside the project tell from this record what was approved, the evidence reviewed, the restrictions enforced, and the precise changes that require reconsideration? If not, the decision is too broad or too thinly documented.

See [Decision states](../reference/decision-states.md).
