# Publish

Products, developers, apps, credentials, subscriptions and the developer portal your consumers actually use.

<a id="intro"></a>

## The consumer-facing half

Everything in the API Gateway section is about how an API **works**. Everything here is about who is allowed to call it and how they get a key. The two halves meet at the API product.

| Screen | Whose object it is |
| --- | --- |
| API products | Yours - what you sell or expose |
| Developers | Theirs - the person or partner company |
| Apps & credentials | Theirs - a client identity holding keys |
| Subscriptions | The link between an app and a product; you approve it |
| Developer portal | The consumer’s view of all of the above |

<a id="products"></a>

## API products

**Route:** `/products` · **Sidebar:** Publish › API Products · **Needs:** `product.view`

The unit a consumer subscribes to - one or more proxies bundled with a quota, scopes and an approval rule.

**What you see**

- Every product with the proxies it contains, its quota and time unit
- Access level: public, private or internal
- Whether subscription is auto-approved or reviewed
- Subscriber count and traffic

**What you can do**

- Create a product and choose which proxies it bundles
- Set the quota, OAuth scopes, access level and approval rule
- Publish it to the portal, or keep it hidden
- Delete a product no app subscribes to

**Good to know:** One proxy can sit in several products at different quotas. That is exactly how a free tier and a partner tier front the same API without duplicating a single route.

<a id="product-detail"></a>

### Product detail

**Route:** `/products/:id` · **Needs:** `product.view`

One product across three tabs: overview, its subscriptions, and its rate plans.

**What you see**

- The APIs included, and what subscribing grants access to
- Quota, scopes, access rule and traffic for this product
- Every subscription against it, with status and requester
- Attached rate plans and their pricing

**What you can do**

- Edit the product
- Approve or reject a subscription request in place
- Manage its rate plans
- Delete it

**Good to know:** Approving a request here does exactly what approving it on the Subscriptions queue does - same endpoint, same audit entry.

<a id="developers"></a>

## Developers

**Route:** `/developers` · **Sidebar:** Publish › Developers · **Needs:** `developer.view`

The people and partner organizations consuming your APIs, and the apps they own.

**What you see**

- Name, email, company and status - active, pending or suspended
- How many apps each owns
- When they joined

**What you can do**

- Onboard a partner directly
- Edit their details
- Suspend or reactivate them
- Search and filter by status

**Good to know:** Suspending a developer disables every app they own at once - the fastest lever you have when a partner needs cutting off, and reversible in one click.

<a id="developer-detail"></a>

### Developer detail

**Route:** `/developers/:id` · **Needs:** `developer.view`

One partner: their profile, their apps and their consumption.

**What you see**

- Contact details and status
- Every app they own, with its credentials and product grants
- Their traffic, error rate and quota usage

**What you can do**

- Edit or suspend the developer
- Open any of their apps

**Good to know:** Developers can also self-register through the portal, if self-registration is enabled in settings.

<a id="apps"></a>

## Apps & credentials

**Route:** `/apps` · **Sidebar:** Publish › Apps & Credentials · **Needs:** `app.view`, `app.view.self`

Every registered client application, its consumer keys and the products it may call. A consumer sees only their own.

**What you see**

- App name, owning developer, status and callback URL
- Credential status, and which products each app is subscribed to
- Traffic per app

**What you can do**

- Register an app - a consumer key and secret are issued immediately
- Open one to manage its keys and subscriptions
- Delete an app

**Good to know:** Two permissions cover this screen: `app.view` sees the whole tenant’s apps, `app.view.self` sees only your own. The consumer role holds the second.

<a id="app-detail"></a>

### App detail

**Route:** `/apps/:id` · **Needs:** `app.view`, `app.view.self`

The credential lifecycle for one client, plus its product access.

**What you see**

- Every credential with its status: active, pending, revoked or expired
- Approved and pending subscriptions
- A prominent banner if the app is suspended

**What you can do**

- Issue a new key
- Rotate a key with a grace period, so the old one keeps working while the consumer migrates
- Reveal a secret - a separate, individually audited action
- Revoke a credential
- Request a subscription to another product

**Good to know:** Secrets are shown exactly once, at issue time, behind an “I have stored it” confirmation. They never appear in a list response - `toJSON` strips them - so revealing one later is its own endpoint, audited at high severity.

<a id="rotation-not-replacement"></a>

### Rotation, not replacement

Rotating issues a new key while the old one stays valid for a grace period you choose. That is what lets a partner migrate without a coordinated outage. Revoking is the immediate version, for when a key has leaked.

<a id="subscriptions"></a>

## Subscriptions

**Route:** `/subscriptions` · **Sidebar:** Publish › Subscriptions · **Needs:** `subscription.view`

Requests for app access to an API product. Approving one activates the app’s credentials against it.

**What you see**

- Counts by status, and tabs for all, pending, approved, rejected and revoked
- Which app is asking for which product, who requested it and when
- Any note the requester left, and any quota override applied

**What you can do**

- Review a request and read its context
- Approve - optionally with a quota override for this consumer
- Reject with a reason
- Revoke access that was previously granted

**Good to know:** A product set to auto-approve never appears in this queue: the subscription is created approved. Reserve the queue for products where access is a decision, and needs `subscription.approve`.

<a id="portal"></a>

## Developer portal

**Route:** `/portal` · **Sidebar:** Publish › Developer Portal · **Needs:** `portal.view`

The consumer’s front door: a searchable catalog of published products, and their own workspace.

**What you see**

- The API catalog - every product published and visible to the caller, with search and tag filters
- A “my workspace” tab with the caller’s apps, keys and subscriptions
- Portal branding - accent colour and welcome message - driven from settings

**What you can do**

- Search and filter the catalog
- Open a product
- Register an app
- Jump to your apps

**Good to know:** Visibility is enforced server-side, not by hiding cards. A private product is not in the response at all for a caller who may not see it.

<a id="portal-product-page"></a>

### Portal product page

**Route:** `/portal/:slug` · **Needs:** `portal.view`

One catalog entry as a consumer sees it, across overview, API reference and pricing.

**What you see**

- What the product includes, its quota and access rules
- The published OpenAPI specification rendered as a browsable operation list
- Published rate plans as pricing cards
- The caller’s own subscription status for this product

**What you can do**

- Subscribe an app to the product
- Register an app first if you have none
- Read the API reference

**Good to know:** If the product auto-approves, subscribing is instant and the key works immediately. Otherwise the request lands on the [Subscriptions](publish.md#subscriptions) queue.

See it as a consumer

Sign in with an API Consumer account - the whole console collapses to this section plus a personal dashboard. It is the clearest way to understand what a partner actually experiences.

---

Source: [Publish](https://docs.sdlccorp.com/docs/conflux/console/publish/)
