#!/usr/bin/env python

import sanic

import authorization
import exception
import xmath

server = sanic.Sanic(__name__)


@server.route("/")
async def index(req):
    return sanic.response.text("Hello World")


@server.middleware("request")
async def when_request(req):
    authorization.check_request_for_authorization_status(req)


@server.middleware("response")
async def when_response(req, res):
    pass


@server.exception(Exception)
async def when_exception(req, ex):
    return exception.process_exception(req, ex)


if "__main__" == __name__:
    server.blueprint(xmath.bp)
    server.run(host="0.0.0.0", port=80, debug=True)
