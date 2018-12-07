import math

import sanic.request
from sanic.response import json


class CommonReply:
    def __init__(self):
        self.code = 0

    @property
    def json(self):
        return json(self.__dict__)


def _fetch_arg(self, field, ignore, arg_type):
    if field not in self.args:
        if ignore:
            return None
        else:
            raise ValueError(f"'{field}' not found")

    if arg_type is float:
        if self.args[field][0] == "e":
            return math.e
        elif self.args[field][0] == "pi":
            return math.pi
    elif arg_type is list:
        return self.args[field]

    try:
        result = arg_type(self.args[field][0])
    except ValueError:
        raise ValueError(f"'{field}' must be {arg_type.__name__}")

    return result


def fetch_str(self, field, ignore=False, default=None):
    res = self._fetch_arg(field, ignore, str)
    return default if res is None else res


def fetch_int(self, field, ignore=False, default=None):
    res = self._fetch_arg(field, ignore, int)
    return default if res is None else res


def fetch_float(self, field, ignore=False, default=None):
    res = self._fetch_arg(field, ignore, float)
    return default if res is None else res


def get_function_param(self, func):
    params = dict()

    default_len = len(func.__defaults__) if func.__defaults__ else 0
    default_index = func.__code__.co_argcount - default_len

    for i in range(func.__code__.co_argcount):
        field = func.__code__.co_varnames[i]
        default = None
        ignore = False
        if default_index <= i:
            default = func.__defaults__[i - default_index]
            ignore = True

        field_type = str
        if field in func.__annotations__:
            field_type = func.__annotations__[field]

        res = self._fetch_arg(field, ignore, field_type)

        if res is None:
            params[field] = default
        else:
            params[field] = res

    return params


sanic.request._fetch_arg = _fetch_arg
sanic.request.fetch_str = fetch_str
sanic.request.fetch_int = fetch_int
sanic.request.fetch_float = fetch_float
sanic.request.get_function_param = get_function_param
