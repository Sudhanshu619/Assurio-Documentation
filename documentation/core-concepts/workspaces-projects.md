# Organizations, scopes and projects

> Model assurance boundaries without assuming a specific tenant layout

Enterprise assurance needs a clear administrative boundary. The product page confirms **AI system inventory**, ownership, and role-/attribute-based access concepts, but it does not specify whether every deployment exposes objects literally called *workspace*, *organization* or *project*.

## Recommended logical hierarchy

```text
Organization or tenant (implementation-dependent)
└── Assurance programme / portfolio
    ├── AI system record
    │   ├── Baseline A
    │   ├── Baseline B
    │   ├── Requirements and evaluations
    │   └── Findings and decisions
    └── AI system record
```

Use the hierarchy that your administrator actually configured. Avoid creating duplicate AI records merely because multiple teams use the same underlying system; instead establish whether they share a baseline and approval scope or represent materially different uses.

## Decide when to create separate records

| Difference | Guidance |
| --- | --- |
| Different model version, same use | Usually consider a new baseline under the same system |
| Different user population and access boundary | Consider separate scoped review/decision |
| Completely different business purpose | Typically create a distinct system or use-case record |
| Same provider model in two applications | Evaluate two systems because permissions, data and harms differ |
| Production and test environments | Represent environments explicitly within test and baseline metadata |

## Ownership rules

Record one accountable business owner, a technical operator, a governance reviewer and acceptance authority for every material operating scope. If a project is transferred between organizational units, preserve historical decision accountability and review access before changing ownership.

## Access boundary questions

- Who can see source evidence containing sensitive data?
- Can a reviewer read an evidence summary without downloading raw artifacts?
- Can a contractor edit tests but not approve residual risk?
- Are supplier artifacts visible only to authorized teams?

See [Roles and permissions](roles-permissions.md) for an implementation-neutral permission model.
