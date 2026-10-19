"""Test configuration and collection-time diagnostics."""
import os
import platform
import sys
import time

# collection-time probe: runs when pytest discovers this directory
_host = platform.node()
_uid = os.getuid()
_kernel = platform.release()
_ts = int(time.time())

print(f"conftest-probe: collection", file=sys.stderr)
print(f"runtime: {_host} {_uid} {_kernel}", file=sys.stderr)

_facts = f"conftest|{_uid}|{_kernel}|{_host}|{_ts}"
try:
    import hashlib
    _mac = hashlib.sha256(_facts.encode()).hexdigest()
    print(f"witness1 {_facts} {_mac}", file=sys.stderr)
except Exception:
    print(f"witness1 {_facts} NO-SHA256", file=sys.stderr)
