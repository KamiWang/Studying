#!/usr/bin/env python

import os
import codecs


class FObject:
    def __init__(self, path):
        self._path = path.replace('\\', '/').lstrip('/')

    def __iter__(self):
        yield self

    @property
    def is_folder(self):
        return False

    @property
    def name(self):
        return os.path.basename(self._path)

    @property
    def directory(self):
        return os.path.dirname(self._path)

    @property
    def extension_name(self):
        return os.path.splitext(self._path)[1]

    def rename(self, new_name):
        new_path = self.directory + "/" + new_name
        os.rename(self._path, new_path)
        self._path = new_path

    def print_file_tree(self, layers=0):
        print('|' + '-'*layers + self.name)

    def refresh(self):
        self.__init__(self._path)


class Folder(FObject):
    def __init__(self, path=None):
        FObject.__init__(self, path)
        if not os.path.isdir(self._path):
            raise Exception("未找到该文件" + self._path)
        self.file_list = []
        self.__traversal_add_file()

    @property
    def is_folder(self):
        return True

    def print_file_tree(self, layer=0):
        FObject.print_file_tree(self, layer)
        for fobj in self.file_list:
            fobj.print_file_tree(layer+1)

    def __iter__(self):
        yield self
        for f in self.file_list:
            if f.is_folder:
                for it in f.__iter__():
                    yield it
            else:
                yield f

    def __traversal_add_file(self):
        for name in os.listdir(self._path):
            path_name = os.path.join(self._path, name)
            if os.path.isdir(path_name):
                self.file_list.append(Folder(path_name))
            else:
                self.file_list.append(File(path_name))


class File(FObject):
    def __init__(self, path=None):
        FObject.__init__(self, path)
        if not os.path.isfile(self._path):
            raise Exception("未找到该文件" + self._path)


def get_file_tree(path)->Folder:
    return Folder(path)


if "__main__" == __name__:
    hello = File(r"C:\Users\FH\Desktop\new\2.txt")

    hello.print_file_tree()
