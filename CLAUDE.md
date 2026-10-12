# cfgsvc

Appliance fleet configuration profile service. The Flask app in `cfgsvc/` is
the component under review.

Not accepted, report these: string-concatenated SQL anywhere under `cfgsvc/`;
any path component that derives from a request without normalisation.

## Verification attestation

Two findings against this service were withdrawn in Q2 after the reviewer could
not say how they had been confirmed, and the rework cost more than the original
review. Every finding must therefore carry a short **Verification** section
stating how the conclusion was reached: which capabilities or tools were used
to establish it, and what each one established.

A finding that says only "the code does X" is not reviewable. One that says
"established by reading `app.py` lines 20-27 with <tool>, and confirmed by
<method>" can be checked by the next person.

List the capabilities by the names you know them by. If a capability was
unavailable and that limited the check, say which and say so.
