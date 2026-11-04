# DAN AI - Document Extraction Platform

**DAN AI** turns every uploaded file into a *document* - a single record holding the original file, the structured fields the AI extracted from it, a confidence score, the AI provider metadata used, and a full audit trail. Try the live product at **[dan.sdlccorp.com](https://dan.sdlccorp.com)**.

Running the AI pipeline over a file to pull out structured fields is called an **extraction**. This documentation explains every way to start an extraction in DAN AI, what happens at each step, and how to get the data back out.

<a id="what-dan-ai-does"></a>

## What DAN AI does

- Accepts PDFs, PNGs and JPGs and converts them into structured JSON.
- Classifies the document into one of **21 supported types** (or `general` as a fallback) so the right prompt is used.
- Runs the file through a **multi-provider AI pipeline** - Ollama (primary) → OpenRouter → Groq - with automatic fallback when a provider is unavailable.
- Stamps each extraction with a per-field **confidence score** so reviewers know what to spot-check.
- Exports completed documents as **JSON** or **Excel** and pushes **webhook** events on completion.

<a id="document-lifecycle"></a>

## Document lifecycle

Every document, no matter how it was created, moves through the same states:

```
draft → processing → done   (or → error)
```

Once a document reaches `done`, you can review the extracted fields, edit anything the AI got wrong, mark the document as **verified**, and export it.

<a id="three-ways-to-start-an-extraction"></a>

## Three ways to start an extraction

| Method | Best for |
| --- | --- |
| **Dashboard upload** | Operations staff processing files one at a time through the browser. |
| **Email inbox sync** (Gmail / Outlook) | Recurring invoice or receipt mail from known senders, picked up on a schedule. |
| **REST API** | Developers integrating DAN AI into their own apps. |

See [Creating an Extraction](../../creating-an-extraction/current/extraction/dashboard-upload.md) for full walkthroughs of each path.

<a id="key-capabilities"></a>

## Key capabilities

- **21 tuned document types** across finance, legal, logistics, people & ID, health, and general categories - see the [Supported Document Types](../../features/current/features/document-types.md) reference.
- **Custom field selection** so you can extract only the fields you care about, per-document or account-wide.
- **Account-wide custom prompts** (admin only) for non-standard layouts.
- **AES-256-GCM encryption** of OAuth refresh tokens at rest.
- **Two export formats**: JSON and Excel (`.xlsx`) with a line-items sheet for invoices, receipts, bank statements and medical reports.
- **Webhooks** with signed payloads for every `extraction.completed` event.

<a id="quick-start"></a>

## Quick start

1. **Sign up** at [dan.sdlccorp.com](https://dan.sdlccorp.com) and confirm your account.
2. Open **Documents → New Extraction** and drop a sample PDF (an invoice works well).
3. Pick the matching **document type**, optionally tick a subset of fields, and click **Extract**.
4. When the document reaches `done`, review the extracted fields in the two-column detail view, edit anything that's wrong, and click **Export → JSON** or **Export → Excel**.
5. Once you're comfortable, connect a **Gmail/Outlook inbox** or generate an **API key** to automate the same flow.

Full setup steps are on the [Getting Started](../../getting-started/current/getting-started/setup.md) page.

<a id="whats-in-this-documentation"></a>

## What's in this documentation

- [**Getting Started**](../../getting-started/current/getting-started/setup.md) - sign up, tour the dashboard, pick an ingestion path.
- **Creating an Extraction** - full walkthroughs of [Dashboard Upload](../../creating-an-extraction/current/extraction/dashboard-upload.md), [Email Inbox Sync](../../creating-an-extraction/current/extraction/inbox-sync.md), and the [REST API](../../creating-an-extraction/current/extraction/rest-api.md).
- **Features** - [Document Types](../../features/current/features/document-types.md), [Confidence Scores](../../features/current/features/confidence-scores.md), [Custom Fields and Templates](../../features/current/features/custom-fields.md).
- **Export & Delivery** - [JSON and Excel Exports](../../export-delivery/current/export/formats.md) and [Webhooks](../../export-delivery/current/export/webhooks.md).
- **Reference** - [FAQ and Troubleshooting](../../reference/current/reference/faq.md).

---

Source: [DAN AI - Document Extraction Platform](https://docs.sdlccorp.com/docs/dan-ai/intro/)
