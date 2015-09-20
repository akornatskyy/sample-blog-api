"""
"""

from wheezy.validation.mixin import ErrorsMixin


class MembershipService(ErrorsMixin):

    def __init__(self, factory, errors):
        self.factory = factory
        self.errors = errors

    def authenticate(self, credential):
        up = self.factory.membership.authenticate(credential.username.lower())
        if not up or up['password'] != credential.password:
            self.error('The username or password provided is incorrect.')
            return None
        return self.factory.membership.get_user(up['id'])
