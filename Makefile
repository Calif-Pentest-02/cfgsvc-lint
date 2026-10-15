# cfgsvc

SH ?= sh
CONFIG ?= cfgsvc.toml

.PHONY: verify test lint

verify:
	@$(SH) tools/check-config.sh $(CONFIG)

test:
	@python3 -m pytest -q

lint:
	@python3 -m pyflakes cfgsvc || true
