# WooCommerce Connector - Configuration and Settings


<a id="field-mapping"></a>

## Field Mapping

Navigate to **WooCommerce > Field Mapping**.

![Field Mapping](https://docs.sdlccorp.com/assets/images/fieldmapping-bcb5a581e4800de8492eedbff9284c36.webp)

<a id="mapping-types"></a>

### Mapping Types

| Type | Description |
| --- | --- |
| **Product Mapping** | Map Odoo product fields to WooCommerce product fields |
| **Customer Mapping** | Map Odoo contact fields to WooCommerce customer fields |
| **Category Mapping** | Map Odoo category fields to WooCommerce category fields |

![Product Field Mapping](https://docs.sdlccorp.com/assets/images/product-field-mapping-02c7808a37337f237b6e6f6e8a6e7589.webp)

![Customer Field Mapping](https://docs.sdlccorp.com/assets/images/customer-field-mapping-c190eed35e84a96bfb5a1da5fcac21e8.webp)

![Category Field Mapping](https://docs.sdlccorp.com/assets/images/category-field-mapping-0f1df1fe87f74599ee3961535e36ea42.webp)

- Each row maps an **Odoo Field** to a **WooCommerce Field**
- Supports dot-notation for nested data (e.g., 'dimensions.length')
- Load default mappings with one click, then customize

<a id="webhooks"></a>

## Webhooks

In your WooCommerce admin:

1. Go to **WooCommerce > Settings > Advanced > Webhooks**
2. Add a new webhook for each event
3. Set Delivery URL to: `https://your-odoo-domain.com/woo/webhook`
4. Set Secret to match the Webhook Secret in your Odoo instance

Supported events: Order created/updated/deleted, Product created/updated/deleted, Customer created/updated, Coupon created/updated

<a id="reports-and-sync-logs"></a>

## Reports and Sync Logs

![Sync Reports](https://docs.sdlccorp.com/assets/images/sync-reports-d324b5b1a3c01bace7bc6cd89492c91a.webp)

![Sales Report](https://docs.sdlccorp.com/assets/images/sales-report-1e70c2f1182378551c64816e1c07d797.webp)

![Webhook Reports](https://docs.sdlccorp.com/assets/images/webhook-reports-1ea63570aff4f21bbe98397cb42cdc46.webp)

![Cancelled Orders](https://docs.sdlccorp.com/assets/images/cancelled-orders-f343718afc944c2e08c646690f8cec8e.webp)

![Mapping Reports](https://docs.sdlccorp.com/assets/images/mapping-reports-ffee08d2ba6a73a881363d452f5a0660.webp)

| Report | Description |
| --- | --- |
| **Sync Reports** | All sync operation reports with status and counts |
| **Sales Report** | Revenue and order analytics |
| **Webhook Reports** | Incoming webhook event logs |
| **Cancelled Orders** | Filtered view of cancelled/refunded orders |
| **Mapping Reports** | Field mapping usage and coverage analysis |

<a id="cron-jobs"></a>

## Cron Jobs

| Cron Job | Interval | Default | Description |
| --- | --- | --- | --- |
| **WooCommerce Auto Sync** | Every 15 min | Enabled | Syncs all enabled entities |
| **Sync Woo Order Status** | Every 5 min | Enabled | Pulls latest order status changes |

<a id="global-settings"></a>

## Global Settings

Navigate to **Settings > WooCommerce**:

- **Default Instance:** Select the default WooCommerce instance
- **Sync Log Retention:** Days to keep sync logs (default: 30)
- **Enable Webhooks:** Toggle webhook processing
- **AI Provider:** Configure AI service for content generation

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [WooCommerce Connector - Configuration and Settings](https://docs.sdlccorp.com/docs/18.0/woocommerce-odoo-connector/configuration/settings/)
