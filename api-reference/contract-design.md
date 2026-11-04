# Endpoint contract worksheet

> Design a verified API reference once the specification is available

**Status:** API shape unknown from public materials. Use this worksheet for each real endpoint once provided by the Assurio engineering team. Do **not** publish any method/path until verified.

## Endpoint documentation template

| Field | Description |
| --- | --- |
| Method and path | Verified verb + absolute/relative route |
| Availability | Cloud/dedicated/edge and supported release |
| Required authorization | Confirmed service role, scope and tenant restrictions |
| Input schema | Field type, required/optional, validation and version |
| Output schema | Success format, identifiers and lifecycle states |
| Errors | Code, retryability, conflict behavior and diagnostic ID |
| Pagination | Cursor/page limits and ordering guarantees |
| Idempotency | Retry safety and duplicate handling |
| Audit logging | Request attribution, sensitive-data policy |
| Example | Sanitized request/response tested against official spec |

## Proposed example evidence payload — NOT an Assurio API contract

```json
{
  "example_only": true,
  "source_system": "external-test-runner",
  "external_record_id": "RUN-220",
  "system_id": "SYS-042",
  "baseline_id": "BASE-042-2026-11",
  "requirement_ids": ["REQ-003"],
  "result": "failed",
  "artifact_uri": "restricted://evaluation/RUN-220",
  "evaluated_at": "2026-11-02T09:00:00Z"
}
```

This illustrates **which information should remain linked**, not the field names or JSON accepted by the platform.

## Definition of done for API publication

- [ ] Engineering has supplied an authoritative OpenAPI/GraphQL/gRPC contract.
- [ ] Documentation examples run successfully against a supported environment.
- [ ] Authentication and tenant isolation are documented and tested.
- [ ] Error handling, pagination, limits and rate policies are confirmed.
- [ ] Security and data-governance reviewers have approved example payloads.
