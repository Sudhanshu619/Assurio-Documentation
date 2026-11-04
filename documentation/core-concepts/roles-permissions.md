# Roles and permissions

> Separate authoring, reviewing and approving authority

Assurio's public description refers to role-based and attribute-based permissions, ownership and accountable acceptance. The exact predefined roles, menu names and authorization matrix depend on the environment; the following is a **recommended governance model**, not an assertion of built-in role names.

## Suggested functional roles

| Function | Responsibility | Should not automatically imply |
| --- | --- | --- |
| Platform administrator | Tenant configuration, integrations, access policy | Acceptance authority |
| Business/system owner | Defines purpose, use, impact and constraints | Independent evidence review |
| Engineering owner | Maintains baseline, tools, configuration | Unilateral residual-risk acceptance |
| Risk reviewer | Reviews risk register, mitigations, exceptions | Production release authority |
| TEVV evaluator | Produces test plans/results | Independent approval of own evidence |
| Assurance reviewer | Challenges completeness and quality | Automatic deployment rights |
| Acceptance authority | Approves, restricts or rejects an operating scope | Ability to suppress adverse evidence |
| Auditor/read-only reviewer | Inspects history and provenance | Editing or decision authority |

## Principle of least privilege

Grant the minimum read/write/approve actions required for each role, and constrain sensitive artifacts by data classification, project, environment and purpose. Where separation of duties is mandatory, ensure the evidence author cannot silently certify their own findings or decision.

## Authorization design checklist

1. Define actors, objects and actions (read, create, modify, review, decide, export, administer).
2. Specify attributes (department, data classification, country, environment, review phase).
3. Set rules for external suppliers and temporary access.
4. Require identity attribution and audit logging for material changes.
5. Establish emergency access, expiration and periodic access recertification.
6. Test denied operations, not just successful operations.

**Critical:** A governance decision is invalid if recorded by someone outside the organization's delegated authority, regardless of UI access. Application permission and organizational authorization are separate checks.
