#!/usr/bin/env python


from abc import ABCMeta, abstractmethod






# 建造者模式
def BuilderPattern():
    class IBuilder(metaclass=ABCMeta):
        @abstractmethod
        def CreateA(self): pass

        @abstractmethod
        def CreateB(self): pass

        @abstractmethod
        def CreateC(self): pass

        @abstractmethod
        def GetClassD(self): pass

    class ClassD:
        def __init__(self):
            self.ca = self.cb = self.cc = None

    class Builder(IBuilder):
        @classmethod
        def assemble(cls):
            cls.CreateA()

        def __init__(self):
            self.d = ClassD()

        def CreateA(self):
            self.d.ca = TestClassA()

        def CreateB(self):
            self.d.cb = TestClassB()

        def CreateC(self):
            self.d.cc = TestClassC()

        def GetClassD(self):
            return self.d

    class Director


if "__main__" == __name__:
    AbstractFactoryPattern()
