# Webhook Logs


<a id="spotting-an-unhealthy-webhook"></a>

## Spotting an unhealthy webhook

A healthy webhook flow looks boring: events arrive, the connector acknowledges them, the queue stays empty. Use this page to spot the opposite:

- **Recurring failures from the same event type** - usually a Shopify-side rate limit or a duplicate registration.
- **Webhooks that haven't arrived in hours** - Shopify may have deactivated the endpoint after too many failures; re-register from [Webhook Configuration](../../../configuration/17.0/configuration/webhook-configuration.md).
- **Slow processing latency** - fine occasionally, concerning if persistent; check the queue.

<a id="overview"></a>

## Overview

This page is the operational dashboard for your Shopify webhooks. Once you've registered the webhooks in [Webhook Configuration](../../../configuration/17.0/configuration/webhook-configuration.md), use this view to:

- See every incoming event with its timestamp, type and processing status.
- Spot a sender that's failing repeatedly (often a Shopify-side rate limit or a duplicate registration).
- Inspect the full payload of any single delivery for debugging.

Monitor incoming webhook events from Shopify in real time.

<a id="viewing-webhook-activity"></a>

## Viewing Webhook Activity

Navigate to **Shopify → Reports → Webhook Reports**

![Reports menu showing Webhook Reports option](https://docs.sdlccorp.com/assets/images/shopify-report.webhokre-1-d25009d690a42318a16d1e965cd8fee5.webp)

| Column | Description |
| --- | --- |
| **Event** | Webhook topic (e.g., `orders/create`) |
| **Status** | Received / Processed / Failed |
| **Payload** | Raw JSON payload from Shopify |
| **Received At** | Timestamp |

You can also view **Mapping Reports** from the Reports menu.

![Reports menu showing Mapping Reports option](https://docs.sdlccorp.com/assets/images/shopify-report.mappingre-1-bea179306be7e498eff39a4ce3d8c36a.webp)

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Webhook Logs](https://docs.sdlccorp.com/docs/17.0/shopify-odoo-connector/reports/webhooks-configuration/)
