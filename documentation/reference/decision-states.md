# Decision states and review lifecycle

> Example governance status vocabulary and transitions

These are **proposed business-state names** for documentation clarity. The application's actual statuses, approvals and automation must be verified before being presented as built-in workflow behavior.

| Conceptual state | Meaning | Typical next action |
| --- | --- | --- |
| Draft | Proposed scope and evidence package is still being prepared | Gather inputs |
| Ready for review | Required artifacts have been submitted | Independent review |
| Changes requested | Critical gaps or clarifications identified | Remediate and resubmit |
| Deferred | Authority will not decide until prerequisites are met | Acquire evidence |
| Approved within scope | Human authority permits specific operation | Enforce conditions |
| Conditionally approved | Bounded operation with explicit limitations | Verify restriction effectiveness |
| Rejected | Proposed operation is not permitted | Revise or discontinue |
| Reassessment required | Evidence or conditions may be stale | Impact review and retest |
| Suspended | Reliance on prior permission has been withdrawn temporarily | Incident/reassessment path |
| Superseded | A later decision replaces a historical one | Retain history |

## Transition rules

A configuration change should not silently change a historical decision to “approved for new version.” Create a new decision or an explicit amendment with changed evidence and new authority where required. Rejected or inconclusive evidence should remain visible even after remediation.

## Review trail

Capture actor identity, time, prior state, new state, rationale, linked evidence and any delegated authority. State labels alone are insufficient for audit reconstruction.
