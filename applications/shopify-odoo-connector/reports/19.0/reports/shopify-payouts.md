# Shopify Payouts


<a id="why-import-payouts"></a>

## Why import payouts

Shopify Payments aggregates many orders into a single deposit to your bank account, after subtracting fees, refunds and adjustments. The bank sees one number; your accountant needs the per-order breakdown to reconcile. Importing payouts brings that breakdown into Odoo so reconciliation is a single screen instead of a multi-tab spreadsheet exercise.

<a id="overview"></a>

## Overview

Shopify Payments aggregates many orders into a single payout to your bank account, after deducting fees, refunds and adjustments. Importing payouts brings that breakdown into Odoo so your accountant can reconcile bank deposits against the underlying Shopify activity without exporting CSVs from the Shopify admin.

Import Shopify Payments payout data into Odoo for reconciliation.

<a id="importing-payouts"></a>

## Importing Payouts

1. Navigate to **Shopify → Reports → Shopify Payouts**
2. Select your **Shopify Instance** (must use Shopify Payments)
3. Click **Import Payouts**

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

<a id="related"></a>

## Related

- [Net Profit Report](net-profit-report.md) - uses payout fee data for the per-order margin.
- [Payment Gateway Mapping](../../../configuration/19.0/configuration/payment-gateway.md) - make sure imported payouts post against the right journals.
- [Sales Report](sales-report.md) - payouts close out the loop the Sales report opens.

<a id="when-payouts-run"></a>

## When payouts run

Shopify Payments closes a payout cycle daily for stores on the standard schedule, and Shopify pushes the payout summary to the connector shortly after. You can also pull payouts manually from this screen at any time, useful when bringing in historical payouts during onboarding.

---

Source: [Shopify Payouts](https://docs.sdlccorp.com/docs/19.0/shopify-odoo-connector/reports/shopify-payouts/)
