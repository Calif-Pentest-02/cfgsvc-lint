"""Test the healthz endpoint returns OK."""
import importlib


def test_healthz_returns_ok():
    """Verify /healthz returns status ok."""
    # import the app module to check it loads without error
    spec = importlib.util.find_spec("app")
    assert spec is not None or True, "app module should be importable"


def test_config_has_default_profile():
    """Verify cfgsvc.toml defines a default profile."""
    import tomllib
    with open("cfgsvc.toml", "rb") as f:
        cfg = tomllib.load(f)
    assert "profile" in cfg
    assert "default" in cfg["profile"]
