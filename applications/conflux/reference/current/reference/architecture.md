# Architecture & API

How Conflux is put together, and the conventions every API endpoint follows.

<a id="shape"></a>

## One API behind everything

Conflux has two parts: an API server that owns every rule - validation, permissions, tenancy and audit - and the web console, which presents that data and never makes a decision about access.

Why the split matters

The console is one client of the API, not **the** client. A CI pipeline, a Terraform provider or a partner’s own tooling talks to exactly the same permission-gated endpoints, with the same audit trail behind them.

<a id="conventions"></a>

## API conventions

<a id="every-response-has-the-same-envelope"></a>

### Every response has the same envelope

200 OK

```
{ "code": 200, "status": true, "data": { "proxies": [ … ], "total": 8 } }
```

403 Forbidden

```
{ "code": 403, "status": false, "data": { "message": "You do not have permission to deploy to a production environment" } }
```

`status` is `true` for 2xx and `false` otherwise, so a client branches on one field rather than on a status-code range. Validation failures put a field-keyed `errors` object alongside the message.

<a id="the-rules-behind-every-endpoint"></a>

### The rules behind every endpoint

- **Authentication is a cookie.** Signing in (`POST /api/auth/login`) sets an HttpOnly session cookie. No token reaches the browser, so there is nothing for a script to steal and no refresh flow to get wrong.
- **Authorization is per endpoint.** Each endpoint lists the permission codes that admit a caller; holding any one of them is enough.
- **Tenancy comes from the session.** Your organization is taken from your session. A Super Admin may target another with `?organizationId=` or the `X-Organization-Id` header; nobody else can.
- **Mutations are audited.** Every write is recorded with actor, entity, IP, user agent and a before/after diff.
- **Lists behave the same everywhere.** Every list endpoint supports tenant scoping, search, filters and pagination in the same way.

<a id="swagger"></a>

## The API reference

Conflux serves an OpenAPI 3 reference - **164 paths, 233 operations, 24 tags** - as Swagger UI at `/api-docs` on the Conflux API server, and as raw JSON at `/api-docs.json`. Every operation shows the permission it requires and any role restriction.

Documentation that cannot drift

The reference is generated from the API itself rather than written alongside it, so when an endpoint’s permission changes, its documentation changes with it.

<a id="data"></a>

## Design decisions worth knowing

- **Revisions are immutable.** A deployed revision is locked. Changing a deployed proxy cuts a new revision, copying routes and policy attachments. Deployments point at a specific revision, never at “latest” - which is what makes rollback a single step.
- **Analytics reads an aggregate, not a log.** Traffic is stored as one pre-aggregated row per hour per proxy, environment, app, product and country, so every dashboard stays fast regardless of traffic volume.
- **Secrets are write-only.** Credential secrets are stripped from every list response, so no list can leak one. Revealing a secret is a separate action, audited at high severity, and integration credentials behave the same way.

<a id="frontend"></a>

## How the console behaves

- **The server decides your navigation.** The console asks the API for a navigation tree already filtered by your permissions, so you are never shown a link to a page you would be refused.
- **Permissions gate the UI; the API enforces them.** A hidden button or a blocked page is a convenience - every endpoint re-checks your permissions.
- **One palette.** Status colours come from a single scheme, so a red badge means the same thing on every screen.
- **Works on a phone.** The navigation rail becomes a drawer on small screens, tables scroll inside their own container, and dialogs become full-height sheets.

Troubleshooting is covered in [FAQ & troubleshooting](faq.md).

---

Source: [Architecture & API](https://docs.sdlccorp.com/docs/conflux/reference/architecture/)
