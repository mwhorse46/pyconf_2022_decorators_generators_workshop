# chain multiple decorators
# we will cache and log arguments at once

def cache(func):
    c_ = {}

    def __inner__(*args):
        res = None
        if v := c_.get(args):
            __inner__.cache_hit += 1
            res = v
        else:
            __inner__.cache_miss += 1
            res = func(*args)
            c_[args] = res
        return res
    __inner__.cache_hit = 0
    __inner__.cache_miss = 0
    return __inner__


def log(func):
    def __inner_log__(*args, **kwargs):
        print(f"{args=} {kwargs=}")
        func(*args, **kwargs)
        __inner_log__.cache_hit = func.cache_hit
        __inner_log__.cache_miss = func.cache_miss
    return __inner_log__


@log
@cache
def abc(*args):
    return sum(args)


abc(1)
# abc(1, 2)
# abc(1, 2)
# abc(1, 2, 3)
# print(abc.cache_hit, abc.cache_miss)

# a = log(cache(abc))

# f = cache(abc) # __inner__
# b = log(f) # __inner__ , returns __inner_log__
# abc == __inner_log__
