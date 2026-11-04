# POS Product Price on Card - Odoo 19 POS Extension

**POS Product Price on Card** is a lightweight extension to Odoo 19's Point of Sale module. It surfaces the selling price of every product directly on the cashier's product grid, so prices are visible at a glance without having to add the product to the cart first.

The module also intelligently surfaces savings: whenever the current order is on a pricelist that lowers the price (loyalty discount, wholesale tier, happy-hour promotion), the original price strikes through, the new price appears in a green pill, and a red `-X%` badge animates onto the card corner. Customers see their savings before they pay - which builds trust and speeds up checkout.

> **In one sentence:** the module makes prices and discounts visible on the POS product grid, with a per-shop on/off toggle and zero impact on the rest of Odoo.

<a id="module-info"></a>

## Module info

| Field | Value |
| --- | --- |
| **Module name** | `sdlc_pos_product_price` |
| **Version** | 19.0.1.0.0 |
| **Odoo version** | 19.0 (Community & Enterprise) |
| **License** | LGPL-3 / OPL-1 |
| **Publisher** | SDLC Corp |
| **Dependencies** | `point_of_sale` (bundled with every Odoo install - no extras) |

<a id="what-it-changes-in-the-pos"></a>

## What it changes in the POS

The module adds **four visible changes** to Odoo 19 Point of Sale:

1. A **green gradient price pill** under every product card in the cashier's grid.
2. A **strike-through original price** next to the pill, shown only when a pricelist applies a discount.
3. An **animated red `-X%` savings badge** in the top-left corner of the card, shown only when discounted.
4. A **toggle on each shop's configuration form** to turn the feature on or off independently per shop.

Non-invasive by design

The module **never modifies prices**. It reads the same pricing logic Odoo uses internally and renders the result. Disabling the module reverts the POS to standard Odoo behaviour with **zero data loss** - the boolean column on `pos.config` is dropped, the JavaScript stops loading, and the form-view inheritance is removed.

<a id="before-vs-after"></a>

## Before vs. after

| Behaviour | Standard Odoo POS | With this module |
| --- | --- | --- |
| Price visible on a product card | Hidden | Shown as a gradient pill |
| Customer-specific pricelist price | Only visible after adding to cart | Live on every card before adding |
| Discount visibility | None on the card | Strike-through plus `-X%` badge |
| Per-shop control | Not applicable | One toggle on each shop's config |
| Reaction to pricelist switch | Static | All cards recalculate instantly |

<a id="who-this-documentation-is-for"></a>

## Who this documentation is for

This guide is written for three roles, each with a different need:

- **Shop managers** who decide which shops show the price pill and want to know how the toggle behaves.
- **Cashiers and operations staff** who interact with the POS daily and need to understand what they see on the screen.
- **IT administrators and Odoo integrators** who install the module, configure pricelists, and troubleshoot issues.

You don't need any Python or web-development knowledge to follow this guide. Where commands appear (for installation), they're spelled out step by step.

<a id="quick-start"></a>

## Quick start

1. Copy the `sdlc_pos_product_price` folder into your Odoo addons directory and restart Odoo.
2. Open **Apps**, click **Update Apps List**, search for *POS Product Price on Card*, and click **Install**.
3. Open any POS shop and start a session. Green price pills appear on every product card.
4. *(Optional)* Create a 20% pricelist in **Point of Sale → Configuration → Pricelists**, attach it to a shop, and reopen the session - every card now shows strike-through originals and a `-X%` badge.

Full walkthrough: [Installation and Setup](../../getting-started/19.0/getting-started/setup.md).

<a id="whats-in-this-documentation"></a>

## What's in this documentation

- [**Installation and Setup**](../../getting-started/19.0/getting-started/setup.md) - install the module and verify it loaded correctly.
- [**The Per-Shop Toggle**](../../configuration/19.0/configuration/per-shop-toggle.md) - find the setting, understand scope, and know when changes take effect.
- [**Using the Module in the POS**](../../usage/19.0/usage/using-in-pos.md) - what the cashier sees, plus a deep-dive into each visual element.
- [**Discount Visuals with Pricelists**](../../usage/19.0/usage/discount-visuals.md) - step-by-step pricelist setup to trigger the strike-through and savings badge.
- [**FAQ and Troubleshooting**](../../reference/19.0/reference/faq.md) - common issues, edge cases, and support contact info.

---

Source: [POS Product Price on Card - Odoo 19 POS Extension](https://docs.sdlccorp.com/docs/19.0/pos-product-price-card/intro/)
