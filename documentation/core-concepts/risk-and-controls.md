# Risk, impact and controls

> Connect potential harms to mitigations and accountable decisions

An AI risk assessment describes what can go wrong, who or what may be affected, and which controls reduce the exposure. Assess the **system in context**, not the model in isolation.

## Assessment dimensions

Consider privacy, confidentiality, fairness, reliability, safety, security, misuse, tool autonomy, supplier dependency, legal duties, environmental conditions, and the quality of human oversight. For each scenario, record the affected actors and credible failure path.

| Record | Question answered |
| --- | --- |
| Risk statement | What failure or harm could occur? |
| Inherent risk | What is the exposure before additional controls? |
| Control | What prevents, detects or limits the harm? |
| Evidence | How do we know the control operated in the relevant conditions? |
| Residual risk | What risk remains after tested mitigation? |
| Owner | Who remains accountable? |
| Exception | What approved deviation exists, for how long and under what restrictions? |

## Controls need an implementation boundary

A requirement such as “no unauthorized record updates” should identify which credentials, gateway, execution tool or human step actually blocks the write. A policy statement by itself does not prove technical enforcement.

## Framework mapping

Assurio describes mapping to NIST AI RMF, ISO/IEC 42001, ISO/IEC 23894, EU AI Act and internal controls. Mappings help navigate obligations and evidence; they **do not automatically confer certification or legal compliance**. See [Framework mapping](../reference/framework-mapping.md).
