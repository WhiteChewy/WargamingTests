"""
Реализация Пирамидаидальной сортировки.

НЕУСТОЙЧИВАЯ СОРТИРОВКА.

Лучшая верменная сложность - Ω(n*log(n))
Средняя временная сложность - Θ(n*log(n))
Худшая временная сложность - O(n*log(n))

Количество применяемой памяти - O(1)

(c) 2021 Kulikov Nikita, Saint-Petersburg, Russia
e-mail: pocketkurt@gmail.com
"""
# -*- coding: utf-8-*-


def heapify(array, heap_size, index):
    maximum = index
    left = (2*index) + 1
    right = (2*index) + 2
    if left < heap_size and array[left] > array[maximum]:
        maximum = left
    if right < heap_size and array[right] > array[maximum]:
        maximum = right
    if maximum != index:
        array[index], array[maximum] = array[maximum], array[index]
        heapify(array, heap_size, maximum)


def heap_sort(array):
    size = len(array)

    for i in range(size, -1, -1):
        heapify(array, size, i)
    for i in range(size-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
