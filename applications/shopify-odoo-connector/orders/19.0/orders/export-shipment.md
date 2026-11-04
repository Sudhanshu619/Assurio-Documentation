# Export Shipment Tracking


<a id="why-this-matters"></a>

## Why this matters

When you fulfil a Shopify order from Odoo, the customer is waiting for the "your order has shipped" email from Shopify with the tracking link. Without exporting the shipment, that email never gets sent - and the order looks "still being processed" in the customer's Shopify account.

Configure the export to run automatically as part of the auto-scheduler so warehouse staff don't have to remember it per order.

<a id="overview"></a>

## Overview

When you ship a Shopify order from Odoo, you usually want Shopify to know about it so it can email the customer the standard "your order has shipped" notification with the tracking number. Export Shipment does exactly that: it takes the Odoo delivery's tracking info and posts it back to the Shopify order.

Push tracking numbers from Odoo delivery orders back to Shopify.

<a id="steps"></a>

## Steps

1. Navigate to **Shopify → Shipping → Delivery Orders** to view all delivery orders.

![Delivery Orders list view](https://docs.sdlccorp.com/assets/images/shopify-deliveryorder-1-42d85b32f35f15025394c66f3fc3a761.webp)

2. Open a delivery order to validate it and add tracking information. Use the **Push Tracking to Shopify** button to export.

![Delivery Order detail with Push Tracking to Shopify button](https://docs.sdlccorp.com/assets/images/shopify-deliveryorder-2-cfa81f8bac7de132264074fb383262c2.webp)

3. Once the delivery is completed, the order status changes to **Done**.

![Delivery Order with Done status](https://docs.sdlccorp.com/assets/images/shopify-deliveryorder-3-e284b9e1430d886bb9d99989b803278a.webp)

4. You can also view the Shopify Tracking records under **Shopify → Shipping → Shopify Tracking**.

![Shopify Tracking list view under Shipping menu](https://docs.sdlccorp.com/assets/images/shopify-tracking-2-f93989736d77300734c646b8868a06a8.webp)

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Export Shipment Tracking](https://docs.sdlccorp.com/docs/19.0/shopify-odoo-connector/orders/export-shipment/)
