# Import Stock from Shopify


<a id="when-to-use-import-not-export"></a>

## When to use import (not export)

Use this action when **Shopify is your source of truth for stock** - for example, when you use a third-party fulfilment service that updates Shopify directly, and you want Odoo to mirror those counts.

If Odoo is your source of truth instead (you fulfil from Odoo warehouses), use [Export Stock](export-stock.md) and skip this page.

<a id="overview"></a>

## Overview

Importing stock pulls Shopify's current inventory into Odoo. Use this when Shopify is your source of truth for stock - for example, when you're using a third-party fulfilment service that updates Shopify directly and you want Odoo to reflect their counts.

If Odoo is your source of truth instead, use [Export Stock](export-stock.md) and skip this page.

Pull inventory levels from Shopify into Odoo.

<a id="manual-import"></a>

## Manual Import

1. Navigate to **Shopify → Inventory** to view the Inventory Report.

![Shopify Inventory Report with Refresh Inventory button](https://docs.sdlccorp.com/assets/images/shopify-inventory-433a2fb3cdf15554a44b61a9c2866d6a.webp)

2. Select your **Shopify Instance**
3. Select the **Location** to import from
4. Click **Import**

warning

Importing stock from Shopify will create inventory adjustments in Odoo. Ensure you
have the correct location mapping configured before running this operation.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Import Stock from Shopify](https://docs.sdlccorp.com/docs/17.0/shopify-odoo-connector/products/import-stock/)
