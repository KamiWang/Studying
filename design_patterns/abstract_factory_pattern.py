#!/usr/bin/env python
# 抽象工厂模式

from abc import ABCMeta, abstractmethod


class Food(metaclass=ABCMeta):
    @abstractmethod
    def GetName(self): pass


class ApplePie(Food):
    def GetName(self):
        return "苹果派"


class BananaPie(Food):
    def GetName(self):
        return "香蕉派"


class AppleJuice(Food):
    def GetName(self):
        return "苹果汁"


class BananaJuice(Food):
    def GetName(self):
        return "香蕉汁"


class FruitFactory(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def MakePie(cls): pass

    @classmethod
    @abstractmethod
    def MakeJuice(cls): pass


class AppleFactory(FruitFactory):
    @classmethod
    def MakePie(cls):
        return ApplePie()

    @classmethod
    def MakeJuice(cls):
        return AppleJuice()


class BananaFactory(FruitFactory):
    @classmethod
    def MakePie(cls):
        return BananaPie()

    @classmethod
    def MakeJuice(cls):
        return BananaJuice()


print(AppleFactory.MakeJuice().GetName())
print(AppleFactory.MakePie().GetName())

print(BananaFactory.MakeJuice().GetName())
print(BananaFactory.MakePie().GetName())
