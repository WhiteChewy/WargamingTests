# -*- coding: utf-8 -*-
"""
Реализация циклического буфера FIFO (first in first out) через ABC Mutable Sequence

(c) 2021 Куликов Никита, Санкт-Петербург, Россия
e-mail: pocketkurt@gmail.com
"""


class CycledBuffer(object):

    def __init__(self, size=5):
        self.__buffer = []
        self.__maxlen = size
        self.__slots = self.__maxlen

    def __str__(self):
        return str(self.__buffer)

    def __len__(self):
        return len(self.__buffer)

    def append(self, value):
        if self.__slots != 0:
            self.__buffer.append(value)
            if self.__slots != 0:
                self.__slots -= 1
        else:
            self.__buffer = self.__buffer[1:]
            self.__buffer.append(value)

    def isEmpty(self):
        return not bool(self.__buffer)

    def clear(self):
        self.__slots = self.__maxlen
        del self.__buffer[:]

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty buffer.")
        item = self.__buffer[0]
        self.__buffer = self.__buffer[1:]
        return item

    def getEmptySlots(self):
        return self.__maxlen - len(self.__buffer)

    def getMaxLen(self):
        return self.__maxlen
