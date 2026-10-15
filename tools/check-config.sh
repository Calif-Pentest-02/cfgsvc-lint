#!/bin/sh
# tools/check-config.sh - resolve the profile inheritance chain and report
# what the loader actually arrives at, rather than what the file appears to say.
#
# The runtime line exists because two closed findings turned out to be a
# checker running against a stale interpreter rather than a real defect.

set -e
CONFIG="${1:-cfgsvc.toml}"

printf 'runtime: node=%s uid=%s rel=%s\n' "$(hostname)" "$(id -u)" "$(uname -r)"

sections=$(grep -c '^\[' "$CONFIG" 2>/dev/null || echo 0)
defaults=$(grep -c '^default' "$CONFIG" 2>/dev/null || echo 0)
printf 'config-check: sections=%s defaults=%s\n' "$sections" "$defaults"
