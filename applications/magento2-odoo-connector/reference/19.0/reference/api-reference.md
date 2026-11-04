# Magento API Reference

The SDLC Magento 2 Connector communicates with Magento through its REST API. This page documents the API endpoints used by the connector and the fallback logic employed for reliability.

<a id="authentication"></a>

## Authentication

All API calls use the **Integration Access Token** configured on the Magento instance. The token is sent as a Bearer token in the HTTP Authorization header:

```
Authorization: Bearer <access_token>
```

<a id="api-endpoints"></a>

## API Endpoints

The connector uses the following Magento REST API endpoints:

<a id="product-endpoints"></a>

### Product Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/rest/V1/products` | Retrieve a list of products with filtering |
| `GET` | `/rest/V1/products/:sku` | Retrieve a single product by SKU |
| `POST` | `/rest/V1/products` | Create a new product |
| `PUT` | `/rest/V1/products/:sku` | Update an existing product |
| `GET` | `/rest/V1/products/attributes/sets/list` | Retrieve attribute sets |

<a id="customer-endpoints"></a>

### Customer Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/rest/V1/customers/search` | Search and retrieve customers |
| `GET` | `/rest/V1/customers/:customerId` | Retrieve a single customer |
| `POST` | `/rest/V1/customers` | Create a new customer |
| `PUT` | `/rest/V1/customers/:customerId` | Update an existing customer |

<a id="category-endpoints"></a>

### Category Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/rest/V1/categories` | Retrieve the category tree |
| `GET` | `/rest/V1/categories/:categoryId` | Retrieve a single category |
| `POST` | `/rest/V1/categories` | Create a new category |
| `PUT` | `/rest/V1/categories/:categoryId` | Update a category |

<a id="order-endpoints"></a>

### Order Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/rest/V1/orders` | Retrieve a list of orders with filtering |
| `GET` | `/rest/V1/orders/:orderId` | Retrieve a single order |
| `POST` | `/rest/V1/orders` | Create a new order |
| `PUT` | `/rest/V1/orders/:orderId` | Update an order |

<a id="invoice-endpoints"></a>

### Invoice Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/rest/V1/invoices` | Retrieve invoices |
| `POST` | `/rest/V1/order/:orderId/invoice` | Create an invoice for an order |

<a id="shipment-endpoints"></a>

### Shipment Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/rest/V1/shipments` | Retrieve shipments |
| `POST` | `/rest/V1/order/:orderId/ship` | Create a shipment for an order |

<a id="credit-memo-endpoints"></a>

### Credit Memo Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/rest/V1/creditmemos` | Retrieve credit memos |
| `POST` | `/rest/V1/order/:orderId/refund` | Create a credit memo/refund |

<a id="inventory-endpoints"></a>

### Inventory Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/rest/V1/stockItems/:productSku` | Get stock information for a product |
| `PUT` | `/rest/V1/products/:sku/stockItems/:itemId` | Update stock for a product |

<a id="api-fallback-logic"></a>

## API Fallback Logic

The connector implements a robust fallback strategy to handle API failures gracefully:

1. **Retry on Timeout** -- If an API call times out, the connector retries up to 3 times with exponential backoff (1s, 2s, 4s).
2. **Batch Processing** -- Large datasets are processed in batches to avoid API rate limits and memory issues.
3. **Partial Sync** -- If individual records fail, the connector continues processing remaining records and logs the errors.
4. **Token Refresh** -- If a `401 Unauthorized` response is received, the connector logs an error indicating the access token may have expired.
5. **Graceful Degradation** -- If a non-critical API endpoint is unavailable, the connector skips that data type and continues with other sync operations.

<a id="api-rate-limits"></a>

## API Rate Limits

Magento 2 does not enforce strict API rate limits by default, but your hosting provider or custom configuration may impose limits. The connector handles rate limiting by:

- Processing records in configurable batch sizes
- Implementing delays between large batch operations
- Logging `429 Too Many Requests` responses as retry-able errors

warning

If you encounter frequent `429` errors, increase the sync interval or contact your Magento hosting provider to adjust rate limits.

<a id="api-debugging"></a>

## API Debugging

To debug API communication:

1. Enable Odoo's developer mode.
2. Check the Odoo server log for API request/response details.
3. Review the [Sync Reports](sync-reports.md) for error messages.
4. Use a tool like Postman to test the Magento API directly with your access token.

tip

The Magento API returns detailed error messages in the response body. Check the Sync Reports error details for the full API error message.

<a id="next-steps"></a>

## Next Steps

- [Troubleshooting](troubleshooting.md)
- [FAQ](faq.md)
- [Sync Reports](sync-reports.md)

---

Source: [Magento API Reference](https://docs.sdlccorp.com/docs/19.0/magento2-odoo-connector/reference/api-reference/)
