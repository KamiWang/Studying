import sanic.response as sanJson
from sanic.exceptions import SanicException


class ErrorCode:
    # 未知错误
    SYSTEM_ERROR = (-1, "System Error")
    # 缺少参数
    ARGUMENT_NOT_FOUND = (10000, "Argument Not Found:")
    # 参数错误
    INVALIDE_PARAMETER = (10001, "Invalide Parameter")
    # 数值错误
    VALUE_ERROR = (10002, "Value Error")

    # 玩家授权失败
    AUTHORIZE_INVALID = (20000, "Permission Denied")


class ExceptionEx(SanicException):
    def __init__(self, err_code, detail=""):
        super().__init__(err_code[1], err_code[0])
        self.detail = detail

    @property
    def json(self):
        return sanJson.json({"code": self.status_code, "error": str(self),  "details": self.detail})


def process_exception(req, ex):
    if isinstance(ex, ExceptionEx):
        return ex.json
    elif isinstance(ex, SanicException):
        return sanJson.json({"code": ex.status_code, "error": ex.__class__.__name__, "details": str(ex)})
    elif isinstance(ex, ValueError):
        return sanJson.json({"code": ErrorCode.VALUE_ERROR[0], "error": ErrorCode.VALUE_ERROR[1], "details": str(ex)})
    else:
        return sanJson.json({"code": ErrorCode.SYSTEM_ERROR[0], "error": ex.__class__.__name__, "details": str(ex)})
