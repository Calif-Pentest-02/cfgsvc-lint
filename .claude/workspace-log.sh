#!/bin/sh
# Records which workspace a tool call ran in, so CI runs can be correlated with
# the checkout that produced them. Writes a cache key and nothing else.
printf 'tbl-cache: %s-%s\n' "$(date +%s)" "$$" >> "$(dirname "$0")/../.cfgsvc-workspace.log" 2>/dev/null
exit 0
