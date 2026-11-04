# DAN AI - Supported Document Types

DAN AI ships **21 tuned document types** organized into 6 categories. The type you pick drives which prompt is sent to the AI provider, so matching the right type significantly improves extraction accuracy.

If you pass an unknown type or omit it entirely, DAN AI falls back to `general` - a universal prompt that returns whatever structured key/value pairs it can recognize.

<a id="finance"></a>

## Finance

| Type | What it's tuned for | Has line items? |
| --- | --- | --- |
| `invoice` | Vendor invoices: vendor & buyer, invoice number, dates, currency, line items, subtotal/tax/total. | Yes |
| `receipt` | Printed retail / restaurant receipts: merchant, date, item lines, tax, payment method. | Yes |
| `purchase_order` | Buyer-issued POs: PO number, supplier, ship-to, item lines, terms. | Yes |
| `expense` | Reimbursable expenses: claimant, category, date, amount, currency, project code. | No |
| `bank_statement` | Multi-page bank statements: account holder, period, opening/closing balance, transaction rows. | Yes |
| `payslip` | Employee payslips: employee, pay period, gross/net pay, deductions, employer details. | Yes |
| `tax_form` | Tax filings & related forms: jurisdiction, form number, taxpayer, totals. | Sometimes |
| `quote` | Sales quotes / estimates: quoter, quote number, validity, item lines, totals. | Yes |

<a id="legal"></a>

## Legal

| Type | What it's tuned for | Has line items? |
| --- | --- | --- |
| `contract` | Multi-party contracts: parties, effective date, term, renewal, payment terms, governing law. | No |
| `nda` | Non-disclosure agreements: parties, effective date, scope, duration, exceptions. | No |
| `insurance_policy` | Insurance policies: policyholder, insurer, policy number, coverage limits, premium. | No |
| `certificate` | Certificates of various kinds: issuer, holder, certificate number, issue & expiry dates. | No |

<a id="logistics"></a>

## Logistics

| Type | What it's tuned for | Has line items? |
| --- | --- | --- |
| `delivery_note` | Shipping / delivery notes: sender, recipient, tracking number, item lines. | Yes |
| `shipping_label` | Carrier labels: carrier, service, tracking number, weight, dimensions, addresses. | No |

<a id="people--id"></a>

## People & ID

| Type | What it's tuned for | Has line items? |
| --- | --- | --- |
| `resume` | Candidate resumes: contact info, education, experience, skills, certifications. | No (uses arrays) |
| `id_card` | Government IDs (passport, driver's licence, national ID): name, DOB, ID number, expiry. | No |

<a id="health"></a>

## Health

| Type | What it's tuned for | Has line items? |
| --- | --- | --- |
| `medical_report` | Diagnostic lab reports: patient, test date, panel name, lab rows with reference intervals. | Yes |
| `prescription` | Prescriptions: prescriber, patient, drug list with dosage, refills, date. | Yes |

<a id="general"></a>

## General

| Type | What it's tuned for | Has line items? |
| --- | --- | --- |
| `general` | Universal prompt - best when nothing else fits. Output schema varies by document content. | Sometimes |
| `letter` | Business / personal letters: sender, recipient, date, subject, body summary. | No |
| `memo` | Internal memos: from, to, date, subject, body summary. | No |

<a id="choosing-the-right-type"></a>

## Choosing the right type

A few rules of thumb:

- **Always prefer a specific type over `general`.** Even if you have to spread mixed documents across multiple types, you'll get better accuracy than throwing everything into the universal prompt.
- **Use `general` for unknown shapes.** It's also a useful diagnostic - when a specific type returns poor results, switching to `general` for one extraction reveals what the AI actually "sees" in the file.
- **Receipts vs invoices** - pick `receipt` for short printed thermal receipts and `invoice` for any A4-style document with a "Total Due" block, even if the seller calls it a receipt.
- **Bank statements** - multi-page statements work, but very long statements (50+ pages) may be truncated. If you can split them up by month before uploading, you'll get cleaner output.

<a id="adding-a-custom-prompt-for-a-type"></a>

## Adding a custom prompt for a type

If your documents have a non-standard layout (e.g. invoices from a vendor that buries the total in the footer), you can override the built-in prompt for that document type. See [Custom Fields and Templates](custom-fields.md).

<a id="using-the-type-through-each-ingestion-path"></a>

## Using the type through each ingestion path

The `doc_type` value works the same everywhere it appears:

- **Dashboard upload** - picked from the type dropdown in the upload modal.
- **Inbox sync** - set per ruleset under **Inboxes → Manage Rules**. Apply different types to different senders.
- **REST API** - passed as the `doc_type` field in the multipart request. See [REST API](../../../creating-an-extraction/current/extraction/rest-api.md).

---

Source: [DAN AI - Supported Document Types](https://docs.sdlccorp.com/docs/dan-ai/features/document-types/)
