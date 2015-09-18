"""
"""

from wheezy.routing import url

from public.web.urls import error_urls
from public.web.urls import public_urls
from public.web.urls import public_api_urls
from public.web.urls import static_urls
from public.web.views import welcome


all_api_urls = []
all_api_urls += public_api_urls

all_urls = [
    url('', welcome, {'path': 'index.html'}, name='default'),
    url('api/v1/', all_api_urls)
]
all_urls += public_urls
all_urls += [('error/', error_urls)]
all_urls += static_urls
