# BigCommerce Connector - Data Synchronization


<a id="product-bindings"></a>

## Product Bindings

Navigate to **BigCommerce > Bindings > Product Bindings**.

![Product Binding Listing](https://docs.sdlccorp.com/assets/images/product-binding-listing-1480241bf02ee2ced8f281ca5c69fb5b.webp)

![Product Binding Form](https://docs.sdlccorp.com/assets/images/product-binding-form-ffc490618a3be05f14ba9c994de5eabe.webp)

- Each binding links one Odoo product to one BigCommerce product by ID
- Products sync with name, SKU, price, description, weight, and dimensions
- Images are downloaded and stored in Odoo
- Click **Push to BigCommerce** to create or update products in your store

<a id="order-bindings"></a>

## Order Bindings

Navigate to **BigCommerce > Bindings > Order Bindings**.

![Order Binding Listing](https://docs.sdlccorp.com/assets/images/order-binding-listing-e0baab0a638c23c06365c365e07868cf.webp)

![Order Binding Form](https://docs.sdlccorp.com/assets/images/order-binding-form-057caf2867a08fb7544214b3526e71cb.webp)

<a id="order-status-mapping"></a>

### Order Status Mapping

| BigCommerce Status | Odoo Status | Description |
| --- | --- | --- |
| Incomplete | Draft | Order started but not completed |
| Pending | Draft | Awaiting payment |
| Awaiting Fulfillment | Confirmed | Payment received, ready to ship |
| Shipped | Shipped | Carrier has the package |
| Completed | Delivered | Order fully fulfilled |
| Cancelled | Cancelled | Order cancelled |

<a id="customer-bindings"></a>

## Customer Bindings

Navigate to **BigCommerce > Bindings > Customer Bindings**.

![Customer Binding Listing](https://docs.sdlccorp.com/assets/images/customer-binding-listing-6743367a64b8c8e2e31cf1ae05f7eb38.webp)

![Customer Binding Form](https://docs.sdlccorp.com/assets/images/customer-binding-form-986e21d6693f8230199adba32edbe81f.webp)

- Customers synced with name, email, phone, company, and addresses
- Billing and shipping addresses imported as child contacts
- Bidirectional: create in Odoo and push to BigCommerce

<a id="category-bindings"></a>

## Category Bindings

Navigate to **BigCommerce > Bindings > Category Bindings**.

![Category Binding Listing](https://docs.sdlccorp.com/assets/images/category-bining-listing-0adcb50379251ab980c8d77ef76a5a77.webp)

![Category Binding Form](https://docs.sdlccorp.com/assets/images/category-bining-form-6f99f4d802d4812e80f304dc3add4193.webp)

- Parent-child relationships maintained during sync
- Bidirectional: create categories in Odoo and push to BigCommerce

<a id="inventory"></a>

## Inventory

Navigate to **BigCommerce > Inventory**.

| Status | Color | Description |
| --- | --- | --- |
| **In Stock** | Green | Above low stock threshold |
| **Low Stock** | Yellow | At or below threshold, above 0 |
| **Out of Stock** | Red | Quantity is 0 |

<a id="webhooks"></a>

## Webhooks

Navigate to **BigCommerce > Webhooks > Subscriptions**.

![Webhook Subscriptions](https://docs.sdlccorp.com/assets/images/webhook-subscription-520e811f070f4aa67a9f4698eb97e2ce.webp)

Subscribe to: orders/created, orders/updated, products/updated, shipments/created

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [BigCommerce Connector - Data Synchronization](https://docs.sdlccorp.com/docs/bigcommerce-odoo-connector/sync/data-sync/)
