import exception as expt
import sanic.response as sanJson
from sanic.request import Request


class CommonReply:
    def __init__(self):
        self.code = 0

    @property
    def json(self):
        return sanJson.json(self.__dict__)


def __fetch_arg(self, field, ignore, arg_type):
    if field not in self.args:
        if ignore == True:
            return None
        else:
            raise expt.ExceptionEx(expt.ErrorCode.ARGUMENT_NOT_FOUND, f"'{field}' not found")
    try:
        result = arg_type(self.args[field][0])
    except ValueError:
        raise expt.ExceptionEx(expt.ErrorCode.INVALIDE_PARAMETER, f"'{field}' must be {arg_type.__name__}")

    return result


def fetch_str(self, field, ignore=False, default=None):
    res = self.__fetch_arg(field, ignore, str)
    return default if res == None else res


def fetch_int(self, field, ignore=False, default=None):
    res = self.__fetch_arg(field, ignore, int)
    return default if res == None else res


def fetch_float(self, field, ignore=False, default=None):
    res = self.__fetch_arg(field, ignore, float)
    return default if res == None else res


def get_function_param(self, func):
    params = dict()

    default_len = len(func.__defaults__) if func.__defaults__ else 0
    default_index = func.__code__.co_argcount - default_len

    for i in range(func.__code__.co_argcount):
        field = func.__code__.co_varnames[i]
        default = None
        ignore = False
        if default_index <= i:
            default = func.__defaults__[i-default_index]
            ignore = True

        field_type = str
        if field in func.__annotations__:
            field_type = func.__annotations__[field]

        res = self.__fetch_arg(field, ignore, field_type)

        if res == None:
            params[field] = default
        else:
            params[field] = res

    return params


Request.__fetch_arg = __fetch_arg
Request.fetch_str = fetch_str
Request.fetch_int = fetch_int
Request.fetch_float = fetch_float
Request.get_function_param = get_function_param
