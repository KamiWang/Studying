#!/usr/bin/env python


import httpserver.sanic_engine as http_engine
from pytools.config import ConfigLoader


def run():
    config = ConfigLoader().listener
    if config.getboolean("run"):
        http_engine.run(config["ip"], config["port"])




