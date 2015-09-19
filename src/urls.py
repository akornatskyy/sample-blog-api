"""
"""

from wheezy.routing import url

from membership.web.urls import membership_api_urls
from membership.web.urls import membership_urls
from public.web.urls import error_urls
from public.web.urls import public_api_urls
from public.web.urls import public_urls
from public.web.urls import static_urls
from shared.views import url_index


all_api_urls = []
all_api_urls += public_api_urls
all_api_urls += membership_api_urls

all_urls = [
    url_index('', name='default'),
    url('api/v1/', all_api_urls)
]
all_urls += membership_urls
all_urls += public_urls
all_urls += [('error/', error_urls)]
all_urls += static_urls
