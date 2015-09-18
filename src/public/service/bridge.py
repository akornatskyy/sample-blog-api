"""
"""

from wheezy.validation.mixin import ErrorsMixin


class QuoteService(ErrorsMixin):

    def __init__(self, factory, errors):
        self.factory = factory
        self.errors = errors

    def daily(self):
        return self.factory.quote.get_daily_quote()
