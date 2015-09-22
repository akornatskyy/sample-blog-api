"""
"""


class QuoteService(object):

    def __init__(self, factory):
        self.factory = factory

    def daily(self):
        return self.factory.quote.get_daily_quote()
