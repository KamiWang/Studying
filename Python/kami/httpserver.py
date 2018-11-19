#!/usr/bin/env python

import xsanic
from common.config_manager import ConfigManager


def start_server():
    config = ConfigManager("./config/httpserver.ini")
    config.select_section("listener")
    xsanic.run(config["ip"], config["port"])


if "__main__" == __name__:
    start_server()
