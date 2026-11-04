# Monitor changes and reassess

> Link changed conditions to affected evidence and decisions

**Goal:** Respond proportionally to material changes after a system has been reviewed or approved.

## Change sources

Changes may be detected through model registries, deployment records, source-control releases, supplier notices, runtime monitoring, identity/policy configuration, incident reports or manual change submissions. Integration implementation varies by deployment.

## Procedure

1. Record the change event, time, system, source and old/new configuration identities.
2. Verify the change actually affects the system or operating scope under review.
3. Traverse dependencies from component to baseline, requirements, controls, test conditions, evidence and decisions.
4. Classify impact: no relevant change, targeted reassessment, full review or immediate operating restriction.
5. Preserve an explicit reason for reusing unaffected evidence.
6. Where needed, rerun critical tests and obtain independent review.
7. Update the decision status and conditions through the accountable authority.
8. Retain the original event, analysis and revised decision for auditability.

## Example impact table

| Change | Likely evidence to revisit | Possible response |
| --- | --- | --- |
| Model revision | Accuracy, refusal, safety, escalation | Targeted TEVV and decision review |
| New agent write tool | Authorization, action boundaries, incident recovery | Critical-gate tests and restricted rollout |
| Retrieval index revision | Grounding, source access, data currency | Regression checks |
| New user group | Entitlements, affected-population harms | Expand scope assessment |
| UI-only visual change | Human usability/accessibility where relevant | Proportional review |

## Handling a critical incident

Follow the organization's incident response process. Preserve operational evidence, identify immediate restrictions and ensure the authority to suspend unsafe use is not ambiguous. The assurance record supports that process but does not replace live technical controls.
