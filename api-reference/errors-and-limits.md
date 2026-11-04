# Errors, retries and limits

> Specify resilience behaviors without inventing response codes

An official Assurio API error catalog, rate-limit policy and pagination scheme were **not found in published product information**. The principles below are engineering requirements to confirm against the implemented API.

## Error taxonomy to document

| Error category | Consumer action |
| --- | --- |
| Invalid input | Fix schema or data and do not blindly retry |
| Unauthorized / forbidden | Refresh/repair authorized credentials or request access |
| Record not found | Check canonical IDs and tenant visibility |
| State conflict | Re-read the current revision and reconcile |
| Rate-limited | Respect confirmed retry/backoff guidance |
| Temporary service failure | Retry only idempotent operations with bounded backoff |
| Partial integration failure | Quarantine and report incomplete evidence imports |

These are **conceptual categories**, not confirmed Assurio status codes or error body values.

## Safe client behavior

Preserve correlation IDs and source record IDs, apply bounded retries, avoid logging tokens and raw sensitive evidence, and expose integration health to human operators. Test for missing evidence and reconciliation drift; a silent import failure can invalidate the completeness of an assurance case.

## Publication checklist

Before a developer example is marked executable, provide verified error response fields, HTTP codes if applicable, max request and upload sizes, pagination rules, concurrency conflicts, schema version policy and official rate limits.
