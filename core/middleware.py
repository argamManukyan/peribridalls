from threading import current_thread

from django.utils.deprecation import MiddlewareMixin

_requests = {}


def current_request():
    return _requests.get(current_thread().ident, None)


class GlobalRequestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        _requests[current_thread().ident] = request
