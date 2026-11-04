# Decisions and change

> Understand bounded acceptance and material reassessment

A **scoped decision** authorizes, restricts, defers or rejects a clearly defined use of a specified AI configuration. It is not a permanent statement about the model in every environment.

## Decision anatomy

A useful record includes decision ID, accountable authority, review date, baseline, purpose, allowed users, permitted operations, excluded behaviors, evidence package, open findings, conditions, expiry/review triggers and rationale.

## Examples of decision outcomes

- **Approved within scope:** requirements satisfied for the declared conditions.
- **Conditionally approved:** operation permitted only with explicit restrictions and owners.
- **Deferred:** additional evidence or independent review is required.
- **Rejected:** a critical requirement or risk tolerance is not met.
- **Suspended/reopened:** material change or incident prevents reliance on prior approval.

These labels are conceptual examples. Check the actual configured status values in your environment.

## What can reopen a decision?

Material changes may include model replacement, prompt or policy revision, new data population, altered permissions, additional agent tools, updated acceptance threshold, changed deployment environment, incidents or a new regulatory requirement.

Impact analysis should identify affected claims and their evidence, preserve the previous decision history and make the reason for reuse of unaffected evidence explicit.

See [Change and reassessment](../guides/change-reassessment.md).
