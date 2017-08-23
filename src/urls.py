"""
"""

from wheezy.routing import url

from membership.web.urls import membership_api_urls
from membership.web.urls import membership_urls
from posts.web.urls import posts_api_urls
from posts.web.urls import posts_urls
from public.web.urls import error_urls
from public.web.urls import public_api_urls
from public.web.urls import public_urls
from public.web.urls import static_urls


all_api_urls = []
all_api_urls += membership_api_urls
all_api_urls += posts_api_urls
all_api_urls += public_api_urls

all_urls = []
all_urls += [url('api/v1/', all_api_urls)]
all_urls += membership_urls
all_urls += posts_urls
all_urls += public_urls
all_urls += [('error/', error_urls)]
all_urls += static_urls
