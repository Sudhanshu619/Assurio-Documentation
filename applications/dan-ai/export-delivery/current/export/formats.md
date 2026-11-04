# DAN AI - JSON and Excel Exports

A completed document can leave DAN AI in two file formats: **JSON** and **Excel**. Both are available from the dashboard (the **Export** dropdown on the document detail page) and via the API.

For receiving extractions as event callbacks instead of polling/exporting, see [Webhooks](webhooks.md).

<a id="json-export"></a>

## JSON export

JSON returns the structured fields exactly as the AI returned them, with human edits layered on top.

<a id="where-to-get-it"></a>

### Where to get it

- **Dashboard** - open a document, click **Export → JSON**. The file downloads as `<reference>.json`.
- **API** - `GET /api/external/v1/documents/:id` returns the same payload shape. There's also `GET /api/v1/documents/:id/export?format=json` for the dashboard-equivalent file response.

<a id="shape"></a>

### Shape

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

<a id="verified-vs-raw-values"></a>

### Verified vs raw values

By the time you export, `fields` contains whichever values are current - the original AI output if nobody touched it, or the human-edited values if someone fixed something and marked the document **verified**.

The original AI response is **not** included in the export payload to keep it small. If you need it (for audit or to compare against a custom-prompt change), query the `document_extractions.raw_response` column directly.

<a id="excel-export"></a>

## Excel export

Excel returns a `.xlsx` workbook with up to two sheets:

| Sheet | Contents |
| --- | --- |
| **Fields** | Every top-level field as a column. One row per document. A `_confidence` column appears next to each field that had a confidence score. |
| **Line Items** | One row per line item. Populated for `invoice`, `receipt`, `bank_statement` and `medical_report`. Omitted otherwise. |

<a id="where-to-get-it-1"></a>

### Where to get it

- **Dashboard** - open a document, click **Export → Excel**. The file downloads as `<reference>.xlsx`.
- **API** - `GET /api/v1/documents/:id/export?format=xlsx` returns the binary `.xlsx`.

<a id="when-the-line-items-sheet-is-empty"></a>

### When the line-items sheet is empty

Resumes, contracts, ID cards, shipping labels and other non-tabular types don't have line items - the **Line Items** sheet is omitted entirely. The export is still valid; only the **Fields** sheet is present.

<a id="exporting-multiple-documents"></a>

## Exporting multiple documents

The dashboard's **Documents** list supports bulk export: tick the documents you want, click **Export → JSON (zip)** or **Export → Excel (combined)**.

- The JSON zip contains one file per document.
- The Excel combined export merges all selected documents into a single workbook - each document is one row in the **Fields** sheet and its line items appended to the **Line Items** sheet (with a `document_id` / `reference` column for grouping).

For programmatic bulk export, iterate the documents list endpoint and pull each one individually.

<a id="choosing-a-format"></a>

## Choosing a format

| Use case | Best format |
| --- | --- |
| Importing into an ERP, accounting system, or your own database | **JSON** - preserves types, easy to parse. |
| Sharing with non-developers (accounting team, auditors) | **Excel** - opens in Excel/Numbers/Sheets without extra tooling. |
| Long-term archival alongside the original file | **JSON** - stable schema, smaller files. |
| Quick spot-check during a manual review | **Excel** - humans read tables faster than JSON. |

<a id="related"></a>

## Related

- [Webhooks](webhooks.md) - push completion events instead of polling.
- [REST API](../../../creating-an-extraction/current/extraction/rest-api.md) - full reference for the document/export endpoints.
- [Confidence Scores](../../../features/current/features/confidence-scores.md) - interpret the `_confidence` columns in the Excel export.

---

Source: [DAN AI - JSON and Excel Exports](https://docs.sdlccorp.com/docs/dan-ai/export/formats/)
