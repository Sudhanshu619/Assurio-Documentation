# Shopify Connector - Troubleshooting


<a id="before-you-open-a-support-ticket"></a>

## Before you open a support ticket

Walk through these in order - they cover ~80% of the issues we see:

1. **Confirm version** - Apps → Shopify Connector. We sometimes ship fixes for the exact issue you've hit.
2. **Test the connection** from the instance form. If it fails, the problem is upstream of any specific feature.
3. **Check the queue** - is there a backlog? Are the same records failing repeatedly?
4. **Check the Activity log** - recent API failures with status codes tell us more than "it doesn't work".

If you still need to open a ticket, include the version, the test-connection result, and a copy of one failing record from the queue.

<a id="common-issues"></a>

## Common Issues

<a id="-connection-test-fails"></a>

### ❌ Connection Test Fails

**Fix:**

1. Double-check the Shopify URL format: `mystore.myshopify.com` (no `https://`)
2. Verify the API key, secret, and access token are correct
3. Ensure the Private App has all required scopes enabled

---


<a id="-webhooks-not-triggering"></a>

### ❌ Webhooks Not Triggering

**Fix:**

1. Verify your Odoo URL is publicly accessible
2. Check firewall rules allow inbound HTTPS on port 443
3. Test the webhook URL manually

---


<a id="-orders-not-importing"></a>

### ❌ Orders Not Importing

**Fix:**

1. Check **Shopify → Operations → Queue** for errors
2. Try importing a specific order by ID to isolate the issue
3. Verify the Shopify order is in the correct status (paid/unfulfilled)

---


<a id="-stock-levels-incorrect"></a>

### ❌ Stock Levels Incorrect

**Fix:**

1. Go to **Shopify → Configuration → Location Mapping**
2. Ensure every Shopify location is mapped to an Odoo internal location
3. Re-run **Export Stock** after fixing the mapping

<a id="getting-support"></a>

## Getting Support

Email: [support@sdlccorp.com](mailto:support@sdlccorp.com)
Website: [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/)

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Shopify Connector - Troubleshooting](https://docs.sdlccorp.com/docs/shopify-odoo-connector/reference/troubleshooting/)
