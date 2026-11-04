# Project & Employee Dashboard - Getting Started

This guide walks you through installing and accessing the Project Analytics Dashboard for Odoo 19.

<a id="requirements"></a>

## Requirements

| Requirement | Details |
| --- | --- |
| **Odoo Version** | 19.0 |
| **Access Level** | Administrator |
| **Required Modules** | Project, HR |
| **Optional Modules** | Timesheets (`hr_timesheet`) for timesheet chart |
| **Python Library** | `xlsxwriter` (for Excel export only) |

<a id="installation-steps"></a>

## Installation Steps

<a id="step-1-find-the-module"></a>

### Step 1: Find the Module

Go to **Apps** and search for **Project Analytics Dashboard** or **SDLC Corp** in the Apps store.

![Apps Store Listing](https://docs.sdlccorp.com/assets/images/01-apps-store-listing-cd90e93cd61e32eee05cc387c6a3be14.webp)

<a id="step-2-install-the-module"></a>

### Step 2: Install the Module

Click the **Install** button on the module card. Odoo will install the module and its dependencies automatically.

![Module Installed](https://docs.sdlccorp.com/assets/images/02-module-installed-39a1de937928afcf46ee27094b0edeaa.webp)

info

The module depends on `project` and `hr`. If these are not already installed, Odoo will install them as part of the process.

<a id="step-3-access-the-dashboard"></a>

### Step 3: Access the Dashboard

After installation, navigate to **Project** in the main menu. The **Dashboard** option appears as the first item in the sidebar.

![Sidebar Menu](https://docs.sdlccorp.com/assets/images/03-sidebar-menu-d6f98560b7487a92b861c8448d736c70.webp)

<a id="no-configuration-required"></a>

## No Configuration Required

The dashboard works immediately with your existing project and HR data. There is no setup wizard or initial configuration needed. All charts and metrics populate automatically from your Odoo database.

tip

Install the `hr_timesheet` module to enable the Timesheet Hours chart on the dashboard. If not installed, the chart is automatically hidden.

<a id="optional-excel-export-setup"></a>

## Optional: Excel Export Setup

For Excel export functionality, ensure `xlsxwriter` is installed on your server:

```
pip install xlsxwriter
```

If not installed, the export button displays a friendly error message instead of failing silently.

<a id="next-steps"></a>

## Next Steps

- [Explore the dashboard](../../../dashboard/17.0/dashboard/overview.md)
- [Use filters and quick actions](../../../features/17.0/features/actions-filters.md)
- [Export to Excel](../../../features/17.0/features/excel-export.md)

<a id="need-help"></a>

## Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/)

---

Source: [Project & Employee Dashboard - Getting Started](https://docs.sdlccorp.com/docs/17.0/project-employee-dashboard/installation/getting-started/)
