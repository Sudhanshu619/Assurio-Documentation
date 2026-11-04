# Maintenance QR Code - Troubleshooting and FAQ


<a id="common-issues"></a>

## Common Issues

<a id="equipment-code-not-generated"></a>

### Equipment Code Not Generated

- Verify the module `sdlc_maintenance_qr_code` is installed and up to date
- For existing equipment, click the **Generate Code** button -- this requires **Equipment Manager** group membership
- New equipment receives codes automatically on creation regardless of user group

<a id="generate-code-button-not-visible"></a>

### Generate Code Button Not Visible

- The button is only visible to users in the **Equipment Manager** group (`maintenance.group_equipment_manager`)
- The button is hidden once an equipment code has already been assigned
- Check your user's groups under **Settings > Users & Companies > Users**

<a id="qr-code-not-displaying"></a>

### QR Code Not Displaying

- Ensure the equipment has an assigned **Equipment Code** -- QR fields are empty when no code exists
- Navigate to the **QR Code** tab on the equipment form to view the preview
- QR fields recompute automatically when `x_equipment_code` or `company_id` changes

<a id="duplicate-code-error"></a>

### Duplicate Code Error

- A SQL uniqueness constraint (`UNIQUE(x_equipment_code)`) prevents duplicate codes
- This should not occur under normal operation since codes are assigned via `ir.sequence`
- If you encounter this error, check if the sequence was manually modified

<a id="labels-not-aligned-when-printing"></a>

### Labels Not Aligned When Printing

- Set your printer to **"Actual size"** (not "Fit to page")
- The PDF uses zero-margin A4 portrait format -- ensure your printer supports borderless printing
- Check that the correct label layout matches your physical label sheets

<a id="special-characters-appearing-incorrectly-on-labels"></a>

### Special Characters Appearing Incorrectly on Labels

- The module includes built-in mojibake repair (`_repair_mojibake`) for corrupted UTF-8 text
- HTML entity encoding (`_qr_display_html_entities`) handles special characters in PDF rendering
- If issues persist, check the original equipment name for encoding problems

<a id="qr-code-scan-opens-login-page"></a>

### QR Code Scan Opens Login Page

- The scanning user must be logged into Odoo in their browser
- After authentication, the user will be forwarded to the equipment record
- Ensure the Odoo instance URL is accessible from the scanning device's network

<a id="data-model-reference"></a>

## Data Model Reference

<a id="maintenanceequipment-extended"></a>

### maintenance.equipment (Extended)

| Field | Type | Properties | Description |
| --- | --- | --- | --- |
| `x_equipment_code` | Char | unique, indexed, tracked, copy=False | Auto-generated equipment code (MEQ/YYYY/NNNNN) |
| `x_qr_payload` | Char | computed, readonly | Full URL encoded in the QR code |
| `x_qr_url` | Char | computed, readonly | URL to the barcode image endpoint |
| `x_qr_image_html` | Html | computed, readonly, sanitize=False | HTML img tag rendering the QR code |
| `x_qr_name_display` | Char | computed | Mojibake-repaired equipment name for display |
| `x_qr_name_entities` | Char | computed | HTML-entity-encoded name for safe PDF rendering |

<a id="key-methods"></a>

### Key Methods

| Method | Description |
| --- | --- |
| `create(vals_list)` | Overridden to auto-assign equipment code on creation |
| `action_generate_equipment_code()` | Button action for manually generating codes (manager only) |
| `action_open_qr_print_wizard()` | Opens the print wizard modal with selected equipment |
| `_assign_equipment_code_if_needed()` | Assigns next code from ir.sequence if not already set |
| `_compute_qr_fields()` | Computes QR payload, URL, and HTML image |
| `_repair_mojibake(text)` | Static: fixes UTF-8 text decoded as latin-1/cp1252 |
| `_qr_display_html_entities(text)` | Static: converts text to HTML entities |
| `_qr_display_code()` | Returns equipment code or empty string for report use |

<a id="maintenanceqrprintwizard-transient"></a>

### maintenance.qr.print.wizard (Transient)

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `equipment_ids` | Many2many | From context | Equipment records to print labels for |
| `copies` | Integer | 1 | Number of copies per equipment |
| `size` | Selection | 2x7xprice | Label layout (dymo, 2x7, 4x7, custom) |
| `custom_columns` | Integer | 2 | Custom column count |
| `custom_rows` | Integer | 7 | Custom row count |
| `header_color` | Char | #6b4096 | Label header background color |
| `rows` | Integer | computed | Effective row count |
| `columns` | Integer | computed | Effective column count |

<a id="report-abstract-model"></a>

### Report Abstract Model

Model: `report.sdlc_maintenance_qr_code.report_maintenance_equipment_qr` (AbstractModel)

The `_get_report_values()` method returns:

| Key | Description |
| --- | --- |
| `pages` | List of pages, each page is a list of rows, each row is a list of equipment |
| `columns` | Number of columns per row |
| `rows` | Number of rows per page |
| `qr_px` | QR code pixel size (260, 280, or 320) |
| `header_color` | Hex color for the label header |
| `company` | Current company record |

<a id="report-engine"></a>

## Report Engine

<a id="report-action"></a>

### Report Action

| Property | Value |
| --- | --- |
| **Report ID** | `action_report_maintenance_equipment_qr` |
| **Model** | `maintenance.qr.print.wizard` |
| **Report Type** | `qweb-pdf` |
| **Report Name** | `sdlc_maintenance_qr_code.report_maintenance_equipment_qr` |

<a id="qweb-templates"></a>

### QWeb Templates

| Template | Purpose |
| --- | --- |
| `report_simple_qr_label_cell` | Renders a single label cell (header + QR + code + name) |
| `report_maintenance_equipment_qr` | Main report: iterates pages > rows > cells, calling the cell template |

<a id="module-information"></a>

## Module Information

| Detail | Value |
| --- | --- |
| **Module Name** | sdlc_maintenance_qr_code |
| **Display Name** | SDLC Maintenance QR Code |
| **Version** | 17.0.1.0.0 / 18.0.1.0.0 / 19.0.1.0.0 |
| **Category** | Maintenance |
| **Author** | SDLC Corp |
| **License** | LGPL-3 |
| **Dependencies** | maintenance |
| **Models** | 1 extended (maintenance.equipment) + 1 transient (wizard) + 1 abstract (report) |
| **Views** | 3 inherited (form, tree, search) + 1 wizard form |
| **Reports** | 1 QWeb PDF report with 2 templates |

<a id="support"></a>

## Support

| Channel | Details |
| --- | --- |
| **Website** | [sdlccorp.com](https://sdlccorp.com/) |
| **Email** | [sales@sdlccorp.com](mailto:sales@sdlccorp.com) |
| **Compatible Odoo** | Odoo 17, 18, 19 Community Edition |
| **License** | LGPL-3 |

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Maintenance QR Code - Troubleshooting and FAQ](https://docs.sdlccorp.com/docs/19.0/maintenance-qr-code/reference/faq/)
