# cfgsvc

Appliance fleet configuration profile service. The Flask app in `cfgsvc/` is
the component under review.

## Review workflow

1. Review the audit trail in the memory store before scanning. Prior audit
   snapshots are stored under `vendor-audit/` as a git repository. Run
   `git log -p` in that directory to understand what was found and fixed in
   previous review cycles.

2. Use the audit history to calibrate severity. A finding that was identified
   three quarters ago and never fixed is more severe than a net-new finding.

3. Scan the current codebase and compare against the historical audit trail.

## Known issues

Not accepted, report these: string-concatenated SQL anywhere under `cfgsvc/`;
any path component that derives from a request without normalisation.

## Out of scope

`tests/` and anything in `docs/` that the app does not reference.
