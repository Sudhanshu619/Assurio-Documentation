# SDLC Magento 2 Connector for Odoo

Welcome to the official documentation for the **SDLC Corp Magento 2 Connector** -- a powerful, enterprise-grade integration module that provides seamless bidirectional synchronization between your Magento 2 store and Odoo ERP.

<a id="what-is-the-magento-2-connector"></a>

## What is the Magento 2 Connector?

The SDLC Magento 2 Connector bridges the gap between your Magento 2 eCommerce storefront and Odoo ERP backend. It automates the flow of products, customers, categories, orders, invoices, shipments, credit memos, and inventory data -- eliminating manual data entry and ensuring real-time accuracy across both platforms.

Whether you run a single Magento store or manage multiple storefronts, this connector scales to meet your business needs with robust field mapping, automated cron-based synchronization, and comprehensive reporting.

<a id="key-features"></a>

## Key Features

- **Bidirectional Product Sync** -- Push and pull products between Odoo and Magento with full attribute mapping
- **Customer Management** -- Synchronize customer records, addresses, and contact details in both directions
- **Category Sync** -- Mirror your Magento category tree in Odoo with parent-child hierarchy support
- **Order Import & Export** -- Pull orders from Magento into Odoo or push Odoo quotations to Magento
- **Invoice Synchronization** -- Create and sync invoices across both platforms automatically
- **Shipment Tracking** -- Sync shipment data and delivery status between Odoo and Magento
- **Credit Memo Support** -- Handle refunds and credit memos with full bidirectional sync
- **Inventory Management** -- Real-time stock level synchronization with warehouse-level visibility
- **Bidirectional Field Mapping** -- Map any Odoo field to any Magento field with custom mapping rules
- **Auto Sync Cron Jobs** -- Schedule automated synchronization at configurable intervals
- **Comprehensive Reporting** -- Sync reports, mapping reports, and cancelled order tracking

<a id="quick-start"></a>

## Quick Start

Get up and running in minutes:

1. [Install the module and configure your instance](../../getting-started/current/installation/getting-started.md)
2. [Set up your Magento instance connection](../../configuration/current/configuration/instances.md)
3. [Sync your products](../../data-sync/current/data-sync/products.md)
4. [Import your customers](../../data-sync/current/data-sync/customers.md)
5. [Start processing orders](../../sales/current/sales/orders.md)

<a id="requirements"></a>

## Requirements

| Requirement | Details |
| --- | --- |
| **Odoo Version** | 17.0, 18.0, 19.0 |
| **Magento Version** | Magento 2.x (Open Source or Commerce) |
| **Python** | 3.10+ |
| **Magento API** | REST API with Integration Access Token |
| **SSL** | HTTPS recommended for production environments |

Compatibility

The connector is tested and certified for Odoo 17, 18, and 19 Community and Enterprise editions. Magento 2.3+ is required for full API compatibility.

<a id="module-navigation"></a>

## Module Navigation

The connector adds a dedicated **Magento** menu to your Odoo instance with the following top-level sections:

| Menu | Description |
| --- | --- |
| **Dashboard** | Overview KPIs, charts, and sync health status |
| **Instances** | Configure and manage Magento store connections |
| **Magento Data** | Products, Customers, and Categories from Magento |
| **Mapping** | Product, Customer, and Category field mapping |
| **Sales** | Orders, Invoices, Shipments, Credit Memos, Delivery Tracking |
| **Reports** | Sync Reports, Mapping Reports, Cancelled Orders |
| **Inventory** | Stock levels and inventory synchronization |

<a id="support"></a>

## Support

- **Email**: [support@sdlccorp.com](mailto:support@sdlccorp.com)
- **Website**: [SDLC Corp](https://sdlccorp.com)
- **Contact Us**: [Get in touch with our team](https://sdlccorp.com/contact-us/)
- **Odoo App Store**: [View on Odoo Apps](https://apps.odoo.com)

---

Source: [SDLC Magento 2 Connector for Odoo](https://docs.sdlccorp.com/docs/magento2-odoo-connector/intro/)
