# coroutines in Python
def a():
    i = 0
    while True:
        n = yield i
        i = n**2


a_ = a()
print(next(a_))
print(a_.send(2))
print(a_.send(3))
print(a_.send(4))
