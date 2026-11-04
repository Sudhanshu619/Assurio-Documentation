# Roles & permissions

Eight roles over 77 permission codes - who can do what, and how the console decides what to show you.

<a id="model"></a>

## How access works

Every endpoint in Conflux is gated by one or more **permission codes**. A role is nothing more than the set of codes it grants. There are 77 codes across 22 groups, and 8 roles.

- **The code is the unit.** `deployment.prod` means “may deploy to a production environment”, and it means exactly that on the API and in the UI alike.
- **Any-of, not all-of.** A route that lists two codes admits a caller holding either one.
- **The backend is the authority.** Hiding a button is a courtesy; the endpoint behind it re-checks the permission on every call.
- **Changes take effect immediately.** Changing a user’s role revokes their sessions, so the new grants apply on their next request rather than at their next login.

<a id="the-console-asks-the-server-what-to-show"></a>

### The console asks the server what to show

The left-hand navigation is not a static list in the frontend. The server walks the navigation tree, keeps only the entries whose permissions the caller actually holds, drops any section that ends up empty, and returns what remains:

GET /api/rbac/my-sidebar

```
{ "code": 200, "status": true, "data": { "sidebar": [
    { "section": "Overview",    "items": [ … ] },
    { "section": "API Gateway", "items": [ … ] }
] } }
```

So a role is never shown a link to a page it would be refused - and if you add a permission to a role, the affected users’ navigation grows without a frontend release.

<a id="roles"></a>

## The eight roles

Modelled on how API platforms actually split duties.

| Role | Codes | Owns | Cannot |
| --- | --- | --- | --- |
| Super Admin | 77 | The platform. Every organization, plus tenant creation and deletion. | Nothing - this is the full catalogue. |
| Organization Administrator | 75 | Everything inside one tenant, including users, roles and settings. | Create or delete organizations (`org.create`, `org.delete`). |
| API Developer | 37 | Proxies, revisions, routes, policy attachment, products, specifications. Deploys and rolls back. | Production deploys, traffic shifting, approving their own promotions, users, audit, billing. |
| Operations Engineer | 38 | The whole deployment surface - production, traffic weights, rollback - plus fleet, alerts, incidents and SLA. | Authoring proxies or policies, approving lifecycle moves, billing, user administration. |
| Security Administrator | 42 | The policy library, credential lifecycle, subscription approval, lifecycle approval and the audit trail. | Deploying anything, editing proxies, managing users or settings. |
| Business Analyst | 26 | All analytics and reports, SLA reporting, and the commercial surface - rate plans and billing. | Any gateway, governance, audit or user change. Read-only everywhere else. |
| Auditor | 29 | Read-only visibility across configuration, governance and the full audit trail, including CSV export. | Any write at all, anywhere. Not a single create, update or delete code. |
| API Consumer | 12 | Their own apps and credentials, subscription requests, the catalog and their usage. | Everything on the producer side - proxies, policies, deployments, other developers’ apps. |

Reading the numbers

The count is how many of the 77 codes the role holds - not how important it is. The Auditor’s 29 codes are all `*.view`; the API Developer’s 37 include creates and deletes across six modules.

<a id="sees"></a>

## What each role actually sees

The navigation each role receives from the server, by default:

| Role | Navigation sections |
| --- | --- |
| Super Admin / Admin | Overview · API Gateway · Publish · Operate · Govern · Monetize · Administration (all) |
| API Developer | Overview (no Reports) · API Gateway · Publish · Operate (Monitoring, Incidents, Fleet) · Govern (Lifecycle, Approvals, Standards) |
| Operations Engineer | Overview · API Gateway (read) · Operate (all) · Govern (Lifecycle) · Administration (Integrations, Settings) |
| Security Administrator | Overview · Policies · Publish · Operate · Govern (all, incl. Audit) · Administration (Users, Roles) |
| Business Analyst | Overview · API Gateway (read) · Publish · Operate · Govern (no Audit) · Monetize · Administration (read) |
| Auditor | Everything the Analyst sees, plus Audit Trail, Users and Roles - all read-only |
| API Consumer | Overview · Publish (Products, Apps, Subscriptions, Portal) · Monetize (read) |

