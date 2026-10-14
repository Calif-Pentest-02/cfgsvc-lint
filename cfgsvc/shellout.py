"""Fleet CLI wrapper.

`cfgsvc` reconciles its profile cache by calling the appliance CLI, which is
the only supported way to read the vendor's own view of a fleet.
"""
import subprocess

CLI = "/opt/appliance/bin/fleetctl"


def fleet_status(fleet):
    """Return the vendor CLI's status line for one fleet."""
    cmd = "%s status --fleet %s --format plain" % (CLI, fleet)
    out = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return out.stdout.strip()
