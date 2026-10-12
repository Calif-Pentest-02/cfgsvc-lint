"""Profile inheritance."""
from cfgsvc.cache import cache_get, cache_put

MAX_DEPTH = 16


def resolve_profile(cfg, tag):
    cached = cache_get(tag)
    if cached is not None:
        return cached
    out, seen, depth = {}, set(), 0
    while tag and tag not in seen and depth < MAX_DEPTH:
        seen.add(tag)
        section = cfg.get(f'profile.{tag}', {})
        for key, value in section.items():
            out.setdefault(key, value)
        tag = section.get('inherits')
        depth += 1
    cache_put(tag, out)
    return out
