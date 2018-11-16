#!/usr/bin/env python

import web_sanic
from configparser import ConfigParser
from common.filesystem import dir_path


if "__main__" == __name__:
    config = ConfigParser()
    config.read(dir_path(__file__) + "config.ini")
    
    ip = config.get("httplistener", "ip")
    port = config.getint("httplistener", "port")

    web_sanic.run(ip, port)
