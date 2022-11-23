# chain multiple decorators
# we will cache and log arguments at once

def cache(func):
    pass
    # c_ = {}
    # func.cache_hit = 0
    # func.cache_miss = 0

    # def __inner__(self, *args, **kwargs):
    #     res = None
    #     if v := c_.get((args, kwargs)):
    #         func.cache_hit += 1
    #         res = v
    #     else:
    #         func.cache_miss += 1
    #         res = func(*args, **kwargs)
    #         c_[(args, kwargs)] = res
    #     return res
    # return __inner__


def log(func):
    pass


@log
@cache
def abc(*args):
    return sum(args)


abc(1)
abc(1, 2)
abc(1, 2)
abc(1, 2, 3)
print(abc.cache_hit, abc.cache_miss)
