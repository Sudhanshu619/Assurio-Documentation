# Product Configuration


<a id="overview"></a>

## Overview

Product configuration controls how the connector translates a Shopify product into an Odoo product (and vice-versa). Before you run a full [product import](../../../products/19.0/products/import-products.md), spend a few minutes here to make sure the mapping matches your Odoo data model.

You can configure attribute mapping (variants), category mapping (Shopify collections ↔ Odoo categories), and per-field sync behaviour for the product master.

Configure how products sync between Shopify and Odoo.

<a id="product-sync-settings"></a>

## Product Sync Settings

Navigate to **Shopify → Configuration → Product Settings**:

| Setting | Description |
| --- | --- |
| **Create Variants** | Auto-create Odoo product variants from Shopify options |
| **Sync Images** | Import product images from Shopify |
| **Price List** | Odoo price list to use for Shopify prices |
| **Product Template** | Default template for new products |
| **Published State** | Only sync published products |

<a id="categories"></a>

## Categories

You can manage Shopify product categories from **Shopify → Shopify Data → Categories**.

![Shopify Data menu showing Categories option](https://docs.sdlccorp.com/assets/images/shopify-categories-1-19a235af024712bf4d850b8266af65b6.webp)

The categories list view shows all synced product categories.

![Shopify Categories list view](https://docs.sdlccorp.com/assets/images/shopify-categories-12png-a019442d221610178880467b982b8abb.webp)

To create or update a category, open the category form and use the **Create in Shopify** or **Update in Shopify** buttons.

![Shopify Category form with Create and Update in Shopify buttons](https://docs.sdlccorp.com/assets/images/shopify-categories-3-b865a76d8ae7fb9ab0569da2de7c6508.webp)

<a id="category-mapping"></a>

### Category Mapping

Navigate to **Shopify → Mapping → Category Mapping** to map category fields between Odoo and Shopify.

![Mapping menu with Category Mapping option](https://docs.sdlccorp.com/assets/images/shopify-mapp.category-1-dbe4968bf21a16852dfee61db9a37f3f.webp)

![Category Mapping list view](https://docs.sdlccorp.com/assets/images/shopify-mapp.category-2-1e380cde59b778736ae075eacfe69311.webp)

To create a new mapping, click **New**, fill in the fields, and click **Test** to verify.

![Category Mapping form - select fields and click Test](https://docs.sdlccorp.com/assets/images/shopify-mapp.category-3-7371619592a6effca191206cab838d6b.webp)

<a id="attribute-mapping"></a>

## Attribute Mapping

Map Shopify product options (Color, Size, etc.) to Odoo product attributes:

1. Go to **Shopify → Configuration → Attribute Mapping**
2. Click **New**
3. Set the **Shopify Attribute Name** and matching **Odoo Attribute**
4. Save

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Product Configuration](https://docs.sdlccorp.com/docs/19.0/shopify-odoo-connector/configuration/product-configuration/)
