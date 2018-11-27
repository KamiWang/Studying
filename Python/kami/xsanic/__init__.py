
import sanic
from sanic.exceptions import SanicException
from sanic.response import json

from common.exception import ExceptionEx, ErrorCode

from xsanic.math_route import bp as mbp

from common.filesystem import exec_dir, path_join


app = sanic.Sanic(__name__)
app.blueprint(mbp)


def run(host, port):
    app.run(host, port)


@app.route("/")
async def index(req):
    return sanic.response.text("Hello World !!!")


@app.route("/favicon.ico")
async def favicon(req):
    path = path_join(exec_dir(), "./resource/icon/favicon.ico")
    return await sanic.response.file(path)


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


def process_exception(request, exception):
    if isinstance(exception, ExceptionEx):
        return json({"code": exception.code, "error": exception.error,  "details": exception.detail})
    elif isinstance(exception, SanicException):
        return json({"code": exception.status_code, "error": exception.__class__.__name__, "details": str(exception)})
    elif isinstance(exception, ValueError):
        return json({"code": ErrorCode.VALUE_ERROR[0], "error": ErrorCode.VALUE_ERROR[1], "details": str(exception)})
    else:
        return json({"code": ErrorCode.SYSTEM_ERROR[0], "error": exception.__class__.__name__, "details": str(exception)})
