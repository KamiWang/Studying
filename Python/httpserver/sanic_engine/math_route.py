from sanic import Blueprint

import mathematics.base as xmb
from pytools.common import format_function_identifier as ffi
from httpserver.sanic_engine.common import CommonReply

bp = Blueprint(__name__, url_prefix="math/")


@bp.route("")
async def home(request):
    reply = CommonReply()
    reply.api_list = list()
    for route in bp.routes:
        if route.uri:
            reply.api_list.append(route.uri)
    return reply.json


@bp.route(ffi(xmb.plus))
async def plus(request):
    params = request.get_function_param(xmb.plus)
    reply = CommonReply()
    reply.result = xmb.plus(**params)
    return reply.json


@bp.route(ffi(xmb.minus))
async def minus(request):
    params = request.get_function_param(xmb.minus)
    reply = CommonReply()
    reply.result = xmb.minus(**params)
    return reply.json


@bp.route(ffi(xmb.multiply))
async def multiply(request):
    params = request.get_function_param(xmb.multiply)
    reply = CommonReply()
    reply.result = xmb.multiply(**params)
    return reply.json


@bp.route(ffi(xmb.divide))
async def divide(request):
    params = request.get_function_param(xmb.divide)
    reply = CommonReply()
    reply.result = xmb.divide(**params)
    return reply.json


@bp.route(ffi(xmb.divide_exactly))
async def divide_exactly(request):
    params = request.get_function_param(xmb.divide_exactly)
    reply = CommonReply()
    result = xmb.divide_exactly(**params)
    reply.result = result[0]
    reply.remainder = result[1]
    return reply.json


@bp.route(ffi(xmb.factorial))
async def factorial(request):
    params = request.get_function_param(xmb.factorial)
    reply = CommonReply()
    reply.result = xmb.factorial(**params)
    return reply.json


@bp.route(ffi(xmb.square_root))
async def square_root(request):
    params = request.get_function_param(xmb.square_root)
    reply = CommonReply()
    reply.result = xmb.square_root(**params)
    return reply.json


@bp.route(ffi(xmb.square))
async def square(request):
    params = request.get_function_param(xmb.square)
    reply = CommonReply()
    reply.result = xmb.square(**params)
    return reply.json


@bp.route(ffi(xmb.radix_convert))
async def radix_convert(request):
    params = request.get_function_param(xmb.radix_convert)
    reply = CommonReply()
    reply.result = xmb.radix_convert(**params)
    return reply.json
