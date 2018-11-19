#!/usr/bin/env python

import web_sanic
from common.config_manager import ConfigManager


def start_server():
    config = ConfigManager("./config/httpserver.ini")
    config.select_section("listener")
    web_sanic.run(config["ip"], config["port"])


if "__main__" == __name__:
    start_server()