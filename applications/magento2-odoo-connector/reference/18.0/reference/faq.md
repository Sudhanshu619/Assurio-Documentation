# Magento 2 Connector - Frequently Asked Questions


<a id="common-questions"></a>

## Common Questions

<a id="1-which-versions-of-odoo-and-magento-are-supported"></a>

### 1. Which versions of Odoo and Magento are supported?

The SDLC Magento 2 Connector supports **Odoo 17, 18, and 19** (Community and Enterprise editions) and **Magento 2.3+** (Open Source and Commerce). The connector uses Magento's standard REST API, which is consistent across all Magento 2.x versions.

---


<a id="2-can-i-connect-multiple-magento-stores-to-a-single-odoo-instance"></a>

### 2. Can I connect multiple Magento stores to a single Odoo instance?

Yes. The connector supports **multi-instance** configuration. You can create a separate instance record for each Magento store under **Magento > Instances**. Each instance operates independently with its own credentials, sync schedules, and field mappings.

---


<a id="3-does-the-connector-support-bidirectional-sync"></a>

### 3. Does the connector support bidirectional sync?

Yes. The connector supports full **bidirectional synchronization** for products, customers, categories, and orders. You can pull data from Magento into Odoo and push data from Odoo to Magento. Field mappings allow you to control exactly which fields are synced in which direction.

---


<a id="4-how-often-does-the-auto-sync-run"></a>

### 4. How often does the auto-sync run?

Auto-sync frequency is fully configurable per instance. You can set it to run **hourly**, **daily**, or **weekly**. The default is hourly (every 1 hour). You can also adjust the specific interval (e.g., every 2 hours, every 6 hours). See [Auto Sync Cron Jobs](../../../advanced/18.0/advanced/auto-sync.md) for configuration details.

---


<a id="5-what-happens-if-a-sync-operation-fails"></a>

### 5. What happens if a sync operation fails?

The connector implements **partial sync** -- if individual records fail, the remaining records continue to process. Failed records are logged in the [Sync Reports](sync-reports.md) with error details. The connector also retries timed-out API calls up to 3 times with exponential backoff.

---


<a id="6-is-the-customers-password-synced-from-odoo-to-magento"></a>

### 6. Is the customer's password synced from Odoo to Magento?

No. For security reasons, passwords are **never synced** between systems. When creating a customer in Magento from Odoo, a default password is assigned. It is recommended to configure Magento to send a welcome email with a password reset link by setting the **Send Welcome Email** option to `Yes` on the customer form.

---


<a id="7-can-i-map-custom-fields-between-odoo-and-magento"></a>

### 7. Can I map custom fields between Odoo and Magento?

Yes. The [Field Mapping](../../../advanced/18.0/advanced/field-mapping.md) system allows you to map **any Odoo field to any Magento attribute**. Use the **Load New Fields** button to discover available fields from both systems, then create mapping records to define the relationships. This works for products, customers, and categories.

---


<a id="8-how-are-inventory-levels-synchronized"></a>

### 8. How are inventory levels synchronized?

Inventory is synced based on the **Auto Sync Scope** configuration. When enabled, the connector compares `qty_available` in Odoo with the Magento stock quantity and updates the target system. You can also manually trigger an inventory refresh from the **Magento > Inventory** view by clicking the **Refresh Inventory** button. See [Inventory Management](../../../advanced/18.0/advanced/inventory.md) for details.

---


<a id="9-what-should-i-do-if-the-test-connection-button-fails"></a>

### 9. What should I do if the Test Connection button fails?

If the Test Connection fails, check the following in order:

1. **Base URL** -- Ensure it includes `https://` and the correct port (if non-standard).
2. **Access Token** -- Verify the token is valid and has not expired. Generate a new one if needed.
3. **SSL** -- For local/development environments, try disabling **Verify SSL**.
4. **Network** -- Ensure the Odoo server can reach the Magento server (check firewalls, DNS resolution).
5. **Magento API** -- Verify the REST API is enabled in Magento's configuration.

See [Troubleshooting](troubleshooting.md) for detailed resolution steps.

---


<a id="10-does-the-connector-handle-taxes-and-discounts"></a>

### 10. Does the connector handle taxes and discounts?

Yes. The connector syncs order totals including **taxes** and **discounts** as they appear in Magento. Tax amounts are mapped to Odoo's tax system based on the configured tax rules. Discount amounts from Magento coupon codes or cart rules are reflected in the order line amounts. For accurate tax handling, ensure your Odoo fiscal positions and tax configurations align with your Magento tax rules.

---


<a id="still-have-questions"></a>

## Still Have Questions?

Contact the SDLC Corp support team:

- **Email**: [support@sdlccorp.com](mailto:support@sdlccorp.com)
- **Website**: [Contact SDLC Corp Support](https://sdlccorp.com/contact-us/)

---

Source: [Magento 2 Connector - Frequently Asked Questions](https://docs.sdlccorp.com/docs/18.0/magento2-odoo-connector/reference/faq/)
