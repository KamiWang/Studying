#!/usr/bin/env python
# 建造者模式

from abc import ABCMeta, abstractmethod


class Mainboard:
    def __init__(self, name):
        self.name = name


class CPU:
    def __init__(self, name):
        self.name = name


class Memory:
    def __init__(self, name):
        self.name = name


class HD:
    def __init__(self, name):
        self.name = name


class PC:
    def __init__(self):
        self.mainboard = self.CPU = self.memory = self.HD = None

    @property
    def is_complete(self):
        if self.mainboard and self.CPU and self.memory and self.HD:
            return True
        return False


class PCBuilder(metaclass=ABCMeta):
    @abstractmethod
    def InstallMainboard(self, PC, computer_parts): pass

    @abstractmethod
    def InstallCPU(self, PC, computer_parts): pass

    @abstractmethod
    def InstallMemory(self, PC, computer_parts): pass

    @abstractmethod
    def InstallHD(self, PC, computer_parts): pass


class Director:
    def assign_task(self, builder: PCBuilder, PC, computer_parts):
        builder.InstallMainboard(PC, computer_parts)
        builder.InstallCPU(PC, computer_parts)
        builder.InstallMemory(PC, computer_parts)
        builder.InstallHD(PC, computer_parts)


class ComputerWorker(PCBuilder):
    def InstallMainboard(self, PC, computer_parts):
        PC.mainboard = computer_parts[0]

    def InstallCPU(self, PC, computer_parts):
        PC.CPU = computer_parts[1]

    def InstallMemory(self, PC, computer_parts):
        PC.memory = computer_parts[2]

    def InstallHD(self, PC, computer_parts):
        PC.HD = computer_parts[3]


if "__main__" == __name__:
    apple_pc = PC()
    assembled_PC = PC()

    computer_parts1 = [Mainboard("苹果主板"), CPU(
        "苹果CPU"), Memory("苹果内存"), HD("苹果硬盘")]
    computer_parts2 = [Mainboard("华硕主板"), CPU(
        "intelCPU"), Memory("威刚内存"), None]

    Director().assign_task(ComputerWorker(), apple_pc, computer_parts1)
    Director().assign_task(ComputerWorker(), assembled_PC, computer_parts2)

    if apple_pc.is_complete:
        print("苹果电脑已完成")
    else:
        print("苹果电脑未完成")

    if assembled_PC.is_complete:
        print("组装电脑已完成")
    else:
        print("组装电脑未完成")
