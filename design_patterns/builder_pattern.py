#!/usr/bin/env python
# 建造者模式

from abc import ABCMeta, abstractmethod


class Mainboard:
    pass


class CPU:
    pass


class Memory:
    pass


class HD:
    pass


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
    def InstallMainboard(self): pass

    @abstractmethod
    def InstallCPU(self): pass

    @abstractmethod
    def InstallMemory(self): pass

    @abstractmethod
    def InstallHD(self): pass


class Director:
    def assign_task(self, builder, PC, computer_parts):
        builder.PC = PC
        builder.computer_parts = computer_parts
        builder.InstallMainboard()
        builder.InstallCPU()
        builder.InstallMemory()
        builder.InstallHD()


class ComputerWorker(PCBuilder):
    def __init__(self):
        self.PC = None
        self.computer_parts = []

    def InstallMainboard(self):
        self.PC.mainboard = self.computer_parts[0]

    def InstallCPU(self):
        self.PC.CPU = self.computer_parts[1]

    def InstallMemory(self):
        self.PC.memory = self.computer_parts[2]

    def InstallHD(self):
        self.PC.HD = self.computer_parts[3]


apple_pc = PC()
computer_parts = [Mainboard(), CPU(), Memory(), HD()]
Director().assign_task(ComputerWorker(), apple_pc, computer_parts)

if apple_pc.is_complete:
    print("电脑已经完成")
