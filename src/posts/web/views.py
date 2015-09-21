"""
"""

from wheezy.core.collections import attrdict
from wheezy.core.comp import u
from wheezy.http.response import not_found
from wheezy.web.authorization import authorize

from shared.views import APIHandler

from posts.validation import post_comment_validator
from posts.validation import search_posts_validator


class SearchPostsHandler(APIHandler):

    def get(self):
        m = attrdict(q=u(''), page=0)
        if (not self.try_update_model(m, self.request.query) or
                not self.validate(m, search_posts_validator)):
            return self.json_errors()
        return self.json_response(self.search_posts(m.q, m.page))

    def search_posts(self, q, page):
        with self.factory('ro') as f:
            return f.posts.search_posts(q, page)


class PostHandler(APIHandler):

    def get(self):
        p = self.get_post(self.route_args.slug,
                          self.request.query.get('fields'))
        if not p:
            return not_found()
        return self.json_response(p)

    def get_post(self, slug, fields):
        with self.factory('ro') as f:
            r = f.posts.get_post(slug)
            if not r:
                return None
            p, post_id = r
            if fields:
                if 'permissions' in fields:
                    p['permissions'] = f.posts.post_permissions(post_id)
                if 'comments' in fields:
                    p['comments'] = f.posts.list_comments(post_id)
        return p


class PostCommentsHandler(APIHandler):

    @authorize
    def post(self):
        m = attrdict(slug=self.route_args.slug, message=u(''))
        if (not self.try_update_model(m) or
                not self.validate(m, post_comment_validator) or
                not self.add_post_comment(m)):
            return self.json_errors()
        r = self.json_response({})
        r.status_code = 201
        return r

    def add_post_comment(self, m):
        with self.factory('rw') as f:
            if not f.posts.add_post_comment(m.slug, m.message):
                return False
            f.session.commit()
        return True
