# Queue Management


<a id="why-a-queue-exists"></a>

## Why a queue exists

The connector batches Shopify sync work into a queue so a failure on one record doesn't block the others. If product A fails to import because Shopify rate-limited the request, products B–Z still flow through. The queue is also what makes "retry just the failures" possible - without it, you'd have to re-run the whole batch.

In day-to-day operation you shouldn't need to touch the queue at all. The auto-scheduler keeps it drained. Visit this page when something looks wrong: orders trickling in, stock that hasn't updated, a warning banner on the dashboard.

<a id="overview"></a>

## Overview

The connector batches Shopify sync work into a queue so failures on one record don't block the others. The Queue Management screen is where you watch that queue, retry anything that failed, and clean out stale records once they're no longer needed.

The connector uses an async queue system for reliable, retryable processing.

<a id="viewing-the-queue"></a>

## Viewing the Queue

Navigate to **Shopify → Operations → Queue**:

| Column | Description |
| --- | --- |
| **Name** | Record type (Order, Product, Customer) |
| **State** | Draft / In Progress / Done / Failed |
| **Instance** | Shopify store instance |
| **Message** | Error details on failure |

<a id="retrying-failed-records"></a>

## Retrying Failed Records

1. Filter by **State = Failed**
2. Select the failed records
3. Click **Action → Set to Draft**
4. The cron will automatically reprocess them

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Queue Management](https://docs.sdlccorp.com/docs/shopify-odoo-connector/operations/queue-management/)
