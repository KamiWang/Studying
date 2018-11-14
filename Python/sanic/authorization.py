import exception as expt

test_flag = False


def check_request_for_authorization_status(req):
    if test_flag:
        raise expt.ExceptionEx(expt.ErrorCode.AUTHORIZE_INVALID)
