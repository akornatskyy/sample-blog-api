"""
"""

from datetime import datetime

from wheezy.core.collections import attrdict
from wheezy.core.datetime import UTC

from shared import mock as _
from membership.repository.mock import find_user_by_id


class PostsRepository(object):

    def __init__(self, session):
        # ensure session is entered
        session.cursor()

    def search_posts(self, q, page):
        posts = samples.posts
        if q:
            q = q.lower()
            posts = _.nfilter(posts, (page + 1) * 2 + 1,
                              lambda p: q in p.title.lower())

        def translate(p):
            a = find_user_by_id(p.author_id)
            return {
                'slug': p.slug,
                'title': p.title,
                'author': {
                    'first_name': a.first_name,
                    'last_name': a.last_name
                },
                'created_on': p.created_on,
                'message': _.trancate_words(p.message, 40)
            }
        return _.pager(posts, page, 2, translate)

    def get_post_id(self, slug):
        p = _.first(samples.posts, lambda p: p.slug == slug)
        return p and p.id

    def get_post(self, slug):
        p = _.first(samples.posts, lambda p: p.slug == slug)
        if not p:
            return None
        a = find_user_by_id(p.author_id)
        return {
            'id': p.id,
            'slug': p.slug,
            'title': p.title,
            'created_on': p.created_on,
            'author': {
                'first_name': a.first_name,
                'last_name': a.last_name
            },
            'message': p.message
        }

    def list_comments(self, post_id, author_id):
        r = []
        author_id = author_id and int(author_id)
        for c in samples.comments:
            if (c.post_id == post_id and
                    (c.moderated or c.author_id == author_id)):
                a = find_user_by_id(c.author_id)
                r.append({
                    'author': {
                        'first_name': a.first_name,
                        'last_name': a.last_name,
                        'gravatar_hash': a.gravatar_hash
                    },
                    'created_on': c.created_on,
                    'message': c.message,
                    'moderated': c.moderated
                })
        return r

    def count_comments_awaiting_moderation(self, user_id, limit):
        user_id = int(user_id)
        return len(_.nfilter(
            samples.comments, limit,
            lambda c: c.author_id == user_id and not c.moderated))

    def add_post_comment(self, post_id, author_id, message):
        now = datetime.utcnow().replace(tzinfo=UTC)
        samples['comments'].insert(0, attrdict(
            author_id=int(author_id),
            created_on=now.isoformat(),
            id='',
            message=message,
            moderated=False,
            post_id=post_id
        ))
        return True


samples = _.load_samples(__file__)
