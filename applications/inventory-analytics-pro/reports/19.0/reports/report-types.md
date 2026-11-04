# Reports & Excel Export


<a id="report-wizard"></a>

## Report Wizard

Go to **Inventory Analytics > Reports > Generate Report** to open the wizard:

![Wizard Form](https://docs.sdlccorp.com/assets/images/22-wizard-form-75ac89c734156750b635b0a44eb28b70.webp)

<a id="configuration"></a>

### Configuration

| Field | Description |
| --- | --- |
| **From Date** | Start of analysis period (default: 90 days ago) |
| **To Date** | End of analysis period (default: today) |
| **Report Type** | Select from 10 specialized reports |
| **Warehouses** | Filter by warehouse (leave empty for all) |
| **Products** | Filter by specific products |
| **Product Categories** | Filter by category |

<a id="10-report-types"></a>

### 10 Report Types

![Report Types](https://docs.sdlccorp.com/assets/images/23-wizard-report-types-b2ed449034b114b8e31431b2c6dd89ba.webp)

| Report | Purpose | Key Columns |
| --- | --- | --- |
| **Dashboard Overview** | Opens interactive dashboard | Charts & KPIs |
| **Health Score** | Composite health grading | Score, Grade, Days Left |
| **Age Analysis** | Stock aging breakdown | Oldest Days, Bracket |
| **Turnover Analysis** | Sales velocity metrics | Opening, Closing, Margin |
| **FSN Classification** | Movement speed classification | FSN, Trend, Sold |
| **XYZ Classification** | Stock value classification | XYZ, Value, ABC |
| **ABC Revenue** | Revenue contribution ranking | Revenue, Share %, ABC |
| **Overstock Analysis** | Excess inventory identification | Overstock Qty/Value |
| **Out of Stock** | Stockout analysis | Days OOS, Lost Revenue |
| **Stock Movement** | In/out/transfer tracking | In, Out, Internal, Adjustments |

<a id="report-examples"></a>

## Report Examples

<a id="health-score-report"></a>

### Health Score Report

![Health Score](https://docs.sdlccorp.com/assets/images/24-report-health-score-aca51a5d860de8aec2b705554571c000.webp)

Color-coded rows: Green (A), Yellow (C/D), Red (F).

<a id="fsn-classification"></a>

### FSN Classification

![FSN](https://docs.sdlccorp.com/assets/images/25-report-fsn-f0e96d6f8003b9f72ce381746d734f66.webp)

Green = Fast Moving, Yellow = Slow Moving, Red = Non-Moving.

<a id="abc-revenue"></a>

### ABC Revenue

Shows revenue share per product with cumulative ABC classification.

<a id="overstock-analysis"></a>

### Overstock Analysis

![Overstock](https://docs.sdlccorp.com/assets/images/26-report-overstock-f21013e68a1630ce52fa512ceb676fbe.webp)

Red rows indicate products with overstock quantity > 0.

<a id="stock-movement"></a>

### Stock Movement

![Movement](https://docs.sdlccorp.com/assets/images/27-report-movement-d3f7fdade64101337d434adcb301f902.webp)

Tracks all stock flows: inbound, outbound, internal transfers, and adjustments.

<a id="turnover-analysis"></a>

### Turnover Analysis

![Turnover](https://docs.sdlccorp.com/assets/images/28-report-turnover-8f42a724435d8b08d7536df0b36cc848.webp)

Red rows = turnover below 1 (slow), Green rows = turnover above 3 (fast).

<a id="age-analysis"></a>

### Age Analysis

![Age](https://docs.sdlccorp.com/assets/images/29-report-age-a6eba9cd3ecdc508d2fa8d9959067c24.webp)

<a id="xyz-classification"></a>

### XYZ Classification

![XYZ](https://docs.sdlccorp.com/assets/images/30-report-xyz-89d7d0dfbe54927776097ba7b4ae5acf.webp)

Green = X (high value), Yellow = Y (medium).

<a id="excel-export"></a>

## Excel Export

From the wizard, click **Export to Excel** to download a formatted multi-sheet workbook:

![Excel Export](https://docs.sdlccorp.com/assets/images/36-excel-export-3e98cc52dd435cdc4bb68c620880ae9e.webp)

The Excel file includes:

- **8 sheets** (one per report type)
- Formatted headers with indigo background
- Grade-colored cells (A/B = green, C/D = yellow, F = red)
- Sum footers on numeric columns
- Frozen header rows

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Reports & Excel Export](https://docs.sdlccorp.com/docs/19.0/inventory-analytics-pro/reports/report-types/)
