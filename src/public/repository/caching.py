from wheezy.caching.patterns import Cached
from wheezy.caching.patterns import key_builder

from config import cache
from public.repository import keys


kb = key_builder(key_prefix='pub')
cached = Cached(cache, kb, time=3600 * 24, namespace='public')


class QuoteRepository(object):

    def __init__(self, inner):
        self.inner = inner

    @cached(make_key=keys.get_daily_quote)
    def get_daily_quote(self):
        return self.inner.get_daily_quote()
