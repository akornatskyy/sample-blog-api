"""
"""

from wheezy.validation.mixin import ErrorsMixin


class MembershipService(ErrorsMixin):

    def __init__(self, factory, errors):
        self.factory = factory
        self.errors = errors

    def authenticate(self, credential):
        if not self.factory.membership.authenticate(credential):
            self.error('The username or password provided is incorrect.')
            return False
        return True
