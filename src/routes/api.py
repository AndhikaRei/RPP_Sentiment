"""
Routing for API.
"""

# Import python modules.
import os
import random
import pickle
from typing import List
from datetime import datetime
from flask import Blueprint, request, url_for, redirect, render_template
from werkzeug.utils import secure_filename

# Import created modules.
from src import db
from src.models.sentiment import Sentiment

# Load model from pickled file
model = pickle.load(open('model.pkl', 'rb'))

# Make the blueprint.
api_route = Blueprint('api_route', __name__, url_prefix='/api/v1')

"""
--------------------------------------------------------------
# Sentiment Api Routes.
--------------------------------------------------------------
"""
@api_route.route("create-sentiment", methods=['POST'])
def create_sentiment():
    """
    Description:
    ------------
    Add a new sentiment to the database.

    Path:
    -----
    POST /api/v1/create-sentiments
    
    Request Body:
    -------------
    text : str
        The content of the sentiment data.
    created_at : datetime
        The creation date of the sentiment data.
    file : file
        The file containing multiple sentiment data.
    """
    from src.app import app
    
    if request.method == 'POST':
        try:
            # Process uploaded file. Assume the file is in csv format.
            if request.files["file"].filename != "":
                
                # Save the file.
                file = request.files["file"]
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(file.filename))
                file.save(filepath)
                
                # Process file content. The content of the file should be in the following format:
                # Text, Created At(Optional)
                with open(filepath, 'r') as f:
                    for line in f.read().splitlines():
                        sentiment_content = line.split(',')
                        # Construct the sentiment object and add it to the database.
                        sentiment = Sentiment(
                            sentiment = random.choice(["Positive", "Negative"]),
                            text = sentiment_content[0].strip()
                        )
                        if len(sentiment_content) > 1:
                            sentiment.created_at = datetime.strptime(
                                sentiment_content[1].strip(), '%Y-%m-%d %H:%M:%S'
                            )
                        db.session.add(sentiment)
                        db.session.commit()    
                return redirect(url_for('webpage_route.dashboard'))    
            
            # Process form data.
            elif request.form["text"] != "":
                
                # Construct the sentiment data and save it to the database.
                sentiment = Sentiment(
                    sentiment = random.choice(["Positive", "Negative"]),
                    text = request.form['text'].strip()
                )
                if request.form['created_at']:
                    sentiment.created_at = datetime.strptime(
                        request.form['created_at'].strip(), '%Y-%m-%dT%H:%M'
                    )
                db.session.add(sentiment)
                db.session.commit()
                return redirect(url_for('webpage_route.dashboard'))
            
            # No data provided.
            else:
                raise Exception("No data provided.")

        except Exception as err:
            return render_template('pages/add-data.html', error = err, form = request.form)

@api_route.route("/delete-sentiment/<int:id>", methods=["POST"])
def delete_sentiment(id):
    """
    Description:
    ------------
    Delete a sentiment from the database.
    
    Path:
    -----
    api/v1/delete-sentiment/<int:id>
    """
    
    # Delete the sentiment from the database if it exists.
    try:        
        sentiment = Sentiment.query.get(id)
        if sentiment is not None:
            db.session.delete(sentiment)
            db.session.commit()
        return redirect(url_for('webpage_route.dashboard'))
    
    except Exception as err:
        sentiments: List[Sentiment] = Sentiment.query.all()
        return render_template('pages/dashboard.html', error = err, sentiments = sentiments)