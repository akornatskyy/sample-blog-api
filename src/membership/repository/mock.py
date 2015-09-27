"""
"""

from wheezy.core.collections import attrdict

from shared import mock as _


class MembershipRepository(object):

    def __init__(self, session):
        # ensure session is entered
        session.cursor()

    def authenticate(self, username):
        u = _.first(samples.users, lambda u: u.username == username)
        if not u:
            return None
        return attrdict(id=u.id, password=u.password)

    def get_user(self, user_id):
        u = find_user_by_id(int(user_id))
        if not u:
            return None
        return attrdict(id=str(u.id), username=u.username)

    def has_account(self, username):
        return _.first(samples.users,
                       lambda u: u.username == username) is not None

    def create_account(self, r):
        # TODO
        samples.users.append(attrdict(
            first_name='',
            id=100,
            last_name='',
            password=r.password,
            username=r.username,
            gravatar_hash=''))
        return False


def find_user_by_id(user_id):
    return _.first(samples.users, lambda u: u.id == user_id)


samples = _.load_samples(__file__)
