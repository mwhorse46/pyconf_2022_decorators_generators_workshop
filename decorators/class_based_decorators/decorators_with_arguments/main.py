# class based decorator with arguments

# We will implement a decorator that would
# iterate a function multiple times
# provided by user
class Iterate:
    pass


@Iterate(5)
def abc():
    print("Hello")


abc()
