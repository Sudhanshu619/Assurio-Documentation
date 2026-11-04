# PrestaShop Connector - Instance Configuration

Navigate to **PrestaShop > Configuration** to manage your store connections.

<a id="creating-a-new-instance"></a>

## Creating a New Instance

Click **Create** and fill in the following fields:

![Configuration Dashboard](https://docs.sdlccorp.com/assets/images/PrestaShop-Configuration-1-b832e2f569209a55db9fd5784122567a.webp)

| Field | Description | Example |
| --- | --- | --- |
| **Configuration Name** | A friendly name for this store | My Europe Store |
| **Company** | Odoo company this store belongs to | My Company |
| **Store URL** | Your PrestaShop store URL | `https://mystore.com` |
| **Webservice URL** | Custom API endpoint (optional) | `https://mystore.com/api` |
| **API Key** | PrestaShop webservice API key | ABCD1234... |

![Configuration Form](https://docs.sdlccorp.com/assets/images/PrestaShop-Configuration-2-bb3bbb2964222dcc337f0f1152e79a11.webp)

The configuration form shows tabs for all connector modules: **Store Product**, **Store Categories**, **Store Customers**, **Store Brands**, **Store Suppliers**, **Store Inventory**, **Store Attributes**.

<a id="testing-the-connection"></a>

## Testing the Connection

Click the **Test Connection** button in the form header. If successful, the status will change to **Connected** (green) and the PrestaShop version will be displayed. If it fails, check the **Last Error** field at the bottom for details.

<a id="sync-buttons"></a>

## Sync Buttons

The configuration form header contains individual sync buttons:

| Button | Action |
| --- | --- |
| **Sync Products** | Import all products from PrestaShop |
| **Sync Categories** | Import product categories |
| **Sync Customers** | Import customer records |
| **Sync Brands** | Import manufacturers/brands |
| **Sync Suppliers** | Import supplier records |
| **Sync Carriers** | Import shipping carriers |
| **Sync Attributes** | Import product attributes and values |
| **Sync Features** | Import product features and values |
| **Sync Taxes** | Import tax rules and rates |

<a id="next-steps"></a>

## Next Steps

- [View the dashboard >](dashboard.md)
- [Understand data sync flow >](data-sync.md)
- [Set up field mapping >](field-mapping.md)

<a id="need-help"></a>

## Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/)

---

Source: [PrestaShop Connector - Instance Configuration](https://docs.sdlccorp.com/docs/19.0/prestashop-odoo-connector/configuration/instance-setup/)
