#!/usr/bin/env python
# 原型模式

import copy


class Robot:
    def __init__(self):
        self.name = "原始机器人"
        self.color = ""
        self.data = []

    def print_info(self):
        print("*"*5, self.name, "*"*5)
        print("颜色:", self.color)
        print("数据:", self.data)

    def clone(self):
        return copy.deepcopy(self)


if "__main__" == __name__:
    r0 = Robot()
    r0.color = "red"
    r0.data = [1, 2, 3, [4, 5, 6, [7, 8, 9]]]

    r1 = r0.clone()
    r1.name = "1号机器人"

    r0.data[3][3][0] = -999

    r0.print_info()
    r1.print_info()
