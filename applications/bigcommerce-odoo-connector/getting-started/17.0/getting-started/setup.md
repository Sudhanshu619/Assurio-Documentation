# BigCommerce Connector - Installation and Setup


<a id="prerequisites"></a>

## Prerequisites

- Odoo 18 Community or Enterprise edition
- Active BigCommerce store with API access
- BigCommerce API credentials (Store Hash, Access Token, Client ID, Client Secret)

<a id="bigcommerce-api-setup"></a>

## BigCommerce API Setup

In your BigCommerce admin panel:

1. Go to **Advanced Settings > API Accounts**
2. Click **Create API Account > Create V2/V3 API Token**
3. Set name: 'Odoo Connector'
4. Grant OAuth scopes: Products (modify), Orders (modify), Customers (modify), Content (modify)
5. Click **Save** and copy the Access Token, Client ID, Client Secret, and Store Hash

![API Credentials](https://docs.sdlccorp.com/assets/images/connector-api-credentials-2061ae5cf68115168c887206aa5aba96.webp)

warning

The Access Token is only shown once. Save it securely before closing.

<a id="instance-configuration"></a>

## Instance Configuration

Navigate to **BigCommerce > Connectors**.

![Connector Listing](https://docs.sdlccorp.com/assets/images/instance-connection-listing-a6bc091459d085dff299775b6b87a8f6.webp)

Click **New** and fill in:

| Field | Required | Description |
| --- | --- | --- |
| **Name** | Yes | Descriptive name (e.g., "US Store") |
| **Store Hash** | Yes | Your BigCommerce store hash |
| **Access Token** | Yes | BigCommerce V2/V3 API access token |
| **Client ID** | Yes | OAuth client ID |
| **Client Secret** | Yes | OAuth client secret |
| **Company** | Yes | The Odoo company this instance belongs to |

![Connector Form](https://docs.sdlccorp.com/assets/images/connector--57a0061bfbab1244f103699cf030137f.webp)

Click **Test Connection** to verify. A green 'Connected' status confirms success.

<a id="sync-actions"></a>

### Sync Actions

Each instance provides header buttons for manual sync:

- **Sync Products** / **Sync Orders** / **Sync Customers** / **Sync Categories** / **Sync Inventory**

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [BigCommerce Connector - Installation and Setup](https://docs.sdlccorp.com/docs/17.0/bigcommerce-odoo-connector/getting-started/setup/)
