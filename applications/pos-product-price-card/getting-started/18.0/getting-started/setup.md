# POS Product Price on Card - Installation and Setup

The module installs like any other Odoo addon. It depends only on `point_of_sale`, which is bundled with every Odoo installation, so **no additional dependencies are required**.

<a id="prerequisites"></a>

## Prerequisites

- **Odoo 19** (Community or Enterprise edition).
- The **Point of Sale** module installed and at least one POS shop configured.
- Filesystem or shell access to the Odoo server to drop in the module folder.
- The module package: `sdlc_pos_product_price.zip` (or the unzipped folder).

<a id="installation-steps"></a>

## Installation steps

<a id="step-1---place-the-module-folder-in-your-addons-path"></a>

### Step 1 - Place the module folder in your addons path

Copy the `sdlc_pos_product_price` folder into your Odoo addons directory (commonly `/mnt/extra-addons/` for Docker, or the path set as `addons_path` in your `odoo.conf`).

```
/mnt/extra-addons/
└── sdlc_pos_product_price/
    ├── __manifest__.py
    ├── models/
    ├── views/
    └── static/
```

The folder name must remain exactly **`sdlc_pos_product_price`** for Odoo to detect it correctly.

<a id="step-2---restart-odoo"></a>

### Step 2 - Restart Odoo

Restart your Odoo service so the new addon is picked up. On a server with a systemd service:

```
sudo systemctl restart odoo
```

On a development server you can also pre-load the module before normal startup:

```
./odoo-bin -c your_odoo.conf -u sdlc_pos_product_price --stop-after-init
```

Then start Odoo normally.

<a id="step-3---refresh-the-apps-list"></a>

### Step 3 - Refresh the apps list

In the Odoo backend:

1. Go to **Apps**.
2. Click **Update Apps List** (requires Developer Mode).
3. Confirm with **Update**.

If you don't see the **Update Apps List** option, enable Developer Mode first under **Settings → Developer Tools → Activate Developer Mode**.

<a id="step-4---install-the-module"></a>

### Step 4 - Install the module

1. In the **Apps** search bar, clear the "Apps" filter and type **"POS Product Price on Card"**.
2. Click the **Install** button on the module card.

Installation completes in a few seconds. Behind the scenes, Odoo:

- Adds one boolean column (`show_product_price_on_card`) to the `pos.config` model.
- Loads the module's JavaScript and SCSS into the Point of Sale asset bundle.
- Inherits the POS shop configuration view to add the **SDLC Product Price Display** section.

<a id="step-5---verify-the-install"></a>

### Step 5 - Verify the install

Open **Point of Sale → Configuration → Point of Sale** and click any existing shop. Scroll to the bottom of the form. You should see a section titled **SDLC Product Price Display** with the **Show Product Price on Card** toggle set to ON.

If you see the section, the module is loaded correctly.

<a id="default-behaviour-after-install"></a>

## Default behaviour after install

Every existing and newly created Point-of-Sale shop has the **Show Product Price on Card** toggle set to **ON** by default. The next POS session opened on any shop will show the green price pill immediately.

To start a fresh session:

1. Go to **Point of Sale** (top-level menu).
2. Find the shop on the dashboard.
3. Click **Open POS** (or **Continue Selling** if a session is already running).
4. If prompted, enter the opening cash balance and confirm.

The product grid now shows the selling price on every card. You're done.

<a id="upgrading-an-existing-install"></a>

## Upgrading an existing install

When a new version of the module is released, drop the new folder over the old one and run:

```
./odoo-bin -c your_odoo.conf -u sdlc_pos_product_price --stop-after-init
```

This re-runs the module's `__manifest__.py` data, refreshes the asset bundle, and applies any schema changes. POS sessions started after the upgrade will pick up the new code.

<a id="uninstalling"></a>

## Uninstalling

To remove the module entirely, go to **Apps**, find the module card, click the kebab menu, and choose **Uninstall**.

On uninstall, Odoo:

- Drops the `show_product_price_on_card` column from `pos.config`.
- Removes the module's JavaScript and SCSS from the POS asset bundle.
- Removes the form-view inheritance.

The POS reverts to vanilla Odoo behaviour with **no data loss** - no orders, pricelists, products or sessions are affected.

<a id="next-steps"></a>

## Next steps

- Toggle the price pill per shop: [The Per-Shop Toggle](../../../configuration/18.0/configuration/per-shop-toggle.md).
- See what the cashier sees: [Using the Module in the POS](../../../usage/18.0/usage/using-in-pos.md).
- Trigger the discount visuals: [Discount Visuals with Pricelists](../../../usage/18.0/usage/discount-visuals.md).

---

Source: [POS Product Price on Card - Installation and Setup](https://docs.sdlccorp.com/docs/18.0/pos-product-price-card/getting-started/setup/)
