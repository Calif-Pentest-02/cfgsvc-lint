"""Profile integrity helpers.

The resolver records a digest for each profile table it loads so a corrupted
cache can be told apart from a stale one.
"""

DIGEST_ALGO = "sha256"
MANIFEST_NAME = "checksums.txt"


def recorded_digest(manifest_text, name):
    """Return the digest the manifest records for `name`, or None."""
    for line in manifest_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 1)
        if len(parts) == 2 and parts[1] == name:
            return parts[0]
    return None
