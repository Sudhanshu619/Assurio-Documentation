# DAN AI - Email Inbox Sync (Gmail / Outlook)

Once a user connects a mailbox from **Inboxes → Connect Gmail** or **Connect Outlook**, DAN AI polls it on a schedule and creates documents automatically from matching attachments.

<a id="1-connect-a-mailbox"></a>

## 1. Connect a mailbox

From the sidebar, open **Inboxes**, then click **Connect Gmail** or **Connect Outlook**.

The flow:

1. You're redirected to the provider's OAuth consent screen (Google or Microsoft).
2. Grant **read-only** mail access:
   - Gmail scope: `gmail.readonly`
   - Outlook scope: `Mail.Read`
3. You're bounced back to `/app/inboxes?status=success`.

The refresh token returned by the provider is stored **encrypted at rest** using AES-256-GCM. DAN AI never sees or stores your mail password - only the refresh token, which you can revoke at any time from your Google/Microsoft account settings.

Read-only access

DAN AI only requests read scopes. It cannot reply to, delete or move your email. If your organization restricts third-party OAuth apps, ask an admin to allow `dan.sdlccorp.com` first.

<a id="2-write-rules"></a>

## 2. Write rules

By default, **every PDF / image attachment** becomes a document. The rule engine lets you narrow that down using conditions on sender, subject, attachment name, attachment type, date, or label.

Open **Inboxes → Manage Rules** for the connected mailbox.

<a id="available-conditions"></a>

### Available conditions

| Condition field | Example operators | Example value |
| --- | --- | --- |
| `from` | equals, contains, domain_equals | `billing@vendor.com` |
| `subject` | contains, starts_with, regex | `Invoice` |
| `attachment_name` | matches, ends_with | `*.pdf` |
| `attachment_type` | equals | `pdf`, `xlsx`, `image` |
| `received_date` | after, before | `2026-01-01` |
| `label` | equals (Gmail labels / Outlook categories) | `Finance/Invoices` |

Conditions inside a single rule are AND-ed. To OR conditions, create separate rules.

<a id="available-actions"></a>

### Available actions

Each rule attaches one or more **actions**:

- `extract_doc` - create a document from this attachment.
- `skip` - ignore this message entirely.
- `tag` - create the document with a custom `rule_tag` for filtering later.

<a id="rule-priority-and-stop-processing"></a>

### Rule priority and stop processing

Rules within a ruleset run in priority order (lowest priority number first). When a rule with `stop_processing = true` matches, later rules are skipped for that message - useful when you want a specific sender rule to short-circuit a more general catch-all rule below it.

<a id="a-typical-ruleset"></a>

### A typical ruleset

```
1.  from contains "billing@" AND attachment_type = pdf
    → extract_doc with tag = "vendor-invoices"
    → stop_processing = true

2.  subject contains "Receipt" AND attachment_type = pdf
    → extract_doc with tag = "receipts"

3.  attachment_type = pdf
    → extract_doc
```

Mail that matches rule 1 is tagged as a vendor invoice and rule 2 and 3 are skipped. Anything else with a PDF attachment falls through to rule 3 and is extracted untagged.

<a id="3-sync-schedule"></a>

## 3. Sync schedule

DAN AI polls each connected inbox on a regular interval (default: every 15 minutes). Mail received between polls is picked up on the next run.

If you need an immediate sync - for example, while testing a new rule - click **Sync Now** on the inbox row to run the sync inline.

<a id="4-monitor-sync-status"></a>

## 4. Monitor sync status

The **Inboxes** page shows each connected account with:

- **Last sync time** - when the inbox was last polled.
- **Sync count** - how many messages were processed in the last run.
- **Documents created** - how many extractions resulted.
- **Last error** (if any) - the most recent failure, with a short reason.

Common reasons a sync stops working:

- The OAuth refresh token expired or was revoked → reconnect the mailbox.
- The provider rate-limited DAN AI → wait for the next interval, no action needed.
- A rule's regex is invalid → fix it under **Manage Rules**.

<a id="dry-running-rules"></a>

## Dry-running rules

Before pushing a ruleset live, open **Manage Rules → Dry Run** and paste a sample email subject + sender. DAN AI shows you which rules would match and what actions would fire - no documents are created. Use this to debug a ruleset that isn't picking up the mail you expected.

<a id="next-steps"></a>

## Next steps

- See exactly what gets created: [Dashboard Upload](dashboard-upload.md) walks through the document detail page that inbox-sync documents land on.
- Receive notifications when these auto-created documents finish: [Webhooks](../../../export-delivery/current/export/webhooks.md).
- Troubleshoot a non-syncing inbox: [FAQ and Troubleshooting](../../../reference/current/reference/faq.md).

---

Source: [DAN AI - Email Inbox Sync (Gmail / Outlook)](https://docs.sdlccorp.com/docs/dan-ai/extraction/inbox-sync/)
