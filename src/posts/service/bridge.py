"""
"""

from wheezy.security.authorization import authorized

from shared.bridge import BaseService


class PostsService(BaseService):

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
        if not self.can_comment():
            self.error('There are too many of your comments awaiting '
                       'moderation. Come back later, please.')
            return False
        post_id = self.factory.posts.get_post_id(slug)
        if not post_id:
            self.error('We\'re sorry... the post cannot be found.')
            return False
        ok = self.factory.posts.add_post_comment(
            post_id, self.principal.id, message)
        if not ok:
            self.error('We\'re sorry... the comment cannot be added.')
            return False
        return True
