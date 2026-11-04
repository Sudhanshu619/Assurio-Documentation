# API Gateway

Proxies and their seven-tab detail view, the policy library, target servers, deployments and environments.

<a id="proxies"></a>

## API proxies

**Route:** `/proxies` · **Sidebar:** API Gateway › API Proxies · **Needs:** `proxy.view`

The programmable façade in front of each backend. Routing, transformation, policy and versioning live here.

**What you see**

- Every proxy with its base path, protocol, version, lifecycle stage and status
- Which environments it is currently deployed to
- Owner, tags and portal visibility

**What you can do**

- Search by name or base path
- Filter by lifecycle stage, protocol or status
- Create a proxy - name, base path, protocol, version, auth scheme, owner, tags
- Open one to reach its seven-tab detail view

**Good to know:** The base path is what makes an incoming call resolve to this proxy, so it must be unique within the organization. Convention is to version it - `/v1/orders` - because that is what lets v1 and v2 run side by side later.

<a id="proxy-detail"></a>

## Proxy detail - the seven tabs

Everything about one API lives behind `/proxies/:id`. The tabs follow the order you would actually work in: describe it, route it, protect it, ship it, version it, prove it, document it.

<a id="1--overview"></a>

### 1 · Overview

**Route:** `/proxies/:id` · **Needs:** `proxy.view`

Identity and current position: machine name, base path, protocol, version, auth scheme, owner, tags, portal visibility, plus live traffic for this proxy.

**What you see**

- Configuration summary
- Traffic, error rate and latency for this proxy alone
- Current lifecycle stage and where it is deployed

**What you can do**

- Edit the proxy
- Request a lifecycle transition
- Export the revision bundle
- Delete the proxy

**Good to know:** Export produces a portable JSON bundle - routes plus resolved policy configuration - for a GitOps promotion flow.

<a id="2--routes"></a>

### 2 · Routes

**Route:** `/proxies/:id` · **Needs:** `proxy.view`

The method-and-path pairs this proxy exposes, and what each one forwards to.

**What you see**

- Method, path and the upstream path it rewrites to
- The target server it resolves to
- Timeout, retries, caching and any conditional routing expression

**What you can do**

- Add a route
- Edit or remove one
- Point a route at a different target server

**Good to know:** A route names a target **server**, not a URL. The environment decides which host that resolves to, which is why the same revision promotes cleanly from staging to production.

<a id="3--policies"></a>

### 3 · Policies

**Route:** `/proxies/:id` · **Needs:** `proxy.view`, `policy.attach`

The policy pipeline editor - the single most important screen in the gateway module.

**What you see**

- All five flows laid out as the request/response pipeline the gateway actually executes
- A “backend target” divider between the request half and the response half
- Each attached policy with its order, condition and enabled state

**What you can do**

- Attach a policy from the catalogue or from an org template
- Reorder within a flow - execution order is the order shown
- Configure a policy through a form generated from its field schema
- Add a condition, or disable a policy without detaching it

**Good to know:** Disabling beats detaching while you are debugging: the attachment and its configuration survive, so re-enabling is one click rather than a re-configure.

<a id="4--deployments"></a>

### 4 · Deployments

**Route:** `/proxies/:id` · **Needs:** `deployment.view`

Where this proxy is running right now, and the history of how it got there.

**What you see**

- Each environment with the revision serving it, its weight and strategy
- Who deployed it and when
- Any rollout still in progress

**What you can do**

- Deploy a revision to an environment
- Roll back
- Shift traffic between revisions

**Good to know:** Production is gated twice: you need `deployment.prod` and the proxy must be approved, published or versioned.

<a id="5--revisions"></a>

### 5 · Revisions

**Route:** `/proxies/:id` · **Needs:** `proxy.view`

The immutable configuration snapshots this proxy has produced.

**What you see**

- Every revision with its number, author, creation time and deployment state
- Which revisions are locked because they are serving traffic

**What you can do**

- Cut a new revision from the current configuration
- Inspect what a revision contained

**Good to know:** Editing a deployed proxy does not mutate what is serving traffic - it cuts a new revision, copying the routes and policy attachments. That is what makes rollback a single write.

<a id="6--governance"></a>

### 6 · Governance

**Route:** `/proxies/:id` · **Needs:** `governance.view`

How this API scores against the organization’s standards.

**What you see**

- Every standard evaluated against this proxy: pass, fail or waived
- Severity and remediation text for each failure
- Whether a failure is blocking or advisory

**What you can do**

- Re-evaluate the standards after a change
- Follow a finding through to the setting that fixes it

**Good to know:** A blocking failure stops the review → approved transition before the request is even created - so fixing findings here is how you unblock a promotion.

<a id="7--specification"></a>

### 7 · Specification

**Route:** `/proxies/:id` · **Needs:** `proxy.view`, `spec.manage`

The OpenAPI document consumers read on the developer portal.

**What you see**

- Every spec version with its changelog
- Which one is currently published
- The rendered operation list: methods, paths, summaries, response codes

