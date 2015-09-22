"""
"""

from wheezy.core.collections import attrdict
from wheezy.core.comp import u
from wheezy.security import Principal
from wheezy.web.authorization import authorize

from shared.views import APIHandler

from membership.validation import credential_validator
from membership.validation import password_match_validator
from membership.validation import signup_validator


class SignInHandler(APIHandler):

    def post(self):
        m = attrdict(username=u(''), password=u(''))
        if (not self.try_update_model(m) or
                not self.validate(m, credential_validator) or
                not self.authenticate(m)):
            return self.json_errors()
        return self.json_response({'username': m.username})

    def authenticate(self, credential):
        with self.factory('ro') as f:
            user = f.membership.authenticate(credential)
            if not user:
                return False
        self.principal = Principal(id=user.id)
        return True


class SignUpHandler(APIHandler):

    def post(self):
        m = attrdict(email=u(''), username=u(''), password=u(''))
        p = attrdict(password=u(''), confirm_password=u(''))
        if (not self.try_update_model(m) &
                self.try_update_model(p) or
                not self.validate(m, credential_validator) &
                self.validate(m, signup_validator) &
                self.validate(p, password_match_validator) or
                not self.create_account(m)):
            return self.json_errors()
        return self.json_response({})

    def create_account(self, m):
        with self.factory('rw') as f:
            if not f.membership.create_account(m):
                return False
            f.session.commit()
        return True


class SignOutHandler(APIHandler):

    def get(self):
        del self.principal
        return self.json_response({})


class UserHandler(APIHandler):

    @authorize
    def get(self):
        u = self.get_user()
        return self.json_response({'username': u.username})

    def get_user(self):
        with self.factory('ro') as f:
            return f.membership.user
