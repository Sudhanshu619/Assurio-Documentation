# Export Stock to Shopify


<a id="manual-vs-automatic-export"></a>

## Manual vs automatic export

- **Manual** - one click from the connector menu, pushes immediately. Use for bulk catch-up after restocks or after a sync outage.
- **Automatic** - runs on a configurable cron. Use for steady-state production. Configure the cadence under [Auto-Scheduler](../../../operations/current/operations/auto-scheduler.md).

<a id="overview"></a>

## Overview

Exporting stock pushes Odoo's current inventory back to Shopify so customers see the right "in stock" numbers. Use this when Odoo is your source of truth for stock and Shopify needs to follow.

<a id="manual-vs-automatic"></a>

### Manual vs. automatic

- **Manual** - one click from the connector menu, pushes immediately. Use for bulk catch-up.
- **Automatic** - runs on a cron schedule (configurable). Use for steady-state production.

Push current Odoo inventory levels to Shopify.

<a id="manual-export"></a>

## Manual Export

You can view inventory status from the **Shopify → Inventory** menu.

![Shopify Inventory Report with Refresh Inventory button](https://docs.sdlccorp.com/assets/images/shopify-inventory-433a2fb3cdf15554a44b61a9c2866d6a.webp)

1. Navigate to **Shopify → Products → Export Stock**
2. Select your **Shopify Instance**
3. Select the **Warehouse** or **Location**
4. Click **Export**

<a id="automatic-export"></a>

## Automatic Export

Enable the **Export Stock Scheduler** in your cron settings for automatic periodic export.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

<a id="related"></a>

## Related

- [Import Stock](import-stock.md) - the opposite direction (Shopify → Odoo).
- [Stock Information](../../../configuration/current/configuration/stock-information.md) - pick which direction is the source of truth.
- [Auto-Scheduler](../../../operations/current/operations/auto-scheduler.md) - set the cadence for automatic stock exports.

---

Source: [Export Stock to Shopify](https://docs.sdlccorp.com/docs/shopify-odoo-connector/products/export-stock/)
