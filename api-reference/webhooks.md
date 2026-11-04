# Events and webhooks

> Define reliable change and evidence notifications

Assurio's connected assurance model includes change monitoring and affected-evidence reassessment. The reviewed public information does **not** document a publicly available webhook service or specific event names. The following is a **recommended design specification** if an event-based integration is supported.

## Events worth modeling

| Conceptual event | Why subscribers care |
| --- | --- |
| Baseline changed | Identify requirements/evidence that need impact review |
| Evidence submitted/revised | Request quality review or re-index evidence |
| Finding status changed | Recheck decision conditions and open exceptions |
| Decision issued/reopened | Synchronize deployment gate or GRC record |
| Control changed | Reassess whether operating permission remains enforceable |

## Questions for engineering

Confirm delivery mechanism, event catalog, schema versioning, signature verification, at-least-once versus exactly-once expectations, ordering, retries, dead-letter queues, replay windows, tenant filtering and revocation. Document timestamps and event identity so duplicate processing is safe.

## Consumer hardening

Use event IDs for idempotency, verify origin and signature when provided, apply least privilege, separate ingestion from processing, and reconcile periodically against authoritative state. A notification should not be treated as proof that an approval change has already been enforced in production.
