"""
"""

from wheezy.security.authorization import authorized
from wheezy.validation.mixin import ErrorsMixin


class PostsService(ErrorsMixin):

    def __init__(self, factory, errors, principal):
        self.factory = factory
        self.errors = errors
        self.principal = principal

    def search_posts(self, q, page):
        return self.factory.posts.search_posts(q, page)

    def get_post(self, slug):
        return self.factory.posts.get_post(slug)

    def post_permissions(self, post_id):
        return {
            'create_comment': self.can_comment()
        }

    def can_comment(self):
        if not self.principal:
            return False
        return self.factory.posts.count_comments_awaiting_moderation(
            self.principal.id, 5) < 5

    def list_comments(self, post_id):
        return self.factory.posts.list_comments(
            post_id, self.principal and self.principal.id)

    @authorized
    def add_post_comment(self, slug, message):
        r = self.factory.posts.add_post_comment(
            slug, self.principal.id, message)
        if not r:
            self.error('Post not found.')
        return r
