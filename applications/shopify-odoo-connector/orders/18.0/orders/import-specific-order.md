# Import Specific Order


<a id="when-to-use-targeted-import"></a>

## When to use targeted import

Use this action whenever a specific order is missing from Odoo (a sync outage, a webhook that didn't fire, a recently-created order during a backfill) or when you want to verify your connector setup against a known reference order before running a full historical import.

It's also the recommended way to onboard a single new order type - for example, the first order of a freshly-launched product line - when you'd rather validate the round-trip on one item before exposing it to the full scheduled sync.

<a id="overview"></a>

## Overview

Targeted order import pulls one specific Shopify order by ID. Use it to recover a single order that got skipped during a sync outage, or to verify on a known reference order that your connector setup is working end-to-end.

Import a single order by its Shopify Order ID.

<a id="steps"></a>

## Steps

1. Navigate to **Shopify → Orders → Import Specific Order**
2. Enter the **Shopify Order ID** (numeric, e.g. `5001234567890`)
3. Click **Import**

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

<a id="related"></a>

## Related

- [Import Unshipped Orders](import-unshipped-orders.md) - bulk catch-up for backlogs.
- [Import Shipped Orders](import-shipped-orders.md) - historical backfill of already-fulfilled orders.
- [Queue Management](../../../operations/18.0/operations/queue-management.md) - retry imports that failed first time round.

---

Source: [Import Specific Order](https://docs.sdlccorp.com/docs/18.0/shopify-odoo-connector/orders/import-specific-order/)
