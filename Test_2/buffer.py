"""
Реализация циклического буфера FIFO (first in first out) через list

(c) 2021 Куликов Никита, Санкт-Петербург, Россия
e-mail: pocketkurt@gmail.com
"""
# -*- coding: utf-8-*-


class CycleBuffer(list):

    def __init__(self, size=5):
        self.size = size  # размер буфера, по умолчанию 5
        self.slots = size  # количество пустых мест в буфере

    # сдвиг буфера "влево"
    def __shift(self):
        for index in range(self.size - self.slots - 1):
            self[index] = self[index+1]

    # добавление объекта в буффер
    def append(self, value):
        # заполнение буфера через метод родительского класса если буфер был пуст
        if self.slots != 0:
            self.slots -= 1
            super(CycleBuffer, self).append(value)
        # если буфер полон
        elif self.slots == 0:
            CycleBuffer.__shift(self)
            super(CycleBuffer, self).pop()
            super(CycleBuffer, self).append(value)

    # получение объекта из буффера
    def pop(self):
        poped = self[0]
        CycleBuffer.__shift(self)
        super(CycleBuffer, self).pop()
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
