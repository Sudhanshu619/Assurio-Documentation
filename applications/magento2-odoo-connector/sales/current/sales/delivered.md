# Delivery Tracking

The Magento 2 Connector provides dedicated views for tracking order delivery status, allowing you to quickly identify delivered orders, pending deliveries, and cancelled orders.

---


<a id="delivered-orders"></a>

## Delivered Orders

<a id="accessing-delivered-orders"></a>

### Accessing Delivered Orders

Navigate to **Magento > Sales > Delivered Orders** to view all orders that have been fully delivered.

![Sales menu showing Delivered Orders option](https://docs.sdlccorp.com/assets/images/s-d-1-005dd1ce9a5d250ffb06971893f29f42.webp)

<a id="delivered-orders-list"></a>

### Delivered Orders List

![Delivered Orders list view](https://docs.sdlccorp.com/assets/images/s-d-11-c38aaa230f9a94dad27bee7ba8dd1d5c.webp)

The Delivered Orders view shows only orders where all items have been shipped and delivered. The list includes the following columns:

| Column | Description |
| --- | --- |
| **Order Reference** | Odoo sale order reference |
| **Order Date** | Date the order was placed |
| **Customer** | Customer name |
| **Magento Order ID** | Magento order increment ID |
| **Magento Instance** | The associated Magento instance |
| **Magento Status** | Current status in Magento |
| **Magento Invoice** | Invoice status |
| **Magento Paid** | Payment status |
| **Delivery Status** | Delivery status (Delivered) |

info

This view is automatically filtered to show only orders with a delivery status of "Delivered." You can use the search bar to further filter by date, customer, or instance.

---


<a id="not-delivered-orders"></a>

## Not Delivered Orders

<a id="accessing-not-delivered-orders"></a>

### Accessing Not Delivered Orders

Navigate to **Magento > Sales > Not Delivered Orders** to view orders that are pending delivery.

![Sales menu showing Not Delivered Orders option](https://docs.sdlccorp.com/assets/images/s-nd-1-a23b8a5e80a1e861695c92369802213f.webp)

<a id="not-delivered-orders-list"></a>

### Not Delivered Orders List

![Not Delivered Orders list view](https://docs.sdlccorp.com/assets/images/s-nd-11-ada5a1c35cc2f6c991e707ac1ef34dae.webp)

The Not Delivered Orders view shows orders that are awaiting shipment or have only been partially delivered:

| Column | Description |
| --- | --- |
| **Order Reference** | Odoo sale order reference (e.g., `S00125`, `S00123`) |
| **Order Date** | Date the order was placed |
| **Customer** | Customer name |
| **Magento Order ID** | Magento order increment ID |
| **Magento Status** | Current status in Magento (pending, processing, closed) |
| **Magento Instance** | The associated Magento instance |
| **Magento Invoice** | Invoice status (Invoiced, Not Invoiced) |
| **Magento Payment** | Payment amount |
| **Magento Paid** | Payment status (Paid, Not Paid) |
| **Delivery Status** | Delivery status (Not Delivered) |

tip

Use the Not Delivered Orders view as a daily checklist to identify orders that need to be fulfilled. Orders showing as "processing" in Magento with "Not Delivered" status are ready for shipment.

---


<a id="cancelled-orders"></a>

## Cancelled Orders

<a id="accessing-cancelled-orders"></a>

### Accessing Cancelled Orders

Navigate to **Magento > Reports > Cancelled Orders** to view orders that have been cancelled.

![Reports menu showing Cancelled Orders option](https://docs.sdlccorp.com/assets/images/s-cancel-order-1-3b09db58c86dd934f99bfaaf2796972e.webp)

<a id="cancelled-orders-list"></a>

### Cancelled Orders List

![Cancelled Orders list view](https://docs.sdlccorp.com/assets/images/s-cancel-order-11-30b02c098709747da5e1abaab9adb15e.webp)

The Cancelled Orders view provides a comprehensive list of all cancelled orders:

| Column | Description |
| --- | --- |
| **Order Reference** | Odoo sale order reference |
| **Order Date** | Date the order was originally placed |
| **Magento Order ID** | Magento order increment ID |
| **Magento Status** | Status in Magento (canceled) |
| **Magento Customer Email** | Customer email from the original order |
| **Magento Payment Status** | Payment status at time of cancellation |
| **Status** | Current Odoo order status |

warning

Cancelled orders in Magento are synced to Odoo automatically. However, if an order was already invoiced or partially shipped in Odoo, the cancellation must be handled manually to reconcile inventory and accounting.

<a id="delivery-status-flow"></a>

## Delivery Status Flow

The following diagram shows the typical order delivery lifecycle:

| Stage | Magento Status | Odoo Delivery Status |
| --- | --- | --- |
| Order placed | `pending` | Not Delivered |
| Payment received | `processing` | Not Delivered |
| Shipment created | `processing` | Started |
| Fully shipped | `complete` | Delivered |
| Order cancelled | `canceled` | N/A |
| Order refunded | `closed` | Varies |

<a id="next-steps"></a>

## Next Steps

- [View Invoices & Shipments](invoices-shipments.md)
- [Check Sync Reports](../../../reference/current/reference/sync-reports.md)
- [Manage Inventory](../../../advanced/current/advanced/inventory.md)

---

Source: [Delivery Tracking](https://docs.sdlccorp.com/docs/magento2-odoo-connector/sales/delivered/)
