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


# --------------------------------------------------------------
# Error Handler Route
# --------------------------------------------------------------
@default_route.errorhandler(HTTP_404_NOT_FOUND)
def handle_404(e):
    """
    Description:
    ------------
    Handle the 404 error.

    Parameters:
    -----------
    e: HTTP_404_NOT_FOUND
        The error that is thrown.
    """

    return jsonify({
        'apiVersion': '1.0',
        'error': {
            'code': HTTP_404_NOT_FOUND,
            'message': 'Not Found'
        }
    }), HTTP_404_NOT_FOUND

@default_route.errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
def handle_500(e):
    """
    Description:
    ------------
    Handle the 500 error.

    Parameters:
    -----------
    e: HTTP_500_INTERNAL_SERVER_ERROR
        The error that is thrown.
    """

    return jsonify({
        'apiVersion': '1.0',
        'error': {
            'code': HTTP_500_INTERNAL_SERVER_ERROR,
            'message': 'Internal Server Error'
        }
    }), HTTP_500_INTERNAL_SERVER_ERROR
