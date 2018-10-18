from flask import Blueprint

blue_print = Blueprint("module1", __name__)


@blue_print.route("/")
def index():
    return "module1"
