# Govern

The lifecycle board, the approval queue, machine-checkable standards, and an audit trail nothing can rewrite.

<a id="lifecycle"></a>

## API lifecycle

Governance in Conflux is not a document - it is four screens that make the rules unavoidable. An API cannot reach production without passing them.

**Route:** `/governance/lifecycle` · **Sidebar:** Govern › Lifecycle · **Needs:** `governance.view`

Draft to retirement. Stages marked with an approval gate need a second person to sign off before the move applies.

**What you see**

- Every API laid out by stage, so what is stuck in review is immediately obvious
- Which stages carry an approval gate
- Pending transition requests against each API

**What you can do**

- Request a transition to the next legal stage
- Open an API to see why it cannot move yet

**Good to know:** Only legal moves are offered. The transition map is enforced on the server, so you cannot skip review by calling the API directly.

<a id="the-six-stages-and-the-legal-moves"></a>

### The six stages and the legal moves

| Stage | Means | Can move to | Gated? |
| --- | --- | --- | --- |
| Draft | Design in progress. Not visible on the portal. | Review | No |
| Review | Standards and policy checks are running against the revision. | Approved, or back to Draft | No |
| Approved | Signed off and cleared to publish. | Published, or back to Review | Yes |
| Published | Live on the portal and deployable to production. | Versioned, Retired | Yes |
| Versioned | A newer major version exists; both run side by side. | Retired, Published | No |
| Retired | Withdrawn from the catalog and archived. | - | Yes |

<a id="approvals"></a>

## Approvals

<a id="lifecycle-approvals"></a>

### Lifecycle approvals

**Route:** `/governance/approvals` · **Sidebar:** Govern › Approvals · **Needs:** `governance.view`, `lifecycle.approve`

Requests to move an API to a gated stage. Approving one applies the stage and publishes or retires the API accordingly.

**What you see**

- Tabs for awaiting decision, approved, rejected, auto-applied and all
- Who requested the move, from which stage to which, and their note
- The governance findings that were true at request time

**What you can do**

- Review a request in context
- Approve it - the stage change applies immediately
- Reject it with a reason

**Good to know:** **Two-person approval is enforced:** the server refuses a decision from the same user who filed the request, whatever their permissions say. That rule cannot be configured away.

Why a request can be blocked before it is even created

If a **blocking** standard is failing, the review → approved request is refused at creation time rather than sitting in a queue for someone to reject. Fix the finding on the proxy’s Governance tab, then request again.

<a id="standards"></a>

## Governance standards

**Route:** `/governance/standards` · **Sidebar:** Govern › Standards · **Needs:** `governance.view`, `standard.manage`

Machine-checkable rules the review stage runs against every API. A blocking standard stops promotion until it passes or is waived.

**What you see**

- Every standard with its code, category, severity and whether it blocks
- A findings tab: which APIs pass, fail or have a waiver, filterable by result and severity
- The org-wide compliance score, broken down by category

**What you can do**

- Create a standard from one of eleven evaluator types
- Toggle whether it blocks promotion
- Waive a finding - recording who accepted the risk and why
- Remove a waiver

**Good to know:** A waiver survives re-evaluation. It is a recorded decision, not a way of silencing the check.

<a id="the-eleven-built-in-standards"></a>

### The eleven built-in standards

| Code | Rule | Severity | Blocking |
| --- | --- | --- | --- |
| SEC-001 | API requires authentication | critical | Yes |
| SEC-002 | A security policy is attached | high | Yes |
| SEC-003 | Traffic is rate limited (quota, spike arrest or connection limit) | high | No |
| NAM-001 | Proxy name follows kebab-case | low | No |
| VER-001 | Base path carries a version segment | medium | No |
| DOC-001 | Published API specification | high | No |
| DOC-002 | Description is meaningful (40+ characters) | low | No |
| DOC-003 | API is tagged | low | No |
| RES-001 | Every route names a target server | medium | No |
| RES-002 | Timeouts stay under the 30s ceiling | medium | No |
| OBS-001 | Logging or tracing is attached | medium | No |

<a id="writing-your-own"></a>

### Writing your own

Custom standards are built from the same eleven evaluators the built-in ones use:

- `naming-pattern` - a field must match a regular expression
- `versioned-base-path` - the base path must carry a version segment
- `required-policy-category` - at least one policy from named categories is attached
- `required-policy-type` - at least one of a named list of policy types is attached
- `auth-required` - the auth scheme is not “none”
- `spec-published` - a specification version is published
- `description-required` - a description of at least N characters
- `routes-have-targets` - no route forwards into the void
- `timeout-ceiling` - no route exceeds a maximum timeout
- `observability-attached` - logging or tracing is present
- `tags-required` - at least N tags

<a id="audit"></a>

## Audit trail

**Route:** `/audit` · **Sidebar:** Govern › Audit Trail · **Needs:** `audit.view`

Every user action, configuration change and security event, recorded immutably. Nothing in Conflux can edit or delete a row here.

**What you see**

- Actor, role, action, entity, IP address and user agent for every event
- A before/after diff on configuration changes
- Seven categories: authentication, authorization, configuration, deployment, security, governance and data access
- Severity from info through critical

**What you can do**

- Filter by category, severity, actor, entity or date range
- Open an entry to read its full diff
- Export the filtered set as CSV - which is itself an audited event, requiring `audit.export`

**Good to know:** Append-only by construction: the table has no updated-at column and the module exposes read and export only. There is no endpoint that could modify a row, for anyone, at any role.

What “audited at high severity” means elsewhere in these docs

A handful of actions - revealing a credential secret, exporting the audit trail, deploying to production, force-resetting a password - are recorded with an elevated severity so they surface first when someone filters this page during a review.

---

Source: [Govern](https://docs.sdlccorp.com/docs/conflux/console/govern/)
