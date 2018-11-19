import sanic
from sanic.exceptions import SanicException
from sanic.response import json

import web_sanic.sanic_common as wsc
from web_sanic.math_route import bp as math_bp
from common.exception import ExceptionEx, ErrorCode


app = sanic.Sanic(__name__)
app.blueprint(math_bp)


@app.route("/")
async def index(req):
    return sanic.response.text("Hello World")


@app.middleware("request")
async def when_request(req):
    # authorization.check_request_for_authorization_status(req)
    pass


@app.middleware("response")
async def when_response(request, response):
    pass


@app.exception(Exception)
async def when_exception(request, exception):
    return process_exception(request, exception)


def run(host, port):
    app.run(host, port)


def process_exception(request, exception):
    if isinstance(exception, ExceptionEx):
        return json({"code": exception.code, "error": exception.error,  "details": exception.detail})
    elif isinstance(exception, SanicException):
        return json({"code": exception.status_code, "error": exception.__class__.__name__, "details": str(exception)})
    elif isinstance(exception, ValueError):
        return json({"code": ErrorCode.VALUE_ERROR[0], "error": ErrorCode.VALUE_ERROR[1], "details": str(exception)})
    else:
        return json({"code": ErrorCode.SYSTEM_ERROR[0], "error": exception.__class__.__name__, "details": str(exception)})
