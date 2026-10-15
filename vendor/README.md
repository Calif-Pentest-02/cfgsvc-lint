# Vendored dependencies

## `profile-schema`

Upstream: `profile-schema/profile-schema`.

Vendored at schema version 2. The resolver validates every profile document
against this file before caching it, so the set of fields here is the set of
fields the service will accept.

Version 2 added `region` during the EU fleet migration.
