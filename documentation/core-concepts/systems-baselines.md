# AI systems and baselines

> Identify the exact AI configuration under review

A **system record** describes the end-to-end AI capability. A **baseline** captures the configuration relevant to a particular evaluation or decision. The difference matters because a new prompt, tool permission or model version can change behavior without changing the system's marketing name.

## Minimum system inventory

| Group | Typical fields |
| --- | --- |
| Identification | Stable system ID, title, description, business owner |
| Purpose | Intended decisions/assistance, affected users, benefits and exclusions |
| Components | Models, agents, orchestration, prompts, data stores, tools, suppliers |
| Authority | Human oversight, escalation, permitted automated actions |
| Context | Regions, deployment modes, operating environments, data classifications |
| Governance | Applicable controls, risk tier, lifecycle status, review dates |

## Baseline manifest

A defensible baseline should identify relevant model and application releases, retrieval corpus or dataset snapshot, tool schemas, permissions, safety thresholds and environment assumptions.

```json
{
  "example_only": true,
  "system_id": "SYS-042",
  "baseline_id": "BASE-042-2026-11",
  "model": { "provider": "example", "version": "v2" },
  "application_release": "1.4.0",
  "retrieval_index_snapshot": "index-2026-11-01",
  "tool_policy_revision": "tool-policy-7",
  "intended_scope": "employee-policy-answers"
}
```

This is an **illustrative documentation schema**, not Assurio's published API or export format.

## Change significance

A patch to UI styling may be irrelevant to answer accuracy but important to accessibility. A permission change can invalidate authorization controls even when benchmark accuracy remains unchanged. Record differences against the baseline and trace them to requirements rather than assuming all changes are equivalent.

Next: [Requirements and claims](requirements-claims.md).
