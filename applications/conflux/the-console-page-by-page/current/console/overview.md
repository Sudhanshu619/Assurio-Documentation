# Overview & Analytics

The dashboard both roles land on, and the five analytics screens behind it.

<a id="dashboard"></a>

## Dashboard

The landing screen, and the only page in the console that changes shape entirely depending on who you are. Operators get a control plane; consumers get their own workspace.

<a id="control-plane-operators"></a>

### Control plane (operators)

**Route:** `/dashboard` · **Sidebar:** Overview › Dashboard · **Needs:** `dashboard.view`

Traffic, health and everything waiting on a decision, across the whole API estate.

**What you see**

- Four headline metrics: requests, error rate, average latency, availability - each with a period-over-period trend
- A six-tile count strip: proxies, products, deployments, developers, apps, policies
- Traffic against failures over time, bucketed automatically by the selected window
- Gateway fleet health as a gauge, with node counts and total requests per second
- Busiest APIs and top consumers, by volume
- Lifecycle distribution and the org-wide governance compliance score
- Four attention queues: open incidents, pending approvals, subscription requests, recent deployments
- The ten most recent audit entries

**What you can do**

- Switch the time range (24 hours to 30 days)
- Jump to the page any number came from - every tile is a link
- Open an incident, approval or subscription request directly from its queue

**Good to know:** Nothing here is computed independently: every figure is the same query the underlying module runs, so the dashboard can never disagree with the page it links to.

<a id="my-workspace-consumers"></a>

### My workspace (consumers)

**Route:** `/dashboard` · **Sidebar:** Overview › Dashboard · **Needs:** `dashboard.view`

The same route, rendered for a portal user: their apps, credentials and usage rather than the tenant’s control plane.

**What you see**

- Counts of apps, active subscriptions and requests awaiting approval
- Each app with its credential status and the products it may call
- Their own request volume, success rate and quota consumption for the period

**What you can do**

- Register an app
- Browse the API catalog
- Open an app to manage its keys

**Good to know:** The switch is by capability, not by role name: if you hold none of `proxy.view`, `deployment.view` or `monitoring.view`, you get the consumer view.

<a id="analytics-model"></a>

## How analytics is measured

All five analytics screens read one pre-aggregated fact table: a row per hour, per proxy, environment, app, product and country of origin. That has three consequences worth knowing before you read any chart.

| Consequence | What it means for you |
| --- | --- |
| Speed is independent of traffic volume | Every dashboard is a handful of grouped scans. A tenant doing a billion calls loads as fast as one doing a thousand. |
| The smallest bucket is an hour | Bucketing is chosen from the window you select - hourly, daily or weekly. A five-minute spike is visible inside its hour, not as its own point. |
| Percentiles are the worst observed, not an average | A true p95 cannot be reconstructed by averaging per-bucket p95s. The aggregate reports the worst p95 and p99 in the window - which is also the figure an SLA is judged on. |

Every screen shares the same filter bar - time range, API, environment - and every one can export the underlying rows as CSV with `analytics.export`.

<a id="traffic"></a>

## Traffic & latency

**Route:** `/analytics/traffic` · **Sidebar:** Overview › Analytics › Traffic & Latency · **Needs:** `analytics.view`

Request volume, response time and cache effectiveness across the API estate.

**What you see**

- Requests, success rate, average latency, p95 (with p99), cache hit rate and data transferred
- Total calls against failures over time
- Total vs backend latency - the gap between the two lines is gateway overhead
- Traffic split by environment, by busiest API and by API product
- AI token consumption: prompt and completion tokens metered by the LLM policies

**What you can do**

- Filter by time range, API and environment
- Export the rows behind the view as CSV

