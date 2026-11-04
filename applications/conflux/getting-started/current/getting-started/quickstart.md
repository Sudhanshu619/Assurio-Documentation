# Quick start

Sign in, see what your role lets you do, and take a ten-minute tour of the console.

<a id="sign-in"></a>

## Sign in

Open your organization's Conflux console and sign in with your email and password. Accounts are usually invited by an administrator from [Administration → Users](../../../the-console-page-by-page/current/console/admin.md#users). If your organization allows open registration, you can also [create an account](../../../the-console-page-by-page/current/console/auth.md#register) yourself.

Forgotten your password? Use the reset link on the sign-in screen - see [Signing in](../../../the-console-page-by-page/current/console/auth.md) for the full flow.

<a id="roles"></a>

## What you see depends on your role

Conflux has eight roles, and the console only shows the pages your role can use. Ask your administrator which role you hold.

| Role | What you will see |
| --- | --- |
| Super Admin | Everything, across all tenants |
| Organization Administrator | Everything inside one tenant |
| API Developer | Proxies, policies, products; non-prod deploys |
| Operations Engineer | Deployments, fleet, alerts, incidents |
| Security Administrator | Policies, credentials, approvals, audit |
| Business Analyst | Analytics, SLA, monetization - read-mostly |
| Auditor | Read-only compliance view |
| API Consumer | The developer portal only |

The full breakdown of what each role can and cannot do is in [Roles & permissions](roles.md).

Two products in one console

An administrator and an API consumer use the same application but see two different products - the operator sees a control plane, the consumer sees a catalog and their own keys.

<a id="tour"></a>

## The ten-minute tour

Sign in as an Organization Administrator and walk these seven stops. They follow the journey an API takes, so by the end the navigation will make sense on its own.

1. **Dashboard - get your bearings**
   Traffic, error rate, fleet health and everything waiting on a decision. Note the four “needs attention” cards: open incidents, pending approvals, subscription requests and recent deployments. This screen never computes a number the underlying page disagrees with - every tile is a link to where the number came from.
2. **API Proxies → open a proxy**
   Seven tabs: Overview, Routes, Policies, Deployments, Revisions, Governance, Specification. Open **Policies** - this is the request/response pipeline as the gateway actually executes it, with the backend target drawn as a divider between the request half and the response half.
3. **Deployments - see how revisions roll out**
   The environment matrix shows which revision serves which environment. During a canary release, traffic is split across two revisions. The traffic-shift editor refuses to save unless the weights total exactly 100.
4. **API Products → Subscriptions**
   A product is what a consumer actually subscribes to - one or more proxies bundled with a quota and an approval rule. The Subscriptions queue holds pending access requests; approving one activates that app’s credentials against the product.
5. **Govern → Lifecycle, then Approvals**
   The board lays every API out by stage. Stages marked with a gate need a second person: try approving a request you filed yourself and Conflux will refuse it.
6. **Operate → Incidents**
   Open one. Acknowledge → investigate → monitor → resolve, each step appending to a timeline that is never rewritten. Alerts are what opened it; the SLA page is what it cost you in error budget.
7. **Audit trail**
   Everything you just did is here, with actor, IP, entity and a before/after diff. Nothing in Conflux can edit or delete a row on this page - there is no endpoint for it.

Next: [Core concepts](concepts.md) if the words **proxy**, **product** and **app** do not yet mean three different things to you.

---

Source: [Quick start](https://docs.sdlccorp.com/docs/conflux/getting-started/quickstart/)
