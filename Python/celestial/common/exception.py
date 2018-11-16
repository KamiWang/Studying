import json


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


class ExceptionEx(Exception):
    def __init__(self, err_code, error_msg, detail=""):
        self.code = err_code
        self.error = error_msg
        self.detail = detail

    @property
    def json(self):
        return json.dumps(self.__dict__)
