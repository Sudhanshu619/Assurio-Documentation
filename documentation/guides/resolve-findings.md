# Manage findings and remediation

> Turn discrepancies into owned, reviewable actions

**Goal:** Make unresolved limitations visible and prevent closed tickets from masking unverified system behavior.

## Procedure

1. Create a unique finding linked to the precise requirement, run, baseline and evidence.
2. Describe observed versus expected behavior and the conditions required to reproduce it.
3. Identify severity based on the relevant control and potential harm, not only the raw test metric.
4. Assign an owner, target resolution, interim restriction and escalation route.
5. Determine a disposition: investigate, remediate, accept through delegated risk authority, document as inconclusive, or reject the proposed use.
6. Re-run tests after a fix against the revised baseline and retain both original and retest evidence.
7. Ask the required reviewer to verify closure. Record who closed the item, why and with which evidence.
8. Assess whether the finding changes the pending or current approval decision.

## Sample finding

| Field | Example |
| --- | --- |
| Finding | FIND-011 |
| Linked requirement | REQ-001 |
| Observation | Contractor can retrieve restricted policy text |
| Severity | Critical under example organization's policy |
| Interim action | Block contractor group pending remediation |
| Owner | Application security lead |
| Closure evidence | Access-denial retest across role matrix |
| Decision impact | Contractor scope excluded until verified |

## Do not confuse status with evidence

A ticket labeled *fixed* is not proof a requirement now passes; evidence for the corrected baseline is needed. A formally risk-accepted exception is not the same as a technical pass.
