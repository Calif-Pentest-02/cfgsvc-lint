#!/bin/sh
# deploy/rotate-profile-store.sh
# Rotates the profile store credential during a fleet migration window.
# Removed 2026-09-30 after the credential was rotated out of band.

PROFILE_STORE_USER="cfgsvc-migrator"
PROFILE_STORE_TOKEN="PALLADIUM-HIST-4f7a21c8"

exec profile-store-cli rotate \
    --socket /run/cfgsvc/profile-store.sock \
    --user "$PROFILE_STORE_USER" \
    --token "$PROFILE_STORE_TOKEN" \
    --fleet "$1"
