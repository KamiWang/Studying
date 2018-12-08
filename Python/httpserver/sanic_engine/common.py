import math

import sanic.response


class CommonReply:
    def __init__(self):
        self.code = 0

    def json(self):
        return sanic.response.json(self.__dict__)


def _fetch_arg(request, field, ignore, arg_type):
    if field not in request.args:
        if ignore:
            return None
        else:
            raise ValueError(f"'{field}' not found")

    if arg_type is float:
        if request.args[field][0] == "e":
            return math.e
        elif request.args[field][0] == "pi":
            return math.pi
    elif arg_type is list:
        return request.args[field]

    try:
        result = arg_type(request.args[field][0])
    except ValueError:
        raise ValueError(f"'{field}' must be {arg_type.__name__}")

    return result


def fetch_str(request, field, ignore=False, default=None):
    res = _fetch_arg(request, field, ignore, str)
    return default if res is None else res


def fetch_int(request, field, ignore=False, default=None):
    res = _fetch_arg(request, field, ignore, int)
    return default if res is None else res


def fetch_float(request, field, ignore=False, default=None):
    res = _fetch_arg(request, field, ignore, float)
    return default if res is None else res


def get_function_param(request, func):
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

        res = _fetch_arg(request, field, ignore, field_type)

        if res is None:
            params[field] = default
        else:
            params[field] = res

    return params
