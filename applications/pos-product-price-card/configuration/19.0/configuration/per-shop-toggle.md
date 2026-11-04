# POS Product Price on Card - Per-Shop Toggle

The module adds a **single setting** to each Point-of-Sale shop's configuration form. There is no other configuration to perform.

<a id="where-to-find-the-toggle"></a>

## Where to find the toggle

1. Open the Odoo backend.
2. Navigate to **Point of Sale → Configuration → Point of Sale**.
3. Click the shop whose behaviour you want to change.
4. Scroll to the bottom of the form. You'll see a section titled **SDLC Product Price Display** with one switch:
   - **Show Product Price on Card** *(boolean - ON by default)*

This section is added by the module's inherited view. If you don't see it, the module isn't installed correctly - re-check [Installation and Setup](../../../getting-started/19.0/getting-started/setup.md).

<a id="how-the-toggle-behaves"></a>

## How the toggle behaves

| Setting | Effect |
| --- | --- |
| **ON (default)** | The product grid in this shop shows the green price pill on every card, with strike-through original price and `-X%` savings badge when a pricelist discount applies. |
| **OFF** | The product grid in this shop reverts to standard Odoo behaviour. No price is shown on any card. The module is still installed; it's just inactive for this shop. |

<a id="scope-each-shop-is-independent"></a>

## Scope: each shop is independent

Each Point-of-Sale shop has its **own independent toggle**. Flipping it on one shop does not affect any other shop - so you can show price pills in your high-street store where customers see the screen, and hide them in a stockroom POS where they're noise.

| Shop | Toggle | Result |
| --- | --- | --- |
| Furniture Showroom | ON | Pills visible - customer-facing display |
| Stockroom Counter | OFF | Image-only cards - fast scan for staff |
| Bakery POS | ON | Pills + discounts for happy-hour pricing |

<a id="when-changes-take-effect"></a>

## When changes take effect

Changes take effect **the next time a cashier opens a fresh POS session** on that shop. POS configurations are loaded into the browser at session start, so a session that's already running keeps using whatever value was active when it opened.

To apply a toggle change to a shop with an active session:

1. The cashier closes the current session from the POS interface (**Close** in the top-right menu, then confirm the cash count).
2. Back in the Odoo backend, you flip the toggle to its new value and **Save**.
3. The cashier opens a new session - the new value is now active.

Sessions don't live-reload

If you change the toggle while a POS session is open, the running session **does not automatically pick up the new value**. The cashier must close the current session and open a new one for the change to apply. There is no in-session refresh button for this setting.

<a id="common-patterns"></a>

## Common patterns

<a id="roll-out-to-all-shops-at-once"></a>

### Roll out to all shops at once

By default every shop has the toggle ON after install. If you've turned it off on some shops and want to roll it back ON site-wide:

1. From the shop list (**Point of Sale → Configuration → Point of Sale**), click the column-toggle icon and add **Show Product Price on Card** as a list column.
2. Sort by that column to see which shops are off.
3. Click into each one, flip the toggle, save.

For very large fleets, an admin can run the equivalent update directly:

```
./odoo-bin shell -c your_odoo.conf
>>> env['pos.config'].search([]).write({'show_product_price_on_card': True})
>>> env.cr.commit()
```

<a id="stagger-a-rollout-for-testing"></a>

### Stagger a rollout for testing

Turn the toggle ON in one pilot shop first. Watch the cashier flow for a week. If the team is happy, enable the remaining shops. If not, you can leave the pilot shop ON for QA while keeping production shops OFF - no separate install/uninstall needed.

<a id="hide-in-a-customer-facing-display-where-margins-are-visible"></a>

### Hide in a customer-facing display where margins are visible

Some retailers don't want customers to see *all* prices at a glance (e.g. on a screen where multiple high-ticket items are visible). Turn the toggle OFF for those shops. The cashier still sees prices in the cart and the receipt; only the grid hides them.

<a id="what-the-toggle-does-not-affect"></a>

## What the toggle does **not** affect

- **Existing orders, sessions and reports** - these are unaffected. Toggling never touches transactional data.
- **The base list price or pricelists** - those are configured under Products and Pricelists, not by this toggle.
- **Other shops** - toggling is strictly per-`pos.config`.

<a id="next-steps"></a>

## Next steps

- See the visual changes in action: [Using the Module in the POS](../../../usage/19.0/usage/using-in-pos.md).
- Set up a discount pricelist so the strike-through and savings badge appear: [Discount Visuals with Pricelists](../../../usage/19.0/usage/discount-visuals.md).

---

Source: [POS Product Price on Card - Per-Shop Toggle](https://docs.sdlccorp.com/docs/19.0/pos-product-price-card/configuration/per-shop-toggle/)
