# Asset Management - FAQ & Troubleshooting

Common questions, troubleshooting steps, and support information for the Asset Management module.

<a id="frequently-asked-questions"></a>

## Frequently Asked Questions

<a id="which-odoo-versions-are-supported"></a>

### Which Odoo versions are supported?

The Asset Management module supports **Odoo 17.0, 18.0, and 19.0** Community Edition. Each version has its own module release (17.0.1.0.0, 18.0.1.0.0, 19.0.1.0.0).

<a id="what-modules-need-to-be-installed-before-asset-management"></a>

### What modules need to be installed before Asset Management?

The following modules are required dependencies:

| Module | Technical Name |
| --- | --- |
| **Contacts** | `base` |
| **Products** | `product` |
| **Employees** | `hr` |
| **Accounting** | `account` |
| **Inventory** | `stock` |
| **Discuss** | `mail` |

<a id="what-is-the-difference-between-single-and-multiple-asset-model-types"></a>

### What is the difference between Single and Multiple asset model types?

- **Single:** Represents one unique physical item (e.g., a laptop or vehicle). Stock is always 1.
- **Multiple:** Represents stock-based items with quantity tracking (e.g., 50 office chairs). Transfers deduct from available stock.

<a id="how-does-automatic-depreciation-work"></a>

### How does automatic depreciation work?

A daily cron job runs `generate_depreciation_entries()` on all assets that have depreciation enabled. It creates depreciation records based on the asset type's method (fixed or percentage), frequency (monthly, yearly, or days), basis (purchase price or current book value), and max entries limit.

<a id="can-i-manually-trigger-depreciation"></a>

### Can I manually trigger depreciation?

Yes. Navigate to **Settings > Technical > Scheduled Actions**, find **Generate Depreciation Entries**, and click **Run Manually**. This requires admin access.

---


<a id="troubleshooting"></a>

## Troubleshooting

<a id="the-asset-management-menu-is-not-visible"></a>

### The Asset Management menu is not visible

**Cause:** The user does not have the appropriate security group assigned.

**Solution:** Go to **Settings > Users & Companies > Users**, select the user, and assign one or more Asset Management security groups (Assets User/Admin, Transfers User/Admin, etc.).

<a id="depreciation-entries-are-not-being-generated"></a>

### Depreciation entries are not being generated

Check the following:

1. **Depreciation is enabled** on the asset form (toggle **Depreciation Apply** must be on)
2. The asset has a valid **Asset Type** with depreciation rules configured
3. The asset status is **not** "Destroyed" (destroyed assets are skipped)
4. The **maximum depreciation entries** limit has not been reached
5. The **start delay** period has passed since asset creation
6. The **frequency interval** has elapsed since the last depreciation entry
7. The cron job is active - check **Settings > Technical > Scheduled Actions**

<a id="transfer-fails-with-a-stock-validation-error"></a>

### Transfer fails with a stock validation error

**Cause:** The requested transfer quantity exceeds the available stock for a Multiple-type asset.

**Solution:** Check the asset's **Current Stock** field (Initial Stock minus Active Transfers). Either reduce the transfer quantity or return previously assigned units first.

<a id="barcode-or-serial-number-conflict"></a>

### Barcode or serial number conflict

**Cause:** Both barcode and serial number fields have uniqueness constraints.

**Solution:** Ensure the barcode or serial number you are entering is not already in use by another asset. Check existing assets using the search/filter tools.

<a id="warranty-status-is-not-updating"></a>

### Warranty status is not updating

**Cause:** Warranty status is a computed field based on the **Warranty Expiration Date**.

**Solution:** Ensure the **Expired Warranty Date** field is set on the asset form under the Vendor/Warranty section. The remaining warranty display and color-coded status are computed automatically.

<a id="location-is-not-linking-to-odoo-inventory"></a>

### Location is not linking to Odoo Inventory

**Cause:** The stock.location record may not have been created.

**Solution:** When saving an asset location without a stock.location link, the module automatically creates one. If this did not happen, manually set the **Stock Location** field on the location record under **Configuration > Locations**.

<a id="dashboard-shows-no-data"></a>

### Dashboard shows no data

**Cause:** The dashboard aggregates data from all asset records. If no assets exist, the dashboard will appear empty.

**Solution:** Create assets or install the module with demo data enabled. The demo data includes 6 assets, 4 transfers, 2 maintenance records, and 2 depreciation entries.

---


<a id="technical-reference"></a>

## Technical Reference

<a id="data-models"></a>

### Data Models

| Model | Type | Description |
| --- | --- | --- |
| `asset.management` | Persistent | Core asset records with 30+ fields |
| `asset.transfer.entry` | Persistent + mail.thread | Asset assignment/return records with chatter |
| `asset.maintenance.entry` | Persistent | Maintenance and repair logs |
| `asset.depreciation.entry` | Persistent | Individual depreciation records |
| `asset.location` | Persistent | Hierarchical location structure |
| `asset.type` | Persistent | Asset classification with depreciation rules |
| `asset.tag` | Persistent | Color-coded categorization tags |
| `asset.vendor` | Persistent | Vendor/supplier management |
| `asset.dashboard` | Persistent (read-only) | KPI aggregation with 30+ computed fields |
| `asset.label.layout` | Transient | Label printing wizard |

<a id="sequences"></a>

### Sequences

| Sequence | Prefix | Padding | Example |
| --- | --- | --- | --- |
| Asset Code | `ASSET/` | 5 | `ASSET/00001` |
| Transfer Code | `TRANSFER/` | 5 | `TRANSFER/00001` |

<a id="scheduled-actions"></a>

### Scheduled Actions

| Action | Frequency | Description |
| --- | --- | --- |
| **Generate Depreciation Entries** | Daily | Runs `generate_depreciation_entries()` on all applicable assets, creating depreciation records based on type rules |

---


<a id="support"></a>

## Support

For additional assistance with the Asset Management module:

- **Website:** [sdlccorp.com](https://sdlccorp.com)
- **Support:** [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/)
- **Email:** [sales@sdlccorp.com](mailto:sales@sdlccorp.com)

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Asset Management - FAQ & Troubleshooting](https://docs.sdlccorp.com/docs/asset-management/reference/faq/)
