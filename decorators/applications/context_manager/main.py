# we will replicate contextlib.contextmanager
from unittest import mock


def contextmanager(func):
    pass


@contextmanager
def create_connection():
    mocked_connection = mock.Mock()
    try:
        yield mocked_connection
    except Exception as e:
        print("got error", e)
    finally:
        mocked_connection.close()
