# Smart Alert Engine

Proactive monitoring with **13 alert types** across **4 severity levels**. Automatically scans your Amazon business every 4 hours and surfaces critical issues before they impact revenue.

<a id="severity-levels"></a>

## Severity Levels

| Level | Priority | Response |
| --- | --- | --- |
| **Critical** | Urgent action required | Immediate investigation |
| **Urgent** | High priority | Same-day action |
| **Warning** | Needs attention | Review within 24–48 hours |
| **Info** | For awareness | Monitor trends |

<a id="complete-alert-types-reference"></a>

## Complete Alert Types Reference

| # | Alert Type | Description | Severity |
| --- | --- | --- | --- |
| 1 | **Stockout Risk** | Product predicted to run out of stock based on sales velocity | Critical |
| 2 | **Low Stock** | Inventory below configured threshold | Warning |
| 3 | **Price War Detected** | Competitors aggressively lowering prices | Urgent |
| 4 | **Buy Box Lost** | Lost the Buy Box to a competitor | Urgent |
| 5 | **Listing Suppressed** | Amazon has suppressed the product listing | Critical |
| 6 | **Possible Hijack** | Unauthorized seller detected on your listing | Critical |
| 7 | **Review Rating Drop** | Significant drop in product review rating | Warning |
| 8 | **Negative Margin** | Product selling below cost after fees | Urgent |
| 9 | **No Sales (7 days)** | No orders received for 7+ consecutive days | Warning |
| 10 | **Sync Error** | API sync failure detected | Info |
| 11 | **Policy Warning** | Potential Amazon policy compliance issue | Warning |
| 12 | **Competitor Undercut** | Competitor priced significantly below you | Warning |
| 13 | **High Return Rate** | Abnormally high return rate detected | Urgent |

<a id="alert-workflow"></a>

## Alert Workflow

```
New → Acknowledged → Resolved / Dismissed
```

| Status | Meaning |
| --- | --- |
| **New** | Just detected, needs review |
| **Acknowledged** | You've seen it and are working on it |
| **Resolved** | Issue fixed |
| **Dismissed** | False positive or not applicable |

<a id="automated-scanning"></a>

## Automated Scanning

| Scheduled Action | Interval |
| --- | --- |
| **Smart Alert Scan** | Every 4 hours |

Enable this scheduled action from the instance form or **Configuration > Technical > Scheduled Actions**.

<a id="accessing-alerts"></a>

## Accessing Alerts

<a id="active-alerts"></a>

### Active Alerts

Go to **Alerts > Active Alerts** to see all unresolved alerts. Filter by:

- Severity level
- Alert type
- Product
- Marketplace
- Date range

<a id="alert-history"></a>

### Alert History

**Alerts > Alert History** shows all alerts ever created, including resolved and dismissed ones, for trend analysis.

<a id="example-alert-responses"></a>

## Example Alert Responses

<a id="stockout-risk-critical"></a>

### Stockout Risk (Critical)

1. Check demand forecast for the product
2. Create a purchase order to replenish stock
3. Acknowledge the alert
4. Resolve once PO is confirmed and inventory is on the way

<a id="possible-hijack-critical"></a>

### Possible Hijack (Critical)

1. Identify the unauthorized seller
2. Report to Amazon via the brand registry
3. File an infringement claim if applicable
4. Monitor the listing until the seller is removed

<a id="negative-margin-urgent"></a>

### Negative Margin (Urgent)

1. Open **Profit Calculator** for the product
2. Review cost breakdown
3. Raise the price via **AI Price Optimizer** or reduce costs
4. Resolve alert once margin is positive

tip

Review alerts every morning as part of your routine. Acknowledging alerts promptly prevents them from piling up and helps the AI learn which alerts are most relevant to your business.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Smart Alert Engine](https://docs.sdlccorp.com/docs/17.0/amazon-odoo-connector/ai-features/smart-alerts/)
