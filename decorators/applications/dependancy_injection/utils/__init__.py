from functools import wraps
from typing import Any, TypeVar
from flask import Request, request
from inspect import Signature, signature, Parameter

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


def is_base_class(cls_obj) -> bool:
    """
    Function to check of cls object is a class and 
    subclass of BaseDependency
    """
    return cls_obj.__class__ == type \
        and issubclass(cls_obj, BaseDependency)


def check_for_qualification(obj) -> tuple[bool, bool, bool]:
    """Function to check if object qualifies 
    to be injected

    Args:
        obj (Any): Object to be verified

    Returns:
        tuple[bool, bool, bool]: returns if object is qualified, is a class, is an instance
    """
    # check if obj is class
    iscls_ = is_base_class(obj)
    # checks if obj is an instance of BaseDependency
    # only if obj is not a subclass of BaseDependency
    isinstance_ = False if iscls_ else isinstance(obj, BaseDependency)
    # check if object is not empty
    # since parameter.default or parameter.annotation is passed
    # if not set, it defaults to `Parameter.empty`
    if obj != Parameter.empty and \
            (iscls_ or isinstance_):
        return True, iscls_, isinstance_
    return False, iscls_, isinstance_


def inject(func: callable):
    sig = get_signature(func=func)

    @wraps(func)
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
