# Magento 2 Connector - Auto Sync Cron Jobs

The Magento 2 Connector includes built-in cron job support that automates data synchronization between Odoo and Magento at configurable intervals. This eliminates the need for manual sync operations and keeps your data continuously up to date.

<a id="enabling-auto-sync"></a>

## Enabling Auto Sync

Auto sync is configured per instance:

1. Navigate to **Magento > Instances**.
2. Open your instance.
3. Scroll down to the **Auto Sync Cron** section.
4. Configure the following settings:

<a id="schedule-settings"></a>

## Schedule Settings

| Field | Description | Default |
| --- | --- | --- |
| **Auto Sync Enabled** | Master toggle to enable or disable automatic synchronization | Disabled |
| **Auto Sync Frequency** | How often the sync runs (Hourly, Daily, Weekly) | Hourly |
| **Hourly Interval** | Specific interval between sync runs (e.g., Every 1 hour(s)) | Every 1 hour(s) |

<a id="auto-sync-scope"></a>

## Auto Sync Scope

Select which data types to include in each automatic sync run:

| Scope Option | Description |
| --- | --- |
| **Products** | Automatically sync products between Odoo and Magento |
| **Customers** | Automatically sync customer records |
| **Categories** | Automatically sync product categories |
| **Orders** | Automatically sync orders, invoices, and shipments |

info

You can enable or disable each scope independently. For example, you might want to sync orders every hour but only sync products once daily.

<a id="built-in-cron-jobs"></a>

## Built-in Cron Jobs

The connector registers the following cron jobs in Odoo's scheduler:

| Cron Job | Description | Source Action |
| --- | --- | --- |
| **Magento Product Sync** | Pulls/pushes product data between systems | `cron_auto_scope` |
| **Magento Customer Sync** | Synchronizes customer records | `cron_auto_scope` |
| **Magento Category Sync** | Synchronizes product categories | `cron_auto_scope` |
| **Magento Order Sync** | Imports new and updated orders from Magento | `cron_auto_scope` |
| **Magento Inventory Sync** | Updates stock quantities across platforms | `cron_auto_scope` |

<a id="how-auto-sync-works"></a>

## How Auto Sync Works

1. **Cron Trigger** -- Odoo's scheduled action system triggers the sync job at the configured interval.
2. **Scope Check** -- The connector checks which data types are enabled in the Auto Sync Scope.
3. **API Call** -- For each enabled scope, the connector queries the Magento REST API for new or updated records.
4. **Data Processing** -- New records are created in Odoo; existing records are updated with the latest data.
5. **Report Logging** -- Each sync operation is logged in the Sync Reports with success/error counts, start time, and end time.

<a id="monitoring-cron-jobs"></a>

## Monitoring Cron Jobs

You can monitor cron job execution in two ways:

<a id="via-sync-reports"></a>

### Via Sync Reports

Navigate to **Magento > Reports > Sync Reports** to view detailed logs of every auto-sync run. Each entry shows:

- The sync type and mode (Cron)
- Source action (`cron_auto_scope`)
- Total records processed
- Success and error counts
- Start and end timestamps

<a id="via-odoo-scheduled-actions"></a>

### Via Odoo Scheduled Actions

Navigate to **Settings > Technical > Scheduled Actions** to view and manage the underlying Odoo cron jobs. Here you can:

- View the next execution time
- Manually trigger a cron job
- Adjust the technical interval settings

tip

If auto-sync appears to not be running, check the Odoo Scheduled Actions view to ensure the cron jobs are active and not stuck.

<a id="best-practices"></a>

## Best Practices

- **Start with hourly sync** -- Begin with hourly synchronization and adjust based on your volume and needs.
- **Monitor error counts** -- Regularly check Sync Reports for rising error counts that may indicate connectivity or data issues.
- **Off-peak scheduling** -- For large catalogs, consider running full product syncs during off-peak hours to minimize API load.
- **Order sync priority** -- Orders should generally sync more frequently than products or categories, as they are time-sensitive.

warning

Running sync too frequently (e.g., every few minutes) may put excessive load on both Odoo and Magento servers. Hourly sync is recommended for most use cases.

<a id="next-steps"></a>

## Next Steps

- [View Sync Reports](../../../reference/19.0/reference/sync-reports.md)
- [Manage Inventory](inventory.md)
- [Troubleshoot sync issues](../../../reference/19.0/reference/troubleshooting.md)

---

Source: [Magento 2 Connector - Auto Sync Cron Jobs](https://docs.sdlccorp.com/docs/19.0/magento2-odoo-connector/advanced/auto-sync/)
