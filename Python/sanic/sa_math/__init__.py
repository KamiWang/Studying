from sanic import Blueprint
import sa_math.test

bp = Blueprint.group(sa_math.test.bp)
