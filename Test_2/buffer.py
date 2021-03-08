# -*- coding: utf-8 -*-
"""
Реализация циклического буфера FIFO (first in first out) через collections.deque

(c) 2021 Куликов Никита, Санкт-Петербург, Россия
e-mail: pocketkurt@gmail.com
"""


class CycleBuffer(list):

    def __init__(self, size=5):
        self.size = size  # размер буфера, по умолчанию 5
        self.slots = size  # количество пустых мест в буфере

    # добавление объекта в буффер
    def append(self, value):
        # заполнение буфера через метод родительского класса если буфер был пуст
        if self.slots != 0:
            self.slots -= 1
            self += [value]
        # если буфер полон
        elif self.slots == 0:
            self = self[1:]
            self += [value]
            return self

    # получение объекта из буффера
    def pop(self):
        poped = self[0]
        self = self[1:]
        self.slots += 1
        return poped

    # пуст ли буффер
    def isEmpty(self):
        return self.slots == self.size

    def clear(self):
        self.slots = self.size
        del self[:]

    def __del__(self):
        del self


x = CycleBuffer()
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
