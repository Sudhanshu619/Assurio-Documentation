# Requirements and controls

> Connect control objectives to measurable TEVV claims

**Goal:** Ensure every high-priority risk and mandatory control has a testable requirement and an evidence plan.

## Procedure

1. Collect the risk register, policies, system baseline and known design limits.
2. Separate policy/control objectives from measurable system requirements.
3. Give each requirement a durable identifier and a version.
4. State conditions, expected observations and thresholds; for qualitative review, define reviewer criteria.
5. Label critical gates that cannot be outweighed by a passing aggregate metric.
6. Specify the method, scenario, environment and owner for verification.
7. Link each requirement to the risks and policies it addresses.
8. Obtain approval of the **criteria before** evaluating against them; document subsequent changes as revisions.

## Example requirements

| ID | Requirement | Method | Critical? |
| --- | --- | --- | --- |
| REQ-001 | Deny cross-role access to restricted documents | Authorization negative tests | Yes |
| REQ-002 | Cite the versioned document used for supported answers | Source-attribution review | Context-dependent |
| REQ-003 | Block prohibited financial-system writes | Tool permission tests | Yes |
| REQ-004 | Escalate out-of-scope requests | Workflow scenario tests | Yes |

## Acceptance criteria template

```text
Requirement ID:
Baseline/revision:
Purpose and linked risk:
Preconditions:
Test scenario or dataset:
Measurement method:
Threshold/critical gate:
Evidence artifact required:
Review owner:
Known exclusions:
```

**Output:** Versioned requirements traceable to policies, risk and [TEVV campaigns](tevv-campaign.md).
