# PrestaShop Connector - Order Management

Navigate to **PrestaShop > Orders > Orders**.

<a id="order-records"></a>

## Order Records

Order records include:

- PrestaShop Order ID and Reference
- Customer, Delivery Address, Invoice Address
- Order Lines with Product, Quantity, Unit Price, Subtotal
- Status: Draft / Confirmed / Shipped / Delivered / Cancelled
- Total Amount (auto-computed from lines)
- Currency, Notes

![Order List](https://docs.sdlccorp.com/assets/images/PrestaShop-order-1-b662dad63576d8faa91760b11ecbef80.webp)

![Order List Continued](https://docs.sdlccorp.com/assets/images/PrestaShop-order-2-3d2cc2bbd08247cb2ab0609a351c3e4d.webp)

---


<a id="creating-an-order"></a>

## Creating an Order

<a id="step-1---select-a-customer"></a>

### Step 1 - Select a Customer

Click **New** to create an order. Select an existing customer or create a new one:

![Select Customer](https://docs.sdlccorp.com/assets/images/PrestaShop-order-3-55b9a3a00ebfe7e2d593ee177066c8f3.webp)

![Customer Selection](https://docs.sdlccorp.com/assets/images/PrestaShop-order-33-867015e0b3eac4cd4c773a1c8c3827a6.webp)

<a id="step-2---add-products"></a>

### Step 2 - Add Products

Add product lines to the order cart:

![Order Cart](https://docs.sdlccorp.com/assets/images/PrestaShop-order-4-23cb124fdf9be44c54c4f8e533355647.webp)

<a id="step-3---configure-payment-and-shipping"></a>

### Step 3 - Configure Payment and Shipping

Set the currency, payment method, and addresses:

![Order Details](https://docs.sdlccorp.com/assets/images/PrestaShop-order-5-ba434e4064a7f042b730348e49d34cb2.webp)

| Field | Description |
| --- | --- |
| **Currency** | Order currency |
| **Payment Method** | Payment gateway used |
| **Shipping Address** | Customer delivery address |
| **Invoice Address** | Billing address |
| **Tracking Number** | Shipment tracking code |
| **Notes** | Internal order notes |

<a id="step-4---confirm-and-sync"></a>

### Step 4 - Confirm and Sync

Use the action buttons to progress the order through its lifecycle:

![Order Confirmed](https://docs.sdlccorp.com/assets/images/PrestaShop-order-6-984382cae07ba73abbb39be6b846a1a5.webp)

| Button | Action |
| --- | --- |
| **Draft** | Order is in draft state |
| **Create in PrestaShop** | Push the order to PrestaShop |
| **Send Invoice** | Generate and send invoice |
| **Shipped** | Mark as shipped with tracking number |
| **Delivered** | Mark as delivered |

<a id="step-5---order-shipped"></a>

### Step 5 - Order Shipped

![Order Shipped](https://docs.sdlccorp.com/assets/images/PrestaShop-order-7-9031d314b39d0db31d7be1b310613a96.webp)

<a id="step-6---order-delivered"></a>

### Step 6 - Order Delivered

![Order Delivered](https://docs.sdlccorp.com/assets/images/PrestaShop-order-8-d4c425e02626a4f289cc09e07d3cb2a0.webp)

---


<a id="cancelled-orders"></a>

## Cancelled Orders

![Cancelled Orders](https://docs.sdlccorp.com/assets/images/PrestaShop-cancell.order-1c0723b7fa81e9b5ff4c428df55e7941.webp)

---


<a id="related-documents"></a>

## Related Documents

<a id="invoices"></a>

### Invoices

Configure invoice settings, prefixes, and numbering:

![Invoice Configuration](https://docs.sdlccorp.com/assets/images/PrestaShop-invoice-1-3e07f737eb31a8251cf5b231f6433f43.webp)

![Invoice List](https://docs.sdlccorp.com/assets/images/PrestaShop-invoices-1-0a4904b9de6ceca21bff15dce14292ec.webp)

<a id="credit-slips"></a>

### Credit Slips

Manage refund document settings:

![Credit Slip Configuration](https://docs.sdlccorp.com/assets/images/PrestaShop-credit.slip-6063479b7f546fc99357b659dc4b52ad.webp)

![Credit Slip List](https://docs.sdlccorp.com/assets/images/PrestaShop-credit.slips-1-1ee75f580d8f4af270e06dd33390f4e7.webp)

<a id="delivery-slips"></a>

### Delivery Slips

Configure delivery document settings and default carrier:

![Delivery Slip Configuration](https://docs.sdlccorp.com/assets/images/PrestaShop-delivery.slip-e0886c7e5947c2923aae1abd7492ea4c.webp)

![Delivery Slip List](https://docs.sdlccorp.com/assets/images/PrestaShop-delivery.slips-1-397cd3e3196fbb08e55caef9f6b42681.webp)

<a id="shopping-carts"></a>

### Shopping Carts

View abandoned and ordered carts:

![Shopping Carts](https://docs.sdlccorp.com/assets/images/PrestaShop-shopping.carts-1-cf08784ac138fdcb21347c97b625b147.webp)

<a id="need-help"></a>

## Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/)

---

Source: [PrestaShop Connector - Order Management](https://docs.sdlccorp.com/docs/19.0/prestashop-odoo-connector/orders/order-management/)
