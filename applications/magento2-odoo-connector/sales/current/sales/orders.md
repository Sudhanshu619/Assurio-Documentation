# Magento 2 Connector - Order Management

The Magento 2 Connector supports full bidirectional order management. You can pull orders from Magento into Odoo for fulfillment, or create orders in Odoo and push them to Magento.

<a id="accessing-magento-orders"></a>

## Accessing Magento Orders

Navigate to **Magento > Sales > Orders** to view all synced orders.

![Sales menu showing order options](https://docs.sdlccorp.com/assets/images/s-order-1-f25747e4a203f9e24c14d75b6f0af007.webp)

<a id="order-list-view"></a>

## Order List View

The order list displays all synchronized orders with key details:

![Magento Orders list view](https://docs.sdlccorp.com/assets/images/s-order-11-6401d34354bea71017d84fab362d7620.webp)

| Column | Description |
| --- | --- |
| **Number** | Odoo sale order reference (e.g., `S00111`) |
| **Magento** | Magento order increment ID |
| **Magento ID** | Magento internal order ID (e.g., `0000000008`) |
| **Magento Status** | Order status in Magento (processing, closed, etc.) |
| **Magento Invoice** | Invoice status (Invoiced, Not Invoiced) |
| **Magento Amount** | Order total amount in Magento |
| **Magento Paid** | Payment status (Paid, Not Paid) |
| **Delivery Status** | Delivery status (Not Delivered, Started, Delivered) |
| **Magento Instance** | The Magento instance this order belongs to |
| **Order Date** | Date and time the order was placed |

<a id="order-form"></a>

## Order Form

Click on an order or click **New** to view the full order form:

![Magento Order form view](https://docs.sdlccorp.com/assets/images/s-order-111-2251a80de33c7c0bfa5372b4f99eab40.webp)

The order form includes:

- **Customer** -- The linked Odoo customer/partner
- **Quotation Template** -- Optional quotation template
- **Quotation Date** -- Date of the quotation
- **Expiration** -- Order expiration date
- **Payment Terms** -- Payment terms (e.g., Immediate)
- **Order Lines** -- Products, quantities, unit prices, taxes, and amounts
- **Optional Products** / **Other Info** / **Customer Signature** tabs

<a id="order-action-buttons"></a>

## Order Action Buttons

| Button | Description |
| --- | --- |
| **Send by Email** | Email the order/quotation to the customer |
| **Confirm** | Confirm the quotation as a sale order |
| **Preview** | Preview the order in the portal |
| **Create in Magento** | Push this order to Magento |
| **Pull from Magento** | Import this order's latest data from Magento |
| **Update in Magento** | Push order updates to Magento |

<a id="pull-workflow-magento-to-odoo"></a>

## Pull Workflow (Magento to Odoo)

When pulling orders from Magento, the connector follows this workflow:

1. **Fetch Orders** -- The connector queries the Magento REST API for new or updated orders.
2. **Resolve Customer** -- The customer is matched to an existing Odoo partner (by email) or a new partner is created.
3. **Resolve Products** -- Each order line item is matched to an Odoo product (by SKU or Magento product ID).
4. **Create Sale Order** -- A new sale order is created in Odoo with all line items, quantities, and prices.
5. **Register Payment** -- If the order is paid in Magento and auto-payment registration is enabled, a payment is recorded.
6. **Update Status** -- The Magento order status, invoice status, and payment status are stored on the Odoo record.

info

Orders are matched by Magento Order ID to prevent duplicates. If an order already exists in Odoo, it is updated rather than recreated.

<a id="push-workflow-odoo-to-magento"></a>

## Push Workflow (Odoo to Magento)

When pushing orders from Odoo to Magento:

1. **Create Quotation** -- Create a new sale order in Odoo with the desired products and customer.
2. **Select Instance** -- Ensure the order is associated with a Magento instance.
3. **Add Products** -- Add order line items with products that are mapped to Magento products.
4. **Confirm Order** -- Confirm the quotation to convert it to a sale order.
5. **Push to Magento** -- Click **Create in Magento** to push the order to your Magento store.

tip

For push operations, ensure the products and customer already exist in Magento (or have been synced). The connector uses the Magento product ID and customer ID to create the order.

<a id="order-status-mapping"></a>

## Order Status Mapping

| Magento Status | Odoo Equivalent |
| --- | --- |
| `pending` | Quotation |
| `processing` | Sale Order (confirmed) |
| `complete` | Sale Order (delivered) |
| `closed` | Sale Order (closed/refunded) |
| `canceled` | Cancelled |
| `holded` | On Hold |

<a id="next-steps"></a>

## Next Steps

- [Manage Invoices & Shipments](invoices-shipments.md)
- [Track Deliveries](delivered.md)
- [View Sync Reports](../../../reference/current/reference/sync-reports.md)

---

Source: [Magento 2 Connector - Order Management](https://docs.sdlccorp.com/docs/magento2-odoo-connector/sales/orders/)
