# DAN AI - Webhooks (Event Notifications)

Webhooks are **not** an export format - they are event callbacks. When an extraction finishes, DAN AI fires an `extraction.completed` event to every registered endpoint.

There are two ways to receive completion events:

- **Account-wide webhooks** - managed under **Developer → Webhooks**. Fire on every completed extraction in the account.
- **Per-request `callback_url`** - passed as a form field on the REST API call. Fires only for that one extraction.

<a id="setting-up-an-account-wide-webhook"></a>

## Setting up an account-wide webhook

1. Open **Developer → Webhooks** in the dashboard.
2. Click **Add Webhook**.
3. Enter the destination URL (must be HTTPS).
4. Tick the events you care about (currently `extraction.completed`).
5. Save. DAN AI generates a **signing secret** - copy it now, you'll need it to verify deliveries.

The endpoint must respond with a 2xx status within **15 seconds**. Anything else is treated as a failure and retried (see [Retries and ordering](webhooks.md#retries-and-ordering)).

<a id="payload-shape"></a>

## Payload shape

```
{
  "event": "extraction.completed",
  "timestamp": "2026-04-15T14:32:18Z",
  "data": {
    "document_id": "42",
    "reference": "DAN-00042",
    "doc_type": "invoice",
    "state": "done",
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
    "source": "dashboard"
  }
}
```

| Key | Notes |
| --- | --- |
| `event` | Always `extraction.completed` today; more event types may be added. |
| `timestamp` | ISO-8601 UTC time DAN AI sent the event. |
| `data.document_id` / `data.reference` | Stable identifiers. Use `document_id` for API calls and `reference` for human-readable references. |
| `data.state` | Either `done` or `error`. Webhooks fire on both - check `state` before acting. |
| `data.source` | Where the document came from: `dashboard`, `inbox`, or `api`. |
| `data.fields` / `data.lines` / `data.confidence` | Same shape as the [REST API response](../../../creating-an-extraction/current/extraction/rest-api.md). |

<a id="verifying-signatures"></a>

## Verifying signatures

Every delivery includes two headers:

```
X-DAN-Signature: t=1716203400,v1=<hex hmac>
X-DAN-Delivery: <unique delivery id>
```

To verify:

1. Take the raw request body (the JSON as bytes, **not** parsed).
2. Compute `HMAC-SHA256(secret, "<timestamp>." + body)`.
3. Compare the hex digest to the `v1` value in `X-DAN-Signature` using a constant-time compare.
4. Reject if the timestamp is more than 5 minutes old (prevents replay).

<a id="nodejs-example"></a>

### Node.js example

```
const crypto = require('crypto');

function verify(req, secret) {
  const sig = req.headers['x-dan-signature'] || '';
  const m = sig.match(/^t=(\d+),v1=([a-f0-9]+)$/);
  if (!m) return false;
  const [, t, v1] = m;
  if (Math.abs(Date.now() / 1000 - Number(t)) > 300) return false;
  const expected = crypto
    .createHmac('sha256', secret)
    .update(`${t}.${req.rawBody}`)
    .digest('hex');
  return crypto.timingSafeEqual(Buffer.from(expected), Buffer.from(v1));
}
```

The raw body matters - most frameworks parse JSON before you see it, which mangles whitespace and breaks the HMAC. Capture `req.rawBody` (or the equivalent buffer) before parsing.

<a id="retries-and-ordering"></a>

## Retries and ordering

DAN AI retries failed deliveries with exponential backoff:

| Attempt | Delay |
| --- | --- |
| 1 (initial) | immediate |
| 2 | 30 seconds |
| 3 | 2 minutes |
| 4 | 10 minutes |
| 5 | 30 minutes |
| 6 (final) | 2 hours |

A delivery is considered failed if your endpoint returns non-2xx, times out (>15 s), or the TLS handshake fails. After the 6th attempt the delivery is marked permanently failed and surfaced under **Developer → Webhooks → Deliveries**.

Webhook deliveries are **not ordered** - a fast extraction triggered after a slow one can land first. If you need ordering, use the `timestamp` field on the payload.

<a id="inspecting-deliveries"></a>

## Inspecting deliveries

The **Developer → Webhooks → Deliveries** page shows the last few hundred attempts per endpoint, with the response status, latency, and full request/response bodies. Use it to debug a webhook that's failing in production.

A common pattern: copy a failing delivery's body and replay it against your local server (`curl -X POST localhost:3000/dan-webhook -H 'content-type: application/json' --data @body.json`).

<a id="per-request-callback_url"></a>

## Per-request `callback_url`

If you only want a callback for one specific extraction (rather than every extraction in the account), pass `callback_url` on the API call:

```
curl -X POST "https://dan.sdlccorp.com/api/external/v1/extract?async=true" \
  -H "X-API-Key: dan_live_xxxxxxxxxxxxxxxxxxxx" \
  -F "document=@invoice.pdf" \
  -F "doc_type=invoice" \
  -F "callback_url=https://your-app.example.com/dan-callback"
```

The callback uses the same payload shape and signature scheme as account-wide webhooks. The signing secret is the same as your account's primary webhook secret.

<a id="related"></a>

## Related

- [REST API](../../../creating-an-extraction/current/extraction/rest-api.md) - including the `callback_url` parameter.
- [JSON and Excel Exports](formats.md) - alternative when polling/exporting fits better than push events.
- [FAQ and Troubleshooting](../../../reference/current/reference/faq.md) - debugging webhook deliveries.

---

Source: [DAN AI - Webhooks (Event Notifications)](https://docs.sdlccorp.com/docs/dan-ai/export/webhooks/)
