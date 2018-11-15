import sanic.response as sanJson
from sanic.exceptions import SanicException


class ErrorCode:
    # 未知错误
    UNKNOWN_ERROR = (-1, "unknown error")
    # 玩家授权失败
    AUTHORIZE_INVALID = (10000, "Permission Denied")
    # 缺少参数
    ARGUMENT_NOT_FOUND = (20000, "argument not found:")
    # 参数错误
    INVALIDE_PARAMETER = (20001, "invalide parameter")

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
        return sanJson.json({"code": ex.status_code, "error": str(ex)})
    else:
        return sanJson.json({"code": ErrorCode.UNKNOWN_ERROR[0], "error": str(ex)})
