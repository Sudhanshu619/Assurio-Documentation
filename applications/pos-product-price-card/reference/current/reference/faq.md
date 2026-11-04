# POS Product Price on Card - FAQ and Troubleshooting

This page collects the issues that show up most often and the questions we get most often. For deeper coverage of a specific topic, follow the links into the rest of the docs.

<a id="troubleshooting"></a>

## Troubleshooting

<a id="the-green-pills-are-not-appearing"></a>

### The green pills are not appearing

Three common causes, in order of likelihood:

1. **The toggle is OFF for this shop.** Check **Configuration → Point of Sale → (your shop) → SDLC Product Price Display** and turn **Show Product Price on Card** ON. Close and reopen the session for the change to apply. See [The Per-Shop Toggle](../../../configuration/current/configuration/per-shop-toggle.md).
2. **The POS browser is showing a cached asset bundle.** Hard-refresh the POS tab with `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (macOS).
3. **The Odoo server still has the old code in memory.** Restart Odoo, or run:

   ```
   ./odoo-bin -c your_odoo.conf -u sdlc_pos_product_price --stop-after-init
   ```

<a id="the-discount-badge-is-not-appearing-even-though-i-applied-a-pricelist"></a>

### The discount badge is not appearing even though I applied a pricelist

- **Confirm the pricelist actually lowers the price for this product.** Some pricelists use a *Fixed Price* rule or only target specific products / categories. Open the pricelist and review its rules under **Point of Sale → Configuration → Pricelists**.
- **Confirm *Flexible Pricelists* is enabled** in the global POS settings (**Point of Sale → Configuration → Settings → Pricing**).
- **Close the session and reopen it.** Pricelist changes do not always propagate to a session that is already running - the POS reads its pricelist configuration at session start.

See the full walkthrough at [Discount Visuals with Pricelists](../../../usage/current/usage/discount-visuals.md).

<a id="i-changed-the-toggle-but-nothing-changed-in-the-pos"></a>

### I changed the toggle but nothing changed in the POS

POS configurations are loaded **when a session opens**. If a session is already running, the cashier must close it and open a new one for the change to take effect. There is no way to live-reload this setting in a running session.

<a id="the-savings-badge-shows-a-strange-percent-like-0-or-nan"></a>

### The savings badge shows a strange percent like `0%` or `NaN%`

This indicates an edge case where the product's **base list price is zero** (or missing). Check the product's **Sales Price** field in **Products → Products**. Set a non-zero price, then close and re-open the POS session.

<a id="a-product-card-shows-the-original-price-as-the-discounted-price"></a>

### A product card shows the original price as the discounted price

Confirm that the **Sales Price** on the product master is higher than the pricelist-resolved price. If they happen to be equal (e.g. a fixed-price rule that matches the list price exactly), the module correctly hides the strike-through - there's no discount to show.

<a id="the-module-is-installed-but-no-sdlc-product-price-display-section-in-the-shop-config"></a>

### The module is installed but no `SDLC Product Price Display` section in the shop config

The module's form-view inheritance didn't load. Try:

1. Restart Odoo.
2. Upgrade the module: `./odoo-bin -c your_odoo.conf -u sdlc_pos_product_price --stop-after-init`.
3. Check the Odoo server log for errors mentioning `sdlc_pos_product_price` - share those with support if the upgrade doesn't fix it.

<a id="after-upgrade-the-pos-shows-a-blank-product-grid"></a>

### After upgrade, the POS shows a blank product grid

Almost always a stale browser cache combined with a new asset bundle. Hard-refresh the POS tab (`Ctrl+Shift+R`) once. If that doesn't fix it, also restart Odoo to force a fresh asset bundle build.

<a id="frequently-asked-questions"></a>

## Frequently asked questions

<a id="does-this-module-change-any-prices"></a>

### Does this module change any prices?

**No.** The module only **reads** existing prices and renders them on the cards. It uses the same pricing resolver Odoo uses internally for the cart, so the pill, strike-through and badge always reflect what the customer would actually pay.

<a id="will-this-module-slow-down-my-pos"></a>

### Will this module slow down my POS?

**No measurable impact.** The price computation is the same one Odoo already runs when a product is added to the cart - the module just runs it earlier, per visible card. With typical grids of 20 to 80 products, the cost is negligible. Bigger grids (200+ products) may add a few milliseconds at session-load time; once loaded, scrolling and rendering are unchanged.

<a id="will-it-conflict-with-other-pos-extensions"></a>

### Will it conflict with other POS extensions?

**No.** The module uses Odoo's official `patch()` API on the `ProductCard` component and inherits the XML template via `t-inherit`. Both are designed to allow multiple extensions to coexist. If you do see a conflict with another extension, share the other module's name with support and we'll investigate compatibility.

<a id="does-it-work-with-product-variants-and-combos"></a>

### Does it work with product variants and combos?

- **Variants** - yes. Variants are resolved through the same pricelist logic Odoo's cart uses, so each variant card shows its own price.
- **Combos** - combo products show their **base price**; combo extras are added when the product is rung up, as in standard Odoo.

<a id="what-happens-when-i-uninstall-the-module"></a>

### What happens when I uninstall the module?

The boolean column on `pos.config` is dropped, the JavaScript stops loading from the asset bundle, and the form-view inheritance is removed. The POS reverts to vanilla Odoo. **No transactional data is lost** - orders, pricelists, products, sessions, reports are all unaffected.

<a id="can-i-customize-the-colors-of-the-pill-or-badge"></a>

### Can I customize the colors of the pill or badge?

**Yes.** All visuals live in a single SCSS file (`static/src/scss/product_card_price.scss`) with clearly named classes. Edit the gradients, shadows and animations to match your brand. After editing, run:

```
./odoo-bin -c your_odoo.conf -u sdlc_pos_product_price --stop-after-init
```

…to rebuild the asset bundle, then hard-refresh the POS.

<a id="does-the-toggle-default-to-on-or-off"></a>

### Does the toggle default to ON or OFF?

**ON.** Every existing and new shop has the price pill visible by default. Flip it OFF on shops where you prefer image-only cards.

<a id="what-versions-of-odoo-does-this-support"></a>

### What versions of Odoo does this support?

This release is built specifically for **Odoo 19.0**. The frontend APIs it uses (`patch()`, the `ProductCard` component, the `getPrice` resolver) all changed between Odoo 17 and Odoo 18/19, so the module is **not backwards-compatible** with Odoo 17.

For Odoo 18 compatibility, contact SDLC Corp - a backport may be available.

<a id="will-the-discount-visuals-respect-a-coupon-or-loyalty-program-discount"></a>

### Will the discount visuals respect a *Coupon* or *Loyalty Program* discount?

The module renders discounts that come from **pricelists**. Coupon codes and Loyalty Program rewards are applied at the cart level (as line discounts), not the price level, so they appear on the cart line - not on the grid pill. This is by design: the grid is a pre-cart view and doesn't know which coupons the customer will redeem.

<a id="can-the-cashier-turn-the-pill-onoff-from-inside-the-pos"></a>

### Can the cashier turn the pill on/off from inside the POS?

No - the toggle is per-shop and lives in the backend. This is deliberate: the visual style should be consistent within a single shop session. If you need cashier-level control, contact SDLC Corp for a customization.

<a id="does-the-price-respect-multi-currency"></a>

### Does the price respect multi-currency?

Yes. The pill is formatted in the **shop's currency**, using Odoo's standard currency formatting (separator, decimals, position of the symbol). Multi-currency pricelists work normally.

<a id="does-the-module-add-any-dependencies-cron-jobs-or-external-services"></a>

### Does the module add any dependencies, cron jobs, or external services?

No. It depends only on `point_of_sale` (bundled with Odoo). No cron jobs are added; no external network calls are made; no third-party libraries are bundled.

<a id="module-reference"></a>

## Module reference

| Field | Value |
| --- | --- |
| **Module name** | `sdlc_pos_product_price` |
| **Display name** | POS Product Price on Card |
| **Version** | 19.0.1.0.0 |
| **Odoo version** | 19.0 (Community & Enterprise) |
| **License** | LGPL-3 / OPL-1 |
| **Dependencies** | `point_of_sale` |
| **Models extended** | `pos.config` (one boolean field added) |
| **Views inherited** | POS shop configuration form |
| **Frontend** | One OWL component patch + one SCSS file |

<a id="support-and-contact"></a>

## Support and contact

For questions, customization requests, translations or support contracts, please contact SDLC Corp directly.

| Channel | Details |
| --- | --- |
| **Publisher** | SDLC Corp |
| **Website** | [sdlccorp.com](https://sdlccorp.com) |
| **Sales / support email** | [sales@sdlccorp.com](mailto:sales@sdlccorp.com) |
| **Contact form** | [Reach SDLC Corp Support](https://sdlccorp.com/contact-us/) |
| **License** | LGPL-3 / OPL-1 |

Average response time on support requests is **one business day**. For installation and configuration help, mentioning your Odoo version and the steps you've already followed will help us reply with a precise answer.

---

Source: [POS Product Price on Card - FAQ and Troubleshooting](https://docs.sdlccorp.com/docs/pos-product-price-card/reference/faq/)
