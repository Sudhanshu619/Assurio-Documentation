# SDLC Financial Reports - Installation and Setup

Install and set up SDLC Financial Reports on your Odoo 17, 18, or 19 Community Edition instance in minutes.

<a id="prerequisites"></a>

## Prerequisites

- A working **Odoo 17, 18, or 19** Community Edition instance
- Admin access to your Odoo instance
- The **Accounting** (`account`) module installed and configured with a chart of accounts
- The **Analytic Accounting** (`analytic`) module installed
- Developer Mode enabled for initial setup

<a id="dependencies"></a>

## Dependencies

<a id="odoo-module-dependencies"></a>

### Odoo Module Dependencies

| Module | Technical Name | Purpose |
| --- | --- | --- |
| **Accounting** | `account` | Core accounting -- provides chart of accounts, journal entries, and move lines |
| **Analytic Accounting** | `analytic` | Analytic accounts -- required for the Analytic Summary Report |

<a id="python-library-dependencies"></a>

### Python Library Dependencies

| Library | Purpose | Installation |
| --- | --- | --- |
| **xlsxwriter** | Excel (XLSX) file generation with formatting, frozen headers, and number styles | `pip install xlsxwriter` |

warning

If `xlsxwriter` is not installed, the Excel export feature will not work. PDF export and interactive views will function normally.

<a id="installation-steps"></a>

## Installation Steps

1. **Download the Module** -- Download `sdlc_financial_reports` from the Odoo App Store or obtain it from SDLC Corp.
2. **Upload to Your Server** -- Place the `sdlc_financial_reports` folder in your Odoo addons directory (e.g., `/odoo/custom/addons/`).
3. **Update Apps List** -- Go to **Settings > Technical > Update Apps List** and click **Update**.
4. **Install the Module** -- Navigate to **Apps**, search for *"SDLC Financial Reports"*, and click **Install**.

tip

If you do not see the module in the Apps list, ensure Developer Mode is enabled and that your addons path in the Odoo configuration file includes the directory where the module is placed.

<a id="verify-installation"></a>

## Verify Installation

After successful installation, you will see:

- A new **Financial Reports** submenu under **Accounting > Reporting**
- 8 report menu items: General Ledger, Partner Ledger, Aged Partner Balance, Trial Balance, Profit & Loss, Balance Sheet, Cash Flow Statement, Analytic Summary Report
- New settings under **Accounting > Settings > Dynamic Financial Reports**

![Financial Reports Menu](https://docs.sdlccorp.com/assets/images/photo1-82219ec844d7df412620771ba1859bd6.webp)

info

No additional configuration is required to start generating reports. The module works out of the box with your existing chart of accounts and journal entries.

<a id="security--access-configuration"></a>

## Security & Access Configuration

The module provides two dedicated security groups for access control.

<a id="security-groups"></a>

### Security Groups

| Group | Implied Groups | Permissions |
| --- | --- | --- |
| **Financial Reports User** | Account Readonly | View and generate all reports, read-only access to report configurations |
| **Financial Reports Manager** | Financial Reports User + Account Manager | Full access: view, generate, configure, and manage all report settings |

<a id="assigning-groups"></a>

### Assigning Groups

1. Go to **Settings > Users & Companies > Users**
2. Select the user
3. Under the **Accounting** section, assign either **Financial Reports User** or **Financial Reports Manager**
4. Save the user record

<a id="multi-company-record-rules"></a>

### Multi-Company Record Rules

A multi-company record rule ensures that report configurations are isolated per company. Users can only access `account.financial.report.config` records where the company matches one of their allowed companies.

<a id="company-settings"></a>

## Company Settings

Navigate to **Accounting > Configuration > Settings** and scroll to the **Dynamic Financial Reports** section to configure defaults.

<a id="default-date-range"></a>

### Default Date Range

| Option | Description |
| --- | --- |
| `Today` | Current date only |
| `This Week` | Monday to Sunday of the current week |
| `This Month` | First to last day of the current month (default) |
| `This Quarter` | First to last day of the current quarter |
| `This Year` | January 1 to December 31 of the current year |
| `Last Month` | Previous calendar month |
| `Last Quarter` | Previous calendar quarter |
| `Last Year` | Previous calendar year |
| `Custom` | Manual date selection |

<a id="display-options"></a>

### Display Options

| Setting | Default | Description |
| --- | --- | --- |
| **Show Zero Balance Accounts** | Off | When enabled, accounts with zero balances are included in reports |
| **Show Hierarchy** | On | When enabled, displays account hierarchy in tree view format |
| **Include Initial Balance** | On | When enabled, shows opening balance row at the start of each account section |

<a id="aging-bucket-configuration"></a>

### Aging Bucket Configuration

| Setting | Default | Description |
| --- | --- | --- |
| **Aging Bucket 1** | 30 days | First aging period boundary (e.g., 0-30 days) |
| **Aging Bucket 2** | 60 days | Second aging period boundary (e.g., 30-60 days) |
| **Aging Bucket 3** | 90 days | Third aging period boundary (e.g., 60-90 days) |
| **Aging Bucket 4** | 120 days | Fourth aging period boundary (e.g., 90-120 days) |

tip

You can change the bucket periods to match your business requirements. For example, set buckets to 15, 30, 45, 60 days for tighter payment monitoring.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [SDLC Financial Reports - Installation and Setup](https://docs.sdlccorp.com/docs/17.0/financial-reports/getting-started/setup/)
