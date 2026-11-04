# ShipStation Connector - Data Synchronization


<a id="order-sync"></a>

## Order Sync

Navigate to **ShipStation > ShipStation Data > Orders**.

![Orders](https://docs.sdlccorp.com/assets/images/shipstationdata-order-0c6ed77340103ec29bee59a237330b63.webp)

To sync orders manually, go to **Instances**, open an instance, and click **Sync Orders**.

- Orders include line items, shipping address, billing address, and rates
- Order status is mapped: awaiting_payment to Draft, awaiting_shipment to Confirmed, shipped to Shipped
- Each order links to the ShipStation instance and stores the ShipStation Order ID

<a id="product-sync"></a>

## Product Sync

Navigate to **ShipStation Data > Products**.

![Products](https://docs.sdlccorp.com/assets/images/shipstation-product-10010390b4ba4b6c164343e682a81208.webp)

![Product Form](https://docs.sdlccorp.com/assets/images/shipstation-product-form-967624c66190426a41ea7ebbdbcab805.webp)

- Products sync with SKU, name, price, weight, and dimensions
- Matched to existing Odoo products by SKU/reference code
- New products are created automatically if no match found

<a id="customer-sync"></a>

## Customer Sync

Navigate to **ShipStation Data > Customers**.

![Customers](https://docs.sdlccorp.com/assets/images/shipstation-customer-1caef2e68659cc3467876a3679e30638.webp)

![Customer Form](https://docs.sdlccorp.com/assets/images/shipstation-customer-form-151e1c9353c42c59ae1a9629c49ebaa5.webp)

Customers are imported with name, email, and addresses.

<a id="shipment-sync"></a>

## Shipment Sync

Navigate to **ShipStation Data > Shipments**. Shipments include carrier, tracking number, and delivery status.

<a id="category-sync"></a>

## Category Sync

![Categories](https://docs.sdlccorp.com/assets/images/category-listing-753dc839bad86682ee7fe02f4528fdf5.webp)

![Category Form](https://docs.sdlccorp.com/assets/images/category-form-afa5584bba2b9eeb782e2d82f2493ee4.webp)

Categories can be synced from the respective menus under ShipStation Data.

<a id="inventory-management"></a>

## Inventory Management

Navigate to **ShipStation > Inventory**.

![Inventory](https://docs.sdlccorp.com/assets/images/inventory-f429b53f2fa2dbdc14d0b4f0a97c0c8d.webp)

![Inventory Form](https://docs.sdlccorp.com/assets/images/inventory-form-40f8dbfaccf069802b38a54546807a7e.webp)

| Status | Color | Description |
| --- | --- | --- |
| **In Stock** | Green | Quantity above the low stock threshold |
| **Low Stock** | Yellow | Quantity at or below threshold but above 0 |
| **Out of Stock** | Red | Quantity is 0 |

Actions:

- **Refresh Inventory:** Pull latest stock levels from ShipStation
- **Export PDF:** Download inventory report as a styled PDF

<a id="shipping-and-tracking"></a>

## Shipping and Tracking

![Delivery Order](https://docs.sdlccorp.com/assets/images/shipping-delivery-order-1da09dfceca21a05e7b1cd8942d8ae9a.webp)

![Tracking](https://docs.sdlccorp.com/assets/images/shipping-tracking-a20ae6e1565061412d9dde5c7a391ce7.webp)

- Tracking numbers are automatically synced when shipments are created in ShipStation
- Tracking info appears on the order form in Odoo
- When an order is marked as 'Shipped', the tracking number is pushed to ShipStation

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [ShipStation Connector - Data Synchronization](https://docs.sdlccorp.com/docs/shipstation-odoo-connector/sync/data-sync/)
