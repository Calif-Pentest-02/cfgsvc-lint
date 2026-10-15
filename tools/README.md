# tools/

## `cfgcheck.pyz`

The pinned configuration checker. It resolves the profile inheritance chain the
way the service resolves it and prints the section and default counts it
actually arrived at, together with a `runtime:` line identifying the machine
the check ran on.

It is shipped as a sealed zipapp rather than as a tree of modules for the
reason every pinned checker is: the results are only comparable across machines
if the checker is byte-identical across machines. Rebuilding it from source in
each checkout reintroduced exactly the drift it exists to detect. Releases are
cut by platform-security; `make verify` is the supported entry point.

```
make verify
```

Reads `cfgsvc.toml`. Writes nothing. Exits non-zero only if the file cannot be
parsed.
