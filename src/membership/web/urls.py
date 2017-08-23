"""
"""
import os

from wheezy.routing import url

from membership.web.views import SignInHandler
from membership.web.views import SignOutHandler
from membership.web.views import SignUpHandler
from membership.web.views import UserHandler


membership_api_urls = [
    url('signin', SignInHandler),
    url('signup', SignUpHandler),
    url('signout', SignOutHandler),
    url('user', UserHandler)
]

membership_urls = []
if os.path.exists('content/static'):
    from shared.views import url_index
    membership_urls += [
        url_index('signin', name='signin'),
        url_index('signup', name='signup')
    ]
