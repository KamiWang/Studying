import math

from sanic import Blueprint

import exception as expt
from sanic_common import CommonReply

bp = Blueprint(__name__, url_prefix='')


@bp.route("")
async def help(req):
    reply = CommonReply()
    reply.api_list = list()
    for route in bp.routes:
        if route.uri:
            reply.api_list.append(route.uri)
    return reply.json


@bp.route("plus")
async def plus(req):
    x = req.fetch_float("x")
    y = req.fetch_float("y")
    reply = CommonReply()
    reply.result = x + y
    return reply.json


@bp.route("minus")
async def minus(req):
    x = req.fetch_float("x")
    y = req.fetch_float("y")
    reply = CommonReply()
    reply.result = x - y
    return reply.json


@bp.route("multiply")
async def multiply(req):
    x = req.fetch_float("x")
    y = req.fetch_float("y")
    reply = CommonReply()
    reply.result = x * y
    return reply.json


@bp.route("divide")
async def divide(req):
    x = req.fetch_float("x")
    y = req.fetch_float("y")
    reply = CommonReply()
    reply.result = x / y
    return reply.json


@bp.route("divideExactly")
async def divide_exactly(req):
    x = req.fetch_float("x")
    y = req.fetch_float("y")
    reply = CommonReply()
    reply.result = x // y
    reply.remainder = x % y
    return reply.json


@bp.route("factorial")
async def factorial(req):
    x = req.fetch_int("x")
    reply = CommonReply()
    reply.result = math.factorial(x)
    return reply.json
