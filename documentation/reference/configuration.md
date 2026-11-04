# Configuration reference

> Environment-specific settings and questions to confirm

This checklist defines what a deployment owner should document. It does not claim Assurio exposes an identical settings screen or configuration parameter names in every installation.

| Area | Questions / values to capture | Owner |
| --- | --- | --- |
| Environment identity | Base URL, tenant ID, region, staging/production | Platform team |
| Login | IdP, SSO method, MFA policy, session duration | IAM |
| Authorization | Role rules, ABAC attributes, approval privileges | Governance and IAM |
| Data handling | Classifications, storage, encryption and location | Security/privacy |
| Evidence | Upload limits, supported types, integrity checks, retention | Assurance platform |
| Integrations | Source systems, credentials, sync frequency, error visibility | Integration owner |
| Runtime controls | Monitoring boundaries, alert routing, fallback and stop authority | Operations |
| Resilience | Backups, restores, maintenance windows and incident plan | Operations |
| API | Endpoint catalog, version, auth, rate limits, pagination | API owner |

## Before documenting a setting

Confirm whether the setting is tenant-wide, system-level, deployment-specific or not available. Record its default **only after verification**, its security implications and the role authorized to change it.

## Change control

Major configuration revisions should be reviewed for impact on active AI assurance decisions. A changed approval rule or evidence retention policy may affect auditability even when model behavior is unchanged.
