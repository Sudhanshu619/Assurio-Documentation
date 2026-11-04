# SDLC Maintenance QR Code

A module for Odoo 17, 18, and 19 Community Edition that generates unique equipment codes, creates scannable QR codes for maintenance equipment, and prints professional QR label sheets in multiple layouts. Warehouse and maintenance teams can scan QR labels on physical equipment to instantly pull up the corresponding record in Odoo -- no manual searching required.

![Maintenance Teams overview in Odoo](https://docs.sdlccorp.com/assets/images/photo2-336290096b51ee3b426068e2ada28a7b.webp)

<a id="key-features"></a>

## Key Features

| Feature | Description |
| --- | --- |
| **Auto Equipment Codes** | Unique codes generated automatically on creation using a yearly-resetting sequence (`MEQ/2026/00001`) |
| **Scannable QR Codes** | QR codes encode a direct URL to the equipment form -- scan with any mobile device to open the record |
| **Label Printing** | Print professional QR label sheets in Dymo, 2x7, 4x7, or custom layouts with zero-margin PDF output |
| **Custom Header Color** | Choose the label header color via a color picker to match your company branding |
| **Multi-Copy Printing** | Print multiple copies of each label in a single batch for placing on equipment and spare tracking |
| **Manager-Only Code Generation** | Equipment code generation restricted to Equipment Managers for controlled asset tracking |

<a id="capabilities-overview"></a>

## Capabilities Overview

| Capability | Description |
| --- | --- |
| **Equipment Code** | Auto-generated unique code per equipment: `MEQ/YYYY/NNNNN` |
| **QR Code Preview** | Live QR code displayed in a dedicated tab on the equipment form |
| **QR Payload URL** | Encodes direct deep-link: `<base_url>/web#id=<id>&model=maintenance.equipment&view_type=form` |
| **Label Layouts** | Dymo (1x1), 2x7, 4x7, or fully custom columns and rows |
| **Label Header** | "PROPERTY OF [company]" banner with customizable color |
| **PDF Output** | Zero-margin A4 portrait for direct printing to label sheets |
| **Batch Printing** | Select multiple equipment from list view and print all labels at once |
| **Search & Filter** | Equipment code added to search view for quick lookup |

<a id="supported-versions"></a>

## Supported Versions

| Detail | Value |
| --- | --- |
| **Odoo Version** | 17.0, 18.0, 19.0 (Community Edition) |
| **Module Version** | 17.0.1.0.0 / 18.0.1.0.0 / 19.0.1.0.0 |
| **Category** | Maintenance |
| **License** | LGPL-3 |

<a id="quick-start"></a>

## Quick Start

1. [Installation and Setup](../../getting-started/current/getting-started/setup.md)
2. [Equipment Codes](../../usage-guide/current/usage/equipment-codes.md)
3. [Printing Labels](../../usage-guide/current/usage/printing-labels.md)

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [SDLC Maintenance QR Code](https://docs.sdlccorp.com/docs/maintenance-qr-code/intro/)
