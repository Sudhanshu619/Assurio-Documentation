# Monetize

Rate plans, subscribers, billing runs and the revenue dashboard - for when the APIs are the product.

<a id="model"></a>

## How billing works here

Monetization sits on top of everything else rather than beside it: a rate plan attaches to an API product, a developer subscribes to the plan, and a billing run prices the traffic that the same analytics aggregate already recorded.

1. **Rate plan** - Commercial terms attached to a product.
2. **Publish it** - Draft plans cannot take subscribers.
3. **Subscriber** - A developer is placed on the plan.
4. **Traffic** - Metered by the same hourly aggregate.
5. **Billing run** - Prices the period, writes invoices.

One source of truth for usage

Billing measures the same traffic table the dashboards read. An invoice and the Traffic screen cannot disagree about how many calls a partner made - which is exactly the argument you want to be able to make in a billing dispute.

<a id="rate-plans"></a>

## Rate plans

**Route:** `/monetization/rate-plans` · **Sidebar:** Monetize › Rate Plans · **Needs:** `monetization.view`

Commercial terms attached to an API product. A developer subscribes to a published plan, and metered usage is priced against it.

**What you see**

- Each plan: type, currency, billing period, setup fee, recurring fee, included allowance and per-call rate
- Volume tiers where the plan is banded
- Status - draft, published or deprecated
- A subscribers tab listing who is on each plan, with prepaid balances

**What you can do**

- Create a plan and attach it to a product
- Publish it, or deprecate it when it is superseded
- Put a developer on a plan
- Top up a prepaid balance
- Cancel a subscriber

**Good to know:** Deprecating a plan keeps existing subscribers on it while stopping new ones - the standard way to retire pricing without repricing everyone mid-contract.

<a id="the-five-plan-types"></a>

### The five plan types

| Type | Charges | Fits |
| --- | --- | --- |
| Free | Nothing. | Evaluation and sandbox tiers |
| Flat rate | One recurring fee covering the whole quota. | Predictable enterprise contracts |
| Pay as you go | An included allowance, then a per-call rate. | Self-service growth |
| Tiered | Volume bands that get cheaper as usage grows. | Rewarding scale; walked band by band at billing time |
| Revenue share | A percentage of the value processed. | Payment and marketplace APIs |

| Billing model | How money moves |
| --- | --- |
| Postpaid | Usage is metered and invoiced in arrears at the end of the period. |
| Prepaid | The subscriber holds a balance that each billing run draws down. Top it up from the subscribers tab. |

<a id="billing"></a>

## Billing

**Route:** `/monetization/billing` · **Sidebar:** Monetize › Billing · **Needs:** `billing.view`, `monetization.view`

What has been billed, collected and is still outstanding across every monetized API product.

**What you see**

- Billed, collected, outstanding and revenue-share totals
- A monthly revenue trend and the top developers by revenue
- Every invoice with its developer, plan, period, call volume, billable calls and status
- Status filters: draft, issued, paid and overdue

**What you can do**

- Run a billing period - measures real traffic, prices it against each plan and writes invoices with line items (needs `rateplan.manage`)
- Open an invoice to read its line items
- Mark an invoice paid

**Good to know:** A billing run is deterministic: re-running the same period against the same traffic produces the same invoice. It reads the aggregate; it does not sample live calls.

<a id="what-lands-on-an-invoice"></a>

### What lands on an invoice

For each subscription in the period: the calls observed, how many of those were **billable** after the included allowance, the rate applied - walking volume bands where the plan is tiered - plus any setup and recurring fees, and any prepaid balance drawn down.

Where consumers see this

Published plans render as pricing cards on the product’s `/portal/:slug` page, so a partner can read the terms before subscribing rather than after their first invoice.

---

Source: [Monetize](https://docs.sdlccorp.com/docs/conflux/console/monetize/)
