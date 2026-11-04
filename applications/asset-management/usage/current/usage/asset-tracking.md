# Asset Tracking & Lifecycle

Create, categorize, and track assets through their entire lifecycle - from procurement to disposal - with full visibility into status, condition, location, transfers, maintenance, and financial details.

<a id="asset-kanban-view"></a>

## Asset Kanban View

The main **Assets** view displays all assets in a Kanban board grouped by status, with rich cards showing type, tags, assigned user, stock levels, financials, and warranty information.

![Asset Kanban view showing assets grouped by status with details like purchase price, book value, and warranty](https://docs.sdlccorp.com/assets/images/photo2-da4f4647ca020f651519ee4565f53053.webp)

<a id="creating-assets"></a>

## Creating Assets

Navigate to **Asset Management > Assets** and click **New** to create an asset record.

<a id="asset-form---basic--financial-information"></a>

### Asset Form - Basic & Financial Information

The asset form is organized into tabs covering all aspects of an asset record.

![Asset form showing basic information and financial details for ASSET/00001](https://docs.sdlccorp.com/assets/images/photo3-df3944825c4cd4bdf2582a29ce108a5f.webp)

| Tab | Fields |
| --- | --- |
| **Basic Information** | Product, Asset Type, Tags, Serial Number, Barcode, Model Type (Single/Multiple), Initial Stock, Condition, Department, Responsible User, Status |
| **Financial** | Purchase Price, Invoice Date, Invoice Link, Current Book Value (computed), Total Depreciation (computed), Total Maintenance Cost (computed) |
| **Depreciation** | Enable Depreciation toggle, Last Depreciation Date, Depreciation Count, Inline depreciation entries table |
| **Maintenance** | Next Maintenance Date (computed), Maintenance Count, Inline maintenance entries table |
| **Vendor / Warranty** | Vendor, Warranty Expiration Date, Remaining Warranty (computed with color), Warranty Status badge |
| **Assignment / Location** | Current Location, Assigned User (computed), Assigned By (computed), Transfer Count, Inline transfer entries table |
| **Documentation** | Notes (text), Document Attachments (many2many to ir.attachment) |

<a id="auto-generated-fields"></a>

### Auto-Generated Fields

- **Asset Code:** Auto-generated via sequence (`ASSET/00001`), readonly
- **Current Book Value:** Purchase Price minus Total Depreciation
- **Current Stock:** Initial Stock minus Active Transfers (for multiple assets)
- **Assigned User / Assign By / Current Location:** Derived from the latest active transfer

<a id="validation-rules"></a>

### Validation Rules

Constraints

- Barcode must be unique across all assets
- Serial number must be unique across all assets
- Purchase price must be greater than or equal to 0

<a id="asset-documentation--transfer-history"></a>

## Asset Documentation & Transfer History

The asset form includes tabs for documentation, internal notes, and a complete transfer history showing all assignment records.

![Asset form documentation tab showing attached documents, internal notes, and transfer history](https://docs.sdlccorp.com/assets/images/photo4-bea6271c839c7409e1540952666eb5b4.webp)

<a id="depreciation--maintenance-settings"></a>

## Depreciation & Maintenance Settings

Each asset has dedicated sections for depreciation settings (when enabled) and maintenance information, along with vendor and warranty details.

![Asset form showing depreciation settings, maintenance information, and documentation section](https://docs.sdlccorp.com/assets/images/photo5-87897ce1d2bfb0a7f1429a67a09705bb.webp)

<a id="asset-lifecycle-statuses"></a>

## Asset Lifecycle Statuses

Assets move through 6 statuses throughout their lifecycle. Status is displayed as colored badges on the asset form and Kanban cards.

| Status | Description | Badge Color |
| --- | --- | --- |
| **Assign** | Asset is assigned to an employee | Blue |
| **Return** | Asset has been returned from assignment | Green |
| **On Hold** | Asset is temporarily unavailable | Orange |
| **In Warehouse** | Asset is in storage / warehouse | Purple |
| **Repair** | Asset is undergoing maintenance or repair | Orange |
| **Destroyed** | Asset has been disposed / written off | Red |

<a id="asset-conditions"></a>

## Asset Conditions

Track the physical condition of each asset using 5 levels:

| Condition | Color |
| --- | --- |
| New | Green |
| Good | Blue |
| Fair | Orange |
| Poor | Orange |
| Damaged | Red |

<a id="stock-management"></a>

## Stock Management

The module supports two asset model types for different use cases.

| Model Type | Description | Example |
| --- | --- | --- |
| **Single** | One unique physical item. Initial stock = 1. Transfers always move 1 unit. | Laptop, Vehicle, CNC Machine |
| **Multiple** | Stock-based items. Set initial quantity. Transfers deduct from available stock. | 50 Office Chairs, 25 Monitors |

<a id="stock-calculations"></a>

### Stock Calculations

| Field | Formula |
| --- | --- |
| **Initial Stock** | Set manually on creation (default: 1) |
| **Active Transfers** | Sum of `stock_qty` from all transfers with status = "assigned" |
| **Current Stock** | `Initial Stock - Active Transfers` |

Stock Validation

When creating a transfer for a multiple-asset, the module validates that sufficient stock is available. If the requested quantity exceeds current stock, a validation error is raised.

<a id="barcode-label-printing"></a>

## Barcode Label Printing

Print professional barcode labels for physical asset identification directly from the asset form using the **Print Label** button.

![Printed barcode label showing company name, barcode, asset code ASSET/00001, and purchase price](data:image/webp;base64,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)

<a id="label-formats"></a>

### Label Formats

| Format | Dimensions | Price | Best For |
| --- | --- | --- | --- |
| **Dymo** | 57 x 32mm | Optional | Dymo label printers |
| **2 x 7 with Price** | 97 x 37.1mm | Yes (top-right) | Standard label sheets |
| **4 x 7 with Price** | 47 x 37.1mm | Yes | Medium labels |
| **4 x 12 with Price** | 43 x 19mm | Yes | Small labels |
| **4 x 12 no Price** | 43 x 19mm | No | Small labels, no price |
| **Custom** | User-defined | Configurable | Custom label sheets |

<a id="transfer-management"></a>

## Transfer Management

Assign assets to employees, track from/to locations, manage returns, and maintain full audit trails via chatter.

![Transfer list view showing transfer codes, assigned employees, dates, locations, and statuses](https://docs.sdlccorp.com/assets/images/photo8-2983067f1185e2096d4bc85e2e04db0e.webp)

<a id="transfer-fields"></a>

### Transfer Fields

| Field | Description |
| --- | --- |
| **Transfer Code** | Auto-generated (`TRANSFER/00001`), unique, readonly |
| **Asset** | The asset being transferred (tracked) |
| **Employee** | Employee receiving the asset (tracked) |
| **Assign Date** | Date of assignment (tracked) |
| **Assigned By** | User who created the transfer (auto-filled, tracked) |
| **From Location** | Source location (dropdown + text, tracked) |
| **To Location** | Destination location (dropdown + text, tracked) |
| **Return Date** | When the asset was returned (must be >= assign date) |
| **Quantity** | Number of units (for multiple-asset types, default: 1) |
| **Status** | `Assigned`, `Returned`, or `Under Maintenance` (tracked) |

Chatter Tracking

All key fields are tracked. Changes to asset, employee, dates, locations, and status are automatically logged as chatter messages with before/after values.

<a id="vendor-management"></a>

## Vendor Management

Manage suppliers and service providers with contact details, service capabilities, ratings, and linked asset and maintenance records.

![Vendor list showing vendor names, contacts, phone numbers, emails, service areas, and ratings](https://docs.sdlccorp.com/assets/images/photo7-837ed0d77b8344f1283d067f51d24071.webp)

<a id="vendor-fields"></a>

### Vendor Fields

| Section | Fields |
| --- | --- |
| **Profile** | Name, Address, Location/Region, Website, Tax ID, Rating (1-5 stars) |
| **Contact** | Contact Person, Phone, Email (validated) |
| **Services** | Repair Service (toggle), Maintenance Service (toggle), Additional Services (toggle) |
| **Counts** | Asset Count (computed), Maintenance Count (computed) - clickable stat buttons |

<a id="maintenance--repair"></a>

## Maintenance & Repair

Log corrective, preventive, and predictive maintenance with vendor tracking, cost recording, priority levels, and document attachments.

![Maintenance/Repair list showing asset references, types, priorities, vendors, costs, dates, and statuses](https://docs.sdlccorp.com/assets/images/photo9-3d3223f83a84872656f19981e000ba7d.webp)

<a id="maintenance-entry-fields"></a>

### Maintenance Entry Fields

| Field | Description |
| --- | --- |
| **Asset** | Asset being serviced |
| **Maintenance Type** | `Corrective`, `Preventive`, or `Predictive` |
| **Priority** | Low (0), Medium (1), High (2), Urgent (3) - displayed as stars |
| **Vendor** | Service provider (from asset.vendor) |
| **Start Date / End Date** | Service period (end must be >= start) |
| **Duration** | Computed: End Date minus Start Date (in days) |
| **Cost** | Maintenance amount (must be >= 0) |
| **Invoice** | Link to accounting invoice |
| **Status** | `Pending`, `In Progress`, `Completed` |
| **Description** | Detailed service notes |
| **Document** | Attach service reports, photos, receipts |

<a id="warranty-tracking"></a>

## Warranty Tracking

Monitor warranty expiration dates with color-coded indicators and dashboard alerts.

<a id="warranty-status-colors"></a>

### Warranty Status Colors

| Status | Condition | Color |
| --- | --- | --- |
| **Safe** | More than 6 months remaining | Green |
| **Warning** | 3 to 6 months remaining | Yellow |
| **Critical** | Less than 3 months remaining | Red |
| **Expired** | Past expiration date | Red |

The **Remaining Warranty** field shows a human-readable countdown such as *"2 Years, 3 Months, 15 Days"* or *"Expired"*. This appears on both the asset form and the Kanban card.

Dashboard Alerts

The dashboard shows a count of assets with warranties expiring within 30 days, displayed in the Alerts and Warnings panel.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Asset Tracking & Lifecycle](https://docs.sdlccorp.com/docs/asset-management/usage/asset-tracking/)
