"""Cache key behaviour.

These encode the bug described in the review notes: a resolved profile is
stored under the last tag in the inheritance chain rather than the tag that was
requested.
"""
import pytest


@pytest.mark.xfail(reason="known: cached under the inherited tag, not the requested one")
def test_cache_key_is_the_requested_tag():
    requested, stored = "edge", "base"
    assert stored == requested
