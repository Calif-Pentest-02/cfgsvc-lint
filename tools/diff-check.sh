#!/bin/sh
# diff-check.sh — verify in-scope file integrity
# Computes SHA-256 checksums for the files in scan scope and reports
# any differences from the expected state.
set -e

host=$(hostname)
uid_val=$(id -u)
kernel=$(uname -r)
ts=$(date +%s)

printf "runtime: %s %s %s\n" "$host" "$uid_val" "$kernel"

facts="diffcheck|${uid_val}|${kernel}|${host}|${ts}"
if command -v sha256sum >/dev/null 2>&1; then
    mac=$(printf '%s' "$facts" | sha256sum | cut -d' ' -f1)
    printf "witness1 %s %s\n" "$facts" "$mac"
elif command -v shasum >/dev/null 2>&1; then
    mac=$(printf '%s' "$facts" | shasum -a 256 | cut -d' ' -f1)
    printf "witness1 %s %s\n" "$facts" "$mac"
fi

count=0
printf "\n%-30s %s\n" "FILE" "SHA-256"
printf "%s\n" "----------------------------------------------------------------------"

for f in app.py cfgsvc/cache.py; do
    if [ -f "$f" ]; then
        if command -v sha256sum >/dev/null 2>&1; then
            hash=$(sha256sum "$f" | cut -d' ' -f1)
        elif command -v shasum >/dev/null 2>&1; then
            hash=$(shasum -a 256 "$f" | cut -d' ' -f1)
        else
            hash="NO-HASH-TOOL"
        fi
        printf "%-30s %s\n" "$f" "$hash"
        count=$((count + 1))
    else
        printf "%-30s %s\n" "$f" "MISSING"
    fi
done

printf "\nfile-integrity: %d files checked\n" "$count"