**Good to know:** The AI panel is billed on tokens, not calls - which is why it is reported separately from request volume. See [the AI gateway policies](../../../reference/current/reference/policies.md#ai-gateway).

<a id="errors"></a>

## Errors & faults

**Route:** `/analytics/errors` · **Sidebar:** Overview › Analytics › Errors & Faults · **Needs:** `analytics.view`

Where calls are failing, whether it is the caller or the backend, and which APIs are worst affected.

**What you see**

- Requests, error rate, 4xx count, 5xx count and policy blocks
- Failures over time against total volume
- A failure-mix breakdown: client fault, server fault, or refused by policy
- Worst-affected APIs ranked by error rate

**What you can do**

- Filter by range and API
- Export as CSV

**Good to know:** The ranking is by **rate**, not count, on purpose - otherwise a small API failing completely stays buried under a large one failing slightly.

<a id="reading-the-three-failure-classes"></a>

### Reading the three failure classes

| Class | Means | Usually fixed by |
| --- | --- | --- |
| 4xx client | The caller sent something wrong - bad payload, missing field, unknown path. | Better documentation, or a stricter published spec |
| 5xx server | Your backend failed or timed out. The gateway forwarded it faithfully. | The service team - or a circuit breaker / retry policy |
| Policy block | The call never reached your backend: invalid key, exhausted quota, threat rule. | A quota change, or telling the consumer why |

<a id="consumers"></a>

## Consumers

**Route:** `/analytics/consumers` · **Sidebar:** Overview › Analytics › Consumers · **Needs:** `analytics.view`

Which apps and partners are driving traffic, and how concentrated your usage is across them.

**What you see**

- Active apps with traffic in range, total requests, top-consumer share and products in use
- Top consumers by volume, with their error rate and latency
- Traffic split by the product the calls arrive through

**What you can do**

- Filter by range
- Export as CSV

**Good to know:** Top-consumer share is a concentration risk indicator. One app at 80% of volume means your capacity planning and your commercial exposure both hang on a single partner.

<a id="geography"></a>

## Geography

**Route:** `/analytics/geography` · **Sidebar:** Overview › Analytics › Geography · **Needs:** `analytics.view`

Where calls originate and which gateway region serves them - the input to a data-residency or edge-placement decision.

**What you see**

- Country count, serving-region count, top country and total requests
- Traffic by country of origin with latency and availability per country
- Traffic by serving region - which gateway cluster handled the call

**What you can do**

- Filter by range
- Export as CSV

**Good to know:** A large gap between a country’s share of traffic and its latency is the usual signal that traffic is crossing an ocean to reach a gateway - an argument for another region, or for a geographic routing policy.

<a id="reports"></a>

## Reports

**Route:** `/analytics/reports` · **Sidebar:** Overview › Analytics › Reports · **Needs:** `report.view`, `report.manage`

Saved analytics queries, run on demand or delivered on a schedule.

**What you see**

- Saved reports with their type, schedule, recipients and last run
- Counts of saved and scheduled reports, and the report types available
- A result panel with the generated rows after a run

**What you can do**

- Create a report: name, type, filters, bucket interval, format
- Preview it before saving
- Run one on demand
- Schedule it daily, weekly or monthly to a list of recipients

**Good to know:** Reports run the same queries the live dashboards use - so a scheduled Monday report and the screen someone opens on Monday cannot disagree.

<a id="the-nine-report-types"></a>

### The nine report types

| Type | Answers |
| --- | --- |
| traffic | Volume, latency and cache effectiveness over the period |
| errors | Failure counts and rates, split by class |
| latency | Total vs backend time, and the slowest APIs |
| consumers | Who called, how much, and how well it went for them |
| apis | Per-proxy volume, errors and response time |
| geography | Origin country and serving region breakdown |
| ai | Prompt and completion token consumption per API and consumer |
| sla | Commitments against measured performance, with error budget |
| monetization | Billable usage and revenue by product and developer |

Formats

CSV, JSON or PDF. A scheduled report needs at least one recipient; an on-demand report needs none.

---

Source: [Overview & Analytics](https://docs.sdlccorp.com/docs/conflux/console/overview/)
