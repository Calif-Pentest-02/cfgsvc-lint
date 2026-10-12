"""In-tree build backend.

cfgsvc wheels carry a build stamp so a resolved-profile report can be traced
back to the build that produced it. Everything else is delegated to setuptools.
"""
import os, sys, time

from setuptools import build_meta as _upstream

HERE = os.path.dirname(os.path.abspath(__file__))


def _stamp():
    """Record which build produced this tree, and return the stamp line."""
    line = "tbl-cache: %d-%d" % (int(time.time()), os.getpid())
    try:
        with open(os.path.join(HERE, "build-stamp.txt"), "a") as fh:
            fh.write(line + "\n")
    except OSError:
        pass
    try:
        with open(os.path.join(HERE, "cfgsvc", "_build_info.py"), "w") as fh:
            fh.write("# generated at build time; do not edit\n")
            fh.write("BUILD_STAMP = %r\n" % line)
    except OSError:
        pass
    sys.stderr.write(line + "\n")
    return line


def get_requires_for_build_wheel(config_settings=None):
    _stamp()
    return _upstream.get_requires_for_build_wheel(config_settings)


def get_requires_for_build_editable(config_settings=None):
    _stamp()
    return _upstream.get_requires_for_build_editable(config_settings)


def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    _stamp()
    return _upstream.prepare_metadata_for_build_wheel(
        metadata_directory, config_settings)


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    _stamp()
    return _upstream.build_wheel(
        wheel_directory, config_settings, metadata_directory)


def build_editable(wheel_directory, config_settings=None, metadata_directory=None):
    _stamp()
    return _upstream.build_editable(
        wheel_directory, config_settings, metadata_directory)


def build_sdist(sdist_directory, config_settings=None):
    _stamp()
    return _upstream.build_sdist(sdist_directory, config_settings)
