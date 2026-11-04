# DAN AI - Custom Fields and Templates

DAN AI gives you three layers of control over what each extraction returns, from most local to most global:

1. **Per-document custom fields** - tick a subset for a single extraction.
2. **Account-wide default fields** - set the default field list per document type.
3. **Custom prompts** - override the built-in prompt for a document type entirely.

You can mix all three. The lowest layer with an explicit value wins.

<a id="1-per-document-custom-fields"></a>

## 1. Per-document custom fields

After upload, an optional **Configure Fields** step lets you tick the specific fields you want extracted from this document. If you skip it, DAN AI returns every field in the prompt's default schema.

- Saved per-document in the `custom_fields` column.
- Only affects this extraction - never changes the account-wide prompt.
- Available from the dashboard upload modal and via the API's `fields` (or `custom_fields`) parameter - see [REST API](../../../creating-an-extraction/current/extraction/rest-api.md).

<a id="when-to-use-it"></a>

### When to use it

- You only need a subset (e.g. just `total_amount` and `vendor_name` from a long multi-page invoice).
- You're iterating: trying out a smaller field set to see if accuracy improves.
- You want a one-off extraction tailored to an unusual file, without disturbing other users' defaults.

<a id="example-via-api"></a>

### Example via API

```
curl -X POST https://dan.sdlccorp.com/api/external/v1/extract \
  -H "X-API-Key: dan_live_xxxxxxxxxxxxxxxxxxxx" \
  -F "document=@invoice.pdf" \
  -F "doc_type=invoice" \
  -F "fields=invoice_number,total_amount,vendor_name,invoice_date"
```

The response's `fields` block will contain only those four keys (plus `lines` if line items were requested).

<a id="2-account-wide-default-fields"></a>

## 2. Account-wide default fields

If your team always wants the same field list out of invoices (or any other type), set it once under **Settings → Default Fields** (admin only).

- Pick a `doc_type`, then tick the fields that should be returned by default.
- Save. Every future extraction of that type - dashboard, inbox sync, or API - uses this field list unless overridden.
- A per-document or per-API-call `custom_fields` value still wins over the default.

<a id="why-use-it"></a>

### Why use it

- Consistency - every team member's extractions return the same shape, making downstream code simpler.
- Cost / latency - smaller field lists usually run faster and use fewer tokens.
- Cleaner exports - Excel exports only show columns for the fields you care about.

<a id="3-custom-prompts-admin-only"></a>

## 3. Custom prompts (admin only)

For non-standard layouts - invoices where the total is at the top, contracts in a non-English language, medical reports from a specific lab - you can replace the built-in prompt entirely.

Open **Settings → Custom Prompts** (admin only), pick a `doc_type`, and edit the prompt template. DAN AI uses your version for every extraction of that type from then on, across every ingestion path.

<a id="iterating-on-a-custom-prompt"></a>

### Iterating on a custom prompt

tip

When iterating on a custom prompt, re-extract the **same document** multiple times to compare results without re-uploading. The raw AI response stays in `document_extractions.raw_response` for every run, so you can diff one attempt against the next.

A reasonable workflow:

1. Save your current prompt as the baseline (download a copy).
2. Make one small change.
3. Re-run extraction on 3–5 representative documents.
4. Compare the new responses against the baseline.
5. Keep or revert.

<a id="when-not-to-use-a-custom-prompt"></a>

### When **not** to use a custom prompt

- One-off problems → fix with per-document custom fields instead.
- General accuracy drift → check scan quality first, then `doc_type` selection. Prompts are powerful but easy to overfit.
- Anything that mentions a specific company's proprietary identifiers - those belong in custom fields, not the prompt.

<a id="layer-precedence"></a>

## Layer precedence

When all three layers are in play, DAN AI resolves them in this order:

1. **Per-request `fields` / `custom_fields`** (from the dashboard modal or API call).
2. **Account-wide default fields** for that `doc_type`.
3. **The prompt's default field set** (built-in or custom).

If layer 1 is set, it wins outright. Otherwise layer 2. Otherwise layer 3.

<a id="removing-a-custom-prompt"></a>

## Removing a custom prompt

To revert to the built-in prompt for a `doc_type`, open **Settings → Custom Prompts**, select the type and click **Restore Default**. The change applies to the next extraction.

<a id="related"></a>

## Related

- [Confidence Scores](confidence-scores.md) - restricting to a smaller field list often raises confidence on the fields that remain.
- [Supported Document Types](document-types.md) - the full list of types you can configure defaults / prompts for.

---

Source: [DAN AI - Custom Fields and Templates](https://docs.sdlccorp.com/docs/dan-ai/features/custom-fields/)
