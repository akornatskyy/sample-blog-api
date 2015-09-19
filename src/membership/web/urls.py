"""
"""

from wheezy.routing import url

from shared.views import url_index

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

membership_urls = [
    url_index('signin', name='signin'),
    url_index('signup', name='signup')
]
