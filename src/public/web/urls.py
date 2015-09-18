"""
"""

from wheezy.routing import url

from public.web.views import DailyQuoteHandler
from public.web.views import css_file
from public.web.views import http400
from public.web.views import http403
from public.web.views import http404
from public.web.views import http500
from public.web.views import js_file
from public.web.views import static_file


public_api_urls = [
    url('quote/daily', DailyQuoteHandler)
]

public_urls = [
]

error_urls = [
    url('400', http400, name='http400'),
    url('403', http403, name='http403'),
    url('404', http404, name='http404'),
    url('500', http500, name='http500'),
]

static_urls = [
    url('js/{path:any}', js_file, name='js'),
    url('css/{path:any}', css_file, name='css'),
    url('favicon.ico', static_file, {'path': 'img/favicon.ico'}),
    url('robots.txt', static_file, {'path': 'robots.txt'}, name='robots')
]
