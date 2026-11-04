# DAN AI - Confidence Scores and Accuracy

Every extraction is stamped with a confidence score between **0 and 100**, visible on the document detail page in the dashboard and in the `accuracy_percent` column of `document_extractions` (or the `confidence` block in API responses).

The score reflects how certain the AI is that the value it returned is correct. It's not a guarantee of correctness - but it's a strong signal for where to focus human review.

<a id="score-ranges"></a>

## Score ranges

| Range | Meaning | Recommended action |
| --- | --- | --- |
| **90 – 100** | High confidence | Auto-approve in most workflows. Spot-check a sample once a week to confirm. |
| **75 – 89** | Medium confidence | Quick human review of the key fields (total, dates, identifiers). |
| **50 – 74** | Low confidence | Full field-by-field review. The file may be scanned, partially obscured, or use unusual terminology. |
| **0 – 49** | Very low / failed | Re-extract with a different `doc_type`, or upload a clearer scan. |

<a id="per-field-vs-document-level"></a>

## Per-field vs document-level

DAN AI reports confidence at **two levels**:

- **Per field** - under `confidence` in the response (e.g. `{ "invoice_number": 95, "total_amount": 97 }`). A field with no entry was extracted with high confidence and the score was suppressed.
- **Document-level** - the overall classifier confidence shown next to the document type (e.g. *invoice · 95%*). This is how sure DAN AI is that the file is actually an invoice.

A document can have a high document-level score (classifier is sure it's an invoice) but a low confidence on individual fields (e.g. the date is hand-written and hard to read). The fix is different for each:

- Low **document-level** confidence → wrong `doc_type` for this file.
- Low **per-field** confidence → scan quality, ambiguous text, or a field the prompt doesn't handle well.

<a id="what-drives-a-low-score"></a>

## What drives a low score

In practice, low confidence usually traces back to one of these:

- **Scan quality** - low contrast, glare, skew, or low DPI. Re-scanning at higher contrast usually beats higher resolution.
- **Hand-written text** - DAN AI handles printed text reliably; handwriting is much harder.
- **Unusual layout** - e.g. an invoice with the total at the top instead of the bottom. Consider an account-wide custom prompt - see [Custom Fields and Templates](custom-fields.md).
- **Wrong document type** - the prompt doesn't know what to look for. Switch types and re-extract.
- **Field not present** - if the AI returns a value but the source file doesn't actually contain that field, the score will usually be low. Consider restricting the extraction to fields you know are present.

<a id="confidence-and-verification"></a>

## Confidence and verification

When a human edits a field and marks the document **verified**, the verified values are what flow into exports and webhook payloads - regardless of confidence score. The original AI response is still preserved in `document_extractions.raw_response` so you can audit edits later.

This means confidence scores guide **review effort before verification**, not what gets exported after.

<a id="using-scores-in-automation"></a>

## Using scores in automation

Two common patterns:

**Pattern 1 - auto-approve high confidence, queue the rest.**
Configure your webhook handler to auto-process documents where every field's confidence is ≥ 90, and create a review task for anything below.

**Pattern 2 - gate by specific fields.**
For invoices, you usually care most about `total_amount` and `invoice_number`. Auto-approve if those two are ≥ 95, regardless of what the others scored.

<a id="where-to-find-scores"></a>

## Where to find scores

| Place | What you see |
| --- | --- |
| Dashboard, document detail page | Document-level type confidence next to the type badge, plus per-field scores beside any uncertain field. |
| REST API response (`/extract`, `/documents/:id`) | `confidence` block keyed by field name; `meta.accuracy_percent` for the document-level score. |
| Webhook payload | Same shape as the API response - `confidence` per field. |
| Excel export | A `_confidence` column appears next to each field column in the top-level sheet. |

<a id="improving-scores-over-time"></a>

## Improving scores over time

If you consistently see low scores on a particular vendor's documents, the most reliable fixes (in order of effort):

1. **Re-scan or re-render the source PDF at higher contrast.** Fastest, no engineering work.
2. **Switch to a more specific `doc_type`.** If you've been using `general`, try `invoice` or `purchase_order`.
3. **Restrict extraction to a custom field list.** Asks the AI to focus only on what you need - see [Custom Fields and Templates](custom-fields.md).
4. **Add an account-wide custom prompt** for that document type. Most invasive but most powerful - best for non-standard layouts you receive often.

---

Source: [DAN AI - Confidence Scores and Accuracy](https://docs.sdlccorp.com/docs/dan-ai/features/confidence-scores/)
