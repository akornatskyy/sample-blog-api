from wheezy.validation.mixin import ErrorsMixin


class BaseService(ErrorsMixin):

    def __init__(self, factory, errors, principal):
        self.factory = factory
        self.errors = errors
        self.principal = principal
