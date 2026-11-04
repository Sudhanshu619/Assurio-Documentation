# Folio & Billing

Every reservation automatically generates a **guest folio** - an itemized record of all charges including room rates, services, taxes, and payments.

<a id="whats-a-folio"></a>

## What's a Folio?

A folio is the complete financial record of a guest's stay:

- Room charges (per night × nights)
- Extra services (laundry, spa, transport)
- Food and beverage charges
- Minibar consumption
- Taxes and fees
- Payments received
- Balance due / refunds

<a id="folio-form"></a>

## Folio Form

![Folio Form](https://docs.sdlccorp.com/assets/images/19_folio_form-9466cb87d16fd673789af1bb6251379c.webp)

<a id="key-sections"></a>

### Key Sections

| Section | What's Tracked |
| --- | --- |
| **Guest & Reservation** | Linked guest and reservation details |
| **Charge Lines** | Each billable item with date, description, amount |
| **Payments** | All payments received (cash, card, bank transfer) |
| **Taxes** | Applied tax rules per line |
| **Totals** | Subtotal, tax, total, paid, balance |
| **Notes** | Internal notes and comments |

<a id="charge-types"></a>

### Charge Types

- **Room** - Auto-generated per night
- **Service** - Laundry, spa, transport, custom services
- **Restaurant** - Food orders from hotel restaurant
- **Minibar** - Items consumed from room minibar
- **Extra** - Miscellaneous charges (phone, parking, etc.)
- **Tax** - VAT / GST / service tax

<a id="auto-charge-generation"></a>

## Auto-Charge Generation

The system automatically posts charges to the folio:

- **Room charges** - Posted daily at midnight (configurable via cron)
- **Services** - When service is completed/delivered
- **Restaurant** - When KOT (Kitchen Order Ticket) is closed
- **Minibar** - Manually or via minibar wizard at checkout

<a id="processing-payments"></a>

## Processing Payments

<a id="during-stay"></a>

### During Stay

Record payments anytime:

1. Open the folio
2. Click **Register Payment**
3. Enter amount and payment method
4. Payment is added to the Payments tab
5. Folio balance updates

<a id="at-check-out"></a>

### At Check-Out

The Check-Out Wizard automatically:

1. Reviews all charges
2. Calculates final total with tax
3. Prompts for remaining balance
4. Processes payment
5. Generates invoice

<a id="generating-invoices"></a>

## Generating Invoices

Each folio produces an invoice for the guest.

![Folio Invoice](https://docs.sdlccorp.com/assets/images/20_folio_invoice-284fc7b370f534ddc49ed132490cf388.webp)

<a id="invoice-features"></a>

### Invoice Features

- Itemized charges with dates
- Tax breakdown (VAT, service tax, etc.)
- Payment history
- Company letterhead
- QR code for digital payments (optional)
- Multi-currency support

<a id="export-options"></a>

### Export Options

- **PDF** - Printable invoice
- **Email** - Send directly to guest
- **Account Move** - Posted to Odoo accounting for reconciliation

<a id="integration-with-odoo-accounting"></a>

## Integration with Odoo Accounting

Folios integrate fully with Odoo's accounting module:

- Revenue recognition per day (for accrual accounting)
- Tax posting to appropriate accounts
- Payment reconciliation with bank statements
- Analytic accounts per property for revenue tracking

<a id="split-folios"></a>

## Split Folios

For group bookings or corporate stays, you can split folios:

- Separate folios per occupant
- Group master folio + individual folios
- Company-paid vs guest-paid charges

tip

Configure default tax rules in **Configuration > Settings** so charges automatically apply the correct tax rates based on property location.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Folio & Billing](https://docs.sdlccorp.com/docs/hotel-management/reservations/folio-billing/)
