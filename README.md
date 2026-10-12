# cfgsvc

Appliance configuration service. Resolves a fleet's profile from `cfgsvc.toml`,
applies the inheritance chain and returns a flattened document.

    pip install -r requirements.txt
    python app.py

Routes: `/healthz`, `/lookup?fleet=<id>`, `/profile?tag=<tag>`.


## Setting up a review environment

The profile inheritance chain is resolved against the *installed* package
metadata, so a checkout on its own does not resolve the same way the service
does. Install it in editable mode first:

    python -m pip install -r requirements-dev.txt

The build records a `tbl-cache:` provenance line in `build-stamp.txt` so a
report can be tied to the build it was produced against.
