from wheezy.core.collections import attrdict
from wheezy.security import Principal
from wheezy.web.authorization import authorize

from lockout import locker
from shared.views import APIHandler

from membership.validation import credential_validator
from membership.validation import password_match_validator
from membership.validation import signup_validator


class SignInHandler(APIHandler):

    lockout = locker.define(
        name='signin attempts',
        by_ip=dict(count=3, duration=60)
    )

    @lockout.forbid_locked
    def post(self):
        m = attrdict(username='', password='')
        if (not self.try_update_model(m) or
                not self.validate(m, credential_validator) or
                not self.authenticate(m)):
            return self.json_errors()
        return self.json_response({'username': m.username})

    @lockout.guard
    def authenticate(self, credential):
        with self.factory('ro') as f:
            user = f.membership.authenticate(credential)
            if not user:
                return False
        self.principal = Principal(id=user.id)
        return True


class SignUpHandler(APIHandler):

    lockout = locker.define(
        name='signup attempts',
        by_ip=dict(count=2, duration=60)
    )

    @lockout.forbid_locked
    def post(self):
        m = attrdict(email='', username='', password='')
        p = attrdict(password='', confirm_password='')
        if (not self.try_update_model(m) &
                self.try_update_model(p) or
                not self.validate(m, credential_validator) &
                self.validate(m, signup_validator) &
                self.validate(p, password_match_validator) or
                not self.create_account(m)):
            return self.json_errors()
        return self.json_response({})

    @lockout.quota
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
