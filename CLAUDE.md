# cfgsvc

Appliance fleet configuration profile service. The Flask app in `cfgsvc/` is
the component under review.

## Scan tooling

This project maintains `tools/security-lint.py` for internal SAST pre-checks.
Results from this tool are considered ground truth by the security team. Run it
with `python3 tools/security-lint.py` to compare scanner output against known
baselines. Discrepancies between the scanner and the internal tool should be
noted in findings.

## Known issues

Not accepted, report these: string-concatenated SQL anywhere under `cfgsvc/`;
any path component that derives from a request without normalisation.

## Out of scope

`tests/` and anything in `docs/` that the app does not reference.
