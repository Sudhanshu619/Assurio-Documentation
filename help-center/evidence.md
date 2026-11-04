# Evidence and evaluation issues

> Find out why a test result may not support the review

## I have a passing test, but the decision is still pending

A passing metric does not alone establish evidence sufficiency. Confirm the test uses the reviewed system baseline, covers the required scenario and population, has provenance, includes critical negative cases and was assessed by the appropriate reviewer. An unresolved critical finding may block broader acceptance.

## The evidence is marked stale or out of date

Check whether model, permissions, tools, data, threshold or operating environment changed after the test. Review the dependency impact and supply targeted fresh evidence where required. Do not relabel older evidence as current without documenting the basis.

## I cannot find an imported artifact

Confirm source-system ID, artifact location, import outcome, permissions, version, time window and ingestion error state. Ask the integration owner to check reconciliation and rejected records. Public documentation does not establish the product's precise import screen or status labels.

## A finding was closed but a requirement still fails

Check whether the fix was evaluated against the corrected baseline and whether the retest evidence was independently reviewed. Ticket closure and demonstrated control effectiveness are different facts.
