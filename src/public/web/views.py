"""
"""

import ujson

from wheezy.http import response_cache
from wheezy.http.transforms import gzip_transform
from wheezy.http.transforms import response_transforms
from wheezy.http.response import HTTPResponse
from wheezy.web.handlers import file_handler

from public.web.profile import public_cache_profile
from public.web.profile import static_cache_profile


wraps_handler = lambda p: lambda h: response_cache(p)(
    response_transforms(gzip_transform(compress_level=9))(h))

w = wraps_handler(public_cache_profile)
welcome = w(file_handler('content/static'))


def error_response(status_code, subject, message):
    b = ujson.encode({
        'ok': False,
        'code': status_code,
        'subject': subject,
        'message': message
    })

    def handler(request):
        r = HTTPResponse('application/json; charset=UTF-8', 'UTF-8')
        r.write_bytes(b)
        r.status_code = status_code
        return r
    return handler


# cached by nginx
http400 = error_response(
    status_code=400,
    subject='Oops! Code 400. Sorry, we can\'t process your request.',
    message='The 400 Bad Request error is an HTTP status code that means \
that the request you sent to the website server (i.e. a request to load a \
web page) was somehow malformed therefore the server was unable to \
understand or process the request.')

http403 = error_response(
    status_code=403,
    subject='Oops! Code 403. Access is denied.',
    message='You do not have permission to view this directory or page \
using the credentials that you supplied.')

http404 = error_response(
    status_code=404,
    subject='Oops! Code 404. Sorry, we can\'t find that page.',
    message='Unfortunately the page you are looking for may have been \
removed, had its name changed, under construction or is temporarily \
unavailable. Try checking the web address for typos, please. We apologize \
for the inconvenience.')

http500 = error_response(
    status_code=500,
    subject='Oops! Code 500. Sorry, we can not process your request.',
    message='The web server encountered an unexpected condition that \
prevented it from fulfilling the request by the client for access to the \
requested URL.')

w = wraps_handler(static_cache_profile)
css_file = w(file_handler('content/static/css'))
js_file = w(file_handler('content/static/js'))
static_file = w(file_handler('content/static'))
