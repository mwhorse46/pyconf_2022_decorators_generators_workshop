# class based decorator with arguments

# We will implement a decorator that would
# iterate a function multiple times
# provided by user
class Iterate:
    def __init__(self, iterate: int = 1) -> None:
        self._iterate = iterate
        self.func = None

    def __call__(self, func: callable):
        self.func = func
        return self.iterate

    def iterate(self, *args, **kwargs):
        for i in range(self._iterate):
            self.func(*args, **kwargs)


@Iterate(5)  # instance of Iterate
def abc():
    print("Hello")


abc()
