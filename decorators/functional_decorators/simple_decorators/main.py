# simple functional decorator
from time import sleep, time
from functools import wraps


def log_time(func):
    @wraps(func)
    def __inner__(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        t2 = time()
        print(f"function {func.__name__} executed for {t2-t} seconds")
    return __inner__


@log_time
def abc():
    t = time()
    sleep(1)
    t2 = time()
    print(f"function kept executing for {t2-t} seconds")


print(abc.__name__)
# func = log_time(abc) # func = __inner__
# func()
# abc = log_time(abc)
