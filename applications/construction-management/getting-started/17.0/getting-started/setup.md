# Construction Management - Installation & Setup

Follow these steps to install and configure the Construction Management module on your Odoo instance.

<a id="prerequisites"></a>

## Prerequisites

Before installing the module, ensure the following Odoo modules are already installed:

| Module | Purpose |
| --- | --- |
| **base** | Core Odoo framework |
| **mail** | Messaging and chatter support |
| **contacts** | Customer and vendor management |
| **hr** | Human Resources (employee records) |
| **stock** | Warehouse and inventory management |
| **purchase** | Purchase order management |
| **account** | Accounting and invoicing |
| **project** | Project management framework |

Dependencies

All eight dependent modules must be installed before the Construction Management module can be activated. The installer will report missing dependencies if any are absent.

<a id="installation-steps"></a>

## Installation Steps

1. Copy the `sdlc_construction_management` folder to your Odoo addons directory.
2. Restart the Odoo server and update the apps list from **Settings > Apps > Update Apps List**.
3. Search for **"Construction Management"** in the Apps menu and click **Install**.
4. Once installed, a new **"Construction"** menu will appear in the top navigation bar.

tip

Ensure that the dependent modules (Stock, Purchase, Account, HR, Project) are already installed before installing this module.

<a id="supported-versions"></a>

## Supported Versions

| Odoo Version | Edition | Status |
| --- | --- | --- |
| **v17** | Community | Supported |
| **v18** | Community | Supported |
| **v19** | Community | Supported |

<a id="initial-configuration"></a>

## Initial Configuration

After installation, configure the following items before creating your first project:

<a id="work-types--sub-types"></a>

### Work Types & Sub Types

Navigate to **Construction > Configuration** to review and customize work types:

- 10 pre-configured **Work Types** (e.g., Brickwork, Electrical Work, Plumbing & Sanitary, RCC Structure)
- 11 pre-configured **Work Sub Types** (e.g., Column Casting, Excavation, PCC, Slab Casting)

![Work Types Configuration](https://docs.sdlccorp.com/assets/images/photo42-5c6987cb6f8d4228996a45a61482c7b9.webp)
*Work Types list with 10 pre-configured types and their codes*

![Work Sub Types Configuration](https://docs.sdlccorp.com/assets/images/photo43-b2e4a3b0916bf1aefd7b76725527d012.webp)
*Work Sub Types list showing parent Work Type, Sub Type name, and code*

tip

You can create custom Work Types and Sub Types to match your organization's specific construction activities. These are used for classification in BOQ, Rate Analysis, Phases, and Budget records.

<a id="access-rights--security"></a>

### Access Rights & Security

The module provides two security groups with different permission levels:

| Security Group | Read | Write | Create | Delete |
| --- | --- | --- | --- | --- |
| **Construction User** | Yes | Yes | Yes | No |
| **Construction Manager** | Yes | Yes | Yes | Yes |

To assign groups, go to **Settings > Users & Companies > Users** and set the Construction field under the **Application Accesses** section.

warning

Only Construction Managers can delete records. Construction Users have full read/write/create access but cannot delete any construction records.

<a id="warehouse-setup"></a>

### Warehouse Setup

Each project requires a **Warehouse** assignment for material requisitions and internal transfers. Ensure your warehouses are properly configured in **Inventory > Configuration > Warehouses** before creating projects.

<a id="construction-menu-structure"></a>

## Construction Menu Structure

After installation, the Construction menu provides access to all features:

| Menu | Sub-menus |
| --- | --- |
| **Construction > Projects** | Projects |
| **Construction > Sub Projects** | Sub Projects |
| **Construction > Tasks** | Tasks |
| **Construction > Budgets** | Bill of Quantities, Budgets |
| **Construction > Rate Analysis** | Rate Analysis |
| **Construction > Executions** | Phases (WBS), Work Orders |
| **Construction > Operations** | Material Requisitions, Extra Expenses, Progress Billing |
| **Construction > Contracts** | Subcontracting, Consume Orders, RA Billings |
| **Construction > Quality Checks** | Quality Checks |
| **Construction > Configuration** | Work Types, Work Sub Types |
| **Construction > Dashboard** | Dashboard |

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Construction Management - Installation & Setup](https://docs.sdlccorp.com/docs/17.0/construction-management/getting-started/setup/)
