import os
import ujson

from wheezy.http import response_cache
from wheezy.http.response import HTTPResponse
from wheezy.http.transforms import gzip_transform
from wheezy.http.transforms import response_transforms
from wheezy.routing import url
from wheezy.web.handlers import BaseHandler
from wheezy.web.handlers import file_handler
from wheezy.web.transforms import handler_transforms

from public.web.profile import public_cache_profile

from factory import Factory


class APIHandler(BaseHandler):

    def factory(self, session_name='ro'):
        return Factory(session_name, self.errors, self.principal)

    def json_errors(self):
        assert self.errors
        r = self.json_response(self.errors)
        r.status_code = 400
        return r

    def json_response(self, obj):
        r = HTTPResponse('application/json; charset=UTF-8', 'UTF-8')
        r.write_bytes(ujson.dumps(obj).encode('UTF-8'))
        return r


compress = handler_transforms(gzip_transform(compress_level=9, min_length=256))


def wraps_handler(p):
    def wrapper(h):
        return response_cache(p)(
            response_transforms(gzip_transform(
                compress_level=9, min_length=256))(h))
    return wrapper


if os.path.exists('content/static'):
    static = wraps_handler(public_cache_profile)(
        file_handler('content/static'))

    def url_index(path, name=None):
        return url(path, static, {'path': 'index.html'}, name=name)
