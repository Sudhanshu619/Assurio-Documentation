# Troubleshooting guide

> A practical matrix for common assurance workflow blockers

| Problem | First checks | When to escalate |
| --- | --- | --- |
| AI system not visible | Tenant, role, system ID, environment | Admin confirms no visibility issue |
| Evidence absent | Baseline, run ID, source sync, classification | Critical evidence missing before review |
| Unclear approval status | Decision ID, last authority, scope, expiry | Production use exceeds recorded permission |
| Risk score disputed | Organization rubric, supporting harms and assumptions | Residual risk exceeds delegated authority |
| Evaluation results conflict | Scenario, method, baseline, data version | Critical gate contradicted |
| Approval invalidated by update | Change record, dependency map, last baseline | Unsafe or high-impact use may continue |
| Report omits finding | Filter, evidence revision, export scope | Audit completeness affected |
| External integration fails | Identity, IDs, schema, retries, reconciliation | Repeated loss or corruption of evidence |

## Minimal reproducible report

```text
Issue summary:
System ID / baseline / decision ID:
Timestamp and timezone:
Expected behavior:
Observed behavior:
Steps to reproduce (sanitized):
Affected role / environment:
Evidence or correlation IDs:
Operational risk / workaround:
```

## Severity guidance

Escalate immediately using your enterprise incident procedure when a restricted agent action is executed, unauthorized data is disclosed, or an unreviewed change affects a critical operating gate. A documentation question and an active control failure require different handling.
