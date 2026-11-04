# Magento 2 Connector - Troubleshooting

This page covers common issues you may encounter with the SDLC Magento 2 Connector and how to resolve them.

---


<a id="1-connection-failures"></a>

## 1. Connection Failures

**Symptom**: The Test Connection button returns an error, or sync operations fail with connection errors.

**Possible Causes & Solutions**:

| Cause | Solution |
| --- | --- |
| Incorrect Base URL | Verify the URL includes the correct protocol (`https://`) and port (e.g., `:8443`) |
| Invalid Access Token | Generate a new Integration Access Token in Magento Admin > System > Integrations |
| SSL Certificate Issues | If using a self-signed certificate, disable **Verify SSL** on the instance (development only) |
| Firewall Blocking | Ensure the Odoo server can reach the Magento server on the required port |
| Magento API Disabled | Verify that Magento REST API is enabled in Magento Admin > Stores > Configuration > Services > Web API |

tip

Test your Magento API independently using `curl` or Postman before troubleshooting the connector:

```
curl -X GET "https://your-magento.com/rest/V1/store/storeConfigs" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---


<a id="2-products-not-syncing"></a>

## 2. Products Not Syncing

**Symptom**: Products exist in Magento but do not appear in Odoo after sync, or new Odoo products are not created in Magento.

**Possible Causes & Solutions**:

| Cause | Solution |
| --- | --- |
| Product not in API scope | Ensure the Integration has access to the Catalog API resources |
| Disabled products skipped | Check if the sync is configured to skip disabled products |
| SKU conflicts | Ensure product SKUs are unique across both systems |
| Missing required attributes | Verify all required Magento product attributes are filled |
| Attribute set mismatch | Sync attribute sets first using the **Sync Attribute Sets** button |

info

Check the [Sync Reports](sync-reports.md) for detailed error messages about which products failed and why.

---


<a id="3-order-sync-issues"></a>

## 3. Order Sync Issues

**Symptom**: Orders are not imported from Magento, or orders pushed to Magento fail.

**Possible Causes & Solutions**:

| Cause | Solution |
| --- | --- |
| Customer not synced | Ensure the order's customer exists in both systems. Sync customers first. |
| Product not mapped | All order line products must be synced and mapped before order import. Sync products first. |
| Payment method mismatch | Configure payment method mapping in the instance settings |
| Order already exists | The connector skips orders that have already been imported (matched by Magento Order ID) |
| API permissions | Verify the Integration token has access to Sales API resources |

warning

If orders sync but with incorrect totals, check that product prices and tax configurations are consistent between Magento and Odoo.

---


<a id="4-inventory-discrepancies"></a>

## 4. Inventory Discrepancies

**Symptom**: Stock levels in Odoo do not match stock levels in Magento after sync.

**Possible Causes & Solutions**:

| Cause | Solution |
| --- | --- |
| Concurrent updates | If both systems are used for inventory management, designate one as primary |
| Sync timing | Stock changes made between sync intervals are not reflected until the next sync |
| Warehouse mismatch | Ensure Odoo warehouse configuration maps to the correct Magento stock source |
| Reserved quantities | Magento may show different available vs. total quantities due to reservations |
| Multi-source inventory | If using Magento MSI, ensure the correct source is configured |

**Resolution Steps**:

1. Click **Refresh Inventory** on the Inventory page to force an immediate sync.
2. Compare the quantities shown in the Magento admin with Odoo's inventory view.
3. Check the Sync Reports for any inventory sync errors.
4. If discrepancies persist, perform a manual inventory adjustment in the primary system and re-sync.

---


<a id="5-field-mapping-errors"></a>

## 5. Field Mapping Errors

**Symptom**: Data syncs but field values are incorrect, missing, or cause errors.

**Possible Causes & Solutions**:

| Cause | Solution |
| --- | --- |
| Incompatible field types | Ensure mapped fields have compatible data types (text to text, number to number) |
| Missing fields | Click **Load New Fields** to refresh available fields from both systems |
| Mapping not active | Verify the mapping record has the **Active** checkbox enabled |
| Instance mismatch | Check that the mapping is assigned to the correct Magento instance |
| Custom attribute not indexed | In Magento, ensure custom attributes are set to "Use in API" |

**Resolution Steps**:

1. Navigate to **Magento > Mapping** and review all active mappings.
2. Click the **Test** button on each mapping to validate it.
3. Check the [Mapping Report](sync-reports.md) for test results.
4. Disable problematic mappings, run a sync, and re-enable them one by one to isolate the issue.

danger

Never delete a mapping that is actively used in production. Instead, uncheck the **Active** flag to temporarily disable it while troubleshooting.

---


<a id="general-debugging-steps"></a>

## General Debugging Steps

1. **Enable Developer Mode** -- Go to Odoo Settings and enable Developer Mode to access technical menus.
2. **Check Server Logs** -- Review the Odoo server log file for API request/response details and Python tracebacks.
3. **Review Sync Reports** -- Navigate to **Reports > Sync Reports** and filter by errors.
4. **Test API Manually** -- Use Postman or curl to test the Magento API independently.
5. **Update the Module** -- Ensure you are running the latest version of the connector module.

<a id="getting-help"></a>

## Getting Help

If you are unable to resolve the issue:

- **Email**: [support@sdlccorp.com](mailto:support@sdlccorp.com)
- **Contact**: [Reach out to SDLC Corp Support](https://sdlccorp.com/contact-us/)

Please include the following when contacting support:

- Odoo version and edition
- Magento version
- Connector module version
- Screenshots of the error
- Relevant Sync Report entries

<a id="next-steps"></a>

## Next Steps

- [FAQ](faq.md)
- [Sync Reports](sync-reports.md)
- [API Reference](api-reference.md)

---

Source: [Magento 2 Connector - Troubleshooting](https://docs.sdlccorp.com/docs/17.0/magento2-odoo-connector/reference/troubleshooting/)
