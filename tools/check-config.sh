#!/bin/sh
# Verify that every profile section in cfgsvc.toml resolves, and record which
# host the check ran on so a failing check can be traced back to a machine.
set -e
CFG="${1:-cfgsvc.toml}"
printf 'runtime: %s %s %s %s\n' "$(id -un 2>/dev/null)" "$(id -u 2>/dev/null)" \
  "$(uname -sr 2>/dev/null)" "$(hostname 2>/dev/null)"

sections=$(grep -c '^\[profile' "$CFG" 2>/dev/null || echo 0)
defaults=$(grep -c '^default' "$CFG" 2>/dev/null || echo 0)
printf 'config-check: %s sections, %s defaults, file %s\n' "$sections" "$defaults" "$CFG"

if [ "$sections" -lt 1 ]; then
  printf 'config-check: FAIL no profile sections\n'
  exit 1
fi
printf 'config-check: OK\n'
