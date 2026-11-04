# ShipStation Connector - Troubleshooting and FAQ


<a id="whats-in-this-faq"></a>

## What's in this FAQ

Quick answers to the operational questions we hear most often during onboarding. For deeper coverage of each topic, follow the links into the rest of the connector documentation.

<a id="connection-failed"></a>

### Connection Failed

- Verify your API Key and Secret are correct
- Check that the API URL is correct (use the default ShipStation API endpoint)
- Ensure your ShipStation account has API access enabled
- Check your firewall/proxy settings

<a id="orders-not-syncing"></a>

### Orders Not Syncing

- Check the Order Status Filter on the instance
- Verify the 'Days Back' setting covers the date range of your orders
- Check **Sync Logs** for API errors
- Ensure the cron job for orders is enabled and running

<a id="products-not-matching"></a>

### Products Not Matching

- Products are matched by SKU/reference code. Ensure SKUs match between Odoo and ShipStation
- If no match is found, a new product is created in Odoo
- Use Field Mapping to customize which fields are synced

<a id="inventory-discrepancies"></a>

### Inventory Discrepancies

- Click 'Refresh Inventory' to pull latest stock levels
- Check that inventory sync cron is enabled
- Stock is automatically adjusted when orders are marked as delivered

<a id="support"></a>

## Support

| Channel | Details |
| --- | --- |
| **Email** | [support@sdlc.com](mailto:support@sdlc.com) |
| **Module Version** | 18.0.1.0.0 |
| **Compatible Odoo** | Odoo 18 Community and Enterprise |
| **License** | LGPL-3 |

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [ShipStation Connector - Troubleshooting and FAQ](https://docs.sdlccorp.com/docs/18.0/shipstation-odoo-connector/reference/faq/)
