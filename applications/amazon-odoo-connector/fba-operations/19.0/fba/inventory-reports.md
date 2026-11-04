# FBA Inventory Reports

Three types of FBA reports automatically sync Amazon inventory data into Odoo.

<a id="report-types"></a>

## Report Types

<a id="1-fba-live-stock-report"></a>

### 1. FBA Live Stock Report

- **What it does:** Updates `amazon.product` quantities in real-time
- **Frequency:** Configurable (typically every 4 hours)
- **Use case:** Always know current FBA stock levels for sales decisions

<a id="2-inventory-adjustment-report"></a>

### 2. Inventory Adjustment Report

- **What it does:** Creates `stock.quant` entries in Odoo warehouse
- **Frequency:** On-demand or scheduled
- **Use case:** Track adjustments from Amazon (lost, found, damaged)

<a id="3-fba-shipment-report"></a>

### 3. FBA Shipment Report

- **What it does:** Updates order status to "Shipped" automatically
- **Frequency:** Hourly (via scheduled action)
- **Use case:** Keep FBA order statuses current without manual updates

<a id="returns--reports"></a>

## Returns & Reports

<a id="return-management"></a>

### Return Management

The connector handles FBA returns automatically:

- Download FBA return reports with order ID, SKU, ASIN, return reason, and status
- Auto-create credit notes (`account.move` reversal) linked to original invoices
- Track return quantities, fulfillment centers, and return dates

<a id="seller-ratings--feedback"></a>

### Seller Ratings & Feedback

- Download seller feedback reports from Amazon
- Auto-calculate average rating and total rating count
- View individual ratings (1–5 stars) with customer feedback text
- Respond to customer feedback directly from Odoo

<a id="accessing-reports"></a>

## Accessing Reports

Navigate to **Amazon > Reports** to view:

- **Sync Reports** - High-level summaries grouped by date and operation
- **Sync Logs** - Detailed request/response data for debugging
- **FBA Reports** - All FBA-specific report types
- **Settlement Reports** - Financial reconciliation data

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [FBA Inventory Reports](https://docs.sdlccorp.com/docs/19.0/amazon-odoo-connector/fba/inventory-reports/)
