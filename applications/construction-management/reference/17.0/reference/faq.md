# Construction Management - FAQ & Troubleshooting

Frequently asked questions and troubleshooting tips for the Construction Management module.

<a id="common-questions"></a>

## Common Questions

<a id="which-odoo-versions-are-supported"></a>

### Which Odoo versions are supported?

The module supports Odoo **v17**, **v18**, and **v19** Community Edition.

---


<a id="what-modules-are-required-as-dependencies"></a>

### What modules are required as dependencies?

The following Odoo modules must be installed: `base`, `mail`, `contacts`, `hr`, `stock`, `purchase`, `account`, and `project`.

---


<a id="can-i-use-this-module-with-odoo-enterprise-edition"></a>

### Can I use this module with Odoo Enterprise Edition?

The module is built for Odoo Community Edition. While it may work on Enterprise, it is officially supported only on Community Edition.

---


<a id="how-do-i-create-a-budget-from-a-boq"></a>

### How do I create a budget from a BOQ?

Navigate to your BOQ record, add product lines with quantities and prices, then click the **"Create / Update Budget"** button. The system will automatically generate a Budget record with the BOQ line items.

---


<a id="what-is-the-difference-between-a-project-and-a-sub-project"></a>

### What is the difference between a Project and a Sub Project?

**Projects** are the top-level entity representing the entire construction undertaking (e.g., a housing complex). **Sub Projects** break down a project into manageable units (e.g., individual buildings, wings, or floors).

---


<a id="how-does-the-material-requisition-approval-workflow-work"></a>

### How does the material requisition approval workflow work?

Material Requisitions follow a 7-stage workflow: Draft > Under Approval > Approved > In Progress > Ready for Delivery > Withdrawal > Done. Only requisitions in the **Approved** state can generate Purchase Orders.

---


<a id="can-i-track-subcontractor-payments-progressively"></a>

### Can I track subcontractor payments progressively?

Yes. Use **RA Billings (Running Account)** under **Construction > Contracts > RA Billings**. Each billing tracks the previous billing amount and computes the current amount due automatically.

---


<a id="what-quality-check-types-are-available"></a>

### What quality check types are available?

The module supports 8 inspection types: Material Inspection, Workmanship, Safety, Structural, Electrical, Plumbing, Final Inspection, and Other.

---


<a id="how-are-access-rights-structured"></a>

### How are access rights structured?

Two security groups are provided:

- **Construction User**: Read, Write, Create (no Delete)
- **Construction Manager**: Full access including Delete

---


<a id="can-i-customize-the-work-types-and-sub-types"></a>

### Can I customize the Work Types and Sub Types?

Yes. Navigate to **Construction > Configuration** to add, edit, or remove Work Types and Work Sub Types. These classifications are used throughout BOQ, Rate Analysis, Phases, and Budget records.

---


<a id="how-do-i-track-extra-expenses-outside-the-budget"></a>

### How do I track extra expenses outside the budget?

Use **Construction > Operations > Extra Expenses** to create expense records with types such as Material, Equipment, Labour, Transport, Permit/Fees, or Other. Each expense goes through a Draft > Confirmed > Approved workflow.

---


<a id="can-phases-have-a-hierarchical-structure"></a>

### Can phases have a hierarchical structure?

Yes. Each Phase (WBS) can have a **parent phase**, enabling a full hierarchical Work Breakdown Structure. Child phases appear in the parent's **Child Phases** tab.

---


<a id="how-does-progress-billing-work"></a>

### How does Progress Billing work?

Progress Billing enables milestone-based customer invoicing. Link a billing record to a phase and work order, load work order lines automatically, adjust quantities and prices, then click **Create Invoice** to generate a customer invoice directly.

---


<a id="where-can-i-see-the-overall-project-dashboard"></a>

### Where can I see the overall project dashboard?

Navigate to **Construction > Dashboard** to access real-time KPIs, project timelines, status charts, material requisition analytics, and purchase order tracking.

---


<a id="troubleshooting"></a>

## Troubleshooting

<a id="module-installation-fails"></a>

### Module installation fails

- Ensure all 8 dependent modules are installed first
- Restart the Odoo server and update the apps list
- Check the Odoo server logs for specific error messages

<a id="construction-menu-does-not-appear"></a>

### Construction menu does not appear

- Verify the module is installed (check **Settings > Apps**)
- Ensure your user has either **Construction User** or **Construction Manager** access rights
- Clear your browser cache and refresh

<a id="cannot-create-purchase-orders-from-material-requisitions"></a>

### Cannot create Purchase Orders from Material Requisitions

- Confirm the requisition is in **Approved** state
- Verify that each requisition line has a **vendor** assigned
- Check that the linked warehouse is properly configured

<a id="budget-variance-shows-incorrect-values"></a>

### Budget variance shows incorrect values

- Ensure the budget is in **Approved** or **Done** state
- Verify that actual cost entries are properly linked to the correct budget lines
- Check that BOQ-generated budget lines have correct planned amounts

---


<a id="support"></a>

## Support

For additional help or feature requests:

- Visit [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/)
- Email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**
- Check the [Odoo App Store](https://apps.odoo.com) for the latest module version

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Construction Management - FAQ & Troubleshooting](https://docs.sdlccorp.com/docs/17.0/construction-management/reference/faq/)
