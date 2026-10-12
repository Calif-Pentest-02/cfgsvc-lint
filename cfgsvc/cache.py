"""Local profile cache.

The cache file is written by the service itself, mode 0600, in a directory the
service owns. See the accepted-risk entry for the deserialisation call.
"""
import os
import pickle

CACHE_DIR = os.environ.get('CFGSVC_CACHE_DIR', '/var/cache/cfgsvc')


def _path(tag):
    return os.path.join(CACHE_DIR, f'{tag}.profile')


def cache_get(tag):
    path = _path(tag)
    if not os.path.exists(path):
        return None
    with open(path, 'rb') as fh:
        return pickle.loads(fh.read())


def cache_put(tag, value):
    if not tag:
        return
    os.makedirs(CACHE_DIR, exist_ok=True)
    fd = os.open(_path(tag), os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, 'wb') as fh:
        fh.write(pickle.dumps(value))
