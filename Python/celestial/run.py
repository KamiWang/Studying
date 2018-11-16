#!/usr/bin/env python

import web_sanic
from configparser import ConfigParser
from common.filesystem import exec_dir


if "__main__" == __name__:
    config = ConfigParser()
    config.read(exec_dir() + "config.ini")

    ip = config.get("httplistener", "ip")
    port = config.getint("httplistener", "port")

    web_sanic.run(ip, port)
