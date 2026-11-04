# ShipStation Connector - Configuration and Settings


<a id="field-mapping"></a>

## Field Mapping

Navigate to **ShipStation > Configuration > Field Mapping**.

![Field Mapping](https://docs.sdlccorp.com/assets/images/field-mapping-listing-4d050b5625a4d71e3740cded709ef4cb.webp)

![Field Mapping Form](https://docs.sdlccorp.com/assets/images/field-mapping-form-4bd3b44a6d49b7067e01a71afd6c05e1.webp)

<a id="mapping-types"></a>

### Mapping Types

| Type | Description |
| --- | --- |
| **Product Mapping** | Map Odoo product fields to ShipStation product fields |
| **Order Mapping** | Map Odoo order fields to ShipStation order fields |
| **Customer Mapping** | Map Odoo customer fields to ShipStation customer fields |
| **Category Mapping** | Map Odoo category fields to ShipStation category fields |
| **Attribute Mapping** | Map product attribute fields |

![Order Field Mapping](https://docs.sdlccorp.com/assets/images/order-field-mapping-listing-7c16d7d9cbf68c1cc4b391a7bb93aa61.webp)

![Customer Field Mapping](https://docs.sdlccorp.com/assets/images/customer-field-mapping-138724a8ea1d58132135d8b4e717dd3a.webp)

![Category Field Mapping](https://docs.sdlccorp.com/assets/images/category-field-mapping-d63ac1a82f7f7970456a21ccddff46fc.webp)

<a id="how-mapping-works"></a>

### How Mapping Works

- Each mapping row defines: **Odoo Field** to **ShipStation Field**
- Supports dot-notation paths for nested data (e.g., 'dimensions.length')
- Mappings are applied during sync to transform data in both directions

<a id="field-keys"></a>

## Field Keys

Navigate to **Configuration > Field Keys** to manage ShipStation API field names used in field mapping.

![Field Keys](https://docs.sdlccorp.com/assets/images/configuration-field-keys-14d4b32abb44ba82ac592ce197742019.webp)

<a id="reports-and-sync-logs"></a>

## Reports and Sync Logs

Navigate to **ShipStation > Reports** for sync operation reports.

![Reports](https://docs.sdlccorp.com/assets/images/report-12c77fc626b0037b58ca2d1ad2b544b3.webp)

- Each report shows: operation type, mode (manual/cron/webhook), status, record counts
- Success, failed, and running states with color-coded badges

<a id="sync-logs"></a>

### Sync Logs

Navigate to **ShipStation > Sync Logs** for raw API request/response logs.

![Sync Logs](https://docs.sdlccorp.com/assets/images/sync-logs-ee8f0b53d2a04323cfc369f2d98427f7.webp)

- Shows the full API URL, method, request body, and response
- Useful for debugging sync issues

<a id="cron-jobs"></a>

## Cron Jobs

| Cron Job | Interval | Default | Description |
| --- | --- | --- | --- |
| **Order Sync** | Every 10 min | Enabled | Pulls new/updated orders |
| **Shipment Sync** | Every 15 min | Enabled | Pulls shipment and tracking updates |
| **Product Sync** | Daily | Enabled | Syncs product catalog changes |
| **Customer Sync** | Every 30 min | Disabled | Imports new customers |
| **Inventory Sync** | Every 60 min | Disabled | Refreshes stock levels |

<a id="general-settings"></a>

## General Settings

Navigate to **Settings > ShipStation** for global configuration:

- **Default Instance:** Select the default ShipStation instance
- **Sync Log Retention:** Number of days to keep sync logs (default: 30)
- **Enable Webhooks:** Turn on/off webhook processing

<a id="dashboard"></a>

## Dashboard

![Dashboard](https://docs.sdlccorp.com/assets/images/dashboard1-0b4fa7b6295dc231abb61ba014c5636e.webp)

![Dashboard Charts](https://docs.sdlccorp.com/assets/images/dashboard2-b2ceef42cb0b65d7c60ff8c5f69b3358.webp)

The dashboard includes AI-powered insights:

- Pending shipment alerts
- Low stock alerts
- Instance health monitoring
- Carrier trends and recommendations

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [ShipStation Connector - Configuration and Settings](https://docs.sdlccorp.com/docs/19.0/shipstation-odoo-connector/configuration/settings/)
