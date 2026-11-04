# Amazon Connector - FAQ & Troubleshooting


<a id="frequently-asked-questions"></a>

## Frequently Asked Questions

<a id="which-odoo-versions-are-supported"></a>

### Which Odoo versions are supported?

Odoo 17, 18, and 19 (both Community and Enterprise editions).

<a id="which-amazon-marketplaces-are-supported"></a>

### Which Amazon marketplaces are supported?

25+ marketplaces across 3 regions:

- **North America:** US, Canada, Mexico, Brazil
- **Europe:** UK, Germany, France, Italy, Spain, Netherlands, Sweden, Poland, Belgium, Turkey, UAE, Saudi Arabia, Egypt, India
- **Far East:** Japan, Australia, Singapore

<a id="whats-the-difference-between-fbm-and-fba"></a>

### What's the difference between FBM and FBA?

- **FBM (Fulfilled by Merchant):** You store, pack, and ship inventory yourself
- **FBA (Fulfilled by Amazon):** Amazon stores your inventory and fulfills orders from their warehouses

The connector supports both, and you can mix strategies per product.

<a id="do-i-need-aws-credentials"></a>

### Do I need AWS credentials?

Yes. Amazon's SP-API requires request signing using AWS IAM credentials. You'll need:

- SP-API refresh token (from your Amazon developer app)
- LWA Client ID and Client Secret
- AWS IAM user Access Key and Secret Key

<a id="is-ai-required"></a>

### Is AI required?

No. All AI features are optional. The connector works fully without AI for order, product, price, and stock sync. AI features add listing optimization, pricing intelligence, forecasting, and proactive alerts.

<a id="which-ai-provider-should-i-choose"></a>

### Which AI provider should I choose?

- **Groq** - Free tier, great for testing
- **OpenAI** (GPT-4) - Highest accuracy, best for production
- **Claude** (Sonnet 4) - Best reasoning for complex analysis
- **Gemini** (2.0 Flash) - Fast and affordable for high-volume use

<a id="how-do-i-handle-rate-limits"></a>

### How do I handle rate limits?

The connector automatically retries rate-limited requests with exponential backoff (1.5s → 3s → 6s). If you still see many 429 errors, increase scheduled action intervals.

<a id="troubleshooting"></a>

## Troubleshooting

<a id="test-connection-fails"></a>

### Test Connection fails

**Possible causes:**

- Invalid SP-API refresh token (expired or wrong region)
- Wrong AWS credentials
- Missing IAM policy for SP-API
- Wrong marketplace region selected

**Solution:** Double-check credentials in your Amazon developer console and AWS IAM. Ensure the IAM user has `execute-api:Invoke` permission for SP-API.

<a id="error-4000003-when-creating-listings"></a>

### Error 4000003 when creating listings

**Cause:** Wrong product type for the Amazon category

**Solution:** The **Product Type Detection** AI feature automatically fixes this. Enable AI features and retry. Without AI, manually select the correct product type on the product form.

<a id="orders-not-syncing"></a>

### Orders not syncing

**Checklist:**

1. Is the scheduled action enabled? (Import FBM Orders or Import All Orders)
2. Check **Reports > Sync Logs** for errors
3. Verify the marketplace is selected on the instance
4. Run **Import Orders** manually to test
5. Check Amazon Seller Central for unfulfillable orders

<a id="stock-not-matching-between-odoo-and-amazon"></a>

### Stock not matching between Odoo and Amazon

**Common causes:**

- FBA and FBM stock mixed in the same warehouse
- Manual stock adjustments in Amazon not pulled yet
- Multiple instances writing to the same products

**Solution:** Use separate warehouses (see [Pro Tips](pro-tips.md)). Run **Pull FBA Stock Levels** manually to force a fresh sync.

<a id="settlement-reports-not-matching-sale-orders"></a>

### Settlement reports not matching sale orders

**Cause:** Timing mismatch between when Amazon settled the payment and when the sale order was completed in Odoo.

**Solution:** Settlement reports use Amazon's disbursement cycle (usually bi-weekly). Reconciliation may span multiple sale orders. Use the variance report to identify discrepancies.

<a id="ai-features-not-working"></a>

### AI features not working

**Checklist:**

1. Global AI toggle enabled in Settings
2. AI Provider selected on the instance
3. API key entered and saved
4. **Test AI Connection** succeeds
5. Sufficient API credits with your provider (OpenAI, Claude, etc.)

<a id="rate-limited-errors-in-ai-logs"></a>

### "Rate limited" errors in AI logs

**Cause:** Too many AI calls in a short time

**Solution:** Use Groq (free, high rate limits) for bulk operations, or throttle bulk AI actions. Consider upgrading your OpenAI/Claude tier for higher rate limits.

<a id="support"></a>

## Support

| Channel | Details |
| --- | --- |
| **Email** | [sales@sdlccorp.com](mailto:sales@sdlccorp.com) |
| **Website** | [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) |
| **License** | LGPL-3 |
| **Module Version** | 3.0 (SP-API + AI) |
| **Author** | SDLC Corp |

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Amazon Connector - FAQ & Troubleshooting](https://docs.sdlccorp.com/docs/19.0/amazon-odoo-connector/reference/faq/)
