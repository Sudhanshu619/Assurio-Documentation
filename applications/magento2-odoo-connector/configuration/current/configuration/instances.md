# Magento 2 Connector - Instance Configuration

The Instance form is the central hub for managing your Magento 2 connection. It stores all connection credentials, sync preferences, payment settings, and auto-sync configuration.

<a id="accessing-instances"></a>

## Accessing Instances

Navigate to **Magento > Instances** to view all configured Magento store connections. Click on an instance to open the configuration form.

![Instance configuration form](https://docs.sdlccorp.com/assets/images/instances-1-e566cc9b4e1b0acb4a8ca27b82cdf53d.webp)

<a id="connection-fields"></a>

## Connection Fields

| Field | Type | Description |
| --- | --- | --- |
| **Name** | Text | A descriptive name for this Magento instance |
| **Base URL** | URL | The base URL of your Magento store (e.g., `https://magento.example.com:8443`) |
| **Access Token** | Text | The Magento Integration Access Token for API authentication |
| **Magento User Password** | Password | The Magento admin user password |
| **Verify SSL** | Checkbox | Enable SSL certificate verification for API calls |
| **Active** | Checkbox | Enable or disable this instance connection |

warning

Always use HTTPS for production environments. Disabling SSL verification is acceptable only for local development or testing setups.

<a id="test-connection"></a>

## Test Connection

Click the **Test Connection** button to verify that Odoo can successfully communicate with your Magento store's REST API. The connector will:

1. Attempt to authenticate using the provided Access Token
2. Query the Magento API for store information
3. Display a success or error message

tip

If the test fails, verify your Base URL includes the correct port (if non-standard) and that your server's firewall allows outbound connections to the Magento host.

<a id="sync-buttons"></a>

## Sync Buttons

The instance form provides quick-action buttons for manual synchronization:

| Button | Action |
| --- | --- |
| **Test Connection** | Validates the API connection to Magento |
| **Sync Products** | Pulls all products from Magento into Odoo |
| **Sync Categories** | Imports the Magento category tree into Odoo |
| **Sync Customers** | Imports customer records from Magento |
| **Sync Orders** | Pulls orders from Magento into Odoo |
| **Sync Attribute Sets** | Imports Magento product attribute sets |

<a id="payment-sync-settings"></a>

## Payment Sync Settings

Configure how payment data is handled during order synchronization:

| Setting | Description |
| --- | --- |
| **Auto Register Magento Payments** | Automatically register payment entries in Odoo when orders are pulled from Magento |
| **Update Magento Status When Paid** | Push payment status updates back to Magento when an invoice is paid in Odoo |

<a id="auto-sync-configuration"></a>

## Auto Sync Configuration

Configure automated synchronization schedules directly from the instance form:

| Field | Description |
| --- | --- |
| **Auto Sync Enabled** | Enable or disable automatic cron-based synchronization |
| **Auto Sync Frequency** | Set the frequency interval (e.g., Hourly) |
| **Hourly Interval** | Define the exact interval (e.g., Every 1 hour(s)) |
| **Auto Sync Scope** | Select which data types to include in auto-sync (Products, Customers, Categories, Orders) |

info

Auto-sync uses Odoo's built-in cron scheduler. See [Auto Sync Cron Jobs](../../../advanced/current/advanced/auto-sync.md) for detailed configuration.

<a id="multi-instance-support"></a>

## Multi-Instance Support

You can configure multiple Magento instances to connect different Magento stores or environments (production, staging) to a single Odoo database. Each instance operates independently with its own:

- Connection credentials
- Sync schedules
- Payment settings
- Field mappings

<a id="next-steps"></a>

## Next Steps

- [Explore the Dashboard](dashboard.md)
- [Set up Product Sync](../../../data-sync/current/data-sync/products.md)
- [Configure Field Mapping](../../../advanced/current/advanced/field-mapping.md)

---

Source: [Magento 2 Connector - Instance Configuration](https://docs.sdlccorp.com/docs/magento2-odoo-connector/configuration/instances/)
