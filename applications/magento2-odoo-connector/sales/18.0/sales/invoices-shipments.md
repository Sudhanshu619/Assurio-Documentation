# Invoices, Shipments & Credit Memos

The Magento 2 Connector synchronizes invoices, shipments, and credit memos between Odoo and Magento, ensuring your financial and fulfillment data stays consistent across both platforms.

---


<a id="invoices"></a>

## Invoices

<a id="accessing-invoices"></a>

### Accessing Invoices

Navigate to **Magento > Sales > Invoices** to view all Magento-synced invoices.

![Sales menu showing Invoices option](https://docs.sdlccorp.com/assets/images/s-invoice-1-5485b2b7f18a7d65dde7fa8fc359afda.webp)

<a id="invoice-list-view"></a>

### Invoice List View

The invoice list displays all synchronized invoices:

![Magento Invoices list view](https://docs.sdlccorp.com/assets/images/s-invoice-11-9bc775aeef43ed835db9ddaa3964961f.webp)

| Column | Description |
| --- | --- |
| **Number** | Odoo invoice reference (e.g., `INV/2026/00064`) |
| **Bill-to Name** | Customer name on the invoice |
| **Invoice Date** | Date the invoice was created |
| **Due Date** | Payment due date |
| **Tax Excluded** | Invoice total excluding tax |
| **Status** | Invoice status (Not Paid, Paid, etc.) |

<a id="creating-an-invoice"></a>

### Creating an Invoice

![Invoice form view](https://docs.sdlccorp.com/assets/images/s-invoice-111-decc6f5d37d59d75e5d921b4d99ab52f.webp)

To create and sync an invoice:

1. Navigate to **Magento > Sales > Invoices**.
2. Click **New** to create a draft invoice.
3. Select the **Customer**.
4. Set the **Invoice Date** and **Due Date**.
5. Add products to the **Invoice Lines** tab.
6. Click **Confirm** to move the invoice from Draft to Posted status.

info

When an invoice is confirmed in Odoo and the instance is configured with **Update Magento Status When Paid**, the payment status is automatically pushed to Magento.

<a id="invoice-sync-behavior"></a>

### Invoice Sync Behavior

| Scenario | Behavior |
| --- | --- |
| Order pulled from Magento with invoice | Invoice is automatically created in Odoo |
| Invoice created in Odoo | Can be pushed to Magento via order update |
| Invoice paid in Odoo | Payment status synced to Magento (if enabled) |
| Invoice paid in Magento | Payment status synced to Odoo on next sync |

---


<a id="shipments"></a>

## Shipments

<a id="accessing-shipments"></a>

### Accessing Shipments

Navigate to **Magento > Sales > Shipments** to view all shipment records.

![Sales menu showing Shipments option](https://docs.sdlccorp.com/assets/images/s-shipment-1-8ccf8cfc0db101aca94bcfba7af1ec4c.webp)

<a id="shipment-list-view"></a>

### Shipment List View

The shipment list shows all synchronized shipment records:

![Magento Shipments list view](https://docs.sdlccorp.com/assets/images/s-shipment-11-a45a7f21e189cb541511217e5e96f9c9.webp)

| Column | Description |
| --- | --- |
| **Shipment** | Odoo delivery reference (e.g., `WH/OUT/00077`) |
| **Ship Date** | Date and time of shipment |
| **Order #** | The associated Magento order ID |
| **Order Date** | Original order date |
| **Ship-to Name** | Recipient name |
| **Customer Email** | Customer email address |
| **Customer Phone** | Customer phone number |
| **Total Quantity** | Total number of items shipped |
| **View** | Link to view full shipment details |

<a id="shipment-sync-behavior"></a>

### Shipment Sync Behavior

- When an order is delivered in Odoo (delivery order validated), the shipment data is synced to Magento.
- When a shipment is created in Magento, the delivery information is pulled into Odoo on the next order sync.
- Tracking numbers and carrier information are included in the sync when available.

tip

Ensure your Odoo warehouse is properly configured with delivery methods to enable accurate shipment tracking between systems.

---


<a id="credit-memos"></a>

## Credit Memos

<a id="accessing-credit-memos"></a>

### Accessing Credit Memos

Navigate to **Magento > Sales > Credit Memos** to view all credit memo records.

![Sales menu showing Credit Memos option](https://docs.sdlccorp.com/assets/images/s-memo-1-2792572ae8c2f3e2caf4e93cd7775cb8.webp)

<a id="credit-memo-list-view"></a>

### Credit Memo List View

The credit memo list displays all synchronized refund records:

![Magento Credit Memos list view](https://docs.sdlccorp.com/assets/images/s-memo-11-c8f367062aa9371a32b22dd323424b36.webp)

| Column | Description |
| --- | --- |
| **Credit Memo** | Magento credit memo ID (e.g., `000000001`) |
| **Credit Memo Created** | Date and time the credit memo was created |
| **Order #** | The associated Magento order ID |
| **Order Date/Time** | Original order date and time |
| **Bill-to Name** | Customer name |
| **Refund Status** | Status of the refund (Refunded, Pending, etc.) |
| **Currency** | Currency of the refund |
| **Refunded** | Refund amount |
| **View** | Link to view full credit memo details |

<a id="credit-memo-sync-behavior"></a>

### Credit Memo Sync Behavior

- Credit memos created in Magento are automatically pulled into Odoo during order sync.
- The refund amount, associated order, and status are all synchronized.
- Corresponding credit notes can be created in Odoo's accounting module.

warning

Credit memos affect inventory and accounting. Ensure your refund policies are consistent between Magento and Odoo to avoid discrepancies.

<a id="next-steps"></a>

## Next Steps

- [Track Delivered & Not Delivered Orders](delivered.md)
- [View Sync Reports](../../../reference/18.0/reference/sync-reports.md)
- [Troubleshoot sync issues](../../../reference/18.0/reference/troubleshooting.md)

---

Source: [Invoices, Shipments & Credit Memos](https://docs.sdlccorp.com/docs/18.0/magento2-odoo-connector/sales/invoices-shipments/)
