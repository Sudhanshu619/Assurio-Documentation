# Field Mapping (Bidirectional)

The Field Mapping system allows you to map any Odoo field to any PrestaShop API field with full control over sync direction.

<a id="accessing-field-mappings"></a>

## Accessing Field Mappings

Navigate to **PrestaShop > Mapping** and select:

- **Product Mapping** - Map `product.template` fields to PS product fields
- **Customer Mapping** - Map `ps.customer` fields to PS customer fields
- **Category Mapping** - Map `product.category` fields to PS category fields
- **Order Mapping** - Map `ps.order` fields to PS order fields

![Product Mapping Menu](https://docs.sdlccorp.com/assets/images/PrestaShop-mapp-product-1-fddba7cce64435c546cd046be58a5d4c.webp)

<a id="creating-field-mappings"></a>

## Creating Field Mappings

Each mapping row defines a connection between one Odoo field and one PrestaShop field:

| Column | Description |
| --- | --- |
| **Mapping Type** | Product / Customer / Category / Order |
| **Instance** | Which PrestaShop store this mapping applies to |
| **Odoo Field** | Dropdown of all stored fields on the Odoo model |
| **PrestaShop Field** | Dropdown of all known PS API fields (47 product, 16 customer, 13 category, 26 order fields) |
| **Custom PS Field** | Enter a custom API field name if not in the dropdown |
| **Direction** | Bidirectional / Odoo to PS / PS to Odoo |
| **Sync on Create** | Apply this mapping when creating new records |
| **Sync on Update** | Apply this mapping when updating existing records |
| **Active** | Enable or disable this individual mapping |
| **Test** | Validate the mapping configuration |

![Product Mapping Empty](https://docs.sdlccorp.com/assets/images/PrestaShop-product-map-2-59e6000a7e1b1ef0d6dacea14415ecfa.webp)

![Product Mapping Active](https://docs.sdlccorp.com/assets/images/PrestaShop-product-map-3-af676f9ff4c7ee52b39db012f5e30252.webp)

<a id="loading-default-mappings"></a>

## Loading Default Mappings

To quickly set up standard mappings:

1. Go to any mapping view (e.g. Product Mapping)
2. Click the **Action** dropdown menu (gear icon)
3. Select **"Load New Fields"**
4. Default mappings will be created for the selected type

<a id="default-mappings-created"></a>

### Default Mappings Created

| Type | Count | Fields Included |
| --- | --- | --- |
| **Product** | 20 mappings | name, price, reference, weight, description, barcode, SEO fields, etc. |
| **Customer** | 7 mappings | first_name, last_name, email, birthday, active, group, opt-in |
| **Category** | 8 mappings | name, description, active, parent, meta fields, URL |
| **Order** | 7 mappings | reference, date, total, status, customer, note, currency |

<a id="category-mapping"></a>

## Category Mapping

![Category Mapping Empty](https://docs.sdlccorp.com/assets/images/PrestaShop-category-map-2-4d04a9950f0f292c47ca1bf0824c262a.webp)

![Category Mapping Active](https://docs.sdlccorp.com/assets/images/PrestaShop-category-map-3-08e38c1b0b0318986d2946de06fb7cd1.webp)

<a id="customer-mapping"></a>

## Customer Mapping

![Customer Mapping Empty](https://docs.sdlccorp.com/assets/images/PrestaShop-customer-map-2-0f1a2137cb503f4e90efdc772d8903d2.webp)

![Customer Mapping Active](https://docs.sdlccorp.com/assets/images/PrestaShop-customer-map-3-be2bf11f23d0f1369d500b0b408761dd.webp)

<a id="order-mapping"></a>

## Order Mapping

![Order Mapping Empty](https://docs.sdlccorp.com/assets/images/PrestaShop-order-map-2-680208df1532403dc6b7881a0246d272.webp)

![Order Mapping Active](https://docs.sdlccorp.com/assets/images/PrestaShop-order-map-3-d79f7252fb5a01dd89e824f0c8bc2bf9.webp)

<a id="sync-direction-explained"></a>

## Sync Direction Explained

| Direction | Behavior |
| --- | --- |
| **Bidirectional** | Field syncs in both directions. PS value saved to Odoo when pulling; Odoo value sent to PS when pushing. |
| **Odoo to PrestaShop** | Field only syncs when pushing data from Odoo to PrestaShop. PS values are NOT pulled into this Odoo field. |
| **PrestaShop to Odoo** | Field only syncs when pulling data from PrestaShop. Odoo values are NOT pushed to this PS field. |

tip

Use "PrestaShop to Odoo" direction for read-only fields that should only be imported. Use "Odoo to PrestaShop" for fields you manage in Odoo and want to push to your store.

<a id="need-help"></a>

## Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/)

---

Source: [Field Mapping (Bidirectional)](https://docs.sdlccorp.com/docs/19.0/prestashop-odoo-connector/configuration/field-mapping/)
