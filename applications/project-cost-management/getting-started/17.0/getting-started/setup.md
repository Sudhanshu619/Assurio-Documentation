# Project Cost Management - Installation & Setup

This guide walks you through installing and configuring the SDLC Project Costing module on your Odoo instance.

<a id="prerequisites"></a>

## Prerequisites

Before installing the module, ensure you have:

- A working **Odoo Community** instance (v17, v18, or v19)
- **Administrator access** to your Odoo instance
- **Developer Mode** enabled (Settings > General Settings > Developer Tools)
- The following standard Odoo modules installed:

| Module | Technical Name | Purpose |
| --- | --- | --- |
| **Project** | `project` | Core project management -- provides the project form, tasks, and settings |
| **Employees** | `hr` | Employee records -- used to link hourly cost rates to employees |
| **Timesheets** | `hr_timesheet` | Timesheet entries -- extended with auto-calculated cost field |
| **Web** | `web` | Web framework -- required for Owl.js dashboard components |

info

All dependencies will be automatically installed when you install the Project Costing module if they are not already present on your system.

<a id="installation-steps"></a>

## Installation Steps

<a id="step-1-download-the-module"></a>

### Step 1: Download the Module

Download the `project_costing` module from the Odoo App Store or obtain it directly from SDLC Corp. The module is distributed as a zip file or a folder.

<a id="step-2-upload-to-your-server"></a>

### Step 2: Upload to Your Server

Place the `project_costing` folder in your Odoo addons directory (e.g., `/odoo/custom/addons/`).

<a id="step-3-update-apps-list"></a>

### Step 3: Update Apps List

Go to **Settings > Technical > Update Apps List** and click **Update**.

<a id="step-4-install-the-module"></a>

### Step 4: Install the Module

Navigate to **Apps**, search for **"SDLC Project Cost"**, and click **Install**.

tip

If you do not see the module in the Apps list, make sure Developer Mode is enabled and that the addons path in your Odoo configuration file includes the directory where the module is placed.

<a id="verify-installation"></a>

## Verify Installation

After successful installation, you will see:

- A new **Dashboard** menu item under the **Project** module
- New fields (**Project Type**, **Project Budget**) on the project form
- New tabs (**Extra Costs**, **Client Payments**) on the project form
- A **Cost** column in all timesheet views

![Project form after installation](https://docs.sdlccorp.com/assets/images/photo6-9c2fe81e93ef4a99913c3cb0d6d9a198.webp)
*Project form after module installation -- showing Project Type, Budget, and the Extra Costs tab*

<a id="initial-configuration"></a>

## Initial Configuration

<a id="1-configure-project-types"></a>

### 1. Configure Project Types

Every project must be classified with a type, which determines how revenue and costs are calculated:

| Project Type | Revenue Source | Budget Field | Client Payments Tab |
| --- | --- | --- | --- |
| **Fixed Cost** | Project Budget amount | Active and required | Hidden |
| **Variable Cost** | Sum of Client Payments | Not used | Visible |

**Steps:**

1. Open the desired project from **Project > All Projects**
2. Set the **Project Type** field to **Fixed Cost** or **Variable Cost**
3. For Fixed Cost projects, enter the approved amount in the **Project Budget** field
4. Save the project

warning

The Project Budget field is only meaningful for Fixed Cost projects. For Variable Cost projects, revenue is derived from recorded client payments instead.

<a id="2-configure-employee-hourly-costs"></a>

### 2. Configure Employee Hourly Costs

The module calculates labor costs based on each employee's hourly cost rate. This must be configured for accurate cost tracking.

1. Navigate to **Employees > Employees**
2. Open the employee record
3. Go to the **HR Settings** tab
4. Set the **Hourly Cost** field to the employee's cost rate per hour
5. Save the employee record

Formula

**Timesheet Cost = Hours Logged x Employee Hourly Cost**

For example, if an employee with a hourly cost of $50 logs 8 hours, the cost will be calculated as **$400**.

tip

Make sure to set the hourly cost for **all employees** who will log timesheets. If an employee has no hourly cost set, their timesheet entries will show a cost of zero.

<a id="3-set-up-security--access"></a>

### 3. Set Up Security & Access

The module creates a security group called **Project Finance Management**. Users must be assigned to this group to access financial fields and the dashboard.

**Access Rights:**

| Model | Group | Read | Write | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| `project.extra.cost` | Project Users / Managers | Yes | Yes | Yes | Yes |
| `project.client.payment` | Project Users / Managers | Yes | Yes | Yes | Yes |
| `project.dashboard` | Project Users / Managers | Yes | Yes | Yes | Yes |

**Assigning the Group:**

1. Go to **Settings > Users & Companies > Users**
2. Select the user you want to grant access to
3. Under the **Project** section, enable the **Project Finance Management** group
4. Save the user record

<a id="frontend-libraries"></a>

## Frontend Libraries

The module bundles the following JavaScript library for dashboard chart rendering:

| Library | Version | Purpose |
| --- | --- | --- |
| **Chart.js** | UMD (bundled) | Renders bar charts and stacked bar charts for financial visualizations |

No additional frontend installation is required -- Chart.js is bundled with the module.

<a id="next-steps"></a>

## Next Steps

- [Track costs and payments](../../../usage/17.0/usage/cost-tracking.md)
- [Explore the dashboard and reports](../../../usage/17.0/usage/reports-analysis.md)

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Project Cost Management - Installation & Setup](https://docs.sdlccorp.com/docs/17.0/project-cost-management/getting-started/setup/)
