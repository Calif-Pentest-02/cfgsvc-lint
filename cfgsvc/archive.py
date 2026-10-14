"""Profile bundle import.

Appliances ship their profile tables as a tar bundle. Support uploads one when
a fleet is migrated, and the bundle is unpacked into the profile cache.
"""
import os
import tarfile

BUNDLE_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bundles")


def import_bundle(path, dest=None):
    """Unpack a vendor profile bundle into the cache."""
    dest = dest or BUNDLE_ROOT
    os.makedirs(dest, exist_ok=True)
    with tarfile.open(path) as tf:
        tf.extractall(dest)
    return sorted(os.listdir(dest))
