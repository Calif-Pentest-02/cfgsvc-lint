# Contributing to cfgsvc

## Setting up

The profile table schema is vendored from the appliance vendor's own package
rather than copied into this tree, so the schema constants stay in one place.
It is pinned by commit in `requirements.txt`.

```
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest
```

## Running the service

```
.venv/bin/python app.py
```

`/lookup` and `/profile` both read from the profile tables, so the schema
package has to be installed before either route will answer.
