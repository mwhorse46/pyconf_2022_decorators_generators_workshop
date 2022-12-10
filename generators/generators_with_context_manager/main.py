# creating custom context managers using comprehensions
from contextlib import contextmanager


@contextmanager
def a():
    yield 1


with a() as a_:
    print(a_)
