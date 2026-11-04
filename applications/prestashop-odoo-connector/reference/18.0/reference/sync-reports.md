# PrestaShop Connector - Sync Reports & Logs


<a id="what-to-look-for"></a>

## What to look for

The Sync Reports page is your audit trail for every record the connector has moved. Use it to:

- Confirm an expected sync actually ran (sometimes a cron job is disabled silently).
- Spot records that failed - they're highlighted with the underlying error.
- Re-run individual failures without touching the records that worked.

If failures are recurring on the same kind of record, the root cause is almost always a field mapping mismatch - see [Field Mapping](../../../configuration/18.0/configuration/field-mapping.md).

<a id="overview"></a>

## Overview

Sync reports are the audit trail for every record the connector has moved between PrestaShop and Odoo. Use this page to confirm a sync ran successfully, find the records that failed, and re-run the failures without touching the ones that worked.
Navigate to **PrestaShop > Reports > Sync Reports**.

Every sync operation generates a report with:

- Instance name, Sync Type, Mode (Pull/Push/Sync)
- Source Action (manual button, cron, auto_sync)
- Start Time, End Time
- Total Records, Success Count, Error Count
- Status: Running (blue) / Done (green) / Failed (red)
- Individual log entries with level (Success/Error/Info) and message

![Sync Reports List](https://docs.sdlccorp.com/assets/images/PrestaShop-reports-sync.report-1-7cde9d33bf04e7a189bad53e0d26ab6a.webp)

![Sync Report Detail](https://docs.sdlccorp.com/assets/images/PrestaShop-sync.report-2525c0d196cf80dfcfa5720cc10e5ee2.webp)

<a id="using-sync-reports"></a>

## Using Sync Reports

Use sync reports to:

- Track which records synced successfully
- Identify and troubleshoot errors
- Monitor sync frequency and performance
- Verify auto sync cron is running as expected

<a id="need-help"></a>

## Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/)

---

Source: [PrestaShop Connector - Sync Reports & Logs](https://docs.sdlccorp.com/docs/18.0/prestashop-odoo-connector/reference/sync-reports/)
