# Pro Tips & Best Practices

Expert tips from the SDLC Corp team to maximize your success with the Amazon connector.

<a id="start-small"></a>

## Start Small

tip

Import a few products first, test the full order flow end-to-end, then gradually enable automation. This helps catch configuration issues early without affecting your live listings.

<a id="recommended-rollout"></a>

### Recommended Rollout

1. **Week 1:** Connect instance, test API, import 5 products manually
2. **Week 2:** Process a handful of orders manually through the full lifecycle
3. **Week 3:** Enable FBM order import scheduled action
4. **Week 4:** Enable price/stock sync and settlement imports
5. **Month 2+:** Full automation with AI features

<a id="separate-warehouses"></a>

## Separate Warehouses

Use **different Odoo warehouses for FBA and FBM stock**. This keeps inventory movements clean and prevents stock counting errors between fulfillment channels.

<a id="recommended-warehouse-structure"></a>

### Recommended Warehouse Structure

- **Warehouse A - Main:** Your own fulfillment (FBM, direct-to-consumer)
- **Warehouse B - Amazon FBA:** Virtual warehouse representing Amazon fulfillment centers
- **Warehouse C - Returns:** Handling returns from both channels

<a id="choose-the-right-ai-provider"></a>

## Choose the Right AI Provider

| Use Case | Recommended Provider |
| --- | --- |
| **Testing / Development** | Groq (free tier) |
| **Production - Best Quality** | OpenAI GPT-4 or Claude |
| **Production - Best Value** | Google Gemini |
| **High-Volume Listing Generation** | Groq or Gemini (faster) |
| **Complex Analysis** | Claude Sonnet 4 |

<a id="monitor-sync-logs"></a>

## Monitor Sync Logs

tip

Always review **Sync Logs** (Reports > Sync Logs) after enabling a new scheduled action. This helps you catch API errors, rate limiting issues, or data mapping problems early.

<a id="what-to-look-for"></a>

### What to Look For

- Consistent 200/201 responses = healthy
- Occasional 429 (rate limit) = normal, retry will handle
- Many 429 errors = increase sync intervals
- 4xx errors other than 429 = configuration or data issue
- 5xx errors = Amazon API issue, usually temporary

<a id="use-smart-alerts"></a>

## Use Smart Alerts

Enable the **Smart Alert Scan** scheduled action. It proactively detects issues like:

- Stockouts before they happen
- Price wars
- Listing suppressions
- Possible hijacks

before they impact your revenue.

<a id="leverage-product-health-scores"></a>

## Leverage Product Health Scores

Enable the daily **Product Health** calculation. Products with grade **D or F** need immediate attention.

tip

Focus on improving the lowest-scoring dimension first. If a product scores poorly on "Listing Quality," better content will have more impact than lowering the price.

<a id="bulk-operations"></a>

## Bulk Operations

Use the **Import / Map Products** wizard for initial setup:

- Supports CSV and Excel files
- Flexible column mapping
- Handles thousands of SKUs efficiently

For ongoing updates, use the scheduled sync actions instead of manual imports.

<a id="handle-api-rate-limits"></a>

## Handle API Rate Limits

The connector has built-in retry with exponential backoff (1.5s, 3s, 6s) for rate-limited requests.

warning

If you see many 429 errors in logs, increase the sync intervals. Amazon enforces different rate limits per API endpoint - some allow 1 request/second, others 5 requests/second.

<a id="rate-limit-guidelines"></a>

### Rate Limit Guidelines

| Operation | Recommended Minimum Interval |
| --- | --- |
| **Order Sync** | 15 min |
| **Product Sync** | 6 hours |
| **Price Updates** | 4 hours |
| **Stock Updates** | 2 hours |
| **FBA Reports** | 4+ hours |
| **Settlement Reports** | Daily |

<a id="ai-api-key-security"></a>

## AI API Key Security

warning

Never commit API keys (OpenAI, Claude, Gemini, Groq) to version control or share them between environments. Store them in Odoo's encrypted instance fields.

<a id="performance-optimization"></a>

## Performance Optimization

- Disable scheduled actions you don't need - don't enable everything
- Configure log retention to purge old data
- Review Sync Reports weekly for failure trends
- Set reasonable AI usage thresholds to control costs

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Pro Tips & Best Practices](https://docs.sdlccorp.com/docs/19.0/amazon-odoo-connector/reference/pro-tips/)
