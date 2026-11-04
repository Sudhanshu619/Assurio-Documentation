# Setup Connector


<a id="whats-covered-here"></a>

## What's covered here

This page walks the end-to-end setup of a single Shopify-Odoo instance:

1. Install the connector module from Apps.
2. Configure your first instance with API keys.
3. Run a connection test before importing any data.
4. Decide on your default warehouse, pricelist, currency and behaviour flags.

For step-by-step on each, follow the links into the sub-pages.

After installing the module, configure the Shopify store connection in Odoo.

<a id="adding-a-new-shopify-instance"></a>

## Adding a New Shopify Instance

1. In Odoo, navigate to **Shopify → Configuration → Shopify Instances**
2. Click **New** to create a new instance

![Shopify Instances list view with New button](https://docs.sdlccorp.com/assets/images/shopify-instance-1-739e7564ec0fc94791a7f151e5583a68.webp)
3. Fill in the required fields:

| Field | Description |
| --- | --- |
| **Name** | A label for this Shopify store (e.g., "My US Store") |
| **Shopify URL** | Your store domain (e.g., `mystore.myshopify.com`) |
| **API Key** | From your Shopify Private App |
| **API Secret** | From your Shopify Private App |
| **Access Token** | Admin API access token |

4. Click **Test Connection** to verify the credentials
5. Click **Save**

<a id="multi-store-setup"></a>

## Multi-Store Setup

The connector supports multiple Shopify stores connected to the same Odoo instance.
Simply repeat the steps above for each store. Each store maintains its own sync settings,
webhooks, and operation queues.

info

For multi-store configurations, you can configure different warehouses and price lists per store instance.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Setup Connector](https://docs.sdlccorp.com/docs/17.0/shopify-odoo-connector/installation/setup-connector/)
