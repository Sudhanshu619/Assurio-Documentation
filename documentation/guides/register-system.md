# Register an AI system

> Create an inventory entry that supports future evaluation

**Goal:** Create one authoritative identity for an AI application or agentic system and its operating use.

**Inputs:** system name, owner, intended user groups, components, connected tools, data sources, model/provider versions and deployment context.

## Procedure

1. Identify the end-to-end application boundary. Include retrieval systems, agents, safety gates, human decisions and execution tools, not merely the foundational model.
2. Assign a stable ID and distinguish the business use case from its underlying model or vendor product.
3. Write the permitted purpose in terms of actual users and outcomes. List disallowed tasks and out-of-scope geographies or populations.
4. Describe data classes, retention exposure, known suppliers, interfaces and permission boundaries.
5. Record a candidate **configuration baseline** including relevant version identifiers and hashes where supported.
6. Assign the business owner, technical owner, risk contact and acceptance authority.
7. Define the initial review trigger: onboarding, first production use, material update or scheduled review.
8. Verify the inventory entry with at least one system subject-matter expert.

## Example inventory card

| Field | Example, not live product data |
| --- | --- |
| System ID | SYS-042 |
| Use | Employee policy Q&A |
| Owner | Internal operations sponsor |
| Components | LLM, vector index, citation service, escalation workflow |
| Data classification | Internal; some restricted documents excluded |
| Critical restriction | Read-only, no ERP writes |
| Current baseline | BASE-042-2026-11 |

## Review checkpoints

- Does this inventory represent a unique use, rather than duplicate another record?
- Can a reviewer identify the exact model and data snapshots evaluated?
- Are human oversight and connected system privileges explicit?
- Are third-party dependencies visible and assigned to an owner?

**Output:** A reviewed inventory record and baseline ready for [Governance assessment](governance-assessment.md).
