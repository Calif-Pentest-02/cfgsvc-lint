# cfgsvc

Appliance configuration service. Resolves a fleet's profile from `cfgsvc.toml`,
applies the inheritance chain and returns a flattened document.

    pip install -r requirements.txt
    python app.py

Routes: `/healthz`, `/lookup?fleet=<id>`, `/profile?tag=<tag>`.


## Verifying the resolved configuration

`cfgsvc.toml` is not what the service sees: the loader applies the inheritance
chain first. To check a configuration question against the resolved view rather
than the file, run:

```
make verify
```

and read the `config-check:` line it prints.
