# Govern agentic AI

> Control tool permissions, autonomy and human oversight

**Goal:** Evaluate AI systems that plan, invoke tools or take actions with meaningful downstream effects.

## Inventory the complete agent boundary

Record the agent identity, model, prompt/policy revisions, memory, orchestrator, tool list, credentials, data access, external systems, action limits, escalation rules and the responsible humans.

## Governance procedure

1. Classify actions into **observe/read**, **recommend**, **prepare**, **execute with approval**, and **autonomous execute** as appropriate to your architecture.
2. Define allowlisted tools and permitted arguments, endpoints and data scopes. Minimize credentials and disable unnecessary write privileges.
3. Identify critical boundaries: transfers, customer changes, production deployment, safety-critical actions, access grants and destructive operations.
4. Set approval gates for actions above the authorized threshold. Ensure the gate is enforced by the system, not just stated in the prompt.
5. Evaluate prompt injection, cross-tool escalation, repeated actions, policy bypass, loops and failure to hand off to humans.
6. Capture tool-call traces and whether execution was allowed, denied, escalated or rolled back.
7. Review the evidence for the deployed combination of model, tool catalog and policy revision.
8. Define reassessment triggers for new tools, scopes, prompts, policies and supplier changes.

## Control checklist

- [ ] Every agent action can be attributed to a configured identity.
- [ ] Write operations require explicit, testable authority.
- [ ] Tools enforce least privilege independently of LLM instructions.
- [ ] High-impact actions have escalation or approval pathways.
- [ ] Logs support reconstruction without exposing unnecessary secrets.
- [ ] Disallowed and degraded scenarios were tested.

**Important:** A model's willingness to follow instructions is not a substitute for an authorization layer outside the model.
