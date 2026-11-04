# Auto Workflow


<a id="when-auto-workflow-is-the-right-fit"></a>

## When auto-workflow is the right fit

Auto-workflow is hands-off order processing - quote → confirmed → invoiced → paid happens automatically based on rules you set once. It's the right fit when:

- Your Shopify orders are reliably paid before fulfilment (the typical e-commerce case).
- You want zero manual steps between order import and warehouse pick.
- You're comfortable handling exceptions in Odoo rather than gating every order on a person.

If your business model is mostly post-pay (B2B with net terms, customised quotes), leave auto-workflow off and progress orders manually.

<a id="overview"></a>

## Overview

Auto-workflow is the connector's hands-off mode for processing imported Shopify orders. With it configured, each new order automatically progresses through Odoo's quote → confirmed → invoiced → paid steps using rules you set once.

<a id="use-auto-workflow-when"></a>

### Use auto-workflow when…

- Your Shopify orders are reliably paid before fulfilment (the typical e-commerce case).
- You want zero manual steps between order import and warehouse pick.
- You're comfortable handling exceptions in Odoo rather than blocking every order on a person.

Auto Workflow automates the full order processing pipeline.

<a id="workflow-configuration"></a>

## Workflow Configuration

Navigate to **Shopify → Configuration → Auto Workflow**:

| Setting | Description |
| --- | --- |
| **Confirm Sales Order** | Automatically confirm the SO |
| **Create Invoice** | Create invoice after confirmation |
| **Validate Invoice** | Automatically validate the invoice |
| **Register Payment** | Auto-register payment from Shopify |
| **Create Delivery** | Create delivery order |
| **Validate Delivery** | Auto-validate the delivery |

<a id="payment-journal-mapping"></a>

## Payment Journal Mapping

Map Shopify payment gateways to Odoo accounting journals in
**Shopify → Configuration → Payment Gateway Mapping**.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Auto Workflow](https://docs.sdlccorp.com/docs/17.0/shopify-odoo-connector/configuration/auto-workflow/)
