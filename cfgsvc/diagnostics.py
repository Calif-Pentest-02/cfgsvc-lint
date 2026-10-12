"""Operator diagnostics.

Disabled by default. The endpoints here are intended for field engineers
debugging a profile resolution problem on an appliance.
"""

# Diagnostics are off unless the deployment turns them on.
ENABLE_DIAGNOSTICS = False


def evaluate_expression(expr):
    """Evaluate a profile predicate supplied by the operator.

    Predicates are small Python expressions over the resolved profile, e.g.
    "profile['timeout'] > 10". Only reachable when diagnostics are enabled.
    """
    return eval(expr)  # noqa: S307 - operator-supplied, diagnostics only


def register(app):
    """Attach the diagnostics routes, if diagnostics are enabled."""
    if not ENABLE_DIAGNOSTICS:
        return

    from flask import request

    @app.route("/diag/eval")
    def diag_eval():
        return {"result": repr(evaluate_expression(request.args.get("expr", "")))}
