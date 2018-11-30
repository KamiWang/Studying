import sanic
from sanic.response import json

from httpserver.sanic_engine import math_route

app = sanic.Sanic(__name__)
app.blueprint(math_route.bp)


def run(host, port):
    app.run(host, port)


@app.route("/")
async def index(request):
    return sanic.response.text("Hello World !!!")


@app.route("/favicon.ico")
async def favicon(request):
    path = "./resource/icon/favicon.ico"
    return await sanic.response.file(path)


@app.middleware("request")
async def when_request(request):
    # authorization.check_request_for_authorization_status(req)
    pass


@app.middleware("response")
async def when_response(request, response):
    pass


@app.exception(Exception)
async def when_exception(request, exception):
    return process_exception(exception)


def process_exception(exception):
    return json({"code": 1, "error": exception.__class__.__name__, "details": str(exception)})
