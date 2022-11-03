"""
Routing for handling default routes such as error pages and unidentified routes.
"""

# Import python modules.
from flask import Blueprint, jsonify, redirect, url_for

# Import created modules.
from src.constants.http_status_codes import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

# Make the blueprint.
default_route = Blueprint('default_route', __name__, url_prefix='/')


# --------------------------------------------------------------
# Default Route
# --------------------------------------------------------------
@default_route.route("")
def index():
    """
    Description:
    ------------
    Redirect to the homepage.
    """

    return redirect(url_for('webpage_route.dashboard'))
