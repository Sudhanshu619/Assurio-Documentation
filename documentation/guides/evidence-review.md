# Review evidence

> Assess whether artifacts are trustworthy and decision-relevant

**Goal:** Verify that evidence is authentic, current, complete and applicable to the proposed operating scope.

## Procedure

1. **Identify:** attach stable evidence IDs and source locations.
2. **Link:** connect each artifact to a baseline, requirement, scenario and test result.
3. **Validate provenance:** identify origin, collection method, evaluator, date, version and integrity control.
4. **Check relevance:** confirm the tested environment and population match the proposed use.
5. **Check sufficiency:** ensure coverage includes critical negative tests, exceptions and likely harms.
6. **Challenge contradictions:** retain failed tests, conflicting findings and uncertainty.
7. **Assess currency:** determine whether baseline or external environment changes have made evidence stale.
8. **Document review:** capture the reviewer, disposition, rationale, additional work and links to the decision package.

## Sample evidence record

```json
{
  "example_only": true,
  "evidence_id": "EVD-017",
  "baseline_id": "BASE-042-2026-11",
  "requirement_ids": ["REQ-003"],
  "test_run_id": "RUN-220",
  "environment": "staging-agent-sandbox",
  "collected_at": "2026-11-02T09:00:00Z",
  "source_artifact": "restricted://review/evidence-017",
  "integrity": { "sha256": "<recorded artifact hash>" },
  "review_status": "pending"
}
```

This record is a **proposed documentation example**, not a confirmed Assurio API payload.

## Common reasons evidence is inadequate

The artifact covers the wrong model version, lacks evaluation method details, omits failed runs, depends on outdated data, was collected outside the declared domain or cannot be accessed by an authorized reviewer. Mark the specific reason and required remediation rather than using an unexplained red status.

See [Evidence quality](../reference/evidence-quality.md).
