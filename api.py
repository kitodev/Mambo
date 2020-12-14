from webob import Request, Response

class Mambo:
    def __call__(self, environ, start_response):
        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)

    def handle_request(self, request):

        response = Response()

        return response
    def __init__(self):
        self.routes = {}
        print(self.routes)

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper

