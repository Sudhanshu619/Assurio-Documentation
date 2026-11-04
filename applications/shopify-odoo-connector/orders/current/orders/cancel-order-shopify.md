# Cancel Order in Shopify


<a id="when-to-cancel-from-odoo"></a>

## When to cancel from Odoo

Cancel from Odoo (instead of switching to the Shopify admin) when:

- Your team works primarily inside Odoo and doesn't have permissioned Shopify access.
- You need a single audit trail of cancellations - Odoo's chatter records why.
- The cancellation is triggered by an Odoo workflow (out-of-stock, fraud check, customer-facing edit).

In the other direction - when the customer cancels from the Shopify admin - see [Import Cancelled Orders](import-cancel-order.md).

<a id="overview"></a>

## Overview

Sometimes an order needs to be cancelled before fulfilment - fraud, customer change of mind, out of stock. Cancelling from Odoo (instead of switching to the Shopify admin) keeps both systems consistent and triggers the standard customer-facing cancellation email from Shopify.

Cancel a Shopify order from within Odoo.

<a id="steps"></a>

## Steps

1. Open the Sales Order in Odoo

![New order form with Create in Shopify button](https://docs.sdlccorp.com/assets/images/shopify-orders-3-564fc81d7fd33197ad25e65b52eb15d6.webp)

2. Once the order is confirmed, you can use the **Cancel** button to cancel it.

![Confirmed Sales Order with Cancel and Create in Shopify buttons](https://docs.sdlccorp.com/assets/images/shopify-orders-4-710b42a772467186dcc623ea04dbdea0.webp)

3. Click **Shopify → Cancel in Shopify**
4. Select the **Cancellation Reason**
5. Choose whether to **Restock Items**
6. Click **Confirm**

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Cancel Order in Shopify](https://docs.sdlccorp.com/docs/shopify-odoo-connector/orders/cancel-order-shopify/)
