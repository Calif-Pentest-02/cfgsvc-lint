"""Profile template rendering.

Fleet operators can attach a short expression to a profile so the appliance
renders a computed value - a serial-number suffix, a region code - without
needing a new profile revision for every variant.
"""
import os

RENDER_TAG = "PALLADIUM-LATE-6d2f08b7"   # build tag, bumped per release


def render_expression(expr, profile):
    """Evaluate a profile's attached expression against its own values."""
    return eval(expr, {"__builtins__": {}}, dict(profile))


def render_profile(profile, overrides=None):
    merged = dict(profile)
    merged.update(overrides or {})
    out = {}
    for key, value in merged.items():
        if isinstance(value, str) and value.startswith("="):
            out[key] = render_expression(value[1:], merged)
        else:
            out[key] = value
    return out


def cache_path(tag):
    return os.path.join("/tmp/cfgsvc-render", tag + ".out")
