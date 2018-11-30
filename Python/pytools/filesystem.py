#!/usr/bin/env python


import os
import sys


def join_exec_path(path):
    return normpath_join(exec_path(), path)


def join_current_path(file_path, path):
    return normpath_join(os.path.dirname(os.path.abspath(file_path)), path)


def normpath_join(*path):
    return os.path.normpath("/".join(path)).replace('\\', '/')


def exec_path():
    return os.path.dirname(sys.argv[0]).replace('\\', '/')


class FileTree:
    def __init__(self, path):
        if os.path.exists(path):
            self.abspath = os.path.abspath(path)
            self.directory = os.path.dirname(self.abspath).replace('\\', '/')
            self.node = FileNode(self.abspath, None, self)
        else:
            raise ValueError("'path' is not exist")

    def __getitem__(self, item):
        return self.node[item]

    def __iter__(self):
        for it in self.node:
            yield it

    @property
    def path(self):
        return self.node.path

    @property
    def root(self):
        return self.node

    def print_tree(self):
        self.node.print_children(0)

    def refresh(self):
        self.__init__(self.abspath)


class FileNode:
    def __init__(self, path, parent, tree):
        self.name = os.path.basename(path)
        self.parent = parent
        self.tree = tree
        self.children = None
        self.is_dir = os.path.isdir(path)
        if self.is_dir:
            self._traversal_children(path)

    def __getitem__(self, item):
        return self.children[item]

    def __iter__(self):
        yield self
        for key in self.children:
            if self.children[key].is_dir:
                for it in self.children[key]:
                    yield it
            else:
                yield self.children[key]

    def print_children(self, layer):
        print('|' + '-' * layer + self.name)
        if self.children is None:
            return
        for key in self.children:
            if self.children[key].is_dir:
                self.children[key].print_children(layer + 1)
            else:
                print('|' + '-' * (layer + 1) + key)

    def rename(self, name):
        os.rename(self.path, os.path.join(self.directory, name))
        if self.parent is not None:
            self.parent.children[name] = self.parent.children.pop(self.name)
        self.name = name

    @property
    def path(self):
        path_list = list()
        node = self
        while node:
            path_list.append(node.name)
            node = node.parent
        path_list.append(self.tree.directory)
        return "/".join(path_list[::-1])

    @property
    def directory(self):
        if self.parent is None:
            return self.tree.directory
        else:
            return self.parent.path

    @property
    def extension_name(self):
        return os.path.splitext(self.name)[1]

    @property
    def filename(self):
        return os.path.splitext(self.name)[0]

    def _traversal_children(self, path):
        self.children = dict()
        for child_name in os.listdir(path):
            child_path = os.path.join(path, child_name)
            node = FileNode(child_path, self, self.tree)
            self.children[child_name] = node


if "__main__" == __name__:
    print(join_exec_path("./"))
