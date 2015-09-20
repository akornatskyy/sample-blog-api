"""
"""

from wheezy.core.descriptors import attribute
from wheezy.core.introspection import import_name

from config import config

from membership.service.bridge import MembershipService
from posts.service.bridge import PostsService
from public.service.bridge import QuoteService


class Factory(object):

    def __init__(self, session_name, **context):
        self.context = context
        self.session = sessions[session_name]()
        self.factory = RepositoryFactory(self.session)

    def __enter__(self):
        self.session.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.__exit__(exc_value, exc_value, traceback)

    @attribute
    def membership(self):
        return MembershipService(self.factory, self.context['errors'])

    @attribute
    def posts(self):
        return PostsService(self.factory,
                            self.context['errors'],
                            self.context['principal'])

    @attribute
    def quote(self):
        return QuoteService(self.factory, self.context['errors'])


class RepositoryFactory(object):

    def __init__(self, session):
        self.session = session

    @attribute
    def membership(self):
        return MembershipPersistence(self.session)

    @attribute
    def posts(self):
        return PostsPersistence(self.session)

    @attribute
    def quote(self):
        return QuotePersistence(self.session)


def mock_sessions():
    from wheezy.core.db import NullSession
    return {
        'ro': NullSession, 'rw': NullSession
    }


# region: configuration details
mode = config.get('runtime', 'mode')
MembershipPersistence = import_name('membership.repository.%s.'
                                    'MembershipRepository' % mode)
PostsPersistence = import_name('posts.repository.%s.'
                               'PostsRepository' % mode)
QuotePersistence = import_name('public.repository.%s.'
                               'QuoteRepository' % mode)
if mode == 'mock':
    sessions = mock_sessions()
else:
    raise NotImplementedError(mode)
del mode, config
