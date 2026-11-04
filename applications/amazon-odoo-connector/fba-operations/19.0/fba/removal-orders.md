# Removal Orders

Request return-to-seller or disposal of FBA inventory directly from Odoo.

<a id="use-cases"></a>

## Use Cases

- Remove slow-moving inventory from Amazon warehouses
- Recall defective or recalled products
- Dispose of damaged or expired inventory
- Return excess stock to your own warehouse
- Avoid long-term storage fees

<a id="status-flow"></a>

## Status Flow

```
Draft → Submitted → Processing → Completed / Cancelled
```

| Status | Meaning |
| --- | --- |
| **Draft** | Being created in Odoo |
| **Submitted** | Sent to Amazon for processing |
| **Processing** | Amazon is preparing the removal |
| **Completed** | Inventory removed successfully |
| **Cancelled** | Removal cancelled (may still be charged) |

<a id="disposition-types"></a>

## Disposition Types

| Type | Meaning |
| --- | --- |
| **Sellable** | Return sellable inventory back to you |
| **Unsellable** | Dispose of damaged/defective inventory |

<a id="tracking"></a>

## Tracking

Each removal order tracks per-SKU:

- **Requested Qty** - What you asked Amazon to remove
- **Shipped Qty** - What Amazon actually shipped back
- **Cancelled Qty** - What Amazon cancelled due to availability

<a id="creating-a-removal-order"></a>

## Creating a Removal Order

1. Go to **FBA > Removal Orders** and click **New**
2. Select the Amazon fulfillment center
3. Choose disposition: **Sellable** (return to you) or **Unsellable** (dispose)
4. Add SKUs and quantities
5. Enter shipping address (for sellable returns)
6. Click **Submit** to send to Amazon

<a id="automated-import"></a>

## Automated Import

| Scheduled Action | Interval |
| --- | --- |
| **Import Removal Orders** | Daily |

This scheduled action pulls existing removal orders from Amazon (including those created directly in Seller Central) into Odoo for unified tracking.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Removal Orders](https://docs.sdlccorp.com/docs/19.0/amazon-odoo-connector/fba/removal-orders/)
