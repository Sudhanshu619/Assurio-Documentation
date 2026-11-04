# Data dictionary

> Recommended records and fields for a traceable assurance process

Use this dictionary to align your onboarding, exported reports and integration contracts. The data types and names below are **suggested logical fields**, not a confirmed Assurio API schema.

| Entity | Example attributes | Key relationship |
| --- | --- | --- |
| AI System | `system_id`, title, intended_use, owner, exclusions | Has baselines |
| Baseline | `baseline_id`, component_versions, domain, effective_time | Belongs to system |
| Requirement | `requirement_id`, revision, criticality, method, threshold | Applies to baseline |
| Risk | `risk_id`, cause, harm, exposure, treatment, owner | Linked to control/requirement |
| Control | `control_id`, policy_ref, owner, enforcement_point | Mitigates risk |
| Evaluation run | `run_id`, method, environment, baseline, started_at | Evaluates requirement |
| Evidence | `evidence_id`, source, provenance, checksum, collected_at | Supports/challenges claim |
| Finding | `finding_id`, severity, observation, owner, disposition | Derived from evidence |
| Review | `review_id`, reviewer, sufficiency, reasoning | Assesses evidence |
| Decision | `decision_id`, authority, baseline, outcome, scope, conditions | Uses reviewed evidence |
| Change event | `change_id`, origin, old/new configuration, impact | May invalidate evidence |

## Identity recommendations

Identifiers should be stable across revisions. When evidence changes, preserve a new revision or amendment relationship instead of silently replacing the original item. Capture origin-system IDs when importing third-party records.

## Time and integrity

Use timezone-aware timestamps and retain enough raw source context for an auditor to reconstruct collection. If checksums or signatures are used, record their algorithms and validation responsibilities; a checksum alone does not establish that the underlying evaluation was appropriate.

## Sensitive information

Store secrets and sensitive personal records only when necessary and authorized. Prefer references to controlled artifacts rather than copying raw customer datasets into every assurance record.
