# DAN AI - Getting Started

This page walks you through creating a DAN AI account, the layout of the dashboard, and choosing the best path to start extracting documents.

<a id="sign-up-and-sign-in"></a>

## Sign up and sign in

1. Visit **[dan.sdlccorp.com](https://dan.sdlccorp.com)** and click **Sign Up**.
2. Use your work email and create a strong password, or sign in with Google.
3. Confirm your email if prompted, then sign in.

You land on the **Dashboard**, which is also where you'll spend most of your time during normal operation.

<a id="dashboard-tour"></a>

## Dashboard tour

The left sidebar contains the main sections you'll use:

| Section | What it does |
| --- | --- |
| **Dashboard** | KPIs and the most recent documents at a glance. |
| **Documents** | The full list of extractions, filterable by state, document type, source, sender, date and confidence. Also where you click **New Extraction**. |
| **Inboxes** | Connected Gmail and Outlook accounts, their rulesets, sync status and last-error info. |
| **Developer** | API keys, webhooks, and an activity log of recent API calls. |
| **Settings** | AI providers, default prompts, account-wide field defaults, and team management (admins only). |

<a id="pick-an-ingestion-path"></a>

## Pick an ingestion path

Decide how documents will flow into DAN AI. You can mix and match - many teams use the dashboard for ad-hoc work, inbox sync for recurring vendor mail, and the API for downstream automation.

| Method | Purpose | Best for |
| --- | --- | --- |
| **Dashboard upload** | Drop a single file from the browser through **New Extraction**, configure fields, and extract on demand. | Operations staff processing files one at a time. |
| **Email inbox sync** (Gmail / Outlook) | Auto-extract attachments from a connected mailbox on a schedule, with a rule engine for filtering. | Recurring invoice or receipt mail from known senders. |
| **REST API** | Send a file programmatically and receive structured JSON in return. Sync by default; queue an async job for long-running extractions. | Developers integrating DAN AI into their own apps. |

Continue with the walkthrough for the path you picked:

- [Dashboard Upload](../../../creating-an-extraction/current/extraction/dashboard-upload.md)
- [Email Inbox Sync](../../../creating-an-extraction/current/extraction/inbox-sync.md)
- [REST API](../../../creating-an-extraction/current/extraction/rest-api.md)

<a id="recommended-first-run"></a>

## Recommended first run

Even if you're going to automate, do **at least one dashboard upload first**. It's the fastest way to see how DAN AI behaves on your own files, which document type fits best, and what confidence scores you can expect - knowledge you'll need before you wire up an inbox rule or write API client code.

<a id="account-wide-settings-worth-setting-early"></a>

## Account-wide settings worth setting early

These live under **Settings** and are admin-only. Configuring them once saves time across every future extraction:

- **AI provider chain** - pick the primary provider (Ollama is the default) and the fallback order.
- **Default fields per document type** - if you always want the same 5 fields from invoices, set them here so every extraction returns just those.
- **Custom prompts** - override the built-in prompt for any document type. Useful when your invoices have non-standard headings or tax columns.

<a id="next-steps"></a>

## Next steps

Pick your ingestion method and follow the corresponding walkthrough, or read the [Supported Document Types](../../../features/current/features/document-types.md) reference to see what DAN AI ships with out of the box.

---

Source: [DAN AI - Getting Started](https://docs.sdlccorp.com/docs/dan-ai/getting-started/setup/)
