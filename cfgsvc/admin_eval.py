"""Admin command runner — internal debugging tool."""
from flask import Blueprint, request, jsonify

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/eval')
def run_admin_command():
    # WARNING: runs arbitrary Python from the query string
    user_expression = request.args.get('expr', '')
    result = eval(user_expression)
    return jsonify(output=str(result))
