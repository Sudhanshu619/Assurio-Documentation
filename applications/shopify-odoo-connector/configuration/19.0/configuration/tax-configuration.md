# Tax Configuration


<a id="why-tax-mapping-matters"></a>

## Why tax mapping matters

Shopify computes tax at the store level using rates per country/state. Odoo computes tax using fiscal positions and tax rules. The two don't agree out of the box: a US store with state-level sales tax produces line-item tax in Shopify, but Odoo would mark the same product with whichever fiscal position the customer record points to.

This screen translates one to the other, so the totals on Shopify and the totals in Odoo stay in lockstep - important for both accounting compliance and customer-facing receipts.

<a id="overview"></a>

## Overview

Shopify computes tax based on store-level tax rates, customer location, and product tax exemptions. Odoo computes tax based on fiscal positions and tax rules. The two don't speak the same language out of the box, so this mapping screen translates one to the other.

Get this right before you run a full order import - it's painful to retroactively fix tax on hundreds of orders.

Map Shopify taxes to Odoo fiscal positions and tax rules.

<a id="tax-mapping"></a>

## Tax Mapping

Navigate to **Shopify → Configuration → Tax Mapping**:

1. Click **New**
2. Set the **Shopify Tax Name** (as it appears in Shopify)
3. Select the corresponding **Odoo Tax**
4. Save

info

If your Shopify store uses Shopify Tax (automatic), the connector reads the tax amount
directly from the order and maps it to the closest Odoo tax based on rate.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Tax Configuration](https://docs.sdlccorp.com/docs/19.0/shopify-odoo-connector/configuration/tax-configuration/)
