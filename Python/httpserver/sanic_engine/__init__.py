import sanic

from httpserver.sanic_engine import math_route
from pytools.config import ConfigLoader
from archive.mysql_engine import MySQLEngine

app = sanic.Sanic(__name__)
app.blueprint(math_route.bp)

MySQL: MySQLEngine = None


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
    return sanic.response.json({"code": 1, "error": exception.__class__.__name__, "details": str(exception)})


@app.listener('before_server_start')
async def setup_db(app, loop):
    config = ConfigLoader().mysql
    global MySQL
    MySQL = MySQLEngine(config["ip"], config["port"], config["user"], config["password"], config["schema"])
    await MySQL.initialize()


@app.listener('after_server_stop')
async def close_db(app, loop):
    global MySQL
    await MySQL.destroy()
