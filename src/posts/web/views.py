"""
"""

from wheezy.core.collections import attrdict
from wheezy.core.comp import u
from wheezy.http.response import not_found
from wheezy.web import handler_cache
from wheezy.web.authorization import authorize

from config import cached
from lockout import locker
from shared.views import APIHandler
from shared.views import compress

from posts.validation import post_comment_validator
from posts.validation import post_spec_validator
from posts.validation import search_posts_validator
from posts.web import keys
from posts.web import profile


class SearchPostsHandler(APIHandler):

    @handler_cache(profile=profile.search_posts)
    @compress
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

    @handler_cache(profile=profile.post)
    @compress
    def get(self):
        m = attrdict(slug=u(''), fields=[''])
        if (not self.try_update_model(m, self.route_args) or
                not self.try_update_model(m, self.request.query) or
                not self.validate(m, post_spec_validator)):
            return self.json_errors()
        p = self.get_post(m.slug, m.fields)
        if not p:
            return not_found()
        r = self.json_response(p)
        if self.principal:
            r.cache_dependency = (
                keys.post(m.slug),
                keys.author_comments(self.principal.id))
        else:
            r.cache_dependency = (keys.post(m.slug),)
        return r

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


class PostCommentsHandler(APIHandler):

    lockout = locker.define(
        name='post comments',
        by_ip=dict(count=2, duration=60)
    )

    @authorize
    @lockout.forbid_locked
    def post(self):
        m = attrdict(slug=u(''), message=u(''))
        if (not self.try_update_model(m, self.route_args) or
                not self.try_update_model(m) or
                not self.validate(m, post_comment_validator) or
                not self.add_post_comment(m)):
            return self.json_errors()
        r = self.json_response({})
        r.status_code = 201
        return r

    @lockout.quota
    def add_post_comment(self, m):
        with self.factory('rw') as f:
            if not f.posts.add_post_comment(m.slug, m.message):
                return False
            f.session.commit()
        cached.dependency.delete_multi((
            keys.post(m.slug),
            keys.author_comments(self.principal.id)))
        return True
