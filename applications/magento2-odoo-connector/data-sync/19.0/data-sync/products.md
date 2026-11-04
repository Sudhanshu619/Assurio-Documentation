# Product Management

The Magento 2 Connector provides full bidirectional product synchronization between Odoo and Magento. Products can be pulled from Magento into Odoo, or pushed from Odoo to Magento, with all key attributes mapped automatically.

<a id="accessing-magento-products"></a>

## Accessing Magento Products

Navigate to **Magento > Magento Data > Products** to view all synced products.

![Magento Data menu with Products option](https://docs.sdlccorp.com/assets/images/mp-1-e02c6083f65592e431e1d4d2c8f3b027.webp)

<a id="product-list-view"></a>

## Product List View

The product list displays all synchronized products with the following columns:

| Column | Description |
| --- | --- |
| **Instance** | The Magento instance this product belongs to |
| **Magento** | The Magento product ID |
| **SKU** | The product SKU from Magento |
| **Name** | Product name |
| **Odoo Product** | The corresponding product record in Odoo (e.g., `[car] 321.99`) |
| **Price** | Product price |
| **Status** | Product status in Magento (Enabled / Disabled) |
| **Visibility** | Magento visibility setting (Catalog, Search, Catalog & Search, Not Visible) |

![Magento Products list view](https://docs.sdlccorp.com/assets/images/mp-11-bfb84f7ca43366a94afaa63e24b9bf21.webp)

<a id="product-mapping-model"></a>

## Product Mapping Model

Each Magento product record maps to an Odoo product with the following field correspondence:

| Magento Field | Odoo Field | Direction |
| --- | --- | --- |
| `name` | `product_template.name` | Bidirectional |
| `sku` | `product_template.default_code` | Bidirectional |
| `price` | `product_template.list_price` | Bidirectional |
| `status` | `product_template.active` | Magento to Odoo |
| `visibility` | Custom field | Magento to Odoo |
| `weight` | `product_template.weight` | Bidirectional |
| `description` | `product_template.description` | Bidirectional |
| `short_description` | `product_template.description_sale` | Bidirectional |
| `qty` | `product.product.qty_available` | Bidirectional (via Inventory) |

<a id="product-actions"></a>

## Product Actions

You can perform the following actions on Magento products:

- **Sync Products** (from Instance) -- Pull all products from Magento into Odoo. New products are created; existing products are updated.
- **Create in Magento** -- Push a new Odoo product to Magento.
- **Update in Magento** -- Push changes made in Odoo back to the Magento store.
- **Pull from Magento** -- Refresh a specific product's data from Magento.

Auto-Sync

When auto-sync is enabled on the instance, products are synchronized automatically at the configured interval. See [Auto Sync Cron Jobs](../../../advanced/19.0/advanced/auto-sync.md) for details.

<a id="creating-a-product-in-magento-from-odoo"></a>

## Creating a Product in Magento from Odoo

1. Navigate to **Magento > Magento Data > Products**.
2. Click **New**.
3. Select the **Instance** to connect to.
4. Fill in the product details (Name, SKU, Price, etc.).
5. Click **Create in Magento**.

The connector will push the product to your Magento store via the REST API and store the returned Magento product ID for future reference.

<a id="pulling-products-from-magento"></a>

## Pulling Products from Magento

To import all products from Magento:

1. Go to **Magento > Instances**.
2. Open your instance.
3. Click **Sync Products**.

The connector fetches all products from Magento, creates or updates the corresponding Odoo product records, and links them via the Magento product ID.

tip

Use [Field Mapping](../../../advanced/19.0/advanced/field-mapping.md) to customize which fields are synced and in which direction.

<a id="next-steps"></a>

## Next Steps

- [Manage Customers](customers.md)
- [Sync Categories](categories.md)
- [Configure Product Field Mapping](../../../advanced/19.0/advanced/field-mapping.md)

---

Source: [Product Management](https://docs.sdlccorp.com/docs/19.0/magento2-odoo-connector/data-sync/products/)
