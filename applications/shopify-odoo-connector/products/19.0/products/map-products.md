# Map Products


<a id="when-manual-mapping-helps"></a>

## When manual mapping helps

Manual mapping pairs an existing Odoo product with an existing Shopify product so future syncs treat them as one. Typical cases:

- The same SKU exists in both systems but got created independently.
- A merge after a data-migration project where both sides have stale data.
- Fixing a one-off mismatch without re-running a full import.

<a id="overview"></a>

## Overview

Sometimes the same product exists in both Shopify and Odoo but the connector hasn't paired them - usually because the SKU differs or one side was created manually before the other. Manual mapping pairs them up by ID so future syncs treat them as the same product.

Link existing Odoo products to their Shopify equivalents without re-importing.

<a id="mapping-steps"></a>

## Mapping Steps

1. Navigate to **Shopify → Mapping → Product Mapping**

![Mapping menu with Product Mapping option](https://docs.sdlccorp.com/assets/images/shopify-mapp.product-1-bb1888c8ffe9db0e3999461df73e5571.webp)

2. The Product Mapping list view shows all existing field mappings.

![Product Mapping list view with New, Test, and Load New Fields buttons](https://docs.sdlccorp.com/assets/images/shopify-mapp.product-2-93ea28a5d5a129a489327f151b5fcd94.webp)

3. Click **New** to create a new mapping. Select the fields and click **Test** to verify.

![Product Mapping form - select fields and click Test](https://docs.sdlccorp.com/assets/images/shopify-mapp.product-3-807b7f61a22b6879131aa5dae2e5cca5.webp)

4. Select the **Odoo Product**
5. Enter the **Shopify Product ID**
6. Enter the **Shopify Variant ID** (if applicable)
7. Save

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Map Products](https://docs.sdlccorp.com/docs/19.0/shopify-odoo-connector/products/map-products/)
