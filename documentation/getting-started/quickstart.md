# Quickstart

> Complete an example assurance review from scope to decision

This walkthrough uses a **hypothetical internal policy assistant**, not a documented customer system or a guaranteed sequence of button clicks in Assurio. Adapt the example to the forms and permissions available in your environment.

## Scenario

An organization operates an employee assistant that answers questions using approved policy documents. It should cite the source material, avoid exposing unauthorized records and refer uncertain requests to a human. It must never modify financial or HR source records.

| Scope attribute | Example value |
| --- | --- |
| System | Internal Policy Assistant |
| Baseline | `policy-assistant/1.0` |
| Intended users | Approved internal employees |
| Sources | Versioned internal policy repository |
| Permitted outputs | Informational, cited answers |
| Prohibited actions | Writing enterprise records; high-stakes individual decisions |
| Required oversight | Human escalation for uncertain or out-of-scope requests |

### Step 1 — Scope the system

Create or locate the AI system record using your deployment's system inventory feature. Capture intended use, user groups, business owner, model/provider, data sources, tools, interfaces, operating environment and exclusions. Assign a stable configuration identifier.

**Check:** Another reviewer should be able to tell what configuration was actually evaluated without asking the project team.

### Step 2 — Set governance and responsibilities

Identify the system owner, risk reviewer, evidence reviewer and authorized acceptance authority. Define the policies and risk criteria that apply. Record whether the same person holds multiple responsibilities and any additional independence requirements.

### Step 3 — Assess risk and controls

Document plausible harms, affected parties, threat or failure modes, severity, likelihood, existing mitigations and residual risk. For the example, include confidential information exposure, inaccurate policy advice, authorization bypass and loss of escalation.

### Step 4 — Declare acceptance criteria

Create testable claims such as:

- **REQ-001 — Entitlements:** users cannot retrieve documents outside their approved access scope.
- **REQ-002 — Grounding:** answers cite the correct version of an approved source.
- **REQ-003 — Escalation:** ambiguous or unsupported requests invoke the agreed human-review pathway.
- **REQ-004 — Non-mutation:** the assistant cannot write to underlying operational systems.

For each claim define the evaluation method, environments, acceptance threshold, known exceptions and owner. A qualitative promise is not a measurable acceptance criterion.

### Step 5 — Connect testing and evidence

Evaluate nominal, boundary, adverse and user-permission scenarios. Preserve run metadata, baseline, test conditions, evaluator, results, source artifacts and any failures. Do not discard inconclusive or negative observations.

### Step 6 — Review findings

Group open issues by their impact on critical controls. If contractor-access tests fail, do not hide them behind an overall answer-quality average. Investigate and either remediate and retest, restrict the affected user group, or block acceptance.

### Step 7 — Record a scoped decision

An authorized person records the outcome, target baseline, approved user groups, allowed activities, excluded actions, conditions, evidence references, unresolved findings and next review trigger. Example: *Restricted internal pilot, employees only; no write actions; subject to monthly evidence review and any model/provider update.*

> The example statement is **illustrative**. It grants no real authorization.

### Step 8 — Reassess after change

If the model, index, retrieval policy or tool permissions change, compare the new configuration with the approved baseline. Identify affected claims, require new evidence for those claims, and document whether operating permission remains valid, is narrowed or is withdrawn.

## Completion checklist

- [ ] System and configuration identified
- [ ] Owner and approval authority named
- [ ] Intended use, users, exclusions documented
- [ ] Risks and control owners defined
- [ ] Testable acceptance criteria recorded
- [ ] Relevant evidence and limitations retained
- [ ] Open findings dispositioned
- [ ] Scoped decision recorded by an authorized person
- [ ] Change triggers and re-review responsibility assigned

Continue with [Your first assurance review](first-assurance-review.md) for a more formal sign-off package.
