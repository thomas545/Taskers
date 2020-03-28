# Middlewares

class MiddlewareMixin:
    def __init__(self, get_response=None):
        self.get_response = get_response
        print("get_response in __init__ - >>>", get_response)
        super().__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        response = response or self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        print("request in __call__ - >>>", request)
        print("response in __call__ - >>>", response)
        return response


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("get_response in __init__ - >>>", get_response)

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        print("request in __call__ - >>>", request)
        print("response in __call__ - >>>", response.Response)
        # Code to be executed for each request/response after
        # the view is called.

        return response