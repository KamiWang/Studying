#!/usr/bin/env python


from configparser import ConfigParser
import httpserver.sanic_engine as http_engine
from pytools.filesystem import join_current_path


def run():
    config = ConfigParser()
    config.read(join_current_path(__file__, "./config.ini"))
    ip = config["listener"]["ip"]
    port = config["listener"]["port"]

    http_engine.run(ip, port)


if "__main__" == __name__:
    run()
