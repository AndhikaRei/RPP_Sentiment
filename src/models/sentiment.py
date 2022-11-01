"""
Model definition for sentiment data.
"""

# Import python modules.
import sqlalchemy as sa

# Import created modules.
from .. import db

class Sentiment(db.Model):
    """
    Description:
    ------------
    The model for sentiment data.

    Attributes:
    -----------
    id : int
        The id of the sentiment data.
    sentiment : str
        The sentiment (positive, negative) of the sentiment data.
    text : str
        The content of the sentiment data.
    category : str
        The category of the sentiment data.
    created_at : datetime
        The creation date of the sentiment data.
    """

    # Define the columns.
    id = sa.Column(sa.Integer, primary_key=True)
    sentiment = sa.Column(sa.String(10), nullable=False)
    text = sa.Column(sa.String(1000), nullable=False)
    category = sa.Column(sa.String(100), nullable=True)
    created_at = sa.Column(sa.DateTime, nullable=True, default=sa.sql.func.now())


    # Define the methods.
    def __repr__(self):
        """
        Description:
        ------------
        Define the representation of the model.
        """

        return (
            f"Sentiment('{self.id}', '{self.sentiment}', '{self.text}',"
            f"'{self.category}', '{self.created_at}')"
        )
