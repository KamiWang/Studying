from flask import Flask


def create_server(config_name):
    app = Flask(__name__)
    from .main import blue_print as main_blueprint
    app.register_blueprint(main_blueprint)

    from .module1 import blue_print as module1_blueprint
    app.register_blueprint(module1_blueprint, url_prefix='/md1')

    return app
