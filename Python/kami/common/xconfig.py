from configparser import ConfigParser

from common.filesystem import exec_dir, path_join


class XConfig:
    def __init__(self, path):
        self.config = ConfigParser()
        self.config.read(path_join(exec_dir(), path))

    def __getitem__(self, index):
        return self.config[index]