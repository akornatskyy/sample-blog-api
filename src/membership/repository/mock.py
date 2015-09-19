import json
import os.path


class MembershipRepository(object):

    def __init__(self, session):
        # ensure session is entered
        session.cursor()

    def authenticate(self, m):
        for u in samples['users']:
            if (u['username'] == m.username and
                    u['password'] == m.password):
                return True
        return False


samples = json.load(open(os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'samples.json')))
