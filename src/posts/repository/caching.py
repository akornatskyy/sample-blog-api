"""
"""

from wheezy.caching.patterns import Cached
from wheezy.caching.patterns import key_builder

from config import cache
from posts.repository import keys


kb = key_builder(key_prefix='pub')
cached = Cached(cache, kb, time=3600 * 24, namespace='public')


class PostsRepository(object):

    def __init__(self, inner):
        self.inner = inner

    @cached(make_key=keys.search_posts)
    def search_posts(self, q, page):
        return self.inner.search_posts(q, page)

    @cached(make_key=keys.get_post_id)
    def get_post_id(self, slug):
        return self.inner.get_post_id(slug)

    @cached(make_key=keys.get_post)
    def get_post(self, slug):
        return self.inner.get_post(slug)

    @cached(make_key=keys.list_comments)
    def list_comments(self, post_id, author_id):
        return self.inner.list_comments(post_id, author_id)

    @cached(make_key=keys.count_comments_awaiting_moderation)
    def count_comments_awaiting_moderation(self, user_id, limit):
        return self.inner.count_comments_awaiting_moderation(user_id, limit)

    def add_post_comment(self, post_id, author_id, message):
        ok = self.inner.add_post_comment(post_id, author_id, message)
        if ok:
            cache.delete_multi((
                keys.list_comments(post_id, author_id),
                keys.count_comments_awaiting_moderation(author_id)))
        return ok
