"""
Реализация циклического буфера FIFO (first in first out) через collections.deque

(c) 2021 Куликов Никита, Санкт-Петербург, Россия
e-mail: pocketkurt@gmail.com
"""
from collections import deque


class CycledBuffer(deque):

    def __init__(self, size=5):
        super(CycledBuffer, self).__init__(maxlen=size)
        self.size = self.maxlen
        self.slots = self.size

    def __str__(self):
        res = "["
        for i in range(len(self)):
            if i == 0:
                res += str(self[i])
            else:
                res += ", " + str(self[i])
        res += "]"
        return res

    def append(self, value):
        super(CycledBuffer, self).append(value)
        if self.slots != 0:
            self.slots -= 1

    def isEmpty(self):
        return len(self) == 0

    def clear(self):
        super(CycledBuffer, self).clear()
        self.slots = self.size

    def pop(self):
        self.slots += 1
        return super(CycledBuffer, self).popleft()
