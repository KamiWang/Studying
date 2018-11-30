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

    @property
    def path(self):
        return self.node.path

    @property
    def root(self):
        return self.node

    def print_tree(self):
        if self.node is None:
            return
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

    def print_children(self, layer=0):
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

    def delete(self):
        for root, dirs, files in os.walk(self.path):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.path)
        if self.parent is None:
            self.tree.node = None
        else:
            self.parent.children.pop(self.name)

    def file_count(self, include_dir=False):
        if self.is_dir:
            count = 0
            for it in self:
                if not include_dir and it.is_dir:
                    continue
                count += 1
            return count
        else:
            return 1

    @property
    def size(self):
        if self.is_dir:
            size = 0
            for it in self:
                size += os.path.getsize(it.path)
            return size
        else:
            return os.path.getsize(self.path)

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
        try:
            for child_name in os.listdir(path):
                child_path = os.path.join(path, child_name)
                node = FileNode(child_path, self, self.tree)
                self.children[child_name] = node
        except PermissionError:
            return


if "__main__" == __name__:
    root = FileTree("D:\腾讯游戏\英雄联盟").root
    print(root.file_count(True))
