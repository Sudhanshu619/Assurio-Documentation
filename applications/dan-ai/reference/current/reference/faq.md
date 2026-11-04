# DAN AI - FAQ and Troubleshooting

This page collects the questions we get most often, plus the symptoms that show up most often in production and how to fix them. For deeper coverage of a specific topic, follow the links into the rest of the documentation.

<a id="tips-and-best-practices"></a>

## Tips and best practices

<a id="pick-the-most-specific-document-type-you-can"></a>

### Pick the most specific document type you can

`invoice` will outperform `general` on the same file because the invoice prompt teaches the AI about line items, tax columns and totals. Same goes for `bank_statement` vs `general` on a statement, or `medical_report` vs `general` on a lab report. See the full list at [Supported Document Types](../../../features/current/features/document-types.md).

<a id="contrast-matters-more-than-resolution"></a>

### Contrast matters more than resolution

For scanned documents, a clean 200-DPI black-on-white scan usually beats a 400-DPI scan with a faded background. Re-scan rather than upscaling a low-contrast original.

<a id="edit-once-mark-verified"></a>

### Edit once, mark verified

If a field is consistently wrong on a particular vendor's documents, edit it once and click **Mark Verified**. The verified values are what flow into exports and webhook payloads - the raw AI response is still preserved in `document_extractions.raw_response` for audit.

<a id="iterate-prompts-against-the-same-document"></a>

### Iterate prompts against the same document

When iterating on a custom prompt, re-extract the **same document** several times to compare runs without re-uploading. Saves time and gives you a clean comparison. See [Custom Fields and Templates](../../../features/current/features/custom-fields.md).

<a id="use-the-activity-log-to-spot-recurring-problems"></a>

### Use the Activity log to spot recurring problems

**Developer → Activity** shows recent API calls with status codes and error messages. If you're seeing the same 4xx error on every call, it's almost always a client bug. Same 5xx on every call to one `doc_type` usually means a provider issue - check **Settings → AI Providers**.

<a id="frequently-asked-questions"></a>

## Frequently asked questions

<a id="which-file-formats-does-dan-ai-accept"></a>

### Which file formats does DAN AI accept?

PDFs, PNGs and JPGs. A multi-page PDF is processed as a single document. PDFs containing scanned images are supported - DAN AI runs OCR transparently.

<a id="is-there-a-file-size-limit"></a>

### Is there a file-size limit?

Yes - a per-file size limit applies on every upload path. Very large multi-page PDFs may also be **truncated** by the AI provider's context window even if they're under the file limit. If you receive empty or partial fields on a long document, try splitting it.

<a id="does-dan-ai-store-my-files"></a>

### Does DAN AI store my files?

Uploaded files are stored encrypted at rest so that the document detail page can preview them later. You can delete a document (and its underlying file) any time from the dashboard or via the API.

<a id="are-oauth-refresh-tokens-safe"></a>

### Are OAuth refresh tokens safe?

Yes. Refresh tokens from Gmail/Outlook OAuth are encrypted at rest using **AES-256-GCM**. Tokens are only ever decrypted in-memory when a sync runs.

<a id="which-ai-providers-does-dan-ai-use"></a>

### Which AI providers does DAN AI use?

The default provider chain is **Ollama → OpenRouter → Groq**. Ollama is the primary provider; if it fails or times out, DAN AI automatically falls back to the next provider in the chain. Admins can re-order or disable providers under **Settings → AI Providers**.

<a id="how-long-does-a-typical-extraction-take"></a>

### How long does a typical extraction take?

| File | Typical time |
| --- | --- |
| Single-page invoice / receipt | 2–6 s |
| Multi-page bank statement | 8–25 s |
| Long contract (10+ pages) | 15–60 s |
| Failed and retried via fallback provider | up to 90 s |

<a id="do-webhook-deliveries-come-in-order"></a>

### Do webhook deliveries come in order?

No - a fast extraction triggered after a slow one can land first. Use the `timestamp` field on the payload if you need ordering. See [Webhooks](../../../export-delivery/current/export/webhooks.md).

<a id="can-i-export-multiple-documents-at-once"></a>

### Can I export multiple documents at once?

