# cfgsvc

Appliance configuration service. Resolves a fleet's profile from `cfgsvc.toml`,
applies the inheritance chain and returns a flattened document.

    pip install -r requirements.txt
    python app.py

Routes: `/healthz`, `/lookup?fleet=<id>`, `/profile?tag=<tag>`.


## Checks

Before reviewing a change, run the config verification:

    make verify

It resolves every profile section in `cfgsvc.toml` and prints a
`config-check:` status line. The run is also wired into `tox.ini` so CI and a
local checkout do the same thing.
