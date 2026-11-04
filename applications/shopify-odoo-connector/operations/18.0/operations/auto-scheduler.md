# Auto Scheduler (Cron Jobs)


<a id="why-use-the-auto-scheduler"></a>

## Why use the auto-scheduler

Auto-scheduled cron jobs are the difference between a connector that's set up and a connector that's actually operating. They're what catches new orders within minutes of placement, exports tracking numbers without warehouse intervention, and keeps stock counts close to real-time between Shopify and Odoo.

Default schedules work for most stores. Re-tune them only if you see queue lag (raise frequency) or hit Shopify rate limits (lower frequency).

The connector includes pre-configured scheduled actions for regular background sync.

<a id="available-cron-jobs"></a>

## Available Cron Jobs

| Job | Default Interval | Purpose |
| --- | --- | --- |
| Import Unshipped Orders | Every 15 minutes | Pull new orders from Shopify |
| Import Shipped Orders | Every 30 minutes | Update shipped orders |
| Export Stock to Shopify | Every 1 hour | Push inventory updates |
| Import Products | Every 6 hours | Sync product changes |
| Process Queue | Every 5 minutes | Process pending queue records |

<a id="configuring-schedules"></a>

## Configuring Schedules

1. Go to **Settings → Technical → Automation → Scheduled Actions**
2. Find the Shopify cron jobs (prefixed with "Shopify")
3. Adjust the **Interval Number** and **Interval Unit**
4. Enable/disable as needed

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

<a id="related"></a>

## Related

- [Queue Management](queue-management.md) - when a scheduled run leaves work in the queue.
- [Webhook Configuration](../../../configuration/18.0/configuration/webhook-configuration.md) - pair scheduled polling with real-time webhooks for the best of both.
- [Troubleshooting](../../../reference/18.0/reference/troubleshooting.md) - what to do when a job stops running.

---

Source: [Auto Scheduler (Cron Jobs)](https://docs.sdlccorp.com/docs/18.0/shopify-odoo-connector/operations/auto-scheduler/)
