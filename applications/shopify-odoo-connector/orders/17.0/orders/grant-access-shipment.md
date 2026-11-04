# Grant Fulfillment Access


<a id="why-this-step-exists"></a>

## Why this step exists

Shopify treats fulfilment as a privileged operation and blocks any third-party app from posting tracking numbers until the merchant has explicitly authorised the fulfilment service. Once you've completed the one-time consent flow on this page, every shipment exported from Odoo lands on the corresponding Shopify order without further intervention.

You only need to do this once per Shopify store. If you ever change the connector's fulfilment-service identifier (rare), re-run the consent flow.

<a id="overview"></a>

## Overview

Shopify treats fulfilment as a privileged operation - a connector can't push tracking numbers back to a Shopify order until you've explicitly granted the fulfilment service permission. This page walks through that one-time consent flow.

Grant shipping access to allow the connector to export tracking numbers back to Shopify.

<a id="configuration"></a>

## Configuration

1. Go to **Shopify → Configuration → Shopify Instances**
2. Open your instance
3. Enable **Grant Fulfillment Access**
4. Save

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

<a id="related"></a>

## Related

- [Export Shipment](export-shipment.md) - once you've granted access, this is where exported tracking numbers land.
- [Auto-Scheduler](../../../operations/17.0/operations/auto-scheduler.md) - set the shipment export to run automatically.
- [Troubleshooting](../../../reference/17.0/reference/troubleshooting.md) - what to check if tracking still isn't reaching the customer.

---

Source: [Grant Fulfillment Access](https://docs.sdlccorp.com/docs/17.0/shopify-odoo-connector/orders/grant-access-shipment/)
