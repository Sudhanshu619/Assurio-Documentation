# ShipStation Connector - Installation and Setup


<a id="prerequisites"></a>

## Prerequisites

- Odoo 18 Community or Enterprise edition
- Python 3.10+
- Active ShipStation account with API access
- Required Odoo modules: base, web, sale_management, stock, delivery, contacts

<a id="installation-steps"></a>

## Installation Steps

1. Copy the `shipstation_connector` folder to your Odoo custom addons directory
2. Restart the Odoo server
3. Go to **Apps**, remove the 'Apps' filter, search for 'ShipStation', and click **Install**
4. After installation, the **ShipStation** menu appears in the navigation

<a id="instance-configuration"></a>

## Instance Configuration

Navigate to **ShipStation > Instances** to configure your account connection.

![Instance Listing](https://docs.sdlccorp.com/assets/images/instance-listing-4ba2f4094c1d618e3999c5ff0edc4d27.webp)

Click **New** and fill in:

| Field | Required | Description |
| --- | --- | --- |
| **Name** | Yes | Descriptive name (e.g., "US Warehouse") |
| **API Key** | Yes | Your ShipStation API Key (from Account > API Settings) |
| **API Secret** | Yes | Your ShipStation API Secret |
| **API URL** | No | ShipStation API endpoint (default value pre-filled) |
| **Active** | No | Enable/disable this instance |
| **Company** | Yes | The Odoo company this instance belongs to |

![Instance Form](https://docs.sdlccorp.com/assets/images/instance-data-d6dc898071d36c8bf8ebe54ac1977f5e.webp)

Click **Test Connection** to verify the API credentials. A green 'Connected' status confirms success.

<a id="sync-settings"></a>

### Sync Settings

On each instance, configure:

- **Order Status Filter:** all / awaiting_payment / awaiting_shipment / shipped / on_hold / cancelled
- **Days Back:** How many days of historical data to import (default: 30)
- **Auto Sync:** Enable/disable scheduled synchronization

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [ShipStation Connector - Installation and Setup](https://docs.sdlccorp.com/docs/shipstation-odoo-connector/getting-started/setup/)
