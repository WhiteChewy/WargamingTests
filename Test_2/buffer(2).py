# -*- coding: utf-8 -*-
"""
Реализация циклического буфера FIFO (first in first out) через ABC Mutable Sequence

(c) 2021 Куликов Никита, Санкт-Петербург, Россия
e-mail: pocketkurt@gmail.com
"""
import collections


class CycledBuffer(collections.MutableSequence):

    def __shift(self):
        for index in range(self.size - self.slots-1):
            self.buff[index] = self.buff[index+1]

    def __init__(self, size=5):
        self.buff = []
        self.size = size
        self.slots = self.size

    def __delitem__(self):
        return self.buff.pop()

    def __getitem__(self, item):
        res = self.buff[0]
        CycledBuffer.__shift(self)
        self.buff.pop()
        self.slots += 1
        return res

    def __len__(self):
        return self.size

    def __setitem__(self, key, value):
        raise NotImplementedError("You can't change values inside the buffer.")

    def __str__(self):
        return str(self.buff)

    def insert(self, value):
        if self.slots != 0:
            self.buff.append(value)
            if self.slots != 0:
                self.slots -= 1
        else:
            CycledBuffer.__shift(self)
            self.buff[-1] = value

    def append(self, value):
        self.insert(value)

    def reverse(self):
        return self.buff.reverse()


x = CycledBuffer()
print(x)
x.insert(1)
print(x)
x.insert(2)
print(x)
x.insert(3)
print(x)
x.insert(4)
print(x)
x.insert(5)
print(x)
x.insert(6)
print(x)
x.insert(7)
print(x)
x.insert(8)
print(x)
x.append(8)
print(x)
x.extend([10, 11, 12])
print(x)
