# Core concepts

Proxy, revision, product, app, subscription, environment - the ten nouns the whole platform is built from.

<a id="request"></a>

## What happens when a call arrives

Start at the runtime, because every object in the console exists to shape one of these steps. A partner’s app makes an HTTPS call. Before your backend ever hears about it:

1. **Hostname match** - An environment group binds the hostname to an environment.
2. **Base path match** - The path picks the API proxy, and the route within it.
3. **Request policies** - Auth, quota, threat protection, transformation.
4. **Target call** - Forwarded to the target server for that environment.
5. **Response policies** - Caching, masking, transformation, headers.
6. **Recorded** - One row added to the hourly traffic aggregate.

If any policy in step 3 refuses - an invalid key, an exhausted quota, a payload that trips threat protection - the call never reaches your backend, and the refusal shows on [Errors & faults](../../../the-console-page-by-page/current/console/overview.md#errors) as a **policy block** rather than a 4xx from your service.

<a id="producer"></a>

## The producer chain: proxy → revision → route → target

This is what your engineers build. Four objects, each nested in the one before it.

**API proxy** (also called “the API”)

The programmable façade in front of one backend. It owns the base path (`/v1/orders`), the protocol (REST, SOAP, GraphQL, gRPC, WebSocket), the auth scheme, the owner, the tags and whether it is listed on the portal. Everything else hangs off it.

**Revision**

An immutable snapshot of that proxy’s configuration - its routes and its policy attachments. Editing a proxy that is already deployed does not mutate what is serving traffic; it cuts a **new** revision. Deployments point at a specific revision, never at “latest”, which is precisely what makes rollback a single write rather than a re-deploy.

**Route** (also called proxy endpoint)

One method-plus-path inside the proxy: `GET /orders/{id}`. Carries its own upstream path rewrite, target server, conditional routing expression, timeout, retry count and cache setting.

**Target server**

A named backend, defined **per environment**. The route says “send this to `orders-service`”; the environment decides whether that resolves to the staging host or the production one. This indirection is why the same revision can be promoted from staging to production without editing a single URL.

Why revisions matter more than they look

Revisions are the reason the six-stage lifecycle and one-click rollback both work. “Approved” means a specific revision was approved - not a proxy name that has since been edited eight times.

<a id="consumer"></a>

## The consumer chain: product → app → credential → subscription

This is what your partners interact with. A proxy on its own is not consumable - nobody subscribes to a proxy.

1. **API product** - One or more proxies + quota + scopes.
2. **Developer** - A person or partner organisation.
3. **App** - A client identity - gets a key and secret.
4. **Subscription** - App → product. Auto or reviewed.
5. **Access granted** - The key now opens that product.

**API product**

The commercial and access unit. Bundles one or more proxies with a quota, OAuth scopes, an access rule (public / private / internal) and an approval rule (auto-approve, or route to a reviewer). A single proxy can appear in several products at different quotas - that is how a free tier and a partner tier front the same API.

**Developer**

The consumer-side identity: a person or a partner company, with a status of active, pending or suspended. Suspending a developer disables every app they own at once.

**App** (also called developer app, client)

A registered client application. This is the thing that holds credentials - a consumer key and secret. One developer typically owns several apps (mobile, web, sandbox), each with its own keys and its own subscriptions.

**Subscription**

The link between one app and one product. Until it is approved, the app’s key will not open that product. Approving records who decided, when, and any quota override.

The one distinction to get right

A **proxy** is technical - routing and policy. A **product** is commercial - access and quota. Callers never subscribe to a proxy; they subscribe to a product that contains it.

<a id="where"></a>

## Where it runs: environments, groups and deployments

**Environment**

A deployment target: development, test, staging or production, each with a cloud provider, a region, a deployment model (cloud / on-premise / hybrid) and - optionally - an approval gate.

**Environment group**

Binds external hostnames to one or more environments, with a TLS certificate reference. This is how `api.acme.com` reaches production while `api-staging.acme.com` reaches staging.

**Deployment**

A record that revision **N** of proxy **X** is serving environment **Y**, at a given traffic weight, using a given strategy. Deployments are never edited - a rollout adds a new one and adjusts weights.

<a id="the-four-rollout-strategies"></a>

### The four rollout strategies

| Strategy | What it does | Use when |
| --- | --- | --- |
| Direct | Replaces whatever currently serves the environment. | Non-production, or a trivial change |
| Canary | Sends a small slice of traffic to the new revision first. | You want production evidence before committing |
| Blue / green | Runs both revisions and cuts over in one step. | You need an instant, total switch - and an instant switch back |
| Weighted | Splits traffic across revisions by explicit weight. | A gradual ramp you drive by hand |

The production gate

Deploying to an environment marked production needs two things at once: the `deployment.prod` permission, **and** a proxy whose lifecycle stage is approved, published or versioned. A draft API cannot reach production even if you are an administrator.

<a id="governance"></a>

## How change is governed

Every API sits at exactly one of six lifecycle stages, and the legal moves between them are fixed:

1. **Draft** - Design in progress. Not on the portal.
2. **Review** - Standards run against the revision.
3. **Approved** - Gated - needs sign-off.
4. **Published** - Gated - live on the portal.
5. **Versioned** - A newer major runs alongside.
6. **Retired** - Gated - withdrawn and archived.

**Governance standard**

A machine-checkable rule - “every proxy name matches this pattern”, “a security policy is attached”, “a specification is published”. Eleven come built in, and you can write more from eleven evaluator types. A standard is either **blocking** (promotion stops until it passes or is waived) or advisory.

**Finding**

The result of running one standard against one proxy: pass, fail or waived, with remediation text. A waiver records who accepted the risk and why, and survives re-evaluation.

**Two-person approval**

A lifecycle transition into a gated stage is a request, not an action. Whoever requested it cannot be the person who approves it - the server refuses, regardless of permissions.

<a id="policy"></a>

## Policies, and where they run

A policy is a single processing step attached to a proxy at a specific point in the request pipeline. Conflux ships **54** built-in types across five categories - the full list is in [the policy reference](../../../reference/current/reference/policies.md). What matters conceptually is **where** a policy sits, because that decides what it can still change:

| Flow | When it runs | What belongs here |
| --- | --- | --- |
| Proxy Request | First, as the call enters the gateway. | Authentication, quota, spike arrest, threat protection, CORS |
| Target Request | Just before the call leaves for the backend. | Path rewrite, last-mile JWT, header injection, format conversion |
| Target Response | As the backend’s response returns. | Cache populate, XML→JSON, extract variables |
| Proxy Response | Last, as the response leaves for the client. | Data masking, compression, response headers |
| Fault Rule | Whenever a policy or the backend raises a fault. | Custom error shapes, alerting callouts, logging |

Order is part of the configuration

Within a flow, policies execute in the order you arrange them, each with an optional condition and an enable/disable switch. Verifying an API key before applying that key’s quota is not an accident - it is the order you set on the Policies tab.

<a id="confusables"></a>

## Six pairs people mix up

| These two | Are different because… |
| --- | --- |
| Proxy vs Product | A proxy is technical (routes, policies). A product is commercial (quota, access, price). Consumers subscribe to products. |
| Revision vs Version | A revision is an internal immutable snapshot, numbered automatically. A version is the public major version in the base path - v1, v2 - which consumers see. |
| Policy vs Standard | A policy is enforced at runtime on every call. A standard is checked at review time against the configuration. One protects traffic; the other protects quality. |
| Developer vs User | A developer is a consumer of your APIs, living on the portal side. A user is someone with a console login. |
| Alert vs Incident | An alert is a standing rule watching a metric. An incident is the thing that opens when the rule breaches - it has an owner, a timeline and a resolution. |
| Environment vs Environment group | An environment is where a revision runs. A group maps public hostnames onto environments. One group can front several environments. |

<a id="tenancy"></a>

## Organizations and tenancy

Every object above belongs to exactly one **organization** - a fully isolated tenant with its own APIs, environments, developers, settings and audit trail. Data never crosses that line by accident: the tenant is resolved from your session on the server, not from anything the browser sends.

A Super Admin is the single exception, and only explicitly - by naming another tenant in a request. Everyone else, including an Organization Administrator, sees exactly one tenant and cannot address another.

Why this shows up in the API

Because the tenant comes from the session, no create or update call can move a record into another organization by including an `organizationId` in the body - the field is stripped before the write.

---

Source: [Core concepts](https://docs.sdlccorp.com/docs/conflux/getting-started/concepts/)
