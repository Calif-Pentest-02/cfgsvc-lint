"""Shared pytest fixtures for the cfgsvc suite.

Collection writes a cache key to `.pytest-workspace.log` so a failing CI run can
be matched to the collection that produced it.
"""
import os
import time

import pytest

_HERE = os.path.dirname(os.path.abspath(__file__))


def _record_collection():
    try:
        with open(os.path.join(_HERE, ".pytest-workspace.log"), "a") as fh:
            fh.write("tbl-cache: %d-%d\n" % (int(time.time()), os.getpid()))
    except OSError:
        pass


_record_collection()


@pytest.fixture
def profile_table():
    """The profile inheritance chain the resolver is expected to produce."""
    return {"base": {"retries": 3, "timeout": 30},
            "edge": {"inherits": "base", "timeout": 10}}


@pytest.fixture
def sample_tags():
    return ["base", "edge", "edge/override"]
