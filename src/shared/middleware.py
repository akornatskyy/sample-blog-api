"""
"""


class HTTPErrorPassThroughMiddleware(object):

    def __init__(self, status_code, route_name):
        self.status_code = status_code
        self.route_name = route_name

    def __call__(self, request, following):
        response = following(request)
        if (response.status_code == self.status_code and
                request.ajax and
                request.path.startswith('/api/')):
            request.environ['route_args']['route_name'] = self.route_name
        return response


def http_error_pass_through_middleware_factory(options):
    route_name = options['http_errors'][400]
    return HTTPErrorPassThroughMiddleware(400, route_name)
