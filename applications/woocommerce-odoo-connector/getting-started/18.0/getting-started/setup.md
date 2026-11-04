# WooCommerce Connector - Installation and Setup


<a id="prerequisites"></a>

## Prerequisites

- Odoo 18 Community or Enterprise edition
- Active WooCommerce store with REST API enabled
- WooCommerce REST API keys (Consumer Key + Consumer Secret)

<a id="woocommerce-api-setup"></a>

## WooCommerce API Setup

In your WooCommerce admin panel:

1. Go to **WooCommerce > Settings > Advanced > REST API**
2. Click **Add Key**
3. Set Description: 'Odoo Connector', User: Admin, Permissions: **Read/Write**
4. Click **Generate API Key**
5. Copy the **Consumer Key** and **Consumer Secret**

warning

The Consumer Secret is only shown once. Save it securely before closing the page.

<a id="instance-configuration"></a>

## Instance Configuration

Navigate to **WooCommerce > Instances**.

![Instance](https://docs.sdlccorp.com/assets/images/instance-2852dbff389f817add62f7204cbdc5e4.webp)

Click **New** and fill in:

| Field | Required | Description |
| --- | --- | --- |
| **Name** | Yes | Descriptive name (e.g., "Main Store") |
| **Store URL** | Yes | Your WooCommerce store URL (e.g., `https://mystore.com`) |
| **Consumer Key** | Yes | WooCommerce REST API Consumer Key |
| **Consumer Secret** | Yes | WooCommerce REST API Consumer Secret |
| **Company** | Yes | The Odoo company this instance belongs to |

Click **Test Connection** to verify.

![Test Connection](https://docs.sdlccorp.com/assets/images/testconnection-633111ea40b25a2c71469d938ba7d54e.webp)

A green 'Connected' status confirms success.

<a id="whats-next"></a>

## What's next

Once your WooCommerce instance is configured and the connection test passes, you're ready to start moving data. The most common sequence:

1. [Configure global Settings](../../../configuration/18.0/configuration/settings.md) - webhooks, field mapping, cron jobs.
2. Pull your existing products with the first scheduled sync.
3. Pull your existing customers - they'll get matched to Odoo contacts by email.
4. Run a quick smoke test by pushing one new test order through.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [WooCommerce Connector - Installation and Setup](https://docs.sdlccorp.com/docs/18.0/woocommerce-odoo-connector/getting-started/setup/)
