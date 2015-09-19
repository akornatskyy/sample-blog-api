"""
"""

from wheezy.validation.mixin import ErrorsMixin


class PostsService(ErrorsMixin):

    def __init__(self, factory, errors):
        self.factory = factory
        self.errors = errors
