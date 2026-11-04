# PrestaShop Connector - Data Synchronization

The connector supports bidirectional synchronization of all data types.

<a id="sync-flow-prestashop-to-odoo-pull"></a>

## Sync Flow: PrestaShop to Odoo (Pull)

When you click a sync button or the auto sync cron runs, data flows as follows:

1. The connector calls the PrestaShop Webservice API (REST)
2. API returns data in JSON format
3. The connector extracts field values from the API response
4. **Field Mappings are applied** - mapped PS fields are converted to Odoo field values
5. If the record exists in Odoo (matched by PS ID), it is **updated**
6. If the record is new, it is **created** in Odoo
7. A **Sync Report** is generated with success/error counts

<a id="sync-flow-odoo-to-prestashop-push"></a>

## Sync Flow: Odoo to PrestaShop (Push)

When you click "Create in PrestaShop" or "Update in PrestaShop" on a record:

1. The connector reads the Odoo record values
2. **Field Mappings are applied** - mapped Odoo fields are converted to PS API values
3. An XML payload is built with the mapped values
4. The connector sends a POST (create) or PUT (update) request to the PS API
5. The PS ID is saved back on the Odoo record

info

The field mapping system overlays values on top of the standard sync. If no mappings are configured, the built-in sync logic handles all fields.

<a id="need-help"></a>

## Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/)

---

Source: [PrestaShop Connector - Data Synchronization](https://docs.sdlccorp.com/docs/17.0/prestashop-odoo-connector/configuration/data-sync/)
