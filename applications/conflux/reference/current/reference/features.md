# Feature inventory

Every capability the platform ships, module by module, with the screen each one lives on.

<a id="intro"></a>

## How this list was assembled

The scope came from reconciling two sources: the Conflux product modules - API Gateway, Security, Developer Portal, Lifecycle & Governance, Analytics & Monitoring, plus the integration framework - and the domain model a mature API management platform actually uses, which is where revisions, API products, environment groups, the policy catalogue, monetization and the newer AI-gateway policies come from.

Every row below is implemented end to end: a database table, a service, a permission-gated REST endpoint and a console screen.

<a id="gateway"></a>

## 1 · API Gateway

| Feature | What it does | Where |
| --- | --- | --- |
| API proxies | The programmable façade in front of a backend: base path, version, protocol, auth scheme, tags, owner, portal visibility. | [Proxies](../../../the-console-page-by-page/current/console/gateway.md#proxies) |
| Multi-protocol | REST, SOAP, GraphQL, gRPC and WebSocket proxies. | Proxies |
| Revisions | Immutable configuration snapshots. Editing a deployed proxy cuts a new revision instead of mutating what serves traffic. | Proxy → Revisions |
| Routes | Per-route method, path, upstream rewrite, target, conditional routing, timeout, retries and edge caching. | Proxy → Routes |
| Target servers | Named backends per environment, with connection pool, timeouts, weight and health probe. | [Target servers](../../../the-console-page-by-page/current/console/gateway.md#targets) |
| Progressive delivery | Direct, canary, blue-green and weighted strategies, with a traffic editor that enforces a 100% total. | [Deployments](../../../the-console-page-by-page/current/console/gateway.md#deployments) |
| One-click rollback | Restores the previous revision at full weight and records what it was rolled back from. | Deployments |
| Resilience policies | Circuit breaker, retry with backoff, timeout and concurrent-connection limits, per route. | Proxy → Policies |
| Transformation engine | Assign Message, Extract Variables, URL rewrite, JSON↔XML, XSL transform, HTTP modifier. | Proxy → Policies |
| Performance | Response cache, lookup/populate/invalidate cache, compression, CORS, payload ceiling. | Proxy → Policies |
| Configuration export | Portable JSON bundle of a revision - routes plus resolved policy config - for GitOps promotion. | Proxy → Overview |
| Environments | Dev, test, staging and production, each with provider, region, deployment model and approval gate. | [Environments](../../../the-console-page-by-page/current/console/gateway.md#environments) |
| Environment groups | Bind external hostnames to environments, with a TLS certificate reference. | Environments → Hostname routing |

<a id="security"></a>

## 2 · Security

| Feature | What it does | Where |
| --- | --- | --- |
| Policy catalogue | 54 built-in types across five categories, each with a field schema that drives its configuration form. | [Policy reference](policies.md) |
| Authentication policies | OAuth 2.0 (four grant types), OpenID Connect, JWT verify/generate/decode, API key, SAML, mutual TLS, LDAP / AD, HTTP Basic, HMAC. | Policies |
| Authorization | 77 fine-grained permission codes across 8 roles, enforced on every endpoint; scope and claims checks available as policy config. | [Roles](../../../getting-started/current/getting-started/roles.md) |
| Threat protection | JSON and XML threat protection, regex protection for SQLi and XSS, bot and abuse detection, data masking. | Policies |
| Rate limiting & quotas | Quota per app, developer, IP or product; spike arrest; concurrent rate limit. | Policies |
| Access control | IP allow/deny by CIDR, and geographic allow/deny by country. | Policies |
| Credential lifecycle | Issue, rotate with a grace period, revoke, and a separately audited reveal. Secrets never appear in a list response. | [App detail](../../../the-console-page-by-page/current/console/publish.md#apps) |
| Policy templates | Fork a catalogue entry into a reusable, pre-approved org template, then attach it by name. | Policies |
| Policy pipeline editor | Attach, order, condition, enable and configure policies across the five gateway flows. | Proxy → Policies |
| Session security | Server-side sessions behind an HttpOnly cookie; a password or role change revokes them immediately. | [Sessions](../../../the-console-page-by-page/current/console/auth.md#sessions) |

<a id="ai"></a>

## 3 · AI Gateway

The module that makes an LLM endpoint a governed API rather than an open door - modelled on the same policy mechanics as everything else.

| Feature | What it does |
| --- | --- |
| LLM token quota | Meters prompt and completion tokens per consumer over a billing interval. |
| Prompt token limit | Rejects or truncates prompts above a token ceiling before they reach the model. |
| Prompt sanitisation | Screens inbound prompts for injection, jailbreaks, PII, secrets and toxicity. |
| Response sanitisation | Screens model output for leaked data, unsafe content and hallucinated links. |
| Semantic caching | Returns a cached completion when an incoming prompt is semantically similar; populate stores the pair with its embedding. |
| Model router | Routes LLM traffic across providers by weight, lowest cost, lowest latency or failover. |
| Token analytics | Prompt and completion consumption per API and per consumer, on the traffic dashboard and in the ai report. |

<a id="portal"></a>

## 4 · Developer Portal

| Feature | What it does | Where |
| --- | --- | --- |
| API catalog | Searchable, tag-filtered product catalog with per-product access rules enforced server-side. | [Portal](../../../the-console-page-by-page/current/console/publish.md#portal) |
| OpenAPI rendering | Published specifications rendered as a browsable operation list with methods, paths, summaries and response codes. | Portal product |
| Specification versioning | Multiple spec versions per proxy with a changelog; exactly one published at a time. | Proxy → Specification |
| Spec generation | Derives a starter OpenAPI 3 document from a proxy’s routes and auth scheme. | Proxy → Specification |
| Self-service credentials | Register an app, receive a consumer key and secret, rotate and revoke. | Apps |
| Subscription workflow | Request access; auto-approve or route to a reviewer queue with a note, quota override and decision record. | Subscriptions |
| Consumer workspace | A consumer’s own apps, credentials, subscriptions and usage - a different landing screen from the operator dashboard. | Dashboard |
| Portal branding | Accent colour, welcome message and self-registration toggle, driven from settings. | Settings → Portal |

<a id="governance"></a>

## 5 · Lifecycle & Governance

| Feature | What it does | Where |
| --- | --- | --- |
| Six-stage pipeline | Draft → review → approved → published → versioned → retired, with the legal transitions enforced server-side. | [Lifecycle](../../../the-console-page-by-page/current/console/govern.md#lifecycle) |
| Approval gates | Approved, published and retired require sign-off, and the requester cannot approve their own request. | [Approvals](../../../the-console-page-by-page/current/console/govern.md#approvals) |
| Lifecycle board | Every API laid out by stage, so what is stuck in review is obvious. | Lifecycle |
| Governance standards | 11 built-in machine-checkable rules across naming, security, documentation, versioning, resilience and observability - plus custom rules from 11 evaluator types. | [Standards](../../../the-console-page-by-page/current/console/govern.md#standards) |
| Blocking vs advisory | A blocking standard stops the review → approved transition until it passes or is waived. | Standards |
| Findings & waivers | Per-proxy pass/fail/waived results with remediation text; a waiver records who accepted the risk and survives re-evaluation. | Standards → Findings |
| Compliance scoring | Org-wide score with a breakdown by category and severity. | Dashboard, Standards |
| Production gate | A production deployment requires both the permission and an approved lifecycle stage. | Deployments |
| Immutable audit history | Append-only trail of user activity, configuration changes and security events with before/after diffs, actor, IP and user agent. | [Audit trail](../../../the-console-page-by-page/current/console/govern.md#audit) |
| Audit-ready reporting | Filter by category, severity, actor, entity and date range; CSV export, itself audited. | Audit trail |

<a id="analytics"></a>

## 6 · Analytics & Monitoring

| Feature | What it does | Where |
| --- | --- | --- |
| Real-time dashboards | Requests, error rate, latency (avg/p50/p95/p99), availability, cache hit rate, throughput and data transferred. | [Traffic](../../../the-console-page-by-page/current/console/overview.md#traffic) |
| Time series | Auto-bucketed by hour, day or week from the selected window, with period-over-period trend arrows. | Traffic |
| Error analysis | 4xx / 5xx / policy-block split, failure trend, and worst offenders ranked by rate rather than count. | [Errors](../../../the-console-page-by-page/current/console/overview.md#errors) |
| Latency analysis | Total vs backend time, so gateway overhead is visible; slowest APIs by p95. | Traffic |
| Consumer analytics | Top apps and developers, traffic share and concentration, service quality per consumer. | [Consumers](../../../the-console-page-by-page/current/console/overview.md#consumers) |
| Geographic usage | Traffic, latency and availability by country of origin and by serving region. | [Geography](../../../the-console-page-by-page/current/console/overview.md#geography) |
| Product analytics | Which commercial bundle traffic arrives through. | Traffic, Consumers |
| SLA monitoring | Availability, latency and error-rate commitments per API, product or consumer, measured against real traffic, with error-budget consumption. | [SLA targets](../../../the-console-page-by-page/current/console/operate.md#sla) |
| Alert rules | Thresholds on seven metrics with a comparator, sustain duration and severity; global or scoped to an API or environment. | [Alerts](../../../the-console-page-by-page/current/console/operate.md#alerts) |
| Incident management | Alert breaches open an incident with an owner; acknowledge → investigate → monitor → resolve, each step appending to a timeline. | [Incidents](../../../the-console-page-by-page/current/console/operate.md#incidents) |
| Gateway fleet | Node-level health, CPU and memory, throughput, connections, uptime and heartbeat; regional roll-up; drain for a rolling upgrade. | [Fleet](../../../the-console-page-by-page/current/console/operate.md#gateways) |
| Custom & scheduled reports | Nine report types, saved queries, on-demand run, preview, and daily/weekly/monthly schedules with recipients. | [Reports](../../../the-console-page-by-page/current/console/overview.md#reports) |
| Analytics export | CSV export by proxy, product, consumer, country or environment. | Every analytics screen |
| Notifications | Per-user in-app inbox with severity, deep links, unread badge and polling. | Header |
| Distributed tracing | Policy that propagates W3C trace context and exports spans (OTLP, Jaeger, Zipkin, Datadog). | Policies |

One measurement, many screens

All of these read the same hourly traffic aggregate, which is why a report, a dashboard, an SLA calculation and an invoice can never disagree about the same hour.

<a id="monetization"></a>

## 7 · Monetization

| Feature | What it does | Where |
| --- | --- | --- |
| Rate plans | Free, flat-rate, pay-as-you-go, tiered and revenue-share, each with currency, billing period, fees, allowance and per-call rate. | [Rate plans](../../../the-console-page-by-page/current/console/monetize.md#rate-plans) |
| Volume tiers | Banded pricing walked band by band at billing time. | Rate plans |
| Prepaid & postpaid | Prepaid plans hold a balance that billing draws down; postpaid are invoiced in arrears. | Rate plans |
| Plan lifecycle | Draft → published → deprecated, with subscribers blocked from unpublished plans. | Rate plans |
| Plan subscriptions | Put a developer on a plan, top up a prepaid balance, cancel. | Rate plans → Subscribers |
| Billing runs | Measures each subscription’s real traffic over a period, prices it against the plan and writes an invoice with line items. | [Billing](../../../the-console-page-by-page/current/console/monetize.md#billing) |
| Revenue dashboard | Billed, collected, outstanding, revenue share, monthly trend and top developers by revenue. | Billing |
| Portal pricing | Published plans rendered as pricing cards on the catalog entry. | Portal product |

<a id="integration"></a>

## 8 · Integration framework

| Feature | What it does |
| --- | --- |
| Connector catalogue | 19 prebuilt connectors, each with its own field and secret schema. |
| Identity | Okta, Microsoft Entra ID, Keycloak, LDAP / Active Directory. |
| ITSM | ServiceNow, Jira. |
| Observability | Datadog, Prometheus, Grafana, Splunk. |
| Cloud | AWS, Azure, Google Cloud. |
| CI/CD | GitHub, GitLab, Azure DevOps, Jenkins. |
| Messaging | Apache Kafka, RabbitMQ. |
| Write-only secrets | Credentials are stored and reported as set or not-set, never returned. A partial form submission keeps the stored value. |
| Connection test | Probes a configured connector and records the result with a last-checked timestamp. |
| GitOps / IaC | Proxy revisions export as a portable JSON bundle for a repository-driven promotion flow. |

<a id="platform"></a>

## 9 · Platform & administration

| Feature | What it does | Where |
| --- | --- | --- |
| Multi-tenancy | Every artifact is scoped to an organization. A super admin may act across tenants explicitly; nobody else sees another tenant’s data. | [Organizations](../../../the-console-page-by-page/current/console/admin.md#organizations) |
| Deployment options | Cloud, on-premise and hybrid recorded per organization and per environment, with provider and region. | Organizations, Environments |
| Users | Invite, edit, suspend, delete, force-reset a password. A role or status change revokes sessions immediately. | [Users](../../../the-console-page-by-page/current/console/admin.md#users) |
| Roles & permissions | 8 system roles over a 77-code catalogue, edited as a matrix. Custom roles supported; the last super admin cannot be demoted or deleted. | [Roles](../../../the-console-page-by-page/current/console/admin.md#roles) |
| Session management | See and revoke your own active sessions per device. | [Profile](../../../the-console-page-by-page/current/console/admin.md#profile) |
| Settings | 30 settings across 8 groups, resolved as platform default then tenant override, with a revert action. | [Settings](../../../the-console-page-by-page/current/console/admin.md#settings) |
| Authentication | Sign-up, sign-in, sign-out, forgot password, reset password (revokes all sessions), change password (keeps the current device). | [Auth](../../../the-console-page-by-page/current/console/auth.md) |
| API documentation | OpenAPI 3 generated from the API itself - 164 paths, 233 operations - served as Swagger UI, including the required permission on every operation. | [Architecture](architecture.md#swagger) |

<a id="out-of-scope-deliberately"></a>

### Out of scope, deliberately

The data plane runtime itself, and the operational guarantees of a running deployment - availability, multi-region, zero-downtime upgrades, disaster recovery - plus commercial services such as support and training. What **is** implemented is the modelling and measurement of those: deployment models, regions, node health, SLA targets and error budgets. See [the FAQ](faq.md#scope) for the full statement.

Counts at a glance

`77` permissions · `8` roles · `54` policy types · `19` connectors · `30` settings · `11` governance standards · `9` report types · `39` tables · `164` API paths · `34` console screens.

---

Source: [Feature inventory](https://docs.sdlccorp.com/docs/conflux/reference/features/)
