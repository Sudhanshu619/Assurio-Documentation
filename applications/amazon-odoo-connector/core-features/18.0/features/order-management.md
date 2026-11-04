# Amazon Connector - Order Management

The Amazon connector automatically imports and manages both **FBM** (Fulfilled by Merchant) and **FBA** (Fulfilled by Amazon) orders from Seller Central into Odoo.

<a id="features"></a>

## Features

- Import FBM and FBA orders automatically
- Auto-create Odoo Sale Orders with full customer details (name, email, phone, shipping address)
- Track delivery status through the full lifecycle
- Support for multiple order types
- Cancel order synchronization with Amazon
- Export tracking numbers from Odoo deliveries to Amazon
- Order lines with per-item quantity, price, and Amazon product link

<a id="delivery-status-flow"></a>

## Delivery Status Flow

Orders move through the following statuses automatically:

```
Pending → Processing → Shipped → In Transit → Out for Delivery → Delivered
```

<a id="order-types-supported"></a>

## Order Types Supported

| Type | Description |
| --- | --- |
| **Standard** | Regular Amazon orders |
| **Preorder** | Pre-order items shipped when available |
| **Back Order** | Items currently out of stock |
| **Long Lead** | Extended delivery windows |
| **Sourcing on Demand** | Custom/made-to-order items |

<a id="importing-orders"></a>

## Importing Orders

<a id="manual-import"></a>

### Manual Import

On the instance form, click **Import Orders** to pull recent orders immediately.

<a id="automatic-import"></a>

### Automatic Import

Two scheduled actions handle automatic order imports:

| Scheduled Action | Interval | Purpose |
| --- | --- | --- |
| **Import All Orders (FBM + FBA)** | 30 min | Combined sync |
| **Import FBM Orders** | 15 min | FBM-only fast sync |

Enable these from **Configuration > Technical > Scheduled Actions** or from the instance form.

<a id="exporting-tracking-numbers"></a>

## Exporting Tracking Numbers

When you ship FBM orders from Odoo:

1. Open the delivery order in **Inventory > Transfers**
2. Enter the tracking number and carrier
3. The **Update FBM Order Status** scheduled action (runs every 1 hour) pushes tracking to Amazon
4. Or click **Export Tracking** manually on the sale order

<a id="cancelling-orders"></a>

## Cancelling Orders

Cancellations sync bidirectionally:

- **Amazon → Odoo:** The **Check Cancelled Orders** scheduled action (every 2 hours) pulls cancellations and updates Odoo sale orders
- **Odoo → Amazon:** Cancel the sale order in Odoo and the connector pushes the cancellation to Amazon

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Amazon Connector - Order Management](https://docs.sdlccorp.com/docs/18.0/amazon-odoo-connector/features/order-management/)
