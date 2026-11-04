# FAQ & troubleshooting

The questions that come up in the first hour, and what to do when a screen is empty or a button is missing.

<a id="first-hour"></a>

## Questions from the first hour

Short answers, each with a link to the longer one.

| Question | Answer |
| --- | --- |
| Does Conflux carry my API traffic? | No. Conflux is the **control plane** - it stores, governs and reports on gateway configuration. Your gateway fleet executes that configuration and carries the live traffic. See [Control plane, not data plane](../../../overview/current/intro.md#control-plane). |
| Why can’t consumers subscribe to a proxy? | They subscribe to a **product**, which bundles one or more proxies with a quota and an access rule. One proxy can sit in several products at different quotas. |
| I edited a deployed proxy - did I just change production? | No. Editing a deployed proxy cuts a new revision. Production keeps serving the revision it was given until you deploy the new one. |
| Where is my consumer secret? | Shown exactly once, at issue time. It is stripped from every list response by design. If it is lost, rotate the credential rather than hunting for it. |
| Why can’t I approve my own request? | Two-person approval is enforced on the server regardless of permissions. Ask a second holder of `lifecycle.approve`. |

<a id="missing"></a>

## A page or button I expected is missing

Almost always a permission, and almost always working as intended. The navigation is built by the server from your grants, so a missing link means the role does not hold the code.

| Symptom | Cause | Fix |
| --- | --- | --- |
| A whole nav section is absent | No item inside it survived the permission filter. | Grant the relevant view code from [Roles & permissions](../../../the-console-page-by-page/current/console/admin.md#roles). |
| The page loads but every action button is gone | You hold the view code but not the write codes. | Expected for the Auditor and Analyst roles - they are read-mostly by design. |
| I typed the URL and got Access denied | The route guard checked your grants before rendering. | Same fix; the API would have refused it anyway. |
| Deploy is refused on production only | Missing `deployment.prod`, or the proxy is not approved. | See [the production gate](../../../getting-started/current/getting-started/concepts.md#where). |
| A lifecycle move is refused before I can request it | A blocking governance standard is failing. | Fix or waive it on the proxy’s Governance tab, then request again. |

<a id="empty"></a>

## The dashboard loads but every chart is empty

If you are looking at a time window with no traffic - or filtered to an API with no traffic - the charts are honestly empty. Widen the range to 7 or 14 days and clear the API filter.

<a id="scope"></a>

## What Conflux manages, and what your gateway runs

Conflux is the control plane. A few things people expect from an API platform are properties of the running gateway deployment rather than of the console:

| Area | Where it lives |
| --- | --- |
| Executing requests - terminating TLS and running the policy chain | Your gateway fleet (the data plane). Conflux stores, governs and reports on its configuration, and the Gateway fleet page models and monitors those nodes. |
| Availability, multi-region, zero-downtime upgrades and disaster recovery | How the gateway fleet is deployed. Conflux models and measures them: deployment models, regions, node health, SLA targets and error budgets. |

Distributed tracing

The tracing policy is configurable end to end - trace context propagation and an OTLP, Jaeger, Zipkin or Datadog exporter - but the spans it describes are emitted by the data plane at runtime, not by the console.

<a id="more"></a>

## Where else to look

| For | Go to |
| --- | --- |
| Exact request and response shapes | The API reference - see [Architecture & API](architecture.md#swagger). Every operation shows its required permission. |
| How a specific screen works | [The console, page by page](../../../the-console-page-by-page/current/console/overview.md) |
| A job you need to complete | [Walkthroughs](walkthroughs.md) |
| Anything else | [Contact SDLC Corp support](https://sdlccorp.com/contact-us/) |

---

Source: [FAQ & troubleshooting](https://docs.sdlccorp.com/docs/conflux/reference/faq/)