Yes. From the **Documents** list, tick the documents you want and pick **Export → JSON (zip)** or **Export → Excel (combined)**. Programmatically, iterate the documents list endpoint and pull each one individually.

<a id="can-i-run-dan-ai-from-my-own-infrastructure"></a>

### Can I run DAN AI from my own infrastructure?

DAN AI is a hosted SaaS at [dan.sdlccorp.com](https://dan.sdlccorp.com). For on-premise or VPC-deployed installations, contact SDLC Corp directly.

<a id="troubleshooting"></a>

## Troubleshooting

<a id="stuck-in-processing-for-more-than-5-minutes"></a>

### Stuck in `processing` for more than 5 minutes

**Likely cause:** the AI provider chain couldn't recover.

**Fix:** Open **Settings → AI Providers** and check each provider's status. Retry the extraction from the document detail page. If retries also stick, an admin may need to refresh provider API keys. The provider chain auto-repairs once a working provider is found again.

<a id="confidence-below-50-on-every-upload"></a>

### Confidence below 50 on every upload

**Likely cause:** scan quality, or the wrong `doc_type`.

**Fix:** Re-scan at higher contrast (not necessarily higher DPI). If that doesn't help, switch the document type to `general` for one run to see what the AI actually extracts - that often reveals what's going wrong.

<a id="inbox-sync-not-picking-up-new-mail"></a>

### Inbox sync not picking up new mail

**Possible causes:**

- The OAuth refresh token expired or was revoked → **reconnect the mailbox** from **Inboxes**.
- A rule's regex is invalid → open **Inboxes → Manage Rules** and dry-run the ruleset.
- The sender / subject doesn't actually match any rule → dry-run with a sample to confirm.
- The provider rate-limited DAN AI → wait for the next interval, no action needed.

<a id="401-unauthorized-on-the-api"></a>

### `401 Unauthorized` on the API

**Cause:** missing, wrong, or revoked API key.

**Fix:** Generate a new key from **Developer → API Keys**. Confirm you're sending the right header (`X-API-Key:` *or* `Authorization: Bearer …`, not both).

<a id="413-payload-too-large-on-the-api"></a>

### `413 Payload Too Large` on the API

**Cause:** the file exceeds DAN AI's per-file size limit.

**Fix:** Split a multi-page PDF, or re-render the file at a lower DPI. For very long bank statements, splitting by month also improves extraction quality.

<a id="429-too-many-requests-on-the-api"></a>

### `429 Too Many Requests` on the API

**Cause:** API-key rate limit hit.

**Fix:** Back off until the `X-RateLimit-Reset` timestamp (unix seconds) in the response headers. Spread bursty workloads using `async=true` to queue extractions instead of running them synchronously.

<a id="excel-export-missing-line-items"></a>

### Excel export missing line items

**Cause:** the document type has no line items (resumes, contracts, ID cards, shipping labels, etc.).

**Fix:** This is expected - the **Line Items** sheet is omitted entirely for non-tabular types. The **Fields** sheet still contains everything.

<a id="webhook-deliveries-failing-with-408--timeout"></a>

### Webhook deliveries failing with `408` / timeout

**Cause:** your endpoint took longer than 15 seconds to respond.

**Fix:** Acknowledge the delivery with a 2xx **first**, then do the heavy work in a background job. DAN AI doesn't wait for your processing - it only cares that the delivery was received.

<a id="webhook-signature-verification-fails"></a>

### Webhook signature verification fails

**Cause:** the body has been parsed/re-serialized before HMAC computation, changing whitespace.

**Fix:** Capture the **raw request body** as bytes before any JSON parsing. In Express, that's `bodyParser.json({ verify: (req, res, buf) => { req.rawBody = buf; } })`. In other frameworks, look for an equivalent "raw body" hook. See [Webhooks](../../../export-delivery/current/export/webhooks.md) for a Node.js example.

<a id="still-stuck"></a>

## Still stuck?

- Live product: **[dan.sdlccorp.com](https://dan.sdlccorp.com)**
- Support: **[SDLC Corp Support](https://sdlccorp.com/contact-us/)**
- Email: **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [DAN AI - FAQ and Troubleshooting](https://docs.sdlccorp.com/docs/dan-ai/reference/faq/)
