# Catalog Management

Navigate to **PrestaShop > Catalog** for all catalog-related data.

<a id="products"></a>

## Products

Synced products appear in **Catalog > Products**. Each product has a **PrestaShop** tab in the form view.

![Product List](https://docs.sdlccorp.com/assets/images/PrestaShop-product-2-993ef1869c70065bb04acc1d886cbc60.webp)

<a id="product-form-fields"></a>

### Product Form Fields

Each product contains the following PrestaShop-specific data:

- **PrestaShop Product ID**, Instance, Active status
- **Type**: Standard / Combinations / Pack / Virtual
- **Brand**, Categories, Related Products
- **Short Description**, Full Description (HTML)
- **SEO fields**: Meta Title, Meta Description, Friendly URL
- **Barcodes**: EAN13, ISBN, UPC, MPN
- **Stock**: Quantity, Low Stock Threshold, Stock Location
- **Pricing**: Wholesale Price, Tax Rules, Unit Price
- **Options**: Visibility, Condition, Available for Order, Show Price
- **Shipping**: Weight, Dimensions, Delivery Times
- **Features**, Customization Fields, Attachments

![Product Form](https://docs.sdlccorp.com/assets/images/PrestaShop-product-3-a78ac3936aa6c2cca0a89c61716ecf3e.webp)

![Product Details](https://docs.sdlccorp.com/assets/images/PrestaShop-prodcut-4-137f73a50c382ce1512deca632916fbb.webp)

---


<a id="categories"></a>

## Categories

Synced categories retain their parent-child hierarchy.

![Category List](https://docs.sdlccorp.com/assets/images/PrestaShop-categories-2-2868f0da3e7db5982d45281e660a3d82.webp)

<a id="category-form"></a>

### Category Form

![Category Form](https://docs.sdlccorp.com/assets/images/PrestaShop-categories-3-e02a9c5073d1ea0699d2ec0034c9a9f3.webp)

Each category includes:

| Field | Description |
| --- | --- |
| **Name** | Category display name |
| **Displayed** | Whether visible in PrestaShop |
| **Description** | Category description |
| **Additional Description** | Extended description |
| **Cover Image** | Main category banner |
| **Thumbnail** | Category thumbnail and menu icon |
| **SEO** | Meta title, description, keywords, friendly URL |
| **PrestaShop Connection** | Category ID mapping |

![Category Details](https://docs.sdlccorp.com/assets/images/PrestaShop-categories-4-8394286516e205ffe5c3cb53841cabeb.webp)

---


<a id="brands"></a>

## Brands

Manage product brands and manufacturers. Brands can be created in PrestaShop directly from Odoo using the **"Create in PrestaShop"** button.

![Brands List](https://docs.sdlccorp.com/assets/images/PrestaShop-brands-2-6758a46ee6d2a487cbc51ffbdaf19163.webp)

![Brand Form](https://docs.sdlccorp.com/assets/images/PrestaShop-brands-3-dba7e2a5f3db4ff749be4b629ad0b313.webp)

![Brand Details](https://docs.sdlccorp.com/assets/images/PrestaShop-brands-4-10f93cbdb11fbac16602be0a740bf3b7.webp)

---


<a id="suppliers"></a>

## Suppliers

![Suppliers List](https://docs.sdlccorp.com/assets/images/PrestaShop-supplier-2-059ca14144cadae0e17f263db731e1b8.webp)

![Supplier Form](https://docs.sdlccorp.com/assets/images/PrestaShop-supplier-3-3634517f3b9866d55a257b766d5fade1.webp)

Suppliers can also be created in PrestaShop directly from Odoo:

![Supplier Details](https://docs.sdlccorp.com/assets/images/PrestaShop-supplier-4-ad1d18b49c3d10295baed8c067300fd1.webp)

---


<a id="attributes--features"></a>

## Attributes & Features

Product attributes (size, color) and features (material, origin) are synced with their values.

<a id="attributes"></a>

### Attributes

![Attributes List](https://docs.sdlccorp.com/assets/images/PrestaShop-attributes-2-3f8b94d697afa59efe1c3cd12d561e52.webp)

![Attribute Form](https://docs.sdlccorp.com/assets/images/PrestaShop-attributes-3-fd4a91569552518be43604f30d1f8b12.webp)

![Attribute with Values](https://docs.sdlccorp.com/assets/images/PrestaShop-attributes-4-766eda8688c6bf220e3bd621d3e2f2ad.webp)

<a id="attribute-values"></a>

### Attribute Values

![Attribute Values List](https://docs.sdlccorp.com/assets/images/PrestaShop-attr-values-1-89a269c52c44e0b04a099bc9e9619403.webp)

![Attribute Value Form](https://docs.sdlccorp.com/assets/images/PrestaShop-attr-values-2-8efe90867a8a4ac0f4df631270db4d44.webp)

Use the **Generate Combinations** wizard to create product variants from synced attributes.

<a id="features"></a>

### Features

![Features List](https://docs.sdlccorp.com/assets/images/PrestaShop-features-2-71213cd13bc996b46149bc1d806650fb.webp)

![Feature Form](https://docs.sdlccorp.com/assets/images/PrestaShop-features-3-a185c98c7ecbcb7ab141cd8ec4fea093.webp)

![Feature with Values](https://docs.sdlccorp.com/assets/images/PrestaShop-features-4-072be1ca51c1d3be0ca49ed04c7907b4.webp)

---


<a id="discounts"></a>

## Discounts

<a id="cart-rules-promotions"></a>

### Cart Rules (Promotions)

Cart rules are promotional codes and automatic discounts applied at checkout.

![Cart Rules List](https://docs.sdlccorp.com/assets/images/PrestaShop-cart.rules-2-ce6d295dc7dd76308fec20b32627a35a.webp)

The form has three tabs: **Information**, **Conditions**, and **Actions**.

![Cart Rule Form](https://docs.sdlccorp.com/assets/images/PrestaShop-cart.rules-3-db94c8ddf01c26ef478f523db1b8b05a.webp)

![Cart Rule Populated](https://docs.sdlccorp.com/assets/images/PrestaShop-cart.rules-4-9b19d95d805d94dccb850d1a719b1bc5.webp)

<a id="catalog-price-rules-bulk-discounts"></a>

### Catalog Price Rules (Bulk Discounts)

Catalog price rules apply automatic discounts based on quantity, customer group, or date range.

![Catalog Rules List](https://docs.sdlccorp.com/assets/images/PrestaShop-catalog.price-2-bbeda1a727c1621ccb86d911117ff8c4.webp)

![Catalog Rule Form](https://docs.sdlccorp.com/assets/images/PrestaShop-catalog.price-3-bb8a359cbdd03fd992fd448dae41f04c.webp)

![Catalog Rule Details](https://docs.sdlccorp.com/assets/images/PrestaShop-catalog.price-4-4db9e0ce9e1f3664b84e11d93111cc8d.webp)

tip

Use cart rules for promotional codes (e.g. "SUMMER10"). Use catalog price rules for volume discounts (e.g. buy 10+ for 15% off).

---


<a id="files"></a>

## Files

Manage downloadable files attached to products (manuals, guides, etc.):

![Files List](https://docs.sdlccorp.com/assets/images/PrestaShop-files-2-b1046bec6f4beff6ff0aa9cd414f822c.webp)

![File Upload Form](https://docs.sdlccorp.com/assets/images/PrestaShop-files-3-b10f8403069bad2d7865ff949ca23683.webp)

<a id="need-help"></a>

## Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/)

---

Source: [Catalog Management](https://docs.sdlccorp.com/docs/18.0/prestashop-odoo-connector/products/catalog-management/)
