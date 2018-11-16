#!/usr/bin/env python

import os
import re
import sys


def exec_dir():
    return os.path.dirname(sys.argv[0]).replace('\\', '/') + '/'


def path_join(*names):
    return "/".join(names)


class FObject:
    def __init__(self, path):
        self._path = path.replace('\\', '/').lstrip('/')
        self._parent = None

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
    def path(self):
        return self._path

    @property
    def extension_name(self):
        return os.path.splitext(self._path)[1]

    @property
    def is_root(self):
        return False if self._parent else True

    @property
    def parent(self):
        return self._parent

    @property
    def root(self):
        obj = self
        while obj._parent:
            obj = obj._parent
        return obj

    def rename(self, new_name):
        new_path = path_join(self.directory, new_name)
        os.rename(self._path, new_path)
        self._path = new_path

    def print_file_tree(self,  layer=0):
        print('|' + '-'*layer + self.name)

    def refresh(self):
        self.__init__(self._path)


class Folder(FObject):
    def __init__(self, path=None):
        FObject.__init__(self, path)
        if not os.path.isdir(self._path):
            raise Exception("Folder not found:" + self._path)
        self._file_list = []
        self.__traversal_add_file()

    def __getitem__(self, index)->FObject:
        if isinstance(index, int):
            return self._file_list[index]
        elif isinstance(index, str):
            return self.children(index)
        else:
            raise Exception("Unknown index")

    def __len__(self):
        return len(self._file_list)

    def __iter__(self):
        yield self
        for f in self._file_list:
            if f.is_folder:
                for it in f.__iter__():
                    yield it
            else:
                yield f

    @property
    def is_folder(self):
        return True

    def children(self, name=None)->FObject:
        if name:
            for f in self._file_list:
                if f.name == name:
                    return f
            raise Exception("File not found:" + path_join(self._path, name))
        else:
            return self._file_list

    def print_file_tree(self, layer=0):
        FObject.print_file_tree(self, layer=layer)
        for fobj in self._file_list:
            fobj.print_file_tree(layer=layer+1)

    def __traversal_add_file(self):
        try:
            for name in os.listdir(self._path):
                path_name = path_join(self._path, name)
                fobj = None
                if os.path.isdir(path_name):
                    fobj = Folder(path_name)
                else:
                    fobj = File(path_name)
                fobj._parent = self
                self._file_list.append(fobj)
        except Exception:
            return


class File(FObject):
    def __init__(self, path=None):
        FObject.__init__(self, path)
        if not os.path.isfile(self._path):
            raise Exception("未找到该文件" + self._path)

    def read_all(self):
        with open(self._path, "r") as openfile:
            return openfile.read()


if __name__ == "__main__":
    print(__file__)
