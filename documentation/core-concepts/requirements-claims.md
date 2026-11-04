# Requirements and claims

> Turn expectations into measurable assurance criteria

An assurance **claim** is a statement that must be supported before a specified use is accepted. A **requirement** makes the claim actionable: it identifies context, verification method and pass/fail or review criteria.

## Good requirement structure

`[ID] [Actor/system] shall [observable behavior] under [conditions], measured by [method], meeting [criterion].`

| Weak wording | Better formulation |
| --- | --- |
| “Agent is secure” | Deny write operations outside the approved tool allowlist in all authorization tests |
| “Model is accurate” | Meet the agreed task-quality threshold on versioned representative and stress-case datasets |
| “Human in the loop” | Escalate designated high-impact actions before execution with traceable reviewer confirmation |
| “Robust to change” | Reassess named requirements after model, data, tool or operating-domain changes |

## Design checklist

Each requirement should include a stable ID, rationale, policy/control reference, risk association, owner, applicable baseline, environmental assumptions, test method, threshold, severity if failed and evidence links. Classify **critical gates** separately from optimization metrics so a serious policy violation cannot be averaged away.

## Requirement lifecycle

1. **Draft:** proposed claim and supporting rationale.
2. **Reviewed:** relevant owners agree on the evaluation method.
3. **Baselined:** requirement revision is fixed for a given evaluation package.
4. **Evaluated:** supporting, adverse or missing evidence is attached.
5. **Decision-linked:** reviewer states how it affects the scoped decision.
6. **Superseded:** changes preserve the earlier record and rationale.

The states above are documentation-level conventions; verify the application's actual status vocabulary before using them in UI instructions.
