# Import Unshipped Orders


<a id="bulk-catch-up-only"></a>

## Bulk catch-up only

Scheduled order import handles new unshipped orders automatically every few minutes. This manual action is for **bulk catch-up** - onboarding your existing open backlog the first time you connect Shopify, or recovering after a sync outage that lasted longer than your usual schedule.

<a id="overview"></a>

## Overview

This action pulls every Shopify order that hasn't yet been fully fulfilled - paid-but-not-shipped, unpaid, on-hold, partially shipped - into Odoo as confirmed sale orders. Use it to onboard your existing open backlog the first time you connect Shopify, or to recover after a sync outage.

For day-to-day, scheduled order import handles new orders automatically. This manual action is for bulk catch-up.

Import all open, unpaid or unshipped orders from Shopify.

<a id="steps"></a>

## Steps

1. Navigate to **Shopify → Shopify Data → Orders**

![Shopify Data menu showing Orders option](https://docs.sdlccorp.com/assets/images/shopify-orders-1-cdc55176e4ba6ae49aed0367c169f731.webp)

2. The orders list view displays all synced Shopify orders.

![Shopify Orders list view](https://docs.sdlccorp.com/assets/images/shopify-orders-2-d29ca1b1c054c57a6c03f420bda216a3.webp)

3. Select your **Shopify Instance**
4. Set the **From Date** (or leave empty for all)
5. Click **Import**

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

<a id="related"></a>

## Related

- [Auto-Scheduler](../../../operations/19.0/operations/auto-scheduler.md) - scheduled order import handles new orders going forward.
- [Order Configuration](../../../configuration/19.0/configuration/order-configuration.md) - set filters, status mapping and customer behaviour.
- [Auto-Workflow](../../../configuration/19.0/configuration/auto-workflow.md) - automate post-import processing (confirm, invoice, validate).

---

Source: [Import Unshipped Orders](https://docs.sdlccorp.com/docs/19.0/shopify-odoo-connector/orders/import-unshipped-orders/)
