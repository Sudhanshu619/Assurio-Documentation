# What is Conflux?

The product in one page: what it manages, what it deliberately does not, and how the console is laid out.

<a id="overview"></a>

## Conflux in one paragraph

Conflux is an **enterprise API management platform**. It is the single place where an organisation designs its APIs, protects them with policy, publishes them to the developers who consume them, watches how they behave in production, governs how they change, and - where the APIs are a product - bills for them.

If your company exposes twenty, two hundred or two thousand HTTP endpoints across a dozen teams, Conflux is the layer that stops that estate becoming twenty different answers to the same questions: who is allowed to call this, how fast, what happens when it breaks, who approved the last change, and what did it cost.

The one-line version

An API proxy sits in front of your backend. Conflux is where you decide what that proxy does, who may call it, and what happens when something goes wrong.

<a id="problem"></a>

## The problem it solves

Without a management layer, every one of these concerns is solved again inside each service, by each team, slightly differently:

- **Access.** Each service invents its own key checking, or trusts the network and checks nothing.
- **Protection.** One noisy client can exhaust a backend nobody thought to rate-limit.
- **Change.** A breaking change ships because there was no gate between “merged” and “live”.
- **Visibility.** Nobody can answer “which partner is causing the 5xx spike?” without grepping logs.
- **Onboarding.** A new consumer waits days for a key that a portal could issue in a minute.
- **Evidence.** An auditor asks who approved a production change last March, and no one can say.

Conflux moves all six out of the services and into one governed layer. The backend team writes business logic; the gateway configuration in front of it handles the rest, and every change to that configuration is versioned, reviewed and recorded.

<a id="control-plane"></a>

## Control plane, not data plane

This distinction explains most of what you will see in the console, so it is worth ten seconds.

- **The data plane:** The gateway nodes that actually receive a caller’s request, run the policy chain, forward it to your backend and return the response. They terminate TLS and carry live traffic.
- **The control plane - this product:** Where that configuration is authored, reviewed, approved, deployed to an environment, measured and audited. Conflux stores the intent; the fleet executes it.

So when you attach a Quota policy in Conflux, you are not throttling a request in that moment - you are declaring that calls to this proxy are capped, versioning that declaration as a revision, and deploying that revision to an environment where the fleet enforces it. The [Gateway fleet](../../the-console-page-by-page/current/console/operate.md#gateways) page is where the two meet: it models and monitors the nodes doing the enforcing.

<a id="modules"></a>

## The seven areas of the console

The left-hand navigation is grouped by the job you are doing, not by the database table you are editing. Roughly in the order an API travels through them:

| Area | The question it answers | Typical owner |
| --- | --- | --- |
| Overview | Is the estate healthy, and what is waiting on me? | Everyone |
| API Gateway | What does this API do, and where is it running? | API developer, Ops |
| Publish | Who is allowed to call it, and how do they get a key? | API developer, Product |
| Operate | Is it behaving, and who is fixing it if not? | Operations engineer |
| Govern | Was this change reviewed, and can we prove it? | Security, Auditor |
| Monetize | What did this usage cost, and who is invoiced? | Business analyst |
| Administration | Who works here, and what may they touch? | Administrator |

Each area has its own chapter in these docs describing every screen inside it - see [The console, page by page](../../the-console-page-by-page/current/console/gateway.md).

<a id="journey"></a>

## The journey an API takes

Almost everything in Conflux is a step on one path. Learn this path and the navigation stops feeling like forty unrelated screens:

1. **Create a proxy** - Base path, protocol, routes to a backend.
2. **Attach policies** - Auth, quota, threat protection, caching.
3. **Pass governance** - Standards run; an approver signs off.
4. **Deploy a revision** - To an environment, direct or canary.
5. **Bundle into a product** - Listed on the developer portal.
6. **App subscribes** - Credentials issued, calls start.
7. **Watch and bill** - Analytics, SLA, incidents, invoices.

A useful mental split

The first four steps are the **producer** side - your engineers. The last three are the **consumer** side - the partners and app developers calling you. The console serves both, and the role you sign in as decides which half you see.

<a id="audiences"></a>

## Who uses it

- **API developers:** Build proxies, wire routes to targets, attach policies, cut revisions and deploy to test environments.
- **Operations engineers:** Deploy to production, run canaries, shift traffic, roll back, and own the alert and incident queue.
- **Security administrators:** Own the policy library and credential lifecycle, approve lifecycle promotions, read the audit trail.
- **Product & analysts:** Bundle proxies into products, set rate plans, read adoption and revenue reporting.
- **API consumers:** Partners and app developers: browse the catalog, register an app, request access, watch their own usage.
- **Auditors:** Read-only across configuration, governance findings and the immutable audit trail.

Access is enforced by `77` permission codes grouped into eight roles. See [Roles & permissions](../../getting-started/current/getting-started/roles.md) for exactly what each one may do.

<a id="next"></a>

## Where to go next

- **Just want to click around?:** [Quick start](../../getting-started/current/getting-started/quickstart.md) - sign in, see what your role can do and take the ten-minute tour.
- **New to API management?:** [Core concepts](../../getting-started/current/getting-started/concepts.md) - proxy, revision, product, app, subscription and the rest, in plain language.
- **Need to do a specific job?:** [Walkthroughs](../../reference/current/reference/walkthroughs.md) - publish an API, run a canary, onboard a partner, handle an incident, bill for usage.

---

Source: [What is Conflux?](https://docs.sdlccorp.com/docs/conflux/intro/)
