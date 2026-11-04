# BigCommerce Connector - Configuration and Settings


<a id="field-mapping"></a>

## Field Mapping

Navigate to **BigCommerce > Field Mappings**.

![Field Mapping](https://docs.sdlccorp.com/assets/images/field-mapping--ea1f137685fc5257d65ca859d3ec62eb.webp)

<a id="mapping-types"></a>

### Mapping Types

| Type | Description |
| --- | --- |
| **Product Mapping** | Map Odoo product fields to BigCommerce product fields |
| **Customer Mapping** | Map Odoo partner fields to BigCommerce customer fields |
| **Order Mapping** | Map Odoo sale order fields to BigCommerce order fields |
| **Category Mapping** | Map Odoo category fields to BigCommerce category fields |

![Product Mapping](https://docs.sdlccorp.com/assets/images/field-mapping-product-47e8ba1cf2f83300407f9c2c4ae37b9c.webp)

![Customer Mapping](https://docs.sdlccorp.com/assets/images/field-mapping-customer-fc5e5c67e0d4596f1ff62e4183e25b22.webp)

![Order Mapping](https://docs.sdlccorp.com/assets/images/field-mapping-order-3fd9c78560216f82e915a286cdaf3553.webp)

![Category Mapping](https://docs.sdlccorp.com/assets/images/field-mapping-category-e44d6a1cb5202db82fe7b842ecde72bd.webp)

<a id="test-wizard"></a>

### Test Wizard

The Field Mapping Test Wizard lets you validate mappings before sync. Select a mapping type and instance, provide a sample JSON payload, and click **Test** to see the resulting Odoo values.

<a id="ai-dashboard-assistant"></a>

## AI Dashboard Assistant

![AI Assistant](https://docs.sdlccorp.com/assets/images/connector-ai-assistent-7e2c279d83fc7885745384d219cefa0e.webp)

The dashboard includes a Google Gemini-powered AI assistant that can:

- Answer questions about your sync data and operations
- Provide business insights from order and product trends
- Suggest actions to resolve sync issues

<a id="automation-rules"></a>

## Automation Rules

![Automation](https://docs.sdlccorp.com/assets/images/connector-automation-9161baa3d97da5d78727b646ed4f04f2.webp)

Auto-assign warehouses, carriers, and sales teams based on order conditions.

<a id="reports-and-sync-logs"></a>

## Reports and Sync Logs

Navigate to **BigCommerce > Logs > Sync Logs**.

![Sync Logs](https://docs.sdlccorp.com/assets/images/logs-9ad36db434ac0f0d4496eef8530fa862.webp)

![Inventory Logs](https://docs.sdlccorp.com/assets/images/inventory-logs-efd0d258473ccf5008c3123a701e8f17.webp)

<a id="cron-jobs"></a>

## Cron Jobs

| Cron Job | Interval | Description |
| --- | --- | --- |
| **Product Sync** | Every 30 min | Syncs product catalog changes |
| **Order Sync** | Every 15 min | Pulls new/updated orders |
| **Customer Sync** | Every 30 min | Imports customer data |
| **Inventory Sync** | Every 20 min | Refreshes stock levels |
| **Process Webhooks** | Every 5 min | Processes queued webhook events |

<a id="global-settings"></a>

## Global Settings

Navigate to **Settings > BigCommerce**:

- **Default Instance:** Select the default BigCommerce instance
- **Gemini API Key:** Configure Google Gemini for AI assistant
- **Webhook Processing:** Enable/disable automatic processing
- **Sync Log Retention:** Days to keep sync logs

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [BigCommerce Connector - Configuration and Settings](https://docs.sdlccorp.com/docs/bigcommerce-odoo-connector/configuration/settings/)
