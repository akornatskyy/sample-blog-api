import json
import os.path

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
        return {'id': u.id, 'password': u.password}

    def get_user(self, user_id):
        u = find_user_by_id(user_id)
        if not u:
            return None
        return {'id': str(u.id)}


def find_user_by_id(user_id):
    return _.first(samples.users, lambda u: u.id == user_id)


samples = json.load(open(os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'samples.json')), object_hook=attrdict)
