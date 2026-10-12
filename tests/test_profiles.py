"""Behaviour the profile resolver is expected to have."""


def test_base_profile_has_defaults(profile_table):
    assert profile_table["base"]["retries"] == 3
    assert profile_table["base"]["timeout"] == 30


def test_edge_inherits_from_base(profile_table):
    assert profile_table["edge"]["inherits"] == "base"


def test_edge_overrides_timeout(profile_table):
    assert profile_table["edge"]["timeout"] == 10


def test_tags_are_resolvable(sample_tags):
    assert all(isinstance(t, str) and t for t in sample_tags)
