# -*- coding: utf-8 -*-
"""
Реализация циклического буфера FIFO (first in first out) через collections.deque

(c) 2021 Куликов Никита, Санкт-Петербург, Россия
e-mail: pocketkurt@gmail.com
"""

from collections import deque


class CycledBuffer(object):

    def __init__(self, size=5):
        self.__buffer = deque(maxlen=size)

    def __str__(self):
        return str(list(self.__buffer))

    def __len__(self):
        return len(self.__buffer)

    def append(self, value):
        self.__buffer.append(value)

    def isEmpty(self):
        return not bool(self.__buffer)

    def clear(self):
        self.__buffer.clear()

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty buffer.")
        return self.__buffer.popleft()

    def getEmptySlots(self):
        return self.__buffer.maxlen - len(self.__buffer)

    def getMaxLen(self):
        return self.__buffer.maxlen
