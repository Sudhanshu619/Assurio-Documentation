# DAN AI - Dashboard Upload

The fastest way to start an extraction. From the sidebar, open **Documents** (or the Dashboard) and click **New Extraction** to open the upload modal.

<a id="1-drop-the-file"></a>

## 1. Drop the file

The upload modal accepts a single file at a time. Supported formats:

- **PDF** (single or multi-page)
- **PNG**
- **JPG / JPEG**

Drag the file into the drop zone or click **Browse**. The file uploads and the document is created in the `draft` state.

<a id="2-choose-a-document-type"></a>

## 2. Choose a document type

Pick the type that best describes the file. The type drives which prompt DAN AI sends to the AI provider, so a good match significantly improves accuracy. DAN AI ships 21 tuned types - anything unspecified falls back to `general`.

The types are grouped by category in the dropdown:

| Category | Types |
| --- | --- |
| **Finance** | `invoice`, `receipt`, `purchase_order`, `expense`, `bank_statement`, `payslip`, `tax_form`, `quote` |
| **Legal** | `contract`, `nda`, `insurance_policy`, `certificate` |
| **Logistics** | `delivery_note`, `shipping_label` |
| **People & ID** | `resume`, `id_card` |
| **Health** | `medical_report`, `prescription` |
| **General** | `general`, `letter`, `memo` |

See the full reference at [Supported Document Types](../../../features/current/features/document-types.md).

tip

Pick the **most specific type you can**. `invoice` will outperform `general` on the same file because the invoice prompt teaches the AI about line items, tax columns and totals.

<a id="3-configure-fields-optional"></a>

## 3. Configure fields (optional)

After upload, an optional **Configure Fields** step lets you tick the specific fields you want extracted from this document. If you skip it, DAN AI returns every field in the prompt's default schema.

- Field selection is saved per-document on the `custom_fields` column.
- It only affects this extraction - it does not change the account-wide prompt.
- Use it when you only need a subset (e.g. just the total and vendor from a long invoice).

To make a field selection the default for *every* extraction of this type, save it as an **account-wide default** under **Settings → Default Fields**.

<a id="4-run-the-extraction"></a>

## 4. Run the extraction

Click **Extract**. DAN AI transitions the document from `draft` to `processing` and dispatches it to the AI provider chain (Ollama → OpenRouter → Groq).

Processing time depends on the file's complexity:

| File type | Typical time |
| --- | --- |
| Single-page invoice / receipt | 2–6 seconds |
| Multi-page bank statement | 8–25 seconds |
| Long contract (10+ pages) | 15–60 seconds |
| Failed / retried via fallback provider | up to 90 seconds |

<a id="5-review-the-result"></a>

## 5. Review the result

When the extraction finishes, the document detail page opens with a two-column layout: the original file preview on one side, the extracted fields on the other.

What you'll see in the header:

- **State badge** - `draft`, `processing`, `done`, or `error`.
- **Document type** with the classifier confidence (e.g. *invoice · 95%*).
- **Verified pill** - appears once a human marks the document verified.

Every field is editable. Save changes inline; the original AI response stays preserved in `document_extractions.raw_response` so you can always diff against what the model returned.

<a id="state-machine"></a>

## State machine

| State | What it means | Triggered by |
| --- | --- | --- |
| `draft` | File uploaded, nothing extracted yet | Upload completes |
| `processing` | Extraction job is running | **Extract** action or a background job picks it up |
| `done` | Extraction finished successfully | AI provider returns valid JSON |
| `error` | Extraction failed | Provider error, malformed response, retry budget exhausted |

A document stuck in `processing` for more than ~5 minutes usually means the AI provider chain couldn't recover - see [FAQ and Troubleshooting](../../../reference/current/reference/faq.md).

<a id="mark-as-verified"></a>

## Mark as verified

Once you've reviewed and (optionally) corrected the fields, click **Mark Verified**. The verified values are what flow into exports and webhook payloads. Verification is per-document; you can always un-verify and re-edit.

<a id="next-steps"></a>

## Next steps

- Export the result: [JSON and Excel Exports](../../../export-delivery/current/export/formats.md)
- Receive completion events: [Webhooks](../../../export-delivery/current/export/webhooks.md)
- Automate the same flow at scale: [Email Inbox Sync](inbox-sync.md) or [REST API](rest-api.md)

---

Source: [DAN AI - Dashboard Upload](https://docs.sdlccorp.com/docs/dan-ai/extraction/dashboard-upload/)
