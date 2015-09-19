import json
import os.path


class PostsRepository(object):

    def __init__(self, session):
        # ensure session is entered
        session.cursor()


samples = json.load(open(os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'samples.json')))
