# Administration

Tenants, users, the role matrix, connectors to the rest of your estate, platform settings and your own profile.

<a id="organizations"></a>

## Organizations

**Route:** `/organizations` · **Sidebar:** Administration › Organizations · **Needs:** `org.view`

Each organization is an isolated tenant: its own APIs, environments, developers and audit trail.

**What you see**

- Every tenant with its slug, deployment model, cloud provider and region
- Its availability target and contact address
- Counts of what it contains - proxies, users, developers, environments

**What you can do**

- Create a tenant (Super Admin only - needs `org.create`)
- Edit deployment model, provider, region or SLA target
- Filter by deployment model
- Delete an empty tenant

**Good to know:** An Organization Administrator can see and edit their own tenant but cannot create or delete tenants - those two codes are what separate the admin role from super admin.

<a id="users"></a>

## Users

**Route:** `/admin/users` · **Sidebar:** Administration › Users · **Needs:** `user.view`

Everyone with access to the Conflux control plane, and the role that decides what they can do.

**What you see**

- Name, email, role, status (active, invited, pending, suspended) and last sign-in
- Which organization each belongs to
- Role and status filters, and search

**What you can do**

- Invite a user and assign their role
- Change a role, or suspend an account
- Force a password reset
- Delete a user

**Good to know:** A role change or a suspension **revokes that user’s sessions immediately** - they do not keep their old permissions until their token expires, because there is no token.

The last-admin guard

Conflux refuses to demote or delete the final Super Admin in a tenant. Otherwise an organization could be left with nobody able to administer it, and no way back in.

<a id="roles"></a>

## Roles & permissions

**Route:** `/admin/roles` · **Sidebar:** Administration › Roles & Permissions · **Needs:** `role.view`, `role.manage`

Every endpoint in Conflux is gated by a permission code. A role is simply the set of codes it grants.

**What you see**

- All 77 permission codes grouped into 22 modules
- Every role as a column, with its grants as a matrix
- How many users hold each role

**What you can do**

- Toggle a permission on or off for a role
- Create a custom role
- Rename or describe a role

**Good to know:** Changes apply immediately for everyone holding that role - grants are cached per role in the API process and the cache is invalidated on write. See [Roles & permissions](../../../getting-started/current/getting-started/roles.md) for the full catalogue.

<a id="integrations"></a>

## Integrations

**Route:** `/integrations` · **Sidebar:** Administration › Integrations · **Needs:** `integration.view`

Connect Conflux to the identity, ITSM, observability, cloud, CI/CD and messaging systems already in your estate.

**What you see**

- 19 prebuilt connectors across six categories, filterable by category
- Connection status: connected, disconnected or error, with a last-checked timestamp
- Per-connector configuration fields, generated from that connector’s schema

**What you can do**

- Configure a connector
- Test the connection - the result and timestamp are recorded
- Disconnect one

**Good to know:** Credentials are **write-only**: they are stored and reported as set or not-set, never returned. A partial form submission keeps the stored value rather than clearing it, so you can edit a hostname without re-typing a secret.

<a id="the-connector-catalogue"></a>

### The connector catalogue

| Category | Connectors |
| --- | --- |
| Identity (4) | Okta · Microsoft Entra ID · Keycloak · LDAP / Active Directory |
| ITSM (2) | ServiceNow · Jira |
| Observability (4) | Datadog · Prometheus · Grafana · Splunk |
| Cloud (3) | Amazon Web Services · Microsoft Azure · Google Cloud |
| CI/CD (4) | GitHub · GitLab · Azure DevOps · Jenkins |
| Messaging (2) | Apache Kafka · RabbitMQ |

<a id="settings"></a>

## Settings

**Route:** `/settings` · **Sidebar:** Administration › Settings · **Needs:** `settings.view`

Platform configuration for this organization. Anything not overridden here inherits the platform default.

**What you see**

- 30 settings across eight groups, one tab per group
- Each setting’s current value, and whether it is a tenant override or the inherited default

**What you can do**

- Change a value (needs `settings.manage`)
- Revert a setting to the platform default

**Good to know:** Resolution is two-level: platform default, then tenant override. Reverting removes the override rather than writing the default value, so a later change to the platform default still reaches you.

<a id="the-eight-groups"></a>

### The eight groups

| Group | Controls | Examples |
| --- | --- | --- |
| General (3) | Platform identity and defaults | Platform name, support email, timezone |
| Gateway (5) | Defaults applied to new routes and proxies | Default timeout, retries, max payload, compression, cache TTL |
| Security (5) | Credential lifetimes, session policy, auth requirements | Require auth on new proxies, credential expiry, rotation grace, session TTL, enforce MFA |
| Governance (3) | How strictly the lifecycle is enforced | Block ungoverned production deploys, require two-person approval, auto-evaluate on new revision |
| Developer portal (5) | Branding and self-service behaviour | Portal enabled, self-registration, auto-approve subscriptions, brand colour, welcome message |
| Monitoring (4) | Alert cadence, SLA defaults, retention | Default SLA target, alert evaluation interval, incident auto-assign, retention days |
| Monetization (3) | Currency and billing-run configuration | Monetization enabled, currency, billing day of month |
| Notifications (2) | Which channels events fan out to | Email notifications, incident channels |

Four settings worth knowing about

`portal.autoApproveSubscriptions` decides whether access requests queue for a human. `security.requireAuthOnNewProxies` stops an unauthenticated API being created by accident. `governance.requireTwoPersonApproval` and `governance.blockUngovernedProdDeploys` are the two levers that make governance binding rather than advisory.

<a id="profile"></a>

## My profile

Reachable from the account menu at any role - it needs no permission at all.

**Route:** `/profile` · **Sidebar:** Account menu › My profile

Your details, password and the devices you are signed in on.

**What you see**

- Profile tab: name, email, role, organization, status, email verification, last sign-in and IP, member since
- Password tab: change your password, with a live strength checklist
- Sessions tab: every active session with its device, IP and last activity

**What you can do**

- Update your name and details
- Change your password
- Revoke an individual session, or all other sessions at once

**Good to know:** Changing your password signs out your other devices but keeps the one you are using - the opposite of a reset from the forgot-password flow, which signs out everything including you.

The header alongside it carries the notification inbox: severity-coded, deep-linked to whatever raised it, with an unread badge that polls in the background and stays quiet about transient network failures.

---

Source: [Administration](https://docs.sdlccorp.com/docs/conflux/console/admin/)
