"""Profile document validation against the vendored schema."""
import json
import os

SCHEMA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "..", "vendor", "profile-schema",
                           "profile-schema.json")


def _schema():
    with open(SCHEMA_PATH) as f:
        return json.load(f)


def allowed_fields():
    """Fields a profile document may carry, per the vendored schema."""
    return list(_schema().get("fields", []))


def validate(profile):
    """Drop anything the vendored schema does not name."""
    allowed = set(allowed_fields())
    return {k: v for k, v in profile.items() if k in allowed}
