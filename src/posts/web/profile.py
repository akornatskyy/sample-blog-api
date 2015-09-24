"""
"""

from datetime import timedelta

from wheezy.http import CacheProfile
from wheezy.http.cache import etag_md5crc32

from config import config


search_posts = CacheProfile(
    'both',
    duration=timedelta(minutes=15),
    # this cause browser to send request each time
    # so the server is able to respond with code 304
    http_max_age=0,
    vary_environ=['HTTP_ACCEPT_ENCODING'],
    vary_query=['q', 'page'],
    etag_func=etag_md5crc32,
    enabled=config.getboolean('cache-profile', 'posts-enabled'))
post = CacheProfile(
    'both',
    duration=timedelta(minutes=15),
    http_max_age=0,
    http_vary=['Cookie'],
    vary_cookies=['_a'],
    vary_environ=['HTTP_ACCEPT_ENCODING'],
    vary_query=['fields'],
    etag_func=etag_md5crc32,
    enabled=config.getboolean('cache-profile', 'posts-enabled'))
