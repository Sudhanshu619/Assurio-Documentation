# Integration troubleshooting

> Diagnose ingestion and synchronization problems

The actual connector catalog, authentication scheme and API paths must be confirmed with the integration owner.

## Diagnostic sequence

1. Identify the source system and target Assurio environment.
2. Verify that the service account still has the intended least-privilege access.
3. Confirm baseline/system IDs and schema version mappings are correct.
4. Compare source artifact count with imported/accepted/rejected record counts.
5. Check for duplicate events, replayed messages or rejected transformations.
6. Validate timestamps, permissions and data classification restrictions.
7. Check whether the artifact was superseded or its source became unavailable.
8. Use your approved support channel for persistent issues, supplying sanitized logs and correlation identifiers.

## Common symptoms

| Symptom | Likely area to investigate |
| --- | --- |
| Missing runs | Ingestion failure or filter/ID mismatch |
| Old evidence | Sync delay, stale baseline or source revision |
| Duplicate records | Missing idempotency or source ID handling |
| Permission denied | Incorrect identity scope or tenant restrictions |
| Partial campaign | Pagination or batch/timeout/retry failures |

**Never** disable audit logging or weaken authentication as a workaround for synchronization failures.
