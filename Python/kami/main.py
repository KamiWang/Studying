#!/usr/bin/env python

import crawler
import xsanic
from common.xconfig import XConfig

config = XConfig("./config.ini")


def start_http_server():
    http_server_config = config["http_server"]
    if http_server_config.getboolean("run") == True:
        xsanic.run(http_server_config.get("ip"), http_server_config.getint("port"))


def start_crawler():
    crawler_config = config["crawler"]
    if crawler_config.getboolean("run") == True:
        crawler.run()


if "__main__" == __name__:
    start_crawler()
    start_http_server()
