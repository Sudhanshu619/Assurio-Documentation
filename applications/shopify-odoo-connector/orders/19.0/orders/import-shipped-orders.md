# Import Shipped Orders


<a id="backfill-vs-new-order-flow"></a>

## Backfill vs new-order flow

This page is for the **backfill** use case - orders that have already shipped through some other channel (third-party fulfilment, the previous ERP, a manual process) and need to land in Odoo as historical records, not as work for the warehouse.

For new orders Odoo should actually ship, use [Import Unshipped Orders](import-unshipped-orders.md) instead.

<a id="overview"></a>

## Overview

This action imports Shopify orders that have **already been shipped** outside Odoo. It marks them as fulfilled on the way in, so Odoo doesn't try to ship them again. Use it for:

- **Backfilling historical orders** when you first install the connector.
- **Bringing in orders shipped via a third party** (drop-shipper, 3PL) that already updated Shopify directly.

If you want orders Odoo should ship, use [Import Unshipped Orders](import-unshipped-orders.md) instead.

Import already-fulfilled orders from Shopify.

<a id="steps"></a>

## Steps

1. Navigate to **Shopify → Orders → Import Shipped Orders**
2. Select your **Shopify Instance**
3. Set a **Date Range**
4. Click **Import**

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

<a id="related"></a>

## Related

- [Import Unshipped Orders](import-unshipped-orders.md) - for orders Odoo should ship.
- [Import Specific Order](import-specific-order.md) - re-sync just one order by ID.
- [Setup Connector](../../../installation/19.0/installation/setup-connector.md) - make sure your instance is configured before bulk backfilling.

---

Source: [Import Shipped Orders](https://docs.sdlccorp.com/docs/19.0/shopify-odoo-connector/orders/import-shipped-orders/)
