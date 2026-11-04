# Pricing and Stock Sync

Bidirectional price and inventory synchronization between Amazon and Odoo with full support for FBA and FBM.

<a id="price-sync"></a>

## Price Sync

<a id="bidirectional-flow"></a>

### Bidirectional Flow

- **Odoo → Amazon:** Push prices from Odoo products to Amazon listings
- **Amazon → Odoo:** Pull Amazon prices into Odoo for reporting

<a id="supported-price-fields"></a>

### Supported Price Fields

| Field | Description |
| --- | --- |
| **Amazon Price** | Current selling price on Amazon |
| **Cost Price** | Cost of goods (COGS) |
| **MRP** | Maximum retail price |
| **Buy Box Price** | Current winning price for the listing |

<a id="bulk-price-updates"></a>

### Bulk Price Updates

Use the **Catalog > Import / Map Products** wizard with the **Update Prices** operation to bulk update prices from a CSV/Excel file.

<a id="scheduled-price-sync"></a>

### Scheduled Price Sync

| Scheduled Action | Interval |
| --- | --- |
| **Update Prices** | Every 4 hours |
| **Pull FBA Prices** | Every 6 hours |

<a id="stock-sync"></a>

## Stock Sync

<a id="bidirectional-flow-1"></a>

### Bidirectional Flow

- **Odoo → Amazon (FBM):** Export Odoo stock levels to Amazon for merchant-fulfilled listings
- **Amazon → Odoo (FBA):** Import Amazon FBA stock into Odoo warehouses

<a id="fba-live-stock-monitoring"></a>

### FBA Live Stock Monitoring

The connector tracks FBA inventory in real-time:

- Live stock reports update Odoo quantities every 4 hours
- Inventory adjustments create stock quant entries automatically
- Separate FBA warehouse recommended for clean tracking

<a id="scheduled-stock-sync"></a>

### Scheduled Stock Sync

| Scheduled Action | Interval | Purpose |
| --- | --- | --- |
| **Export Stock Levels** | 2 hours | FBM stock push to Amazon |
| **Pull FBA Stock Levels** | 4 hours | FBA stock pull from Amazon |

<a id="bulk-stock-updates"></a>

### Bulk Stock Updates

Use **Catalog > Import / Map Products** with the **Update Stock** operation for bulk inventory updates via CSV/Excel.

warning

Keep FBA and FBM warehouses separate in Odoo. Mixing the two can cause incorrect stock counts since FBA stock is managed by Amazon's fulfillment network, not your local warehouse.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Pricing and Stock Sync](https://docs.sdlccorp.com/docs/17.0/amazon-odoo-connector/features/pricing-stock/)
