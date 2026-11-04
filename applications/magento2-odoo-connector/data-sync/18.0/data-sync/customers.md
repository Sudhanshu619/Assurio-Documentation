# Magento 2 Connector - Customer Management

The Magento 2 Connector synchronizes customer data bidirectionally between Odoo and Magento. Customer records, including names, contact details, and addresses, are kept in sync across both platforms.

<a id="accessing-magento-customers"></a>

## Accessing Magento Customers

Navigate to **Magento > Magento Data > Customers** to view all synced customer records.

![Magento Data menu showing Customers option](https://docs.sdlccorp.com/assets/images/mc-1-dd2a751af45c39b323ab5e04d081cd59.webp)

<a id="customer-list-view"></a>

## Customer List View

The customer list provides an overview of all synchronized customers:

![Magento Customers list view](https://docs.sdlccorp.com/assets/images/mc-11-b29c1b77ac13108f8091046b3e2ab3d8.webp)

| Column | Description |
| --- | --- |
| **Magento ID** | The customer ID in Magento |
| **Instance** | The Magento instance this customer belongs to |
| **Name** | Customer full name |
| **Email** | Customer email address |
| **Phone** | Customer phone number |
| **City** | Customer city |
| **State/Province** | Customer state or province |

<a id="customer-form-fields"></a>

## Customer Form Fields

Click on a customer record to view or edit the full details:

![Magento Customer form view](https://docs.sdlccorp.com/assets/images/mc-111-808f2387c241a63e7c9e7b9a30f28f45.webp)

| Field | Description |
| --- | --- |
| **Instance** | The Magento instance connection |
| **Name** | Full customer name |
| **Magento ID** | The Magento customer ID (auto-populated on sync) |
| **Name Prefix** | Customer name prefix (Mr., Mrs., etc.) |
| **Firstname** | Customer first name |
| **Middle Name/Initial** | Customer middle name or initial |
| **Lastname** | Customer last name |
| **Name Suffix** | Customer name suffix (Jr., Sr., etc.) |
| **Email** | Customer email address |
| **Phone** | Customer phone number |
| **VAT Number** | Customer VAT/Tax identification number |
| **Send Welcome Email** | Whether to send a welcome email (Yes/No) |
| **Default Billing Address** | Default billing address (Yes/No) |
| **Default Shipping Address** | Default shipping address (Yes/No) |
| **Company** | Customer company name |
| **Street** | Street address |
| **City** | City |

<a id="customer-actions"></a>

## Customer Actions

The customer form provides three primary action buttons:

| Button | Description |
| --- | --- |
| **Create in Magento** | Push a new customer record from Odoo to Magento |
| **Update in Magento** | Push updated customer data from Odoo to Magento |
| **Pull from Magento** | Refresh the customer record with the latest data from Magento |

Default Password

When creating a customer in Magento from Odoo, the system assigns a default password. Ensure you communicate password reset instructions to the customer, or configure Magento to send a welcome email with a password setup link by setting **Send Welcome Email** to `Yes`.

<a id="syncing-customers"></a>

## Syncing Customers

<a id="pull-customers-from-magento"></a>

### Pull Customers from Magento

1. Go to **Magento > Instances**.
2. Open your instance.
3. Click **Sync Customers**.
4. All customer records from Magento will be imported into Odoo.

<a id="push-a-customer-to-magento"></a>

### Push a Customer to Magento

1. Navigate to **Magento > Magento Data > Customers**.
2. Click **New**.
3. Select the **Instance**.
4. Fill in all required fields.
5. Click **Create in Magento**.

info

Customers synced from Magento are automatically linked to Odoo `res.partner` records. If a matching partner already exists (by email), the connector links to the existing record instead of creating a duplicate.

<a id="next-steps"></a>

## Next Steps

- [Manage Categories](categories.md)
- [Configure Customer Field Mapping](../../../advanced/18.0/advanced/field-mapping.md)
- [View Sync Reports](../../../reference/18.0/reference/sync-reports.md)

---

Source: [Magento 2 Connector - Customer Management](https://docs.sdlccorp.com/docs/18.0/magento2-odoo-connector/data-sync/customers/)
