# Project Cost Management - FAQ & Troubleshooting

Common questions and solutions for the SDLC Project Costing module.

<a id="frequently-asked-questions"></a>

## Frequently Asked Questions

<a id="what-odoo-versions-does-this-module-support"></a>

### What Odoo versions does this module support?

The module supports **Odoo 17.0, 18.0, and 19.0** (Community edition). Each version has a matching module version.

<a id="what-is-the-difference-between-fixed-cost-and-variable-cost-projects"></a>

### What is the difference between Fixed Cost and Variable Cost projects?

| Aspect | Fixed Cost | Variable Cost |
| --- | --- | --- |
| **Revenue source** | Project Budget field | Sum of Client Payments |
| **Budget field** | Active and required | Not used |
| **Client Payments tab** | Hidden | Visible |
| **Dashboard view** | Budget vs Actual chart | Client Payments vs Costs chart |

<a id="can-i-use-both-project-types-in-the-same-odoo-instance"></a>

### Can I use both project types in the same Odoo instance?

Yes. Each project is configured independently. You can have a mix of Fixed Cost and Variable Cost projects, and the dashboard will display appropriate charts and metrics for each type.

<a id="does-the-module-require-the-accounting-module"></a>

### Does the module require the Accounting module?

No. The module depends on **Project** (`project`), **Employees** (`hr`), **Timesheets** (`hr_timesheet`), and **Web** (`web`). It does not require the Accounting module. Cost tracking is handled through the module's own models and computed fields.

<a id="how-is-profit-calculated"></a>

### How is profit calculated?

**Profit = Total Revenue - Total Cost**

Where:

- **Total Revenue** = Project Budget (Fixed Cost) or Sum of Client Payments (Variable Cost)
- **Total Cost** = Labor Cost (from timesheets) + Extra Costs (from the Extra Costs tab)
- **Margin %** = Profit / Total Revenue x 100

<a id="can-i-export-dashboard-data"></a>

### Can I export dashboard data?

The dashboard is a real-time interactive view. For data export, you can use Odoo's built-in list view export functionality on the underlying models (Projects, Timesheets, Extra Costs, Client Payments).

---


<a id="troubleshooting"></a>

## Troubleshooting

<a id="module-does-not-appear-in-the-apps-list"></a>

### Module does not appear in the Apps list

1. Ensure **Developer Mode** is enabled: go to **Settings > General Settings > Developer Tools**
2. Verify the `project_costing` folder is placed in a directory listed in your Odoo addons path
3. Go to **Settings > Technical > Update Apps List** and click **Update**
4. Search again for **"SDLC Project Cost"** in the Apps menu

<a id="timesheet-cost-shows-zero"></a>

### Timesheet cost shows zero

- Verify the employee has an **Hourly Cost** set in **Employees > Employee Record > HR Settings**
- The cost is computed as `Hours x Hourly Cost`. If the hourly cost is zero or not set, the result will be zero
- After updating the hourly cost, new timesheet entries will use the updated rate. Existing entries may need to be re-saved

<a id="dashboard-is-blank-or-shows-no-data"></a>

### Dashboard is blank or shows no data

- Ensure at least one project has a **Project Type** set (Fixed Cost or Variable Cost)
- Check that the **date filters** on the dashboard are not excluding all your data -- try clearing the Start Date and End Date fields
- Verify the user has the **Project Finance Management** security group assigned

<a id="extra-costs-tab-is-missing"></a>

### Extra Costs tab is missing

- The Extra Costs tab should appear on all project forms after module installation
- Ensure the module is properly installed (check **Apps > Installed** for "SDLC Project Cost")
- Try refreshing the browser or clearing the browser cache

<a id="client-payments-tab-is-not-visible"></a>

### Client Payments tab is not visible

- The Client Payments tab is **only visible when the Project Type is set to Variable Cost**
- Open the project form and set the **Project Type** field to **Variable Cost**
- Save the project -- the Client Payments tab will appear

<a id="over-budget-alert-not-showing"></a>

### Over Budget alert not showing

- Over Budget alerts only apply to **Fixed Cost** projects with a **Project Budget** set
- The alert triggers when Total Cost (Labor + Extra Costs) exceeds the Project Budget value
- Ensure your project has actual costs recorded via timesheets or extra cost entries

<a id="user-cannot-access-the-dashboard"></a>

### User cannot access the dashboard

- The user must be assigned to the **Project Finance Management** security group
- Go to **Settings > Users & Companies > Users**, select the user, and enable the group under the **Project** section

---


<a id="data-models-reference"></a>

## Data Models Reference

The module creates or extends the following Odoo models:

<a id="projectproject-extended"></a>

### project.project (Extended)

| Field | Type | Description |
| --- | --- | --- |
| `project_type` | Selection | Project type: "Fixed Cost" or "Variable Cost" |
| `project_budget` | Monetary | Approved budget amount for the project |
| `extra_cost_ids` | One2many | Related extra cost records |
| `client_payment_ids` | One2many | Related client payment records |
| `total_extra_cost` | Monetary (Computed) | Sum of all extra costs for the project |
| `total_client_payment` | Monetary (Computed) | Sum of all client payments for the project |
| `total_revenue` | Monetary (Computed) | Total revenue based on project type |
| `currency_id` | Many2one | Currency used for monetary fields |

<a id="projectextracost"></a>

### project.extra.cost

| Field | Type | Description |
| --- | --- | --- |
| `name` | Char | Description of the expense |
| `amount` | Monetary | Expense amount |
| `project_id` | Many2one | Related project |
| `currency_id` | Many2one | Currency (related from project) |
| `date` | Date | Date the expense was incurred |
| `notes` | Text | Optional notes |

<a id="projectclientpayment"></a>

### project.client.payment

| Field | Type | Description |
| --- | --- | --- |
| `name` | Char | Description of the payment |
| `amount` | Monetary | Payment amount |
| `project_id` | Many2one | Related project |
| `currency_id` | Many2one | Currency (related from project) |
| `payment_date` | Date | Date payment was received |
| `notes` | Text | Optional notes |

<a id="accountanalyticline-extended"></a>

### account.analytic.line (Extended)

| Field | Type | Description |
| --- | --- | --- |
| `cost` | Monetary (Computed) | Calculated as `unit_amount x employee_id.hourly_cost` |

<a id="projectdashboard"></a>

### project.dashboard

| Method | Returns |
| --- | --- |
| `get_dashboard_data()` | Dictionary containing: statistics, project_budget_details, over_budget_projects, cost_breakdown, revenue_breakdown, cost_analysis, budget_vs_actual, client_payment_analysis |

---


<a id="support"></a>

## Support

- **Website:** [sdlccorp.com](https://sdlccorp.com)
- **Odoo App Store:** Search for "SDLC Project Cost"
- **Module Technical Name:** `project_costing`

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Project Cost Management - FAQ & Troubleshooting](https://docs.sdlccorp.com/docs/project-cost-management/reference/faq/)
