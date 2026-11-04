# Alerts, Reorder Suggestions & Vendor Scorecard


<a id="reorder-suggestions"></a>

## Reorder Suggestions

Go to **Inventory Analytics > Reports > Reorder Suggestions**:

![Reorder Suggestions](https://docs.sdlccorp.com/assets/images/31-reorder-suggestions-a0dd456d23dcf357a4f8ea230ac4b2d6.webp)

The system auto-calculates for every product:

| Field | Formula |
| --- | --- |
| **Avg Daily Sales** | Total sold / days in period |
| **Days of Stock** | Current stock / avg daily sales |
| **Safety Stock** | Avg daily x lead time x 1.5 |
| **Reorder Point** | (Avg daily x lead time) + safety stock |
| **Suggested Qty** | (30 days demand + safety stock) - current stock |

<a id="urgency-levels"></a>

### Urgency Levels

| Urgency | Condition | Color |
| --- | --- | --- |
| **Critical: Order Now** | Zero stock or days left under lead time | Red |
| **Order Soon** | Days left under 2x lead time | Orange |
| **Adequate Stock** | Normal stock levels | Green |
| **Overstocked** | Days of stock > 90 | Gray |

<a id="create-rfq"></a>

### Create RFQ

Select products and click **Create RFQ from Selected** to generate draft purchase orders:

![Create RFQ](https://docs.sdlccorp.com/assets/images/32-reorder-create-rfq-cfe3988563b2f0b71db96f8598e47147.webp)

- Groups products by preferred vendor
- Creates one PO per vendor
- Pre-fills quantity, price, and planned delivery date
- Opens the created PO for review

<a id="vendor-scorecard"></a>

## Vendor Scorecard

Go to **Inventory Analytics > Reports > Vendor Scorecard**:

![Vendor Scorecard](https://docs.sdlccorp.com/assets/images/33-vendor-scorecard-fc7df5820868a9de7b83c67d923faf03.webp)

<a id="scoring-methodology"></a>

### Scoring Methodology

| Metric | Weight | Description |
| --- | --- | --- |
| **On-Time Delivery %** | 35% | Percentage of lines delivered within 7 days |
| **Quality Score** | 25% | 100 minus return rate |
| **Price Competitiveness** | 20% | Lower avg price = higher score |
| **Lead Time Score** | 20% | Faster delivery = higher score |

Grades: A (85+), B (70-84), C (55-69), D (40-54), F (under 40). Color-coded: Green (A/B), Yellow (C), Red (D/F).

<a id="alert-configuration"></a>

## Alert Configuration

Go to **Inventory Analytics > Configuration > Alerts**:

![Alerts List](https://docs.sdlccorp.com/assets/images/34-alerts-list-abea8399ffa3cb3631dd49920da84dc2.webp)

<a id="creating-an-alert"></a>

### Creating an Alert

Click **New** to create an alert rule:

![Alert Form](https://docs.sdlccorp.com/assets/images/35-alert-form-057fc3513aed20f9de4090f07ccd2497.webp)

| Field | Description |
| --- | --- |
| **Name** | Human-readable alert name |
| **Alert Type** | What condition to check (see below) |
| **Threshold** | Numeric trigger value |
| **Notify Users** | Users who receive the notification |
| **Warehouses** | Limit to specific warehouses (empty = all) |

<a id="alert-types"></a>

### Alert Types

| Type | Triggers When |
| --- | --- |
| **Health Score Below Threshold** | Any product's health score below threshold |
| **Out of Stock Products** | Any product has zero stock |
| **Overstock Value Exceeds** | Any product's overstock value > threshold |
| **Low Turnover Products** | Any product's turnover ratio below threshold |
| **Stock Aging Beyond Days** | Any product's oldest stock > threshold days |

<a id="how-alerts-work"></a>

### How Alerts Work

- A **daily cron job** runs automatically
- Checks all active alert rules against a 90-day analysis
- Creates **mail activity (Todo)** for each configured user
- Includes product names and a link to the dashboard

tip

Start with these 5 alerts: Health below 40, Out of Stock, Overstock over 5000, Turnover below 1, Aging over 90 days.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Alerts, Reorder Suggestions & Vendor Scorecard](https://docs.sdlccorp.com/docs/17.0/inventory-analytics-pro/features/alerts-reorder/)
