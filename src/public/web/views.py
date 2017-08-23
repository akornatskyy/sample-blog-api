"""
"""

import os
import ujson

from wheezy.http import response_cache
from wheezy.http.response import HTTPResponse
from wheezy.http.response import bad_request
from wheezy.web.handlers import file_handler

from shared.views import APIHandler
from shared.views import compress
from shared.views import wraps_handler

from public.web.profile import public_cache_profile
from public.web.profile import static_cache_profile


class DailyQuoteHandler(APIHandler):

    @response_cache(public_cache_profile)
    @compress
    def get(self):
        if not self.request.ajax:
            return bad_request()
        return self.json_response(self.get_daily_quote())

    def get_daily_quote(self):
        with self.factory() as f:
            return f.quote.daily()


# region: static file handlers

def error_response(status_code, subject, message):
    b = ujson.dumps({
        'ok': False,
        'code': status_code,
        'subject': subject,
        'message': message
    })

    def handler(request):
        r = HTTPResponse('application/json; charset=UTF-8', 'UTF-8')
        r.write_bytes(b.encode('UTF-8'))
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

http401 = error_response(
    status_code=401,
    subject='Oops! Code 401. Sorry, requires authorization.',
    message='Your credentials do not allow access to this resource.')

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


if os.path.exists('content/static'):
    w = wraps_handler(static_cache_profile)
    css_file = w(file_handler('content/static/css'))
    js_file = w(file_handler('content/static/js'))
    static_file = w(file_handler('content/static'))
