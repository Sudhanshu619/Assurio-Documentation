# Deployment and environment planning

> Plan hosted, dedicated and controlled enterprise configurations

Assurio's product description references customer-hosted and dedicated deployments, connected edge and disconnected design considerations. These choices are **architectural capabilities/designs**, not evidence that every hosting mode is available in every subscription or release.

## Choose the operating pattern

| Pattern | Considerations |
| --- | --- |
| Hosted service | Tenant isolation, region, identity, encryption, retention, SLA |
| Dedicated/customer-hosted | Responsibility split, upgrades, infrastructure monitoring, backups |
| Connected edge | Network trust, worker identity, bandwidth, data minimization |
| Disconnected operation | Offline authorization, local logs, sync conflict, evidence freshness |

## Planning checklist

1. Define data classifications and whether evidence may leave the customer's environment.
2. Agree on identity integration, role- and attribute-based access, audit log retention and incident ownership.
3. Identify all ingestion and execution workers; separate untrusted evaluation workloads from evidence services.
4. Set encryption, key lifecycle, backup, restoration testing and disaster-recovery objectives.
5. Define synchronization semantics, stale evidence labeling, conflict resolution and reconciliation.
6. Specify deployment change management and rollback readiness.
7. Validate support ownership, observability, upgrade and release-notification processes.

## Before production

Request a deployment-specific architecture diagram, hardening guide, data processing terms, service-level targets and threat model from the Assurio provider or your technical team. Never infer hosting region, certifications, uptime guarantees or default retention values from marketing copy.
