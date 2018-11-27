#!/usr/bin/env python

import xsanic
from common.xconfig import XConfig

import crawler


def start_http_server():
    http_config = XConfig("./config/httpserver.ini")
    xsanic.run(http_config["listener"]["ip"], http_config["listener"]["port"])


if "__main__" == __name__:
    urls = ["https://www.qq.com"]
    crawler.run(urls)

    start_http_server()
