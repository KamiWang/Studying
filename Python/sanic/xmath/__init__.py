from sanic import Blueprint
import xmath.index

bp = Blueprint.group(xmath.index.bp)