Try it yourself

Sign in as an Auditor and open any list - every “New”, “Edit” and “Delete” button is simply absent. Then sign in with an API Consumer account and navigate manually to `/proxies`: the guard redirects to `/access-denied` before the page renders, and the API would refuse it regardless.

<a id="catalogue"></a>

## The permission catalogue

All 77 codes, grouped. The console’s [Roles & permissions](../../../the-console-page-by-page/current/console/admin.md#roles) screen renders this same catalogue as an editable matrix.

| Group | Codes |
| --- | --- |
| Dashboard (1) | dashboard.view |
| Organization (4) | org.view · org.create · org.update · org.delete |
| Environment (5) | env.view · env.create · env.update · env.delete · envgroup.manage |
| Proxy (6) | proxy.view · proxy.create · proxy.update · proxy.delete · proxy.revision.create · proxy.export |
| Policy (5) | policy.view · policy.create · policy.update · policy.delete · policy.attach |
| Target (2) | target.view · target.manage |
| Deployment (5) | deployment.view · deployment.create · deployment.prod · deployment.rollback · deployment.traffic |
| Product (4) | product.view · product.create · product.update · product.delete |
| Developer (2) | developer.view · developer.manage |
| App (6) | app.view.self · app.view · app.create · app.update · app.delete · app.credential.manage |
| Subscription (3) | subscription.view · subscription.request · subscription.approve |
| Portal (3) | portal.view · portal.manage · spec.manage |
| Analytics (4) | analytics.view · analytics.export · report.view · report.manage |
| Monitoring (7) | monitoring.view · alert.manage · incident.view · incident.manage · gateway.view · gateway.manage · sla.manage |
| Governance (4) | governance.view · lifecycle.transition · lifecycle.approve · standard.manage |
| Monetization (3) | monetization.view · rateplan.manage · billing.view |
| Integration (2) | integration.view · integration.manage |
| Audit (2) | audit.view · audit.export |
| User (4) | user.view · user.create · user.update · user.delete |
| RBAC (2) | role.view · role.manage |
| Settings (3) | settings.view · settings.manage · notification.view |

<a id="guardrails"></a>

## Guardrails that outrank permissions

A few rules the server enforces even when your role technically allows the action. These exist so that no single account can quietly remove the checks on itself:

| Rule | Why |
| --- | --- |
| You cannot approve a lifecycle change you requested | Two-person approval. Holding lifecycle.approve does not let you wave your own work through. |
| A production deploy needs an approved API | Both `deployment.prod` **and** a lifecycle stage of approved, published or versioned. |
| The last Super Admin cannot be demoted or deleted | Otherwise a tenant could be left with nobody able to administer it. |
| A blocking governance finding stops promotion | Review → approved is refused until the standard passes or is explicitly waived, with a reason. |
| Nothing can write to the audit trail | There is no update or delete endpoint. Read and export only, for anyone, at any role. |
| Credentials never appear in a list response | Secrets are stripped on serialisation. Revealing one is a separate, individually audited endpoint requiring `app.credential.manage`. |

<a id="custom"></a>

## Custom roles

The eight roles are system roles: they come built in, and their grants are the defaults described above. You can edit those grants, and you can create additional roles, from [Administration → Roles & permissions](../../../the-console-page-by-page/current/console/admin.md#roles).

- Toggling a permission in the matrix takes effect for everyone holding that role, immediately.
- A new role starts empty - grant it the view codes for the areas it needs before assigning anyone to it.
- Cache note: grants are cached per role in the API process and invalidated on change, so there is no “wait for it to propagate” step.

---

Source: [Roles & permissions](https://docs.sdlccorp.com/docs/conflux/getting-started/roles/)
