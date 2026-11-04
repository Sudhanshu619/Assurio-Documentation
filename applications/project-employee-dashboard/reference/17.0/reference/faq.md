# Project & Employee Dashboard - Frequently Asked Questions


<a id="common-questions"></a>

## Common Questions

<a id="does-the-dashboard-work-without-the-timesheets-module"></a>

### Does the dashboard work without the Timesheets module?

Yes. The Timesheet Hours chart is automatically hidden if `hr_timesheet` is not installed. All other features work normally.

---


<a id="how-often-does-the-data-refresh"></a>

### How often does the data refresh?

The dashboard auto-refreshes every 60 seconds. You can also press **R** to manually refresh at any time. A green **Live** badge in the header indicates active monitoring.

---


<a id="can-i-filter-by-multiple-criteria-at-once"></a>

### Can I filter by multiple criteria at once?

Yes. You can combine filters for Project, Department, Date From, and Date To. All filters apply simultaneously and every chart, card, and table updates instantly.

---


<a id="what-is-the-productivity-score"></a>

### What is the Productivity Score?

It is a 0--100 gauge calculated from: completion rate (60% weight), overdue penalty (30% weight), and activity bonus (10% weight for having 5+ tasks).

---


<a id="how-are-the-smart-insights-generated"></a>

### How are the Smart Insights generated?

They are rule-based text insights, not AI or ML. The system evaluates completion rates, overdue counts, project progress, and workload balance to generate up to 5 actionable recommendations.

---


<a id="does-excel-export-require-anything-extra"></a>

### Does Excel export require anything extra?

Yes, the `xlsxwriter` Python library must be installed on the server. Install it with `pip install xlsxwriter`. If not installed, the export button shows a friendly error message. See the [Excel Export guide](../../../features/17.0/features/excel-export.md) for details.

---


<a id="does-the-export-respect-active-filters"></a>

### Does the export respect active filters?

Yes. Whatever filters you have applied on the dashboard are carried through to the Excel export. Only the filtered data appears in the downloaded file.

---


<a id="can-i-use-this-on-a-tv-or-projector"></a>

### Can I use this on a TV or projector?

Yes. Press **F** for fullscreen mode. Combined with the 60-second auto-refresh, it works perfectly as a live dashboard display for stand-up meetings or war rooms. See the [Fullscreen section](../../../features/17.0/features/actions-filters.md#fullscreen-mode) for details.

---


<a id="does-it-support-dark-mode"></a>

### Does it support dark mode?

Yes. The dashboard automatically detects your Odoo theme setting and adjusts all chart colours, card backgrounds, and text for both light and dark modes. See the [Dark Mode guide](../../../features/17.0/features/dark-mode.md) for details.

---


<a id="how-do-i-create-a-task-from-the-dashboard"></a>

### How do I create a task from the dashboard?

Press **N** or click the **+ Quick Task** button. Enter a task name, select a project, and click Submit. The task is created in Odoo and the dashboard refreshes automatically. See the [Quick Task section](../../../features/17.0/features/actions-filters.md#quick-task-create) for a walkthrough.

---


<a id="what-happens-when-all-tasks-are-completed"></a>

### What happens when all tasks are completed?

When your team reaches 100% completion, a celebratory confetti animation fires automatically on the dashboard.

---


<a id="which-odoo-version-is-supported"></a>

### Which Odoo version is supported?

The module is built for **Odoo 19**. It requires the Project and HR modules as dependencies.

---


<a id="how-do-i-get-support"></a>

### How do I get support?

Contact SDLC Corp via [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email [sales@sdlccorp.com](mailto:sales@sdlccorp.com).

---

Source: [Project & Employee Dashboard - Frequently Asked Questions](https://docs.sdlccorp.com/docs/17.0/project-employee-dashboard/reference/faq/)
