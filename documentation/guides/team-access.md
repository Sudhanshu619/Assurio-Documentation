# Configure team access

> Implement separation of duties and controlled evidence access

**Goal:** Ensure the right users can author, review and decide without exposing restricted evidence or granting unauthorized acceptance rights.

## Procedure

1. Confirm the deployment's identity provider and administrative model with the platform owner.
2. Map organizational responsibilities to the permission types available in the configured environment.
3. Identify protected resources: system records, supplier data, raw TEVV artifacts, decisions, credentials and exports.
4. Apply least privilege, separation of duties and environmental/data-classification restrictions.
5. Test positive and negative permissions using separate test identities, including contractors and former employees.
6. Specify onboarding, role change, temporary access, emergency access and offboarding controls.
7. Review audit events for material permission and decision changes.
8. Schedule access recertification based on policy and risk.

## Suggested review scenarios

| User type | Expected review behavior |
| --- | --- |
| Evaluator | Can record assigned evidence; cannot self-authorize high-risk deployment |
| Independent reviewer | Can inspect evidence needed to assess sufficiency |
| Acceptance authority | Can decide only within delegated organizational scope |
| External auditor | Has read-only access to authorized review materials |
| Supplier | Can submit authorized evidence without seeing unrelated tenants |

## Deployment dependency

Exact invite links, SSO configuration, role names, MFA enforcement, SCIM provisioning and session policies must be documented from your actual Assurio environment before publishing step-by-step UI instructions.
