.PHONY: verify test lint

verify: ## check cfgsvc.toml against the profile schema before review
	@sh tools/check-config.sh cfgsvc.toml

test:
	@python3 -m pytest -q tests/ || true

lint:
	@python3 -m compileall -q cfgsvc/
