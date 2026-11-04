# Generate Shopify API Keys

To connect Odoo with Shopify, you need to create a Custom App in Shopify and obtain API credentials.

<a id="creating-a-custom-app-in-shopify"></a>

## Creating a Custom App in Shopify

1. Log in to your **Shopify Admin**
2. Go to **Settings → Apps and sales channels**
3. Click **Develop apps** (top right)
4. Click **Allow custom app development** if prompted
5. Click **Create an app**
6. Enter an app name (e.g., `SDLC Odoo Connector`)
7. Click **Create app**

<a id="configuring-api-scopes"></a>

## Configuring API Scopes

Once the app is created:

1. Click **Configure Admin API scopes**
2. Enable the following scopes:

| Scope | Required For |
| --- | --- |
| `read_products`, `write_products` | Product sync |
| `read_orders`, `write_orders` | Order management |
| `read_inventory`, `write_inventory` | Inventory sync |
| `read_customers`, `write_customers` | Customer sync |
| `read_shipping`, `write_shipping` | Shipment export |
| `read_fulfillments`, `write_fulfillments` | Fulfillment sync |
| `read_locations` | Warehouse mapping |
| `read_reports` | Payout reports |

3. Click **Save**

<a id="obtaining-credentials"></a>

## Obtaining Credentials

1. Click **Install app**
2. Note your **API key** and **API secret key**
3. Copy the **Admin API access token** (shown only once: save it immediately)

warning

The Admin API access token is shown **only once**. Copy and store it securely before closing the page.

<a id="entering-credentials-in-odoo"></a>

## Entering Credentials in Odoo

Enter these values in your Shopify instance configuration in Odoo.
Refer to [Setup Connector](setup-connector.md) for the full steps.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Generate Shopify API Keys](https://docs.sdlccorp.com/docs/19.0/shopify-odoo-connector/installation/generate-api-keys/)
