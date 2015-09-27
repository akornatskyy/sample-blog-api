"""
"""


class HTTPErrorPassThroughMiddleware(object):

    def __init__(self, http_errors):
        self.http_errors = http_errors

    def __call__(self, request, following):
        response = following(request)
        if (response and response.status_code >= 400 and
                request.ajax and
                request.path.startswith('/api/')):
            request.environ['route_args']['route_name'] = \
                self.http_errors[response.status_code]
        return response


def http_error_pass_through_middleware_factory(options):
    return HTTPErrorPassThroughMiddleware(options['http_errors'])
