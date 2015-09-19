"""
"""

from wheezy.core.collections import attrdict
from wheezy.core.comp import u
from wheezy.security import Principal
from wheezy.web.authorization import authorize

from shared.views import APIHandler

from membership.validation import credential_validator


class SignInHandler(APIHandler):

    def post(self):
        m = attrdict(username=u(''), password=u(''))
        m.update(self.request.form)
        if (not self.validate(m, credential_validator) or
                not self.authenticate(m)):
            return self.json_errors()
        return self.json_response({'username': m.username})

    def authenticate(self, credential):
        with self.factory('ro') as f:
            if not f.membership.authenticate(credential):
                return False
        self.principal = Principal(id=credential.username)
        return True


class SignUpHandler(APIHandler):

    def post(self):
        m = attrdict(email=u(''), username=u(''), password=u(''))
        m.update(self.request.form)
        if not self.signup(m):
            return self.json_errors()
        return self.json_response({})

    def signup(self, m):
        self.error('This feature is not available yet.')
        return False


class SignOutHandler(APIHandler):

    def get(self):
        del self.principal
        return self.json_response({'ok': True})


class UserHandler(APIHandler):

    @authorize
    def get(self):
        return self.json_response({'username': self.principal.id})
