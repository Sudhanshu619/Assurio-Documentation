# Amazon Connector - Installation and Setup


<a id="prerequisites"></a>

## Prerequisites

- Odoo 17, 18, or 19 (Community or Enterprise edition)
- Active Amazon Seller Central account
- Amazon SP-API application credentials (refresh token, Client ID, Client Secret)
- AWS IAM user with Access Key and Secret Key for SP-API signing

<a id="step-by-step-setup"></a>

## Step-by-Step Setup

<a id="step-1-create-an-instance"></a>

### Step 1. Create an Instance

Go to **Amazon > Configuration > Instances** and click **New**. Fill in:

| Field | Required | Description |
| --- | --- | --- |
| **Name** | Yes | Descriptive instance name (e.g., "US Seller Account") |
| **Marketplace Region** | Yes | North America, Europe, or Far East |
| **Marketplaces** | Yes | Select active marketplaces (e.g., US, CA, MX) |
| **SP-API Refresh Token** | Yes | From your Amazon developer console |
| **Client ID** | Yes | LWA client ID from Amazon |
| **Client Secret** | Yes | LWA client secret |
| **AWS Access Key** | Yes | IAM access key for SP-API |
| **AWS Secret Key** | Yes | IAM secret key for SP-API |
| **Company** | Yes | Odoo company for this instance |

<a id="step-2-test-connection"></a>

### Step 2. Test Connection

Click **Test Connection** on the instance form to verify your API credentials are working. You should see a green confirmation badge.

<a id="step-3-import-products"></a>

### Step 3. Import Products

Navigate to **Catalog > Import / Map Products** to bulk-map or import your Amazon SKUs via CSV or Excel file. Supports 4 operations:

- **Map** - Link existing Odoo products to Amazon SKUs
- **Import** - Create new Odoo products from Amazon catalog
- **Update Prices** - Bulk update prices
- **Update Stock** - Bulk update inventory

<a id="step-4-sync-orders"></a>

### Step 4. Sync Orders

Click **Import Orders** on the instance form, or let the scheduled action run automatically every 15–30 minutes.

<a id="step-5-enable-ai-optional"></a>

### Step 5. Enable AI (Optional)

In **Configuration > Settings**, enable AI features and select your preferred AI provider (OpenAI, Claude, Gemini, or Groq). See the [AI Features guide](../../../ai-features/18.0/ai-features/overview.md) for details.

<a id="step-6-set-up-warehouses"></a>

### Step 6. Set Up Warehouses

tip

Configure **separate warehouses for FBA and FBM stock** to keep inventory movements clean and prevent stock counting errors between fulfillment channels.

<a id="step-7-enable-automation"></a>

### Step 7. Enable Automation

Review the 15 scheduled actions on your instance and enable the ones you need. See [Automation & Scheduling](../../../core-features/18.0/features/automation.md) for the complete list.

<a id="security-notes"></a>

## Security Notes

warning

Never commit SP-API credentials or AWS keys to version control. Store them securely in the Odoo instance form which encrypts sensitive fields at rest.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Amazon Connector - Installation and Setup](https://docs.sdlccorp.com/docs/18.0/amazon-odoo-connector/getting-started/setup/)
