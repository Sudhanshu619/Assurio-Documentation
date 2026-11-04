# Category Management

The Magento 2 Connector synchronizes product categories between Odoo and Magento, preserving the parent-child hierarchy. Categories can be pulled from Magento or created in Magento directly from Odoo.

<a id="accessing-magento-categories"></a>

## Accessing Magento Categories

Navigate to **Magento > Magento Data > Categories** to view all synced categories.

![Magento Data menu showing Categories option](https://docs.sdlccorp.com/assets/images/mcat-1-4d81639d10e6fa6a35957956b87cd6f3.webp)

<a id="category-list-view"></a>

## Category List View

The category list displays all synchronized categories with their hierarchy:

![Magento Categories list view](https://docs.sdlccorp.com/assets/images/mcat-11-cc6581add785d20981cd29e7654464db.webp)

| Column | Description |
| --- | --- |
| **Instance** | The Magento instance this category belongs to |
| **Magento** | The Magento category ID |
| **Name** | Category name |
| **Parent** | Parent category name (for subcategories) |
| **Is Active** | Whether the category is active in Magento |

The list view clearly shows the category hierarchy. For example:

- **Default Category** (root)
  - **farhan** (child of Default Category)
    - **electronics** (child of farhan)
  - **cloth** (child of Default Category)
  - **Plastic** (child of Default Category)
- **Magento Category 1** (root)
  - **Limon** (child of farhan)

<a id="category-form"></a>

## Category Form

Click **New** to create a new category or click an existing category to edit it.

![Magento Category form view](https://docs.sdlccorp.com/assets/images/mcat-111-b76d491ec03d341911958f48796eff5f.webp)

| Field | Description |
| --- | --- |
| **Instance** | Select the Magento instance |
| **Magento** | The Magento category ID (auto-populated on sync) |
| **Name** | Category name |
| **Parent** | Select the parent category for hierarchy placement |
| **Is Active** | Enable or disable the category |

<a id="category-actions"></a>

## Category Actions

| Action | Description |
| --- | --- |
| **Sync Categories** (from Instance) | Pull all categories from Magento into Odoo, preserving hierarchy |
| **Create in Magento** | Push a new category from Odoo to Magento |

<a id="syncing-categories"></a>

## Syncing Categories

<a id="pull-categories-from-magento"></a>

### Pull Categories from Magento

1. Navigate to **Magento > Instances**.
2. Open your instance.
3. Click **Sync Categories**.
4. The connector imports all Magento categories with their parent-child relationships.

<a id="create-a-category-in-magento"></a>

### Create a Category in Magento

1. Go to **Magento > Magento Data > Categories**.
2. Click **New**.
3. Select the **Instance**.
4. Enter the **Name**.
5. Select a **Parent** category (or leave blank for a root category).
6. Ensure **Is Active** is checked.
7. Click **Create in Magento**.

info

Category hierarchy is fully preserved during synchronization. When you sync categories, child categories are automatically linked to their parent categories in Odoo.

tip

Categories synced from Magento can be used in product records to maintain consistent categorization across both platforms.

<a id="next-steps"></a>

## Next Steps

- [Manage Products](products.md)
- [Configure Category Field Mapping](../../../advanced/19.0/advanced/field-mapping.md)
- [Process Orders](../../../sales/19.0/sales/orders.md)

---

Source: [Category Management](https://docs.sdlccorp.com/docs/19.0/magento2-odoo-connector/data-sync/categories/)
