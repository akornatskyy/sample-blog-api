from wheezy.caching.patterns import Cached
from wheezy.caching.patterns import key_builder

from config import cache
from membership.repository import keys


kb = key_builder(key_prefix='mbr')
cached = Cached(cache, kb, time=3600 * 24, namespace='membership')


class MembershipRepository(object):

    def __init__(self, inner):
        self.inner = inner

    @cached(make_key=keys.authenticate)
    def authenticate(self, username):
        return self.inner.authenticate(username)

    @cached(make_key=keys.get_user)
    def get_user(self, user_id):
        return self.inner.get_user(user_id)

    @cached(make_key=keys.has_account)
    def has_account(self, username):
        return self.inner.has_account(username)

    def create_account(self, r):
        return self.inner.create_account(r)
