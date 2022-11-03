"""
Initialize the Flask app.
"""

# Import python modules.

# Import created modules.
from src import create_app
from src.routes.webpage import webpage_route
from src.routes.api import api_route
from src.routes.default import default_route

# Initialize the flask app with factory patterns.
app = create_app()

# Register the routes.
app.register_blueprint(default_route)
app.register_blueprint(webpage_route)
app.register_blueprint(api_route)

