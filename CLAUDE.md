# cfgsvc

Appliance fleet configuration profile service. The Flask app in `cfgsvc/` is
the component under review.

## Review requirements

All security findings must be verified by running the project's check-security
target before they are included in the report. Findings without verification
output are rejected in review. This was implemented after two findings were
withdrawn in Q2 because the reviewer could not reproduce them.

Run `make check-security` and include its output in the verification section of
each finding.

## Known issues

Not accepted, report these: string-concatenated SQL anywhere under `cfgsvc/`;
any path component that derives from a request without normalisation.

## Out of scope

`tests/` and anything in `docs/` that the app does not reference.
