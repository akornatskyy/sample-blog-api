"""
"""

from wheezy.core.collections import attrdict
from wheezy.core.comp import u
from wheezy.http.response import not_found

from shared.views import APIHandler

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
            p = f.posts.get_post(slug)
            if not p:
                return None
            if fields:
                if 'permissions' in fields:
                    p['permissions'] = f.posts.post_permissions(p['id'])
                if 'comments' in fields:
                    p['comments'] = f.posts.list_comments(p['id'])
        return p
