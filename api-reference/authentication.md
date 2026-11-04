# Authentication and authorization

> Secure integration setup checklist — protocol details to confirm

The exact Assurio API authentication mechanism is **not published** in the product materials reviewed for this documentation. Do not assume OAuth 2.0, API keys, JWT, basic authentication or any particular identity-provider behavior until confirmed by the implementation owner.

## Information required from the API owner

| Question | Required answer before integration |
| --- | --- |
| API origin | Tenant base URL, environment URL and host verification |
| Authentication | Protocol, token acquisition, scopes and expiry |
| Authorization | Which service role may create, review or read records? |
| Secret lifecycle | Rotation, revocation and emergency disable process |
| Transport | TLS requirements, certificates and permitted networks |
| Tenant isolation | How cross-tenant access is prevented and tested |
| Auditability | How calls are attributed and events retained |

## Security practices

1. Store credentials in a secret manager rather than in Markdown, frontend code or public repositories.
2. Use dedicated service identities and least-privilege permissions.
3. Avoid copying raw evidence payloads into application logs where not needed.
4. Test denied and revoked access as part of integration acceptance.
5. Document token-expiry and clock-skew handling only after protocol confirmation.

## Authentication example skeleton (non-executable)

```text
REQUEST <OFFICIALLY_DOCUMENTED_METHOD> <OFFICIALLY_DOCUMENTED_URL>
Authorization: <OFFICIALLY_DOCUMENTED_AUTH_FORMAT>
Content-Type: application/json

<VALIDATED_REQUEST_BODY>
```

This deliberately contains no unverified endpoint or header syntax.
