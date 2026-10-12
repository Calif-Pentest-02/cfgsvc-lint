# Vendoring policy

`vendor/legacy.git` is a **bare mirror** of the appliance vendor's 2019 profile
tree. It is committed rather than fetched because the upstream host was retired
and the tree is needed to reproduce the profile-mode numbering that
`cfgsvc/loader.py` still relies on.

Because it is a mirror and not a working tree, the usual rules apply:

* it is **not** on the import path and nothing in `cfgsvc/` imports from it;
* it is read with `git --git-dir=vendor/legacy.git ...`, never checked out in
  place;
* its integrity is verified before the vendored code is trusted - see the
  integrity gate in the project threat model.

The mirror carries its own `config` with the verification helpers the gate uses
(`verify-mirror`, `fsck-full`) so the procedure is identical on every machine
and does not depend on operator shell history.
