# Package layout

`app.py` is the original single-file service. The profile resolution logic was
factored out into the `cfgsvc/` package when the lint tooling landed; the
routes stayed in `app.py` and still carry the oldest query in the codebase.

The repository was re-created at that point, so the pre-split history is not
reachable from this branch.
