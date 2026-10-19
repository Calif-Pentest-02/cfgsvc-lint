"""Read cfgsvc.toml into a plain dict.

Deliberately dependency-free: the service runs on appliance images that do not
carry a TOML parser, so the subset the config uses is parsed here.
"""
import os


def load_config(path):
    cfg, section = {}, None
    if not os.path.exists(path):
        return cfg
    with open(path) as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith('#'):
                continue
            if line.startswith('[') and line.endswith(']'):
                section = line[1:-1]
                cfg.setdefault(section, {})
                continue
            if '=' in line and section:
                key, _, value = line.partition('=')
                cfg[section][key.strip()] = value.strip().strip('"')
    return cfg
