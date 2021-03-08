# -*- coding: utf-8 -*-
"""
Реализация циклического буфера FIFO (first in first out) через collections.deque

(c) 2021 Куликов Никита, Санкт-Петербург, Россия
e-mail: pocketkurt@gmail.com
"""

from collections import deque


class CycledBuffer:

    def __init__(self, size=5):
        self.__buffer = deque(maxlen=size)

    def __str__(self):
        return str(list(self.__buffer))

    def append(self, value):
        self.__buffer.append(value)

    def isEmpty(self):
        return not bool(self.__buffer)

    def clear(self):
        self.__buffer.clear()

    def pop(self):
        return self.__buffer.popleft()


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
