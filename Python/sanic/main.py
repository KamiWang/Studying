#!/usr/bin/env python

from sanic import Sanic
import sanic.response as res
import sa_math

server = Sanic(__name__)


@server.route("/")
async def index(request):
    return res.text("Hello World")


if "__main__" == __name__:
    server.blueprint(sa_math.bp)
    server.run(host="127.0.0.1", port=80)
