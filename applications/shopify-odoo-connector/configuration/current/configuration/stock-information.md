# Stock & Location Configuration


<a id="why-stock-configuration-matters"></a>

## Why stock configuration matters

Shopify treats each store location (or "fulfilment location") as a separate inventory pool. Odoo treats stock as belonging to a warehouse. Without an explicit mapping, the connector defaults every Shopify location to your Odoo company's primary warehouse - which is fine for single-warehouse setups but causes silent stock drift for anyone with more than one location.

Spend a few minutes on this page before you run a full stock import; it's much harder to retrofit warehouse routing on hundreds of already-imported products.

Configure how inventory levels sync between Shopify locations and Odoo warehouses.

<a id="location-mapping"></a>

## Location Mapping

1. Go to **Shopify → Configuration → Location Mapping**
2. Click **Import Locations** to fetch all Shopify locations
3. For each Shopify location, select the corresponding **Odoo Location**
4. Save

<a id="stock-update-method"></a>

## Stock Update Method

| Method | Description |
| --- | --- |
| **On Hand Qty** | Syncs the current on-hand quantity |
| **Forecasted Qty** | Syncs the forecasted quantity |

<a id="inventory-sync-direction"></a>

## Inventory Sync Direction

| Direction | Description |
| --- | --- |
| **Odoo → Shopify** | Export stock from Odoo to Shopify |
| **Shopify → Odoo** | Import stock from Shopify to Odoo |
| **Bidirectional** | Real-time sync in both directions |

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

<a id="related"></a>

## Related

- [Export Stock](../../../products/current/products/export-stock.md) - push Odoo levels to Shopify.
- [Import Stock](../../../products/current/products/import-stock.md) - pull Shopify levels into Odoo.
- [Import Location](../../../operations/current/operations/import-location.md) - make sure stock routes to the right Odoo warehouse.

---

Source: [Stock & Location Configuration](https://docs.sdlccorp.com/docs/shopify-odoo-connector/configuration/stock-information/)
