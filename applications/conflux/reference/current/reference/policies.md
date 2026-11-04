# Policy reference

All 54 built-in policy types across five categories, what each one does, and where in the pipeline it belongs.

<a id="how"></a>

## How policies work

A policy is one processing step attached to a proxy at a specific point in the request pipeline. You attach it, order it, optionally give it a condition, and configure it through a form generated from that policy type’s field schema.

- **Category** groups policies by intent - it does not restrict where they can be attached.
- **Flow** decides when it runs: proxy request, target request, target response, proxy response, or on fault.
- **Order** within a flow is execution order. Verifying an API key before applying that key’s quota is a choice you make here.
- **Condition** makes a policy apply selectively - one route, one client type, one header value.
- **Enabled** can be turned off without detaching, so the configuration survives while you debug.

The forms are generated, not hand-built

Every policy type carries a field schema on the backend, and the configuration form is rendered from it. Adding a new policy type is a backend-only change - no frontend release is needed for its form to appear.

<a id="traffic-management"></a>

## Traffic management (11)

Protecting your backend from load, and protecting your latency from your backend.

| Policy | What it does | Usual flow |
| --- | --- | --- |
| Quota | Caps the number of calls an app or developer may make over a time interval. | Proxy request |
| Spike Arrest | Smooths traffic bursts by throttling the instantaneous request rate. | Proxy request |
| Concurrent Rate Limit | Limits simultaneous in-flight connections to a backend target. | Target request |
| Response Cache | Caches backend responses at the gateway to cut latency and origin load. | Proxy request / response |
| Lookup Cache | Reads a value from the shared cache into a flow variable. | Proxy request |
| Populate Cache | Writes a flow variable into the shared cache under a key. | Target response |
| Invalidate Cache | Evicts one or more cache entries, typically after a write operation. | Target response |
| Compression | Applies gzip or brotli compression to responses above a size threshold. | Proxy response |
| Circuit Breaker | Trips open after repeated backend failures and fails fast until the target recovers. | Target request |
| Retry | Retries idempotent backend calls with backoff on transient failures. | Target request |
| Timeout | Bounds how long the gateway waits on connect and read for the target. | Target request |

Quota vs Spike Arrest

They solve different problems and are usually attached together. Quota is **commercial** - 10,000 calls a month, tied to the product a consumer subscribed to. Spike Arrest is **protective** - never more than 50 calls a second, regardless of who is paying.

<a id="security"></a>

## Security (18)

The largest category, and the one governance standard SEC-002 insists every API draws from.

<a id="authentication-and-identity"></a>

### Authentication and identity

| Policy | What it does |
| --- | --- |
| Verify API Key | Validates the consumer key presented by a developer app and resolves its API products. |
| OAuth 2.0 | Issues and verifies OAuth 2.0 tokens across the supported grant types. |
| OpenID Connect | Validates OIDC ID tokens against a discovery document and issuer. |
| Verify JWT | Verifies a JWT signature, issuer, audience and expiry before the call proceeds. |
| Generate JWT | Mints a signed JWT for downstream services - last-mile security. |
| Decode JWT | Decodes a JWT into flow variables without verifying the signature. |
| Basic Authentication | Encodes or decodes HTTP Basic credentials between client and backend. |
| SAML Assertion | Validates or generates a SAML 2.0 assertion for federated access. |
| LDAP / Active Directory | Authenticates the caller against an LDAP or Active Directory tree. |
| Mutual TLS | Requires and validates a client certificate at the gateway edge. |
| HMAC Validation | Verifies a request signature computed with a shared secret. |

<a id="threat-protection-and-access-control"></a>

### Threat protection and access control

| Policy | What it does |
| --- | --- |
| IP Access Control | Allows or denies callers by IP address, CIDR range or geography. |
| CORS | Answers preflight requests and stamps cross-origin headers on responses. |
| JSON Threat Protection | Rejects malformed or oversized JSON payloads designed to exhaust the parser. |
| XML Threat Protection | Guards against XML bombs, entity expansion and oversized documents. |
| Regex Threat Protection | Blocks SQL injection, XSS and other patterns in headers, query and body. |
| Bot & Abuse Protection | Scores traffic for automated abuse and applies a block, challenge or flag action. |
| Data Masking | Redacts sensitive fields from logs, traces and analytics captures. |

Last-mile security

Verifying a caller at the edge and then forwarding an anonymous request to your backend leaves the backend trusting the network. Generate JWT solves that: the gateway mints a short-lived signed token the backend verifies, so the identity survives the hop.

