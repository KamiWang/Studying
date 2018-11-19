from configparser import ConfigParser

from common.filesystem import exec_dir, path_join


class ConfigLoader:
    def __init__(self, path):
        self.config = ConfigParser()
        self.config.read(path_join(exec_dir(), path))
        self.section = ""

    def __getitem__(self, index):
        return self.config[self.section][index]

    def select_section(self, section):
        self.section = section
