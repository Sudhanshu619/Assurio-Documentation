# Interactive Analytics Dashboard

The dashboard provides a real-time overview of your inventory health with interactive charts, KPIs, and actionable insights.

<a id="health-score-gauge"></a>

## Health Score Gauge

The central gauge shows your **overall inventory health** on a 0-100 scale:

![Health Score Gauge](https://docs.sdlccorp.com/assets/images/04-dashboard-health-gauge-ea2bd18e4f02362fab388a9f400555ae.webp)

| Grade | Score | Meaning |
| --- | --- | --- |
| **A** | 85-100 | Excellent: well-optimized inventory |
| **B** | 70-84 | Good: minor improvements possible |
| **C** | 55-69 | Average: attention needed |
| **D** | 40-54 | Poor: significant issues |
| **F** | 0-39 | Critical: immediate action required |

The score is a weighted composite of: turnover ratio (30%), gross margin (20%), days of stock (25%), stock age (15%), and out-of-stock penalty (-10 points).

<a id="kpi-cards"></a>

## KPI Cards

![KPI Cards](https://docs.sdlccorp.com/assets/images/05-dashboard-kpi-cards-54792a0c9cf47486598d49da3f61b9bc.webp)

| KPI | What It Shows |
| --- | --- |
| **Stock Value** | Total value of all inventory on hand |
| **Avg Turnover** | Mean turnover ratio across all products |
| **Out of Stock** | Count of products with zero stock |
| **Overstock Value** | Total value of excess inventory (beyond 90-day need) |

<a id="filters"></a>

## Filters

Use the left sidebar to filter dashboard data:

![Filters](https://docs.sdlccorp.com/assets/images/06-dashboard-filters-sidebar-13d30cfc2c498709dbb1c670121de596.webp)

| Filter | Options |
| --- | --- |
| **Period** | Last 30/90/180/365 days, or custom date range |
| **Warehouse** | All or specific warehouse |
| **Category** | All or specific product category |
| **FSN Class** | All, Fast, Slow, or Non-Moving |
| **Health Grade** | All, A, B, C, D, or F |

Custom date range:

![Custom Period](https://docs.sdlccorp.com/assets/images/07-dashboard-period-custom-91c39a607ff6a7e043ea373fa24871fb.webp)

Filtered results:

![Filtered](https://docs.sdlccorp.com/assets/images/08-dashboard-filtered-443ec56d71a85f81468657829b250168.webp)

<a id="classification-charts"></a>

## Classification Charts

<a id="fsn-distribution"></a>

### FSN Distribution

![FSN Chart](https://docs.sdlccorp.com/assets/images/09-chart-fsn-bar-4e989ece516bbe67c4b149cd7c4a8d25.webp)

- **Fast Moving (F)**: Turnover ratio > 3
- **Slow Moving (S)**: Turnover ratio 1-3
- **Non-Moving (N)**: Turnover ratio below 1

<a id="abc-revenue-split"></a>

### ABC Revenue Split

![ABC Chart](https://docs.sdlccorp.com/assets/images/10-chart-abc-doughnut-6ba66391077d8fad9618fa9530142992.webp)

- **A**: Top 80% cumulative revenue
- **B**: Next 15% (80-95%)
- **C**: Bottom 5% (95-100%)

<a id="abc-fsn-matrix"></a>

### ABC-FSN Matrix

![Matrix](https://docs.sdlccorp.com/assets/images/11-matrix-abc-fsn-801d046c3c30bbdcf823019e38a40c48.webp)

A 3x3 grid combining ABC (revenue) and FSN (movement) classifications to identify strategic product segments.

<a id="insights"></a>

## Insights

<a id="inventory-aging"></a>

### Inventory Aging

![Age Chart](https://docs.sdlccorp.com/assets/images/12-chart-age-bars-92770934a4ae37cbb7d3f1a45db56eb2.webp)

Brackets: 0-30 days, 31-60, 61-90, 91-180, and 180+ days.

<a id="demand-trends"></a>

### Demand Trends

![Trends](https://docs.sdlccorp.com/assets/images/13-chart-trends-doughnut-a825dfc8ab2a5a48b8e9deab90a80ba8.webp)

Compares first-half vs second-half period sales to detect direction.

<a id="category-wise-fsn"></a>

### Category-wise FSN

![Category FSN](https://docs.sdlccorp.com/assets/images/14-chart-category-fsn-stacked-14ca4705858698fe07530a8c1648d0d2.webp)

Identifies which product categories have the most non-moving stock.

<a id="rankings"></a>

## Rankings

**Top 5 Revenue Generators:**

![Top 5](https://docs.sdlccorp.com/assets/images/15-top5-revenue-541028c701621556532a7f7a8ea42f39.webp)

**Bottom 5 by Health Score:**

![Bottom 5](https://docs.sdlccorp.com/assets/images/16-bottom5-health-6ceaebf49e83ebc780ce8f10618bf4e4.webp)

<a id="cash-flow-impact"></a>

## Cash Flow Impact

![Cash Flow](https://docs.sdlccorp.com/assets/images/17-cash-flow-tiles-62a1f01c03e3baefdbba62a6d4ac3df1.webp)

| Metric | Description |
| --- | --- |
| **Capital Locked** | Total stock value tied up |
| **Daily Holding Cost** | ~25% annual carrying cost / 365 |
| **Dead Stock Value** | Value in non-moving products |
| **Potential Savings** | Estimated savings if dead/slow stock cleared |

<a id="stock-coverage"></a>

## Stock Coverage

![Coverage](https://docs.sdlccorp.com/assets/images/18-stock-coverage-timeline-d01cfd02f73fdc47b8b86d9db2d3d5e4.webp)

Shows days of stock remaining for the 15 most urgent products. Color: Red (under 14 days), Amber (14-30), Green (30-90), Blue (90+).

<a id="executive-summary"></a>

## Executive Summary

![Summary](https://docs.sdlccorp.com/assets/images/19-executive-summary-531f79edd27bfa877522973f3577b8b3.webp)

Auto-generated insights highlighting critical issues, growth opportunities, and top performers.

<a id="attention-products"></a>

## Attention Products

![Attention](https://docs.sdlccorp.com/assets/images/20-attention-products-6403ca8dbcd96192501c3c5498711725.webp)

Bottom 10 products by health score. Out-of-stock items show a **Create RFQ** button:

![Create RFQ](https://docs.sdlccorp.com/assets/images/21-create-rfq-button-443298476598041789f11e5d0d9ccd2a.webp)

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Interactive Analytics Dashboard](https://docs.sdlccorp.com/docs/17.0/inventory-analytics-pro/dashboard/overview/)
