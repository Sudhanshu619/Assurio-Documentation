# WooCommerce Connector - Data Synchronization


<a id="product-sync"></a>

## Product Sync

Navigate to **WooCommerce > WooCommerce Data > Products**.

![Products](https://docs.sdlccorp.com/assets/images/products-0cd12269cd29de29e1da7282316bd891.webp)

- Products sync with name, SKU, price, description, images, weight, and dimensions
- Product variants and attributes are synced
- Matched to existing Odoo products by SKU/reference
- Click **Create in WooCommerce** or **Update in WooCommerce** to push products

<a id="ai-content-generation"></a>

### AI Content Generation

Use the **AI Content Wizard** to automatically generate:

- Product descriptions (long and short)
- SEO-optimized meta titles and descriptions
- Marketing copy based on product attributes

<a id="order-sync"></a>

## Order Sync

Navigate to **WooCommerce Data > Orders**.

![Orders](https://docs.sdlccorp.com/assets/images/orders-15d3f7828bc1feb9f08cb9b517f9f5be.webp)

<a id="order-status-mapping"></a>

### Order Status Mapping

| WooCommerce Status | Odoo Status | Description |
| --- | --- | --- |
| pending | Draft | Awaiting payment |
| processing | Confirmed | Payment received, being processed |
| on-hold | Draft | Awaiting action |
| completed | Delivered | Order fulfilled |
| cancelled | Cancelled | Order cancelled |
| refunded | Cancelled | Order fully refunded |

When you change an order status in Odoo, the status is automatically pushed back to WooCommerce.

<a id="customer-sync"></a>

## Customer Sync

Navigate to **WooCommerce Data > Customers**.

![Customers](https://docs.sdlccorp.com/assets/images/customers-fbb84f3e45b1fedc15a0ffd3bc70fd41.webp)

- Customers imported with name, email, phone, billing and shipping addresses
- Linked to Odoo contacts (res.partner)
- Guest customers handled gracefully

<a id="category-sync"></a>

## Category Sync

Navigate to **WooCommerce Data > Categories**.

![Categories](https://docs.sdlccorp.com/assets/images/categories-fce028a5aff8b589bc0426fd32b85158.webp)

- Bidirectional: create categories in Odoo and push to WooCommerce
- Parent-child relationships maintained

<a id="coupon-management"></a>

## Coupon Management

Navigate to **WooCommerce > Coupons**.

![Coupons](https://docs.sdlccorp.com/assets/images/coupons-203bd1968db1f5f37aa14a4de1ef3056.webp)

| Field | Description |
| --- | --- |
| **Code** | Unique discount code (e.g., SAVE20) |
| **Discount Type** | Percentage or Fixed amount |
| **Amount** | Discount value |
| **Expiry Date** | When the coupon expires |
| **Minimum Spend** | Minimum order total to apply |
| **Usage Limit** | How many times the coupon can be used |
| **Free Shipping** | Whether coupon grants free shipping |

<a id="inventory-management"></a>

## Inventory Management

Navigate to **WooCommerce > Inventory**.

![Inventory](https://docs.sdlccorp.com/assets/images/inventory-0ab25186cf6a0fd57271c0b76f92aed2.webp)

| Status | Color | Description |
| --- | --- | --- |
| **In Stock** | Green | Above low stock threshold |
| **Low Stock** | Yellow | At or below threshold, above 0 |
| **Out of Stock** | Red | Quantity is 0 |

<a id="shipping-and-tracking"></a>

## Shipping and Tracking

Navigate to **WooCommerce > Shipping**.

![Shipping](https://docs.sdlccorp.com/assets/images/shipping-a6b3aae7504e9d19a68da56f61546ef1.webp)

![Delivery Orders](https://docs.sdlccorp.com/assets/images/delivery-orders-fb7981c93b415ed01d622e24ba5f36b2.webp)

![Tracking](https://docs.sdlccorp.com/assets/images/woo-tracking-94368269d9d0f8de382914ee0319f44c.webp)

- Tracking numbers synced when shipments are created
- Tracking info pushed back to WooCommerce for customer visibility

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [WooCommerce Connector - Data Synchronization](https://docs.sdlccorp.com/docs/19.0/woocommerce-odoo-connector/sync/data-sync/)
