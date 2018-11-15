import exception as expt
import sanic.response as sanJson


class CommonReply:
    def __init__(self):
        self.code = 0

    @property
    def json(self):
        return sanJson.json(self.__dict__)


def __fetch_arg(request, field, ignore, arg_type):
    if field not in request.args:
        if ignore:
            return None
        else:
            raise expt.ExceptionEx(expt.ErrorCode.ARGUMENT_NOT_FOUND, f"'{field}' not found")
    try:
        result = arg_type(request.args[field][0])
    except ValueError:
        raise expt.ExceptionEx(expt.ErrorCode.INVALIDE_PARAMETER, f"'{field}' must be {arg_type.__name__}")

    return result


def fetch_str(request, field, ignore=False, default=None):
    res = __fetch_arg(request, field, ignore, str)
    return res if res else default


def fetch_int(request, field, ignore=False, default=None):
    res = __fetch_arg(request, field, ignore, int)
    return res if res else default


def fetch_float(request, field, ignore=False, default=None):
    res = __fetch_arg(request, field, ignore, float)
    return res if res else default
