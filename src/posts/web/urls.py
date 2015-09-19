"""
"""

from wheezy.routing import url

from shared.views import url_index

from posts.web.views import PostHandler
from posts.web.views import SearchPostsHandler


posts_api_urls = [
    url('search/posts', SearchPostsHandler),
    url('post/{slug}', PostHandler)
]

posts_urls = [
    url_index('posts', name='posts'),
    url_index('post/{slug}', name='post')
]
