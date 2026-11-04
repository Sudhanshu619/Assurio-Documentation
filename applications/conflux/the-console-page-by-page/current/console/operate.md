# Operate

Live health, alert rules, the incident queue, the gateway fleet and the SLA commitments you are measured against.

<a id="monitoring"></a>

## Monitoring

Where an operations engineer starts a shift. Analytics answers “what happened”; monitoring answers “what is happening, and is anyone on it”.

**Route:** `/monitoring` · **Sidebar:** Operate › Monitoring · **Needs:** `monitoring.view`

Live service health across traffic, the gateway fleet, SLA commitments and open incidents.

**What you see**

- Current traffic, error rate and latency against the recent baseline
- Fleet roll-up: healthy, degraded, draining and offline node counts
- SLA compliance summary and error-budget consumption
- Open incidents with severity and owner
- Armed alert rules and which are currently breaching

**What you can do**

- Open the fleet view
- Jump to all incidents
- Manage alert rules

**Good to know:** Everything here is a roll-up of a page you can open directly - this screen decides what deserves your attention, not what the numbers are.

<a id="alerts"></a>

## Alert rules

**Route:** `/alerts` · **Sidebar:** Operate › Alerts · **Needs:** `monitoring.view`, `alert.manage`

Watch a metric and open an incident when it stays outside its threshold for long enough to matter.

**What you see**

- Each rule: metric, comparator, threshold, sustain duration and severity
- Whether the rule is armed or paused
- Its scope - global, or narrowed to one API or environment

**What you can do**

- Create a rule
- Tune a threshold or sustain window
- Pause a rule instead of deleting it while you tune it
- Filter by severity or metric

**Good to know:** The **sustained for** field is what separates a page-worthy alert from noise: it stops a single bad minute waking anyone.

<a id="the-seven-metrics-you-can-alert-on"></a>

### The seven metrics you can alert on

| Metric | Typical rule |
| --- | --- |
| Error rate (%) | above 5 for 10 minutes → high |
| p95 latency (ms) | above 800 for 15 minutes → medium |
| p99 latency (ms) | above 2000 for 15 minutes → medium |
| Requests | below an expected floor for 30 minutes → a silent integration |
| Availability (%) | below 99.9 for 5 minutes → critical |
| Quota usage (%) | above 90 → warn the consumer before they hit the wall |
| Cache hit rate (%) | below an expected floor → a caching regression |

Comparators

Above, at or above, below, at or below. Combine with the scope field to say “p95 above 800ms, but only in production, and only for the Payments API”.

<a id="incidents"></a>

## Incidents

**Route:** `/incidents` · **Sidebar:** Operate › Incidents · **Needs:** `incident.view`

Everything an alert opened or an operator raised, with the running timeline of what was done about it.

**What you see**

- Status tabs and severity filters
- For each incident: what triggered it, the measured value against the threshold, the affected API
- Start time, duration, acknowledgement and resolution times, and the assignee
- A timeline of every status change and note

**What you can do**

- Raise an incident by hand
- Acknowledge one and take ownership
- Move it through investigating and monitoring
- Add a note at any point
- Resolve it with a resolution summary

**Good to know:** The timeline is append-only. Editing history would defeat the purpose of having a record of what was believed, and when.

1. **Open** - An alert breached, or someone raised it.
2. **Acknowledged** - Someone owns it. The clock on response stops.
3. **Investigating** - Cause being established; notes accumulate.
4. **Monitoring** - A fix is in; watching for recurrence.
5. **Resolved** - Closed with a summary. Duration is now fixed.

<a id="gateways"></a>

## Gateway fleet

**Route:** `/gateways` · **Sidebar:** Operate › Gateway Fleet · **Needs:** `gateway.view`

Every data-plane node serving traffic, its load and where it sits.

**What you see**

- Node status: healthy, degraded, draining or offline
- CPU and memory, requests per second, active connections, uptime and last heartbeat
- Region and environment for each node, with a regional roll-up

**What you can do**

- Register a node
- Drain a node - it stops taking new traffic while finishing what it has, for a rolling upgrade
- Return a drained node to service
- Retire a node

**Good to know:** This is the one screen that looks at the **data plane** rather than at configuration. A node that stops sending heartbeats shows as offline here well before consumers notice anything.

<a id="sla"></a>

## SLA targets

**Route:** `/sla` · **Sidebar:** Operate › SLA Targets · **Needs:** `monitoring.view`, `sla.manage`

The availability and latency you have committed to, measured against the traffic actually observed.

**What you see**

- Each commitment: metric, target value, measurement window and scope
- Measured performance against the target, and whether it is currently met
- Error budget: how much of the allowed failure you have already spent this period

**What you can do**

- Define a target - scoped to an API, a product or a specific consumer
- Adjust the target or window
- Retire a commitment that no longer applies

**Good to know:** Measured against the same traffic aggregate the dashboards read, so an SLA report and the Traffic screen cannot tell two different stories about the same hour.

<a id="reading-an-error-budget"></a>

### Reading an error budget

A 99.9% availability target over 30 days allows roughly 43 minutes of failure. If you have spent 30 of them by the 10th, the budget line is the argument for pausing risky deploys - which is precisely the conversation the number exists to start. A target scoped to one partner is how you hold a contractual commitment to `that` consumer rather than an estate-wide average.

---

Source: [Operate](https://docs.sdlccorp.com/docs/conflux/console/operate/)
