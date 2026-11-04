# Installation & Requirements


<a id="after-installation"></a>

## After installation

Once the SDLC PrestaShop Odoo Connector is installed and your store's API credentials are configured, the recommended first-week sequence is:

1. **[Instance Setup](../../../configuration/current/configuration/instance-setup.md)** - store URL, API key, test connection.
2. **[Field Mapping](../../../configuration/current/configuration/field-mapping.md)** - load the defaults, customize only what you need.
3. **[Data Sync](../../../configuration/current/configuration/data-sync.md)** - pick the entity to pull first (usually products), run a manual sync, review the [Sync Reports](../../../reference/current/reference/sync-reports.md).
4. **[Auto-Sync](../../../configuration/current/configuration/auto-sync.md)** - enable scheduled jobs only after the manual sync round-trips cleanly.

<a id="prerequisites"></a>

## Prerequisites

- Odoo 18 Community or Enterprise Edition
- Python 3.10+
- PrestaShop 1.7+ or 8.x with Webservice API enabled
- PrestaShop API Key with full permissions
- Odoo modules: `base`, `product`, `mail`, `account`

<a id="installation-steps"></a>

## Installation Steps

**Step 1:** Copy the `sdlc_prestashop_connector` folder into your Odoo custom addons directory.

**Step 2:** Restart the Odoo server with `--update=sdlc_prestashop_connector` or use the Apps menu.

**Step 3:** Go to **Apps**, remove the "Apps" filter, search for "PrestaShop", and click **Install**.

**Step 4:** The **PrestaShop** menu will appear in the top navigation bar.

<a id="prestashop-api-setup"></a>

## PrestaShop API Setup

In your PrestaShop admin panel:

1. Go to **Advanced Parameters > Webservice**
2. Click **Add New Webservice Key**
3. Generate or enter an API key
4. Set permissions: check **all resources** with GET, POST, PUT, DELETE
5. Enable the webservice and save
6. Copy the API key for use in Odoo

warning

The API key must have full permissions on all resources. Missing permissions will cause sync failures for the affected data types.

<a id="next-steps"></a>

## Next Steps

- [Configure your PrestaShop instance >](../../../configuration/current/configuration/instance-setup.md)
- [Explore the dashboard >](../../../configuration/current/configuration/dashboard.md)

<a id="need-help"></a>

## Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/)

---

Source: [Installation & Requirements](https://docs.sdlccorp.com/docs/prestashop-odoo-connector/installation/getting-started/)
