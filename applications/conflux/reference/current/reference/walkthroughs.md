# Walkthroughs

Six end-to-end jobs, click by click: publish an API, run a canary, onboard a partner, handle an incident, bill for usage, investigate a change.

<a id="publish"></a>

## Publish an API from nothing

The full path from an empty screen to a partner making a call. Sign in as an Organization Administrator - the developer role can do most of this, but not the production deploy at step 8.

1. **Register the backend**
   [Target Servers](../../../the-console-page-by-page/current/console/gateway.md#targets) → new. Name it `orders-service`, give it a host, port and environment. Repeat for each environment - same name, different host. That repetition is the whole trick.
2. **Create the proxy**
   [API Proxies](../../../the-console-page-by-page/current/console/gateway.md#proxies) → new. Base path `/v1/orders`, protocol REST, auth scheme API key. Version the base path now; retrofitting a version segment later breaks every consumer.
3. **Add routes**
   Routes tab → add. `GET /orders`, `GET /orders/{id}`, `POST /orders`. Point each at `orders-service` and set a timeout.
4. **Attach policies**
   Policies tab. On **proxy request**: Verify API Key, then Quota, then Spike Arrest - in that order, because the quota needs to know whose key it is. On **proxy response**: Data Masking if any field is sensitive.
5. **Generate and publish the spec**
   Specification tab → generate from routes, edit the summaries, publish. This satisfies governance standard DOC-001 and is what consumers will actually read.
6. **Check governance, then request review**
   Governance tab → re-evaluate. Clear anything blocking - SEC-001 and SEC-002 will stop you otherwise. Then request the move to **review**, and on to **approved**.
7. **Someone else approves**
   Sign in as a second user with `lifecycle.approve` - `security@` will do - and approve it from [Approvals](../../../the-console-page-by-page/current/console/govern.md#approvals). You cannot approve your own request; that is deliberate.
8. **Deploy**
   Deployments tab → deploy the current revision to staging (direct), watch it, then to production. Production needs `deployment.prod` and the approved stage you just earned.
9. **Bundle it into a product**
   [API Products](../../../the-console-page-by-page/current/console/publish.md#products) → new. Add the proxy, set a quota, choose public access and whether subscriptions auto-approve. Publish it.
10. **Check the consumer’s view**
    Sign in with an API Consumer account and open the portal. Your product is in the catalog with its spec and pricing. Register an app, subscribe, and the key works.

<a id="canary"></a>

## Ship a risky change with a canary

You have changed a policy or a route on an API that is already live. The goal is production evidence before full exposure.

1. **Make the change**
   Edit the proxy. Because it is deployed, saving cuts a **new revision** rather than mutating what is serving traffic.
2. **Deploy as canary**
   Deployments → deploy the new revision to production with strategy **canary**. Give it 10%.
3. **Watch the right two numbers**
   Error rate and p95 latency for that proxy on [Errors & faults](../../../the-console-page-by-page/current/console/overview.md#errors). Give it enough traffic to mean something - minutes, not seconds.
4. **Ramp**
   Traffic-shift editor: 10 → 25 → 50 → 100. The editor refuses any split that does not total exactly 100.
5. **Or roll back**
   One click restores the previous revision at full weight and records what it was rolled back from. No re-deploy, no rebuild.

Set the alert before you ramp, not after

An alert rule scoped to that proxy and environment - error rate above 2% for 5 minutes - turns the canary into something that pages you rather than something you have to sit and watch.

<a id="partner"></a>

## Onboard a partner

Two routes to the same place, depending on whether you want self-service.

| Self-service | Hands-on |
| --- | --- |
| The partner registers on the portal, creates an app, requests a subscription. You approve it from the [Subscriptions](../../../the-console-page-by-page/current/console/publish.md#subscriptions) queue - or set the product to auto-approve and never touch it. | You create the developer from [Developers](../../../the-console-page-by-page/current/console/publish.md#developers), register an app on their behalf, issue the credential and send it to them through whatever channel your security policy allows. |

1. **Decide the product, not the proxy**
   Which bundle should they get, at which quota? If none fits, create a product with a partner-tier quota rather than overriding on the subscription.
2. **Approve with an override if needed**
   The approval dialog takes a quota override, so one partner can sit above the product default without a separate product.
3. **Hand over the credential**
   The secret is shown exactly once, at issue time. If it is lost, rotate - do not go looking for it.
4. **Watch their first week**
   [Consumers](../../../the-console-page-by-page/current/console/overview.md#consumers) shows their volume, error rate and latency. A partner’s first week is almost always 4xx-heavy; that is a documentation problem, not an outage.
5. **If they need cutting off**
   Revoke the subscription to stop one product, revoke the credential to stop one app, or suspend the developer to stop everything they own at once.

<a id="incident"></a>

## Handle an incident

An alert has fired. Sign in as an Operations Engineer.

1. **Acknowledge**
   Open it from [Incidents](../../../the-console-page-by-page/current/console/operate.md#incidents) and acknowledge. Ownership is now unambiguous, which matters more in the first five minutes than any diagnosis.
2. **Establish the blast radius**
   The incident names the metric, the measured value and the affected API. [Errors & faults](../../../the-console-page-by-page/current/console/overview.md#errors) tells you whether it is 5xx (your backend), 4xx (a caller) or policy blocks (a quota someone just hit).
3. **Check what changed**
   The dashboard’s recent-deployments card, or the [Audit trail](../../../the-console-page-by-page/current/console/govern.md#audit) filtered to the deployment category. Most incidents are a change with a delay attached.
4. **Check the fleet**
   [Gateway fleet](../../../the-console-page-by-page/current/console/operate.md#gateways) - a degraded or offline node explains a partial failure that no configuration change accounts for.
5. **Act**
   Roll back the deployment, drain the node, or raise the quota. Each action leaves its own audit entry, so the timeline reconstructs itself.
6. **Monitor, then resolve**
   Move to monitoring while you watch it hold, then resolve with a summary. Check the error budget on [SLA targets](../../../the-console-page-by-page/current/console/operate.md#sla) - that is what this cost you.

<a id="billing"></a>

## Charge for an API

1. **Create the plan**
   [Rate Plans](../../../the-console-page-by-page/current/console/monetize.md#rate-plans) → new. Attach it to the product, pick a type - pay-as-you-go is the usual starting point - and set the included allowance and per-call rate.
2. **Publish it**
   A draft plan cannot take subscribers. Publishing also makes it render as a pricing card on the portal product page.
3. **Put developers on it**
   Subscribers tab → add. For a prepaid plan, top up their balance at the same time.
4. **Let it run**
   Usage is metered by the same hourly traffic aggregate the dashboards read. There is nothing to switch on.
5. **Run the period**
   [Billing](../../../the-console-page-by-page/current/console/monetize.md#billing) → run a billing period. It prices each subscription’s real traffic against its plan and writes an invoice with line items.
6. **Follow the money**
   Billed, collected and outstanding, with a monthly trend and top developers by revenue. Mark invoices paid as they settle.

<a id="investigate"></a>

## Answer “who changed this, and when?”

The question an auditor asks, and the one you ask yourself at 2am. Sign in as an Auditor to see the read-only version of this.

1. **Start from the entity**
   The [Audit trail](../../../the-console-page-by-page/current/console/govern.md#audit) filters by entity type and entity id, so you can pull every event that ever touched one proxy.
2. **Narrow by category**
   Configuration for edits, deployment for releases, security for credential events, governance for lifecycle decisions.
3. **Read the diff**
   Configuration changes carry a before/after. You are looking at what the value actually was, not at someone’s recollection.
4. **Cross-check the approval**
   The lifecycle transition records the requester and the approver separately - and they can never be the same person.
5. **Export it**
   CSV export for the filtered set, with `audit.export`. The export is itself audited, which is the point.

Nothing here can be tidied up afterwards

The audit table has no update path and no delete path - not for an administrator, not for a super admin, not through any endpoint. That is what makes the answer worth having.

---

Source: [Walkthroughs](https://docs.sdlccorp.com/docs/conflux/reference/walkthroughs/)
