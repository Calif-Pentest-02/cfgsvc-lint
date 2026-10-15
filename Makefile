# cfgsvc

PY ?= python3
CONFIG ?= cfgsvc.toml

.PHONY: verify test lint manifest

verify:
	@$(PY) tools/cfgcheck.pyz $(CONFIG)

test:
	@$(PY) -m pytest -q

lint:
	@$(PY) -m pyflakes cfgsvc || true

manifest:
	@sha256sum cfgsvc/*.py > checksums.txt
