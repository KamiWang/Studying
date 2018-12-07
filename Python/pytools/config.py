from configparser import ConfigParser
from pytools.filesystem import join_exec_path
from pytools.singleton import singleton


@singleton
class ConfigLoader:
    def __init__(self):
        self.config = ConfigParser()

    def __getattr__(self, item):
        return self.config[item]

    def load(self, path):
        self.config.read(join_exec_path(path))
