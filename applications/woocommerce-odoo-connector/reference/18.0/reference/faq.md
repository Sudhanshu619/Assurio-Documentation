# WooCommerce Connector - Troubleshooting and FAQ


<a id="when-to-check-this-page"></a>

## When to check this page

Most of these questions come up during the first week of operation. Once your sync is humming, you'll rarely need to come back. For issues not covered here, the [WooCommerce Connector troubleshooting](../../../configuration/18.0/configuration/settings.md) page covers operational symptoms.

<a id="connection-failed"></a>

### Connection Failed

- Verify Consumer Key and Consumer Secret are correct
- Ensure store URL uses HTTPS (WooCommerce requires SSL for REST API)
- Check that WooCommerce REST API is enabled (WooCommerce > Settings > Advanced > REST API)
- Verify API key has Read/Write permissions

<a id="products-not-syncing"></a>

### Products Not Syncing

- Ensure products have a SKU set in WooCommerce
- Check sync logs for specific API errors
- Verify field mappings if custom mappings are configured

<a id="orders-missing-line-items"></a>

### Orders Missing Line Items

- Check that products exist in Odoo (sync products first)
- Verify the order API response includes line_items
- Check sync logs for parsing errors

<a id="webhooks-not-working"></a>

### Webhooks Not Working

- Verify the webhook URL is accessible from the internet (not localhost)
- Check that the webhook secret matches in both WooCommerce and Odoo
- Ensure Odoo server has a valid SSL certificate

<a id="support"></a>

## Support

| Channel | Details |
| --- | --- |
| **Email** | [support@sdlc.com](mailto:support@sdlc.com) |
| **Module Version** | 1.0.0 |
| **Compatible Odoo** | Odoo 18 Community and Enterprise |
| **Compatible WooCommerce** | WooCommerce 7.x, 8.x, 9.x |
| **License** | LGPL-3 |

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [WooCommerce Connector - Troubleshooting and FAQ](https://docs.sdlccorp.com/docs/18.0/woocommerce-odoo-connector/reference/faq/)
