# PrestaShop Connector - Troubleshooting


<a id="connection-test-fails"></a>

## Connection Test fails

- Verify the **Store URL** is correct and accessible from the server
- Check the API key has **full permissions** in PrestaShop
- Try adding `/api` to the URL manually in the Webservice URL field
- Check if the PrestaShop webservice is **enabled**
- Look at the **"Last Error"** field for specific error messages

---


<a id="no-products-imported"></a>

## No products imported

- Ensure connection is established (status = Connected)
- Check if products exist in PrestaShop
- Look at **Sync Reports** for error details
- Verify the API key has GET permission on "products" resource

---


<a id="field-mapping-not-working"></a>

## Field mapping not working

- Verify the mapping is **Active** (toggle ON)
- Check the **Direction** matches your sync flow
- Use the **Test** button to validate the mapping
- Ensure the Odoo field name matches an actual stored field
- Check Sync Reports for mapping-related errors

---


<a id="auto-sync-cron-not-running"></a>

## Auto sync cron not running

- Verify **Auto Sync Enabled** is checked
- Check that the instance is in **Connected** state
- Go to **Settings > Technical > Scheduled Actions** and find the cron
- Verify the **Next Execution Date** is set correctly
- Check the Odoo server logs for cron errors

---


<a id="images-not-syncing"></a>

## Images not syncing

- Ensure the PrestaShop API has **image permissions** enabled
- Check if the product has images in PrestaShop
- Large images may timeout - check server timeout settings

<a id="need-help"></a>

## Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/)

---

Source: [PrestaShop Connector - Troubleshooting](https://docs.sdlccorp.com/docs/prestashop-odoo-connector/reference/troubleshooting/)
