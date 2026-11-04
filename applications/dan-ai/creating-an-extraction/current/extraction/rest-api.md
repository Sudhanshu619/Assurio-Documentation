# DAN AI - REST API

For programmatic use. Generate an API key from **Developer → API Keys**, then send files to the public extraction endpoint under `/api/external/v1`.

<a id="authentication"></a>

## Authentication

External endpoints authenticate with your raw API key, via either header:

```
X-API-Key: dan_live_xxxxxxxxxxxxxxxxxxxx
Authorization: Bearer dan_live_xxxxxxxxxxxxxxxxxxxx
```

Keys are shown **once** at creation time and stored as a SHA-256 hash server-side. Lost keys cannot be recovered - revoke and regenerate from **Developer → API Keys**.

Treat keys as secrets

Never commit a key to source control, embed it in client-side JavaScript, or share it in screenshots. If a key leaks, revoke it immediately from the dashboard - the revocation takes effect on the next request.

<a id="endpoints"></a>

## Endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/api/external/v1/health` | Confirm the key works. Returns `{ ok: true }`. |
| `POST` | `/api/external/v1/extract` | Upload a file and extract (synchronous by default). |
| `POST` | `/api/external/v1/extract?async=true` | Queue extraction; returns a job id to poll. |
| `GET` | `/api/external/v1/documents/:id` | Fetch a previously extracted document. |
| `GET` | `/api/external/v1/jobs/:id` | Poll an async extraction job. |

All paths are relative to your DAN AI base URL, e.g. `https://dan.sdlccorp.com/api/external/v1/extract`.

<a id="request-format"></a>

## Request format

`POST /api/external/v1/extract` is a `multipart/form-data` request:

| Field | Type | Notes |
| --- | --- | --- |
| `document` | file | The PDF, PNG, or JPG to extract. **Required.** |
| `doc_type` | string | One of the 21 supported types. Optional - falls back to `general` if omitted or invalid. |
| `fields` / `custom_fields` | string | Comma-separated list of fields to restrict the extraction to. Optional. |
| `async` | boolean-ish | Use `true`, `1`, or `yes` to queue a job. Optional. |
| `callback_url` | URL | DAN AI posts the completed payload here. Optional. Useful when combined with `async=true`. |

<a id="example-synchronous-extraction"></a>

### Example: synchronous extraction

```
curl -X POST https://dan.sdlccorp.com/api/external/v1/extract \
  -H "X-API-Key: dan_live_xxxxxxxxxxxxxxxxxxxx" \
  -F "document=@invoice.pdf" \
  -F "doc_type=invoice" \
  -F "fields=invoice_number,total_amount,vendor_name"
```

<a id="example-async-with-callback"></a>

### Example: async with callback

```
curl -X POST "https://dan.sdlccorp.com/api/external/v1/extract?async=true" \
  -H "X-API-Key: dan_live_xxxxxxxxxxxxxxxxxxxx" \
  -F "document=@statement.pdf" \
  -F "doc_type=bank_statement" \
  -F "callback_url=https://your-app.example.com/dan-webhook"
```

<a id="response-example"></a>

## Response example

A successful synchronous extraction returns the full document payload:

```
{
  "fields": {
    "invoice_number": "INV-0001",
    "vendor_name": "Acme Corp",
    "invoice_date": "2026-04-15",
    "total_amount": 1250,
    "currency": "USD"
  },
  "lines": [
    { "description": "Consulting", "quantity": 10, "price_unit": 125 }
  ],
  "confidence": { "invoice_number": 95, "total_amount": 97 },
  "ai": {
    "provider": "ollama",
    "model": "qwen2.5vl:32b",
    "process_time_ms": 3120,
    "total_tokens": 1842
  },
  "meta": {
    "success": true,
    "document_id": "42",
    "reference": "DAN-00042",
    "doc_type": "invoice",
    "state": "done"
  }
}
```

<a id="top-level-keys"></a>

### Top-level keys

| Key | What it holds |
| --- | --- |
| `fields` | The structured fields the AI extracted, keyed by field name. |
| `lines` | Line-item rows, populated for invoices, receipts, bank statements and medical reports. Empty array otherwise. |
| `confidence` | Per-field confidence score (0–100). Only fields the AI is uncertain about always appear here. |
| `ai` | Which provider/model handled the request and how much it cost. |
| `meta` | Document identifiers and the final state (`done` or `error`). |

<a id="polling-for-status-async-jobs"></a>

## Polling for status (async jobs)

When you pass `async=true`, the call returns a job id immediately instead of the extracted payload:

```
{ "job_id": "job_abc123", "state": "queued", "poll_url": "/api/external/v1/jobs/job_abc123" }
```

Poll `GET /api/external/v1/jobs/:id` until the job reports `done` or `error`:

```
{ "job_id": "job_abc123", "state": "done", "document_id": "42" }
```

Then fetch the result from `GET /api/external/v1/documents/:id`.

A reasonable poll cadence: every **3 seconds for the first 30 seconds**, then every **10 seconds** after that. Most documents finish in under a minute.

<a id="error-responses"></a>

## Error responses

DAN AI uses standard HTTP status codes:

| Status | Meaning |
| --- | --- |
| `400` | Request malformed (missing `document`, unsupported file type, bad `doc_type`). |
| `401` | Missing, wrong or revoked API key. |
| `413` | File too large (DAN AI's per-file limit). |
| `429` | Rate limit hit. Back off and retry. |
| `5xx` | Provider error or DAN AI internal issue. Safe to retry the same request. |

Error bodies use the shape:

```
{ "error": { "code": "invalid_doc_type", "message": "doc_type 'foo' is not supported" } }
```

<a id="rate-limits"></a>

## Rate limits

API keys are subject to a per-key rate limit. The current limit and your remaining quota are returned in response headers:

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 87
X-RateLimit-Reset: 1716203400
```

If you hit `429`, sleep until `X-RateLimit-Reset` (unix seconds) and retry. The dashboard's **Developer → Activity** page shows recent API calls and their status codes, which is the fastest way to spot a misbehaving client.

<a id="next-steps"></a>

## Next steps

- Configure webhook delivery so you don't have to poll: [Webhooks](../../../export-delivery/current/export/webhooks.md).
- Understand the `confidence` block: [Confidence Scores](../../../features/current/features/confidence-scores.md).
- See every `doc_type` value the API accepts: [Supported Document Types](../../../features/current/features/document-types.md).

---

Source: [DAN AI - REST API](https://docs.sdlccorp.com/docs/dan-ai/extraction/rest-api/)
