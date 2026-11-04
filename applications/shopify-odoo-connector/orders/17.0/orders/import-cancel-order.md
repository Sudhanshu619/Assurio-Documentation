# Import Cancel Orders


<a id="why-this-matters"></a>

## Why this matters

When a Shopify order is cancelled - by the customer, by the merchant, or by Shopify's automated fraud filter - the matching Odoo sale order needs to follow suit. Otherwise it sits "open" forever, distorting sales reports, confusing the fulfilment team, and (if invoicing is configured) potentially generating an invoice for a transaction that never happened.

This sync is one-way: cancellations from Shopify land in Odoo. To cancel from the Odoo side and push it to Shopify, use [Cancel Shopify Order](cancel-order-shopify.md).

<a id="overview"></a>

## Overview

If a customer cancels an order in Shopify (or the Shopify Fraud Filter cancels one for you), this action mirrors that cancellation in Odoo. Without it, the order stays "open" in Odoo's sales pipeline forever, distorting reports and confusing fulfilment.

Sync cancelled orders from Shopify to Odoo.

<a id="steps"></a>

## Steps

1. Navigate to **Shopify → Orders → Import Cancel Orders**
2. Select your **Shopify Instance**
3. Click **Import**

You can view cancelled order reports by navigating to **Shopify → Reports → Cancelled Orders**.

![Reports menu showing Cancelled Orders option](https://docs.sdlccorp.com/assets/images/shopify-report.cancel-order.re-1-dbb0e5ef844ec3e6b306638f3bb32f3f.webp)

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

<a id="related"></a>

## Related

- [Cancel Shopify Order](cancel-order-shopify.md) - the opposite direction (Odoo → Shopify).
- [Auto-Scheduler](../../../operations/17.0/operations/auto-scheduler.md) - keep cancellation sync running on a schedule.
- [Webhooks](../../../configuration/17.0/configuration/webhook-configuration.md) - push cancellations in real-time instead of polling.

---

Source: [Import Cancel Orders](https://docs.sdlccorp.com/docs/17.0/shopify-odoo-connector/orders/import-cancel-order/)
