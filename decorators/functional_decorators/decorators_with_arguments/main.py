# functional decorator with arguments
# function to handle multiple exceptions
from functools import wraps


class FakeException(Exception):
    pass


def handle_exceptions(*exceptions):
    def decorator(func):
        @wraps(func)
        def __inner__(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                return res
            except Exception as e:
                for exception in exceptions:
                    if isinstance(e, exception):
                        print(f"func {func.__name__} raised {e}")
                        break
                else:
                    raise (e)
        return __inner__
    return decorator


# @handle_exceptions(exceptions=[FakeException])
@handle_exceptions()
def abc():
    raise FakeException("This is just for demo")


abc()
# f = handle_exceptions(exceptions=[FakeException])  # decorator
# g = f(abc)  # decorator(abc) = __inner__
# g()
