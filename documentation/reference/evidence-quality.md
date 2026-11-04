# Evidence quality checklist

> Review relevance, integrity, coverage and currency independently

Before relying on an artifact in a decision, score its suitability for the exact claim and scope under review. This is an evidence-review aid, not a platform-published grading system.

## Seven review dimensions

| Dimension | Reviewer question | Failure example |
| --- | --- | --- |
| Identity | What baseline produced this? | Model version not identified |
| Provenance | Who/what generated the artifact? | Unattributed screenshot |
| Integrity | Can change or corruption be detected? | File edited with no revision history |
| Relevance | Is the tested context the approved context? | English-only test for multilingual system |
| Coverage | Are important adverse and edge cases represented? | No authorization negative tests |
| Currency | Has a material dependency changed? | Old tool-permission evidence |
| Review | Was the limitation independently considered? | Self-declared “passed” with no challenge |

## Review disposition

Record **adequate**, **adequate with limitations**, **insufficient**, **stale**, or **not applicable** using vocabulary approved by your organization. A passing result without provenance may still be inadequate for decision-making.

## Audit-ready evidence note template

```text
Artifact ID and revision:
Source system / collector:
Evaluated baseline and domain:
Requirements addressed:
Coverage and limitations:
Integrity/provenance check:
Known adverse or contradictory evidence:
Reviewer and date:
Disposition and rationale:
Follow-up action / expiry trigger:
```
