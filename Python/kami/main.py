#!/usr/bin/env python


import xsanic
from common.xconfig import XConfig

config = XConfig("./config.ini")


def start_http_server():
    http_server_config = config["http_server"]
    if http_server_config.getboolean("run"):
        xsanic.run(http_server_config.get("ip"),
                   http_server_config.getint("port"))


if "__main__" == __name__:
    start_http_server()
