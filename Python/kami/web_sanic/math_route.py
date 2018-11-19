from sanic import Blueprint

import xmath.basic as xmb
from common.string_tools import format_func_name_to_camel as f2c
from web_sanic.sanic_common import CommonReply

bp = Blueprint(__name__, url_prefix='math/')


@bp.route("")
async def help(req):
    reply = CommonReply()
    reply.api_list = list()
    for route in bp.routes:
        if route.uri:
            reply.api_list.append(route.uri)
    return reply.json


@bp.route(f2c(xmb.plus))
async def plus(request):
    params = request.get_function_param(xmb.plus)
    reply = CommonReply()
    reply.result = xmb.plus(**params)
    return reply.json


@bp.route(f2c(xmb.minus))
async def minus(request):
    params = request.get_function_param(xmb.minus)
    reply = CommonReply()
    reply.result = xmb.minus(**params)
    return reply.json


@bp.route(f2c(xmb.multiply))
async def multiply(request):
    params = request.get_function_param(xmb.multiply)
    reply = CommonReply()
    reply.result = xmb.multiply(**params)
    return reply.json


@bp.route(f2c(xmb.divide))
async def divide(request):
    params = request.get_function_param(xmb.divide)
    reply = CommonReply()
    reply.result = xmb.divide(**params)
    return reply.json


@bp.route(f2c(xmb.divide_exactly))
async def divide_exactly(request):
    params = request.get_function_param(xmb.divide_exactly)
    reply = CommonReply()
    result = xmb.divide_exactly(**params)
    reply.result = result[0]
    reply.remainder = result[1]
    return reply.json


@bp.route(f2c(xmb.factorial))
async def factorial(request):
    params = request.get_function_param(xmb.factorial)
    reply = CommonReply()
    reply.result = xmb.factorial(**params)
    return reply.json


@bp.route(f2c(xmb.sqrt))
async def sqrt(request):
    params = request.get_function_param(xmb.sqrt)
    reply = CommonReply()
    reply.result = xmb.sqrt(**params)
    return reply.json


@bp.route(f2c(xmb.square))
async def square(request):
    params = request.get_function_param(xmb.square)
    reply = CommonReply()
    reply.result = xmb.square(**params)
    return reply.json


@bp.route(f2c(xmb.radix_convert))
async def radix_convert(request):
    params = request.get_function_param(xmb.radix_convert)
    reply = CommonReply()
    reply.result = xmb.radix_convert(**params)
    return reply.json
