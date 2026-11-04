# POS Product Price on Card - Using the Module in the POS

Once the module is installed and the shop's toggle is **ON**, the cashier uses Odoo POS exactly as before. **No new buttons. No new menus.** The module simply makes information that was previously hidden, visible.

<a id="opening-the-pos"></a>

## Opening the POS

1. From the Odoo backend, navigate to **Point of Sale** (top menu).
2. On the dashboard, find the shop you want to open.
3. Click **Open POS** (or **Continue Selling** if a session is already open).
4. If prompted, enter the opening cash balance and confirm.

The POS interface loads. The product grid is the central area showing every product as a card; the module's changes are visible on every card.

<a id="what-the-cashier-sees"></a>

## What the cashier sees

The product grid now shows the **selling price on every card**, formatted in the shop's currency. The price is the one the customer will actually be charged, including any pricelist discounts. The cashier never has to tap a product just to see its price.

When a customer is added to the order and that customer has a pricelist that lowers the price (loyalty member, wholesaler, happy-hour pricing), **every card in the grid recalculates instantly**:

- The original price appears next to the discounted price with a **line through it**.
- A small red **percent-off badge** animates into the top-left corner of each card.
- The pill itself shows the new (lower) price.

Discount calculator on demand

The cashier can use this as a quick discount calculator. Pick a customer with a 20% pricelist, glance at the grid, and instantly see the discounted price on every product without ringing anything up.

<a id="feature-deep-dive"></a>

## Feature deep-dive

The module renders three distinct visual elements on each product card. They're all read-only - clicking them adds the product to the cart, same as clicking the card itself.

<a id="1-the-green-price-pill"></a>

### 1. The green price pill

The pill renders under each product's name. Specs:

- **Shape**: rounded pill with soft drop-shadow.
- **Background**: green gradient (`#0f6c2f` → `#15803d`).
- **Text**: white, bold, in the shop's currency format (e.g. `$ 295.00`).
- **Value**: the current selling price for **this customer**, in **this shop's** currency, including any pricelist discount that applies.

On hover, the pill subtly lifts and brightens - a small visual cue that the card is interactive. Hovering does *not* change the price.

<a id="2-the-strike-through-original-price"></a>

### 2. The strike-through original price

When the current order is on a pricelist that lowers the price, the module reads the product's **base list price** from the product master and renders it next to the pill with a line through it.

- **Color**: muted grey, so it doesn't visually compete with the green pill.
- **Visibility**: hidden automatically when there is no discount, so non-discounted cards stay clean.

If the pricelist *doesn't* lower the price for a particular product (e.g. a category exclusion), the strike-through is also hidden for that card - only cards where the price actually changed get the marker.

<a id="3-the-animated--x-savings-badge"></a>

### 3. The animated `-X%` savings badge

The badge is a small red rounded pill placed in the top-left corner of the card.

- **Text**: discount as a negative percentage, e.g. `-20%`.
- **Animation**: on first render, it scales up with a quick keyframe animation, drawing the eye to the savings.
- **Computation**: `round((1 - current / original) * 100)`. The display value is always a whole-percent integer.

The badge has the same hide-when-no-discount logic as the strike-through.

<a id="reaction-to-pricelist-switches"></a>

## Reaction to pricelist switches

The product grid is reactive. When you:

- **Select a customer** with a different default pricelist, OR
- **Manually switch the pricelist** from the order's pricelist selector,

…every visible card recalculates **instantly**. No page reload. The pill, strike-through and badge all update together so the cashier always sees what the customer will pay.

<a id="what-the-cashier-does-not-see"></a>

## What the cashier does *not* see

- **Margin** - the module shows the selling price, not the cost. Cost / margin is not a POS concept and is not surfaced by this module.
- **Per-line pricing breakdown** - that's still visible in the cart on the right side of the POS, as in standard Odoo. The grid only shows the headline price.
- **Tax inclusion** - the price respects the shop's default tax-display mode (inclusive vs. exclusive). The toggle behaves the same way as the cart's price display.

<a id="combos-and-variants"></a>

## Combos and variants

- **Variants** are resolved through the **same pricelist logic** Odoo's cart uses. Each variant card shows its own price.
- **Combos** show their base price; combo extras are added when the product is rung up, as in standard Odoo.

<a id="refresh-and-troubleshooting"></a>

## Refresh and troubleshooting

If you've just changed the toggle or installed an update and the cashier doesn't see the expected behaviour, three things to try in order:

1. **Hard-refresh the POS tab** (`Ctrl+Shift+R` on Windows/Linux, `Cmd+Shift+R` on macOS) to bust the browser's asset cache.
2. **Close and reopen the POS session** - many POS settings only load at session start.
3. **Restart the Odoo server** if the JavaScript still looks stale.

For more involved fixes, see [FAQ and Troubleshooting](../../../reference/current/reference/faq.md).

<a id="next-steps"></a>

## Next steps

- Trigger the strike-through and badge by setting up a pricelist: [Discount Visuals with Pricelists](discount-visuals.md).

---

Source: [POS Product Price on Card - Using the Module in the POS](https://docs.sdlccorp.com/docs/pos-product-price-card/usage/using-in-pos/)
