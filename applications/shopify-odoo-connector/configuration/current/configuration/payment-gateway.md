# Payment Gateway Configuration


<a id="why-this-mapping-matters"></a>

## Why this mapping matters

Every imported Shopify order has a payment record naming the gateway the customer used. Without an Odoo mapping, the connector doesn't know which accounting journal to post against - Stripe vs PayPal vs Shop Pay vs manual gift card. Set this up before the first scheduled order import and you'll save reconciliation pain downstream.

<a id="overview"></a>

## Overview

Every Shopify order arrives with a payment record naming the gateway the customer used (Stripe, PayPal, Shop Pay, manual, etc.). Without a mapping, the connector can't tell Odoo accounting which journal that payment belongs to. This page sets that mapping up so accounting stays clean.

Map Shopify payment gateways to Odoo accounting journals.

<a id="gateway-mapping"></a>

## Gateway Mapping

Navigate to **Shopify → Configuration → Payment Gateway**:

1. Click **New**
2. Set the **Shopify Gateway Name** (e.g., `shopify_payments`, `paypal`, `stripe`)
3. Select the **Odoo Journal**
4. Save

<a id="common-gateway-mappings"></a>

## Common Gateway Mappings

| Shopify Gateway | Recommended Odoo Journal |
| --- | --- |
| Shopify Payments | Shopify Bank Journal |
| PayPal | PayPal Journal |
| Stripe | Stripe Journal |
| Cash on Delivery | Cash Journal |
| Manual | Bank Journal |

tip

Create a dedicated bank journal in Odoo for each Shopify payment gateway for clean reconciliation.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Payment Gateway Configuration](https://docs.sdlccorp.com/docs/shopify-odoo-connector/configuration/payment-gateway/)