**What you can do**

- Generate a starter OpenAPI 3 document from the routes and auth scheme
- Upload or edit a version
- Publish exactly one version to the portal

**Good to know:** Exactly one version is published at a time. Publishing a new one replaces what the portal shows without deleting the history.

<a id="policies"></a>

## Policies

**Route:** `/policies` · **Sidebar:** API Gateway › Policies · **Needs:** `policy.view`

Security, traffic management, mediation, extension and AI-gateway policy - the library every proxy draws from.

**What you see**

- 54 built-in policy types across five categories, each with its description and field schema
- Your organization’s own reusable templates alongside them
- Which proxies currently attach each policy

**What you can do**

- Search and filter by category, or by built-in vs your templates
- Fork a catalogue entry into a pre-configured org template
- Edit or retire a template

**Good to know:** A template is the answer to “every partner API should use the same quota settings”. Configure it once as **Standard Partner Quota**, then attach it by name - and change it in one place later.

<a id="the-five-categories"></a>

### The five categories

| Category | Count | What it covers |
| --- | --- | --- |
| Traffic management | 11 | Quota, spike arrest, caching, compression, circuit breaker, retry, timeout |
| Security | 18 | OAuth 2.0, OIDC, JWT, API key, SAML, mTLS, LDAP, HMAC, threat protection, IP control, masking |
| Mediation | 11 | Assign message, extract variables, URL rewrite, JSON↔XML, XSLT, spec validation, raise fault |
| Extension | 7 | JavaScript, service callout, flow callout, logging, key-value map, data capture, tracing |
| AI gateway | 7 | LLM token quota, prompt limit, prompt/response sanitisation, semantic cache, model router |

Every type is listed with its purpose in [the policy reference](../../../reference/current/reference/policies.md).

<a id="targets"></a>

## Target servers

**Route:** `/targets` · **Sidebar:** API Gateway › Target Servers · **Needs:** `target.view`

The backends behind each proxy route, with their connection pool, timeout and health-probe settings.

**What you see**

- Name, host, port, protocol and base path
- The environment each definition belongs to, and its current health
- Connect and read timeouts, max connections, load-balance weight, health-check path and probe interval

**What you can do**

- Register a backend
- Filter by environment or health state
- Edit connection and probe settings
- Remove a target that no route references

**Good to know:** Keep the **name** stable across environments - that is the whole mechanism. Define `orders-service` once per environment pointing at different hosts, and a single proxy revision works in all of them.

<a id="deployments"></a>

## Deployments

**Route:** `/deployments` · **Sidebar:** API Gateway › Deployments · **Needs:** `deployment.view`

Which revision serves which environment, and how traffic is split between them during a progressive rollout.

**What you see**

- An environment matrix: every proxy against every environment, with the revision and weight in each cell
- A history tab of every deployment with actor, strategy, status and timestamp
- Rollouts in progress, with their current traffic split

**What you can do**

- Deploy a revision - choose environment and strategy
- Shift traffic between revisions during a canary or weighted rollout
- Roll back to the previous revision at full weight

**Good to know:** The traffic editor refuses to save unless the weights total exactly 100. A split that does not add up is not a rollout - it is an outage on the missing percent.

<a id="a-canary-start-to-finish"></a>

### A canary, start to finish

1. **Deploy as canary** - New revision takes 10%; the incumbent keeps 90%.
2. **Watch** - Error rate and p95 for the new revision on Traffic and Errors.
3. **Shift** - 10 → 25 → 50, as evidence allows.
4. **Complete** - New revision at 100. The old one stops serving.
5. **Or roll back** - One click restores the previous revision at full weight.

Rollback records what it undid

A rollback is not a silent revert - it writes a deployment recording which revision it was rolled back from, so the history reads as a decision rather than a mystery.

<a id="environments"></a>

## Environments

**Route:** `/environments` · **Sidebar:** API Gateway › Environments · **Needs:** `env.view`

Deployment targets and the hostnames that route to them. Production environments gate deployments behind approval.

**What you see**

- Each environment: type (development / test / staging / production), region, cloud provider and deployment model
- Whether it is flagged production, and whether it requires approval
- Health, deployed proxy count and traffic
- A second tab for hostname routing: environment groups binding hostnames to environments with a TLS certificate reference

**What you can do**

- Create an environment
- Edit its region, provider, deployment model or approval gate
- Create an environment group and bind hostnames to it
- Delete an environment that has nothing deployed to it

**Good to know:** The **is production** flag is not cosmetic. It is what turns on the double gate on deployment, so mark real production environments accordingly - and only those.

| Object | Answers |
| --- | --- |
| Environment | “Where does this revision run?” - dev, test, staging, production |
| Environment group | “What hostname do callers use to get there?” - api.acme.com → production |
| Target server | “What backend does it forward to in that environment?” |

---

Source: [API Gateway](https://docs.sdlccorp.com/docs/conflux/console/gateway/)
