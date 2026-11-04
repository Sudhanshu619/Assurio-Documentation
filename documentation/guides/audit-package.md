# Prepare an audit package

> Export a coherent chain from scope to accountable decision

**Goal:** Help an internal or external reviewer understand one decision without searching through disconnected test folders.

## Recommended contents

| Section | Minimum contents |
| --- | --- |
| System scope | Purpose, users, exclusions, operating domain and baseline |
| Governance | Named roles, policies, delegated authority and access |
| Risk | Inherent/residual exposure, mitigations, exceptions |
| Requirements | Versioned acceptance criteria and critical gates |
| TEVV | Test plans, environments, run metadata, result summaries |
| Evidence index | Source, artifact IDs, provenance, status, integrity metadata |
| Findings | Open and closed findings, deviations and retests |
| Decision | Outcome, reviewer, rationale, conditions, restrictions, expiry |
| Change history | Relevant component changes and reassessment records |

## Procedure

1. Choose one decision and its exact baseline. Avoid merging incompatible versions into a single unexplained package.
2. Generate or assemble a requirements-to-evidence traceability index.
3. Include rejected, failed and inconclusive evidence that materially informed the review.
4. Redact sensitive data only according to a documented policy and retain artifact identifiers so provenance is not lost.
5. Verify permissions for the intended reviewers and a safe expiration or revocation path for shared files.
6. Record package date, generator/author, contents checksum where applicable, and the decision ID.
7. Ask a reviewer who was not on the delivery team to trace a sample claim and find its evidence.

**Export behavior:** Public materials do not establish native Assurio export buttons or exact downloadable formats. The package above is a recommended information structure, not a promised product feature.
