# Plan a TEVV campaign

> Design meaningful validation across relevant environments

**Goal:** Build evaluation coverage that supports or challenges the claims associated with a declared system baseline.

## Procedure

1. Identify claims, risk-critical gates and operational scenarios.
2. Choose appropriate levels: unit/component, integrated application, security/authorization, agent action, user workflow and operational testing.
3. Select environments (offline test, simulation, SIL, HIL, controlled field or production observation where lawful and appropriate).
4. Define representative nominal, boundary, degraded, adversarial and rare-event scenarios.
5. Specify data versions, sampling strategy, test isolation, evaluation rubric, baseline identifiers and expected outcomes.
6. Assign executors, independent reviewers and rerun rules.
7. Capture execution IDs, time, inputs, evaluator version, metrics, outputs and raw artifacts.
8. Record failed and inconclusive results without suppressing inconvenient observations.
9. Check coverage gaps and require further evidence where decision-critical claims remain unsupported.

## Evidence matrix

| Claim | Nominal cases | Adverse cases | Environment | Minimum evidence |
| --- | --- | --- | --- | --- |
| Document access | Authorized role | Unauthorized role | Integrated test | Request logs and policy decisions |
| Escalation | Known answer | Unknown/high-risk answer | End-to-end | Transcript plus escalation trace |
| Tool safety | Approved read | Prohibited write | Agent sandbox | Tool authorization logs |
| Performance | Expected load | Degraded response | Staging | Timings, failures, trace metadata |

## Confidence and validity

A benchmark pass does not prove performance on unrepresented users, geographies or future model versions. Record dataset coverage and limitations; keep qualitative human adjudications where automated scores are insufficient.

**Output:** A run-indexed evidence set linked to the exact baseline and criteria. Continue to [Evidence review](evidence-review.md).
