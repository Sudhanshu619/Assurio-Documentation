# Inventory Analytics Pro - Frequently Asked Questions


<a id="common-questions"></a>

## Common Questions

<a id="does-it-work-with-odoo-community-and-enterprise"></a>

### Does it work with Odoo Community and Enterprise?

Yes. The module supports both Odoo 19 Community and Enterprise editions.

---


<a id="do-i-need-to-import-data"></a>

### Do I need to import data?

No. The module reads directly from your existing Sales, Purchase, and Inventory modules. Any data you already have is automatically analyzed.

---


<a id="what-if-i-have-no-sales-history"></a>

### What if I have no sales history?

Products without sales history will show as Non-Moving (FSN = N) with low health scores. The dashboard will still work but classifications will be limited.

---


<a id="how-often-is-the-dashboard-updated"></a>

### How often is the dashboard updated?

Every time you open the dashboard, it recomputes from fresh data. There is no caching: you always see current results.

---


<a id="can-i-filter-by-multiple-warehouses"></a>

### Can I filter by multiple warehouses?

From the dashboard, you can filter by one warehouse at a time. From the Report Wizard, you can select multiple warehouses using the tags widget.

---


<a id="how-does-the-health-score-work"></a>

### How does the Health Score work?

It's a weighted composite: Turnover (30%), Margin (20%), Days of Stock (25%), Age (15%), and OOS Penalty (-10). Scores range from 0-100 with letter grades A through F.

---


<a id="what-does-overstock-mean"></a>

### What does "Overstock" mean?

A product is overstocked when its current quantity exceeds 90 days of average sales. The overstock value = excess quantity x unit cost.

---


<a id="how-do-alerts-work"></a>

### How do alerts work?

A daily scheduled action checks all active alert rules. When products match the alert condition, it creates a Todo activity for each configured user with product details and a dashboard link.

---


<a id="can-i-export-to-excel"></a>

### Can I export to Excel?

Yes. From the Report Wizard, click **Export to Excel** to download a multi-sheet formatted workbook with all 8 report types.

---


<a id="who-can-access-the-module"></a>

### Who can access the module?

- **Stock Users**: Can view reports and reorder suggestions
- **Stock Managers**: Full access including alert configuration

---


<a id="does-it-affect-my-inventory-data"></a>

### Does it affect my inventory data?

No. The module only **reads** from existing tables. It never modifies your sales orders, stock quantities, or purchase orders. The only write operation is creating draft POs via the "Create RFQ" button.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Inventory Analytics Pro - Frequently Asked Questions](https://docs.sdlccorp.com/docs/17.0/inventory-analytics-pro/reference/faq/)
