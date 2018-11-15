import math

from sanic import Blueprint

import exception as expt
import sanic_common as sc
import common as com
import xmath.math_base as xmb

bp = Blueprint(__name__, url_prefix='')


@bp.route("")
async def help(req):
    reply = sc.CommonReply()
    reply.api_list = list()
    for route in bp.routes:
        if route.uri:
            reply.api_list.append(route.uri)
    return reply.json


@bp.route("plus")
async def plus(req):
    a = req.fetch_float("a")
    b = req.fetch_float("b")
    reply = sc.CommonReply()
    reply.result = a + b
    return reply.json


@bp.route("minus")
async def minus(req):
    a = req.fetch_float("a")
    b = req.fetch_float("b")
    reply = sc.CommonReply()
    reply.result = a - b
    return reply.json


@bp.route("multiply")
async def multiply(req):
    a = req.fetch_float("a")
    b = req.fetch_float("b")
    reply = sc.CommonReply()
    reply.result = a * b
    return reply.json


@bp.route("divide")
async def divide(req):
    a = req.fetch_float("a")
    b = req.fetch_float("b")
    reply = sc.CommonReply()
    reply.result = a / b
    return reply.json


@bp.route("divideExactly")
async def divide_exactly(req):
    a = req.fetch_float("a")
    b = req.fetch_float("b")
    reply = sc.CommonReply()
    reply.result = a // b
    reply.remainder = a % b
    return reply.json


@bp.route("factorial")
async def factorial(req):
    a = req.fetch_int("a")
    reply = sc.CommonReply()
    reply.result = math.factorial(a)
    return reply.json


@bp.route("sqrt")
async def sqrt(req):
    a = req.fetch_float("a")
    reply = sc.CommonReply()
    reply.result = math.sqrt(a)
    return reply.json


@bp.route("square")
async def square(req):
    a = req.fetch_float("a")
    n = req.fetch_float("n", ignore=True, default=2.0)
    reply = sc.CommonReply()
    reply.result = a**n
    return reply.json


@bp.route(com.function_name_capitalize(xmb.radix_convert))
async def radix_convert(req):
    params = req.get_function_param(xmb.radix_convert)
    reply = sc.CommonReply()
    reply.result = xmb.radix_convert(**params)
    return reply.json
