"""
Seeder for sentiment data.
"""

# Import python modules.
import datetime
from flask_seeder import Seeder

# Import created modules.
from src.models.sentiment import Sentiment

# Database Seeder.
class SentimentSeeder(Seeder):
    """
    Description:
    ------------
        Class for seeding sentiment data.
    """

    def run(self):
        """
        Description:
        ------------
            Run the seeder.
        """

        sentiments = [
            {
                'sentiment': 'Positive',
                'text': 'Dummy positive sentiment data.',
                'category': 'Product',
                'created_at': datetime.datetime.now(),
            },
            {
                'sentiment': 'Negative',
                'text': 'Dummy negative sentiment data.',
                'category': 'Product',
                'created_at': datetime.datetime.now(),
            }
        ]

        # Insert the data.
        for sentiment in sentiments:
            sentiment_data = Sentiment(**sentiment)
            print(f"Adding sentiment: {sentiment_data}")
            self.db.session.add(sentiment_data)
        self.db.session.commit()
