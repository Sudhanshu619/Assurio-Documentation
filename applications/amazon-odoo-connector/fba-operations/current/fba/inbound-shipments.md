# FBA Inbound Shipments (v2024 API)

Create and manage FBA inbound shipment plans using Amazon's latest **v2024 Fulfillment Inbound API**.

<a id="features"></a>

## Features

- Create inbound shipment plans directly from Odoo
- Support for **Partnered** (Amazon-partnered) or **Non-partnered** carriers
- Download shipping labels directly from Amazon
- Track discrepancies between shipped and received quantities
- Linked to Odoo delivery orders (`stock.picking`) for warehouse management

<a id="shipment-status-flow"></a>

## Shipment Status Flow

Shipments progress through these statuses:

```
Draft → Planning → Submitted → Shipped → In Transit → Receiving → Closed
```

| Status | Meaning |
| --- | --- |
| **Draft** | Being created, not yet submitted |
| **Planning** | Submitted to Amazon, awaiting plan approval |
| **Submitted** | Plan approved, awaiting shipment |
| **Shipped** | Carrier has picked up |
| **In Transit** | Moving to fulfillment center |
| **Receiving** | Amazon is processing receipt |
| **Closed** | Fully received, quantities reconciled |

<a id="carrier-options"></a>

## Carrier Options

<a id="partnered-carrier"></a>

### Partnered Carrier

Use Amazon's partnered carriers (UPS, FedEx) with negotiated rates:

- Discounted shipping rates
- Automatic label generation
- Direct tracking integration

<a id="non-partnered-carrier"></a>

### Non-Partnered Carrier

Use your own carrier or freight forwarder:

- Manual tracking number entry
- Upload your own shipping labels
- Flexible routing

<a id="creating-an-inbound-shipment"></a>

## Creating an Inbound Shipment

1. Go to **FBA > Inbound Shipments** and click **New**
2. Select the source warehouse (Odoo)
3. Select the destination Amazon fulfillment center
4. Add products and quantities
5. Click **Submit Plan** to send to Amazon
6. Once approved, select carrier and print labels
7. Ship and track

<a id="discrepancy-tracking"></a>

## Discrepancy Tracking

When Amazon receives your shipment, the connector automatically compares:

- **Shipped Qty** (what you sent)
- **Received Qty** (what Amazon confirmed)
- **Variance** (difference for reporting)

Discrepancies appear in the shipment record for investigation and potential reimbursement claims.

tip

Link inbound shipments to Odoo delivery orders (`stock.picking`) for complete warehouse tracking. This creates a full audit trail from your warehouse to Amazon's fulfillment center.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [FBA Inbound Shipments (v2024 API)](https://docs.sdlccorp.com/docs/amazon-odoo-connector/fba/inbound-shipments/)
