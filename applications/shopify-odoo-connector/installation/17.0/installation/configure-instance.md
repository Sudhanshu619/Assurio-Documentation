# Configure Your Odoo Instance


<a id="field-reference"></a>

## Field reference

The Instance Configuration form has a few sections of settings; the most important are at the top:

- **Store URL / API credentials** - what you generated under [Generate API Keys](generate-api-keys.md).
- **Default warehouse** - every Shopify location maps here unless you set up per-location mapping later.
- **Default pricelist / currency** - used for newly-imported customers and orders.
- **Behaviour defaults** - what happens to imported customers (match by email vs always create), what happens to orders (quote vs confirmed), how products map.

Defaults are sensible for a single-store setup. Multi-store or B2B installs typically tune them.

After entering your Shopify credentials, configure the sync settings for your Odoo instance.

<a id="basic-configuration"></a>

## Basic Configuration

Navigate to **Shopify → Configuration → Shopify Instances** and open your instance.

![Shopify Instance configuration form with sync buttons](https://docs.sdlccorp.com/assets/images/shopify-instance-2-f033328e59a1cba24c9c2207d89845de.webp)

<a id="company--warehouse"></a>

### Company & Warehouse

| Setting | Description |
| --- | --- |
| **Company** | The Odoo company to sync data into |
| **Warehouse** | Default warehouse for inventory operations |
| **Sales Team** | Sales team assigned to Shopify orders |

<a id="customer-settings"></a>

### Customer Settings

| Setting | Description |
| --- | --- |
| **Default Customer** | Fallback customer for guest checkouts |
| **Customer Import** | Auto-create customers on order import |

<a id="product-settings"></a>

### Product Settings

| Setting | Description |
| --- | --- |
| **Product Type** | Default product type (Storable/Consumable) |
| **UoM** | Default unit of measure |

<a id="saving-the-configuration"></a>

## Saving the Configuration

Click **Save** after configuring all fields. The connector will validate the connection
and display a green status indicator if everything is set up correctly.

<a id="next-step"></a>

## Next Step

Proceed to [Webhook Configuration](../../../configuration/17.0/configuration/webhook-configuration.md) to enable real-time sync.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Configure Your Odoo Instance](https://docs.sdlccorp.com/docs/17.0/shopify-odoo-connector/installation/configure-instance/)
