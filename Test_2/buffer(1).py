# -*- coding: utf-8 -*-
"""
Реализация циклического буфера FIFO (first in first out) через collections.deque

(c) 2021 Куликов Никита, Санкт-Петербург, Россия
e-mail: pocketkurt@gmail.com
"""

from collections import deque


class CycledBuffer:

    def __init__(self, size=5):
        self.buf = deque(maxlen=size)
        self.slots = self.buf.maxlen

    def __str__(self):
        return str(list(self.buf))

    def append(self, value):
        self.buf.append(value)
        if self.slots != 0:
            self.slots -= 1

    def isEmpty(self):
        return not bool(self.buf)

    def clear(self):
        self.buf.clear()
        self.slots = self.buf.maxlen

    def pop(self):
        self.slots += 1
        return self.buf.popleft()


x = CycledBuffer()
x.append(1)
print(x)
x.append(2)
print(x)
x.append(3)
print(x)
x.append(4)
print(x)
x.append(5)
print(x)
x.append(6)
print(x)
print(x.pop())
print(x.isEmpty())
print(x)
print(x.clear())
print(x)