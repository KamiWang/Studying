#!/usr/bin/env python

import pytools.filesystem as fs

if __name__ == "__main__":
    tree = fs.FileTree(fs.join_current_path(__file__, "./"))

    result = tree.root.delete_all([".idea", "__pycache__"])
    print(f"删除了{result}个结果")
