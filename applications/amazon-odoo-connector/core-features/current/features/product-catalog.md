# Product Catalog

Full product sync between Amazon and Odoo with support for ASINs, variations, categories, and bulk operations.

<a id="product-identifiers"></a>

## Product Identifiers

Each product syncs with complete Amazon identification:

| Identifier | Description |
| --- | --- |
| **SKU** | Seller SKU (internal reference) |
| **ASIN** | Amazon Standard Identification Number |
| **Parent ASIN** | Parent product for variations |
| **FNSKU** | Fulfillment Network SKU (FBA) |
| **Barcode** | GTIN / EAN / UPC |

<a id="12-product-categories"></a>

## 12 Product Categories

The connector supports specialized fields for each category:

| Category | Specialized Fields |
| --- | --- |
| **Footwear** | Size, material, gender, sport type |
| **Clothing** | Size, color, material, fit, style |
| **Electronics** | Brand, model, specifications |
| **Beauty** | Ingredients, skin type, volume |
| **Home** | Dimensions, material, room type |
| **Sports** | Sport type, skill level, athlete |
| **Food** | Ingredients, allergens, weight |
| **Books** | Author, ISBN, publisher, format |
| **Toys** | Age range, material, safety certs |
| **Jewelry** | Material, stone type, weight |
| **Automotive** | Make, model, year, part number |
| **General** | Standard product fields |

<a id="variations"></a>

## Variations

Products support the following variation attributes:

- Color
- Size
- Material
- Pattern
- Style
- Athlete
- ...and more (customizable per category)

<a id="seo-content"></a>

## SEO Content

Each product supports rich SEO content:

- Up to **5 bullet points** per product (SEO-optimized)
- Rich product description
- **9 product image slots** with URL download capability
- Backend search keywords (max 250 chars)

<a id="bulk-import-via-csvexcel"></a>

## Bulk Import via CSV/Excel

Navigate to **Catalog > Import / Map Products**. The wizard supports 4 operations:

| Operation | Purpose |
| --- | --- |
| **Map** | Link existing Odoo products to Amazon SKUs by matching |
| **Import** | Create new Odoo products from Amazon catalog data |
| **Update Prices** | Bulk update Amazon prices from CSV |
| **Update Stock** | Bulk update inventory levels from CSV |

<a id="gtin-exemption"></a>

## GTIN Exemption

tip

For handmade or custom products without a GTIN/EAN/UPC, enable **GTIN Exemption** on the product form. The connector will submit the product without a barcode identifier.

<a id="scheduled-product-sync"></a>

## Scheduled Product Sync

| Scheduled Action | Interval |
| --- | --- |
| **Sync Products** | Every 6 hours |

This pulls product data updates from Amazon (title, description, images, categories) and applies changes to Odoo.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Product Catalog](https://docs.sdlccorp.com/docs/amazon-odoo-connector/features/product-catalog/)
