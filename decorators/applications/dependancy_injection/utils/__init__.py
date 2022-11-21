from inspect import Signature, signature, Parameter
from flask import Request, request
from typing import Any, Callable, TypeVar

T = TypeVar('T')


class BaseDependency(object):
    type_: str = "args"
    message: str = "query params"

    def __init__(self, name: str = None) -> None:
        self.__name = name

    def __call__(self, name: str = None) -> Any:
        resolved_name = self.__name or name
        val = self.__resolve(request, resolved_name)
        if not val:
            raise Exception(f"Missing {self.message} {resolved_name}")
        return val

    def __resolve(self, request_: Request, name: str):
        return getattr(request_, self.type_).get(name)


class Query(BaseDependency):
    pass


class Path(BaseDependency):
    type_: str = "view_args"
    message: str = "URL argument"


class Body(BaseDependency):
    type_: str = "json"
    message: str = "Body"


def get_signature(func) -> Signature:
    return signature(func)


def isclass(cls) -> bool:
    return cls.__class__ == type


def check_for_qualification(obj):
    iscls_ = isclass(obj)
    isinstance_ = isinstance(obj, BaseDependency)
    if obj != Parameter.empty and \
        ((iscls_ and issubclass(obj, BaseDependency))
         or isinstance_):
        return True, iscls_, isinstance_
    return False, iscls_, isinstance_


def inject(func: callable):
    sig = get_signature(func=func)

    def __inner__(*args, **kwargs):
        k_ = {}
        for name, param in sig.parameters.items():
            if (r := check_for_qualification(param.default)) and r[0]:
                (_, iscls, _) = r
                if iscls:
                    k_[name] = param.default()(name)
                else:
                    k_[name] = param.default(name)
            elif (r := check_for_qualification(param.annotation)) and r[0]:
                (_, iscls, _) = r
                if iscls:
                    k_[name] = param.annotation()(name)
                else:
                    k_[name] = param.annotation(name)
            return func(*args, **k_, **kwargs)
    return __inner__
