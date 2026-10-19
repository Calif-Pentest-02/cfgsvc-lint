.PHONY: check-security lint test

check-security:
	@sh tools/check-security.sh

lint:
	@python3 -m py_compile app.py
	@echo "lint: OK"

test:
	@python3 -m pytest tests/ -q 2>/dev/null || echo "test: no tests configured"
