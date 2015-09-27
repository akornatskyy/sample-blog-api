"""
"""

from wheezy.core.descriptors import attribute
from wheezy.security.authorization import authorized

from shared.bridge import BaseService


class MembershipService(BaseService):

    @attribute
    @authorized
    def user(self):
        return self.factory.membership.get_user(self.principal.id)

    def authenticate(self, credential):
        up = self.factory.membership.authenticate(credential.username.lower())
        if not up or up.password != credential.password:
            self.error('The username or password provided is incorrect.')
            return None
        return self.factory.membership.get_user(up.id)

    def create_account(self, registration):
        if self.factory.membership.has_account(registration.username):
            self.error(
                'The user with such username is already registered. '
                'Please try another.',
                name='username')
            return False
        if not self.factory.membership.create_account(registration):
            self.error(
                'The system was unable to create an account for you. '
                'Please try again later.')
            return False
        return True
