# Resource & Material Management

The Construction Management module provides comprehensive tools for managing materials, procurement, subcontracting, and expenses throughout your construction projects.

---


<a id="material-requisitions"></a>

## Material Requisitions

Material Requisitions manage the procurement workflow from request to delivery. Navigate to **Construction > Operations > Material Requisitions**.

<a id="material-requisition-list-view"></a>

### Material Requisition List View

![Material Requisitions List View](https://docs.sdlccorp.com/assets/images/photo26-e5ab47d8cf9e0a36663b06d08756cb95.webp)
*Material Requisitions list view with Operations menu dropdown*

<a id="material-requisition-workflow"></a>

### Material Requisition Workflow

The MREQ has the most comprehensive approval workflow in the module:

| Stage | Description |
| --- | --- |
| **Draft** | Requisition created |
| **Under Approval** | Submitted for manager approval |
| **Approved** | Approved by manager |
| **In Progress** | Purchase orders being processed |
| **Ready for Delivery** | Materials ready at warehouse |
| **Withdrawal** | Materials being withdrawn |
| **Done** | Requisition complete |

<a id="material-requisition-form-view"></a>

### Material Requisition Form View

| Field / Feature | Details |
| --- | --- |
| **Smart Buttons** | Purchase Orders count and Internal Transfers count |
| **Work Order Link** | Link to the work order requiring materials |
| **Requested By / Approved By** | Track who requested and approved |
| **Warehouse & Department** | Source warehouse and department |
| **Requisition Lines** | Products with quantities, prices, vendors, and notes |
| **Create Purchase Order** | Auto-generate PO from approved requisition lines |
| **Create Internal Transfer** | Auto-create stock transfer for warehouse fulfillment |

![Material Requisition Form](https://docs.sdlccorp.com/assets/images/photo27-e43014fd14250569e07d0c6ba40c546e.webp)
*Material Requisition form with 7-stage status bar, smart buttons, and requisition lines*

Important

Only requisitions in the **Approved** state can generate Purchase Orders. The system validates vendor assignment on each line before PO creation.

---


<a id="extra-expenses"></a>

## Extra Expenses

Track additional costs outside the regular budget. Navigate to **Construction > Operations > Extra Expenses**.

<a id="extra-expenses-list-view"></a>

### Extra Expenses List View

![Extra Expenses List View](https://docs.sdlccorp.com/assets/images/photo28-9c8cdceba048f9d42bb8ba4e358ed8c8.webp)
*Extra Expenses list view with Operations menu dropdown*

<a id="extra-expense-workflow"></a>

### Extra Expense Workflow

| Stage | Description |
| --- | --- |
| **Draft** | Expense created |
| **Confirmed** | Submitted for review |
| **Approved** | Expense approved |

<a id="extra-expense-form-view"></a>

### Extra Expense Form View

Expense types include:

| Type | Description |
| --- | --- |
| **Material** | Additional material costs |
| **Equipment** | Extra equipment expenses |
| **Labour** | Unplanned labour costs |
| **Transport** | Transportation expenses |
| **Permit/Fees** | Permit and fee costs |
| **Other** | Miscellaneous expenses |

Each expense captures **Product**, **Quantity**, **Unit Price**, and auto-computed **Amount**.

![Extra Expense Form](https://docs.sdlccorp.com/assets/images/photo29-80ee34865f5670efaf14753d8481a519.webp)
*Extra Expense form with expense type, product details, and approval tracking*

---


<a id="subcontracting"></a>

## Subcontracting

Manage subcontractor agreements, material consumption, and running account billings. Navigate to **Construction > Contracts > Subcontracting**.

<a id="subcontracting-list-view"></a>

### Subcontracting List View

![Subcontracting List View](https://docs.sdlccorp.com/assets/images/photo34-83c7370e02ee8c067b05905a0dc9170c.webp)
*Subcontracting list view with Contracts menu dropdown*

<a id="subcontract-workflow"></a>

### Subcontract Workflow

| Stage | Description |
| --- | --- |
| **Draft** | Contract created |
| **Confirmed** | Contract terms agreed |
| **In Progress** | Work underway |
| **Completed** | Contract fulfilled |

<a id="subcontract-form-view"></a>

### Subcontract Form View

| Field / Tab | Details |
| --- | --- |
| **Subcontractor** | Vendor partner selection |
| **Start/End Date** | Contract duration |
| **Smart Buttons** | Consume Orders count and RA Billings count |
| **Scope of Work Tab** | Detailed work description |
| **Work Lines Tab** | Work items with description, quantity, rate, and amount |
| **Work Completion Tab** | Upload completion certificate, enter completion date and notes |
| **Notes Tab** | Additional contract notes |
| **Contract Amount** | Auto-computed from work lines |
| **Billed Amount** | Auto-computed from approved RA billings |

![Subcontract Form](https://docs.sdlccorp.com/assets/images/photo35-3c40b8a7f00b2d1f97e811cdf3de9fc3.webp)
*Subcontract form with scope of work, smart buttons, and status workflow*

---


<a id="consume-orders"></a>

## Consume Orders

Track materials consumed by subcontractors. Navigate to **Construction > Contracts > Consume Orders**.

<a id="consume-orders-list-view"></a>

### Consume Orders List View

![Consume Orders List View](https://docs.sdlccorp.com/assets/images/photo36-133c44c496b2a887b9324096ed616d77.webp)
*Consume Orders list view under Contracts menu*

<a id="consume-order-workflow"></a>

### Consume Order Workflow

| Stage | Description |
| --- | --- |
| **Draft** | Order created |
| **Confirmed** | Order confirmed |
| **Done** | Materials consumed |

Each consume order is linked to a subcontract and contains product lines with quantity and UOM. This tracks materials provided to the subcontractor for their work.

![Consume Order Form](https://docs.sdlccorp.com/assets/images/photo37-085e9d7641f46c0fa3d03f49db691739.webp)
*Consume Order form with subcontract linkage and product lines*

---


<a id="ra-billings-running-account"></a>

## RA Billings (Running Account)

RA Billings track progressive payments to subcontractors. Navigate to **Construction > Contracts > RA Billings**.

<a id="ra-billings-list-view"></a>

### RA Billings List View

![RA Billings List View](https://docs.sdlccorp.com/assets/images/photo38-70c29ddd79e4051a9a2c53d51cdee933.webp)
*RA Billings list view showing billing amounts and status*

<a id="ra-billing-workflow"></a>

### RA Billing Workflow

| Stage | Description |
| --- | --- |
| **Draft** | Billing created |
| **Submitted** | Sent for approval |
| **Approved** | Payment authorized |

<a id="ra-billing-form-view"></a>

### RA Billing Form View

| Field | Details |
| --- | --- |
| **Subcontract** | Linked subcontract record |
| **Billing No.** | Sequential billing number |
| **Previous Billing Amount** | Amount billed in previous RA bills |
| **Billing Lines** | Description, Quantity, UOM, Rate, Amount, and Completion % |
| **Current Amount** | Auto-computed (Total - Previous Billing) |

![RA Billing Form](https://docs.sdlccorp.com/assets/images/photo39-5a3796c89ca4a1322e58d3d69cb25939.webp)
*RA Billing form with billing lines, completion tracking, and amount computation*

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Resource & Material Management](https://docs.sdlccorp.com/docs/18.0/construction-management/operations/resource-management/)
