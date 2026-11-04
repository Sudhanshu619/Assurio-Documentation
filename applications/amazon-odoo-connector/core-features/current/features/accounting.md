# Accounting and Settlements

Automated processing of Amazon settlement reports, reimbursements, and tax invoices for complete financial reconciliation.

<a id="settlement-reports"></a>

## Settlement Reports

Amazon settlement reports contain detailed breakdowns of payments, fees, refunds, and other financial transactions.

<a id="whats-processed"></a>

### What's Processed

- Order payments
- Amazon referral fees
- FBA fulfillment fees
- Shipping fees
- Refunds and chargebacks
- Promotional rebates
- Other marketplace transactions

<a id="auto-reconciliation"></a>

### Auto-Reconciliation

- Settlement lines automatically link to Odoo sale orders and invoices
- Easy matching by order ID, ASIN, and transaction date
- Variance reports flag unmatched transactions

<a id="scheduled-action"></a>

### Scheduled Action

| Scheduled Action | Interval |
| --- | --- |
| **Import Settlement Reports** | Daily |

<a id="reimbursements"></a>

## Reimbursements

Amazon issues reimbursements for lost inventory, damaged items, and customer refunds Amazon paid on your behalf.

- Auto-create reimbursement vendor bills in Odoo
- Linked to original Amazon transaction for audit trail
- Journal entries posted to configured reimbursement accounts

<a id="vcs-tax-invoices"></a>

## VCS Tax Invoices

The connector supports Amazon's **VAT Calculation Service (VCS)** for European marketplaces:

- Download VCS tax invoice reports
- Automatic tax invoice generation in Odoo
- Multi-country VAT handling (DE, FR, IT, ES, UK, etc.)

<a id="invoice-upload-to-amazon"></a>

## Invoice Upload to Amazon

For marketplaces requiring invoice upload (India, UAE, etc.):

1. Generate the invoice in Odoo (Sales > Invoices)
2. Click **Upload to Amazon** on the invoice
3. The connector sends the PDF via SP-API
4. Amazon attaches it to the customer's order

tip

Enable the **Import Settlement Reports** scheduled action to run daily. This keeps your Odoo accounting in sync with Amazon's payment cycle automatically.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Accounting and Settlements](https://docs.sdlccorp.com/docs/amazon-odoo-connector/features/accounting/)
