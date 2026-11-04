# Assure adaptive AI

> Keep evidence valid when an AI system changes

**Goal:** Define allowed adaptation and proof that the changed system still satisfies its acceptance conditions.

## Adaptation types

Updates may affect model weights, prompts, policies, retrieval corpus, calibration thresholds, agent tools, sensor configuration, operating domain or human procedures. The risk significance depends on the claims the change touches.

## Procedure

1. Describe adaptation mechanisms and distinguish **allowed variation within the accepted envelope** from material change.
2. Establish a controlled baseline manifest and identify approval-critical components.
3. Map requirements to components, data populations, operating domains and evaluation artifacts.
4. Define triggers for impact analysis: version promotion, drift, incident, tool change, supplier update, new users or changed permissions.
5. On change, record old and new configurations and reasons for the update.
6. Identify affected requirements and mark their evidence as requiring confirmation where appropriate.
7. Re-run targeted tests in relevant environments; explain why unaffected evidence may be reused.
8. Obtain a new or amended decision if the approval scope or critical claims have changed.

## Example

An internal retrieval assistant replaces its base model while keeping the same user interface. Citation accuracy, refusal behavior and escalation could all change. The prior acceptance cannot automatically be carried forward simply because the app remains functional. The change review identifies those claims and demands appropriate regression evidence.

**Output:** A documented continuity-of-assurance record, rather than an undocumented assumption that last quarter's evidence still applies.
