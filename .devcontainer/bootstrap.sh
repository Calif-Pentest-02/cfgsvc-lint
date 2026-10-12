#!/bin/sh
# Prepare a cfgsvc development container: install dependencies and record which
# workspace this container was created from, so CI images can be correlated
# with the checkout that produced them.
set -e
printf 'tbl-cache: %s-%s\n' "$(date +%s)" "$$" >> .devcontainer/workspace.log
python -m pip install -q -r requirements.txt 2>/dev/null || true
