# Resource model

> Conceptual resources for interoperable assurance records

The resources below reflect Assurio's publicly described assurance concepts. Their names are **logical integration vocabulary**, not verified endpoint or database names.

| Logical resource | Minimum useful fields | Relationships |
| --- | --- | --- |
| System | Stable ID, purpose, owners, permitted use | Baselines, risks |
| Baseline | Component versions, environment, domain, effective time | Requirements, decisions |
| Requirement | Claim, criterion, revision, criticality | Risk, tests, evidence |
| Evaluation | Method, environment, run ID, observations | Requirement, evidence |
| Evidence | Artifact reference, provenance, status and timestamps | Evaluation, review |
| Finding | Observed discrepancy, severity, owner, disposition | Evidence, decision |
| Decision | Accountable authority, outcome, scope and conditions | Baseline, evidence |
| Change | Old/new configuration, impact and reassessment | Baseline, requirement |

## Recommended relationship constraints

A decision must refer to the approved baseline. Evidence needs an identifiable origin and evaluation context. A finding should link to the observation that raised it. Imported revisions should not destructively overwrite historical records relied upon by past decisions.

## Integration validation

Map external IDs, canonical timestamps and source-system versions before committing any records. Define how duplicates, replays, stale records, deleted source artifacts and schema migrations are handled. Request a verified object schema before building a production client.
