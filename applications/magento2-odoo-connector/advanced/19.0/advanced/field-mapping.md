# Bidirectional Field Mapping

The Magento 2 Connector provides a powerful field mapping system that allows you to define custom bidirectional mappings between Odoo fields and Magento fields. This gives you full control over which data flows between the two systems and how it is transformed.

<a id="mapping-types"></a>

## Mapping Types

The connector supports three types of field mapping:

| Mapping Type | Description | Menu Path |
| --- | --- | --- |
| **Product Mapping** | Map Odoo product fields to Magento product attributes | Magento > Mapping > Product Mapping |
| **Customer Mapping** | Map Odoo partner fields to Magento customer attributes | Magento > Mapping > Customer Mapping |
| **Category Mapping** | Map Odoo category fields to Magento category attributes | Magento > Mapping > Category Mapping |

<a id="accessing-field-mapping"></a>

## Accessing Field Mapping

Navigate to **Magento > Mapping** and select the mapping type you want to configure.

<a id="product-mapping"></a>

### Product Mapping

![Mapping menu showing Product Mapping](https://docs.sdlccorp.com/assets/images/mmp-1-87888429f442409223f9f772be991dc3.webp)

<a id="customer-mapping"></a>

### Customer Mapping

![Mapping menu showing Customer Mapping](https://docs.sdlccorp.com/assets/images/mmc-1-3317bd52bd4ce161e97a4fb91e1ed9b5.webp)

<a id="category-mapping"></a>

### Category Mapping

![Mapping menu showing Category Mapping](https://docs.sdlccorp.com/assets/images/mmcat-1-2ed39c878fb332bf34e137f82d7606c7.webp)

<a id="how-mapping-works"></a>

## How Mapping Works

Each mapping record defines a link between one Odoo field and one Magento field:

| Column | Description |
| --- | --- |
| **Mapping Type** | The entity type (Product, Customer, or Category) |
| **Instance** | The Magento instance this mapping applies to |
| **Odoo Field** | The Odoo model field (e.g., `Price (Magento Product Mapping)`) |
| **Magento Field** | The corresponding Magento attribute (e.g., `Name`) |
| **Active** | Enable or disable this mapping rule |

<a id="product-mapping-example"></a>

### Product Mapping Example

![Product Mapping list view](https://docs.sdlccorp.com/assets/images/mmp-11-2d6f0c603c5c9ce1b3b2f0ebff388645.webp)

In this example, the Odoo field `Price (Magento Product Mapping)` is mapped to the Magento field `Name`, meaning during sync operations the connector will synchronize these field values between the two systems.

<a id="customer-mapping-example"></a>

### Customer Mapping Example

![Customer Mapping list view](https://docs.sdlccorp.com/assets/images/mmc-11-04ff5ccef3855e98446aed3f5c3cc674.webp)

Here, the Odoo field `Phone (Magento Customer)` is mapped to the Magento field `Lastname`.

<a id="creating-a-new-mapping"></a>

## Creating a New Mapping

<a id="step-1-open-the-mapping-view"></a>

### Step 1: Open the Mapping View

Navigate to the appropriate mapping type under **Magento > Mapping**.

<a id="step-2-click-new"></a>

### Step 2: Click New

Click the **New** button to create a new mapping record.

<a id="step-3-configure-the-mapping"></a>

### Step 3: Configure the Mapping

![Product Mapping form](https://docs.sdlccorp.com/assets/images/mmpp-111-14070c4ec259128cbb5a6cfa0862f724.webp)

1. **Mapping Type** -- Pre-filled based on the mapping view (Product, Customer, or Category).
2. **Instance** -- Select the Magento instance. This is especially important if you have multiple stores connected.
3. **Odoo Field** -- Select the Odoo field from the dropdown. The connector dynamically loads available fields from the relevant Odoo model.
4. **Magento Field** -- Select the Magento attribute from the dropdown.
5. **Active** -- Check to enable this mapping.

![Customer Mapping form](https://docs.sdlccorp.com/assets/images/mmc-111-26350c6d5cdbb4f64e41e1dd6a373cf5.webp)

![Category Mapping form](https://docs.sdlccorp.com/assets/images/mmcat-111-496946cf4c6b15381e5fa074308de1a6.webp)

Multi-Store

If you have connected multiple Magento stores, select the specific instance to apply the mapping only to that store. Leave blank to apply globally.

<a id="loading-available-fields"></a>

## Loading Available Fields

Click the **Load New Fields** button (green button in the toolbar) to refresh the list of available Odoo and Magento fields. This is useful when:

- You have added new custom attributes in Magento
- You have installed new Odoo modules that add fields to product or partner models
- Field lists appear empty or incomplete

![Category Mapping with Load New Fields button](https://docs.sdlccorp.com/assets/images/mmcat-11-67b9d2e32999b9ca914ea4dabe7e65a3.webp)

tip

After installing new modules or adding custom attributes in Magento, always click **Load New Fields** to ensure the latest fields are available for mapping.

<a id="testing-mappings"></a>

## Testing Mappings

Click the **Test** button (red button in the toolbar) to validate your mapping configuration:

1. The connector attempts to read the mapped fields from both systems.
2. It verifies that the field types are compatible.
3. A success or error message is displayed.

warning

Incompatible field types (e.g., mapping a text field to a numeric field) may cause sync errors. Always test your mappings after creating or modifying them.

<a id="advanced-features"></a>

## Advanced Features

- **Multiple Mappings per Entity** -- You can create as many mapping rules as needed for each entity type. All active mappings are applied during sync operations.
- **Instance-Specific Mappings** -- Different Magento stores can have different mapping configurations.
- **Dynamic Field Discovery** -- The connector introspects both Odoo models and the Magento API to discover available fields.
- **Selective Sync** -- Only mapped fields are synchronized, giving you precise control over data flow.

<a id="best-practices"></a>

## Best Practices

1. **Start with defaults** -- The connector includes sensible default mappings for common fields. Only add custom mappings when needed.
2. **Test before production** -- Always test new mappings in a staging environment first.
3. **Document your mappings** -- Keep a record of custom mappings for reference during troubleshooting.
4. **Use consistent naming** -- Name your mapping records clearly to identify them at a glance.

<a id="next-steps"></a>

## Next Steps

- [Configure Auto Sync](auto-sync.md)
- [Manage Inventory](inventory.md)
- [View Mapping Reports](../../../reference/19.0/reference/sync-reports.md)

---

Source: [Bidirectional Field Mapping](https://docs.sdlccorp.com/docs/19.0/magento2-odoo-connector/advanced/field-mapping/)
