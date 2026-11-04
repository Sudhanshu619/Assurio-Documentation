# Webhook Configuration


<a id="when-to-use-webhooks-vs-polling"></a>

## When to use webhooks vs polling

Polling (the scheduled cron jobs) is the connector's safety net - it catches anything webhooks missed. Webhooks are how the connector reacts in seconds rather than minutes. Use both: register webhooks for the events that matter most (new order, order paid, fulfilment), and leave the cron job in place to catch up if a webhook fails.

The connector ships with one-click webhook registration, so you don't need to click around the Shopify admin.

<a id="overview"></a>

## Overview

Webhooks let Shopify push events to Odoo the moment they happen - a new order, a customer update, a stock change - instead of waiting for the next scheduled sync. The connector ships with a one-click registration step that creates every webhook Shopify supports for the integration.

Webhooks enable real-time sync between Shopify and Odoo.

<a id="auto-register-webhooks"></a>

## Auto-Register Webhooks

1. Go to **Shopify → Configuration → Shopify Instances**
2. Open your instance
3. Click **Register Webhooks**
4. All webhooks are created automatically in Shopify

<a id="registered-webhook-events"></a>

## Registered Webhook Events

| Event | Trigger |
| --- | --- |
| `orders/create` | New order placed |
| `orders/updated` | Order status changed |
| `orders/cancelled` | Order cancelled |
| `orders/fulfilled` | Order shipped |
| `refunds/create` | Refund issued |
| `products/create` | New product added |
| `products/update` | Product updated |
| `inventory_levels/update` | Stock changed |
| `customers/create` | New customer |

<a id="troubleshooting"></a>

## Troubleshooting

**Webhooks not triggering?**

- Ensure Odoo is accessible from the internet
- Check **Shopify → Operations → Webhook Logs** for delivery errors
- Re-register webhooks from the instance configuration

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Webhook Configuration](https://docs.sdlccorp.com/docs/shopify-odoo-connector/configuration/webhook-configuration/)
