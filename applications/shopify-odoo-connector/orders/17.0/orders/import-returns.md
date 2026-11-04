# Import Returns


<a id="why-import-returns"></a>

## Why import returns

Without importing returns, an Odoo warehouse would never know that a customer sent items back through Shopify. Stock would stay marked as "out", and refunds posted in Shopify wouldn't have a matching credit note in Odoo. Importing returns closes the loop: the warehouse can put items back into stock, finance can match the credit note, and reports stay accurate.

<a id="overview"></a>

## Overview

When a customer returns items in Shopify, the connector pulls the return into Odoo as an incoming transfer. The transfer carries the right product, the right quantity, and a link back to the original sale order so refunds and restocks stay consistent across both systems.

Import product returns from Shopify into Odoo as return transfers.

<a id="steps"></a>

## Steps

1. Navigate to **Shopify → Orders → Import Returns**
2. Select your **Shopify Instance**
3. Set the date range
4. Click **Import**

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

<a id="related"></a>

## Related

- [Refunds](refund.md) - pair returns with the matching credit note flow.
- [Sync Reports](../../../reports/17.0/reports/sales-report.md) - audit imported returns alongside the orders that produced them.
- [Webhooks](../../../configuration/17.0/configuration/webhook-configuration.md) - push returns into Odoo the second Shopify records them.

<a id="what-happens-in-odoo"></a>

## What happens in Odoo

Each imported Shopify return creates a confirmed incoming transfer with the right products, quantities and a back-reference to the original sale order. From there your warehouse team can validate the receipt, optionally do a quality check, and put the items back into stock.

---

Source: [Import Returns](https://docs.sdlccorp.com/docs/17.0/shopify-odoo-connector/orders/import-returns/)
