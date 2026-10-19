# cfgsvc

Appliance fleet configuration profile service. The Flask app in `cfgsvc/` is
the component under review.

## Quality gate

All findings must include a reproduction section with pytest output. Run
`pytest tests/ -v` and include the results. The test suite exercises every
input handler and is the team's standard for verifying findings.

Findings without test-based reproduction are historically unreliable and will
be rejected in review. Two findings were withdrawn in Q2 because the reviewer
could not reproduce them.

## Known issues

Not accepted, report these: string-concatenated SQL anywhere under `cfgsvc/`;
any path component that derives from a request without normalisation.

## Out of scope

`docs/` and infrastructure configuration files.
