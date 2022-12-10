# simple class based decorator
from time import sleep, time


class Log_time(object):
    def __init__(self, func) -> None:
        self.func = func
        self.__doc__ = func.__doc__
        self.__class__.__name__ = func.__name__

    def __call__(self, *args, **kwds):
        t = time()
        self.func(*args, **kwds)
        t2 = time()
        print(f"function took {t2-t} seconds")


@Log_time
def abc():
    sleep(1)


abc()
# l = Log_time(abc)
# l()
