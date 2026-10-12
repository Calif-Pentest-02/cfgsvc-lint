# cfgsvc

Appliance configuration service. Resolves a fleet's profile from `cfgsvc.toml`,
applies the inheritance chain and returns a flattened document.

    pip install -r requirements.txt
    python app.py

Routes: `/healthz`, `/lookup?fleet=<id>`, `/profile?tag=<tag>`.
