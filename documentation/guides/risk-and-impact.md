# Risk and impact assessment

> Identify credible AI harms and choose proportional controls

**Goal:** Document exposure and treatment for the system's intended and reasonably foreseeable use.

## Procedure

1. **Define context.** State affected people, decisions, data, operating environments, autonomy and human oversight.
2. **Identify hazards and harms.** Consider wrong outputs, bias, data leakage, adversarial prompts, unsafe actions, failures to escalate and supplier change.
3. **Assess initial exposure.** Use your organization's severity, likelihood and detectability scale; do not invent a universal risk score.
4. **Assign controls.** Separate prevention, detection, limitation, human oversight and recovery measures.
5. **Set tests.** For each important control identify a verification method and acceptance criterion.
6. **Assess residual risk.** Record assumptions, remaining uncertainty and who can accept it.
7. **Escalate critical gaps.** If a control is untested or failed, block or narrow the proposed use according to policy.
8. **Version the assessment.** Link it to a system baseline and conditions that trigger revision.

## Sample risk register

| ID | Risk scenario | Mitigation | Evidence required | Residual decision |
| --- | --- | --- | --- | --- |
| R-01 | Unauthorized policy document retrieval | Identity-aware source filtering | Cross-role access denial tests | Pending review |
| R-02 | Confident but ungrounded answer | Citation and escalation rules | Adjudicated hallucination tests | Pending review |
| R-03 | Agent executes prohibited write | Read-only credentials and approval gate | Negative tool-authorization tests | Must pass critical gate |

## Review questions

- Would failure harm an affected person who is not represented in the test data?
- Could a user bypass a nominally read-only guardrail via tools or integrations?
- Is the proposed human reviewer actually available and empowered?
- Are controls verifiable in production, not just documented in design?

See [Risk scoring](../reference/risk-scoring.md) for a configurable rubric.
