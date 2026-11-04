# Plan integrations

> Connect evidence sources without losing identity or provenance

**Goal:** Integrate engineering, governance and monitoring tools so imported records remain usable for a later audit or decision.

Assurio publicly describes intended connections to requirements tools, model registries, MLOps, observability, simulation, testing infrastructure and enterprise GRC/ERP/CRM workflows. **Specific native connectors and public endpoints are not verified here.**

## Integration design process

1. Inventory sources, data owners, permitted data classifications and target use cases.
2. Establish stable cross-system identifiers for AI system, baseline, requirement, test run and evidence item.
3. Document expected event semantics: created, revised, superseded, revoked, retested, reviewed.
4. Choose pull/push/batch behavior based on availability, freshness and failure tolerance.
5. Define authentication, service identities, least-privilege roles, secrets rotation and encryption.
6. Establish idempotency, retries, dead-letter handling, clock normalization and reconciliation checks.
7. Validate source authenticity and attach provenance or integrity metadata where appropriate.
8. Test changed schemas, duplicate events, missing records, partial outages and permission denials.

## Integration contract checklist

| Topic | Questions to settle |
| --- | --- |
| Identifier | Which field is canonical across systems? |
| Versioning | What change creates a new baseline/evidence revision? |
| Security | Which actor can access which classifications? |
| Completeness | How are missing and rejected records reported? |
| Freshness | When is evidence considered stale? |
| Errors | Are updates retried safely and visibly? |
| Audit | Can the source and transformation be reconstructed? |

See [API reference](../../api-reference/README.md) for a specification-ready template without invented endpoint paths.
