from flask import Blueprint

blue_print = Blueprint("main", __name__)


@blue_print.route("/")
def index():
    return "Hello World!"
