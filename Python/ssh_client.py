#!/usr/bin/env python

import paramiko


class SSHClient:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.ssh = paramiko.SSHClient()

    def __del__(self):
        self.ssh.close()


cc = SSHClient(1,1,1,1)

print("1")