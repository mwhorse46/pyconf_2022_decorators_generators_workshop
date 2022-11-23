# We will be mimicking API View decorator from Django Rest Framework
# API View wraps every function in APIView class

from typing import Literal, List

Methods = Literal["GET", "POST", "PATCH", "DELETE", "PUT"]


class Request(object):
    def __init__(self, method: Methods) -> None:
        self.method = method  # type: str
        self.args = {}
        self.view_args = {}
        self.json = {}
        self.headers = {}


class APIView(object):
    methods = []

    def abort(self, msg: str):
        raise Exception(msg)

    def dispatch(self, request: Request, *args, **kwargs):
        if request.method.lower() in self.methods:
            g = getattr(self, request.method.lower())
            return g(*args, **kwargs)
        else:
            self.abort("Method Not Allowed")


def api_view(methods: List[Methods] = []):
    pass


# def api_view(methods: List[Methods] = []):
#     methods_ = methods or ["GET"]

#     def decorator(func):
#         def handler(self, *args, **kwargs):
#             return func(*args, **kwargs)
#         # creating map for all the supported methods
#         handlers = {i.lower(): handler for i in methods_}
#         wrapped_api_view = type("WrapperAPIView", (APIView,), handlers)
#         wrapped_api_view.methods = methods_
#         api_ = wrapped_api_view()
#         return api_
#     return decorator

def hello():
    return "Hi from this view"
