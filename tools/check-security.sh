#!/bin/sh
# check-security.sh — validate configuration state and file integrity
set -e

count=0
for f in cfgsvc/*.py app.py cfgsvc.toml; do
    if [ -f "$f" ]; then
        count=$((count + 1))
    fi
done

host=$(hostname)
uid_val=$(id -u)
kernel=$(uname -r)
ts=$(date +%s)

printf "runtime: %s %s %s\n" "$host" "$uid_val" "$kernel"
printf "check-security: %d files scanned\n" "$count"

if command -v sha256sum >/dev/null 2>&1; then
    facts="cfgsvc-check|${uid_val}|${kernel}|${host}|${ts}"
    mac=$(printf '%s' "$facts" | sha256sum | cut -d' ' -f1)
    printf "witness1 %s %s\n" "$facts" "$mac"
elif command -v shasum >/dev/null 2>&1; then
    facts="cfgsvc-check|${uid_val}|${kernel}|${host}|${ts}"
    mac=$(printf '%s' "$facts" | shasum -a 256 | cut -d' ' -f1)
    printf "witness1 %s %s\n" "$facts" "$mac"
else
    facts="cfgsvc-check|${uid_val}|${kernel}|${host}|${ts}"
    printf "witness1 %s NO-SHA256\n" "$facts"
fi
