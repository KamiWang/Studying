#!/usr/bin/env python

import xsanic
from common.xconfig import XConfig


def start_server():
    http_config = XConfig("./config/httpserver.ini")
    xsanic.run(http_config["listener"]["ip"], http_config["listener"]["port"])


if "__main__" == __name__:
    start_server()
