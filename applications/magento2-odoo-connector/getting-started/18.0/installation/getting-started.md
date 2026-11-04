# Magento 2 Connector - Installation & Setup

This guide walks you through installing the SDLC Magento 2 Connector module in Odoo and connecting it to your Magento 2 store.

<a id="prerequisites"></a>

## Prerequisites

Before you begin, ensure you have the following:

| Requirement | Details |
| --- | --- |
| **Odoo Instance** | A running Odoo 17, 18, or 19 instance (Community or Enterprise) |
| **Magento 2 Store** | A Magento 2.3+ store with REST API enabled |
| **Admin Access** | Administrator privileges on both Odoo and Magento |
| **API Token** | A Magento Integration Access Token (see below) |
| **Network Access** | Odoo server must be able to reach Magento's API endpoint |

<a id="step-1-install-the-module"></a>

## Step 1: Install the Module

1. Download the **SDLC Magento 2 Connector** module from the Odoo App Store or your SDLC Corp delivery package.
2. Place the module folder (`sdlc_magento_connector`) in your Odoo addons directory.
3. Restart the Odoo server.
4. Navigate to **Apps** in Odoo, click **Update Apps List**.
5. Search for **Magento** and click **Install**.

tip

If you are using Odoo.sh, upload the module to your custom addons repository and trigger a rebuild.

<a id="step-2-generate-a-magento-api-access-token"></a>

## Step 2: Generate a Magento API Access Token

The connector communicates with Magento via the REST API. You need an Integration Access Token:

1. Log in to your **Magento Admin Panel**.
2. Navigate to **System > Extensions > Integrations**.
3. Click **Add New Integration**.
4. Fill in the integration details:
   - **Name**: `Odoo Connector`
   - **Email**: Your admin email
   - **Password**: Your Magento admin password
5. Go to the **API** tab and select the required resource access:
   - **Resource Access**: Set to `All` (or selectively grant Products, Customers, Orders, Sales, Catalog, and Inventory)
6. Click **Save** and then **Activate**.
7. Confirm activation to receive the **Access Token**.

Important

Copy and securely store the Access Token immediately. Magento only displays it once. If lost, you must create a new integration.

<a id="step-3-configure-the-magento-instance-in-odoo"></a>

## Step 3: Configure the Magento Instance in Odoo

1. Open Odoo and navigate to **Magento > Instances**.
2. Click **New** to create a new instance.
3. Fill in the connection details:

| Field | Description |
| --- | --- |
| **Name** | A descriptive name for this connection (e.g., `My Magento Store`) |
| **Base URL** | Your Magento store URL (e.g., `https://magento.example.com`) |
| **Access Token** | The integration token generated in Step 2 |
| **Magento User Password** | Your Magento admin password |
| **Verify SSL** | Enable for production environments with valid SSL certificates |
| **Active** | Check to enable this instance |

4. Click **Test Connection** to verify the connection.

![Instance configuration form](https://docs.sdlccorp.com/assets/images/instances-1-e566cc9b4e1b0acb4a8ca27b82cdf53d.webp)

<a id="step-4-initial-sync"></a>

## Step 4: Initial Sync

Once your connection is verified, perform the initial data sync:

1. Click **Sync Products** to pull your Magento product catalog into Odoo.
2. Click **Sync Categories** to import your category hierarchy.
3. Click **Sync Customers** to import customer records.
4. Click **Sync Orders** to pull existing orders.

info

The initial sync may take several minutes depending on the size of your Magento catalog. You can monitor progress in **Reports > Sync Reports**.

<a id="next-steps"></a>

## Next Steps

- [Configure your instance settings in detail](../../../configuration/18.0/configuration/instances.md)
- [Set up auto-sync cron jobs](../../../advanced/18.0/advanced/auto-sync.md)
- [Configure field mapping](../../../advanced/18.0/advanced/field-mapping.md)

---

Source: [Magento 2 Connector - Installation & Setup](https://docs.sdlccorp.com/docs/18.0/magento2-odoo-connector/installation/getting-started/)