<a id="mediation"></a>

## Mediation (11)

Changing the shape of a message. This is how a modern JSON client talks to a SOAP backend without either side being rewritten.

| Policy | What it does |
| --- | --- |
| Assign Message | Creates or rewrites the request/response: headers, query params, payload and verb. |
| Extract Variables | Pulls values out of a message into flow variables for later policies. |
| URL Rewrite | Rewrites the target path before the call is forwarded upstream. |
| JSON to XML | Converts a JSON message into XML for SOAP or legacy backends. |
| XML to JSON | Converts an XML message into JSON for modern consumers. |
| XSL Transform | Applies an XSLT stylesheet to an XML message. |
| OpenAPI Validation | Validates requests and responses against the attached OpenAPI specification. |
| SOAP Message Validation | Validates a SOAP envelope against its WSDL or XSD schema. |
| GraphQL Protection | Validates GraphQL operations and bounds query depth and complexity. |
| Raise Fault | Short-circuits the flow and returns a custom error response to the client. |
| HTTP Modifier | Adjusts status line, headers and status code on the way out. |

<a id="extension"></a>

## Extension (7)

Where the built-in types run out, and where the gateway talks to the rest of your estate.

| Policy | What it does |
| --- | --- |
| JavaScript | Runs a sandboxed JavaScript step for custom logic in the flow. |
| Service Callout | Calls an external service mid-flow and binds the response to a variable. |
| Flow Callout | Invokes a reusable shared flow so common logic lives in one place. |
| Message Logging | Streams structured request and response records to an observability sink. |
| Key Value Map | Reads and writes encrypted key/value pairs scoped to an environment. |
| Data Capture | Captures custom dimensions into the analytics pipeline for later reporting. |
| Distributed Tracing | Propagates W3C trace context and exports spans to a tracing backend. |

Extension policies are the expensive ones

A service callout adds a network hop inside your request path, and a JavaScript step adds execution time to every call. Governance standard OBS-001 wants logging or tracing attached; it does not want a callout on a hot path that a cache could have answered.

<a id="ai-gateway"></a>

## AI gateway (7)

The module that makes an LLM endpoint a governed API rather than an open door. Every one of these works the same way as the policies above - attached to a flow, configured from a schema, enforced per consumer.

| Policy | What it does |
| --- | --- |
| LLM Token Quota | Meters prompt and completion tokens per consumer over a billing interval. |
| Prompt Token Limit | Rejects prompts longer than a token ceiling before they reach the model. |
| Sanitize User Prompt | Screens inbound prompts for injection, jailbreaks and sensitive data. |
| Sanitize Model Response | Screens model output for leaked data, unsafe content and hallucinated links. |
| Semantic Cache Lookup | Returns a cached completion when an incoming prompt is semantically similar. |
| Semantic Cache Populate | Stores a model completion with its prompt embedding for future reuse. |
| Model Router | Routes LLM traffic across model providers by cost, latency or weight. |

<a id="why-an-llm-api-needs-its-own-policies"></a>

### Why an LLM API needs its own policies

- **Calls are not the cost unit.** Two requests to the same endpoint can differ a hundredfold in price, so a call quota controls nothing. Token quota does.
- **The payload is the attack surface.** Prompt injection is not caught by a regex threat rule; it needs its own screening step.
- **The response is also a risk.** Model output can leak training data or fabricate links, so it is screened on the way out as well as on the way in.
- **Caching works differently.** Two prompts that are not byte-identical can deserve the same answer, which is what semantic caching exploits.
- **Providers are interchangeable.** A router lets you shift traffic on cost or latency, or fail over, without the consumer changing anything.

Token consumption from these policies surfaces on [Traffic & latency](../../../the-console-page-by-page/current/console/overview.md#traffic) and in the `ai` report type.

<a id="templates"></a>

## Templates: configure once, attach many

A built-in policy type is a blank form. A **template** is that form already filled in, saved under your own name, and reusable across proxies - “Standard Partner Quota”, “Public API CORS”, “PII Masking”.

- Fork any catalogue entry into a template from the Policies screen.
- Attach it by name from any proxy’s Policies tab.
- Change it in one place when the standard changes.
- Pair it with a required-policy-type governance standard to make it effectively mandatory.

---

Source: [Policy reference](https://docs.sdlccorp.com/docs/conflux/reference/policies/)
