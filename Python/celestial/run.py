#!/usr/bin/env python

import web_sanic
from common.config_loader import ConfigLoader


if "__main__" == __name__:
    config = ConfigLoader("./config.ini")
    config.select_section("httplistener")

    web_sanic.run(config["ip"], config["port"])
