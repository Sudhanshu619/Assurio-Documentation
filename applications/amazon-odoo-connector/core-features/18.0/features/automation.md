# Automation and Scheduling

The connector includes **15 scheduled actions** (all disabled by default). Enable them selectively on your Instance form or via **Configuration > Technical > Scheduled Actions**.

<a id="complete-schedule-reference"></a>

## Complete Schedule Reference

| Scheduled Action | Interval | Category |
| --- | --- | --- |
| **Import All Orders (FBM+FBA)** | 30 min | Orders |
| **Import FBM Orders** | 15 min | FBM |
| **Sync Products** | 6 hours | Products |
| **Update Prices** | 4 hours | Prices |
| **Export Stock Levels** | 2 hours | FBM Stock |
| **Pull FBA Stock Levels** | 4 hours | FBA Stock |
| **Pull FBA Prices** | 6 hours | FBA Prices |
| **Update FBM Order Status** | 1 hour | FBM Orders |
| **Check Cancelled Orders** | 2 hours | Orders |
| **Import Settlement Reports** | Daily | Accounting |
| **Import Removal Orders** | Daily | FBA |
| **Full Bidirectional Sync** | 1 hour | Master |
| **Master Auto-Sync Scheduler** | 15 min | Master |
| **Smart Alert Scan** | 4 hours | AI/Alerts |
| **Calculate Product Health** | Daily | AI/Health |

<a id="recommended-setup"></a>

## Recommended Setup

<a id="beginner-start-small"></a>

### Beginner (Start Small)

Enable these first and verify they work before expanding:

- Import All Orders (FBM+FBA) - 30 min
- Update FBM Order Status - 1 hour
- Import Settlement Reports - Daily

<a id="production-full-automation"></a>

### Production (Full Automation)

Once comfortable, enable all scheduled actions for complete automation:

- All order, product, price, and stock syncs
- Smart Alert Scan for proactive monitoring
- Calculate Product Health for AI health scoring

<a id="api-rate-limits"></a>

## API Rate Limits

warning

The connector has built-in retry with exponential backoff (1.5s, 3s, 6s) for rate-limited requests. If you see many 429 errors in logs, increase the sync intervals to reduce API call frequency.

<a id="managing-scheduled-actions"></a>

## Managing Scheduled Actions

<a id="from-the-instance-form"></a>

### From the Instance Form

Open your Amazon instance and toggle each scheduled action on or off directly.

<a id="from-technical-menu"></a>

### From Technical Menu

Navigate to **Configuration > Technical > Scheduled Actions** and filter by "amazon" to see all connector actions. You can:

- Enable/disable individual actions
- Adjust intervals
- Run manually on demand
- Review last execution log

tip

Always review **Sync Logs** (Reports > Sync Logs) after enabling a new scheduled action. This helps catch API errors, rate limiting issues, or data mapping problems early.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Automation and Scheduling](https://docs.sdlccorp.com/docs/18.0/amazon-odoo-connector/features/automation/)
