# PrestaShop Connector - Auto Sync Cron Jobs

Schedule automatic synchronization from the instance configuration form.

<a id="setting-up-auto-sync"></a>

## Setting Up Auto Sync

Open any PrestaShop instance configuration and go to the **Auto Sync Cron** tab.

<a id="schedule-settings"></a>

## Schedule Settings

| Field | Description |
| --- | --- |
| **Auto Sync Enabled** | Master toggle to enable/disable scheduled sync |
| **Auto Sync Frequency** | Hourly / Daily / Weekly / Monthly |
| **Repeat Every** | Number + unit (e.g. "Every 2 Day(s)") |
| **Day of Week** | For weekly frequency - which day to run (Monday-Sunday) |
| **Day of Month** | For monthly frequency - which day (1-28) |
| **Run At (HH:MM)** | Time of day to run (server time) |
| **Run At Minute** | For hourly frequency - which minute of the hour |

<a id="sync-scope"></a>

## Sync Scope

Select which data types to include in the auto sync:

- Products, Customers, Categories, Orders
- Brands, Carriers, Suppliers
- Attributes, Features, Taxes

<a id="run-history"></a>

## Run History

| Field | Description |
| --- | --- |
| **Scheduled Action** | Link to the created `ir.cron` record |
| **Next Scheduled Run** | When the cron will run next |
| **Last Auto Sync Run** | Timestamp of last completed run |
| **Last Run Status** | Success (green) / Partial (yellow) / Failed (red) / Never (blue) |
| **Duration** | How long the last sync took (seconds) |
| **Total Runs** | Counter of all auto sync executions |

<a id="action-buttons"></a>

## Action Buttons

- **Run Sync Now** - Manually trigger the auto sync immediately (with confirmation dialog)
- **View Sync Logs** - Open filtered list of all auto sync reports for this instance

info

The auto sync generates a detailed sync report for each run. Each scope type (products, customers, etc.) is logged individually with success/error counts.

<a id="sync-order"></a>

## Sync Order

When auto sync runs, entities are synced in dependency order:

**Categories > Brands > Suppliers > Attributes > Features > Taxes > Carriers > Products > Customers**

This ensures dependencies (like categories and brands) exist before products are imported.

<a id="need-help"></a>

## Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/)

---

Source: [PrestaShop Connector - Auto Sync Cron Jobs](https://docs.sdlccorp.com/docs/17.0/prestashop-odoo-connector/configuration/auto-sync/)
