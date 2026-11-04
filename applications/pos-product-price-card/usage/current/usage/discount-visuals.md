# POS Product Price on Card - Discount Visuals with Pricelists

The strike-through original price and the animated savings badge **only appear when there is a price difference** between the product's base list price and the current pricelist-resolved price. To see them, you need to either configure a discount pricelist or already have one in place.

This page walks through a clean, repeatable setup using a 20%-off loyalty pricelist as the example. The same pattern applies to wholesale tiers, happy-hour promotions, or any other percentage discount.

<a id="how-the-visuals-are-triggered"></a>

## How the visuals are triggered

The module subscribes to the same pricing resolver Odoo POS uses internally. For every visible product card, it computes:

```
original = product.list_price  (the product master's Sales Price)
current  = pricelist.resolve(product, customer, qty, date)
```

- If `current < original`, the module renders the strike-through original next to the green pill and shows a `-X%` badge in the corner.
- If `current == original`, only the green pill is shown.
- If `current > original` (extremely rare - a pricelist that *adds* a markup), the strike-through is hidden - the module never shows a "negative discount".

<a id="step-by-step-set-up-a-20-loyalty-pricelist"></a>

## Step-by-step: set up a 20% loyalty pricelist

<a id="step-1---create-a-new-pricelist"></a>

### Step 1 - Create a new pricelist

1. Go to **Point of Sale → Configuration → Pricelists**.
2. Click **New**.
3. Name it **"Loyalty 20% Off"**.
4. Leave the currency as the company default (or pick one if you run multi-currency).
5. **Save**.

<a id="step-2---add-a-discount-rule"></a>

### Step 2 - Add a discount rule

In the pricelist's **Rules** tab, click **Add a line** and fill in:

| Field | Value |
| --- | --- |
| **Applicable On** | All Products |
| **Computation** | Percentage (Discount) |
| **Discount %** | `20` |
| **Date Start / Date End** | *(leave blank for no expiration)* |

Click **Save & Close** to add the rule, then **Save** the pricelist.

<a id="step-3---enable-pricelists-on-the-shop"></a>

### Step 3 - Enable pricelists on the shop

1. Go to **Point of Sale → Configuration → Settings**.
2. Find the **Pricing** section.
3. Tick **Flexible Pricelists**.
4. **Save**.

Flexible Pricelists is what tells the POS to honour custom pricelists at runtime. Without it, the shop only uses its default pricelist and won't show the loyalty discount.

<a id="step-4---add-the-pricelist-to-the-shops-available-list"></a>

### Step 4 - Add the pricelist to the shop's available list

1. Open **Point of Sale → Configuration → Point of Sale**.
2. Click the shop where you want the discount available.
3. In the **Available Pricelists** field (under the Pricing section), add **"Loyalty 20% Off"**.
4. *(Optional)* Set it as the **Default Pricelist** so every new order starts with it applied. Otherwise the cashier will switch to it manually per order.
5. **Save**.

<a id="step-5---open-a-new-pos-session"></a>

### Step 5 - Open a new POS session

If a session is already open on this shop, **close it first** - POS configs (including pricelist settings) are loaded at session start.

Then open a fresh session from the POS dashboard. The product grid now shows three module-rendered elements on every card:

1. The green **discounted price pill** (e.g. `$ 236.00` instead of `$ 295.00`).
2. The **crossed-out original price** in muted grey next to the pill.
3. The red **`-20%` savings badge** in the top-left corner of the card.

If you set the pricelist as the default, every order starts with these visible immediately. If you didn't, the cashier switches the pricelist from the order's pricelist selector - and the entire grid recalculates instantly.

<a id="variants-and-special-pricelist-rules"></a>

## Variants and special pricelist rules

The module honours **every** Odoo pricelist rule type. A few patterns to be aware of:

- **Per-category rules** - e.g. "20% off all Chairs, full price on Desks". Only the Chairs cards show the strike-through and badge; Desks show the plain green pill.
- **Per-product rules** - only the specific products in the rule are discounted.
- **Quantity-based tiers** - the discount applies based on a default `qty=1`. Larger-quantity tiers won't show on the grid (because the cashier hasn't yet added a quantity); they kick in once the line is in the cart.
- **Fixed price rules** - the strike-through shows the difference between list price and fixed price. If the fixed price equals the list price for a product, the strike-through is hidden.
- **Other pricelists (parent fallback)** - Odoo lets one pricelist "inherit" from another. The module resolves the final price exactly as the cart does.

<a id="multiple-pricelists-in-one-session"></a>

## Multiple pricelists in one session

The cashier can switch pricelists per order:

- Order #1 - Walk-in customer → Default pricelist → no discount visible on cards.
- Order #2 - Loyalty member → Loyalty 20% Off → strike-through + badge on every card.
- Order #3 - Wholesale account → Wholesale Tier → different discount, different badge `-X%`.

Each switch is instant; no reload, no flicker.

<a id="tax-handling"></a>

## Tax handling

Discount visuals respect the shop's **tax display mode**:

- **Tax included** - both the pill and the strike-through show tax-inclusive prices. The `-X%` is based on tax-inclusive amounts.
- **Tax excluded** - both show tax-exclusive prices.

This mirrors how the cart and receipt display prices, so the badge always reflects what the customer will see at checkout.

<a id="troubleshooting-discount-visuals"></a>

## Troubleshooting discount visuals

If you've set everything up but the strike-through and badge aren't appearing:

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Plain green pill only, no strike-through | The pricelist isn't actually selected on the order, or doesn't lower the price for this product | Open the order's pricelist selector and confirm; review the pricelist's rules in the backend |
| Strike-through visible but no `-X%` badge | Edge case where the discount rounds to 0% (very small absolute difference) | Either expected, or raise the discount % |
| All cards show `-100%` or weird values | Product's Sales Price is `0` | Set a non-zero Sales Price on the product master |
| Nothing changed after editing the pricelist | The session is using the old pricelist data loaded at session start | Close and reopen the POS session |

See [FAQ and Troubleshooting](../../../reference/current/reference/faq.md) for more.

<a id="next-steps"></a>

## Next steps

- All cosmetic settings (colors, shadows, animations) live in `static/src/scss/product_card_price.scss` - see the FAQ for customization notes.
- For routine cashier flow without discounts, see [Using the Module in the POS](using-in-pos.md).

---

Source: [POS Product Price on Card - Discount Visuals with Pricelists](https://docs.sdlccorp.com/docs/pos-product-price-card/usage/discount-visuals/)
