"""
Routing for the webpages.
"""

# Import python modules.
from typing import List
from flask import Blueprint, render_template

# Import created modules.
from src import db
from src.models.sentiment import Sentiment

# Make the blueprint.
webpage_route = Blueprint('webpage_route', __name__, url_prefix='/')


"""
--------------------------------------------------------------
# Sentiment Tracker Webpages.
--------------------------------------------------------------
"""
@webpage_route.route("dashboard")
def dashboard():
    """
    Description:
    ------------
    Sentiment tracker webpage.
    """
    sentiments: List[Sentiment] = Sentiment.query.all()
    return render_template('pages/dashboard.html', sentiments=sentiments)

@webpage_route.route("add-data")
def add_data():
    """
    Description:
    ------------
    Add sentiment data webpage.
    """
    return render_template('pages/add-data.html')

@webpage_route.route("contributor")
def contributor():
    """
    Description:
    ------------
    Website contributor webpage.
    """

    return render_template('pages/contributor.html')
    