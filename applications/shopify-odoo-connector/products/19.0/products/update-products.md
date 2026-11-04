# Update Products in Shopify


<a id="which-fields-get-pushed"></a>

## Which fields get pushed

By default the connector pushes the full set of mapped product fields back to Shopify - name, description, attributes, images, pricing. Narrow what gets pushed under [Product Configuration](../../../configuration/19.0/configuration/product-configuration.md).

<a id="overview"></a>

## Overview

Update is the Odoo-to-Shopify direction of the product sync. When you change a product in Odoo (price, name, image, description, etc.) and you want that change to land in Shopify, this is the action that does it.

By default the connector pushes the full set of mapped fields. You can narrow what gets pushed in [Product Configuration](../../../configuration/19.0/configuration/product-configuration.md).

Push product changes from Odoo back to Shopify.

<a id="updating-a-single-product"></a>

## Updating a Single Product

1. Open the product in Odoo. The product form shows **Create in Shopify** and **Update in Shopify** buttons.

![Shopify Product form with Create and Update in Shopify buttons](https://docs.sdlccorp.com/assets/images/shopify-product-3-4fdb3b13877e4cc5628765779fb20423.webp)

2. Click **Shopify → Update in Shopify**

<a id="bulk-update"></a>

## Bulk Update

1. Navigate to **Shopify → Products → Update Products**
2. Select your **Shopify Instance**
3. Choose products to update (or select all)
4. Click **Update**

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

<a id="related"></a>

## Related

- [Import Products](import-products.md) - pull catalog from Shopify first.
- [Product Configuration](../../../configuration/19.0/configuration/product-configuration.md) - narrow which fields get pushed.
- [Auto-Scheduler](../../../operations/19.0/operations/auto-scheduler.md) - schedule automatic Odoo→Shopify product updates.

---

Source: [Update Products in Shopify](https://docs.sdlccorp.com/docs/19.0/shopify-odoo-connector/products/update-products/)
