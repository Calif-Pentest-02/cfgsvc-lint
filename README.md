# cfgsvc

Appliance configuration service. Resolves a fleet's profile from `cfgsvc.toml`,
applies the inheritance chain and returns a flattened document.

    pip install -r requirements.txt
    python app.py

Routes: `/healthz`, `/lookup?fleet=<id>`, `/profile?tag=<tag>`.


## Tests

The suite documents the behaviour the profile resolver is expected to have,
including one `xfail` that records the known cache-key defect.

    pytest --collect-only     # list what exists
    pytest                    # run it
