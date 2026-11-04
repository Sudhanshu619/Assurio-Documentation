# API reference

> Integration guidance and specification-ready contracts

Assurio describes integration with model registries, MLOps, requirements systems, testing, observability, simulation, GRC and enterprise applications. **The public product site does not disclose authenticated API endpoints, a base URL, an OpenAPI document, versioning rules, API keys, rate limits or webhook event names.**

This section is intentionally organized as an **integration design reference**, not a fabricated executable API. It gives developers a structured contract to complete using an authoritative Assurio API specification.

## Developer starting points

| Page | Purpose |
| --- | --- |
| [Authentication](authentication.md) | Questions and safeguards for credentials and access |
| [Resource model](objects.md) | Logical objects to exchange with external systems |
| [Contract design](contract-design.md) | Endpoint specification worksheet and sample payload shapes |
| [Webhooks and events](webhooks.md) | Event semantics and delivery guarantees to define |
| [Errors and limits](errors-and-limits.md) | Standard error-handling requirements to confirm |

## Do not use example code as a live API client

Examples in this section are labeled **proposed / illustrative**. Before publishing a runnable SDK tutorial, obtain an official OpenAPI or equivalent schema, confirmed tenant hostnames and auth mechanism, and integration permissions. Never invent paths like `/v1/systems` and present them as existing product routes.

For operational design, see [Integration guide](../documentation/guides/integrations.md).
