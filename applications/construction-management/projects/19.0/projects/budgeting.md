# Budgeting & BOQ

The Construction Management module provides comprehensive financial planning tools including Bill of Quantities (BOQ), Budget Management, and Rate Analysis.

---


<a id="bill-of-quantities-boq"></a>

## Bill of Quantities (BOQ)

The BOQ module enables precise quantity estimation for construction work. Navigate to **Construction > Budgets > Bill of Quantities**.

<a id="boq-list-view"></a>

### BOQ List View

| Column | Description |
| --- | --- |
| **Reference** | Auto-generated (BOQ/XXXX) |
| **Project** | Associated project |
| **Sub Project** | Associated sub-project |
| **Work Type** | Classification of work |
| **Work Sub Type** | Sub-classification |
| **Quantity** | Computed quantity |
| **Total Amount** | Computed total |

![BOQ List View](https://docs.sdlccorp.com/assets/images/photo10-d65414fe3c95c1bc993fec86b1009cb3.webp)
*Bill of Quantities list view with Budgets menu dropdown*

<a id="boq-measurements"></a>

### BOQ Measurements

Each BOQ record captures measurement dimensions for automatic quantity computation:

| Field | Description |
| --- | --- |
| **Work Type / Sub Type** | Classification (e.g., Brickwork, Electrical Work) |
| **Unit of Measure** | UOM for measurement (e.g., sq ft, cubic m) |
| **Length x Width x Height x Nos** | Dimensions multiplied to compute Quantity automatically |

![BOQ Measurements](https://docs.sdlccorp.com/assets/images/photo11-83be27f418505a1750d1e2a274ba2e9f.webp)
*BOQ form with measurement dimensions (Length x Width x Height x Nos = Quantity)*

<a id="boq-lines--budget-creation"></a>

### BOQ Lines & Budget Creation

Add product lines with quantity, UOM, unit price, and computed amount. The **"Create / Update Budget"** button automatically generates a Budget record from the BOQ lines.

![BOQ Lines](https://docs.sdlccorp.com/assets/images/photo12-14069ee641a9a493ad7603fe9f8e9806.webp)
*BOQ lines with products and the Create/Update Budget button*

tip

When you click "Create / Update Budget", the system automatically creates a new Budget or updates an existing one with the BOQ line items, saving manual data entry.

---


<a id="budgets"></a>

## Budgets

Budget management tracks planned vs actual costs with variance analysis. Navigate to **Construction > Budgets > Budgets**.

<a id="budget-list-view"></a>

### Budget List View

| Column | Description |
| --- | --- |
| **Reference** | Auto-generated (BDG/XXXX) |
| **Project** | Associated project |
| **Sub Project** | Associated sub-project |
| **Date** | Budget date |
| **Total Planned** | Total planned cost |
| **Total Actual** | Total actual cost incurred |
| **Total Variance** | Auto-computed (Planned - Actual) |
| **Status** | Current approval state |

![Budget List View](https://docs.sdlccorp.com/assets/images/photo13-1de221c23334dbe4c6a64c2568c2627b.webp)
*Budgets list view with financial summary columns*

<a id="budget-approval-workflow"></a>

### Budget Approval Workflow

Budgets follow a multi-stage approval process:

| Stage | Description |
| --- | --- |
| **Draft** | Budget created, lines being added |
| **Confirmed** | Budget submitted for review |
| **Approved** | Budget approved by manager |
| **Done** | Budget finalized and locked |

<a id="budget-form-view"></a>

### Budget Form View

Budget Lines include the following fields:

| Field | Description |
| --- | --- |
| **Work Type** | Category of work (e.g., Brickwork) |
| **Product** | Specific material or service |
| **Planned Amount** | Estimated cost |
| **Actual Amount** | Real cost incurred |
| **Variance** | Auto-computed (Planned - Actual) |
| **Progress (%)** | Percentage of budget utilized |

![Budget Form - Lines](https://docs.sdlccorp.com/assets/images/photo14-de1970ccca9dda6fbf2fdd7a2480b0a2.webp)
*Budget form with status bar and budget lines showing variance tracking*

![Budget Form - Totals](https://docs.sdlccorp.com/assets/images/photo15-2182504da62fe1d1dc2693b042514e65.webp)
*Budget totals summary: Total Planned, Total Actual, and Total Variance*

---


<a id="rate-analysis"></a>

## Rate Analysis

Rate Analysis breaks down per-unit costs into five categories. Navigate to **Construction > Rate Analysis**.

<a id="rate-analysis-list-view"></a>

### Rate Analysis List View

![Rate Analysis List View](https://docs.sdlccorp.com/assets/images/photo16-517386ab93de26aa962dcf67e00b0acf.webp)
*Rate Analysis list view with Reference, Title, Work Type, and Total Amount*

<a id="rate-analysis-form-view"></a>

### Rate Analysis Form View

The form provides five categorized tabs for detailed cost breakdown:

| Tab | Description |
| --- | --- |
| **Materials** | Raw materials and consumables |
| **Equipment** | Machinery and tools |
| **Labour** | Worker wages and fees |
| **Overhead** | Indirect costs |
| **Others** | Miscellaneous costs |

Each line includes **Product**, **Description**, **Quantity**, **UOM**, **Unit Price**, and computed **Amount**. Category-wise totals and a grand Total Amount are auto-calculated.

![Rate Analysis Form](https://docs.sdlccorp.com/assets/images/photo17-5cc4fe98c6023e8043d031e76a04af24.webp)
*Rate Analysis form with five category tabs and material line items*

![Rate Analysis Totals](https://docs.sdlccorp.com/assets/images/photo18-637515c4f76dfd94d10f40e3f8e30f71.webp)
*Rate Analysis with Material Total and overall Total Amount computation*

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Budgeting & BOQ](https://docs.sdlccorp.com/docs/19.0/construction-management/projects/budgeting/)
