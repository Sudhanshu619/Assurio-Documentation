# Import Products


<a id="overview"></a>

## Overview

A full product import pulls every product from your Shopify store into Odoo, creating Odoo product templates and variants that mirror what's in Shopify. Use it once during initial onboarding, and then again whenever you've made bulk changes in Shopify that you want to bring into Odoo in a single pass.

The import covers the product master plus its variants, attributes, prices, images and SKUs. Stock levels are imported separately - see [Import Stock](import-stock.md) for that.

<a id="when-to-use-a-full-import"></a>

### When to use a full import

- **Initial setup**, to bring your existing Shopify catalog into Odoo.
- **After bulk catalog edits in Shopify** that you want reflected in Odoo all at once.
- **When you suspect drift** between the two systems and want to reset the baseline.

For day-to-day, a few specific products at a time, use [Import Specific Products](import-specific-products.md) instead.

Import all products from your Shopify store into Odoo.

<a id="running-a-full-import"></a>

## Running a Full Import

1. Navigate to **Shopify → Shopify Data → Products**

![Shopify Data menu showing Products option](https://docs.sdlccorp.com/assets/images/shopify-product-1-0955e88920e7b348904cb6f7a5d456ed.webp)

2. The products list view shows all synced Shopify products.

![Shopify Products list view](https://docs.sdlccorp.com/assets/images/shopify-product-2-b5bc23278845311e7911a1b4f6171e84.webp)

3. Select your **Shopify Instance**
4. Leave the date filter empty for a full import, or set a **From Date** for incremental sync
5. Click **Import**

<a id="what-gets-created-in-odoo"></a>

## What Gets Created in Odoo

| Shopify | Odoo |
| --- | --- |
| Product | Product Template |
| Variant (Color/Size) | Product Variant |
| Product Image | Product Image |
| Price | Sales Price |
| Collection | Internal Category |
| Tags | Tags |

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Import Products](https://docs.sdlccorp.com/docs/19.0/shopify-odoo-connector/products/import-products/)
