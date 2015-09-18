import json
import os.path


class QuoteRepository(object):

    def __init__(self, session):
        # ensure session is entered
        session.cursor()

    def get_daily_quote(self):
        return samples['quote']


samples = json.load(open(os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'samples.json')))
