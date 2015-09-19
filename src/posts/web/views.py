"""
"""

from shared.views import APIHandler


class SearchPostsHandler(APIHandler):

    def get(self):
        return self.json_response({})


class PostHandler(APIHandler):

    def get(self):
        return self.json_response({})
