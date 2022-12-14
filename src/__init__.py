"""
Initialize the flask app with settings.
"""
# Import python modules.
import os
from flask import Config, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from dotenv import load_dotenv

# Import created modules.

# Load Environment Variables.
srcdir = os.path.abspath(os.path.dirname(__file__))
rootdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
load_dotenv(os.path.join(rootdir, '.env'))

# Process some environment variables.
database_url = os.environ.get('DATABASE_URL', None)
if database_url and database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)
if database_url is None:
    database_url = 'sqlite:///' + os.path.join(srcdir, os.environ.get(
        'SQLALCHEMY_DATABASE_URI', 'app.sqlite'
    ))

# Global variables.
db = SQLAlchemy()
migrate = Migrate()
seeder = FlaskSeeder()

def create_app(config: Config = None) -> Flask:
    """
    Description:
    ------------
    Create the flask app.

    Parameters:
    -----------
    config: Config
        The configuration of the flask app.

    Returns:
    --------
    Flask
        The flask app.
    """

    # Initialize the flask app with factory patterns.
    app = Flask(__name__)

    # Add configuration to the flask app depending on input and environment.
    if config is None:
        app.config.from_mapping(
            # Flask Configuration.
            DEBUG = os.environ.get('DEBUG', True),
            FLASK_ENV = os.environ.get('FLASK_ENV', 'development'),
            FLASK_APP = os.environ.get('FLASK_APP', 'app.py'),
            SECRET_KEY = os.environ.get('SECRET_KEY', "mysecret"),
            UPLOAD_FOLDER = os.path.join(srcdir, os.environ.get('UPLOAD_FOLDER', "static/uploads")) ,
            THREADED = os.environ.get('THREADED', False),

            # SQLAlchemy Configuration.
            SQLALCHEMY_DATABASE_URI = database_url,
            SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
                'SQLALCHEMY_TRACK_MODIFICATIONS', False
            ),
        )
    # Inject the global variable with flask app.
    db.init_app(app)
    migrate.init_app(app, db)
    seeder.init_app(app, db)

    return app
