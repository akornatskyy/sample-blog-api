"""
"""

import ujson

from wheezy.http.response import HTTPResponse
from wheezy.web.handlers import BaseHandler

from factory import Factory


class APIHandler(BaseHandler):

    def factory(self, session_name='ro'):
        return Factory(session_name, **self.context)

    def json_response(self, obj):
        r = HTTPResponse('application/json; charset=UTF-8', 'UTF-8')
        r.write_bytes(ujson.dumps(obj))
        return r
