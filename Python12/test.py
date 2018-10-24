#!/usr/bin/env python

class A:
    vv = 2
    def cc(self):
        print(2)


class B:
    vv = 3

    def cc(self):
        print(2)


a1 = B()

a2 = A()

a2 = a1

print(a1.vv)
print(B.vv)
print(a2.vv)
