#!/usr/bin/env python

import httpserver

from pytools.config import ConfigLoader

if "__main__" == __name__:
    ConfigLoader().load("./config.ini")
    httpserver.run()
