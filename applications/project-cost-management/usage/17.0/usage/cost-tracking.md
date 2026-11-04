# Cost Tracking & Management

The Project Costing module captures project costs from three sources: **extra costs** (miscellaneous expenses), **client payments** (for variable cost projects), and **timesheet costing** (automatic labor cost calculation). This page covers how to use each of these features.

<a id="extra-costs"></a>

## Extra Costs

Track miscellaneous project expenses such as software licenses, travel, subcontractor fees, or any other non-labor costs directly from the project form.

<a id="overview"></a>

### Overview

The **Extra Costs** tab is available on every project form, regardless of project type. Each extra cost entry records a date, description, amount, and optional notes. The **Total Extra Cost** is computed automatically as the sum of all entries.

<a id="adding-extra-costs"></a>

### Adding Extra Costs

1. Open the project from **Project > All Projects**
2. Navigate to the **Extra Costs** tab
3. Click **Add a line** to create a new entry
4. Fill in the **Date**, **Cost Name**, and **Amount**
5. Optionally add **Notes** for additional context
6. Save the project

![Extra Costs tab on project form](https://docs.sdlccorp.com/assets/images/photo6-9c2fe81e93ef4a99913c3cb0d6d9a198.webp)
*Extra Costs tab -- log miscellaneous project expenses with date, name, and amount*

<a id="fields-reference"></a>

### Fields Reference

| Field | Type | Description |
| --- | --- | --- |
| **Date** | Date | The date the expense was incurred |
| **Cost Name** | Text | Short description of the expense |
| **Amount** | Monetary | Cost amount in the project's currency |
| **Notes** | Text | Optional additional details or justification |

<a id="total-extra-cost"></a>

### Total Extra Cost

The **Total Extra Cost** is a computed field displayed at the bottom of the Extra Costs tab. It automatically sums all extra cost entries for the project and feeds into the dashboard's cost breakdown.

![Extra Costs with total](https://docs.sdlccorp.com/assets/images/photo7-38843399c2b640bcc384a7a78f3b8ce2.webp)
*Itemized expenses and computed Total Extra Cost ($150.00) at the bottom of the tab*

---


<a id="client-payments"></a>

## Client Payments

Record and track payment installments or milestone-based payments from clients for Variable Cost projects.

<a id="overview-1"></a>

### Overview

The **Client Payments** tab is visible on the project form **only when the project type is set to Variable Cost**. It allows you to record each payment received from the client with a date, name, amount, and optional notes.

info

Client Payments are only available for **Variable Cost** projects. For Fixed Cost projects, revenue is derived from the Project Budget field instead.

<a id="recording-a-payment"></a>

### Recording a Payment

1. Open the project and ensure the **Project Type** is set to **Variable Cost**
2. Navigate to the **Client Payments** tab
3. Click **Add a line**
4. Enter the **Payment Date**, **Payment Name**, and **Amount**
5. Optionally add **Notes**
6. Save the project

![Client Payments tab](https://docs.sdlccorp.com/assets/images/photo8-6d8520a1ce2a90461d0e9dffbc56f8c8.webp)
*Client Payments tab -- record payment installments from clients with date, name, and amount*

<a id="fields-reference-1"></a>

### Fields Reference

| Field | Type | Description |
| --- | --- | --- |
| **Payment Date** | Date | The date the payment was received |
| **Payment Name** | Text | Description of the payment (e.g., "Milestone 1 Payment") |
| **Amount** | Monetary | Payment amount in the project's currency |
| **Notes** | Text | Optional additional details about the payment |

<a id="total-client-payment"></a>

### Total Client Payment

The **Total Client Payment** is computed automatically as the sum of all payment entries. For Variable Cost projects, this total becomes the project's **Total Revenue** on the dashboard.

<a id="revenue-calculation-logic"></a>

### Revenue Calculation Logic

| Project Type | Revenue Source | Formula |
| --- | --- | --- |
| **Fixed Cost** | Project Budget | `Total Revenue = Project Budget` |
| **Variable Cost** | Client Payments | `Total Revenue = Sum of Client Payments` |

---


<a id="timesheet-costing"></a>

## Timesheet Costing

The module extends Odoo's timesheet views with an auto-calculated **Cost** field based on each employee's hourly cost rate.

<a id="how-it-works"></a>

### How It Works

The module inherits the `account.analytic.line` model (Odoo's timesheet model) and adds a computed **Cost** field. Every time an employee logs hours on a timesheet, the cost is calculated automatically:

Formula

**Cost = Unit Amount (hours) x Employee Hourly Cost**

<a id="where-cost-appears"></a>

### Where Cost Appears

The Cost field is added to all four standard timesheet views:

| View | Type | Cost Field |
| --- | --- | --- |
| **My Timesheets** | Form view | Read-only, auto-computed |
| **My Timesheets** | List/Tree view | Read-only column |
| **All Timesheets** | Form view | Read-only, auto-computed |
| **All Timesheets** | List/Tree view | Read-only column |

![Timesheet with Cost field](https://docs.sdlccorp.com/assets/images/photo9-bc880167dd6e763fa7cd8afd1e4e6d95.webp)
*Timesheet entries with auto-calculated Cost field (rightmost column) based on employee hourly rate and hours logged*

<a id="impact-on-dashboard"></a>

### Impact on Dashboard

Timesheet costs feed into multiple dashboard components:

- **Total Cost** KPI card -- includes all labor costs across projects
- **Cost Breakdown** panel -- shows Labor Cost as a separate line item
- **Cost Analysis** chart -- displays Labor Cost vs Extra Costs per project
- **Budget Details** table -- shows hours logged and labor cost per project

<a id="total-cost-calculation"></a>

### Total Cost Calculation

The module tracks two cost components that together make up the total project cost:

| Component | Source | Description |
| --- | --- | --- |
| **Labor Cost** | Timesheets | Sum of all `hours x hourly_cost` for the project |
| **Extra Costs** | Extra Costs tab | Sum of all miscellaneous expense entries |
| **Total Cost** | Computed | Labor Cost + Extra Costs |

tip

If an employee's timesheet entries show a cost of zero, verify that their **Hourly Cost** is set in **Employees > Employee Record > HR Settings**.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Cost Tracking & Management](https://docs.sdlccorp.com/docs/17.0/project-cost-management/usage/cost-tracking/)
