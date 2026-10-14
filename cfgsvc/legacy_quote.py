"""Shell quoting helpers kept from the appliance vendor tooling.

The vendor tooling shelled out to the appliance CLI and quoted its arguments
with the standard library helper it had at the time.
"""
import pipes


def quote_arg(value):
    """Quote a single argument for the appliance CLI."""
    return pipes.quote(str(value))


def quote_all(values):
    return " ".join(quote_arg(v) for v in values)
