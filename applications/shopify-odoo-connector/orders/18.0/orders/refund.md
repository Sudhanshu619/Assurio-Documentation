# Process Refunds


<a id="what-the-refund-action-does"></a>

## What the refund action does

Triggering a refund from Odoo:

1. Posts a **credit note** in Odoo against the original sale order's invoice.
2. Calls the **Shopify refund API** to refund the customer through the original payment gateway.
3. Optionally puts returned items back into Odoo inventory (your choice per refund).
4. Triggers Shopify's standard "you've been refunded" email to the customer.

The customer never sees the Odoo side - everything looks like a normal Shopify refund.

<a id="overview"></a>

## Overview

The refund action wraps the whole refund workflow into a single step: post the credit note in Odoo, refund the customer through the original payment gateway in Shopify, and (optionally) put returned items back into inventory. The Shopify-side refund is what triggers the customer's "you've been refunded" email.

Process full or partial refunds for Shopify orders.

<a id="refund-steps"></a>

## Refund Steps

1. Navigate to **Shopify → Orders → Import Refunds** to pull existing refunds
2. Or open a Sales Order in Odoo and click **Shopify → Create Refund**
3. Select the items and quantities to refund
4. Click **Refund**

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

<a id="related"></a>

## Related

- [Import Returns](import-returns.md) - the matching return-of-goods side of the refund.
- [Payment Gateway Mapping](../../../configuration/18.0/configuration/payment-gateway.md) - make sure refunds post to the right journal.
- [Order Configuration](../../../configuration/18.0/configuration/order-configuration.md) - set defaults for refund behaviour.

---

Source: [Process Refunds](https://docs.sdlccorp.com/docs/18.0/shopify-odoo-connector/orders/refund/)
