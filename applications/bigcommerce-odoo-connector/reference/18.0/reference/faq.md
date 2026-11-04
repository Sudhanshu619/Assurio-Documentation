# BigCommerce Connector - Troubleshooting and FAQ


<a id="what-this-faq-covers"></a>

## What this FAQ covers

Most questions on this page come up in the first week of operation - connection failures, webhook setup, sync timing. Once the connector is humming, day-to-day operation rarely needs the FAQ; see the [Settings](../../../configuration/18.0/configuration/settings.md) page when you need to retune.

<a id="connection-failed"></a>

### Connection Failed

- Verify Store Hash, Access Token, Client ID, and Client Secret
- Ensure API account has required OAuth scopes (Products, Orders, Customers modify)
- Check that your BigCommerce store is active and not suspended

<a id="products-not-syncing"></a>

### Products Not Syncing

- Ensure products have a SKU set in BigCommerce
- Check product bindings for error status
- Review sync logs for specific API error messages

<a id="orders-missing"></a>

### Orders Missing

- Check the order date range (default sync is recent orders only)
- Verify order status filter matches expected orders
- Ensure customer sync has run first (orders link to customers)

<a id="webhooks-not-working"></a>

### Webhooks Not Working

- Verify Odoo server is accessible from the internet
- Check webhook subscriptions are active in BigCommerce admin
- Ensure the webhook cron job is running

<a id="support"></a>

## Support

| Channel | Details |
| --- | --- |
| **Email** | [support@sdlc.com](mailto:support@sdlc.com) |
| **Module Version** | 18.0.2.0.0 |
| **Compatible Odoo** | Odoo 18 Community and Enterprise |
| **Compatible BigCommerce** | BigCommerce V2/V3 API |
| **License** | LGPL-3 |

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [BigCommerce Connector - Troubleshooting and FAQ](https://docs.sdlccorp.com/docs/18.0/bigcommerce-odoo-connector/reference/faq/)
