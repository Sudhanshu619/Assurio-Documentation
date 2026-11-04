# PrestaShop Connector - Frequently Asked Questions


<a id="common-questions"></a>

## Common Questions

<a id="can-i-connect-multiple-prestashop-stores"></a>

### Can I connect multiple PrestaShop stores?

Yes. Create a separate instance configuration for each store. All data is tagged with the instance ID, so products from different stores are kept separate.

---


<a id="does-the-mapping-work-in-both-directions"></a>

### Does the mapping work in both directions?

Yes. Set the Direction to "Bidirectional" and the field will sync both ways - from PS to Odoo when pulling, and from Odoo to PS when pushing.

---


<a id="what-happens-if-i-disable-a-mapping"></a>

### What happens if I disable a mapping?

The mapping is ignored during sync. The built-in sync logic still handles standard fields. Only custom mappings you created are affected.

---


<a id="can-i-map-a-field-that-is-not-in-the-dropdown"></a>

### Can I map a field that is not in the dropdown?

Yes. Use the "Custom PS Field" column to enter any PrestaShop API field name manually.

---


<a id="how-do-i-reset-field-mappings"></a>

### How do I reset field mappings?

Delete the existing mappings and use **Action > Load New Fields** to recreate defaults.

---


<a id="does-auto-sync-create-reports"></a>

### Does auto sync create reports?

Yes. Every auto sync run generates a Sync Report with detailed success/error logs. View them from the Auto Sync Cron tab or **PrestaShop > Reports > Sync Reports**.

---


<a id="what-order-does-auto-sync-run-entities"></a>

### What order does auto sync run entities?

Categories > Brands > Suppliers > Attributes > Features > Taxes > Carriers > Products > Customers (dependencies first).

---


<a id="can-i-run-auto-sync-manually"></a>

### Can I run auto sync manually?

Yes. Click **"Run Sync Now"** on the Auto Sync Cron tab to trigger it immediately.

---


<a id="how-do-i-get-support"></a>

### How do I get support?

Contact SDLC Corp via [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email [sales@sdlccorp.com](mailto:sales@sdlccorp.com).

---

Source: [PrestaShop Connector - Frequently Asked Questions](https://docs.sdlccorp.com/docs/17.0/prestashop-odoo-connector/reference/faq/)
