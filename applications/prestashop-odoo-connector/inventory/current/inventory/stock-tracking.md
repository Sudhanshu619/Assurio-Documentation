# PrestaShop Connector - Inventory Management


<a id="when-to-refresh-manually"></a>

## When to refresh manually

The auto-sync keeps PrestaShop stock and Odoo stock in step on a schedule. Use the manual refresh on this page when:

- A specific product looks wrong and you want to force-sync it before troubleshooting deeper.
- You've made a bulk stock change in one system and don't want to wait for the next scheduled run.
- You're debugging a discrepancy and want a clean before/after view to compare.

<a id="overview"></a>

## Overview

The Inventory section of the PrestaShop Odoo Connector is your live view of stock as PrestaShop reports it, alongside Odoo's own warehouse counts. Use it to spot drift early and trigger a refresh before mismatched counts cause oversells.
Navigate to **PrestaShop > Inventory**.

The inventory view shows all synced products with their stock status:

![Inventory View](https://docs.sdlccorp.com/assets/images/PrestaShop-inventory-8e9a4fa1feda70533b4c4aca6a82d108.webp)

<a id="stock-status"></a>

## Stock Status

| Status | Color | Description |
| --- | --- | --- |
| **In Stock** | Green | Quantity is above the low stock threshold |
| **Low Stock** | Orange | Quantity is at or below the threshold but greater than 0 |
| **Out of Stock** | Red | Quantity is zero |

<a id="actions"></a>

## Actions

- Use the **Refresh Inventory** button to re-sync stock quantities from PrestaShop
- **PDF reports** can be downloaded for in-stock and out-of-stock products

<a id="need-help"></a>

## Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/)

---

Source: [PrestaShop Connector - Inventory Management](https://docs.sdlccorp.com/docs/prestashop-odoo-connector/inventory/stock-tracking/)
