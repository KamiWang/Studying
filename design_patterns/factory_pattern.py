#!/usr/bin/env python
# 工厂模式

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


class FruitFactory(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def MakeFruit(cls): pass


class AppleFactory(FruitFactory):
    @classmethod
    def MakeFruit(cls):
        return Apple()


class BananaFactory(FruitFactory):
    @classmethod
    def MakeFruit(cls):
        return Banana()


class OrangeFactory(FruitFactory):
    @classmethod
    def MakeFruit(cls):
        return Orange()


if "__main__" == __name__:
    print(AppleFactory.MakeFruit().GetName())
    print(BananaFactory.MakeFruit().GetName())
    print(OrangeFactory.MakeFruit().GetName())
