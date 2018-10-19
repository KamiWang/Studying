#!/usr/bin/env python
# 简单工厂模式(静态工厂模式)

from abc import ABCMeta, abstractmethod


class Fruit(metaclass=ABCMeta):
    @abstractmethod
    def GetName(self): pass


class Apple(Fruit):
    def GetName(self):
        return "苹果"


class Banana(Fruit):
    def GetName(self):
        return "香蕉"


class Orange(Fruit):
    def GetName(self):
        return "桔子"


class FruitFactory:
    @classmethod
    def CreateClass(cls, type_name) -> Fruit:
        if "苹果" == type_name:
            return Apple()
        elif "香蕉" == type_name:
            return Banana()
        elif "桔子" == type_name:
            return Orange()



if "__main__" == __name__:
    print(FruitFactory.CreateClass("苹果").GetName())
    print(FruitFactory.CreateClass("香蕉").GetName())
    print(FruitFactory.CreateClass("桔子").GetName())
