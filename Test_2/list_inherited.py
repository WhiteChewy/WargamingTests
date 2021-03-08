# -*- coding: utf-8-*-
"""
Реализация циклического буфера FIFO (first in first out) через list

(c) 2021 Куликов Никита, Санкт-Петербург, Россия
e-mail: pocketkurt@gmail.com
"""


class CycledBuffer(list):

    def __init__(self, size=5):
        super(CycledBuffer, self).__init__()
        self.__maxlen = size  # размер буфера, по умолчанию 5
        self.__slots = size  # количество пустых мест в буфере

    # сдвиг буфера "влево"
    def __shift(self):
        for index in range(self.__maxlen - self.__slots - 1):
            self[index] = self[index + 1]

    # добавление объекта в буффер
    def append(self, value):
        # заполнение буфера через метод родительского класса если буфер был пуст
        if self.__slots != 0:
            self.__slots -= 1
            super(CycledBuffer, self).append(value)
        # если буфер полон
        elif self.__slots == 0:
            self.__shift()
            super(CycledBuffer, self).pop()
            super(CycledBuffer, self).append(value)

    # пуст ли буффер
    def isEmpty(self):
        return self.__slots == self.__maxlen

    def clear(self):
        self.__slots = self.__maxlen
        del self[:]

    # получение объекта из буффера
    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty buffer.")
        item = self[0]
        self.__shift()
        super(CycledBuffer, self).pop()
        self.__slots += 1
        return item

    def getEmptySlots(self):
        return self.__slots

    def getMaxLen(self):
        return self.__maxlen
