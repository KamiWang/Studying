#!/usr/bin/env python

import app

if __name__ == '__main__':
    server = app.create_server(None)
    server.run(debug=True)
