#!/usr/bin/env python

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False


class CLineStyle:
    solid = "-"
    dashed = "--"
    dashdot = "-."
    dotted = ":"
    none = " "


class CDataStyle:
    def __init__(self):
        self.color = "black"
        self.label = "data"
        self.linestyle = CLineStyle.solid


class Axes:
    default_style = CDataStyle()

    def __init__(self, axes):
        self.axes: plt.Axes = axes

    def add_plot(self, x, y,  style=default_style):
        self.axes.plot(x, y, **style.__dict__)

    def add_bar(self, x, y,  style=default_style):
        self.axes.bar(x, y,  **style.__dict__)

    def add_scatter(self,  x, y, style=default_style):
        self.axes.scatter(x, y, **style.__dict__)

    def set_facecolor(self, color):
        """设置背景色"""
        self.axes.set_facecolor(color)

    def legend(self, loc=0):
        """
        loc{0:best, 1:upper_right, 2:upper_left, 3:lower_left, 4:lower_right,
        5:right, 6:center_left, 7:center_right, 8:lower_center, 9:upper center, 10:center}
        """
        self.axes.legend(loc=loc)

    def grid(self, is_show):
        """网格"""
        self.axes.grid(is_show)

    def set_xlim(self, x1, x2):
        self.axes.set_xlim(x1, x2)

    def set_ylim(self, y1, y2):
        self.axes.set_ylim(y1, y2)

    def set_xticks(self, ticks, label=None):
        """自己设x轴刻度和标签"""
        self.axes.set_xticks(ticks)
        if label:
            self.axes.set_xticklabels(label)

    def set_yticks(self, ticks, label=None):
        """自己设y轴刻度和标签"""
        self.axes.set_yticks(ticks)
        if label:
            self.axes.set_yticklabels(label)

    def set_title(self, title):
        self.axes.set_title(title)


class Figure:
    def __init__(self, size=None):
        self.figure: plt.Figure = plt.figure(figsize=(10, 10))
        if size:
            self.set_size(*size)

    @staticmethod
    def show():
        plt.show()

    def set_size(self, widht, height):
        """厘米"""
        self.figure.set_size_inches(widht/2.54, height/2.54)

    def add_axes(self, grid=111, custom=None)->Axes:
        """
        grid = [row_count][column_count][num]
        custom = (x,y,width,height) %
        """
        if custom:
            return Axes(self.figure.add_axes(custom))
        else:
            return Axes(self.figure.add_subplot(grid))

    def save(self, path):
        self.figure.savefig(path)


if __name__ == "__main__":
    fig = Figure()
    ax = fig.add_axes()
    ax.add_plot([1, 2, 3, 4], [2, 3, 4, 5])
    ax.grid(True)
    Figure.show()
