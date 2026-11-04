# Magento 2 Connector Dashboard

The Magento Connector Dashboard provides a real-time overview of your integration health, synchronization status, and key performance indicators at a glance.

<a id="accessing-the-dashboard"></a>

## Accessing the Dashboard

Navigate to **Magento > Dashboard** to open the main dashboard view.

<a id="header-controls"></a>

## Header Controls

The dashboard header provides quick-access controls:

- **Instance Selector** -- Switch between multiple Magento instances to view instance-specific metrics
- **Refresh** -- Manually refresh all dashboard data
- **Date Range Filter** -- Filter KPIs and charts by a specific time period

<a id="kpi-cards"></a>

## KPI Cards

The dashboard displays key metrics as summary cards:

| KPI Card | Description |
| --- | --- |
| **Total Products** | Number of products synced between Odoo and Magento |
| **Total Customers** | Number of customer records synchronized |
| **Total Orders** | Total orders imported from Magento |
| **Total Revenue** | Cumulative revenue from synced Magento orders |
| **Pending Sync** | Number of records waiting to be synchronized |
| **Sync Errors** | Number of sync operations that encountered errors |

tip

Click on any KPI card to drill down into the corresponding list view for detailed inspection.

<a id="charts-and-analytics"></a>

## Charts and Analytics

The dashboard includes visual analytics to help you monitor sync trends:

- **Sync Activity Timeline** -- A line chart showing sync operations over time, broken down by data type (Products, Customers, Orders, Categories)
- **Order Volume Chart** -- Bar chart displaying order import volume by day or week
- **Revenue Trend** -- Line chart tracking total revenue from Magento orders over the selected period
- **Sync Success Rate** -- Pie or donut chart showing the ratio of successful vs. failed sync operations

<a id="sync-health"></a>

## Sync Health

The sync health section provides a quick status indicator for each data type:

| Data Type | Status Indicators |
| --- | --- |
| **Products** | Last sync time, success/fail count, pending items |
| **Customers** | Last sync time, success/fail count, pending items |
| **Categories** | Last sync time, success/fail count |
| **Orders** | Last sync time, success/fail count, pending items |
| **Inventory** | Last stock update time, items out of sync |

info

The dashboard auto-refreshes periodically. For immediate updates, use the manual Refresh button.

<a id="using-the-dashboard-effectively"></a>

## Using the Dashboard Effectively

- **Monitor daily** -- Check the dashboard each morning to ensure overnight cron syncs completed successfully
- **Watch for errors** -- A rising error count indicates configuration or connectivity issues that need attention
- **Track trends** -- Use the charts to identify peak order periods and plan sync schedules accordingly

<a id="next-steps"></a>

## Next Steps

- [View detailed Sync Reports](../../../reference/18.0/reference/sync-reports.md)
- [Configure Auto Sync schedules](../../../advanced/18.0/advanced/auto-sync.md)
- [Troubleshoot sync issues](../../../reference/18.0/reference/troubleshooting.md)

---

Source: [Magento 2 Connector Dashboard](https://docs.sdlccorp.com/docs/18.0/magento2-odoo-connector/configuration/dashboard/)
