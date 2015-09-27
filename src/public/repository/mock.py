"""
"""

from shared import mock as _


class QuoteRepository(object):

    def __init__(self, session):
        # ensure session is entered
        session.cursor()

    def get_daily_quote(self):
        return samples['quote']


samples = _.load_samples(__file__)
